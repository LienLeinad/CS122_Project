from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import SampleModel, Student, CustomUser, Module,HomeworkDetail, HomeworkSubmission
from django.contrib import messages
from .forms import UserRegisterForm,HomeWorkUpload, UserUpdateForm,StudentRegistrationForm,ModuleUploadForm,HomeworkSubmissionForm,CommentForm
from django.contrib.auth.decorators import login_required
from wsgiref.util import FileWrapper
import os, tempfile, zipfile, mimetypes, io
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.db import connection
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

def register_choice(request):
    return render(request,'chooseProfile.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        form2 = StudentRegistrationForm(request.POST)
        if form.is_valid():
            print('form is valid')
            form.save()
            username = form.cleaned_data.get('username')
            temp = CustomUser.objects.get(username = username)
            if form.cleaned_data.get('user_type') == 'ST':
                
                if form2.is_valid():
                    temp_student = Student(user = temp, teacher = form2.cleaned_data.get('teacher'))
                    temp_student.save()

            messages.success(request,f'Account Created for {username}! go ahead and log in!')
            return redirect('register')
    else:
        form = UserRegisterForm()
        form2 = StudentRegistrationForm()
    context = {'form':form,'form2':form2}
    return render(request,'register.html', context)

def profile(request):
    if not request.user.is_authenticated:
        return redirect('invalid_login')
    else:
        user = request.user
        user_type = user.user_type
        
        if user_type == 'ST':
            student = Student.objects.get(user = user)
            teacher = student.teacher
            first_name = user.first_name
            last_name = user.last_name
            user_name = user.username
            contact = user.contact
            email = user.email
            street_name = user.street_name
            city = user.city
            birthday = user.birthday
            context = {'email': email,'first_name': first_name,'last_name':last_name,'user_name':user_name,'contact':contact, 'city': city, 'street_name': street_name, 'birthday': birthday, 'student':student,'teacher':teacher}
            return render(request,'Profiles/studentProfile_student.1.html', context)
        elif user_type == 'TU':
            first_name = user.first_name
            last_name = user.last_name
            user_name = user.username
            contact = user.contact
            email = user.email
            context = {'email': email,'first_name': first_name,'last_name':last_name,'user_name':user_name,'contact':contact,}
            return render(request,'Profiles/tutorProfile_tutor.1.html', context)
    

def login(request):
    if not request.user.is_authenticated:
        return redirect('invalid_login')
    else:
        user = request.user
        user_type = user.user_type
        if user_type == 'ST':
            first_name = user.first_name
            last_name = user.last_name
            new_modules = Module.objects.order_by('-pub_date')[:3]
            latest_module = Module.objects.order_by('-pub_date').filter()[0]
            context = {'first_name': first_name, 'last_name':last_name,'latest_module':latest_module,'new_modules':new_modules}

            return render(request,'Home/home_student.html', context)
        elif user_type == 'TU':
            first_name = user.first_name
            last_name = user.last_name
            new_modules = Module.objects.order_by('-pub_date')[:3]
            latest_module = Module.objects.order_by('-pub_date').filter()[0]
            context = {'first_name': first_name, 'last_name':last_name,'latest_module':latest_module,'new_modules':new_modules}
            return render(request,'Home/home_tutor.html', context)

def user_update(request, username):
    
    if not request.user.is_authenticated:
        return redirect('invalid_login')
    else:

        if request.method == 'POST':
            user_update_form = UserUpdateForm(data = request.POST)
            if user_update_form.is_valid():
                current_user = CustomUser.objects.get(username = username)
                if  user_update_form.cleaned_data.get('street_name') == "":
                    print('do nothin street')
                else:
                    current_user.street_name = user_update_form.cleaned_data.get('street_name')

                if  user_update_form.cleaned_data.get('city') == "":
                    print('do nothincity')
                else:
                    current_user.city = user_update_form.cleaned_data.get('city')

                if  user_update_form.cleaned_data.get('contact') == "":
                    print('do nothincontact')
                else:
                    current_user.contact = user_update_form.cleaned_data.get('contact')

                if  user_update_form.cleaned_data.get('emergency_contact') == "":
                    print('do nothinem')
                else:
                    current_user.emergency_contact = user_update_form.cleaned_data.get('emergency_contact')
                current_user.save(force_update = True)
                return redirect(profile)
        else: 
            user_update_form = UserUpdateForm()
        context = {
            'form':user_update_form,
        }
    if request.user.user_type == "TU":
        template = 'Profiles/editProfile_tutor.html'
    elif request.user.user_type == "ST":
        template = 'Profiles/editProfile_student.html'
    return render(request, template, context)

def student_list(request):
    if not request.user.is_authenticated or request.user.user_type == "ST":
        return redirect('invalid_login')
    else:
        students =  Student.objects.filter(teacher = request.user )
        context = {'students':students, 'user':request.user}

        return render(request,'all_students/allStudents_tutor.html',context)

def cross_profile_student(request):
    if not request.user.is_authenticated:
        return redirect('invalid_login')
    else: 
        student_user = Student.objects.get(user = request.user)
        Teacher = student_user.teacher
        template = 'Profiles/tutorProfile_student.html'
        context = {'user':Teacher, 'student_user':request.user}

        return render(request,template,context)
        
def cross_profile_tutor(request,user_name):
    if not request.user.is_authenticated:
        return redirect('invalid_login')
    else: 
        student = CustomUser.objects.get(username = user_name)
        teacher = request.user
        student_user= Student.objects.get(user = student)
        submissions = HomeworkSubmission.objects.filter(StudentID = student_user)
        modules = Module.objects.all()
        context = {'student':student, 'teacher':teacher,'submissions':submissions,'modules':modules}
        return render(request, 'Profiles/studentProfile_tutor.html',context)

def module_tutor(request,ModuleTitle):
    if not request.user.is_authenticated or request.user.user_type == "ST":
        return redirect('invalid_login')
    else:
        module = Module.objects.get(ModuleTitle = ModuleTitle)
        HomeworkDetails = HomeworkDetail.objects.get(ModuleTitle = module)
        Students = Student.objects.filter(teacher = request.user)
       
        submission_list = HomeworkSubmission.objects.filter(Homework = HomeworkDetails).all()
        # with connection.cursor() as cursor:
        #     cursor.execute("SELECT * FROM Student")
        #     submission_list = cursor.fetchall()
        print(submission_list)
        context = {
        'module':module,
        'HomeworkDetails':HomeworkDetails,
        'user':request.user,
        'submission_list':submission_list,
        'Students':Students,
        }
    return render(request, 'module/module_tutor.html', context)
     
def module_student(request,ModuleTitle):
    if not request.user.is_authenticated or request.user.user_type == "TU":
        return redirect('invalid_login')
    else:
        module = Module.objects.get(ModuleTitle = ModuleTitle)
        homework = HomeworkDetail.objects.get(ModuleTitle = module)

        if request.method == "POST":
            form = HomeworkSubmissionForm(request.POST,request.FILES)
            if form.is_valid():
                HomeworkSubmissions = HomeworkSubmission(Homework = homework, ContentFile = form.cleaned_data.get('ContentFile'), StudentID = Student.objects.get(user = request.user))
                HomeworkSubmissions.save()
                return redirect('module_student', ModuleTitle = ModuleTitle)
        form = HomeworkSubmissionForm()
        submission = HomeworkSubmission.objects.filter(StudentID = Student.objects.get(user = request.user),Homework = homework)
        print(submission)
        context = {'module':module, 'user':request.user, 'homework':homework, 'form':form, 'submission':submission}
        return render(request,'module/module_student.html',context)

def module_upload(request):
    if not request.user.is_authenticated or request.user.user_type == "ST":
        return redirect('invalid_login')
    else:
        if request.method == 'POST':
            form = ModuleUploadForm(request.POST,request.FILES)
            print('I got here')
            if form.is_valid():
                ModuleTitle = form.cleaned_data.get('ModuleTitle')
                Description = form.cleaned_data.get('Description')
                Tutor = request.user
                file = form.cleaned_data.get('file')
                module = Module(ModuleTitle = ModuleTitle, Description = Description, Tutor = Tutor, file = file)
                module.save() 
                print('form is valid')
                return redirect('upload/%s' %(ModuleTitle))
        form = ModuleUploadForm()
        context = {'form':form}
        return render(request, 'all_modules/module_upload/module_upload.html',context)

def homework_upload(request, ModuleTitle):
    if request.method == "POST":
        form = HomeWorkUpload(data = request.POST)
        if form.is_valid():
            ModuleTitle_temp = ModuleTitle
            deadline = form.cleaned_data.get('deadline')
            details = form.cleaned_data.get('details')
            HomeWorkUploaded = HomeworkDetail(ModuleTitle = Module.objects.get(ModuleTitle = ModuleTitle_temp), deadline = deadline, details = details)
            HomeWorkUploaded.save()
            return redirect('module_list')
    form = HomeWorkUpload()
    context = {'form':form}
    return render(request,'all_modules/module_upload/homework_upload.html', context)

def module_list(request):
    if not request.user.is_authenticated:
        return redirect('invalid_login')
    else:
        user = request.user
        module = Module.objects.all()
        context = {'Module': module}
        if user.user_type == "TU":
            return render(request, 'all_modules/allModules_tutor.html',context)
        elif user.user_type == "ST":
            return render(request,'all_modules/allModules_student.html',context)
  

def send_file(request, file_name):
    filename = os.path.join(settings.MEDIA_ROOT, file_name)
    wrapper = FileWrapper(open(filename, 'rb'))
    content_type = mimetypes.guess_type(filename)[0]
    response = HttpResponse(wrapper, content_type=content_type)
    response['Content-Length'] = os.path.getsize(filename)    
    response['Content-Disposition'] = "attachment; filename=%s"%file_name # I honestly have no idea why this works, just took it off a previous project's code (BioPhil website), I'll cite cite it in the COA
    return response

def comment_upload(request,ModuleTitle, id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            homework = HomeworkSubmission.objects.get(id = id)
            homework.Comment = form.cleaned_data.get('Comment')
            homework.save()
            return redirect('module_tutor', ModuleTitle = ModuleTitle)
    form = CommentForm()
    return render(request,'module/comment/comment.html', {'form':form})
