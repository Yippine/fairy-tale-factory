from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('userinfo/', views.user_info, name='user_info'),
    path('userinfo1/', views.user_info_1, name='user_info_1'),
    path('userinfo2/', views.user_info_2, name='user_info_2'),
    path('aboutus/', views.about_us, name='about_us'),
]
