from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.forms import UserChangeForm

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

    # FOR TEST PURPOSES ONLY  #
    def getTitle(self):       #
        return self.title     #
                              #
    def getBody(self):        #
        return self.body      #
                              #
    def getDate(self):        #
        return self.date      #
                              #
    def setTitle(self, title):#
        self.title = title    #
                              #
    def setBody(self, body):  #
        self.body = body      #
                              #
    def setDate(self, date):  #
        self.date = date      #
    # FOR TEST PURPOSES ONLY  #

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

    def str(self):
        return self.class_room + ' -> ' + self.subject

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    # class Meta:
    #     # for admin
    #     verbose_name = "Student connection to Class "
    #     verbose_name_plural = "Classes"