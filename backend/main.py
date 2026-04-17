from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel

from backend.db import load_emails
from backend.search import search_emails
from backend.nlp import extract_query
from backend.gmail_service import fetch_emails_from_gmail

# cached_emails = []

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all (for now)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# emails = fetch_emails_from_gmail(query.query)

class Query(BaseModel):
    query:str
    
@app.post("/search")
def search(query: Query):
    emails = fetch_emails_from_gmail(query.query)
    query_data = extract_query(query.query)
    results = search_emails(query_data,emails)
    print("QUERY:", query.query)
    print("EMAIL COUNT:", len(emails))
    return results

# @app.post("/search")
# def search(query: Query):
#     global cached_emails

#     # 🔥 fetch only once
#     if not cached_emails:
#         cached_emails = fetch_emails_from_gmail(query.query)

#     query_data = extract_query(query.query)
#     results = search_emails(query_data, cached_emails)

#     return results










# query = "React developer with 2 years experience"

# query_data = extract_query(query)


# results = search_emails(query_data,emails)

# for email in results:
#     print(email["subject"]) 