import os, json
from django.core.management.base import BaseCommand
from django.conf import settings
from utils.common_utils import clear_directory

class Command(BaseCommand):
    help = "Generate and update cover design JSON files based on cover_design_link.json"

    def handle(self, *args, **kwargs):
        cover_design_link_file = os.path.join(
            settings.BASE_DIR,
            "story/static/json/data",
            "cover_design_link.json",
        )
        origin_dir = os.path.join(settings.BASE_DIR, "story/static/json/original")
        generated_dir = os.path.join(settings.BASE_DIR, "story/static/json/generated")
        if not os.path.exists(generated_dir):
            os.makedirs(generated_dir)

        with open(cover_design_link_file, "r", encoding="utf-8") as file:
            cover_design_links = json.load(file)

        cover_design_map = {
            item["item_name"]
            + "_"
            + str(item["cover_design_id"]): item["cover_design_link"]
            for item in cover_design_links
        }

        origin_files = {}
        for filename in os.listdir(origin_dir):
            if filename.endswith(".json"):
                item_name, cover_design_id = os.path.splitext(filename)[0].rsplit(
                    "_", 1
                )
                if item_name not in origin_files:
                    origin_files[item_name] = []
                origin_files[item_name].append((int(cover_design_id), filename))

        # clear_directory(generated_dir)
        
        for item_name, files in origin_files.items():
            files.sort(key=lambda x: x[0])
            _, last_file_name = files[-1]

            with open(
                os.path.join(origin_dir, last_file_name), "r", encoding="utf-8"
            ) as file:
                last_file_data = json.load(file)

            for key, link in cover_design_map.items():
                if item_name in key:
                    _, cover_design_id = key.rsplit("_", 1)
                    new_file_name = f"{item_name}_{cover_design_id}.json"
                    new_file_data = last_file_data.copy()
                    new_file_data["cover_design_id"] = int(cover_design_id)
                    new_file_data["cover_design_link"] = link

                    with open(
                        os.path.join(generated_dir, new_file_name),
                        "w",
                        encoding="utf-8",
                    ) as outfile:
                        json.dump(new_file_data, outfile, indent=4, ensure_ascii=False)

        for key, link in cover_design_map.items():
            if not os.path.exists(os.path.join(generated_dir, key + ".json")):
                item_name, cover_design_id = key.rsplit("_", 1)
                new_file_data = {
                    "item_name": item_name,
                    "item_type": -1,
                    "cover_design_id": int(cover_design_id),
                    "cover_design_model": "",
                    "cover_design_lora": "",
                    "cover_design_positive_prompt": "",
                    "cover_design_negative_prompt": "",
                    # "cover_design_seed_value": -1,
                    "cover_design_link": link,
                }
                with open(os.path.join(generated_dir, key + ".json"), "w", encoding="utf-8") as outfile:
                    json.dump(new_file_data, outfile, indent=4, ensure_ascii=False)

        self.stdout.write(
            self.style.SUCCESS("Successfully processed and generated JSON files.")
        )
