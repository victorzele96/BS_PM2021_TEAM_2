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
from .models import StudentForm as StudentExtra
from .models import TeacherForm as TeacherExtra

from .models import Classroom
from .models import StudentClassroom
from .models import ClassSubject

from .models import Subject





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

            return render(request=request, template_name="school/register.html",
                          context={"form": form, "extra_form": teacher_form})

    form = TeacherUserForm()
    teacher_form = TeacherForm()
    return render(request=request, template_name="school/register.html",
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

            return render(request=request, template_name="school/registerStudent.html",
                          context={"form": form, "extra_form": student_form})  # , "p_reg_form": p_reg_form

    form = StudentUserForm()
    student_form = StudentForm()
    return render(request=request, template_name="school/registerStudent.html",
                  context={"form": form, "extra_form": student_form})  # , "p_reg_form": p_reg_form


def add_display_news(request):
    news = Article.objects.all().order_by('date')
    if request.method == "POST":
        article_form = ArticleForm(request.POST)

        if article_form.is_valid():
            article_form.date = datetime.now()
            article = article_form.save()

            messages.success(request, f"New article: {article} has been saved")
            # login(request, user)

            article_form = ArticleForm()
            return render(request, '../templates/school/news.html', {'news': news, "article_form": article_form})

        else:
            for msg in article_form.error_messages:
                messages.error(request, f"{msg}: {article_form.error_messages[msg]}")

            return render(request, '../templates/school/news.html', {'news': news, "article_form": article_form})

    article_form = ArticleForm()
    return render(request, '../templates/school/news.html', {'news': news, "article_form": article_form})


def delete_news(request, pk):
    article = Article.objects.get(id=pk)
    article.delete()
    return redirect('school_news')


def get_users(request):
    students = StudentExtra.objects.all()
    return render(request, '../templates/school/User_list.html', {'students': students})


def delete_student_from_school_view(request, pk):
    student = StudentExtra.objects.get(id=pk)
    user = User.objects.get(id=student.user_id)
    user.delete()
    student.delete()
    return redirect('user_details')


def student_update_from_school(request, pk):
    student = StudentExtra.objects.get(id=pk)
    user = User.objects.get(id=student.user_id)

    base_details = StudentUserForm(instance=user)
    extra_details = StudentForm(instance=student)
    details = {'base_details': base_details, 'extra_details': extra_details}

    if request.method == 'POST':
        base_details = StudentUserForm(request.POST, instance=user)
        extra_details = StudentForm(request.POST, instance=student)
        if (base_details.is_valid() and extra_details.is_valid()) or (base_details.is_valid()
                                                                      and extra_details.is_valid()
                                                                      and base_details.password1 is None
                                                                      and base_details.password2 is None):
            user = base_details.save()
            # user.set_password(user.password)
            user.save()
            extra = extra_details.save(commit=False)
            extra.save()
            return redirect('user_details')
        else:
            print("The user didn\'t changed !")
    return render(request, '../templates/school/student_update.html', context=details)


def student_update_from_student(request, pk):
    user = User.objects.get(id=pk)
    student = StudentExtra.objects.get(user_id=pk)

    base_details = StudentUserForm(instance=user)
    extra_details = StudentForm(instance=student)
    details = {'base_details': base_details, 'extra_details': extra_details}

    if request.method == 'POST':
        base_details = StudentUserForm(request.POST, instance=user)
        extra_details = StudentForm(request.POST, instance=student)
        if (base_details.is_valid() and extra_details.is_valid()) or (base_details.is_valid()
                                                                      and extra_details.is_valid()
                                                                      and base_details.password1 is None
                                                                      and base_details.password2 is None):
            user = base_details.save()
            # user.set_password(user.password)
            user.save()
            extra = extra_details.save(commit=False)
            extra.save()
            return redirect('studentHome')
        else:
            print("The user didn\'t changed !")
    return render(request, '../templates/school/student_update.html', context=details)


def teacher_details(request):
    teachers = TeacherExtra.objects.all()
    return render(request, '../templates/school/teacher_view.html', {'teachers': teachers})


def delete_teacher_from_school_view(request, pk):
    teacher = TeacherExtra.objects.get(id=pk)
    user = User.objects.get(id=teacher.user_id)
    user.delete()
    teacher.delete()
    return redirect('teacher_details')


def teacher_update_from_school(request, pk):
    teacher = TeacherExtra.objects.get(id=pk)
    user = User.objects.get(id=teacher.user_id)

    base_details = TeacherUserForm(instance=user)
    extra_details = TeacherForm(instance=teacher)
    details = {'base_details': base_details, 'extra_details': extra_details}

    if request.method == 'POST':
        base_details = TeacherUserForm(request.POST, instance=user)
        extra_details = TeacherForm(request.POST, instance=teacher)
        if (base_details.is_valid() and extra_details.is_valid()) or (base_details.is_valid()
                                                                      and extra_details.is_valid()
                                                                      and base_details.password1 is None
                                                                      and base_details.password2 is None):
            user = base_details.save()
            # user.set_password(user.password)
            user.save()
            extra = extra_details.save(commit=False)
            extra.save()
            return redirect('teacher_details')
        else:
            print("The user didn\'t changed !")
    return render(request, '../templates/school/teacher_update.html', context=details)


def teacher_update_from_teacher(request, pk):
    user = User.objects.get(id=pk)
    teacher = TeacherExtra.objects.get(user_id=pk)

    base_details = TeacherUserForm(instance=user)
    extra_details = TeacherForm(instance=teacher)
    details = {'base_details': base_details, 'extra_details': extra_details}

    if request.method == 'POST':
        base_details = TeacherUserForm(request.POST, instance=user)
        extra_details = TeacherForm(request.POST, instance=teacher)
        if (base_details.is_valid() and extra_details.is_valid()) or (base_details.is_valid()
                                                                      and extra_details.is_valid()
                                                                      and base_details.password1 is None
                                                                      and base_details.password2 is None):
            user = base_details.save()
            # user.set_password(user.password)
            user.save()
            extra = extra_details.save(commit=False)
            extra.save()
            return render(request, '../templates/teacher/teacherHome.html')# ----------------------------------logout when password change
        else:
            print("The user didn\'t changed !")
    return render(request, '../templates/school/teacher_update.html', context=details)

@staff_member_required
def del_user(request, username):
    try:
        u = User.objects.get(username=username)
        u.delete()
        messages.success(request, "The user is deleted")

    except User.DoesNotExist:
        messages.error(request, "User does not exist")
        return render(request, '../templates/school/schoolHome.html')

    except Exception as e:
        return render(request, '../templates/school/schoolHome.html', {'err': e.message})

    return redirect("get_users")


def view_class(request, pk):
    connection = StudentClassroom.objects.filter(class_room=pk)
    # users = User.objects.filter(id__criteria=connection.user)
    # user = User.objects.none()
    #
    obj = Classroom.objects.get(id=pk)

    list_of_ids = []
    for c in connection:
        # user = user | c.user
        list_of_ids.append(c.user.id)
        # list_of_ids.append(User.objects.get(id=c.user.id))
    user = User.objects.filter(id__in=list_of_ids)


    return render(request, '../templates/school/class/viewClass.html', {'user': user,'obj': obj})




############################################################################################
############################################################################################
############################################################################################

def Add_Student_To_Class(request):
    if request.method == "POST":
        form = StudentUserForm(request.POST)

        if form.is_valid():
            # form.date = datetime.now()
            new_connection = form.save()

            messages.success(request, f"New new_connection: {new_connection} has been saved")

            return redirect('view_class')

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request, '../templates/school/class/add_student_to_class.html', {"form": form})

    form = StudentUserForm()
    return render(request, '../templates/school/class/add_student_to_class.html', {"form": form})




