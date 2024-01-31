from django.shortcuts import render
from .forms import LoginForm, RegisterForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

def login(request):
    return render(request, 'login.html')

def login_by_data(request):
    form = LoginForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
    context = {
        'form':form
    }
    return render(request, 'login_by_data.html',context)

def register(request):
    return render(request, 'register.html')

def register_by_data(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            login_url = reverse('login_by_data')
            return HttpResponseRedirect(login_url)
    else:
        form = RegisterForm()
    context ={
        'form': form
    }
    return render(request, 'register_by_data.html', context)

def logout(request):
    logout(request)
    return HttpResponseRedirect('/login')

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
