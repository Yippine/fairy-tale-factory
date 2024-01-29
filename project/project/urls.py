from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # 一般網頁
    path('home/', views.home, name='home'),
    path('aboutus/', views.about_us, name='about_us'),

    # 新版網頁
    path('homenew/', views.home_new, name='home'),
    path('aboutusnew/', views.about_us_new, name='about_us'),

    # 後台網頁
    path('admin/', admin.site.urls),

    # APP 設定
    path('user/', include('user.urls')),
    path('story/', include('story.urls')),

    # 自動導頁
    path('', views.redirect_to_home, name='redirect_home'),
    re_path(r'^.*/$', TemplateView.as_view(template_name='404.html'), name="redirect_to_not_found"),
]
