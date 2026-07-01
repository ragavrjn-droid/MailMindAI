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

        if "error" in result:
            print(f"Error : {result['error']}")
            continue

        print(f"Recruitment     : {result['is_recruitment']}")
        print(f"Company         : {result['company']}")
        print(f"Role            : {result['role']}")
        print(f"Interview Date  : {result['interview_date']}")
        print(f"Action Required : {result['action_required']}")
        print(f"Confidence      : {result['confidence']}")

    print("\nApplication finished.")


if __name__ == "__main__":
    main()