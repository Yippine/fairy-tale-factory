from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from story.models import Item

def create_story(request):
    return render(request, "menu/create_story.html")

def select_main_role(request):
    return render(request, "menu/select_main_role.html")

def select_main_role_by_data(request):
    items = Item.objects.all().filter(item_type=1)
    return render(request, "menu/select_main_role_by_data.html", {"items": items})

def select_sup_role(request):
    return render(request, "menu/select_sup_role.html")

def select_sup_role_by_data(request):
    items = Item.objects.all().filter(item_type=1)
    return render(request, "menu/select_sup_role_by_data.html", {"items": items})

def select_item(request):
    return render(request, "menu/select_item.html")

def select_item_by_data(request):
    items = Item.objects.all().filter(item_type=2)
    return render(request, "menu/select_item_by_data.html", {"items": items})

def main_role_details(request):
    return render(request, "menu/main_role_details.html")

def main_role_details_by_data(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return JsonResponse({
        'item_name': item.item_name,
        'item_info': item.item_info
    })

def sup_role_details(request):
    return render(request, "menu/sup_role_details.html")

def sup_role_details_by_data(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return JsonResponse({
        'item_name': item.item_name,
        'item_info': item.item_info
    })

def item_details(request):
    return render(request, "menu/item_details.html")

def item_details_by_data(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return JsonResponse({
        'item_name': item.item_name,
        'item_info': item.item_info
    })

def loading(request):
    return render(request, "display/loading.html")

def storybook_display(request):
    return render(request, "display/storybook_display.html")

def social_features(request):
    return render(request, "display/social_features.html")

def my_storybooks(request):
    return render(request, "display/my_storybooks.html")

def create_story_new(request):
    return render(request, "menu/create_story_new.html")

def select_main_role_new(request):
    return render(request, "menu/select_main_role_new.html")

def select_sup_role_new(request):
    return render(request, "menu/select_sup_role_new.html")

def select_item_new(request):
    items = Item.objects.all().filter(item_type=2)
    return render(request, "menu/select_item_new.html", {"items": items})

def main_role_details_new(request):
    return render(request, "menu/main_role_details_new.html")

def sup_role_details_new(request):
    return render(request, "menu/sup_role_details_new.html")

def item_details_new(request):
    return render(request, "menu/item_details_new.html")

def loading_new(request):
    return render(request, "display/loading_new.html")

def storybook_display_new(request):
    return render(request, "display/storybook_display_new.html")

def social_features_new(request):
    return render(request, "display/social_features_new.html")

def my_storybooks_new(request):
    return render(request, "display/my_storybooks_new.html")
