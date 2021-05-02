from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date, datetime

from .forms import *
from .models import Article




# Home Section
def home(request):
    print(request.user.username)
    print(request.user.id)

    # currentProfile = Profile.objects.get(user_id = request.user.id)
    news = Article.objects.all().order_by('-date')
    # return render(request, '../templates/home.html',{'news': news, 'currentProfile': currentProfile})
    return render(request, '../templates/home.html', {'news': news})


# School Section
##########################################################################################
def schoolHome(request):
    return render(request, '../templates/school/schoolHome.html')

def register_teacher(request):
    if request.method == "POST":
        form = TeacherUserForm(request.POST)
        teacher_form = TeacherForm(request.POST)
        if form.is_valid() and teacher_form.is_valid():
            user = form.save()
            user.refresh_from_db()
            username = form.cleaned_data.get('username')

            teacher_form = TeacherForm(request.POST)
            teacher_form.full_clean()
            teacher = teacher_form.save(commit=False)
            teacher.user = user

            teacher.save()

            messages.success(request, f"New account created: {username}")
            return redirect("home")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request=request,template_name="school/register.html",
                          context={"form": form, "extra_form": teacher_form})

    form = TeacherUserForm()
    teacher_form = TeacherForm()
    return render(request=request,template_name="school/register.html",
                  context={"form": form, "extra_form": teacher_form})


def register_student(request):
    if request.method == "POST":
        form = StudentUserForm(request.POST)
        student_form = StudentForm(request.POST)
        if form.is_valid() and student_form.is_valid():
            user = form.save()
            user.refresh_from_db()
            username = form.cleaned_data.get('username')

            student_form = StudentForm(request.POST)
            student_form.full_clean()
            student = student_form.save(commit=False)
            student.user = user

            student.save()

            messages.success(request, f"New account created: {username}")
            return redirect("home")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request=request,template_name="school/register.html",
                          context={"form": form, "extra_form": student_form}) #, "p_reg_form": p_reg_form

    form = StudentUserForm()
    student_form = StudentForm()
    return render(request=request,template_name="school/register.html",
                  context={"form": form, "extra_form": student_form})  #, "p_reg_form": p_reg_form


def add_display_news(request):
    news = Article.objects.all().order_by('date')
    if request.method == "POST":
        article_form = ArticleForm(request.POST)

        if article_form.is_valid():
            article_form.date=datetime.now()
            article = article_form.save()

            messages.success(request, f"New article: {article} has been saved")
            # login(request, user)

            article_form = ArticleForm()
            return render(request, '../templates/school/news.html', {'news': news, "article_form": article_form})

        else:
            for msg in article_form.error_messages:
                messages.error(request, f"{msg}: {article_form.error_messages[msg]}")

            return render(request, '../templates/school/news.html', {'news': news, "article_form": article_form})

    article_form=ArticleForm()
    return render(request, '../templates/school/news.html', {'news': news, "article_form": article_form})


def get_users(request):
    users = User.objects.all()
    return render(request, '../templates/school/User_list.html', {'users': users})


@staff_member_required
def del_user(request, username):
    try:
        u = User.objects.get(username = username)
        u.delete()
        messages.success(request, "The user is deleted")

    except User.DoesNotExist:
        messages.error(request, "User doesnot exist")
        return render(request, '../templates/school/schoolHome.html')

    except Exception as e:
        return render(request, '../templates/school/schoolHome.html',{'err':e.message})

    return redirect("get_users")
##########################################################################################

# Staff Section
##########################################################################################
def teacherHome(request):
    return render(request, '../templates/teacher/teacherHome.html')
##########################################################################################

# Student Section
##########################################################################################
def studentHome(request):
    return render(request, '../templates/student/studentHome.html')
##########################################################################################


# Other Section
##########################################################################################
@login_required
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("home")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")

                if request.user.is_superuser:
                    return redirect('/school')
                if request.user.is_staff:
                    return redirect('/teacher')
                return redirect('/student')

            else:
                messages.error(request, "Invalid username or password.")
                return render(request=request,
                              template_name="login.html",
                              context={"form": form})
        else:
            messages.error(request, "Invalid username or password.")
            return render(request=request,
                          template_name="login.html",
                          context={"form": form})
    form = AuthenticationForm()
    return render(request=request,
                  template_name="login.html",
                  context={"form": form})
##########################################################################################
# def updateTheme(request):
#     user = request.user
#
#     if user.AuthenticationMiddleware:
#         print(user.theme)
#     else:
#         print("Hello Nice Guest")