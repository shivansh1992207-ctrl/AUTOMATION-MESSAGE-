import requests
import time

TOKEN = "EAAD6V7os0gcBPM6GfBXCneynStu5SnwxGw9V6oZB49t57CjD3dKu7e2ZAfPlcLlShmDeN0bsk8UMs1MToEnyD5RjwuKjdQPs06ctzuj9k3V2uDQZAWLvKvjhEOYBv3tcOlbPd9YvZA85mJDbrxlJ5ZBxudB9miZCEv345QTTcSBQ7kigW7CZBCKW7YRMpG85QZDZD"
UID = "30658091933805221"
MESSAGE = "Hello! This is a test message from your automation bot."
INTERVAL_SECONDS = 30

def send_message(token, recipient_id, message):
    url = f"https://graph.facebook.com/v16.0/me/messages?access_token={token}"
    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": message}
    }
    response = requests.post(url, json=payload)
    print(f"Sent to {recipient_id}: {response.status_code} - {response.text}")

def main():
    print("Messenger bot started. Sending message every
          
