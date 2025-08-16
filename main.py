import requests
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

TOKEN = "EAAD6V7os0gcBPI5h8ZCZB1uzxUZB21ztVdbB94usEg4CtKWWrZB51K8jUa8PzngnzPTSXrMf5jG07awKcRDCuSaGZAZCw45mZAZB394zTrqJaYouMDBj8qbY8Pu8fsgHKxgSDEbhVRykzrZB0jA9fC8LXZBRLKeXNXTE2FHtc5q2eYCqAgMVg1Uq7GF4ZCJZAUZARbaMJdAZDZD"
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
    