def add_subject_to_class(request):
    if request.method == "POST":
        form = ClassSubjectForm(request.POST)

        if form.is_valid():
            # form.date = datetime.now()
            new_connection = form.save()

            messages.success(request, f"New new_connection: {new_connection} has been saved")

            return redirect('view_class')

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request, '../templates/school/class/add_subject_to_class.html', {"form": form})

    form = ClassSubjectForm()
    return render(request, '../templates/school/class/add_subject_to_class.html', {"form": form})





def view_class_list(request):
    model = Classroom.objects.all()
    return render(request, '../templates/school/class/view_class_list.html', {'model': model})




def View_Sched(request, pk):
    # model = ClassSubject.objects.get(subject=pk)

    subject_list = ClassSubject.objects.filter(subject=pk)

    connection = ClassSubject.objects.get(subject=pk)



    # connection = StudentClassroom.objects.filter(class_room=pk)
    # users = User.objects.filter(id__criteria=connection.user)
    # user = User.objects.none()
    #

    # list_of_ids = []
    # for c in connection:
    #     # user = user | c.user
    #     list_of_ids.append(c.user.id)
    #     # list_of_ids.append(User.objects.get(id=c.user.id))
    # user = User.objects.filter(id__in=list_of_ids)



    return render(request, '../templates/school/class/view_sched.html', {'subject_list': subject_list})

    list_of_ids = []
    for c in connection:
        # user = user | c.user
        list_of_ids.append(c.user.id)
        # list_of_ids.append(User.objects.get(id=c.user.id))
    user = User.objects.filter(id__in=list_of_ids)



    return render(request, '../templates/school/class/viewClass.html', {'user': user})






