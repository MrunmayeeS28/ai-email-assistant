# AI Email Assistant

This project is an AI-based Email Assistant that helps users search emails more efficiently.

Instead of manually going through emails, users can enter a query such as "Java developer" or "internship", and the system will fetch and display the most relevant emails.

---

## Overview

The application integrates with Gmail using the Gmail API and allows users to search emails using natural language queries. It combines keyword-based search with simple NLP to improve relevance.

---

## Features

- Gmail API integration for fetching emails  
- Search using natural language queries  
- Full-text search across email subject and body  
- Relevance-based ranking of results  
- Preview display instead of full email body  
- Highlighting of search keywords in subject and preview  
- Clean and simple user interface  

---

## Tech Stack

- Frontend: React  
- Backend: FastAPI (Python)  
- API: Gmail API  
- Query processing using basic NLP  

---

## Project Structure
ai-email-assistant/
│
├── backend/
│ ├── main.py
│ ├── gmail_service.py
│ ├── search.py
│ ├── nlp.py
│
├── frontend/
│ ├── src/
│ ├── public/
│
├── README.md
└── .gitignore
---

## Setup Instructions

### 1. Clone the repository


git clone https://github.com/MrunmayeeS28/ai-email-assistant.git

cd ai-email-assistant


---

### 2. Backend Setup

Install dependencies:


pip install fastapi uvicorn google-api-python-client google-auth-httplib2 google-auth-oauthlib


Run the server:


uvicorn backend.main:app --reload


Backend will run on:


http://127.0.0.1:8000


---

### 3. Frontend Setup


cd frontend
npm install
npm start


Frontend will run on:


http://localhost:3000


---

## Gmail API Setup

- Go to Google Cloud Console  
- Enable Gmail API  
- Create OAuth credentials  
- Download credentials.json  
- Place it in the project root directory  

---

## How It Works

1. The user enters a query  
2. The system processes the query using NLP  
3. Gmail API fetches related emails  
4. Emails are ranked based on relevance  
5. Results are displayed with subject, sender, and preview  

---

## Example

Query:


java developer


Output includes:

- Subject  
- Sender  
- Preview of the email  
- Highlighted keywords  

---

## Future Improvements

- Add full email view functionality  
- Improve performance using caching  
- Add advanced filters such as date and sender  
- Improve ranking using advanced NLP techniques  

---

## Author

Mrunmayee Surate  

---

## Note

- credentials.json and token.pkl are not included for security reasons  
- These files must be added manually to run the project  
