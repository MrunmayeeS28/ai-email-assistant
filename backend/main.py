from fastapi import FastAPI
from pydantic import BaseModel

from backend.db import load_emails
from backend.search import search_emails
from backend.nlp import extract_query
from backend.gmail_service import fetch_emails_from_gmail

app = FastAPI()

emails = fetch_emails_from_gmail()

class Query(BaseModel):
    query:str
    
@app.post("/search")
def search(query: Query):
    query_data = extract_query(query.query)
    results = search_emails(query_data,emails)
    print(emails)
    return results










# query = "React developer with 2 years experience"

# query_data = extract_query(query)


# results = search_emails(query_data,emails)

# for email in results:
#     print(email["subject"]) 