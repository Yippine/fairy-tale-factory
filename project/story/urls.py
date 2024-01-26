from django.urls import path
from . import views

urlpatterns = [
    path('createstory/', views.create_story, name='menu/create_story'),
    path('itemdetails/', views.item_details, name='menu/item_details'),
    path('itemdetails2/', views.item_details2, name='item_details2'),
    path('selectitem/', views.select_item, name='menu/select_item'),
    path('selectitem2/', views.select_item2, name='menu/select_item2'),
    path('mainroledetails/', views.main_role_details, name='menu/main_role_details'),
    path('suproledetails/', views.sup_role_details, name='menu/sup_role_details'),
    path('selectmainrole/', views.select_main_role, name='menu/select_main_role'),
    path('selectsuprole/', views.select_sup_role, name='menu/select_sup_role'),
    path('loading/', views.loading, name='display/loading'),
    path('mystorybooks/', views.my_storybooks, name='display/my_storybooks'),
    path('socialfeatures/', views.social_features, name='display/social_features'),
    path('storybookdisplay/', views.storybook_display, name='display/storybook_display'),
]
