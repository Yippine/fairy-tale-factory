# chatgpt_api資訊
from openai import OpenAI

API_KEY = "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"
client = OpenAI(organization="org-BbuOFHuZiHsodlzbcmMNJlLp", api_key=API_KEY)

# 假故事資訊包
story_info = {
    "main_character_info": """主角名稱：夸父
 主角特徵：力大無窮
 主角性格：堅毅、慈悲""",
    "supporting_character_info": """配角名稱：醜小鴨
 配角特徵：一度被認為醜陋的外貌
 配角性格：堅毅、善良""",
    "props_info": """道具名稱：玫瑰
 道具功能：代表貝兒的願望，她在鄉下看不到玫瑰，所以希望父親帶回一支。""",
    "story_text": """故事發生的地點：大地
 故事背景敘述：太陽異常火熱，人們苦不堪言，祈求夸父的力量。夸父決定追逐太陽，調整天氣，為百姓帶來涼爽。他踏遍千山萬水，但太陽總是逃之夭夭。在追逐過程中，遇到無盡困難，但堅持不懈。最終，夸父倦怠犧牲，他的傳奇事蹟感動眾生，成為永恆的傳說。他的身軀、頭髮、血液都融入大自然，成為大地的一部分。夸父節紀念這位英雄。""",
}

# 用故事資訊生成全新內文
def gen_story_text(story_info):
    # 故事資訊生成指令
    text_prompt = gen_text_prompt(story_info)
    # 指令連接api生成新故事
    # story_text = call_chatgpt_api(text_prompt)
    story_text = ''
    return story_text

# 故事資訊生成指令包
def gen_text_prompt(story_info):
    text_prompt = f'''您是一位在台灣最吸引人、最受矚目、最熱門、最廣為討論且最值得推薦的童話故事作家，需要創作一個適合台灣地區 3 到 12 歲小朋友的童話故事。故事必須包含 1 個主角、1 個配角和 1 個道具，並按照以下要素進行故事創作：

一、主角資訊
{story_info["main_character_info"]}

二、配角資訊
{story_info["supporting_character_info"]}

三、道具資訊
{story_info["props_info"]}

四、故事範例
{story_info["story_text"]}

五、生成格式
"""【起】故事開頭，主角和配角的介紹，故事背景簡介。
【承】主角面臨挑戰或問題，展開情節，加入道具。
【轉】高潮部分，意想不到的情節發生，深刻的教訓浮現。
【合】結局，主角得到成長或改變，故事總結。
給我流暢的故事不要有任何註解,不要有起承轉合的字樣,
不要輸出:很高興為您創作一個適合 3 到 12 歲小朋友的童話故事。"""

六、故事要素
1. 創造力:故事情節要富有想像力。
2. 深刻的情感:主角和配角之間有情感連結，故事觸動人心。
3. 簡單而深刻的教訓:故事要傳達明確的價值觀或教訓。
4. 精彩的角色:主角和配角要有鮮明的性格。
5. 意想不到的情節:故事中要有令人驚喜的轉折。
6. 豐富的描述:場景和角色要有生動的描寫。
7. 流暢的文筆:故事要流暢易讀。
8. 現代感:故事要吸引當代年輕讀者。
9. 年齡適宜性:適合3到12歲的小朋友閱讀。
10. 教育性質:故事要有教育價值。
11. 文化連結:故事要具有台灣文化元素。
12. 趣味性:故事要引人入勝，讓小朋友喜歡閱讀。
13. 視覺元素:可以包括圖畫或插圖。
14. 情感連結:故事要觸動讀者的情感。
15. 啟發性:故事要啟發讀者思考。
16. 長度和結構:故事要遵循起承轉合結構，長度約360字左右。

請以您的專業經驗，根據以上指令創作一個動人的童話故事，完美地結合上述的 1 個主角、1 個配角和 1 個道具，且充分發揮這三個元素的功能和特色，創作出新穎、有趣且完全不突兀的故事內容。謝謝！'''
    return text_prompt

# 指令連接api生成新故事包
def call_chatgpt_api(text_prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"{text_prompt}"},
        ],
    )

    story_text = response.choices[0].message.content
    return story_text

if __name__ == "__main__":
    gen_story_text(story_info)
