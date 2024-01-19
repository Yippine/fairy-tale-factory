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
