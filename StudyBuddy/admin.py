from django.contrib import admin

# from .models import Article
from .models import *
# from .forms import *
# Register your models here.


admin.site.register(Article)

admin.site.register(Classroom)
admin.site.register(StudentClassroom)
admin.site.register(Subject)
admin.site.register(ClassSubject)
admin.site.register(TeacherFile)

admin.site.register(Subject_Exercise)

