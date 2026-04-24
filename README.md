# AI Email Assistant

This project is an AI-powered Email Assistant that allows users to search emails using natural language queries.  
It improves traditional email search by combining Natural Language Processing (NLP) with semantic search.

---

## Overview

Instead of manually browsing emails, users can type queries like:

"Frontend developer with React experience"

The system processes the query and returns the most relevant emails using meaning-based matching and filtering.

---

## Architecture Overview

User (React Frontend)
        ↓
Search Query
        ↓
FastAPI Backend (/search)
        ↓
NLP Processing (extract_query)
        ↓
Gmail API (fetch emails)
        ↓
Data Preprocessing (clean email content)
        ↓
Semantic Search (Sentence Transformers)
        ↓
Ranking + Filtering
        ↓
Frontend Display (results + highlights)

---

## NLP Approach

The system uses a hybrid NLP approach combining rule-based extraction and semantic understanding.

### 1. Keyword Extraction
- Removes stopwords (e.g., "show", "give", "emails")
- Extracts meaningful keywords from the query

### 2. Structured Query Processing
The query is converted into structured filters:
- Role (e.g., frontend developer)
- Skills (e.g., React, Python)
- Experience (e.g., 2 years)

### 3. Semantic Matching
- Uses Sentence Transformers (`all-MiniLM-L6-v2`)
- Converts text into embeddings (numerical vectors)
- Uses cosine similarity to compare:
  - User query
  - Email content

This allows the system to understand meaning, not just keywords.

### 4. Hybrid Search Logic
- Combines keyword filtering and semantic similarity
- Improves accuracy and relevance

---

## Smart Search Engine

- Filters emails based on:
  - Keywords
  - Skills
  - Experience (if present)
- Ranks results using:
  - Semantic similarity score
  - Keyword matching boost

---

## Data Processing

- Removes HTML tags from emails  
- Cleans unnecessary text (signatures, footer, etc.)  
- Extracts meaningful content  

---

## Features

- Natural language email search  
- Semantic search (meaning-based)  
- Auto-tagging (Job, Internship, Shopping)  
- Email preview with metadata (sender, date)  
- Keyword highlighting  
- Pagination / Load More  
- OAuth-based Gmail authentication  

---

## Tech Stack

- Frontend: React.js  
- Backend: FastAPI (Python)  
- NLP: Sentence Transformers  
- API: Gmail API (OAuth 2.0)  

---

## Project Structure

ai-email-assistant/
│
├── backend/
│   ├── main.py              # API routes
│   ├── gmail_service.py     # Gmail integration
│   ├── search.py            # Search + ranking logic
│   ├── nlp.py               # Query processing
│
├── frontend/
│   ├── src/
│   ├── public/
│
├── README.md
└── .gitignore

---

## Setup Instructions

### 1. Clone Repository

git clone https://github.com/MrunmayeeS28/ai-email-assistant.git  
cd ai-email-assistant  

---

### 2. Backend Setup

Install dependencies:

pip install fastapi uvicorn google-api-python-client google-auth-httplib2 google-auth-oauthlib sentence-transformers  

Run server:

uvicorn backend.main:app --reload  

Backend runs on:  
http://127.0.0.1:8000  

---

### 3. Frontend Setup

cd frontend  
npm install  
npm start  

Frontend runs on:  
http://localhost:3000  

---

## Gmail API Setup

- Go to Google Cloud Console  
- Enable Gmail API  
- Create OAuth credentials  
- Download credentials.json  
- Place it in the project root  

First run:
- Login popup will appear  
- token.pkl will be generated  

---

## How It Works

1. User enters a query  
2. NLP module processes the query  
3. Gmail API fetches emails  
4. Emails are cleaned and processed  
5. Semantic + keyword search is applied  
6. Results are ranked and displayed  

---

## Example

Query:

java developer with 2 years experience  

Output includes:
- Relevant emails  
- Subject, sender, preview  
- Highlighted keywords  

---

## Limitations

- Basic intent understanding (rule-based)  
- Limited email fetch for performance  
- Single-user authentication (demo purpose)  

---

## Future Improvements

- Multi-user authentication  
- Advanced intent classification  
- Full email indexing  
- Resume/CV parsing  
- AI-based email summarization  

---

## Author

Mrunmayee Surate  

---

## Note

- credentials.json and token.pkl are not included for security reasons  
- These files must be added manually  

---

## Final Result

- Meets all core requirements  
- Uses NLP and semantic search  
- Clean architecture  
- Fully functional system  