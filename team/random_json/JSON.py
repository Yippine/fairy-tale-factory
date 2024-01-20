import json
import random
import os
def random_json():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_json_path = os.path.join(current_dir, 'DATA.json')
    item_json_path = os.path.join(current_dir, 'ITEM.json')
    extract_random_article(data_json_path)
    extract_random_item(item_json_path)
def extract_random_article(json_file_path): 
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    random_key = random.choice(list(data.keys()))
    other_values = list(data.values())
    other_values.remove(data[random_key])
    random_value = random.choice(other_values)

    print(random_key, random_value)

def extract_random_item(json_file_path_item):
    with open(json_file_path_item, 'r', encoding='utf-8') as file:
        data = json.load(file)
    random_key = random.choice(list(data.keys()))
    value = data[random_key]
    print(random_key, value)

random_json()