class NotificationService:
    """
    Handles all user notifications.

    Currently notifications are printed to
    the console.

    Later this service will send WhatsApp
    messages without changing the rest of
    the application.
    """

    @staticmethod
    def send(result: dict):

        print("\n" + "=" * 60)
        print("📬 NEW RECRUITMENT EMAIL")
        print("=" * 60)

        print(f"Company         : {result.get('company', 'Unknown')}")
        print(f"Role            : {result.get('role', 'Unknown')}")
        print(f"Interview Date  : {result.get('interview_date', 'Not provided')}")
        print(f"Action Required : {result.get('action_required', 'None')}")
        print(f"Confidence      : {result.get('confidence', 0.0)}")

        print("=" * 60)