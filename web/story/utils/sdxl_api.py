import os, io, warnings, threading, time
from datetime import datetime
from queue import Queue

from PIL import Image
from decouple import config
from stability_sdk import client
from stability_sdk.interfaces.gooseai.generation import generation_pb2 as generation

# 您應該將這些常數替換為您設定中的實際值
STEPS = 20 # 擴散步驟數
SAMPLES = 1 # 要產生的影像數量
WIDTH = 1024 # 產生影像的寬度
HEIGHT = 1024 # 產生影像的高度
CFG_SCALE = 7 # 提示中使用的 CFG 比例
SAMPLER = generation.SAMPLER_K_EULER_ANCESTRAL # 產生中使用的取樣器

def create_image_from_prompt(
    prompt: str, negative_prompt: str, seed: int, generated_image_paths: Queue
) -> None:
    os.environ["STABILITY_HOST"] = config("STABILITY_HOST")
    os.environ["STABILITY_KEY"] = config("STABILITY_KEY")
    stability_api = client.StabilityInference(
        key=os.environ["STABILITY_KEY"],
        verbose=True,
        engine="stable-diffusion-xl-1024-v1-0",
    )
    answers = stability_api.generate(
        prompt=[
            generation.Prompt(
                text=prompt, parameters=generation.PromptParameters(weight=1)
            ),
            generation.Prompt(
                text=negative_prompt, parameters=generation.PromptParameters(weight=-1)
            ),
        ],
        seed=seed,
        steps=STEPS,
        cfg_scale=CFG_SCALE,
        width=WIDTH,
        height=HEIGHT,
        samples=SAMPLES,
        sampler=SAMPLER,
    )
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                warnings.warn(
                    "Your request activated the API's safety filters and could not be processed."
                    "Please modify the prompt and try again."
                )
            if artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary))
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                file_name = f"{timestamp}.png" # 使用時間戳記命名文件
                media_folder = "media"
                if not os.path.exists(media_folder):
                    os.makedirs(media_folder)
                file_path = os.path.join(media_folder, file_name)
                img.save(file_path)
                generated_image_paths.put(file_path)
                threading.Thread(
                    target=delete_after_10_minutes, args=(file_path,), daemon=True
                ).start()
                return file_path # 傳回產生影像的路徑

def delete_after_10_minutes(file_path: str) -> None:
    # 函式將在10分鐘後刪除圖像文件
    time.sleep(600)
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted {file_path} after 10 minutes.")
