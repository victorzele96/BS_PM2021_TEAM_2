from django.forms import ModelForm, TextInput
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.db.models.functions import Now
from datetime import date, datetime, timedelta


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


class TeacherForm(forms.ModelForm):
    class Meta:
        model = TeacherForm
        fields = ('phone', 'subjects')


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


###################################   NEW  ##################################################
#
class ClassroomForm(forms.ModelForm):
    # classroom = Classroom.objects.all()
    # list_of_ids = []
    # if classroom:
    #     for c in classroom:
    #         list_of_ids.append(c.teacher.id)
    #     user = User.objects.filter(id__in=list_of_ids)
    #
    # list_id = []
    # for temp_obj in (User.objects.filter(is_staff=True) & User.objects.filter(is_superuser=False)):
    #     if temp_obj not in user:
    #         list_id.append(temp_obj.id)
    # qs = User.objects.filter(id__in=list_id)

    teacher = forms.ModelChoiceField(
        # queryset=qs,
        queryset=User.objects.filter(is_staff=True) & User.objects.filter(is_superuser=False),
        initial=0
    )

    class Meta:
        model = Classroom
        # fields = ("class_name","teacher")
        fields = ("class_name",)

    #
    def save(self, commit=True):
        classroom = super(ClassroomForm, self).save(commit=False)
        classroom.teacher = self.cleaned_data["teacher"]
        if commit:
            classroom.save()
        return classroom

#
class StudentClassroomForm(forms.ModelForm):
    # Sclassroom = StudentClassroom.objects.all()
    # list_of_ids = []
    # if Sclassroom:
    #     for c in Sclassroom:
    #         list_of_ids.append(c.user_id)
    # usert = User.objects.filter(id__in=list_of_ids)
    #
    # list_id = []
    # for temp_obj in (User.objects.filter(is_staff=False) & User.objects.filter(is_superuser=False)):
    #     if temp_obj not in usert:
    #         list_id.append(temp_obj.id)
    # # qs = User.objects.filter(id__in=list_id)

    class_room = forms.ModelChoiceField(
        # queryset=User.objects.get(is_staff=True, is_superuser=False),
        queryset=Classroom.objects.all(),
        initial=0
    )

    user = forms.ModelChoiceField(
        # queryset=User.objects.get(is_staff=True, is_superuser=False),
        # queryset=User.objects.filter(is_staff=False),
        # queryset=User.objects.filter(id__in=list_id),
        queryset = User.objects.filter(is_staff=True),
        initial=0
    )

    class Meta:
        model = StudentClassroom
        fields = ("class_room", "user")

    def save(self, commit=True):
        sc = super(StudentClassroomForm, self).save(commit=False)
        sc.class_room = self.cleaned_data["class_room"]
        sc.student = self.cleaned_data["user"]
        if commit:
            # if not StudentClassroom.objects.get(user_id=sc.student.id):
            #     sc.save()
            # else:
            # raise ValueError("user must be a student")
            sc.save()
        return sc


class SubjectForm(forms.ModelForm):
    teacher = forms.ModelChoiceField(
        # queryset=User.objects.get(is_staff=True, is_superuser=False),
        queryset=User.objects.filter(is_staff=True) & User.objects.filter(is_superuser=False),
        initial=0
    )

    duration = forms.IntegerField(label='Duration', required=True,
                                  validators=[MinValueValidator(1), MaxValueValidator(4)])

    class Meta:
        model = Subject
        fields = ("subject_name",)

    def save(self, commit=True):
        subject = super(SubjectForm, self).save(commit=False)
        subject.teacher = self.cleaned_data["teacher"]
        subject.duration = self.cleaned_data["duration"]
        if commit:
            subject.save()
        return subject


# DAYS_OF_WEEK = (
#     ('Sunday', 'Sunday'),
#     ('Monday', 'Monday'),
#     ('Tuesday', 'Tuesday'),
#     ('Wednesday', 'Wednesday'),
#     ('Thursday', 'Thursday'),
#     ('Friday', 'Friday'),
#     ('Saturday', 'Saturday'),
#
# )

DAYS_OF_WEEK = (
    (1, 'Sunday'),
    (2, 'Monday'),
    (3, 'Tuesday'),
    (4, 'Wednesday'),
    (5, 'Thursday'),

)


