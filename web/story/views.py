import os, re, json, threading, logging
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .dto import CreateStoryDto
from .models import CoverDesign, Item, OriginalStory, NewStory
from .utils.dto_utils import get_select_item_page, get_create_story_page
from .utils.common_utils import split_paragraphs
from .utils.create_new_text import gen_story_text
from .utils.sdxl_api import create_image_from_prompt
from .utils.create_prompt import create_prompt
from queue import Queue

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
    create_story_page = request.session.get("create_story_page", {})
    main_role_name = create_story_page.get("main_role", {}).get("item_name")
    sup_role_name = create_story_page.get("sup_role", {}).get("item_name")
    item_name = create_story_page.get("item", {}).get("item_name")
    if main_role_name and sup_role_name and item_name:
        main_role_detail = Item.objects.filter(item_name=main_role_name).values('item_info').first()
        sup_role_detail = Item.objects.filter(item_name=sup_role_name).values('item_info').first()
        item_detail = Item.objects.filter(item_name=item_name).values('item_info').first()
        orm_story = OriginalStory.objects.filter(original_story_name=create_story_page.get("main_role", {}).get("item_name")).values('original_story_content')
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
        # story_text = gen_story_text(story_info)
        # generated_story = NewStory(tw_new_story_content=story_text)
        # generated_story.save()
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
    # try:
    #     item_name = request.GET.get("item_name")
    #     item = Item.objects.get(item_name=item_name)
    #     cover_design = CoverDesign.objects.get(item_id=item.item_id, cover_design_id=0)
    #     cover_design_link = cover_design.cover_design_link
    # except (Item.DoesNotExist, CoverDesign.DoesNotExist):
    #     cover_design_link = None
    # return JsonResponse({"cover_design_link": cover_design_link})

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

def generate_images_background(article_list, seed):
    generated_image_paths = Queue()  # 使用队列存储生成的图片路径
    threads = []
    for article in article_list:
        prompt = create_prompt(article)
        t = threading.Thread(target=create_image_from_prompt, args=(prompt, seed, generated_image_paths))
        threads.append(t)
        t.start()
        logging.info(f"Generated image for prompt: {prompt}")
    # 等待所有线程完成
    for t in threads:
        t.join()
    
    # 将队列中的路径取出放入列表中
    generated_image_paths_list = list(generated_image_paths.queue)
    
    return generated_image_paths_list  # 返回生成的图片路径列表

def storybook_display_new(request):
    # newstory = NewStory.objects.last()
    # new_story_content = newstory.tw_new_story_content
    # article_list = split_paragraphs(new_story_content)
    article_list = []
    if article_list:
        page_number = int(request.GET.get("page_number", 1))
        if page_number < 1:
            page_number = 1
        if page_number > len(article_list):
            page_number = len(article_list)
        current_article = article_list[page_number - 1]
        
        # 生成图片并获取生成的图片路径列表
        generated_image_paths_list = generate_images_background(article_list, 2751417741)
        print(generated_image_paths_list)
        # 构建 article_list_with_images
        article_list_with_images = [{"text": paragraph, "image_path": os.path.join('\\', path)} for path, paragraph in zip(generated_image_paths_list, article_list)]
        article_list_json = json.dumps(article_list_with_images)
        print(article_list_with_images)
        # 返回快速渲染的页面
        return render(
            request,
            "display/storybook_display_new.html",
            {
                "article_list": article_list_with_images,
                "page_number": page_number,
                "article_list_json": article_list_json,
            },
        )
    return render(request, "display/storybook_display_new.html", {"article_list": []})



def social_features_new(request):
    return render(request, "display/social_features_new.html")

def my_storybooks_new(request):
    return render(request, "display/my_storybooks_new.html")
