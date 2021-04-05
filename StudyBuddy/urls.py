from django.urls import path

from django.conf.urls import url
from django.urls import path,include
from django.views.generic import ListView,DetailView

from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    url(r'^$', views.home, name='home'),

    path("register_teacher/", views.register_teacher, name="register_teacher"),
    path("register_student/", views.register_student, name="register_student"),
    path("login/", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
]