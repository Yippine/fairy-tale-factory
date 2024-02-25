import os
import io
import warnings
import threading
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
import time
from datetime import datetime

STEPS = 50
SAMPLES = 1
WIDTH = 1024
HEIGHT = 1024

def create_image_from_prompt(prompt: str, seed: int) -> None:
    os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'
    os.environ['STABILITY_KEY'] = 'sk-0f3HL8RwR1B8BJbv0ihvwVDwb76W3lqdt6geSZKzKt2BNB4H'

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
                img.save(file_name)
                threading.Thread(target=delete_after_10_minutes, args=(file_name,)).start()

def delete_after_10_minutes(file_name: str) -> None:
    time.sleep(600)  
    if os.path.exists(file_name):
        os.remove(file_name)
        print(f"Deleted {file_name} after 10 minutes.")


