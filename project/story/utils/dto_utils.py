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
