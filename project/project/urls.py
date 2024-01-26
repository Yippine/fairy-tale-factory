from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.redirect_to_home, name='redirect_home'),
    path('home/', views.home, name='home'),
    path('aboutus/', views.about_us, name='about_us'),
    path('user/', include('user.urls')),
    path('story/', include('story.urls')),
    re_path(r'^.*/$', TemplateView.as_view(template_name='404.html'), name="redirect_to_not_found"),
]
