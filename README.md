# 📧 AI Email Assistant

## 📌 Overview
The AI Email Assistant is a backend system that fetches emails from Gmail and allows users to search emails using natural language queries. It uses basic NLP techniques to understand user intent and returns relevant emails.

---

## 🚀 Features
- Fetch emails using Gmail API
- Search emails using natural language (e.g., "Java developer", "internship")
- Extract key information like role, skills, and experience
- Rank emails based on relevance
- Tag emails (Candidate, Internship, General)

---

## 🛠️ Technologies Used
- Python
- FastAPI
- Gmail API
- Basic NLP (custom logic)

---

## ⚙️ How It Works
1. Gmail API fetches emails
2. NLP module processes user query
3. Search logic matches query with emails
4. Emails are ranked based on score
5. Results are returned via API

---

## ▶️ How to Run the Project

### 1. Clone the repository
```bash
git clone https://github.com/your-username/ai-email-assistant.git
cd ai-email-assistant

2. Install dependencies:
pip install fastapi uvicorn google-api-python-client google-auth-httplib2 google-auth-oauthlib

3. Run the server
uvicorn backend.main:app --reload


4. Open in browser
http://127.0.0.1:8000/docs

5. Example Query
{
  "query": "software engineer"
}
Example Output
[
  {
    "subject": "Software Engineer Opportunity",
    "sender": "hr@example.com",
    "body": "We are hiring...",
    "tag": "Candidate"
  }
]