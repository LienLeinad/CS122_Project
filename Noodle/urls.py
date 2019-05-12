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
    path('home/', auth_views.LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'logout.html'), name = 'logout'),
    path('login/modules/',views.module_list, name = 'module_list'),
    path('login/students', views.student_list, name = 'student_list')
 ]