## create class room
# def my_test(request):
#     if request.method == 'POST':
#         form = ClassroomForm(request.POST)
#         if form.is_valid():
#             # form.teacher=User.objects.get(id=form.teacher)
#
#             obj = form.save(commit=False)
#             obj.save()
#             return redirect('/school')
#
#         else:
#             messages.error(request, "Invalid username or password.")
#             return render(request=request,
#                           template_name="../templates/school/MY_TEST.html",
#                           context={"form": form})
#     form = ClassroomForm()
#     return render(request=request,
#                   template_name="../templates/school/MY_TEST.html",
#                   context={"form": form})


def create_class(request):

    if request.method == "POST":
        form = ClassroomForm(request.POST)

        if form.is_valid():
            form.date = datetime.now()
            new_class = form.save()

            messages.success(request, f"New article: {new_class} has been saved")

            return redirect('view_class_list')

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request, '../templates/school/class/create_class.html', {"form": form})

    form = ClassroomForm()
    return render(request, '../templates/school/class/create_class.html', {"form": form})


def view_class_list(request):
    return render(request, '../templates/school/viewClass.html')


def create_class(request):
    return render(request, '../templates/school/viewClass.html')

##########################################################################################

# Staff Section
##########################################################################################
def teacherHome(request):
    return render(request, '../templates/teacher/teacherHome.html')

def add_exercise(request):
    return render(request, '../templates/teacher/addExercise.html')

def teacherSchedule(request):
    act_classes = Subject.objects.filter(teacher_id=request.user.id)
    # classroom = Classroom.objects.get()
    complex_model = ClassSubject.objects.none()
    for act_class in act_classes:
        complex_model = complex_model | ClassSubject.objects.filter(class_room_id=act_class.id)

    # model = ClassSubject.objects.filter(class_room__id=act_classes.all())
    return render(request, '../templates/teacher/teacherSchedule.html', {'model': complex_model})


def upload_file(request):
    if request.method == 'POST':
        form = File_Upload_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('teacherHome')
    else:
        form = TeacherFile()
    return render(request, '../templates/teacher/teacher_file_view.html', {
        'form': form
    })



# def upload_file(request):
#     upload_file_model
#     return render(request, '../templates/teacher/teacherSchedule.html', {'upload_file_model': upload_file_model})


##########################################################################################

# Student Section
##########################################################################################
def studentHome(request):
    return render(request, '../templates/student/studentHome.html')

def studentSchedule(request):

    class_connection = Subject.objects.get(user_id=request.user.id)
    # classroom = Classroom.objects.get()
    model = ClassSubject.objects.filter(id=class_connection.class_room.id)
    return render(request, '../templates/teacher/teacherSchedule.html', {'model': model})


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



## here just to tests

## create class room
# def my_test(request):
#     if request.method == 'POST':
#         form = ClassroomForm(request.POST)
#         if form.is_valid():
#             # form.teacher=User.objects.get(id=form.teacher)
#
#             obj = form.save(commit=False)
#             obj.save()
#             return redirect('/school')
#
#         else:
#             messages.error(request, "Invalid username or password.")
#             return render(request=request,
#                           template_name="../templates/school/MY_TEST.html",
#                           context={"form": form})
#     form = ClassroomForm()
#     return render(request=request,
#                   template_name="../templates/school/MY_TEST.html",
#                   context={"form": form})

### conect student to class
# def my_test(request):
#     if request.method == 'POST':
#         form = StudentClassroomForm(request.POST)
#         if form.is_valid():
#             # form.teacher=User.objects.get(id=form.teacher)
#
#             obj = form.save(commit=False)
#             obj.save()
#             return redirect('/school')
#
#         else:
#             messages.error(request, "Invalid username or password.")
#             return render(request=request,
#                           template_name="../templates/school/MY_TEST.html",
#                           context={"form": form})
#     form = StudentClassroomForm()
#     return render(request=request,
#                   template_name="../templates/school/MY_TEST.html",
#                   context={"form": form})

#
# ### subject test
#
# def my_test(request):
#     if request.method == 'POST':
#         form = SubjectForm(request.POST)
#         if form.is_valid():
#             # form.teacher=User.objects.get(id=form.teacher)
#
#             obj = form.save(commit=False)
#             obj.save()
#             return redirect('/school')
#
#         else:
#             messages.error(request, "Invalid username or password.")
#             return render(request=request,
#                           template_name="../templates/school/MY_TEST.html",
#                           context={"form": form})
#     form = SubjectForm()
#     return render(request=request,
#                   template_name="../templates/school/MY_TEST.html",
#                   context={"form": form})



### subject test

def my_test(request):
    if request.method == 'POST':
        form = ClassSubjectForm(request.POST)
        if form.is_valid():
            # form.teacher=User.objects.get(id=form.teacher)

            obj = form.save(commit=False)
            obj.save()
            return redirect('/school')

        else:
            messages.error(request, "Invalid username or password.")
            return render(request=request,
                          template_name="../templates/school/MY_TEST.html",
                          context={"form": form})
    form = ClassSubjectForm()
    return render(request=request,
                  template_name="../templates/school/MY_TEST.html",
                  context={"form": form})