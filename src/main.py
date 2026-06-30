from services.gmail_service import GmailService


def main():

    print("=" * 50)
    print("MailMindAI")
    print("=" * 50)

    gmail = GmailService()

    gmail.authenticate()

    email = gmail.get_latest_email()

    if email:
        print("\nLatest Email")
        print("-" * 50)
        print(f"From    : {email['from']}")
        print(f"Subject : {email['subject']}")
        print(f"Date    : {email['date']}")
    else:
        print("Inbox is empty.")

    print("\nApplication finished.")


if __name__ == "__main__":
    main()
