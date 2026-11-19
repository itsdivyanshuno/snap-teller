
import cv2
import os


def extract_frames(video_path, output_dir, num_frames=6):
    os.makedirs(output_dir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise ValueError("Could not open video file")

    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if total_frames <= 0:
        cap.release()
        raise ValueError("Video contains no readable frames")

    count = min(num_frames, total_frames)
    positions = [
        int(i * (total_frames - 1) / max(count - 1, 1))
        for i in range(count)
    ]

    saved_frames = []

    for i, position in enumerate(positions):
        cap.set(cv2.CAP_PROP_POS_FRAMES, position)
        success, frame = cap.read()

        if success:
            frame_path = os.path.join(output_dir, f"frame_{i}.jpg")
            cv2.imwrite(frame_path, frame)
            saved_frames.append(frame_path)

    cap.release()

    if not saved_frames:
        raise ValueError("Could not extract any frames")

    return saved_frames
