<div align="center">

<img src="https://img.shields.io/badge/VidSnapAI-FF6B6B?style=for-the-badge&logoColor=white" alt="VidSnapAI" />

# 🎬 VidSnapAI

### Turn images + text → shareable Instagram Reels in seconds

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![ElevenLabs](https://img.shields.io/badge/ElevenLabs-TTS-6C3BF5?style=flat-square)](https://elevenlabs.io)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-Video-007808?style=flat-square&logo=ffmpeg&logoColor=white)](https://ffmpeg.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)

<br/>

> Upload your images. Describe your vision. Get a 1080×1920 reel with AI voiceover — ready to post.

</div>

---

## ✨ What It Does

VidSnapAI takes a set of images and a plain-text description, then automatically:

- 🗣️ **Generates a voiceover** from your text using the ElevenLabs API
- 🎞️ **Stitches your images** into a vertical 9:16 video using FFmpeg
- 📦 **Delivers an MP4** — 1080×1920, 30fps, Instagram-ready

No video editing skills required.

---

## 🚀 Demo Flow

```
📸 Upload Images   →   ✍️ Enter Description   →   ⚙️ Processing   →   🎬 Your Reel
```

1. Go to `/create` → upload one or more images
2. Type the voiceover script in the text box
3. Hit **Create Reel** — processing runs in the background
4. Visit `/gallery` to watch and download your reel

---

## 🛠️ Tech Stack

| Layer | Tool |
|:---|:---|
| 🐍 Backend | Python + Flask |
| 🗣️ Text-to-Speech | ElevenLabs API (`eleven_turbo_v2_5`) |
| 🎞️ Video Processing | FFmpeg (libx264 + AAC) |
| 🌐 Frontend | Jinja2 + Bootstrap 5 + Vanilla JS |

---

## 📁 Project Structure

```
VidSnapAI/
│
├── main.py                  # Flask app — routes & file handling
├── generate_process.py      # Background processor (polling loop)
├── text_to_audio.py         # ElevenLabs TTS integration
├── config.py                # 🔑 API keys (do NOT commit this)
├── done.txt                 # Tracks processed reel UUIDs
│
├── user_uploads/            # One folder per reel session (UUID)
│   └── <uuid>/
│       ├── *.jpg / *.png    # Uploaded images
│       ├── desc.txt         # Voiceover text
│       ├── audio.mp3        # Generated audio
│       └── input.txt        # FFmpeg concat manifest
│
├── static/
│   ├── reels/               # 🎬 Output MP4 files
│   └── css/
│       ├── style.css
│       ├── create.css
│       └── gallery.css
│
└── templates/
    ├── base.html
    ├── index.html
    ├── create.html
    └── gallery.html
```

---

## ⚡ Getting Started

### Prerequisites

- Python **3.8+**
- **FFmpeg** installed and on your system PATH → [Download here](https://ffmpeg.org/download.html)
- An **ElevenLabs** API key → [Get one free](https://elevenlabs.io)

### 1. Clone the repo

```bash
git clone https://github.com/your-username/VidSnapAI.git
cd VidSnapAI
```

### 2. Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install flask elevenlabs werkzeug
```

### 4. Configure your API key

Create a `config.py` file:

```python
ELEVENLABS_API_KEY = "your_api_key_here"
```

> ⚠️ **Never commit `config.py` to GitHub.** Add it to `.gitignore` immediately.
> Better yet, use an environment variable:
> ```python
> import os
> ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")
> ```

### 5. Run

```bash
python main.py
```

Open `http://127.0.0.1:5000` 🎉

---

## 🔩 Under the Hood — FFmpeg Command

```bash
ffmpeg -f concat -safe 0 -i input.txt -i audio.mp3 \
  -vf "scale=1080:1920:force_original_aspect_ratio=decrease, \
       pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" \
  -c:v libx264 -c:a aac -shortest -r 30 -pix_fmt yuv420p \
  static/reels/<uuid>.mp4
```

Each image is displayed for **1 second** by default. Output is a `1080×1920` portrait MP4 at 30fps.

---

## 📄 Recommended `.gitignore`

```gitignore
# Secrets
config.py
.env

# Runtime data
user_uploads/
static/reels/
done.txt

# Python
venv/
__pycache__/
*.pyc
*.pyo
```

---

## 🗺️ Roadmap

- [ ] 🔄 Real-time progress indicator during reel creation
- [ ] ⏱️ Configurable per-image display duration
- [ ] 🎵 Background music support
- [ ] 🔐 User authentication + private galleries
- [ ] ☁️ Cloud storage for reels (S3 / Cloudinary)
- [ ] 🐳 Docker + one-command deployment
- [ ] 📱 Direct Instagram publish via Graph API

---

## 👨‍💻 Author

Built by **Aatesh Yadav** — Computer Science Engineering, JUIT Solan

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://linkedin.com/in/your-profile)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/your-username)

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

<div align="center">
<br/>
⭐ If you found this useful, give it a star!
</div>
