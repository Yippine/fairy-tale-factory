from story.models import Item
from story.dto import ItemDTO, SelectItemDto, CreateStoryDto

def get_select_item_page(request):
    select_item_page = request.session.get("select_item_page", {})
    if not select_item_page:
        select_item_page = SelectItemDto(item_page="", item_page_text="", item=ItemDTO()).to_dict()
        request.session["select_item_page"] = select_item_page
    return select_item_page

def get_create_story_page(request):
    create_story_page = request.session.get("create_story_page", {})
    if not create_story_page:
        create_story_page = CreateStoryDto(
            main_role=ItemDTO(), sup_role=ItemDTO(), item=ItemDTO()
        ).to_dict()
        request.session["create_story_page"] = create_story_page
    return create_story_page

def get_role_info_by_role_item(role_item):
    """
    根據角色和角色物品，返回角色資訊。

    Parameters:
        role_item (object): 包含角色物品資訊的物件。
        role (str): 角色名稱。

    Returns:
        str: 角色資訊。
    """
    item = Item.objects.filter(item_id=role_item.item_id).values('item_id', 'item_info').first()
    return item.get('item_info', '')

def get_original_story_content(role_item, role):
    """
    從資料庫中檢索角色物品的原始故事內容。

    Args:
        role_item: 角色的物品。
        role: 角色的名稱。

    Returns:
        dict: 包含原始故事內容的字典。如果找不到故事或故事內容，則返回空字典。
    """
    original_story_content = ""
    
    return original_story_content
