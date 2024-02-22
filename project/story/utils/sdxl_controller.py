import os
import io
import warnings
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
import deepl
from datetime import datetime
import re

STEPS = 50
SAMPLES = 1
WIDTH = 1024
HEIGHT = 1024

def generate_story_image(story_content: str):
    """依照新故事內容生成故事圖片"""
    # 示範代碼 - 將故事內容轉換成圖片
    translated_story = translate_story_to_en(story_content)
    create_image_from_story(translated_story)

def translate_story_to_en(story_content: str) -> str:
    """將新故事內容翻譯成英文"""
    # 示範代碼 - 翻譯故事內容
    auth_key = "41859e07-ba78-461b-b0dd-e95bf7d6fc87:fx"
    translator = deepl.Translator(auth_key)
    en_story_content = translator.translate_text(story_content, target_lang="EN-US")
    return en_story_content

def create_image_from_story(en_story_content: str) -> object:
    """串接 SDXL API 生成圖片"""
    # 示範代碼 - 串接SDXL API
    os.environ["STABILITY_HOST"] = "grpc.stability.ai:443"
    os.environ["STABILITY_KEY"] = "sk-3dZtO5r3cmr27DnU0JSpp2GBvOJnkNfQrSKSe6e4GjC2SrkM"
    stability_api = client.StabilityInference(
        key=os.environ["STABILITY_KEY"],
        verbose=True,
        engine="stable-diffusion-xl-1024-v1-0",
    )
    answers = stability_api.generate(
        prompt=f"{en_story_content}",
        steps=STEPS,  # Amount of inference steps performed on image generation. Defaults to 30.
        cfg_scale=8.0,  # Influences how strongly your generation is guided to match your prompt.
        # Setting this value higher increases the strength in which it tries to match your prompt.
        # Defaults to 7.0 if not specified.
        width=WIDTH,  # Generation width, defaults to 512 if not included.
        height=HEIGHT,  # Generation height, defaults to 512 if not included.
        samples=SAMPLES,  # Number of images to generate, defaults to 1 if not included.
        sampler=generation.SAMPLER_K_DPMPP_2M,  # (Available Samplers: ddim, plms, k_euler, k_euler_ancestral, k_heun, k_dpm_2, k_dpm_2_ancestral, k_dpmpp_2s_ancestral, k_lms, k_dpmpp_2m, k_dpmpp_sde)
    )
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                warnings.warn(
                    "Your request activated the API's safety filters and could not be processed."
                    "Please modify the prompt and try again."
                )
            if artifact.type == generation.ARTIFACT_IMAGE:
                image = Image.open(io.BytesIO(artifact.binary))
                timestamp = re.sub(
                    r"[^a-zA-Z0-9]", "-", datetime.now().strftime("%Y%m%d%H%M%S")
                )
                filepath = r"static/img/stories"
                file = os.path.join(filepath, timestamp + ".png")
                image.save(file)
