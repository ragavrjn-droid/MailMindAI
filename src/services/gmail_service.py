from pathlib import Path
import base64

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from models.email import Email
from services.email_parser import EmailParser


SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly"
]


class GmailService:

    def __init__(self):
        self.creds = None

    def authenticate(self):

        credentials_path = Path("credentials/client_secret.json")
        token_path = Path("credentials/token.json")

        if token_path.exists():
            self.creds = Credentials.from_authorized_user_file(
                token_path,
                SCOPES
            )

        if (
            not self.creds
            or not self.creds.valid
        ):

            if (
                self.creds
                and self.creds.expired
                and self.creds.refresh_token
            ):
                self.creds.refresh(Request())

            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    credentials_path,
                    SCOPES
                )

                self.creds = flow.run_local_server(port=0)

            token_path.write_text(self.creds.to_json())

        print("✅ Gmail authentication successful")

    def _extract_body(self, payload: dict) -> str:
        """
        Extract the email body from the Gmail payload.

        Preference:
        1. text/plain
        2. first available body
        """

        if "parts" in payload:

            # Prefer plain text
            for part in payload["parts"]:

                if part.get("mimeType") == "text/plain":

                    data = part.get("body", {}).get("data")

                    if data:

                        return base64.urlsafe_b64decode(
                            data + "=" * (-len(data) % 4)
                        ).decode(
                            "utf-8",
                            errors="ignore"
                        )

            # Otherwise use first available part
            for part in payload["parts"]:

                data = part.get("body", {}).get("data")

                if data:

                    return base64.urlsafe_b64decode(
                        data + "=" * (-len(data) % 4)
                    ).decode(
                        "utf-8",
                        errors="ignore"
                    )

        data = payload.get("body", {}).get("data")

        if data:

            return base64.urlsafe_b64decode(
                data + "=" * (-len(data) % 4)
            ).decode(
                "utf-8",
                errors="ignore"
            )

        return ""

    def get_latest_email(self) -> Email | None:
        """
        Fetch the newest email from the inbox.
        """

        service = build(
            "gmail",
            "v1",
            credentials=self.creds
        )

        results = (
            service.users()
            .messages()
            .list(
                userId="me",
                maxResults=1,
            )
            .execute()
        )

        messages = results.get("messages", [])

        if not messages:
            return None

        message = (
            service.users()
            .messages()
            .get(
                userId="me",
                id=messages[0]["id"],
                format="full",
            )
            .execute()
        )

        headers = {
            header["name"]: header["value"]
            for header in message["payload"]["headers"]
        }

        return Email(
            message_id=message["id"],
            thread_id=message["threadId"],
            sender=headers.get("From", ""),
            subject=headers.get("Subject", ""),
            date=headers.get("Date", ""),
            body=EmailParser.clean(
                self._extract_body(message["payload"])
            ),
            label_ids=message.get("labelIds", []),
        )

    def search_emails(
        self,
        query: str,
        limit: int = 20,
    ) -> list[Email]:
        """
        Search Gmail and return Email objects.
        """

        service = build(
            "gmail",
            "v1",
            credentials=self.creds
        )

        results = (
            service.users()
            .messages()
            .list(
                userId="me",
                q=query,
                maxResults=limit,
            )
            .execute()
        )

        messages = results.get("messages", [])

        emails: list[Email] = []

        for item in messages:

            message = (
                service.users()
                .messages()
                .get(
                    userId="me",
                    id=item["id"],
                    format="full",
                )
                .execute()
            )

            headers = {
                header["name"]: header["value"]
                for header in message["payload"]["headers"]
            }

            emails.append(
                Email(
                    message_id=message["id"],
                    thread_id=message["threadId"],
                    sender=headers.get("From", ""),
                    subject=headers.get("Subject", ""),
                    date=headers.get("Date", ""),
                    body=EmailParser.clean(
                        self._extract_body(
                            message["payload"]
                        )
                    ),
                    label_ids=message.get("labelIds", []),
                )
            )

        return emails