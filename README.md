# 🎥 SnapTeller

> Turn videos into stories, insights, and summaries.

SnapTeller is an AI-powered video analyzer that extracts important frames from a video and uses Google's Gemini AI to understand and describe the content.

Instead of watching the entire video manually, SnapTeller gives you a quick AI-generated understanding of what's happening in the video.

## ✨ Features

- 🎬 Upload and analyze videos
- 🖼️ Extract important frames from videos
- 🤖 AI-powered video understanding using Google Gemini
- 📝 Generate video descriptions and summaries
- ⚡ Fast frame processing
- 🌐 Simple web-based frontend
- 🚀 FastAPI backend
- 📁 Local video processing

## 🛠️ Tech Stack

### Backend

- Python
- FastAPI
- Uvicorn
- OpenCV
- Google Gemini API
- Pillow
- Python-dotenv

### Frontend

- HTML
- CSS
- JavaScript

## 📂 Project Structure

snap-teller/
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── uploads/
│
├── ai_analyzer.py
├── video_processor.py
├── main.py
│
├── check_gemini.py
├── check_models.py
├── test_ai.py
├── test_video.py
│
├── .gitignore
└── README.md

## ⚙️ Installation

### 1. Clone the repository

git clone https://github.com/itsdivyanshuno/snap-teller.git
cd snap-teller

### 2. Create a virtual environment

python3 -m venv venv

Activate it:

source venv/bin/activate

### 3. Install dependencies

pip install fastapi uvicorn opencv-python google-genai python-multipart Pillow python-dotenv

## 🔑 Gemini API Setup

Create a `.env` file in the project root:

GEMINI_API_KEY=your_api_key_here

Add your Google Gemini API key.

Never commit your `.env` file or expose your API key publicly.

## ▶️ Run SnapTeller

### Start the backend

uvicorn main:app --reload

Backend:

http://127.0.0.1:8000

### Start the frontend

Open another terminal:

cd frontend
python3 -m http.server 5500

Open:

http://localhost:5500

## 🔄 How It Works

             🎥 Video
                │
                ▼
          📤 Video Upload
                │
                ▼
       🎞️ Frame Extraction
                │
                ▼
        🖼️ Important Frames
                │
                ▼
           🤖 Gemini AI
                │
                ▼
        📝 Video Analysis
                │
                ▼
         🎯 SnapTeller Result

SnapTeller extracts selected frames from the uploaded video and sends them for AI analysis. Gemini then interprets the visual content and generates useful information about the video.

## 🧪 Testing

Test video processing:

python test_video.py

Test AI analysis:

python test_ai.py

Check Gemini configuration:

python check_gemini.py

## 🚀 Future Improvements

- 🎤 Audio and speech analysis
- ⏱️ Timestamp-based video insights
- 📌 Automatic highlight detection
- 📊 More detailed video analytics
- 🧠 Better scene understanding
- 🎞️ Support for longer videos
- 📱 Improved responsive UI
- 🔐 User authentication
- ☁️ Cloud-based video processing

## 👨‍💻 Author

**Divyansh Shukla**

GitHub: https://github.com/itsdivyanshuno

LinkedIn: https://www.linkedin.com/in/itsdivyanshuno

## ⭐ Support

If you find SnapTeller interesting, consider giving the repository a ⭐ on GitHub.

---

**SnapTeller — Watch less. Understand more. 🎥🤖**
