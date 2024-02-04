from django.shortcuts import render, redirect


#使用 redirect 函數將請求重定向到 "/home"。
def redirect_to_home(request):
    return redirect("/home")


#render 函數將 home.html 模板渲染為HTTP響應
def home(request):
    return render(request, "home.html")

def about_us(request):
    return render(request, 'about_us.html')

def home_new(request):
    return render(request, "home_new.html")

def about_us_new(request):
    return render(request, 'about_us_new.html')
