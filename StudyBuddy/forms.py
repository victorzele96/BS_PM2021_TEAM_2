from django.forms import ModelForm,TextInput
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

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['Class', 'birth_date']

class TeacherUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

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
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(StudentUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.is_staff = False
            user.save()
        return user