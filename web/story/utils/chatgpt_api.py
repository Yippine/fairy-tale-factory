# chatgpt_api資訊
from openai import OpenAI
from decouple import config

client = OpenAI(organization=config("OPENAI_ORGANIZATION"), api_key=config("OPENAI_API_KEY"))

def check_storyboard_desc_prompt(prompt, article):
    # 檢查提示是否以 " 或 ' 開頭或結尾
    if prompt.startswith('"') or prompt.startswith("'"):
        prompt = prompt[1:]
    if prompt.endswith('"') or prompt.endswith("'"):
        prompt = prompt[:-1]
    # 檢查提示是否包含「抱歉」，並將其替換為原故事內容
    print(f'【prompt】{prompt}')
    if "sorry" in prompt.lower():
        prompt = article
        print('【warn】Prompt 未正確生成，替換回原故事內容。')
    print()
    return prompt

def gen_storyboard_desc_prompt(article):
    desc_prompt = f'''When faced with user-provided story content, adhere to the following structure to create Stable Diffusion image prompts:

1. Subject and Action Description: Select the core characters or objects from the story and describe their expressions and actions.
2. Setting and Background: Determine the environmental setting of the image, such as indoor, outdoor, or specific scenes.
3. Image Type and Art Style: Specify the type of image (digital illustration, comic cover) and the artistic style (e.g., Ghibli).
4. Details and Rendering Information: Include information about lighting, camera angle, rendering style, resolution, and level of detail.

Please provide drawing instructions suitable for Stable Diffusion directly. Below are examples in the format for your reference:
"Miyazaki-style forest explorer, digital illustration, inspired by Ghibli, wide shot, natural twilight lighting, (detail: 1.5), (forest background: 1.25), (adventure atmosphere: 1.3), (animation texture: 1.4)"
"Fantasy floating castle, photo style, inspired by Miyazaki and Rutkowski's art, 35mm lens, high angle view, (HDR lighting: 1.25), (surreal colors: 1.5), (detailed clouds: 1.2), (dreamy atmosphere: 1.4)"
"Robot and boy's friendship, comic cover, abstract expressionism, Marat Safin style, mid shot, studio lighting, (warm tones: 1.25), (refined shadows: 1.3), (storyline: 1.4), (nostalgic feel: 1.2)"

Key points to note:
Please create high-quality Stable Diffusion image prompts directly with keywords describing the framing of the scene in the Ghibli style for the various story contents provided by the user, following the above guidelines. Without providing any additional context or supplementary explanatory information. Please respond using American vocabulary and grammar.

The story content provided by the user:"""{article}"""'''
    gpt_response = gen_storyboard_desc_by_chatgpt(desc_prompt)
    print(f'\n【article】{article}')
    gpt_response = check_storyboard_desc_prompt(gpt_response, article)
    positive_prompt = (
        # "((best quality)),((masterpiece)),(detailed:1.4),(ghibli: 1.75),(clear and distinct face features: 1.75),\n"
        "((best quality)),((masterpiece)),(detailed:1.4),(ghibli: 1.75),(detaied face: 1.75),(perfect face: 1.75),(full body: 1.5),\n"
        + gpt_response
        + "\n<lora:GoodHands-beta2:1>,<lora:CharacterDesign_Concept-10:0.5>,<lora:add_detail:0.6>,<lora:lightAndShadow_v10:0.6>,"
    )
#     negative_prompt = '''Artwork of low, average, or poor quality, with low resolution, grainy, or imperfect images. The artist's signature or trademark elements may be present, but there may be issues or errors with the artwork, such as missing or extra digits, or strange colors.

# Some images have poor quality and may feature disfigured or mutated body parts, including the head, face, five senses, lips, teeth, neck, limbs, arms, elbows, palms, fists, fingers, nails, legs, feet, and genitalia of both sexes. The artwork shows a mutated arm, disproportionate body, missing/disconnected body parts, unattractive face/features, glowing eyes, droopy pointed ears, plastic hair, dark skin/long neck, weird lines/folds, disturbing body/limbs, extra body part, cloned face, abnormal features, big nose, (nipples: 1.2), Changed arms, changed hands, changed fists, some fists, incorrect hands for fists, changed fingers, missing fingers, no thumb or finger in the right place, four fingers and one thumb on each hand, different sized fingers, fingers overlapping, fingers fused together, messy fingers, unclear visuals, blurry, cut off, not shown, shown in different angles, or repeated images.

# The artwork also suffers from poor quality and distracting backgrounds.'''
    negative_prompt = '''(worst quality, low quality:1.4),monochrome,lowres,bad anatomy,bad hands,text,error,missing fingers,extra digit,fewer digits,cropped,worst quality,low quality,normal quality,jpeg artifacts,((signature)),watermark,username,blurry,deformed eyes,((disfigured)),bad art,deformed,((extra limbs)),((duplicate)),morbid,multilated,bad body,one hand with less than 5 fingers,stacked torses,stacked hands,totem pole,((text)),'''
    return positive_prompt, negative_prompt

def gen_storyboard_desc_by_chatgpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {
                "role": "system",
                "content": "You're a master of AI illustration in the style of Studio Ghibli and an expert in the field of AI painting prompts.",
            },
            {"role": "user", "content": f"{prompt}"},
        ],
        temperature=0.7,
        max_tokens=1500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    gpt_response = response.choices[0].message.content
    return gpt_response

def gen_story_by_chatgpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
            {"role": "user", "content": f"{prompt}"},
        ],
        response_format={"type": "json_object"},
        temperature=0.7,
        # max_tokens=1500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["故事結束。"], # 終止符，可根據需要調整
    )
    gpt_response = response.choices[0].message.content
    return gpt_response

if __name__ == "__main__":
    article = "一天晚上，當他們正準備啟程時，突然出現了一群兇猛的海盜，他們的領袖就是虎克船長。"
    positive_prompt, negative_prompt = gen_storyboard_desc_prompt(article)
    print(f'【positive_prompt】{positive_prompt}\n')
    print(f'【negative_prompt】{negative_prompt}')
