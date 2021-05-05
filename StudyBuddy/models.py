from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


# Create your models here.


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

    def __str__(self):
        return f'{self.user.username} Student'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

# class ConnStudentUser(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     studentUser = models.ForeignKey(StudentForm, on_delete=models.CASCADE)
#
# class ConnTeacherUser(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     teacherUser = models.ForeignKey(TeacherForm, on_delete=models.CASCADE)
