import requests

# Facebook API credentials
ACCESS_TOKEN = 'EAAD6V7os0gcBPOyv15I7SXpLKEZBsj8ZAshFoLA2e4Hf6XUsTvrY8qrEuTXXA8XmXIBfZB71jzubAaO5ZCwJ2WJjS8xNEjheR9pcHFYlFO3GyxC6BZOC8JAELZAe3YgXZAolI1HrN1sFASLoG7AxxFExRwXhMGC0G1fzaoIWGgpGwOht6TdnkOixQQJ50XAAZDZD'
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
send_message_to_group(GROUP_ID, "Hello, this is a test message.", ACCESS_TOKEN)
