import time
from video_processor import extract_frames
from ai_analyzer import analyze_video_frames

start = time.time()
frames = extract_frames("sample.mp4", "uploads/frames", num_frames=6)
print(f"Frame extraction: {time.time() - start:.2f}s")

start = time.time()
summary = analyze_video_frames(frames)
print(f"Gemini analysis: {time.time() - start:.2f}s")

print("\nVIDEO ANALYSIS:\n")
print(summary)