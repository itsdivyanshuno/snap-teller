import os
import time
from google import genai
from PIL import Image
from dotenv import load_dotenv
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing from .env")

client = genai.Client(
    api_key=api_key,
    http_options=types.HttpOptions(timeout=120000)
)


def analyze_video_frames(frame_paths):
    images = []

    for path in frame_paths:
        print(f"Loading: {path}")
        images.append(Image.open(path).convert("RGB"))

    prompt = """
    Describe the main events in these video frames in chronological order.
    Be concise and mention only what is visible.
    """

    print(f"Sending {len(images)} frames to Gemini...")
    start = time.time()

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=[prompt, *images]
        )

        print(f"Gemini response received in {time.time() - start:.2f}s")
        return response.text or "No description returned."

    finally:
        for image in images:
            image.close()
