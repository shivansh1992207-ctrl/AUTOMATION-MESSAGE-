import requests

# Facebook API credentials
ACCESS_TOKEN = 'EAAD6V7os0gcBPLhAvpVGRHn2cZC8DYXq9GE0NPMBfDrKEBXt9xZA4roFilEZAKFjMu7GKVaQYguAZABNigdtVNCd6KLBoZCDY6vp646urECVVqhPu8ORulzrQh6CzVhIBcZBe5ndKZAFOnZBMnSE6r2BBrUFANMSVjbeyRaqwfZAk0Lmeawj5fsCPoTWEC4cChWNxwAZDZD'
GROUP_ID = '30658091933805221'

# Function to send a message to a Facebook Messenger group
def send_message_to_group(group_id, message, access_token):
    url = f"https://graph.facebook.com/v19.0/me/messages"
    payload = {
        'recipient': {'id': group_id},
        'message': {'text': message},
        'access_token': access_token
    }
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Error: {response.status_code} - {response.text}")

# Example usage
try:
    send_message_to_group(GROUP_ID, "Hello, this is a test message.", ACCESS_TOKEN)
except Exception as e:
    print(f"An error occurred: {e}")
