from django.contrib import admin
from django.urls import include, path, re_path
from .views import redirect_to_home, home
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_home, name='redirect_home'),
    path('home/', home, name='home'),
    path('user/', include('user.urls')),
    path('story/', include('story.urls')),
    re_path(r'^.*/$', TemplateView.as_view(template_name='404.html'), name="redirect_to_not_found"),
]
