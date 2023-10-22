# Gmail Auto-Reply Script
# This Script Was Written By Chatgpt!

This Python script allows you to automatically send replies to specific emails using the Gmail API. It authenticates your application, retrieves unread emails with specific criteria, and sends auto-replies to those emails.

## Prerequisites

- Python 3 installed on your system.
- Necessary Python libraries installed:
 ```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
  ```
- ## Setup

1. **Obtain Gmail API Credentials:**
 - Go to the [Google Cloud Console](https://console.cloud.google.com/).
 - Create a new project and enable the Gmail API.
 - Create OAuth 2.0 credentials (a client ID and client secret).

2. **Download Client Secret JSON:**
 - Download the `client_secret.json` file from your Google Cloud Project. This file will be used to authenticate your application.

3. **Configure Script:**
 - Replace `'client_secret.json'` with the path to your downloaded `client_secret.json` file.
 - Modify `message_ids` with the actual message IDs to which you want to send auto-replies.

## Usage

Run the script using Python 3:
```python script_name.py```
The script will authenticate your application, fetch emails based on specified criteria, and send auto-replies to the selected emails.

## Notes

- Ensure your Gmail account allows access from less secure apps. Visit your Google Account settings to enable this option.
- Handle sensitive information such as API credentials securely. Avoid hardcoding them directly into the script.
- Customize the auto-reply message and email selection logic according to your requirements.
