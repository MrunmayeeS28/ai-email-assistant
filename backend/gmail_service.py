from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import os
import pickle
import base64

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_body(payload):
    if 'parts' in payload:
        for part in payload['parts']:
            if part['mimeType'] in ['text/plain', 'text/html']:
                if 'data' in part['body']:
                    return base64.urlsafe_b64decode(part['body']['data']).decode(errors="ignore")
            # 🔁 check nested parts
            if 'parts' in part:
                return get_body(part)

    elif 'body' in payload and 'data' in payload['body']:
        return base64.urlsafe_b64decode(payload['body']['data']).decode(errors="ignore")

    return "No content"


def authenticate_gmail():
    creds = None

    if os.path.exists('token.pkl'):
        with open('token.pkl', 'rb') as token:
            creds = pickle.load(token)

    if not creds:
        BASE_DIR = os.path.dirname(os.path.dirname(__file__))
        cred_path = os.path.join(BASE_DIR, "credentials.json")

        flow = InstalledAppFlow.from_client_secrets_file(
            cred_path, SCOPES)
        creds = flow.run_local_server(port=0)

        with open('token.pkl', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    return service


def fetch_emails_from_gmail():
    service = authenticate_gmail()

    results = service.users().messages().list(userId='me', maxResults=5).execute()
    messages = results.get('messages', [])

    emails = []

    for msg in messages:
        msg_data = service.users().messages().get(userId='me', id=msg['id']).execute()

        headers = msg_data['payload']['headers']

        subject = ""
        sender = ""

        for h in headers:
            if h['name'] == 'Subject':
                subject = h['value']
            if h['name'] == 'From':
                sender = h['value']

        body = get_body(msg_data['payload'])

        emails.append({
            "subject": subject,
            "sender": sender,
            "date": "N/A",
            "body": body
        })

    return emails