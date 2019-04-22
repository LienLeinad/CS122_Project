from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required = False)
    STUDENT = 'ST'
    TUTOR = 'TU'
    USER_TYPES = [
        (STUDENT,'Student'),
        (TUTOR,'Tutor')
    ]
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    
    street_name = forms.CharField(max_length=30)
    city = forms.CharField(max_length= 40)
    contact = forms.CharField(max_length=11)

    user_type = forms.ChoiceField(choices = USER_TYPES)
    class Meta :
        model = CustomUser
        fields = ['username', 'email','first_name','last_name','user_type','street_name','city','contact', 'password1', 'password2']
