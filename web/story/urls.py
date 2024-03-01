from django.urls import path
from utils.common_utils import handle_post_request
from . import views

urlpatterns = [
    # 一般網頁
    path('setcreatestorypage/', lambda request: handle_post_request(request)),
    path('createstory/', views.create_story, name='menu/create_story'),
    path('setfetchstorypromptpage/', lambda request: handle_post_request(request)),
    path('fetchstoryprompt/', views.fetch_story_prompt, name='menu/fetch_story_prompt'),
    path('setselectitempage/', lambda request: handle_post_request(request)),
    path('selectitem/', views.select_item, name='menu/select_item'),
    path('fetchiteminfo/', views.fetch_item_info, name='menu/fetch_item_info'),
    path('getstoryelementname/', views.get_story_element_name, name='menu/get_story_element_name'),
    path('storybookdisplay/', views.storybook_display, name='display/storybook_display'),
    path('mystorybooks/', views.my_storybooks, name='display/my_storybooks'),

    # 新版網頁
    path('mystorybooksnew/', views.my_storybooks_new, name='display/my_storybooks_new'),
]
