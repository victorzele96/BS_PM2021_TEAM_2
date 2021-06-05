from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.conf import settings
import os


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
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
            return render(request,
                          '../templates/teacher/teacherHome.html')  # ----------------------------------logout when password change
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

    return render(request, '../templates/school/class/viewClass.html', {'user': user, 'obj': obj})


############################################################################################
############################################################################################
############################################################################################

def Add_Student_To_Class(request):
    if request.method == "POST":
        form = StudentClassroomForm(request.POST)

        if form.is_valid():
            # form.date = datetime.now()
            new_connection = form.save()

            messages.success(request, f"New new_connection: {new_connection} has been saved")

            return redirect('view_class', new_connection.class_room.id)

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            return render(request, '../templates/school/class/add_student_to_class.html', {"form": form})

    form = StudentClassroomForm()
    return render(request, '../templates/school/class/add_student_to_class.html', {"form": form})


def add_subject_to_class(request):
    if request.method == "POST":
        form = ClassSubjectForm(request.POST)

        if form.is_valid():
            # form.date = datetime.now()
            new_connection = form.save()

            messages.success(request, f"New new_connection: {new_connection} has been saved")

            return redirect('view_class', new_connection.class_room.id)

        else:
            # for msg in form.error_messages:
            #     messages.error(request, f"{msg}: {form.error_messages[msg]}")

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

    # list_of_ids = []
    # for c in connection:
    #     # user = user | c.user
    #     list_of_ids.append(c.user.id)
    #     # list_of_ids.append(User.objects.get(id=c.user.id))
    # user = User.objects.filter(id__in=list_of_ids)
    #
    # return render(request, '../templates/school/class/viewClass.html', {'user': user})


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
    classroom = Classroom.objects.all()
    teacher_list = []
    for cr in classroom:
        teacher_list.append(User.objects.get(id=cr.teacher_id))
    other_teacher_list_temp = User.objects.filter(is_staff=True) & User.objects.filter(is_superuser=False)
    other_teacher_list=[u for u in other_teacher_list_temp]

    if teacher_list != other_teacher_list:
        if request.method == "POST":
            form = ClassroomForm(request.POST)
            if form.is_valid():
                new_class = form.save(commit=False)
                new_class.save()
                messages.success(request, f"New article: {new_class} has been saved")
                return redirect('view_class_list')
            else:
                for msg in form.error_messages:
                    messages.error(request, f"{msg}: {form.error_messages[msg]}")
                return render(request, '../templates/school/class/create_class.html', {"form": form})
        form = ClassroomForm()
        return render(request, '../templates/school/class/create_class.html', {"form": form})
    else:
        return HttpResponse("No teacher to add !!!!!!!!!!")




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


##########################################################################################

# Staff Section
##########################################################################################
def teacherHome(request):
    return render(request, '../templates/teacher/teacherHome.html')


def add_exercise(request):
    return render(request, '../templates/teacher/addExercise.html')

def t_my_class(request):
    # class_id = StudentClassroom.objects.get(user_id=request.user.id).class_room.id
    classroom = Classroom.objects.get(teacher_id=request.user.id)
    students_ids = StudentClassroom.objects.filter(class_room_id=classroom.id)

    list_of_ids = []
    for s in students_ids:
        if s.user.id != request.user.id:
            list_of_ids.append(s.user.id)
    user = User.objects.filter(id__in=list_of_ids)

    class_chat= Class_Chat.objects.filter(receiver_class_id=classroom.id)

    return render(request, '../templates/student/my_class/my_class.html', {'classroom': classroom, 'users': user, 'class_chat': class_chat})




