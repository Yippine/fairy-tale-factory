import os
import io
import warnings
import threading
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
import time
from datetime import datetime
from queue import Queue  

STEPS = 50
SAMPLES = 1
WIDTH = 1024
HEIGHT = 1024

def create_image_from_prompt(prompt: str, seed: int, generated_image_paths: Queue) -> None:
    os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'
    os.environ['STABILITY_KEY'] = 'sk-OSaQac65efrL6dB6qvuTj4AA7c6IHPmFZCf16S4FDhrWfTM5'

    stability_api = client.StabilityInference(
        key=os.environ['STABILITY_KEY'],
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
        sampler=generation.SAMPLER_K_DPMPP_2M
    )
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                warnings.warn(
                    "Your request activated the API's safety filters and could not be processed."
                    "Please modify the prompt and try again.")
            if artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary))
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                file_name = f"{timestamp}.png"  # 使用传入的 seed 参数创建文件名
                # 保存到 media 文件夹
                media_folder = 'media'
                if not os.path.exists(media_folder):
                    os.makedirs(media_folder)
                file_path = os.path.join(media_folder, file_name)
                img.save(file_path)
                generated_image_paths.put(file_path)
                threading.Thread(target=delete_after_10_minutes, args=(file_path,), daemon=True).start()
                
                return file_path  # 返回生成的图像路径

def delete_after_10_minutes(file_path: str) -> None:
    time.sleep(600)  
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted {file_path} after 10 minutes.")
