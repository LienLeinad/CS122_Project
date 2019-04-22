from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import SampleModel
from django.contrib import messages
from .forms import UserRegisterForm
# Create your views here.
def index(request):
    name_list = SampleModel.objects.all()
    
    context = {'name_list':name_list,}
    return render(request, 'template.html',context)


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            print('form is valid')
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account Created for {username}! go ahead and log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    context = {'form':form,}
    return render(request,'register.html', context)

# def login(request):
#     user_list = UserModel.objects.all()
#     context = {'user_list':user_list}
#     return render(request,'login.html',context)

# def user_page(request, user_type, UserID):
#     User = UserModel.objects.get(UserID = UserID)
#     if 


# def user_page(request):
#     # User = UserModel.objects.get(user_ID = user_ID)
#     # first_name = User.first_name
#     # last_name = User.last_name
#     # context = {'first_name':first_name, 'last_name':last_name}
#     return render(request, 'tutorProfile_tutor.html')