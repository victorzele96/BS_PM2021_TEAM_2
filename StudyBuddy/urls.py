from django.urls import path

from django.conf.urls import url
from django.urls import path,include
from django.views.generic import ListView,DetailView

from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    # url(r'^$', views.home, name='home'),


    # Home
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path("login/", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),

    # School
    path("school/", views.schoolHome, name="schoolHome"),
    path("school/register_teacher/", views.register_teacher, name="register_teacher"),
    path("school/register_student/", views.register_student, name="register_student"),



    # Teacher
    path("teacher/", views.teacherHome, name="teacherHome"),



    # Student
    path("student/", views.studentHome, name="studentHome"),

]