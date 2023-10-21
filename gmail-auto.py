from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64
import os.path
import json

# Define the SCOPES required for Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def create_service():
    creds = None

    # The file token.json stores the user's access and refresh tokens, and is created automatically when the
    # authorization flow completes for the first time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)
    return service

def send_auto_reply(service, message_id):
    auto_reply = "Thank you for your email. This is an auto-reply."
    message = service.users().messages().get(userId='me', id=message_id).execute()
    msg_str = base64.urlsafe_b64decode(message['raw'].encode('ASCII')).decode('utf-8')
    auto_reply_msg = f"Subject: Re: {message['subject']}\nTo: {message['from']}\n\n{auto_reply}"
    service.users().messages().send(userId='me', body={'raw': base64.urlsafe_b64encode(auto_reply_msg.encode()).decode()}).execute()

if __name__ == '__main__':
    service = create_service()
    # Get message IDs that require auto-replies
    message_ids = ['message_id_1', 'message_id_2']  # Replace with actual message IDs
    for message_id in message_ids:
        send_auto_reply(service, message_id)
