from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,Student,Module, HomeworkDetail,HomeworkSubmission
BIRTH_YEAR_CHOICES = [
    '2008',
    '2009',
    '2010',
    '2011',
    '2012',
    '2013',
    '2014',
    '2015',
    '2016',
    '2017',
    '2018',
    '2019',
    '2020',
    '2021',
    '2022',
    '2023',
    '2024',
    '2025',
    '2026',
    '2027',
    '2028',
    '2029',
    '2030',
    '2031',
    
]
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
    birthday = forms.DateField( widget=forms.widgets.SelectDateWidget(years = BIRTH_YEAR_CHOICES))
    class Meta :
        model = CustomUser
        fields = ['username', 'email','first_name','last_name','user_type','street_name','city','contact', 'password1', 'password2', 'emergency_contact', 'city', 'street_name', 'birthday']

class HomeWorkUpload(forms.ModelForm):
    deadline = forms.DateField(widget = forms.SelectDateWidget)
    details = forms.CharField(widget = forms.Textarea)
    class Meta:
        model = HomeworkDetail
        fields = ['deadline', 'details']

class HomeworkSubmissionForm(forms.ModelForm):
    ContentFile = forms.FileField()
    class Meta:
        model = HomeworkSubmission
        fields = ['ContentFile']

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

class CommentForm(forms.ModelForm):
    Comment = forms.CharField(widget = forms.Textarea)
    class Meta:
        model = HomeworkSubmission
        fields = ['Comment']