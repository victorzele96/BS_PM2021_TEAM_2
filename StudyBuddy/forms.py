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

class ClassroomForm(forms.ModelForm):

    teacher = forms.ModelChoiceField(
        # queryset=User.objects.get(is_staff=True, is_superuser=False),
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



class StudentClassroomForm(forms.ModelForm):
    class_room = forms.ModelChoiceField(
        # queryset=User.objects.get(is_staff=True, is_superuser=False),
        queryset=Classroom.objects.all(),
        initial=0
    )

    student = forms.ModelChoiceField(
        # queryset=User.objects.get(is_staff=True, is_superuser=False),
        queryset=User.objects.filter(is_staff=False),
        initial=0
    )



    class Meta:
        model = StudentClassroom
        fields = ("class_room","student")

    def save(self, commit=True):
        sc = super(StudentClassroomForm, self).save(commit=False)
        sc.class_room = self.cleaned_data["class_room"]
        sc.user = self.cleaned_data["student"]
        if commit:
            if not StudentClassroom.objects.get(user_id=sc.user.id):
                sc.save()
            else:
                raise ValueError("user must be a student")
        return sc



class SubjectForm(forms.ModelForm):
    teacher = forms.ModelChoiceField(
        # queryset=User.objects.get(is_staff=True, is_superuser=False),
        queryset=User.objects.filter(is_staff=True) & User.objects.filter(is_superuser=False),
        initial=0
    )

    duration = forms.IntegerField(label='Duration', required=True, validators=[MinValueValidator(1), MaxValueValidator(4)])

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




DAYS_OF_WEEK = (
    ('Sunday', 'Sunday'),
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),

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
        class_subject.days = self.cleaned_data["day".str()]
        class_subject.start_time = self.cleaned_data["start_time"]
        # class_subject.end_time = class_subject.start_time + forms.TimeField(
        #     datetime.time(class_subject.subject.duration, 0, 0))
        # class_subject.end_time = class_subject.start_time + time(class_subject.subject.duration, 0, 0)
        class_subject.end_time = class_subject.start_time+(timedelta(hours=class_subject.subject.duration))
        print(class_subject.start_time)
        if commit:
            # print("class_subject.start_time    >>>>" + class_subject.start_time)
            # print("TIME    >>>>" + datetime.time(class_subject.subject.duration, 0, 0))
            # class_subject.end_time = class_subject.start_time + forms.TimeField(datetime.time(class_subject.subject.duration, 0, 0))
            class_subject.save()
        return class_subject


class File_Upload_Form(forms.ModelForm):
    class Meta:
        model = TeacherFile
        fields=('name','file')