from django.db import models
from django.contrib.auth.models import User,AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

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
    
