import json
import os

def main():
    # 讓使用者輸入檔案名稱
    item_name = input("請輸入檔案名稱(不需要加.json): ")
    
    # 提供的範例文本
    text = text = """
    parameters

((best quality)),((masterpiece)),(detailed:1.4),
(CharacterSheet:1),(multiple views, full body, upper body, reference sheet:1),back view,front view,
(white backgeround, simple background:1.5),(twinkle smile:1.2),necklace,
((ghibli)),1 girl,(little girl:1.3),(short:1.3),green hair,flower wreath,pink dress,barefoot,
<lora:GoodHands-beta2:1>,
<lora:CharacterDesign_Concept-10:0.8>,
Negative prompt: (worst quality, low quality:1.4),monochrome,lowres,bad anatomy,bad hands,text,error,missing fingers,extra digit,fewer digits,cropped,worst quality,low quality,normal quality,jpeg artifacts,((signature)),watermark,username,blurry,deformed eyes,((disfigured)),bad art,deformed,((extra limbs)),((duplicate)),morbid,multilated,bad body,one hand with less than 5 fingers,stacked torses,stacked hands,totem pole,((text)),
Steps: 60, Sampler: DPM++ 2M Karras, CFG scale: 7, Seed: 1053580445, Size: 1080x720, Model hash: a85383c15e, Model: sdvn8Art_ghibli, Clip skip: 2, Token merging ratio: 0.5, Lora hashes: "GoodHands-beta2: c05ed279295e, CharacterDesign_Concept-10: 6f65857a23ad", Version: v1.7.0


    """
    
    # 解析文本並轉換為JSON格式
    json_data = parse_text_to_json(text)

    # 讓使用者輸入item_name
    json_file_name = item_name + '_' + str(json_data["cover_design_id"]) + '.json'
    json_data["item_name"] = item_name

    # 儲存為JSON檔案
    save_to_json(json_data, json_data["item_name"], json_file_name)
    print(f"檔案已儲存至資料夾 {json_data['item_name']} 下的 {json_file_name}")

def parse_text_to_json(text):
    # 將文字分割成不同部分
    parts = text.split("Steps:")[0].split("Negative prompt:")
    positive_prompt = parts[0].strip()
    negative_prompt_parts = parts[1].strip().split("Model hash:")
    negative_prompt = negative_prompt_parts[0].strip()

    # 初始化變量
    seed_value = 0
    model = ""
    lora_hashes = ""

    # 檢查並提取Model相關信息
    model_info_parts = text.split("Model:")
    if len(model_info_parts) > 1:
        model_info = model_info_parts[1].split(",")[0].strip()
        model = model_info.split(",")[0].strip()

    # 檢查並提取Lora hashes相關信息
    lora_info_parts = text.split('Lora hashes: "')
    if len(lora_info_parts) > 1:
        lora_hashes = lora_info_parts[1].split('"')[0].strip()

    # 檢查並提取Seed值
    seed_parts = text.split("Seed:")
    if len(seed_parts) > 1:
        seed_value = int(seed_parts[1].split(",")[0].strip())

    return {
        "item_name": "",
        "cover_design_id": 1,
        "cover_design_model": model,
        "cover_design_lora": lora_hashes,
        "cover_design_positive_prompt": positive_prompt,
        "cover_design_negative_prompt": negative_prompt,
        "cover_design_seed_value": seed_value,
        "cover_design_link": ""
    }


def save_to_json(data, folder_name, filename):
    # 檢查資料夾是否存在，如果不存在則創建
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # 構建完整的檔案路徑
    file_path = os.path.join(folder_name, filename)

    # 儲存JSON檔案
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
