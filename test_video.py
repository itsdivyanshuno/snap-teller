
from video_processor import extract_frames

frames = extract_frames(
    "sample.mp4",
    "uploads/frames",
    num_frames=6
)

print("Frames extracted:", len(frames))

for frame in frames:
    print(frame)
