from django.http import HttpResponse
from django.shortcuts import render

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

def login_new(request):
    return render(request, 'login_new.html')

def register_new(request):
    return render(request, 'register_new.html')

def user_info_new(request):
    return render(request, 'user_info_new.html')

def user_info_1_new(request):
    return render(request, 'user_info_1_new.html')

def user_info_2_new(request):
    return render(request, 'user_info_2_new.html')
