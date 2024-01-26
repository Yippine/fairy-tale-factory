from django.shortcuts import render, redirect

def redirect_to_home(request):
    return redirect("/home")

def home(request):
    return render(request, "home.html")

def about_us(request):
    return render(request, 'about_us.html')
