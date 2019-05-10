from django.contrib import admin
from .models import CustomUser,Student,Module
# from .models import SampleModel, UserModel
# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Student)
admin.site.register(Module)
# admin.site.register(SampleModel)
# admin.site.register(UserModel)