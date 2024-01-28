from django.shortcuts import render, get_object_or_404
from story.models import Item

def create_story(request):
    return render(request, "menu/create_story.html")

def item_details(request):
    return render(request, "menu/item_details.html")

def select_item(request):
    items = Item.objects.all().filter(item_type=2)
    return render(request, "menu/select_item.html", {'items': items})

def select_item2(request):
    items = Item.objects.all().filter(item_type=2)
    return render(request, "menu/select_item2.html", {'items': items})

def item_details2(request):
    item_id = request.POST.get('item')
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'menu/item_details2.html', {'selected_item': item})

def main_role_details(request, main_role_name):
    main_role_id = request.POST.get('role')
    mainrole = get_object_or_404(Item, pk=main_role_id)
    return render(request, "menu/main_role_details.html",{'select_main_role': mainrole})

def sup_role_details(request):
    sup_role_id = request.POST.get('role')
    suprole = get_object_or_404(Item, pk=sup_role_id)
    return render(request, "menu/sup_role_details.html",{sup_role_details: suprole})

def select_main_role(request):
    MainRole = Item.objects.all().filter(item_type=1)
    return render(request, "menu/select_main_role.html",{'select_main_role': MainRole})

def select_sup_role(request):
    SupRole = Item.objects.all().filter(item_type=1)
    return render(request, "menu/select_sup_role.html", {'select_sup_role': SupRole})

def loading(request):
    return render(request, "display/loading.html")

def my_storybooks(request):
    return render(request, "display/my_storybooks.html")

def social_features(request):
    return render(request, "display/social_features.html")

def storybook_display(request):
    return render(request, "display/storybook_display.html")
