from django.db import models
from django.contrib.auth.forms import UserChangeForm

# Create your models here.


class Article(models.Model):
    title = models.CharField()
    body = models.TextField()
    date = models.DateTimeField('date published')

    def __str__(self):
        return self.title

    class Meta:
        #for admin
        verbose_name = "Article"
        verbose_name_plural = "Articles"