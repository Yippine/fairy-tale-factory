import os
import json
from django.conf import settings
from django.utils import timezone
from story.models import CoverDesign, Item

def fetch_and_store_json_info():
    json_dir = os.path.join(settings.BASE_DIR, "story/static/json")
    for filename in os.listdir(json_dir):
        if filename.endswith(".json"):
            with open(os.path.join(json_dir, filename), "r", encoding="utf-8") as file:
                data = json.load(file)
                item_name = data.get("item_name")
                item_type = data.get("item_type") # 假設可以從JSON檔案取得item_type
                # 尋找或新增 item 並取得 item_id，確保提供所有必填字段
                item, _ = Item.objects.get_or_create(
                    item_name=item_name,
                    defaults={"item_type": item_type}, # 提供item_type值
                )
                # 儲存或更新 cover_design 記錄
                CoverDesign.objects.update_or_create(
                    item=item, # 使用 item 物件而不是 item_id
                    cover_design_id=data.get("cover_design_id"),
                    defaults={
                        "cover_design_model": data.get("cover_design_model"),
                        "cover_design_lora": data.get("cover_design_lora"),
                        "cover_design_positive_prompt": data.get(
                            "cover_design_positive_prompt"
                        ),
                        "cover_design_negative_prompt": data.get(
                            "cover_design_negative_prompt"
                        ),
                        "cover_design_seed_value": data.get("cover_design_seed_value"),
                        "cover_design_link": data.get("cover_design_link"),
                        "creation_time": timezone.now(),
                        "modification_time": timezone.now(),
                    },
                )

if __name__ == "__main__":
    fetch_and_store_json_info()
