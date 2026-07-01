from dataclasses import dataclass


@dataclass
class Email:
    """
    Represents a Gmail message inside MailMindAI.
    """

    message_id: str
    thread_id: str

    sender: str
    subject: str
    date: str

    body: str = ""

    label_ids: list[str] | None = None