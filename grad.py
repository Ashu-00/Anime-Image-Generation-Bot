from gradio_client import Client
import os
from PIL import Image
import random


def get_image(prompt,
              negative_prompt="",
              width=1024,
              height=1024,
              guidance_scale=7,
              num_inference_steps=28,
              seed=random.randint(0, 2147483647),
              style="(None)"):
    client = Client("cagliostrolab/animagine-xl-3.1",
                    verbose=True,
                    download_files="images")
    result = client.submit(
        prompt,  # str  in 'Prompt' Textbox component
        "nsfw, lowres, (bad), text, error, fewer, extra, missing, worst quality, jpeg artifacts, low quality, watermark, unfinished, displeasing, oldest, early, chromatic aberration, signature, extra digits, artistic error, username, scan, [abstract]"
        + negative_prompt,  # str  in 'Negative Prompt' Textbox component
        seed,  # float (numeric value between 0 and 2147483647) in 'Seed' Slider component
        width,  # float (numeric value between 512 and 2048) in 'Width' Slider component
        height,  # float (numeric value between 512 and 2048) in 'Height' Slider component
        guidance_scale,  # float (numeric value between 1 and 12) in 'Guidance scale' Slider component
        num_inference_steps,  # float (numeric value between 1 and 50) in 'Number of inference steps' Slider component
        "Euler a",  # Literal['DPM++ 2M Karras', 'DPM++ SDE Karras', 'DPM++ 2M SDE Karras', 'Euler', 'Euler a', 'DDIM']  in 'Sampler' Dropdown component
        "Custom",  # Literal['1024 x 1024', '1152 x 896', '896 x 1152', '1216 x 832', '832 x 1216', '1344 x 768', '768 x 1344', '1536 x 640', '640 x 1536', 'Custom']  in 'Aspect Ratio' Radio component
        style,  # Literal['(None)', 'Cinematic', 'Photographic', 'Anime', 'Manga', 'Digital Art', 'Pixel art', 'Fantasy art', 'Neonpunk', '3D Model']  in 'Style Preset' Radio component
        "Standard v3.1",  # Literal['(None)', 'Standard v3.0', 'Standard v3.1', 'Light v3.1', 'Heavy v3.1']  in 'Quality Tags Presets' Dropdown component
        False,  # bool  in 'Use Upscaler' Checkbox component
        0,  # float (numeric value between 0 and 1) in 'Strength' Slider component
        1,  # float (numeric value between 1 and 1.5) in 'Upscale by' Slider component
        False,  # bool  in 'Add Quality Tags' Checkbox component
        api_name="/run",
    )

    print(result.status())
    while not result.done():
        status = result.status()
        #print(f"Current in position {status.rank} out of {status.queue_size}")

    x = result.outputs()
    print("result", x[0][0][0]["image"])
    return x[0][0][0]["image"]
