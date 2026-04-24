from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import os
import pickle
import base64
import re

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_body(payload):
    if 'parts' in payload:
        for part in payload['parts']:
            if part['mimeType'] == 'text/plain':
                return base64.urlsafe_b64decode(part['body']['data']).decode(errors="ignore")
            elif part['mimeType'] == 'text/html':
                raw = base64.urlsafe_b64decode(part['body']['data']).decode(errors="ignore")
                
                import re
                clean = re.sub('<.*?>', '', raw)
                return clean

    elif 'body' in payload and 'data' in payload['body']:
        return base64.urlsafe_b64decode(payload['body']['data']).decode(errors="ignore")

    return "No content"


# def authenticate_gmail():
#     creds = None

#     if os.path.exists('token.pkl'):
#         with open('token.pkl', 'rb') as token:
#             creds = pickle.load(token)

#     if not creds:
#         BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#         cred_path = os.path.join(BASE_DIR, "credentials.json")

#         flow = InstalledAppFlow.from_client_secrets_file(
#             cred_path, SCOPES)
#         creds = flow.run_local_server(port=0)

#         with open('token.pkl', 'wb') as token:
#             pickle.dump(creds, token)

#     service = build('gmail', 'v1', credentials=creds)
#     return service

def authenticate_gmail():
    creds = None

    # 🔥 check if token exists
    if os.path.exists("token.pkl"):
        with open("token.pkl", "rb") as token:
            creds = pickle.load(token)

    # 🔥 if not logged in → login
    if not creds:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json",
            SCOPES
        )
        creds = flow.run_local_server(port=0, prompt="consent")

        # 🔥 save token (for reuse)
        with open("token.pkl", "wb") as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    return service


def fetch_emails_from_gmail(query, max_total=200):
    service = authenticate_gmail()

    emails = []
    next_page_token = None

    while True:
        results = service.users().messages().list(
            userId='me',
            q=query,
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        messages = results.get('messages', [])

        for msg in messages:
            msg_data = service.users().messages().get(
                userId='me',
                id=msg['id']
            ).execute()

            headers = msg_data['payload']['headers']

            subject = ""
            sender = ""
            date = ""

            for h in headers:
                if h['name'] == 'Subject':
                    subject = h['value']
                elif h['name'] == 'From':
                    sender = h['value']
                elif h['name'] == 'Date':
                    date = h['value']

            body = get_body(msg_data['payload'])

            emails.append({
                "subject": subject,
                "sender": sender,
                "date": date,
                "body": body
            })

        # 🔥 pagination control
        next_page_token = results.get('nextPageToken')

        # 🔥 stop conditions
        if not next_page_token or len(emails) >= max_total:
            break

    return emails