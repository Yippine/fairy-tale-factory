import os
import re
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from .dto import SelectItemDTO
from .models import Item

@csrf_exempt
def set_select_item(request):
    if request.method == "POST":
        json_dict = json.loads(request.body.decode("utf-8"))
        select_item = json_dict.get("select_item", {})
        request.session["select_item"] = select_item
        request.session.modified = True
        return JsonResponse({"status": "success"})
    return JsonResponse({"status": "error"}, status=400)

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

def main_role_details_by_data(request):
    item_id = request.GET.get("item_id")
    item = get_object_or_404(Item, pk=item_id)
    return JsonResponse({"item_name": item.item_name, "item_info": item.item_info})

def sup_role_details(request):
    return render(request, "menu/sup_role_details.html")

def sup_role_details_by_data(request):
    item_id = request.GET.get("item_id")
    item = get_object_or_404(Item, pk=item_id)
    return JsonResponse({"item_name": item.item_name, "item_info": item.item_info})

def item_details(request):
    return render(request, "menu/item_details.html")

def item_details_by_data(request):
    item_id = request.GET.get("item_id")
    item = get_object_or_404(Item, pk=item_id)
    return JsonResponse({"item_name": item.item_name, "item_info": item.item_info})

def loading(request):
    return render(request, "display/loading.html")

def storybook_display(request):
    a = """在一個村莊裡，有一個年輕的牧羊男孩負責放牧村民的羊群。他的工作是保護羊群免受狼的攻擊。這位男孩很快感到了無聊，於是他開始用喊叫「狼來了！」來尋求村民的注意。

村民聽到他的呼喊，紛紛前來幫助，但當他們到達時，發現並沒有狼。男孩哈哈大笑，對於自己的惡作劇感到非常高興。

幾天後，男孩再次感到無聊，並再次欺騙村民，喊道：“狼來了！狼來了！”村民再次趕來，但這一次還是沒有發現狼，只有一個嘲笑他們的男孩。

然而，當狼真的出現並威脅到羊群時，男孩急切地大聲呼喊，但這一次村民不再相信他，以為他再次在開玩笑，因此沒有人來救助他。最終，狼襲擊了羊群，男孩無法阻止，導致許多羊被狼吞噬。

這個故事的教訓是告訴人們不要撒謊和欺騙。如果你一再說謊，別人就會失去對你的信任。即使說真話時，也可能因為過去的謊言而失去幫助和支持。因此，這個故事強調了誠實和信任的重要性。"""
    article_list = split_paragraphs(a)

    if article_list:
        page_number = int(request.GET.get("page_number", 1)) # 取得頁數，預設為第一頁
        if page_number < 1:
            page_number = 1
        if page_number > len(article_list):
            page_number = len(article_list)
        current_article = article_list[page_number - 1]
        return render(request, "display/storybook_display.html", {"article_list": current_article, "page_number": page_number},)
    else:
        # 如果 article_list 為空，你可以加入一些適當的處理方式，例如傳回一個錯誤訊息給使用者
        return HttpResponse("文章列表為空，請檢查您的資料。")

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
    item_type_enum = {
        "main_role": 1,
        "sup_role": 1,
        "item": 2
    }
    select_item_dict = request.session.get('select_item')
    dto = SelectItemDTO.from_dict(select_item_dict)
    item_type = item_type_enum.get(dto.item_page)
    items = Item.objects.filter(item_type=item_type, disable_time__isnull=True).values(
        "item_id", "item_name"
    )
    return render(
        request,
        "menu/select_item_new.html",
        {
            "items": items
        }
    )

def main_role_details_new(request):
    return render(request, "menu/main_role_details_new.html")

def sup_role_details_new(request):
    return render(request, "menu/sup_role_details_new.html")

def item_details_new(request):
    return render(request, "menu/item_details_new.html")

def item_details_by_data_new(request):
    item_id = request.GET.get("item_id")
    item = get_object_or_404(Item, pk=item_id)
    return JsonResponse({"item_info": item.item_info})

def get_story_element_name_new(request):
    item_name = request.GET.get("item_name")
    dir_path = "story/static/img/story_elements/"
    img_name = "問號 0.jpg"
    for file_name in os.listdir(dir_path):
        if file_name.endswith((".jpg", ".png", ".jpeg", ".gif")):
            match = re.match(r"((.+)\s\d\.(jpg|png|jpeg|gif))", file_name)
            if match and item_name == match.group(2):
                img_name = match.group(1)
    return JsonResponse({"img_name": img_name})

def loading_new(request):
    return render(request, "display/loading_new.html")

def storybook_display_new(request):
    return render(request, "display/storybook_display_new.html")

def social_features_new(request):
    return render(request, "display/social_features_new.html")

def my_storybooks_new(request):
    return render(request, "display/my_storybooks_new.html")
