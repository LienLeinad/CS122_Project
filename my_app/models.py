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
    birthday = models.DateField(null = True,blank = True,editable = True)
    #username is not seen, it'sbuilt in, userID is also the object ID
    def __str__(self):
        return self.username

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)#PK and FK
    #related_name just makes it so that I can have two foreign keys in this model that refers to the same table which is CustomUser
    teacher = models.ForeignKey(CustomUser,related_name='CustomUser', on_delete = models.CASCADE, blank = True)#https://stackoverflow.com/questions/2642613/what-is-related-name-used-for-in-django
    def __str__(self):
        return str(self.user)

class Module(models.Model):
    ModuleTitle = models.CharField(max_length = 40, unique = True)#PK
    Description = models.TextField(max_length = 500)
    pub_date = models.DateTimeField(auto_now_add = True, editable = False)
    Tutor = models.ForeignKey(CustomUser, on_delete = models.CASCADE)#FK to CustomUser
    file = models.FileField(blank = True)
    def filename(self):
        return os.path.basename(self.file.name)
    def __str__(self):
        return str(self.ModuleTitle)



class HomeworkDetail(models.Model):
    ModuleTitle = models.ForeignKey(Module, on_delete = models.CASCADE) #PK/FK
    pub_date = models.DateField(auto_now_add = True, editable = False)
    deadline = models.DateField(default = now, editable = True)
    details = models.TextField(default='No Details')
    def __str__(self):
        return str(self.ModuleTitle)

class HomeworkSubmission(models.Model):
	# pk = object id
    Homework = models.ForeignKey(HomeworkDetail, on_delete = models.CASCADE)
    ContentFile = models.FileField(blank = True)
    StudentID = models.ForeignKey(Student,on_delete = models.CASCADE)
    Comment = models.TextField(default = "", null = True)


	
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
    
