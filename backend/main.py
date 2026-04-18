from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel

from backend.search import search_emails
from backend.nlp import extract_query
from backend.gmail_service import fetch_emails_from_gmail

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Query(BaseModel):
    query: str


@app.post("/search")
def search(request: Query):
    
    #STEP 1: NLP extraction
    query_data = extract_query(request.query)
    
    #STEP 2: Build smart Gmail query (IMPORTANT FIX)
    gmail_query_parts = []

    if query_data["role"]:
        gmail_query_parts.append(query_data["role"])

    for skill in query_data["skills"]:
        gmail_query_parts.append(skill)

    if query_data["experience"]:
        gmail_query_parts.append(query_data["experience"])

    gmail_query = " ".join(gmail_query_parts).strip()

    #fallback (if NLP fails)
    if not gmail_query:
        gmail_query = request.query

    #STEP 3: Fetch emails from Gmail
    emails = fetch_emails_from_gmail(gmail_query)

    #STEP 4: Apply search logic
    results = search_emails(query_data, emails)

    #Debug logs (keep for now)
    print("USER QUERY:", request.query)
    print("GMAIL QUERY:", gmail_query)
    print("EMAIL COUNT:", len(emails))

    return results
