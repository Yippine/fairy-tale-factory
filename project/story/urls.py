from django.urls import path
from . import views

urlpatterns = [
    # 一般網頁
    path('createstory/', views.create_story, name='menu/create_story'),
    path('selectmainrole/', views.select_main_role, name='menu/select_main_role'),
    path('selectsuprole/', views.select_sup_role, name='menu/select_sup_role'),
    path('selectitem/', views.select_item, name='menu/select_item'),
    path('mainroledetails/', views.main_role_details, name='menu/main_role_details'),
    path('suproledetails/', views.sup_role_details, name='menu/sup_role_details'),
    path('itemdetails/', views.item_details, name='menu/item_details'),
    path('loading/', views.loading, name='display/loading'),
    path('storybookdisplay/', views.storybook_display, name='display/storybook_display'),
    path('socialfeatures/', views.social_features, name='display/social_features'),
    path('mystorybooks/', views.my_storybooks, name='display/my_storybooks'),

    # 新版網頁
    path('createstorynew/', views.create_story_new, name='menu/create_story_new'),
    path('selectmainrolenew/', views.select_main_role_new, name='menu/select_main_role_new'),
    path('selectsuprolenew/', views.select_sup_role_new, name='menu/select_sup_role_new'),
    path('selectitemnew/', views.select_item_new, name='menu/select_item_new'),
    path('mainroledetailsnew/', views.main_role_details_new, name='menu/main_role_details_new'),
    path('suproledetailsnew/', views.sup_role_details_new, name='menu/sup_role_details_new'),
    path('itemdetailsnew/', views.item_details_new, name='menu/item_details_new'),
    path('itemdetailsbydatanew/', views.item_details_by_data_new, name='menu/item_details_by_data_new'),
    path('getstoryelementnamenew/', views.get_story_element_name_new, name='menu/get_story_element_name_new'),
    path('loadingnew/', views.loading_new, name='display/loading_new'),
    path('storybookdisplaynew/', views.storybook_display_new, name='display/storybook_display_new'),
    path('socialfeaturesnew/', views.social_features_new, name='display/social_features_new'),
    path('mystorybooksnew/', views.my_storybooks_new, name='display/my_storybooks_new'),

    # 連接資料庫
    path('selectmainrolebydata/', views.select_main_role_by_data, name='menu/select_main_role_by_data'),
    path('selectsuprolebydata/', views.select_sup_role_by_data, name='menu/select_sup_role_by_data'),
    path('selectitembydata/', views.select_item_by_data, name='menu/select_item_by_data'),
    path('mainroledetailsbydata/', views.main_role_details_by_data, name='menu/main_role_details_by_data'),
    path('suproledetailsbydata/', views.sup_role_details_by_data, name='menu/sup_role_details_by_data'),
    path('itemdetailsbydata/', views.item_details_by_data, name='menu/item_details_by_data'),
]
