from django.shortcuts import render

def create_story(request):
    return render(request, "menu/create_story.html")

def item_details(request):
    return render(request, "menu/item_details.html")

def select_item(request):
    return render(request, "menu/select_item.html")

def main_role_details(request):
    return render(request, "menu/main_role_details.html")

def sup_role_details(request):
    return render(request, "menu/sup_role_details.html")

def select_main_role(request):
    return render(request, "menu/select_main_role.html")

def select_sup_role(request):
    return render(request, "menu/select_sup_role.html")

def loading(request):
    return render(request, "display/loading.html")

def my_storybooks(request):
    return render(request, "display/my_storybooks.html")

def social_features(request):
    return render(request, "display/social_features.html")

def storybook_display(request):
    return render(request, "display/storybook_display.html")
