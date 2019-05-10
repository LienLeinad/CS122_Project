from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date
from django.utils.timezone import now
# Create your models here.
class SampleModel (models.Model):
    first_name = models.CharField(max_length = 15)
    last_name = models.CharField(max_length = 20)
    age = models.IntegerField
    def __str__(self):
        return str(self.first_name)

class CustomUser(AbstractUser):
    STUDENT = 'ST'
    TUTOR = 'TU'
    USER_TYPES = (
        (STUDENT,'Student'),
        (TUTOR,'Tutor')
    )
    user_type = models.CharField(
        max_length = 2,
        choices = USER_TYPES,
        default = TUTOR
    )
    street_name = models.CharField(
        max_length = 30
    )
    city = models.CharField(
        max_length = 40
    )
    contact = models.CharField(
        max_length = 11
    )
    emergency_contact = models.CharField(
        max_length = 50
    )
    birthday = models.DateField(default = now, editable = True)
    
    def __str__(self):
        return self.username

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    #related_name just makes it so that I can have two foreign keys in this model that refers to the same table which is CustomUser
    teacher = models.ForeignKey(CustomUser,related_name='CustomUser', on_delete = models.CASCADE, blank = True)#https://stackoverflow.com/questions/2642613/what-is-related-name-used-for-in-django
    def __str__(self):
        return str(self.user)

class Module(models.Model):
    ModuleTitle = models.CharField(max_length = 40, unique = True)
    Description = models.TextField(max_length = 500)
    pub_date = models.DateTimeField(auto_now_add = True, editable = False)
    Tutor = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
# class UserModel (models.Model):
#     STUDENT = 'ST'
#     TUTOR = 'TU'

#     USER_TYPES = (
#         (STUDENT,'Student'),
#         (TUTOR,'Tutor'),
#     )
#     user_type = models.CharField(
#         max_length = 2,
#         choices = USER_TYPES,
#         default = TUTOR,
#     )
#     user_ID = models.CharField(
#         max_length = 10,
#     )
#     first_name = models.CharField(
#         max_length = 40,
#     ) 
#     middle_initial = models.CharField(
#         max_length = 40,
#     )
#     last_name = models.CharField(
#         max_length = 40,
#     )
#     # username = models.CharField(
#     #     max_length = 40,
#     #     unique = True,
#     #     editable = False,
#     # )
#     email = models.EmailField(
#         max_length = 40,
#     )
#     contact = models.CharField(
#         max_length = 11,
#     )
    
