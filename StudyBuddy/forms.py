from django.forms import ModelForm, TextInput
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.db.models.functions import Now
from datetime import date, datetime


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body']

    def save(self, commit=True):
        article = super(ArticleForm, self).save(commit=False)

        if commit:
            article.date = datetime.now()
            article.save()
        return


class TeacherForm(forms.ModelForm):
    class Meta:
        model = TeacherForm
        fields = ('phone', 'subjects')


class StudentForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={
        "class": "input",
        "type": "date",
        "placeholder": "YYYY-MM-DD"
    }))
    class Meta:
        model = StudentForm
        fields = ('grade', 'birth_date', 'personalPhone', 'parentName_M', 'parentPhone_M', 'parentName_F',
                  'parentPhone_F')


class TeacherUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(TeacherUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.is_staff = True
            user.save()
        return user


class StudentUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(StudentUserForm, self).save(commit=False)  # create user in auth table
        user.email = self.cleaned_data["email"]
        if commit:
            user.is_staff = False
            user.save()
        return user
