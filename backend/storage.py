import json
import os

# file path
FILE_PATH = os.path.join(os.path.dirname(__file__), "emails.json")

def save_emails_locally(emails):
    with open(FILE_PATH, "w", encoding="utf-8") as f:
        json.dump(emails, f, ensure_ascii=False, indent=2)

def load_local_emails():
    if not os.path.exists(FILE_PATH):
        return []
    
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)