"""Noodle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_app import views
from django.contrib.auth.views import login
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name = 'index' ),
    path('register/', views.register, name = 'register'),
    path('login/', views.login,name = 'user_login'),
    path('login/profile/',views.profile, name = 'user_profile'),
    path('login_error/',views.invalid_login, name = 'invalid_login'),
    path('login/profile/update/<username>/', views.user_update, name = 'update'),
    path('home/', auth_views.LoginView.as_view(template_name = 'login.1.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'logout.html'), name = 'logout'),
    path('login/modules/',views.module_list, name = 'module_list'),
    path('login/modules/<ModuleTitle>', views.module_tutor, name = 'module_tutor'),
    path('login/modules/student/<ModuleTitle>',views.module_student,name = 'module_student'),
    path('login/module/<ModuleTitle>/<str:file_name>', views.send_file, name = 'send_file'),
    path('login/students', views.student_list, name = 'student_list'),
    path('login/modules/upload/', views.module_upload,name = 'module_upload'),
    path('reg', views.register_choice, name = 'choose'),
    path('login/profile/tutor', views.cross_profile_student, name = 'cross_profile_student'),
    path('login/profile/students/cross/<user_name>',views.cross_profile_tutor,name = 'cross_profile_tutor'),
    path('modules/<str:file_name>', views.send_file, name = 'module_download'),
    path('login/modules/submission/modules/<str:file_name>', views.send_file, name = 'submission_download'),
    path('login/modules/upload/upload/<ModuleTitle>', views.homework_upload, name = 'homework_upload'),
    path('login/modules/<ModuleTitle>/module/comment/<id>', views.comment_upload, name = 'comment'),
    path('login/profile/students/cross/modules/<ModuleTitle>', views.module_tutor, name = 'cross_module_tutor')
 ]
