from django.http import HttpResponse
from django.shortcuts import render
from .models import User

def get_first_user(request):
    first_user = User.objects.first()
    if first_user:
        user_type_display = first_user.get_user_type_display()
        return HttpResponse(f'<h1>User ID: {first_user.user_id}, User Type: {first_user.user_type} - {user_type_display}, User Name: {first_user.user_name}</h1>')
    else:
        return HttpResponse('<h1>No user found</h1>')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def user_info(request):
    return render(request, 'user_info.html')

def user_info_1(request):
    return render(request, 'user_info_1.html')

def user_info_2(request):
    return render(request, 'user_info_2.html')

def about_us(request):
    return render(request, 'about_us.html')
