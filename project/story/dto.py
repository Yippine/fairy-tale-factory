import json

class SelectItemDTO:
    def __init__(self, item_page="", main_role={}, sup_role={}, item={}):
        self.item_page = item_page
        self.story_info = self.StoryInfoDTO(main_role, sup_role, item)

    @staticmethod
    def from_dict(json_dict):
        if json_dict is None:
            return SelectItemDTO()
        story_info = json_dict.get("story_info", {})
        return SelectItemDTO(
            item_page=json_dict.get("item_page", ""),
            main_role=story_info.get("main_role", {}),
            sup_role=story_info.get("sup_role", {}),
            item=story_info.get("item", {}),
        )

    def to_dict(self):
        return {
            "item_page": self.item_page,
            "story_info": self.story_info.to_dict(),
        }

    class StoryInfoDTO:
        def __init__(self, main_role={}, sup_role={}, item={}):
            self.main_role = SelectItemDTO.ItemDTO(**main_role)
            self.sup_role = SelectItemDTO.ItemDTO(**sup_role)
            self.item = SelectItemDTO.ItemDTO(**item)
        
        def to_dict(self):
            return {
                "main_role": self.main_role.to_dict(),
                "sup_role": self.sup_role.to_dict(),
                "item": self.item.to_dict(),
            }

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

if __name__ == "__main__":
    ################ 方法一：透過 dict 定義 SelectItemDTO ################
    json_dict = {
        "item_page": "examplePage",
        "story_info": {
            "main_role": {
                "item_id": "1",
                "item_name": "Main Character",
                "cover_design_link": "/images/main.png"
            },
            "sup_role": {
                "item_id": "2",
                "item_name": "Supporting Character",
                "cover_design_link": "/images/support.png"
            },
            "item": {
                "item_id": "3",
                "item_name": "Magic Sword",
                "cover_design_link": "/images/item.png"
            }
        }
    }
    dto = SelectItemDTO.from_dict(json_dict)
    print(dto.story_info.main_role.item_name)

    ################ 方法二：自行定義 ################
    # 初始化一個空的 SelectItemDTO
    dto = SelectItemDTO()

    # 單獨賦值 item_page
    dto.item_page = "newitem_page"

    # 為 main_role 的 name 賦值前，確保 main_role 已經是 ItemDTO 的實例
    # 如果在初始化時 main_role 沒有被賦值，您可以先創建一個 ItemDTO 實例
    dto.story_info.main_role = SelectItemDTO.ItemDTO()

    # 現在可以安全地為 main_role 的 name 賦值了
    dto.story_info.main_role.item_name = "New Main Character Name"

    # 檢查賦值結果
    print(dto.item_page)  # 輸出: newitem_page
    print(dto.story_info.main_role.item_name)  # 輸出: New Main Character Name
