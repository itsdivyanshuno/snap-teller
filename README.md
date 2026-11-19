# 🎥 SnapTeller

### AI-Powered Video Understanding

<p align="center">

**Upload a video → Extract frames → Gemini analyzes → Get insights**

<br>

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white)](https://opencv.org/)
[![Gemini](https://img.shields.io/badge/Gemini-AI-8E75B2?style=flat-square&logo=google&logoColor=white)](https://ai.google.dev/)

</p>

---

## ✨ What is SnapTeller?

SnapTeller turns videos into **AI-generated visual insights** using OpenCV and Google Gemini.

Instead of watching the entire video, SnapTeller extracts important frames and lets AI understand what's happening.

---

## 🧠 How It Works

```mermaid
flowchart LR
    A["🎥 Video"] --> B["🎞️ Frame Extraction"]
    B --> C["🤖 Gemini AI"]
    C --> D["🧠 Understanding"]
    D --> E["✨ Insights"]

    style A fill:#1e293b,color:#fff
    style B fill:#2563eb,color:#fff
    style C fill:#7c3aed,color:#fff
    style D fill:#0891b2,color:#fff
    style E fill:#059669,color:#fff
```

### ⚡ Core Pipeline

**Video → OpenCV → Selected Frames → Gemini → AI Analysis**

---

## 🏗️ Architecture

```mermaid
flowchart LR
    U["👤 User"] --> F["🌐 Frontend"]
    F --> A["⚡ FastAPI"]
    A --> P["🎞️ Video Processor"]
    P --> O["👁️ OpenCV"]
    O --> G["🤖 Gemini"]
    G --> A
    A --> F
    F --> R["📊 Result"]

    style F fill:#2563eb,color:#fff
    style A fill:#0891b2,color:#fff
    style P fill:#475569,color:#fff
    style O fill:#5b21b6,color:#fff
    style G fill:#7c3aed,color:#fff
    style R fill:#059669,color:#fff
```

---

## 🚀 Features

| | Feature |
|---|---|
| 🎬 | Video upload & analysis |
| 🖼️ | Automatic frame extraction |
| 🤖 | Gemini-powered visual understanding |
| 📝 | AI-generated descriptions |
| ⚡ | Fast lightweight processing |
| 🌐 | Simple web interface |
| 🔐 | Environment-based API keys |

---

## 🛠️ Tech Stack

**Backend:** Python · FastAPI · Uvicorn

**AI / Vision:** Google Gemini · OpenCV · Pillow

**Frontend:** HTML · CSS · JavaScript

**Tools:** Git · GitHub · Python venv

---

## 📂 Project Structure

    snap-teller/
    ├── frontend/
    │   ├── index.html
    │   ├── script.js
    │   └── style.css
    ├── main.py
    ├── ai_analyzer.py
    ├── video_processor.py
    ├── test_ai.py
    ├── test_video.py
    └── README.md

---

## ⚙️ Quick Start

### 1. Clone

    git clone https://github.com/itsdivyanshuno/snap-teller.git
    cd snap-teller

### 2. Setup

    python3 -m venv venv
    source venv/bin/activate
    pip install fastapi uvicorn opencv-python google-genai python-multipart Pillow python-dotenv

### 3. Add Gemini API Key

Create `.env`:

    GEMINI_API_KEY=your_api_key_here

### 4. Run Backend

    uvicorn main:app --reload

**API:** `http://127.0.0.1:8000`

### 5. Run Frontend

    cd frontend
    python3 -m http.server 5500

**App:** `http://localhost:5500`

---

## 🔄 Request Flow

```mermaid
sequenceDiagram
    participant U as 👤 User
    participant F as 🌐 Frontend
    participant B as ⚡ FastAPI
    participant O as 👁️ OpenCV
    participant G as 🤖 Gemini

    U->>F: Upload Video
    F->>B: Send Video
    B->>O: Extract Frames
    O->>G: Send Frames
    G->>B: AI Analysis
    B->>F: Return Result
    F->>U: ✨ Display Insights
```

---

## 🔮 Roadmap

- 🎤 Audio & speech analysis
- ⏱️ Timestamp-based insights
- 📌 Automatic highlight detection
- 🧠 Better scene understanding
- 📊 Video analytics
- ☁️ Cloud processing
- 🔐 User authentication

---

## 👨‍💻 Author

**Divyansh Shukla**

B.Tech Information Technology — **HBTU Kanpur**

[![GitHub](https://img.shields.io/badge/GitHub-itsdivyanshuno-181717?style=flat-square&logo=github)](https://github.com/itsdivyanshuno)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-itsdivyanshuno-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/itsdivyanshuno)

---

<p align="center">

### 🎥 **SnapTeller**
**Watch less. Understand more.**

*Built with Python · OpenCV · FastAPI · Gemini AI*

</p>
