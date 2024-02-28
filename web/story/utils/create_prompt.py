from openai import OpenAI
API_KEY = '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'
client = OpenAI(organization = 'org-BbuOFHuZiHsodlzbcmMNJlLp', api_key=API_KEY)
article = '一天晚上，當他們正準備啟程時，突然出現了一群兇猛的海盜，他們的領袖就是虎克船長。'

def create_prompt(article):
    prompt = gen_prompt(article)
    # gpt_response = call_chatgpt_api(prompt)
    gpt_response = ''
    if ":" in gpt_response:
        prompt_result = gpt_response.split(":")[1].strip()
        return prompt_result

def gen_prompt(article):
    prompt = f'''請根據以下文本,幫我生成用於使用AI生圖工具的英文prompt
    ,{article},
    並以以下格式生成。
    prompt:英文prompt'''
    return prompt

def call_chatgpt_api(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{prompt}"},
        ]
    )   

    gpt_response = response.choices[0].message.content
    return gpt_response


create_prompt(article)
