from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.http import HttpResponseRedirect 
from django.urls import reverse
from .models import User
from django.contrib import messages
from .Custom import custom_login_required

def login(request):
    return render(request, 'login.html')

def login_by_data(request):
    form = LoginForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        user_name = form.cleaned_data['user_name']
        user_password = form.cleaned_data['user_password']
        
        try:
            user = User.objects.get(user_name=user_name)
        except User.DoesNotExist:
            user = None

        if user and user.user_password == user_password:
            print('登入成功用户ID:', user.user_id)
            request.session['user_id'] = user.user_id   
            request.user = user
            print('Session user_id:', request.session.get('user_id'))
            messages.success(request, '登入成功')
            return redirect('/story/createstory/')  
        else:
            print('帳號或密碼錯誤')
            messages.error(request, '帳號或密碼錯誤')
            return render(request, 'login_by_data.html', {'form':form})

    return render(request, 'login_by_data.html', {'form':form})

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
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('home')

def user_info(request):
    return render(request, 'user_info.html')

def user_info_1(request):
    return render(request, 'user_info_1.html')

@custom_login_required
def user_info_1_by_data(request):
    user_id = request.user.user_id
    user_name = request.user.user_name
    user_email = request.user.user_email
    user_info = {
        'user_id': user_id,
        'user_name': user_name,
        'user_email': user_email
    }
    return render(request, 'user_info_1_by_data.html', {'user_info': user_info})

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
