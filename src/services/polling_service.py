import time

from services.pipeline_service import PipelineService


class PollingService:
    """
    Runs MailMindAI continuously.

    Responsibilities:
        - Authenticate Gmail once
        - Execute the pipeline periodically
        - Display application status
    """

    POLL_INTERVAL = 60  # seconds

    def __init__(self):

        self.pipeline = PipelineService()

    def start(self):

        print("=" * 50)
        print("MailMindAI Started")
        print("=" * 50)

        # Authenticate Gmail once
        self.pipeline.authenticate()

        try:

            while True:

                print("\nChecking Gmail...\n")

                results = self.pipeline.run()

                if not results:
                    print("No new emails to process.")

                else:
                    print(f"Processed {len(results)} new email(s).")

                print(f"\nSleeping {self.POLL_INTERVAL} seconds...\n")

                time.sleep(self.POLL_INTERVAL)

        except KeyboardInterrupt:

            print("\nStopping MailMindAI...")

        finally:

            self.pipeline.close()