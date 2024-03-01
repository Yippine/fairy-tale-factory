# chatgpt_api資訊
from openai import OpenAI
from decouple import config

client = OpenAI(organization=config("OPENAI_ORGANIZATION"), api_key=config("OPENAI_API_KEY"))

def gen_storyboard_desc_prompt(article):
    desc_prompt = f'''You're an expert in the AI painting prompt domain, having delved deep into it for decades. Can you help me paint a scene by Studio Ghibli style that fits the user's description, immersing the audience in it? Present the most captivating, trending, talked-about, and recommendable scenario through AI-generated imagery. This scene description should be concise, not exceeding three times the length of the article provided by user.

User Description:"""{article}"""'''
    gpt_response = gen_storyboard_desc_by_chatgpt(desc_prompt)
    positive_prompt = (
        "((best quality)),((masterpiece)),(detailed:1.4),(ghibli: 1.75),(clear and distinct face features: 1.75),\n"
        + gpt_response
        + "\n<lora:GoodHands-beta2:1>,<lora:CharacterDesign_Concept-10:0.8>,<lora:add_detail:0.6>,<lora:lightAndShadow_v10:0.6>,"
    )
    negative_prompt = '''Artwork of low, average, or poor quality, with low resolution, grainy, or imperfect images. The artist's signature or trademark elements may be present, but there may be issues or errors with the artwork, such as missing or extra digits, or strange colors.

Some images have poor quality and may feature disfigured or mutated body parts, including the head, face, five senses, lips, teeth, neck, limbs, arms, elbows, palms, fists, fingers, nails, legs, feet, and genitalia of both sexes. The artwork shows a mutated arm, disproportionate body, missing/disconnected body parts, unattractive face/features, glowing eyes, droopy pointed ears, plastic hair, dark skin/long neck, weird lines/folds, disturbing body/limbs, extra body part, cloned face, abnormal features, big nose, (nipples: 1.2), Changed arms, changed hands, changed fists, some fists, incorrect hands for fists, changed fingers, missing fingers, no thumb or finger in the right place, four fingers and one thumb on each hand, different sized fingers, fingers overlapping, fingers fused together, messy fingers, unclear visuals, blurry, cut off, not shown, shown in different angles, or repeated images.

The artwork also suffers from poor quality and distracting backgrounds.'''
    return positive_prompt, negative_prompt

def gen_storyboard_desc_by_chatgpt(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {
                "role": "system",
                "content": "You're an expert in the field of AI painting prompts.",
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
    print(f'positive_prompt: {positive_prompt}')
    print(f'negative_prompt: {negative_prompt}')
