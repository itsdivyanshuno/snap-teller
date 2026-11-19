import os
import shutil
import uuid

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from video_processor import extract_frames
from ai_analyzer import analyze_video_frames

app = FastAPI(title="AI Video Analyzer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.get("/")
def home():
    return {"message": "AI Video Analyzer API is running"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/analyze")
async def analyze_video(file: UploadFile = File(...)):
    if not file.filename or not file.filename.lower().endswith(
        (".mp4", ".mov", ".avi", ".mkv", ".webm")
    ):
        raise HTTPException(
            status_code=400,
            detail="Please upload a supported video file."
        )

    job_id = uuid.uuid4().hex
    video_path = os.path.join(UPLOAD_DIR, f"{job_id}_{file.filename}")
    frames_dir = os.path.join(UPLOAD_DIR, f"frames_{job_id}")

    try:
        with open(video_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        frames = extract_frames(
            video_path,
            frames_dir,
            num_frames=6
        )

        summary = analyze_video_frames(frames)

        return {
            "filename": file.filename,
            "frames_analyzed": len(frames),
            "summary": summary
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    finally:
        await file.close()
        if os.path.exists(video_path):
            os.remove(video_path)
        shutil.rmtree(frames_dir, ignore_errors=True)
