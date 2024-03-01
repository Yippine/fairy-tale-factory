# chatgpt_api資訊
from openai import OpenAI
from decouple import config

client = OpenAI(organization=config("OPENAI_ORGANIZATION"), api_key=config("OPENAI_API_KEY"))

def gen_storyboard_desc_prompt(article):
    desc_prompt = f'''你是 AI 繪圖領域的專家，已經深耕此領域數十年。請你幫我描繪符合使用者描述的場景，讓觀眾沉浸其中，透過 AI 繪圖呈現最吸引人、最熱門、最廣為討論且最值得推薦的情境。這段場景描述必須使用美國本土的英語文法和詞彙，並呈現出觀眾心目中最完美的分鏡描述。

使用者描述如下："""{article}"""'''
    positive_prompt = call_chatgpt_api(desc_prompt)
    negative_prompt = '''Artwork of low, average, or poor quality, with low resolution, grainy, or imperfect images. The artist's signature or trademark elements may be present, but there may be issues or errors with the artwork, such as missing or extra digits, or strange colors.

Some images have poor quality and may feature disfigured or mutated body parts, including the head, face, five senses, lips, teeth, neck, limbs, arms, elbows, palms, fists, fingers, nails, legs, feet, and genitalia of both sexes. The artwork shows a mutated arm, disproportionate body, missing/disconnected body parts, unattractive face/features, glowing eyes, droopy pointed ears, plastic hair, dark skin/long neck, weird lines/folds, disturbing body/limbs, extra body part, cloned face, abnormal features, big nose, (nipples: 1.2), Changed arms, changed hands, changed fists, some fists, incorrect hands for fists, changed fingers, missing fingers, no thumb or finger in the right place, four fingers and one thumb on each hand, different sized fingers, fingers overlapping, fingers fused together, messy fingers, unclear visuals, blurry, cut off, not shown, shown in different angles, or repeated images.

The artwork also suffers from poor quality and distracting backgrounds.'''
    return positive_prompt, negative_prompt

def call_chatgpt_api(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
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

def call_chatgpt_api_by_json(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
            {"role": "user", "content": f"{prompt}"},
        ],
        response_format={"type": "json_object"},
        temperature=0.7,
        max_tokens=1500,
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
    print(f'positive_prompt: {positive_prompt}')
    print(f'negative_prompt: {negative_prompt}')
