# 🔍 HackTrail – AI-Powered Resume Shortlisting System

HackTrail is an intelligent job screening platform powered by NLP and GenAI techniques. It parses CVs, compares them with a job description, ranks the candidates, and emails shortlisted applicants automatically using Gmail.

---

## ✨ Features

- 📥 Upload multiple PDF resumes in one go
- 📝 Paste a Job Description — we’ll extract keywords
- 📊 AI-based CV scoring using TF-IDF + cosine similarity
- ✉️ Emails are sent to top candidates automatically
- 🌑 Beautiful dark UI for modern UX
- 🔒 Gmail App Password support (secure sending)

---

## 🛠 Project Structure
```
HACKTRAIL/
│
├── agents/                      # 🧠 All AI agents (each in its own file)
│   ├── jd_summarizer.py         # JD Summarizer Agent
│   ├── cv_parser.py             # CV Parser Agent
│   ├── matcher.py               # Matcher Agent
│   ├── scheduler.py             # Scheduler Agent
|
├── data/                        # 📄 Input files
│   ├── sample_jds/              # Sample Job Descriptions
│   ├── sample_cvs/              # Sample Resumes
│   └── dataset/
│
├── utils/                       # 🔧 Utility functions (PDF reader, email sender, etc.)
│   ├── pdf_reader.py
│   ├── email_sender.py
│   └── preprocessing.py
│
├── models/                      # 🤖 ML models (used by learning agent)
│   └── match_predictor.pkl
│
├── static/css/                    # 🌐 Assets for dashboard
│   └── style.css
│
├── templates/                   # 🧩 HTML templates for dashboard 
│   └── shortlist_ui.html
│
├── main.py                      # 🚀 Main controller to run the app
├── uploaded_cvs                 # 📦 Store CVs upload by user (per run new file created)
├── README.md                    # 📘 Project overview & setup instructions
├── Structure.tx                 # 👩🏻‍💻Project structure
└── demo_video_link.txt          # 📹 Link to demo video
```


---

## 🚀 How to Run

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/hacktrail.git
cd hacktrail-job-screening
```

### 2. Install dependencies

```bash
pip install flask python-dotenv PyPDF2 scikit-learn nltk
```

### 3. Download NLTK data (only once)

```bash
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
```
### 4.Add Gmail & App Password

Go to Google App Passwords
Select Mail → Windows Computer
Copy the 16-character password

```bash
EMAIL_PASS=xxxx xxxx xxxx xxxx
```

---

## 🌐 Run the app
```bash
python main.py
```
Then open http://127.0.0.1:5000 in your browser 🚀

---

## 🧠 Built With

- Python 🐍
- Flask
- NLTK
- TF-IDF & Cosine Similarity
- Gmail SMTP
- HTML5 + CSS (dark theme)

---

## 🤝 Contributing
Pull requests are welcome! If you find bugs or have ideas, feel free to open an issue.

## 📜 License
MIT License © 2025 HackTrail_Team
