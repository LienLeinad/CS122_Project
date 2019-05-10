from django.contrib import admin
from .models import CustomUser,Student
# from .models import SampleModel, UserModel
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Student)
# admin.site.register(SampleModel)
# admin.site.register(UserModel)