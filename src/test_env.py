from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("TWILIO_ACCOUNT_SID"))
print(os.getenv("TWILIO_WHATSAPP_FROM"))
print(os.getenv("TWILIO_WHATSAPP_TO"))