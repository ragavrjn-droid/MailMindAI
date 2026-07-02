from services.twilio_service import TwilioService


class NotificationService:
    """
    Handles user notifications.

    Responsibility:
        - Format recruitment notifications
        - Delegate message delivery to TwilioService
    """

    def __init__(self):

        self.twilio = TwilioService()

    def send(self, result: dict):
        """
        Sends a WhatsApp notification for
        a recruitment email.
        """

        message = f"""
📬 MailMindAI detected a recruitment email

🏢 Company: {result.get("company", "Unknown")}

💼 Role: {result.get("role", "Unknown")}

📅 Interview: {result.get("interview_date", "Not provided")}

✅ Action: {result.get("action_required", "None")}

🎯 Confidence: {result.get("confidence", 0.0)}
"""

        sid = self.twilio.send_message(message.strip())

        print("✅ WhatsApp notification sent.")
        print(f"Twilio SID: {sid}")