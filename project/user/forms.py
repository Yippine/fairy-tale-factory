from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import User
import re

class RegisterForm(forms.ModelForm):
    password_regex = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$")

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields["user_password"].validators.append(self.validate_password)

    def validate_password(self, value):
        if not self.password_regex.match(value):
            raise ValidationError("密碼需要至少包含一個小寫字母、一個大寫字母和一個數字，並且至少為8個字符長。")

    class Meta:
        model = User
        fields = ("user_email", "user_name", "user_password")
        widgets = {
            "user_name": forms.TextInput(attrs={"class": "form-control"}),
            "user_email": forms.TextInput(attrs={"class": "form-control"}),
            "user_password": forms.TextInput(attrs={"class": "form-control"}),
        }
        labels = {"user_name": "帳號", "user_email": "電子郵件", "user_password": "密碼"}

class LoginForm(forms.Form):
    username = forms.CharField(
        label="帳號", widget=forms.TextInput(attrs={"class": "form-control"})
    )

    password = forms.CharField(
        label="密碼", widget=forms.PasswordInput(attrs={"class": "form-control"})
    )
