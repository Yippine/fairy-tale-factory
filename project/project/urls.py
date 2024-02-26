from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    # 一般網頁
    path('home/', views.home, name='home'),
    path('aboutus/', views.about_us, name='about_us'),
    path('talktochatgpt/', views.talk_to_chatgpt, name='talk_to_chatgpt'),
    path('searchfiles/', views.search_files, name='search_files'),
    path('getfilecontent/', views.get_file_content, name='get_file_content'),

    # 新版網頁
    path('homenew/', views.home_new, name='home_new'),
    path('aboutusnew/', views.about_us_new, name='about_us_new'),
    path('talktochatgptnew/', views.talk_to_chatgpt_new, name='talk_to_chatgpt_new'),
    path('searchfilesnew/', views.search_files_new, name='search_files_new'),
    path('getfilecontentnew/', views.get_file_content_new, name='get_file_content_new'),

    # 後台網頁
    path('admin/', admin.site.urls),

    # APP 設定
    path('user/', include('user.urls')),
    path('story/', include('story.urls')),

    # 自動導頁
    path('', views.redirect_to_home, name='redirect_home'),
    re_path(r'^.*/$', TemplateView.as_view(template_name='404.html'), name="redirect_to_not_found"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
