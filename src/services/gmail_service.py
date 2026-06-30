from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


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

    def get_latest_email(self):
        """Fetch the newest email from the inbox."""

        service = build("gmail", "v1", credentials=self.creds)

        results = (
            service.users()
            .messages()
            .list(userId="me", maxResults=1)
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
                format="metadata",
            )
            .execute()
        )

        email = {
            "from": "",
            "subject": "",
            "date": "",
        }

        for header in message["payload"]["headers"]:
            if header["name"] == "From":
                email["from"] = header["value"]
            elif header["name"] == "Subject":
                email["subject"] = header["value"]
            elif header["name"] == "Date":
                email["date"] = header["value"]

        return email
