from django.shortcuts import redirect
from django.contrib.auth.backends import BaseBackend
from .models import User

def custom_login_required(view_func):
    def wrapper(request, *args, **kwargs):
        user_id = request.session.get("user_id")
        if user_id:
            user = User.objects.get(user_id=user_id)
            request.user = user
            return view_func(request, *args, **kwargs)
        else:
            return redirect("/user/loginbydata/")
    return wrapper

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, user_name=None, password=None, **kwargs):
        try:
            user = User.objects.get(user_name=user_name)
        except User.DoesNotExist:
            return None
        if user.user_password == password:
            return user
        return None
