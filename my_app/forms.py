from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,Student,Module

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
    street_name = forms.CharField(max_length=30, required = False)
    city = forms.CharField(max_length= 40, required = False)
    contact = forms.CharField(max_length=11, required = False)
    emergency_contact = forms.CharField(max_length = 50, required = False)
    user_type = forms.ChoiceField(choices = USER_TYPES)
    birthday = forms.DateField( widget=forms.widgets.DateInput(format="%m/%d/%Y"))
    class Meta :
        model = CustomUser
        fields = ['username', 'email','first_name','last_name','user_type','street_name','city','contact', 'password1', 'password2', 'emergency_contact', 'city', 'street_name', 'birthday']


class StudentRegistrationForm(forms.ModelForm):
    teacher = forms.ModelChoiceField(queryset = CustomUser.objects.filter(user_type = 'TU'), required= False)
    class Meta:
        model = Student
        fields = ['teacher']
class UserUpdateForm(forms.ModelForm):
    street_name = forms.CharField(max_length=30, required = False)
    city = forms.CharField(max_length= 40, required = False)
    contact = forms.CharField(max_length=11, required = False)
    emergency_contact = forms.CharField(max_length = 50, required = False)
    class Meta :
        model = CustomUser
        fields = ['contact', 'emergency_contact', 'city', 'street_name']
class ModuleUploadForm(forms.ModelForm):
    ModuleTitle = forms.CharField(max_length = 40)
    Description = forms.CharField(widget = forms.Textarea)
    # Tutor = forms.ModelChoiceField(queryset = CustomUser.objects.filter(user_type = 'TU'))
    file = forms.FileField(allow_empty_file = True)
    class Meta:
        model = Module
        fields = ['ModuleTitle','Description','file']