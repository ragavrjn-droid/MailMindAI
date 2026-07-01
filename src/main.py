from services.gmail_service import GmailService
from services.ai_service import AIService


def main():

    print("=" * 50)
    print("MailMindAI")
    print("=" * 50)

    gmail = GmailService()
    gmail.authenticate()

    emails = gmail.search_emails(
        query="is:unread newer_than:1d",
        limit=10,
    )

    if not emails:
        print("\nNo unread emails found.")
        print("\nApplication finished.")
        return

    print(f"\nFound {len(emails)} unread email(s)")
    print("=" * 50)

    for index, email in enumerate(emails, start=1):

        print(f"\nAnalysing Email #{index}")
        print("-" * 50)

        result = AIService.analyze_email(email)

        print(f"From      : {email.sender}")
        print(f"Subject   : {email.subject}")
        print(f"Date      : {email.date}")

        print("\nAI Result")
        print("-" * 50)

        # AI failed
        if result.get("error"):

            print("Status : AI Error")
            print(f"Reason : {result['error']}")
            continue

        # Not recruitment
        if not result.get("is_recruitment", False):

            print("Status : Not a recruitment email")
            print(f"Confidence : {result.get('confidence', 0.0)}")
            continue

        # Recruitment email
        print("Status          : Recruitment Email")
        print(f"Company         : {result.get('company', '')}")
        print(f"Role            : {result.get('role', '')}")
        print(f"Interview Date  : {result.get('interview_date', '')}")
        print(f"Action Required : {result.get('action_required', '')}")
        print(f"Confidence      : {result.get('confidence', 0.0)}")

    print("\nApplication finished.")


if __name__ == "__main__":
    main()