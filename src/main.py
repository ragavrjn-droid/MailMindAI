from services.gmail_service import GmailService


def main():

    print("=" * 50)
    print("MailMindAI")
    print("=" * 50)

    gmail = GmailService()

    gmail.authenticate()

    emails = gmail.search_emails(
        query="is:unread",
        limit=10,
    )

    if emails:
        print(f"\nFound {len(emails)} unread email(s)")
        print("=" * 50)

        for index, email in enumerate(emails, start=1):
            print(f"\nEmail #{index}")
            print("-" * 50)
            print(f"From    : {email.sender}")
            print(f"Subject : {email.subject}")
            print(f"Date    : {email.date}")

            preview = email.body.strip() if email.body else "(No body found)"
            if len(preview) > 300:
                preview = preview[:300] + "..."

            print("\nBody Preview")
            print("-" * 50)
            print(preview)
    else:
        print("\nNo unread emails found.")

    print("\nApplication finished.")


if __name__ == "__main__":
    main()
