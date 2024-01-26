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

def about_us(request):
    return render(request, 'about_us.html')
