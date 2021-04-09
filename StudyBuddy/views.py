from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import *

def home(request):
    return render(request, '../templates/home.html')

def adminHome(request):
    return render(request, '../templates/admin/adminHome.html')

def teacherHome(request):
    return render(request, '../templates/teacher/teacherHome.html')

def studentHome(request):
    return render(request, '../templates/student/studentHome.html')



def register_teacher(request):
    if request.method == "POST":
        form = TeacherUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("home")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request=request,
                          template_name="register.html",
                          context={"form":form})

    form = TeacherUserForm
    return render(request = request,
                  template_name="register.html",
                  context={"form":form})


def register_student(request):
    if request.method == "POST":
        form = StudentUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("home")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request = request,
                          template_name="register.html",
                          context={"form":form})

    form = TeacherUserForm
    return render(request = request,
                  template_name="register.html",
                  context={"form":form})




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
                    return redirect('/admin')
                if request.user.is_staff:
                    return redirect('/teacher')
                return redirect('/student')

            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,
                  template_name="login.html",
                  context={"form": form})
