from services.gmail_service import GmailService
from services.ai_service import AIService
from services.guardrail_service import GuardrailService
from services.database_service import DatabaseService
from services.notification_service import NotificationService


class PipelineService:
    """
    Executes one MailMindAI processing cycle.

    Responsibilities:
        - Retrieve unread emails
        - Skip already processed emails
        - Analyse emails using AI
        - Validate AI output
        - Send WhatsApp notification
        - Store processed emails
        - Return structured results
    """

    def __init__(self):

        self.gmail = GmailService()
        self.database = DatabaseService()
        self.notification = NotificationService()

    def authenticate(self):
        """
        Authenticate Gmail once when the application starts.
        """

        self.gmail.authenticate()

    def run(self):
        """
        Execute one pipeline cycle.

        Returns:
            List of dictionaries containing processing results.
        """

        emails = self.gmail.search_emails(
            query="is:unread newer_than:1d",
            limit=10,
        )

        results = []

        if not emails:
            return results

        for email in emails:

            # Skip emails already processed
            if self.database.is_processed(email.message_id):
                continue

            ai_result = AIService.analyze_email(email)

            is_valid, reason = GuardrailService.validate(ai_result)

            pipeline_result = {
                "email": email,
                "ai_result": ai_result,
                "valid": is_valid,
                "reason": reason,
            }

            results.append(pipeline_result)

            # Send WhatsApp notification only for valid recruitment emails
            if is_valid:
                try:
                    self.notification.send(ai_result)
                except Exception as ex:
                    print(f"Notification Error: {ex}")
                    continue

            # Save only after successful processing
            self.database.mark_processed(email, ai_result)

        return results

    def close(self):
        """
        Close database connection.
        """

        self.database.close()