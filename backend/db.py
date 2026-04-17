import os 
import json

def load_emails():
    BASE_DIR = os.path.dirname(__file__)
    file_path = os.path.join(BASE_DIR, "emails.json")
    
    with open(file_path) as f:
        return json.load(f)