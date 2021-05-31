from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.forms import UserChangeForm
from datetime import date, datetime




# import myFields

# Create your models here.


# DAYS_OF_WEEK = (
#     (0, 'Sunday'),
#     (1, 'Monday'),
#     (2, 'Tuesday'),
#     (3, 'Wednesday'),
#     (4, 'Thursday'),
#     (5, 'Friday'),
#     (6, 'Saturday'),
#
# )

# DAYS_OF_WEEK = (
#     ('Sunday', 0),
#     ('Monday', 1),
#     ('Tuesday', 2),
#     ('Wednesday', 3),
#     ('Thursday', 4),
#     ('Friday', 5),
#     ('Saturday', 6),
#
# )

DAYS_OF_WEEK = (
    ('Sunday', 0),
    ('Monday', 1),
    ('Tuesday', 2),
    ('Wednesday', 3),
    ('Thursday', 4),
    ('Friday', 5),
    ('Saturday', 6),

)


class Article(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    date = models.DateTimeField('date published')

    def str(self):
        return self.title

    class Meta:
        # for admin
        verbose_name = "Article"
        verbose_name_plural = "Articles"


class TeacherForm(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phone = models.CharField("phone", max_length=10)
    subjects = models.CharField("subjects", max_length=80)
    theme = models.IntegerField(default=0)

    def str(self):
        return f'{self.user.username} Teacher'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class StudentForm(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    grade = models.CharField("grade", max_length=50)
    birth_date = models.DateField("Birth Date", blank=True)
    personalPhone = models.CharField("Personal Phone", max_length=10, blank=True)

    parentName_M = models.CharField("mother name", max_length=20)  # mother = _M
    parentPhone_M = models.CharField("mother phone", max_length=10)

    parentName_F = models.CharField("father name", max_length=20, blank=True)
    parentPhone_F = models.CharField("father phone", max_length=10, blank=True)

    theme = models.IntegerField(default=0)

    def str(self):
        return f'{self.user.username} Student'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Classroom(models.Model):
    class_name = models.CharField("class name", max_length=50)
    teacher = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def str(self):
        return self.class_name

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"

    def save(self, *args, **kwargs):
        # if self.teacher.is_staff:
        # print("self.user = " + self.teacher)
        if User.objects.get(id=self.teacher.id).is_staff:
            super().save(*args, **kwargs)
        else:
            raise ValueError("user must be staff member")


class StudentClassroom(models.Model):
    class_room = models.ForeignKey(Classroom, null=True, on_delete=models.CASCADE)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def str(self):
        return self.class_room

    def save(self, *args, **kwargs):
        # print("---->>>>>   "+self.objects.get(user_id=self.user.id))
        # if not StudentClassroom.objects.get(user_id=self.user.id):
        # if not self.objects.get(user_id=self.user.id):
        if not User.objects.get(id=self.user.id).is_staff:
            super().save(*args, **kwargs)
        else:
            raise ValueError("user must be a student")
        # else:
        #     raise ValueError("student already connected to the class ")
        # if not self.user.is_staff:
        #     super().save(*args, **kwargs)
        # else:
        #     raise ValueError("user must be a student")


class Subject(models.Model):
    subject_name = models.CharField("subject name", max_length=50)
    teacher = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    # test = models.TimeField
    duration = models.IntegerField(null=True, validators=[MaxValueValidator(4), MinValueValidator(1)])  # review.models

    def str(self):
        return self.subject_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class ClassSubject(models.Model):
    # subject = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
    subject = models.OneToOneField(Subject, null=True, on_delete=models.CASCADE)
    # class_room = models.OneToOneField(Classroom, null=True, on_delete=models.CASCADE)
    class_room = models.ForeignKey(Classroom, null=True, on_delete=models.CASCADE)
    # day = myFields.DayOfTheWeekField()
    # days = models.CharField(max_length=9, choices=DAYS_OF_WEEK)
    days = models.CharField(max_length=9)
    start_time = models.TimeField()
    end_time = models.TimeField(null=True)
    meeting = models.URLField(max_length=200, null=True)

    def str(self):
        return self.class_room + ' -> ' + self.subject

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    # class Meta:
    #     # for admin
    #     verbose_name = "Student connection to Class "
    #     verbose_name_plural = "Classes"


class TeacherFile(models.Model):
    subject = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)

    name = models.CharField(max_length=256)
    description = models.TextField(null=True)
    file = models.FileField(upload_to='books/')
    upload_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    question = models.TextField()

    a = models.TextField()
    b = models.TextField()
    c = models.TextField()
    d = models.TextField()

    ans = models.CharField(max_length=1)

    def str(self):
        return self.question


class Subject_Exam(models.Model):
    subject = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
    exercise = models.OneToOneField(Exercise, null=True, on_delete=models.CASCADE)

    description = models.TextField(null=True)

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def duration(self):
        return self.end_time - self.start_time

    def time_left(self):
        return self.end_time - datetime.now()

    def get_qws_amount(self):
        return Subject_Exam.objects.filter(subject=self.subject).count()


class Subject_Exercise(models.Model):
    subject = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
    exercise = models.OneToOneField(Exercise, null=True, on_delete=models.CASCADE)

    description = models.TextField(null=True)

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def duration(self):
        return self.end_time - self.start_time

    def time_left(self):
        return self.end_time - datetime.now()

    def get_qws_amount(self):
        return Subject_Exercise.objects.filter(subject=self.subject).count()


class Private_Chat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    # receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    # receiver = models.OneToOneField(User, on_delete=models.CASCADE)
    receiver_id = models.IntegerField()# integer witch represents user id
    msg = models.TextField()
    publish_date = models.DateTimeField('date published')

    def str(self):
        return self.msg


class Class_Chat(models.Model):
    sender = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    receiver_class = models.ForeignKey(Classroom, null=True, on_delete=models.CASCADE)
    msg = models.TextField()
    publish_date = models.DateTimeField('date published')

    def str(self):
        return self.msg