def teacher_add_exercise(request, pk):
    # here we will add func off exercise data
    form = ExerciseForm(request.POST)
    if form.is_valid():
        obj = form.save()
        # task = Task.objects.get(id=pk)

        new_task = Task_Exercises(task_id=pk ,exercise_id=obj.id)
        # print(task)
        # task.exercise_id = obj.id
        # task.save()
        # new_task = Subject_Exercise(subject=task.subject,
        #                             description=task.description,
        #                             start_time=task.start_time,
        #                             end_time=task.end_time)
        new_task.save()
        # pk = new_task.subject_id
        return redirect('teacher_exercise_view', pk)
    else:
        return HttpResponse('you are loser !!! try again')

    # return redirect('teacher_exercise_view', pk)
    #
    #
    #
    # print(request.POST)
    # print(pk)
    # return render(request, '../templates/teacher/teacher_exercise_view.html')


def teacher_add_task(request, pk):
    # form = SubjectExerciseForm()
    form = TaskForm(request.POST)
    if form.is_valid():
        # print(request.POST['description'])
        new_task = Task(subject=Subject.objects.get(id=pk),
                                name=request.POST['name'],
                               description=request.POST['description'],
                               start_time=request.POST['start_time'],
                               end_time=request.POST['end_time'])
        new_task.save()
        return redirect('teacher_task_view', pk)

    else:
        return HttpResponse('you are loser !!! try again')
        # return HttpResponse(form.start_time.errors)

    # subject = models.ForeignKey(Subject, null=True, on_delete=models.CASCADE)
    # exercise = models.OneToOneField(Exercise, null=True, on_delete=models.CASCADE)
    #
    # description = models.TextField(null=True)
    #
    # start_time = models.DateTimeField()
    # end_time = models.DateTimeField()



def teacher_exercise_view(request, pk):
    ex = Task_Exercises.objects.filter(task_id=pk)
    # print("---->  ", my_subject)
    list_of_ids = []
    for s in ex:
        list_of_ids.append(s.exercise_id)

    # print("---->  " , list_of_ids)
    ex = Exercise.objects.filter(id__in=list_of_ids)
    ret_pk = pk
    return render(request, '../templates/teacher/teacher_exercise_view.html', {'model': ex, 'ret_pk': ret_pk})



# def teacher_exercise_view(request, pk):
#     my_subject = Subject_Exercise.objects.filter(subject_id=pk)
#     # print("---->  ", my_subject)
#     list_of_ids = []
#     for s in my_subject:
#         # user = user | c.user
#         list_of_ids.append(s.exercise_id)
#         # list_of_ids.append(User.objects.get(id=c.user.id))
#     # print("---->  " , list_of_ids)
#     ex = Exercise.objects.filter(id__in=list_of_ids)
#     ret_pk = pk
#     return render(request, '../templates/teacher/teacher_exercise_view.html', {'model': ex, 'ret_pk': ret_pk})


def teacher_task_view(request, pk):
    # tasks = Subject_Exercise.objects.filter(subject_id=pk).first()
    tasks = Task.objects.filter(subject_id=pk)

    ret_pk = pk
    return render(request, '../templates/teacher/teacher_task_view.html', {'model_2': tasks, 'ret_pk': ret_pk})

def teacherSchedule(request):
    act_classes = Subject.objects.filter(teacher_id=request.user.id)
    # classroom = Classroom.objects.get()
    complex_model = ClassSubject.objects.none()
    for act_class in act_classes:
        complex_model = complex_model | ClassSubject.objects.filter(class_room_id=act_class.id)

    # model = ClassSubject.objects.filter(class_room__id=act_classes.all())
    return render(request, '../templates/teacher/teacherSchedule.html', {'model': complex_model})


def view_t_classes(request):
    main_class = Classroom.objects.filter(teacher=request.user)
    my_subjects = Subject.objects.filter(teacher=request.user)

    return render(request, '../templates/teacher/view_classes.html', {'model': main_class, "model_2": my_subjects})


