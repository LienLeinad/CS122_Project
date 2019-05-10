from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import SampleModel
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    name_list = SampleModel.objects.all()
    
    context = {'name_list':name_list,}
    return render(request, 'template.html',context)

def invalid_login(request):
    if not request.user.is_authenticated:
        return render(request,'login_error.html')
    else:
        return redirect('user_login')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print('form is valid')
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account Created for {username}! go ahead and log in!')
            return redirect('register')
    else:
        form = UserRegisterForm()
    context = {'form':form,}
    return render(request,'register.html', context)

def profile(request):
    if not request.user.is_authenticated:
        return redirect('invalid_login')
    else:
        user = request.user
        user_type = user.user_type
        if user_type == 'ST':
            first_name = user.first_name
            last_name = user.last_name
            user_name = user.user_name
            contact = user.contact
            email = user.email
            context = {'email': email,
            'first_name': first_name,
            'last_name':last_name,
            'user_name':user_name,
            'contact':contact
            }

            return render(request,'Profiles/tutorProfile_tutor.html', context)
        elif user_type == 'TU':
            first_name = user.first_name
            last_name = user.last_name
            context = {'first_name': first_name, 'last_name':last_name}
            return render(request,'Profiles/tutorProfile_tutor.html', context)
    

def login(request):
    if not request.user.is_authenticated:
        return redirect('invalid_login')
    else:
        user = request.user
        user_type = user.user_type
        if user_type == 'ST':
            first_name = user.first_name
            last_name = user.last_name
            context = {'first_name': first_name, 'last_name':last_name}

            return render(request,'Home/home_student.html', context)
        elif user_type == 'TU':
            first_name = user.first_name
            last_name = user.last_name
            context = {'first_name': first_name, 'last_name':last_name}
            return render(request,'Home/home_tutor.html', context)
