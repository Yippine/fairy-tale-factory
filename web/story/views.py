import json
import logging
import os
import re
import threading
from queue import Queue

from decouple import config
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render

from .dto import CreateStoryDto
from .models import Item, NewStory, CoverDesign
from .utils.common_utils import split_paragraphs
from .utils.chatgpt_api import gen_storyboard_desc_prompt, call_chatgpt_api
from .utils.dto_utils import get_create_story_page, get_select_item_page
from .utils.sdxl_api import create_image_from_prompt

lock = threading.Lock()
generated_image_paths = Queue()

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
    pass

def social_features(request):
    return render(request, "display/social_features.html")

def my_storybooks(request):
    return render(request, "display/my_storybooks.html")

def create_story_new(request):
    # 調用 fetch_text_prompt_new 函式
    response = fetch_text_prompt_new(request)
    # JsonResponse 對象的內容是 bytes，需要解碼成 str
    response_content = response.content.decode('utf-8')
    # 將 JSON 字符串轉換成 Python 字典
    response_data = json.loads(response_content)
    # 從字典中取得 text_prompt
    all_roles_have_names = response_data.get('all_roles_have_names', False)
    if all_roles_have_names:
        text_prompt = response_data.get('text_prompt', '')
        print(f"text_prompt: {text_prompt}")
        story_text = call_chatgpt_api(text_prompt)
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

def fetch_text_prompt_new(request):
    create_story_page = request.session.get("create_story_page", {})
    create_story_dto = CreateStoryDto.from_dict(create_story_page)
    roles = ["main_role", "sup_role", "item"] # 定義角色列表
    # 初始化數據字典
    data = {f"{role}_{info}": "" for role in roles for info in ["id", "name", "info"]}
    data["original_story_content"] = ""
    # 檢查是否所有角色的 item_name 都有值
    all_roles_have_names = True # 初始化為 True
    # 用一個循環處理所有角色，避免代碼重複
    for role in roles:
        role_item = getattr(create_story_dto, role, None)
        if role_item:
            data[f"{role}_name"] = role_item.item_name
            data[f"{role}_id"] = role_item.item_id
            # 如果任一角色的 item_name 沒有值，更新標誌
            if not role_item.item_name:
                all_roles_have_names = False
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
    text_prompt = f'''您是一位在最吸引人、最受矚目、最熱門、最廣為討論且最值得推薦的童話故事作家，需要創作一個適合台灣地區 3 到 12 歲小朋友的童話故事。故事必須包含 1 個主角、1 個配角和 1 個道具，並按照以下要素進行故事創作：

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

請以您的專業經驗，根據以上指令直接創作出一個動人的童話故事，完美地結合上述的 1 個主角、1 個配角和 1 個道具，且充分發揮這三個元素的功能和特色，創作出新穎、有趣且完全不突兀的故事內容。'''
    return JsonResponse(
        {"text_prompt": text_prompt, "all_roles_have_names": all_roles_have_names}
    )

def loading_new(request):
    return render(request, "display/loading_new.html")

def get_cover_design_seed_value(item_name):
    try:
        item = Item.objects.filter(item_name=item_name).first()  # 使用 filter 取得第一個符合的對象
        if item:
            cover_design = CoverDesign.objects.filter(
                item_id=item.item_id
            ).first()  # 使用 filter 取得第一個符合的對象
            if cover_design:
                return cover_design.cover_design_seed_value
    except Item.DoesNotExist:
        pass
    except CoverDesign.DoesNotExist:
        pass
    return None

def generate_images_background(data):
    generated_image_paths = Queue() # 使用隊列存儲生成的圖片路徑
    threads = []
    for article in data["article_list"]:
        prompt, negative_prompt = gen_storyboard_desc_prompt(article)
        # 初始化種子值為配置中的默認值
        seed = int(config("SEED_VALUE"))
        # 檢查項目名稱出現的順序並選擇種子值
        positions = {
            "main_role": article.find(data["main_role_name"]),
            "sup_role": article.find(data["sup_role_name"]),
            "item": article.find(data["item_name"]),
        }
        # 過濾未找到的項目，即 find 方法返回 -1 的項目
        positions = {k: v for k, v in positions.items() if v != -1}
        # 如果有找到任何名稱，則按出現順序選擇種子值
        if positions:
            seed_name = min(positions, key=positions.get)
            seed = data.get(f"{seed_name}_seed")
            if seed is None:
                seed = int(config("SEED_VALUE"))
            print(f"{seed_name}_seed: {seed}")
        t = threading.Thread(
            target=create_image_from_prompt, args=(prompt, negative_prompt, seed, generated_image_paths)
        )
        threads.append(t)
        t.start()
        logging.info(f"Generated image for prompt: {prompt}")
    # 等待所有執行緒完成
    for t in threads:
        t.join()
    # 將隊列中的路徑取出放入列表中
    generated_image_paths_list = list(generated_image_paths.queue)
    return generated_image_paths_list # 返回生成的圖片路徑列表

def storybook_display_new(request):
    newstory = NewStory.objects.last()
    new_story_content = newstory.tw_new_story_content
    article_list = split_paragraphs(new_story_content)
    if article_list:
        create_story_page = request.session.get("create_story_page", {})
        main_role_name = create_story_page.get("main_role", {}).get("item_name")
        sup_role_name = create_story_page.get("sup_role", {}).get("item_name")
        item_name = create_story_page.get("item", {}).get("item_name")
        page_data = {
            "main_role_name": main_role_name,
            "main_role_seed": get_cover_design_seed_value(main_role_name),
            "sup_role_name": sup_role_name,
            "sup_role_seed": get_cover_design_seed_value(sup_role_name),
            "item_name": item_name,
            "item_seed": get_cover_design_seed_value(item_name),
            "article_list": article_list,
        }
        page_number = int(request.GET.get("page_number", 1))
        if page_number < 1:
            page_number = 1
        if page_number > len(article_list):
            page_number = len(article_list)
        generated_image_paths_list = generate_images_background(page_data)
        print(f"generated_image_paths_list: {generated_image_paths_list}")
        article_list_with_images = [
            {"text": paragraph, "image_path": os.path.join("\\", path)}
            for path, paragraph in zip(generated_image_paths_list, article_list)
        ]
        print(f"article_list_with_images: {article_list_with_images}")
        render_data = {
            "story_title": f'{page_data["main_role_name"]}和{page_data["sup_role_name"]}的童話故事',
            "page_number": page_number,
            "article_list": article_list_with_images,
            "article_list_json": json.dumps(article_list_with_images),
        }
        return render(request, "display/storybook_display_new.html", render_data)
    return render(request, "display/storybook_display_new.html", {"article_list": []})

def social_features_new(request):
    return render(request, "display/social_features_new.html")

def my_storybooks_new(request):
    return render(request, "display/my_storybooks_new.html")
