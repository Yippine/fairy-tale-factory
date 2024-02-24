import os
import re
import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt
from .dto import ItemDTO, SelectItemDto, CreateStoryDto
from .models import Item, OriginalStory, NewStory
from .utils.dto_utils import (
    get_role_info_by_role_item,
    get_select_item_page,
    get_create_story_page,
)
from .utils.common_utils import split_paragraphs
from .utils.create_new_text import gen_story_text
from .utils import sdxl_controller

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
    create_story_page = request.session.get("create_story_page", {})
    main_role_name = create_story_page.get("main_role", {}).get("item_name")
    sup_role_name = create_story_page.get("sup_role", {}).get("item_name")
    item_name = create_story_page.get("item", {}).get("item_name")
    main_role_detail = (
        Item.objects.filter(item_name=main_role_name).values("item_info").first()
    )
    sup_role_detail = (
        Item.objects.filter(item_name=sup_role_name).values("item_info").first()
    )
    item_detail = Item.objects.filter(item_name=item_name).values("item_info").first()
    orm_story = OriginalStory.objects.filter(
        original_story_name=create_story_page.get("main_role", {}).get("item_name")
    ).values("original_story_content")
    story_info = {
        "main_character_info": f"""主角名稱：{main_role_name}
        主角特徵：{main_role_detail}
        """,
        "supporting_character_info": f"""配角名稱：{sup_role_name}
        配角特徵：{sup_role_detail}
        """,
        "props_info": f"""道具名稱：{item_name}
        道具功能：{item_detail}""",
        "story_text": f"""
        故事背景敘述：{orm_story}""",
    }
    story_text = gen_story_text(story_info)
    generated_story = NewStory(tw_new_story_content=story_text)
    generated_story.save()
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
            match = re.match(r"((.+)_\d\.(jpg|png|jpeg|gif|tif))", file_name)
            if match and item_name == match.group(2):
                img_name = match.group(1)
                break
    return JsonResponse({"img_name": img_name})

def fetch_text_command_new(request):
    create_story_page = request.session.get("create_story_page", {})
    create_story_dto = CreateStoryDto.from_dict(create_story_page)
    roles = ["main_role", "sup_role", "item"]  # 定義角色列表
    # 初始化數據字典
    data = {f"{role}_{info}": "" for role in roles for info in ["id", "name", "info"]}
    data["original_story_content"] = ""
    # 用一個循環處理所有角色，避免代碼重複
    for role in roles:
        role_item = getattr(create_story_dto, role, None)
        if role_item:
            data[f"{role}_name"] = role_item.item_name
            data[f"{role}_id"] = role_item.item_id
            if role_item.item_id:
                item_with_story = (
                    Item.objects.filter(item_id=role_item.item_id)
                    .select_related("original_story")
                    .first()
                )
                print(f"item_with_story: {item_with_story}")
                if item_with_story and item_with_story.original_story:
                    data[f"{role}_info"] = item_with_story.item_info
                    if role == "main_role":
                        data[
                            "original_story_content"
                        ] = item_with_story.original_story.original_story_content
    story_example_spacing = "\n" if data["original_story_content"] else ""
    text_command = f'''您是一位在最吸引人、最受矚目、最熱門、最廣為討論且最值得推薦的童話故事作家，需要創作一個適合台灣地區 3 到 12 歲小朋友的童話故事。故事必須包含 1 個主角、1 個配角和 1 個道具，並按照以下要素進行故事創作：

一、主角資訊
主角名稱：{data['main_role_name']}
特徵性格：{data['main_role_info']}

二、配角資訊
配角名稱：{data['sup_role_name']}
特徵性格：{data['sup_role_info']}

三、道具資訊
道具名稱：{data['item_name']}
神奇特性：{data['item_info']}

四、故事範例{story_example_spacing}{data['original_story_content']}

五、生成格式
"""【故事名稱】為接下來的故事取一個最吸引人、最受矚目、最熱門、最廣為討論且最值得推薦的故事名稱。
【起】故事開頭，主角和配角的介紹，故事背景簡介。
【承】主角面臨挑戰或問題，展開情節，加入道具。
【轉】高潮部分，意想不到的情節發生，深刻的教訓浮現。
【合】結局，主角得到成長或改變，故事總結。"""

六、故事要素
1. 創造力：故事情節要富有想像力。
2. 深刻的情感：主角和配角之間有情感連結，故事觸動人心。
3. 簡單而深刻的教訓：故事要傳達明確的價值觀或教訓。
4. 精彩的角色：主角和配角要有鮮明的性格。
5. 意想不到的情節：故事中要有令人驚喜的轉折。
6. 豐富的描述：場景和角色要有生動的描寫。
7. 流暢的文筆：故事要流暢易讀。
8. 現代感：故事要吸引當代年輕讀者。
9. 年齡適宜性：適合3到12歲的小朋友閱讀。
10. 教育性質：故事要有教育價值。
11. 文化連結：故事要具有文化元素。
12. 趣味性：故事要引人入勝，讓小朋友喜歡閱讀。
13. 視覺元素：可以包括圖畫或插圖。
14. 情感連結：故事要觸動讀者的情感。
15. 啟發性：故事要啟發讀者思考。
16. 長度和結構：故事要遵循起承轉合結構，長度約360字左右。

請以您的專業經驗，直接創作出，根據以上指令創作一個動人的童話故事，完美地結合上述的 1 個主角、1 個配角和 1 個道具，且充分發揮這三個元素的功能和特色，創作出新穎、有趣且完全不突兀的故事內容。'''
    return JsonResponse({"text_command": text_command})

def loading_new(request):
    return render(request, "display/loading_new.html")

def storybook_display_new(request):
    newstory = NewStory.objects.last()
    new_story_content = newstory.tw_new_story_content
    article_list = split_paragraphs(new_story_content)
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
            "display/storybook_display_new.html",
            {
                "article_list": current_article,
                "page_number": page_number,
                "article_list_json": article_list_json,
            },
        )
    return render(request, "display/storybook_display_new.html")

def social_features_new(request):
    return render(request, "display/social_features_new.html")

def my_storybooks_new(request):
    return render(request, "display/my_storybooks_new.html")
