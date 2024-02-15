import json

class ItemDTO:
    def __init__(self, item_id="", item_name="", cover_design_link=""):
        self.item_id = item_id
        self.item_name = item_name
        self.cover_design_link = cover_design_link

    def to_dict(self):
        return {
            "item_id": self.item_id,
            "item_name": self.item_name,
            "cover_design_link": self.cover_design_link,
        }

    @staticmethod
    def from_dict(data):
        return ItemDTO(
            item_id=data.get("item_id", ""),
            item_name=data.get("item_name", ""),
            cover_design_link=data.get("cover_design_link", ""),
        )

class SelectItemDto:
    def __init__(self, item_page="", item=ItemDTO()):
        self.item_page = item_page
        self.item = item

    def to_dict(self):
        return {
            "item_page": self.item_page,
            **self.item.to_dict(),
        }

    @staticmethod
    def from_dict(data):
        item = ItemDTO.from_dict(data)
        return SelectItemDto(item_page=data.get("item_page", ""), item=item)

class CreateStoryDto:
    def __init__(self, main_role=ItemDTO(), sup_role=ItemDTO(), item=ItemDTO()):
        self.main_role = main_role
        self.sup_role = sup_role
        self.item = item

    def to_dict(self):
        return {
            "main_role": self.main_role.to_dict(),
            "sup_role": self.sup_role.to_dict(),
            "item": self.item.to_dict(),
        }

    @staticmethod
    def from_dict(data):
        return CreateStoryDto(
            main_role=ItemDTO.from_dict(data.get("main_role", {})),
            sup_role=ItemDTO.from_dict(data.get("sup_role", {})),
            item=ItemDTO.from_dict(data.get("item", {})),
        )

if __name__ == "__main__":
    # Test data
    select_item_dict = {
        "item_page": "example.com",
        "item_id": "1",
        "item_name": "Main Role",
        "cover_design_link": "main_role_cover.jpg",
    }
    create_story_dict = {
        "main_role": {
            "item_id": "1",
            "item_name": "Main Role",
            "cover_design_link": "main_role_cover.jpg",
        },
        "sup_role": {
            "item_id": "2",
            "item_name": "Sup Role",
            "cover_design_link": "sup_role_cover.jpg",
        },
        "item": {
            "item_id": "3",
            "item_name": "Item",
            "cover_design_link": "item_cover.jpg",
        },
        "item_page": "example.com",
    }

    # Testing from_dict method
    select_item_dto = SelectItemDto.from_dict(select_item_dict)
    create_story_dto = CreateStoryDto.from_dict(create_story_dict)

    print("Testing from_dict method:")
    print("SelectItemDto:")
    print(select_item_dto.to_dict())
    print("CreateStoryDto:")
    print(create_story_dto.to_dict())
    print()

    # Testing to_dict method
    select_item_dto = SelectItemDto(
        item_page="example.com",
        item=ItemDTO(
            item_id="1", item_name="Main Role", cover_design_link="main_role_cover.jpg"
        ),
    )
    create_story_dto = CreateStoryDto(
        main_role=ItemDTO(
            item_id="1", item_name="Main Role", cover_design_link="main_role_cover.jpg"
        ),
        sup_role=ItemDTO(
            item_id="2", item_name="Sup Role", cover_design_link="sup_role_cover.jpg"
        ),
        item=ItemDTO(item_id="3", item_name="Item", cover_design_link="item_cover.jpg"),
    )

    print("Testing to_dict method:")
    print("SelectItemDto:")
    print(select_item_dto.to_dict())
    print("CreateStoryDto:")
    print(create_story_dto.to_dict())