# def upload_file(request, pk):
#     if request.method == 'POST':
#         form = File_Upload_Form(request.POST, request.FILES)
#         print("------------------                     TEST     upload_file     -----  ID :"+str(pk))
#         # form.subject = Subject.objects.get(id=pk).id
#         form.subject = Subject.objects.get(id=pk)
#         # print(form.subject)
#         if form.is_valid():
#             # form.subject = Subject.objects.get(id=pk)
#
#             print("------------------                     TEST     upload_file          -----------------------------")
#             form.save()
#             return redirect('view_t_classes')
#         else:
#             print(form.errors)
#             # for msg in form.error_messages:
#             #     messages.error(request, f"{msg}: {form.error_messages[msg]}")
#             return render(request, '../templates/teacher/upload_file.html', {'form': form})
#
#
#     form = File_Upload_Form()
#     form.subject = Subject.objects.get(id=pk)
#     return render(request, '../templates/teacher/upload_file.html', {
#         'form': form
#     })


def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload_file(request, pk):
    if request.method == 'POST':
        # print(request.POST)
        # print(request.FILES)
        # form = FileUploadForm(request.POST)
        form = File_Upload_Form(request.POST, request.FILES)
        # form.file=request.POST['file']
        # print("------------------                     TEST     upload_file     -----  ID :"+str(pk))
        # form.subject = Subject.objects.get(id=pk).id
        # form.subject = Subject.objects.get(id=pk)
        # print(type(request.POST['file']))
        if form.is_valid():
            # newFile=TeacherFile(subject=Subject.objects.get(id=pk), name="TEST", description="Fuck off", file=request.FILES['file'])
            newFile = TeacherFile(subject=Subject.objects.get(id=pk), name=request.POST['name'],
                                  description=request.POST['description'], file=request.FILES['file'])
            newFile.save()
            # print("------------------            YES   YES   YES   -------------------")
            return redirect('view_t_classes')
        else:
            print(form.errors)
            # for msg in form.error_messages:
            #     messages.error(request, f"{msg}: {form.error_messages[msg]}")
            return render(request, '../templates/teacher/upload_file.html', {'form': form, 'ret_pk': pk})

    form = File_Upload_Form()
    # form.subject = Subject.objects.get(id=pk)
    return render(request, '../templates/teacher/upload_file.html', {
        'form': form, 'ret_pk': pk
    })


def teacher_file_view(request, pk):
    model = TeacherFile.objects.filter(subject_id=pk)
    # ret_pk = Subject.objects.get(id=pk)
    ret_pk = pk
    return render(request, '../templates/teacher/teacher_file_view.html', {
        'model': model, 'ret_pk': ret_pk
    })




# def upload_file(request):
#     upload_file_model
#     return render(request, '../templates/teacher/teacherSchedule.html', {'upload_file_model': upload_file_model})


##########################################################################################

# Student Section
##########################################################################################
def studentHome(request):
    student_class = StudentClassroom.objects.get(user_id=request.user.id)
    all_students_in_class = StudentClassroom.objects.filter(class_room_id=student_class.class_room.id)

    birthdays = []
    for student in all_students_in_class:
        std = StudentExtra.objects.get(user_id=student.user.id)
        if std.birth_date.day == datetime.today().day and std.birth_date.month == datetime.today().month:
            birthdays.append(std.birth_date.strftime('%x') + " " + std.user.first_name + " " + std.user.last_name)

    print(birthdays)

    return render(request, '../templates/student/studentHome.html', {'birthdays': birthdays})


# import datetime

