import time

from services.pipeline_service import PipelineService
from services.notification_service import NotificationService


class PollingService:
    """
    Runs MailMindAI continuously.

    Responsibilities:
        - Authenticate Gmail once
        - Execute the pipeline periodically
        - Notify the user about recruitment emails
    """

    POLL_INTERVAL = 60  # seconds

    def __init__(self):

        self.pipeline = PipelineService()

    def start(self):

        print("=" * 50)
        print("MailMindAI Started")
        print("=" * 50)

        # Authenticate Gmail only once
        self.pipeline.authenticate()

        try:

            while True:

                print("\nChecking Gmail...\n")

                results = self.pipeline.run()

                if not results:
                    print("No new emails to process.")

                for item in results:

                    email = item["email"]
                    result = item["ai_result"]

                    print("-" * 60)
                    print(f"Subject : {email.subject}")
                    print(f"From    : {email.sender}")

                    if not item["valid"]:
                        print(f"Skipped : {item['reason']}")
                        continue

                    NotificationService.send(result)

                print(f"\nSleeping {self.POLL_INTERVAL} seconds...\n")

                time.sleep(self.POLL_INTERVAL)

        except KeyboardInterrupt:

            print("\nStopping MailMindAI...")

        finally:

            self.pipeline.close()