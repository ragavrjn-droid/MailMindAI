from dotenv import load_dotenv
from twilio.rest import Client

import os

load_dotenv()

client = Client(
    os.getenv("TWILIO_ACCOUNT_SID"),
    os.getenv("TWILIO_AUTH_TOKEN"),
)

message = client.messages.create(
    from_=os.getenv("TWILIO_WHATSAPP_FROM"),
    to=os.getenv("TWILIO_WHATSAPP_TO"),
    body="🎉 MailMindAI is successfully connected to WhatsApp!"
)

print("Message SID:", message.sid)
print("Message Status:", message.status)