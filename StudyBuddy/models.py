from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    class Meta:
        #for admin
        verbose_name = "Article"
        verbose_name_plural = "Articles"



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    Class = models.CharField("Class", max_length=50, blank=True)
    birth_date = models.DateField("Birth Date", blank=True)
    ID_TZ = models.IntegerField(default=None, blank=True)
    Personal_Phone = models.CharField("Personal Phone", max_length=10, blank=True)

    Parent_1_first_name = models.CharField("Parent_1_first_name", max_length=50, blank=True)
    Parent_1_Phone = models.CharField("Parent_1_Phone", max_length=10, blank=True)

    Parent_2_first_name = models.CharField("Parent_2_first_name", max_length=50, blank=True)
    Parent_2_Phone = models.CharField("Parent_2_Phone", max_length=10, blank=True)


    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)