def studentSchedule(request):
    import datetime
    # class_connection = Subject.objects.get(user_id=request.user.id)
    class_connection = StudentClassroom.objects.get(user_id=request.user.id)

    time = ['08:00 AM', '09:00 AM', '10:00 AM', '11:00 AM', '12:00 AM',
            '13:00 AM', '14:00 AM', '15:00 AM', '16:00 AM']
    days = [1, 2, 3, 4, 5, 6]

    # classroom = Classroom.objects.get()
    model = ClassSubject.objects.filter(class_room_id=class_connection.class_room.id)

    # arr[time.len()][days.len()][]

    # obj_dic = {1: [], 2: [], 3: [], 4: [], 5: []}
    obj_dic = {1: {datetime.time(8,0,0): None,
                   datetime.time(9,0,0): None,
                   datetime.time(10,0,0): None,
                   datetime.time(11,0,0): None,
                   datetime.time(12,0,0): None,
                   datetime.time(13,0,0): None,
                   datetime.time(14,0,0): None,
                   datetime.time(15,0,0): None,
                   datetime.time(16,0,0): None},
               2: {datetime.time(8,0,0): None,
                   datetime.time(9,0,0): None,
                   datetime.time(10,0,0): None,
                   datetime.time(11,0,0): None,
                   datetime.time(12,0,0): None,
                   datetime.time(13,0,0): None,
                   datetime.time(14,0,0): None,
                   datetime.time(15,0,0): None,
                   datetime.time(16,0,0): None},
               3: {datetime.time(8, 0, 0): None,
                   datetime.time(9, 0, 0): None,
                   datetime.time(10, 0, 0): None,
                   datetime.time(11, 0, 0): None,
                   datetime.time(12, 0, 0): None,
                   datetime.time(13, 0, 0): None,
                   datetime.time(14, 0, 0): None,
                   datetime.time(15, 0, 0): None,
                   datetime.time(16, 0, 0): None},
               4: {datetime.time(8, 0, 0): None,
                   datetime.time(9, 0, 0): None,
                   datetime.time(10, 0, 0): None,
                   datetime.time(11, 0, 0): None,
                   datetime.time(12, 0, 0): None,
                   datetime.time(13, 0, 0): None,
                   datetime.time(14, 0, 0): None,
                   datetime.time(15, 0, 0): None,
                   datetime.time(16, 0, 0): None},
               5: {datetime.time(8, 0, 0): None,
                   datetime.time(9, 0, 0): None,
                   datetime.time(10, 0, 0): None,
                   datetime.time(11, 0, 0): None,
                   datetime.time(12, 0, 0): None,
                   datetime.time(13, 0, 0): None,
                   datetime.time(14, 0, 0): None,
                   datetime.time(15, 0, 0): None,
                   datetime.time(16, 0, 0): None}}

    rev_obj_dic = {8: {1: None, 2: None, 3: None, 4: None, 5: None},
                   9: {1: None, 2: None, 3: None, 4: None, 5: None},
                   10: {1: None, 2: None, 3: None, 4: None, 5: None},
                   11: {1: None, 2: None, 3: None, 4: None, 5: None},
                   12: {1: None, 2: None, 3: None, 4: None, 5: None},
                   13: {1: None, 2: None, 3: None, 4: None, 5: None},
                   14: {1: None, 2: None, 3: None, 4: None, 5: None},
                   15: {1: None, 2: None, 3: None, 4: None, 5: None},
                   16: {1: None, 2: None, 3: None, 4: None, 5: None},
                   }

    for key, val in rev_obj_dic.items():
        for d in val.keys():
            rev_obj_dic[key][d] = {'subject_name': None, 'subject_id': None}

    obj_arr = []
    # inner_arr=[]
    for cs in model:
        subject_name = cs.subject.subject_name
        start_time = cs.start_time
        end_time = cs.end_time
        day = cs.days

        # print(day)
        # print(type(day))






        if day == '1':
            day = 1
        elif day == '2':
            day = 2
        elif day == '3':
            day = 3
        elif day == '4':
            day = 4
        elif day == '5':
            day = 5
        else:
            day = None

        # datetime.time(8,00,00)

        # print(datetime.time(8,0,0))
        # print(start_time)
        # print(type(start_time))
        # print(end_time)

        if start_time == datetime.time(8,0,0) and end_time != datetime.time(8,0,0):
            if day != None:
                obj = {'day': day, 'start_time': start_time, 'subject_name': subject_name, 'subject_id': cs.subject.id}
                obj_arr.append(obj)
                # obj_dic[day].append({start_time: {'subject_name': subject_name, 'subject_id': cs.subject.id}})
                # obj_dic[day] = {start_time: {'subject_name': subject_name, 'subject_id': cs.subject.id}}
                obj_dic[day][start_time] = {'subject_name': subject_name, 'subject_id': cs.subject.id}
                rev_obj_dic[8][day] = {'subject_name': subject_name, 'subject_id': cs.subject.id}

                # obj_dic[day][datetime.time(8,0,0)] = {'subject_name': subject_name, 'subject_id': cs.subject.id}

            # obj_dic = {'day': {day: {start_time: {'subject_name': subject_name, 'subject_id': cs.subject.id}}}}


            start_time = datetime.time(9,0,0)
        # else:
        #     rev_obj_dic[8][day] = {'subject_name': None, 'subject_id': None}
        if start_time == datetime.time(9,0,0) and end_time != datetime.time(9,0,0):
            if day != None:
                obj = {'day': day, 'start_time': start_time, 'subject_name': subject_name, 'subject_id': cs.subject.id}
                obj_arr.append(obj)
                # obj_dic[day].append({start_time: {'subject_name': subject_name, 'subject_id': cs.subject.id}})
                obj_dic[day][start_time] = {'subject_name': subject_name, 'subject_id': cs.subject.id}
                rev_obj_dic[9][day] = {'subject_name': subject_name, 'subject_id': cs.subject.id}

            start_time = datetime.time(10,0,0)

        if start_time == datetime.time(10,0,0) and end_time != datetime.time(10,0,0):
            if day != None:
                obj = {'day': day, 'start_time': start_time, 'subject_name': subject_name, 'subject_id': cs.subject.id}
                obj_arr.append(obj)
                # obj_dic[day].append({start_time: {'subject_name': subject_name, 'subject_id': cs.subject.id}})
                obj_dic[day][start_time] = {'subject_name': subject_name, 'subject_id': cs.subject.id}
                rev_obj_dic[10][day] = {'subject_name': subject_name, 'subject_id': cs.subject.id}
            start_time = datetime.time(11,0,0)

        if start_time == datetime.time(11,0,0) and end_time != datetime.time(11,0,0):
            if day != None:
                obj = {'day': day, 'start_time': start_time, 'subject_name': subject_name, 'subject_id': cs.subject.id}
                obj_arr.append(obj)
                # obj_dic[day].append({start_time: {'subject_name': subject_name, 'subject_id': cs.subject.id}})
                obj_dic[day][start_time] = {'subject_name': subject_name, 'subject_id': cs.subject.id}
                rev_obj_dic[11][day] = {'subject_name': subject_name, 'subject_id': cs.subject.id}
            start_time = datetime.time(12,0,0)

        if start_time == datetime.time(12,0,0) and end_time != datetime.time(12,0,0):
            if day != None:
                obj = {'day': day, 'start_time': start_time, 'subject_name': subject_name, 'subject_id': cs.subject.id}
                obj_arr.append(obj)
                # obj_dic[day].append({start_time: {'subject_name': subject_name, 'subject_id': cs.subject.id}})
                obj_dic[day][start_time] = {'subject_name': subject_name, 'subject_id': cs.subject.id}
                rev_obj_dic[12][day] = {'subject_name': subject_name, 'subject_id': cs.subject.id}
            start_time = datetime.time(13,0,0)

        if start_time == datetime.time(13,0,0) and end_time != datetime.time(13,0,0):
            if day != None:
                obj = {'day': day, 'start_time': start_time, 'subject_name': subject_name, 'subject_id': cs.subject.id}
                obj_arr.append(obj)
                # obj_dic[day].append({start_time: {'subject_name': subject_name, 'subject_id': cs.subject.id}})
                obj_dic[day][start_time] = {'subject_name': subject_name, 'subject_id': cs.subject.id}
                rev_obj_dic[13][day] = {'subject_name': subject_name, 'subject_id': cs.subject.id}
            start_time = datetime.time(14,0,0)

        if start_time == datetime.time(14,0,0) and end_time != datetime.time(14,0,0):
            if day != None:
                obj = {'day': day, 'start_time': start_time, 'subject_name': subject_name, 'subject_id': cs.subject.id}
                obj_arr.append(obj)
                # obj_dic[day].append({start_time: {'subject_name': subject_name, 'subject_id': cs.subject.id}})
                obj_dic[day][start_time] = {'subject_name': subject_name, 'subject_id': cs.subject.id}
                rev_obj_dic[14][day] = {'subject_name': subject_name, 'subject_id': cs.subject.id}
            start_time = datetime.time(15,0,0)

        if start_time == datetime.time(15,0,0) and end_time != datetime.time(15,0,0):
            if day != None:
                obj = {'day': day, 'start_time': start_time, 'subject_name': subject_name, 'subject_id': cs.subject.id}
                obj_arr.append(obj)
                # obj_dic[day].append({start_time: {'subject_name': subject_name, 'subject_id': cs.subject.id}})
                obj_dic[day][start_time] = {'subject_name': subject_name, 'subject_id': cs.subject.id}
                rev_obj_dic[15][day] = {'subject_name': subject_name, 'subject_id': cs.subject.id}
            start_time = datetime.time(16,0,0)

        if start_time == datetime.time(16,0,0) and end_time != datetime.time(16,0,0):
            if day != None:
                obj = {'day': day, 'start_time': start_time, 'subject_name': subject_name, 'subject_id': cs.subject.id}
                obj_arr.append(obj)
                # obj_dic[day].append({start_time: {'subject_name': subject_name, 'subject_id': cs.subject.id}})
                obj_dic[day][start_time] = {'subject_name': subject_name, 'subject_id': cs.subject.id}
                rev_obj_dic[16][day] = {'subject_name': subject_name, 'subject_id': cs.subject.id}
            start_time = datetime.time(17,0,0)

        else:
            start_time = None
            # obj = {'day': day, 'start_time': start_time, 'subject_name': subject_name, 'subject_id': cs.subject.id}
            # obj_arr.append(obj)


        # obj = {'day': day, 'start_time': start_time}
        # print(obj["day"])
        # print(type(obj["day"]))
        # obj_arr.append(obj)
    # print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    # print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    # print("")
    # print(obj_arr)
    # print("")
    # print("")
    # print(obj_dic)
    # print("")
    # print("")
    # print(rev_obj_dic)
    # print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    # print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")




    return render(request, '../templates/student/studentSchedule.html', {'model': model, 'time': time, 'days': days, 'obj_arr': obj_arr, 'obj_dic': obj_dic, 'rev_obj_dic': rev_obj_dic})


