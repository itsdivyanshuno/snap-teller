```markdown
# 🎥 SnapTeller

> **Turn videos into stories, insights, and summaries.**

**SnapTeller** is an AI-powered video analyzer that transforms raw videos into meaningful insights using **Computer Vision + Google Gemini AI**.

Instead of manually watching an entire video, SnapTeller extracts important frames, analyzes the visual content, and generates an AI-powered understanding of what is happening in the video.

---

## ✨ Features

- 🎬 Upload and analyze videos
- 🖼️ Automatic video frame extraction
- 🤖 AI-powered visual understanding using Google Gemini
- 📝 AI-generated video descriptions and summaries
- ⚡ Fast video processing
- 🌐 Simple and lightweight web interface
- 🚀 FastAPI backend
- 👁️ OpenCV-powered computer vision
- 🔐 Environment-based API key configuration
- 📁 Local video processing

---

## 🧠 How SnapTeller Works

SnapTeller follows a simple AI-powered video analysis pipeline:

**Upload → Process → Extract → Analyze → Understand → Result**

1. **Upload** — The user uploads a video through the frontend.
2. **Backend Processing** — FastAPI receives the uploaded video.
3. **Frame Extraction** — OpenCV processes the video and extracts selected frames.
4. **AI Analysis** — Extracted frames are sent to Google Gemini.
5. **Visual Understanding** — Gemini interprets the visual content.
6. **Result Generation** — SnapTeller returns an AI-generated analysis.

---

## 🔄 Video Analysis Pipeline

    ```mermaid
    flowchart TD
        A["🎥 Upload Video"] --> B["📤 FastAPI Backend"]
        B --> C["🎞️ Video Processor"]
        C --> D["🖼️ Extract Important Frames"]
        D --> E["🤖 Google Gemini AI"]
        E --> F["🧠 Visual Understanding"]
        F --> G["📝 Generate Analysis"]
        G --> H["✨ SnapTeller Result"]

        A:::user
        B:::backend
        C:::process
        D:::process
        E:::ai
        F:::ai
        G:::result
        H:::result

        classDef user fill:#1e293b,color:#fff,stroke:#64748b
        classDef backend fill:#2563eb,color:#fff,stroke:#60a5fa
        classDef process fill:#475569,color:#fff,stroke:#94a3b8
        classDef ai fill:#7c3aed,color:#fff,stroke:#a78bfa
        classDef result fill:#059669,color:#fff,stroke:#34d399
    ```

---

## 🏗️ System Architecture

    ```mermaid
    flowchart LR
        U["👤 User"] --> FE["🌐 Frontend<br/>HTML + CSS + JavaScript"]
        FE --> API["⚡ FastAPI"]
        API --> VP["🎞️ Video Processor"]
        VP --> CV["👁️ OpenCV"]
        CV --> FR["🖼️ Extracted Frames"]
        FR --> AI["🤖 Gemini AI"]
        AI --> API
        API --> FE
        FE --> R["📊 Analysis Result"]

        style U fill:#1e293b,color:#fff
        style FE fill:#2563eb,color:#fff
        style API fill:#0891b2,color:#fff
        style VP fill:#475569,color:#fff
        style CV fill:#475569,color:#fff
        style FR fill:#64748b,color:#fff
        style AI fill:#7c3aed,color:#fff
        style R fill:#059669,color:#fff
    ```

---

## 🔍 Architecture Breakdown

| Component | Responsibility |
|---|---|
| 🌐 Frontend | Video upload and result display |
| ⚡ FastAPI | API and request handling |
| 🎞️ Video Processor | Video processing and frame extraction |
| 👁️ OpenCV | Computer vision and frame processing |
| 🤖 Gemini AI | Visual understanding and analysis |
| 📊 Frontend UI | Display generated insights |

---

## 🛠️ Tech Stack

### Backend

- 🐍 Python
- ⚡ FastAPI
- 🚀 Uvicorn
- 👁️ OpenCV
- 🤖 Google Gemini API
- 🖼️ Pillow
- 🔑 Python-dotenv

### Frontend

- 🌐 HTML5
- 🎨 CSS3
- ⚡ JavaScript

### Development

- 🐙 Git
- 🐙 GitHub
- 🐍 Python Virtual Environment

---

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
    ├── main.py
    ├── ai_analyzer.py
    ├── video_processor.py
    │
    ├── check_gemini.py
    ├── check_models.py
    ├── test_ai.py
    ├── test_video.py
    │
    ├── .gitignore
    └── README.md

### 📌 Core Files

| File | Purpose |
|---|---|
| `main.py` | FastAPI application and API endpoints |
| `video_processor.py` | Video processing and frame extraction |
| `ai_analyzer.py` | Gemini AI integration and video analysis |
| `frontend/index.html` | Main frontend interface |
| `frontend/script.js` | Frontend logic and API communication |
| `frontend/style.css` | Frontend styling |
| `test_video.py` | Video processing tests |
| `test_ai.py` | AI analysis tests |
| `check_gemini.py` | Gemini configuration check |
| `check_models.py` | Available model check |

---

## ⚙️ Installation

### 1. Clone the Repository

    git clone https://github.com/itsdivyanshuno/snap-teller.git
    cd snap-teller

### 2. Create a Virtual Environment

    python3 -m venv venv

### 3. Activate the Virtual Environment

#### Linux / macOS

    source venv/bin/activate

#### Windows

    venv\Scripts\activate

### 4. Install Dependencies

    pip install fastapi uvicorn opencv-python google-genai python-multipart Pillow python-dotenv

---

## 🔑 Gemini API Setup

SnapTeller requires a **Google Gemini API key** for AI-powered video analysis.

Create a `.env` file in the project root:

    GEMINI_API_KEY=your_api_key_here

Add your Gemini API key.

### ⚠️ Security

Never commit your `.env` file to GitHub.

Recommended `.gitignore` entries:

    .env
    .env.*
    venv/
    __pycache__/
    *.pyc
    uploads/*
    *.mp4
    *.mov
    *.avi
    *.mkv

---

## ▶️ Run SnapTeller

### Start the Backend

From the project root:

    uvicorn main:app --reload

Backend:

**http://127.0.0.1:8000**

### Start the Frontend

Open another terminal:

    cd frontend
    python3 -m http.server 5500

Frontend:

**http://localhost:5500**

---

## 🔄 Complete Request Flow

    ```mermaid
    sequenceDiagram
        participant U as 👤 User
        participant F as 🌐 Frontend
        participant B as ⚡ FastAPI
        participant V as 🎞️ Video Processor
        participant G as 🤖 Gemini AI

        U->>F: Upload video
        F->>B: Send video
        B->>V: Process video
        V->>V: Extract important frames
        V->>G: Send frames
        G->>V: AI analysis
        V->>B: Return analysis
        B->>F: Send result
        F->>U: Display insights
    ```

---

## 🎯 Usage

Once both servers are running:

1. Open **http://localhost:5500**
2. Upload a video
3. SnapTeller processes the video
4. Important frames are extracted
5. Frames are analyzed by Gemini
6. AI-generated analysis is returned
7. The result is displayed on the frontend

### Processing Flow

**🎥 Video → 🎞️ Frame Extraction → 🤖 Gemini AI → 🧠 Analysis → ✨ Result**

---

## 🧪 Testing

### Test Video Processing

    python test_video.py

### Test AI Analysis

    python test_ai.py

### Check Gemini Configuration

    python check_gemini.py

### Check Available Gemini Models

    python check_models.py

---

## ⚡ Processing Approach

SnapTeller uses a lightweight processing pipeline:

    🎥 Video
       │
       ▼
    🎞️ Video Processing
       │
       ▼
    🖼️ Frame Extraction
       │
       ▼
    🤖 Gemini AI
       │
       ▼
    🧠 Visual Understanding
       │
       ▼
    📝 AI Analysis
       │
       ▼
    ✨ SnapTeller Result

Instead of attempting to process every frame of a video, SnapTeller extracts selected frames and uses them for AI analysis.

This helps reduce unnecessary processing while keeping the AI focused on important visual information.

---

## 💡 Why SnapTeller?

Long videos can contain a huge amount of information, but users don't always have time to watch everything.

SnapTeller aims to make video understanding faster by combining:

**Computer Vision + Generative AI + Simple UX**

> **Don't just watch the video. Understand it.**

---

## 🔮 Future Improvements

- 🎤 Audio and speech analysis
- 🗣️ Automatic speech transcription
- ⏱️ Timestamp-based insights
- 📌 Automatic highlight detection
- 📊 Advanced video analytics
- 🧠 Improved scene understanding
- 🎞️ Better support for long videos
- 📱 Fully responsive interface
- 🔐 User authentication
- ☁️ Cloud-based video processing
- 💾 Video analysis history
- 📈 Analytics dashboard
- 🎯 Automatic key-moment detection

---

## 🚧 Project Status

**SnapTeller is currently under active development.**

The current version focuses on:

- Video upload
- Frame extraction
- Gemini-powered visual analysis
- AI-generated video understanding
- Local frontend/backend execution

More advanced video intelligence features can be added in future versions.

---

## 👨‍💻 Author

### Divyansh Shukla

**B.Tech Information Technology — HBTU Kanpur**

🔗 **GitHub**  
https://github.com/itsdivyanshuno

🔗 **LinkedIn**  
https://www.linkedin.com/in/itsdivyanshuno

---

## ⭐ Support

If you find **SnapTeller** interesting or useful, consider giving the repository a ⭐ on GitHub.

It helps support the project and encourages further development.

---

<div align="center">

# 🎥 SnapTeller

### Watch less. Understand more.

**Built with Python · OpenCV · FastAPI · Gemini AI**

</div>
```