class ClassSubjectForm(forms.ModelForm):
    class_room = forms.ModelChoiceField(
        # queryset=User.objects.get(is_staff=True, is_superuser=False),
        queryset=Classroom.objects.all(),
        initial=0
    )

    subject = forms.ModelChoiceField(
        # queryset=User.objects.get(is_staff=True, is_superuser=False),
        queryset=Subject.objects.all(),
        initial=0
    )

    # day = forms.MultipleChoiceField(
    #     # queryset=User.objects.get(is_staff=True, is_superuser=False),
    #     # widgets={'day': forms.CheckboxSelectMultiple},
    #     # initial=0
    #     # widget=gears.widgets.CustomCheckboxSelectMultiple,
    #     required=True,
    #     choices=[(0, 'Sunday'),
    #         (1, 'Monday'),
    #         (2, 'Tuesday'),
    #         (3, 'Wednesday'),
    #         (4, 'Thursday'),
    #         (5, 'Friday'),
    #         (6, 'Saturday')]
    #         )
    # start_time = forms.TimeField(input_formats=["%H.%M"])
    # end_time = forms.TimeField(input_formats=["%H.%M"])
    start_time = forms.DateTimeField(input_formats=["%H.%M"])
    # end_time = forms.TimeField(input_formats=["%H.%M"])
    day = forms.MultipleChoiceField(
        # queryset=User.objects.get(is_staff=True, is_superuser=False),
        # widgets={'day': forms.CheckboxSelectMultiple},
        # initial=0
        # widget=gears.widgets.CustomCheckboxSelectMultiple,
        required=True,
        choices=DAYS_OF_WEEK
    )

    class Meta:
        model = ClassSubject
        # widgets = {'day': forms.CheckboxSelectMultiple}
        fields = ("class_room", "subject")

    def save(self, commit=True):
        class_subject = super(ClassSubjectForm, self).save(commit=False)
        class_subject.class_room = self.cleaned_data["class_room"]
        class_subject.subject = self.cleaned_data["subject"]
        # class_subject.days = self.cleaned_data["day"]
        # class_subject.days = self.day.str()
        class_subject.days = int(self.cleaned_data["day"][0])
        class_subject.start_time = self.cleaned_data["start_time"]
        # class_subject.end_time = class_subject.start_time + forms.TimeField(
        #     datetime.time(class_subject.subject.duration, 0, 0))
        # class_subject.end_time = class_subject.start_time + time(class_subject.subject.duration, 0, 0)
        class_subject.end_time = class_subject.start_time + (timedelta(hours=class_subject.subject.duration))
        print(class_subject.start_time)
        if commit:
            # print("class_subject.start_time    >>>>" + class_subject.start_time)
            # print("TIME    >>>>" + datetime.time(class_subject.subject.duration, 0, 0))
            # class_subject.end_time = class_subject.start_time + forms.TimeField(datetime.time(class_subject.subject.duration, 0, 0))
            class_subject.save()
        return class_subject


class File_Upload_Form(forms.ModelForm):
    subject = Subject.objects.none()
    file = forms.FileField(label='Select a file')

    class Meta:
        model = TeacherFile
        fields = ('name', 'description', 'file')

    def save(self, commit=True):
        act_file = super(File_Upload_Form, self).save(commit=False)
        # act_file.file = self.cleaned_data["file"]
        # file.subject = self.cleaned_data["subject"]

        if commit:
            # act_file.upload_time = datetime.now()
            act_file.save()
        return act_file


class FileUploadForm(forms.Form):
    file = forms.FileField(label='Select a file')


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = '__all__'
    def save(self,commit=True):
        act_ex = super(ExerciseForm, self).save(commit=False)
        if commit:
            act_ex.save()
        return act_ex

class SubjectExamForm(forms.ModelForm):
    ### need two more fields subject(key) and exercise(key) to use this form correct
    class Meta:
        model = Subject_Exam
        fields = ('description', 'start_time', 'end_time')


class SubjectExerciseForm(forms.ModelForm):
    description = forms.TextInput()
    start_time = forms.DateTimeField()
    end_time = forms.DateTimeField()
    ### need two more fields subject(key) and exercise(key) to use this form correct
    class Meta:
        model = Subject_Exercise
        fields = ('description', 'start_time', 'end_time')

    def save(self, commit=True):
        new_form = super(SubjectExerciseForm, self).save(commit=False)
        self.description = self.cleaned_data["description"]
        self.start_time = self.cleaned_data["start_time"]
        self.end_time = self.cleaned_data["end_time"]
        # act_file.file = self.cleaned_data["file"]
        # file.subject = self.cleaned_data["subject"]

        if commit:
            # act_file.upload_time = datetime.now()
            new_form.save()
        return new_form


# class StudentExercisesForm(forms.ModelForm):
#     ### need two more fields student(key) and subject_exercise(O-T-O_key) to use this form correct
#     class Meta:
#         model = Student_Exercises
#         fields = ('description', 'start_time', 'end_time')


class PrivateChatForm(forms.Form):
    receiver_id = forms.ModelChoiceField(
            queryset=User.objects.all(),
            initial=0
    )
    msg = forms.CharField(widget=forms.Textarea)

    class Meta:
        fields = ('msg', 'receiver_id')

    def save(self, commit=True):
        msg = super(PrivateChatForm, self).save(commit=False)
        user = self.cleaned_data["receiver_id"]
        msg.receiver_id = user.id
        if commit:
            msg.publish_date = datetime.now()
            msg.save()
        return msg


class PrivateChatReceiveForm(forms.Form):

    msg = forms.CharField(widget=forms.Textarea)
    class Meta:
        fields = ('msg',)

    def save(self, commit=True):
        msg = super(PrivateChatForm, self).save(commit=False)

        if commit:
            msg.publish_date = datetime.now()
            msg.save()
        return msg


    def save(self, commit=True):
        private_chat = super(PrivateChatForm, self).save(commit=False)

        if commit:
            private_chat.publish_date = datetime.now()
            private_chat.save()
        return private_chat


class PrivateChatTestForm(forms.ModelForm):
    class Meta:
        model = Private_Chat
        fields = ('msg', 'publish_date', 'receiver_id')


class ClassChatTestForm(forms.ModelForm):
    class Meta:
        model = Class_Chat
        fields = ('msg', 'publish_date')


class ClassChatForm(forms.ModelForm):
    class Meta:
        model = Class_Chat
        fields = ('msg', 'publish_date')

    def save(self, commit=True):
        class_chat = super(ClassChatForm, self).save(commit=False)

        if commit:
            class_chat.publish_date = datetime.now()
            class_chat.save()
        return class_chat


class ClassChatReceiveForm(forms.Form):

    msg = forms.CharField(widget=forms.Textarea)
    class Meta:
        fields = ('msg',)

    def save(self, commit=True):
        msg = super(PrivateChatForm, self).save(commit=False)

        if commit:
            msg.publish_date = datetime.now()
            msg.save()
        return msg


