from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel

from backend.search import search_emails
from backend.nlp import extract_query
from backend.gmail_service import fetch_emails_from_gmail
from backend.storage import save_emails_locally, load_local_emails

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
    use_cache: bool = True   
    page: int = 1
    limit: int = 5
      

# @app.post("/search")
# def search(request: Query):
    
#     query_data = extract_query(request.query)
#     emails = fetch_emails_from_gmail("")
#     print("Fetched emails:", len(emails))
    
#     results = search_emails(query_data, emails)

#     start = (request.page - 1) * request.limit
#     end = start + request.limit

#     return results

@app.post("/search")
def search(request: Query):

    query_data = extract_query(request.query)

    print("Fetching fresh emails...")

    keywords = query_data.get("keywords", [])

    if keywords:
        gmail_query = " OR ".join(keywords)
    else:
        gmail_query = request.query

    emails = fetch_emails_from_gmail(gmail_query)

    # overwrite cache
    save_emails_locally(emails)

    print("Emails used:", len(emails))

    results = search_emails(query_data, emails)

    return results