import requests
import time
import logging

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

TOKEN = """EAAD6V7os0gcBPM6GfBXCneynStu5SnwxGw9V6oZB49t57CjD3dKu7e2ZAfPlcLlShmDeN0bsk8UMs1MToEnyD5RjwuKjdQPs06ctzuj9k3V2uDQZAWLvKvjhEOYBv3tcOlbPd9YvZA85mJDbrxlJ5ZBxudB9miZCEv345QTTcSBQ7kigW7CZBCKW7YRMpG85QZDZD"""
UID = "30658091933805221"
MESSAGE = "Hello! This is a test message from your automation bot."
INTERVAL_SECONDS = 30

def send_message(token, recipient_id, message):
    url = f"https://graph.facebook.com/v16.0/me/messages?access_token={token}"
    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": message}
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            logging.info(f"Message sent to {recipient_id} successfully.")
        else:
            logging.error(f"Failed to send message to {recipient_id}: {response.status_code} - {response.text}")
    except Exception as e:
        logging.error(f"Exception occurred while sending message to {recipient_id}: {e}")

def main():
    logging.info("Messenger bot started. Sending message every 30 seconds...")
    while True:
        send_message(TOKEN, UID, MESSAGE)
        time.sleep(INTERVAL_SECONDS)

if __name__ == "__main__":
    main()
    