def s_view_subject(request, pk):
    subject = Subject.objects.get(id=pk)
    student_classroom = StudentClassroom.objects.get(user_id=request.user.id)
    my_classroom = Classroom.objects.get(id=student_classroom.class_room.id)
    subject_class = ClassSubject.objects.get(subject_id=pk, class_room_id=my_classroom.id)
    files = TeacherFile.objects.filter(subject_id=pk)
    teacher= User.objects.get(id=subject.teacher_id)
    return render(request, '../templates/student/s_view_subject.html', {"subject": subject, 'subject_class': subject_class, 'files': files, 'teacher': teacher})


def my_class(request):
    class_id = StudentClassroom.objects.get(user_id=request.user.id).class_room.id
    classroom = Classroom.objects.get(id=class_id)
    students_ids = StudentClassroom.objects.filter(class_room_id=class_id)

    list_of_ids = []
    for s in students_ids:
        if s.user.id != request.user.id:
            list_of_ids.append(s.user.id)
    user = User.objects.filter(id__in=list_of_ids)

    class_chat= Class_Chat.objects.filter(receiver_class_id=classroom.id)

    return render(request, '../templates/student/my_class/my_class.html', {'classroom': classroom, 'users': user, 'class_chat': class_chat})



def class_msg(request, pk):
    if request.method == 'POST':
        form = ClassChatReceiveForm(request.POST)

        if form.is_valid():
            new_msg = Class_Chat(sender=request.user, receiver_class=Classroom.objects.get(id=pk),
                                   msg=request.POST['msg'], publish_date=datetime.now())
            new_msg.save()
            return redirect('my_class')
        else:
            print(form.errors)
            return HttpResponse('you are loser !!! try again')

    form = PrivateChatReceiveForm()

    return render(request=request, template_name="../templates/receive.html", context={"form": form})



