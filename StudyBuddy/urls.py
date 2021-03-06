from django.urls import path

from django.conf.urls import url
from django.urls import path, include
from django.views.generic import ListView, DetailView

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
    path("school/news/", views.add_display_news, name="school_news"),
    path("school/delete_news/<int:pk>", views.delete_news, name='delete_news'),
    path("school/user_details/", views.get_users, name="user_details"),
    path("delete-student-from-school/<int:pk>", views.delete_student_from_school_view,name='delete-student-from-school'),
    path("school/student_update/<int:pk>", views.student_update_from_school, name="student_update_from_school"),
    path("school/teacher_details/", views.teacher_details, name="teacher_details"),
    path("delete-teacher-from-school/<int:pk>", views.delete_teacher_from_school_view,name='delete-teacher-from-school'),
    path("school/teacher_update_from_school/<int:pk>", views.teacher_update_from_school,name="teacher_update_from_school"),


    path("school/classes", views.view_class_list, name="view_class_list"),
    path("school/classes/create_class", views.create_class, name="create_class"),
    path("school/classes/class/<int:pk>", views.view_class, name="view_class"),
    # path("school/classes/class/view_class_schedule", views.view_class_schedule, name="view_class_schedule"),
    # path("school/classes/class/create_class_schedule", views.create_class_schedule, name="create_class_schedule"),
    path("school/classes/class/Add_Student_To_Class", views.Add_Student_To_Class, name="Add_Student_To_Class"),
    path("school/classes/class/View_Sched/<int:pk>", views.View_Sched, name="View_Sched"),
    path("school/classes/class/add_subject_to_class", views.add_subject_to_class, name="add_subject_to_class"),




    path("school/my_test", views.my_test, name="my_test"),  # here just for test


    path("school/view_class/", views.view_class, name="view_class"),
    # url(r'^school/user_details/(?P<username>[\w|\W.-]+)/$', views.del_user, name='del_user'),

    # Teacher
    path("teacher/", views.teacherHome, name="teacherHome"),
    path("teacher/add-exercise", views.add_exercise, name="add_exercise"),
    path("teacher/teacher_update/<int:pk>", views.teacher_update_from_teacher,
         name="teacher_update_from_teacher"),
    path("teacher/teacherSchedule", views.teacherSchedule, name="teacherSchedule"),
    path("teacher/upload_file", views.upload_file, name="upload_file"),




    # Student
    path("student/", views.studentHome, name="studentHome"),
    path("student/student_update/<int:pk>", views.student_update_from_student,
         name="student_update_from_student"),
    path("student/studentSchedule", views.studentSchedule, name="studentSchedule"),


]
