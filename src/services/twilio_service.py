import os

from dotenv import load_dotenv
from twilio.rest import Client


load_dotenv()


class TwilioService:
    """
    Handles all Twilio WhatsApp communication.

    Responsibility:
        Send WhatsApp notifications.
    """

    def __init__(self):

        self.client = Client(
            os.getenv("TWILIO_ACCOUNT_SID"),
            os.getenv("TWILIO_AUTH_TOKEN"),
        )

        self.from_number = os.getenv("TWILIO_WHATSAPP_FROM")
        self.to_number = os.getenv("TWILIO_WHATSAPP_TO")

    def send_message(self, message: str):

        twilio_message = self.client.messages.create(

            from_=self.from_number,
            to=self.to_number,
            body=message,

        )

        return twilio_message.sid