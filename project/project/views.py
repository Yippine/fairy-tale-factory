from django.shortcuts import render, redirect

def redirect_to_home(request):
    return redirect("/home")

def home(request):
    return render(request, "home.html")