def download(request, pk):
    act_file = TeacherFile.objects.get(id=pk)
    file_path = os.path.join(settings.MEDIA_ROOT, str(act_file.file))

    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    raise Http404

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
def my_test(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            # form.teacher=User.objects.get(id=form.teacher)

            obj = form.save(commit=False)
            obj.save()
            return redirect('/school')

        else:
            messages.error(request, "Invalid username or password.")
            return render(request=request,
                          template_name="../templates/school/create_subject.html",
                          context={"form": form})
    form = SubjectForm()
    return render(request=request,
                  template_name="../templates/school/create_subject.html",
                  context={"form": form})


# ### subject test
#
# def my_test(request):
#     if request.method == 'POST':
#         form = ClassSubjectForm(request.POST)
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
#     form = ClassSubjectForm()
#     return render(request=request,
#                   template_name="../templates/school/MY_TEST.html",
#                   context={"form": form})

def chat(request):
    model = Private_Chat.objects.filter(receiver_id=request.user.id)
    return render(request=request, template_name="../templates/chat.html", context={"model": model})

def send_msg(request):
    if request.method == 'POST':
        form = PrivateChatForm(request.POST)
        form.my_id = request.user.id
        # print(form)
        # print("&&&&&&&&&&&&&&&&&*^(*^*&T^*&^%&*T&^RT&^R&^%&(^%*&%*&^*&%R&^")
        # print(request.POST)


        if form.is_valid():
            new_msg = Private_Chat(sender=request.user, receiver_id=request.POST['receiver_id'],
                                   msg=request.POST['msg'], publish_date=datetime.now())
            new_msg.save()
            return redirect('send_msg')
        else:
            print(form.errors)
            return HttpResponse('you are loser !!! try again')


    form = PrivateChatForm()
    print(request.user.id)
    form.my_id = request.user.id
    return render(request=request, template_name="../templates/send_msg.html", context={"form": form})


def view_subject(request, pk):
    connection = ClassSubject.objects.filter(subject_id=pk)
    return render(request=request, template_name="../templates/teacher/view_subject.html",
                  context={"model": connection})


def change_meeting_url(request, pk):
    print(pk)  # didnt get the right id of the object and when submit all data disappear
    print(request.POST['met-url'])
    # connection = ClassSubject.objects.filter(subject_id=pk)
    connection = ClassSubject.objects.get(id=pk)
    print(connection)
    connection.meeting = request.POST['met-url']
    print(connection.meeting)
    connection.save()
    return redirect('view_subject', pk)
    # return render(request=request, template_name="../templates/teacher/view_subject.html",
    #               context={"model": connection})


def receive(request, pk):
    if request.method == 'POST':
        form = PrivateChatReceiveForm(request.POST)
        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print(type(pk))
        print(pk)
        if form.is_valid():
            new_msg = Private_Chat(sender=request.user, receiver_id=pk,
                                   msg=request.POST['msg'], publish_date=datetime.now())
            new_msg.save()
            return redirect('chat')
        else:
            print(form.errors)
            return HttpResponse('you are loser !!! try again')


    form = PrivateChatReceiveForm()

    return render(request=request, template_name="../templates/receive.html", context={"form": form})

