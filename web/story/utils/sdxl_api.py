import os, io, warnings, threading
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
import time
from datetime import datetime
from queue import Queue
from decouple import config

STEPS = 50
SAMPLES = 1
WIDTH = 1024
HEIGHT = 1024

def create_image_from_prompt(
    prompt: str, seed: int, generated_image_paths: Queue
) -> None:
    os.environ["STABILITY_HOST"] = config("STABILITY_HOST")
    os.environ["STABILITY_KEY"] = config("STABILITY_KEY")
    stability_api = client.StabilityInference(
        key=os.environ["STABILITY_KEY"],
        verbose=True,
        engine="stable-diffusion-xl-1024-v1-0",
    )
    answers = stability_api.generate(
        prompt=prompt,
        seed=seed,
        steps=STEPS,
        cfg_scale=8.0,
        width=WIDTH,
        height=HEIGHT,
        samples=SAMPLES,
        sampler=generation.SAMPLER_K_DPMPP_2M,
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
                file_name = f"{timestamp}.png" # 使用傳入的 seed 參數建立檔案名
                # 儲存到 media 資料夾
                media_folder = "media"
                if not os.path.exists(media_folder):
                    os.makedirs(media_folder)
                file_path = os.path.join(media_folder, file_name)
                img.save(file_path)
                generated_image_paths.put(file_path)
                threading.Thread(
                    target=delete_after_10_minutes, args=(file_path,), daemon=True
                ).start()
                return file_path # 返回生成的圖像路徑

def delete_after_10_minutes(file_path: str) -> None:
    time.sleep(600)
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted {file_path} after 10 minutes.")
