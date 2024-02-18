import os
import re
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from .dto import ItemDTO, SelectItemDto, CreateStoryDto
from .models import Item
from .utils.dto_utils import get_select_item_page, get_create_story_page
from .utils.common_utils import split_paragraphs

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
    a = """有一天，大地上空的太陽變得異常火熱，炙烤著整個世界。 人們汗流浹背，苦不堪言。 於是，他們紛紛祈求夸父的力量，期望他能夠幫助解決這個燙人的難題。 夸父心懷天下蒼生，毅然決定追逐太陽，調整天氣，為百姓帶來涼爽。

夸父開始了他驚險又艱辛的追逐之旅。 他的步伐踏遍了千山萬水，縱橫了原野和河流。 他毫不猶豫地奔跑著，一往無前，但太陽似乎總是掛在他眼前，處處逃之夭夭。 夸父不禁感慨萬分，原來即便是力大無窮的他，也無法逾越天上神聖的界限。

在追逐的過程中，夸父遇見了無盡的艱難與困境。 有時他會穿越蒼茫的沙漠，有時會穿越蓊鬱的叢林。 他時而奔馳於高山之巔，時而穿越湍急的江河。 然而，太陽的速度總是超越他的步伐，如影隨形卻又不可捉摸。

隨著時間的推移，夸父的體力逐漸消耗殆盡，口渴難耐。 但他的堅持卻是無法動搖的，因為他深知，只有追上太陽，才能讓天空恢復正常，為人們帶來安慰和快樂。

然而，命運的捉弄，夸父最終感到疲憊不堪，倦怠滿身。 他在追逐的旅程中，因過度的努力而英勇地犧牲了。 夸父倒下的地方，天地為之一震，萬物為之黯然。 他的傳奇事蹟感動了天地間的眾生，人們為了紀念他的英勇和犧牲，舉行了隆重的祭祀儀式。

夸父死後，他的高大身軀變成了山脈，頭髮變成了樹木，血液變成了河流，扔出去的那根手杖，變成了一片桃林。 他的一切都融入了大自然，成為了大地的一部分。 夸父的靈魂和力量繼續流傳，他的英勇事蹟成為了永恆的傳說，激勵後人努力向前邁進。 夸父節的日子，人們總是在夜晚點燃篝火，唱起傳承千古的歌謠，紀念這位曾經為了眾生而追逐太陽的英雄。"""
    article_list = split_paragraphs(a)
    if article_list:
        page_number = int(request.GET.get("page_number", 1))
        if page_number < 1:
            page_number = 1
        if page_number > len(article_list):
            page_number = len(article_list)
        current_article = article_list[page_number - 1]
        article_list_json = json.dumps(article_list)
        return render(
            request,
            "display/storybook_display.html",
            {
                "article_list": current_article,
                "page_number": page_number,
                "article_list_json": article_list_json,
            },
        )

def social_features(request):
    return render(request, "display/social_features.html")

def my_storybooks(request):
    return render(request, "display/my_storybooks.html")

def create_story_new(request):
    return render(
        request,
        "menu/create_story_new.html",
        {
            "select_item_page": json.dumps(get_select_item_page(request)),
            "create_story_page": json.dumps(get_create_story_page(request)),
        },
    )

def select_item_new(request):
    item_type_enum = {"main_role": 1, "sup_role": 1, "item": 2}
    select_item_page = get_select_item_page(request)
    item_page = select_item_page.get("item_page", "")
    item_type = item_type_enum.get(item_page, 0)
    items = Item.objects.filter(item_type=item_type, disable_time__isnull=True).values(
        "item_id", "item_name"
    )
    create_story_page = get_create_story_page(request)
    return render(
        request,
        "menu/select_item_new.html",
        {
            "items": items,
            "select_item_page": json.dumps(select_item_page),
            "create_story_page": json.dumps(create_story_page),
        },
    )

def item_details_by_data_new(request):
    item_id = request.GET.get("item_id")
    item = get_object_or_404(Item, pk=item_id)
    return JsonResponse({"item_info": item.item_info})

def get_story_element_name_new(request):
    item_name = request.GET.get("item_name")
    dir_path = "story/static/img/story_elements/"
    img_name = "問號_0.jpg"
    for file_name in os.listdir(dir_path):
        if file_name.endswith((".jpg", ".png", ".jpeg", ".gif")):
            match = re.match(r"((.+)_\d\.(jpg|png|jpeg|gif))", file_name)
            if match and item_name == match.group(2):
                img_name = match.group(1)
                break
    return JsonResponse({"img_name": img_name})

def loading_new(request):
    return render(request, "display/loading_new.html")

def storybook_display_new(request):
    return render(request, "display/storybook_display_new.html")

def social_features_new(request):
    return render(request, "display/social_features_new.html")

def my_storybooks_new(request):
    return render(request, "display/my_storybooks_new.html")
