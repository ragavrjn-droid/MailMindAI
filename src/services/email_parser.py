from bs4 import BeautifulSoup
import re


class EmailParser:
    """
    Cleans raw Gmail email bodies.

    Responsibilities:
    - Convert HTML emails into plain text
    - Remove scripts and styles
    - Remove excessive blank lines
    - Return clean text ready for AI processing
    """

    @staticmethod
    def clean(text: str) -> str:
        """
        Clean an email body.

        Args:
            text: Raw email body from Gmail API

        Returns:
            Clean plain-text email body
        """

        if not text:
            return ""

        # Detect HTML emails
        lower = text.lower()

        if (
            "<html" in lower
            or "<body" in lower
            or "<div" in lower
            or "<table" in lower
        ):
            soup = BeautifulSoup(text, "html.parser")

            # Remove non-visible content
            for tag in soup(["script", "style"]):
                tag.decompose()

            # Convert HTML → plain text
            text = soup.get_text(separator="\n")

        # Remove leading/trailing whitespace
        lines = [line.strip() for line in text.splitlines()]

        # Remove empty lines
        lines = [line for line in lines if line]

        text = "\n".join(lines)

        # Collapse multiple blank lines
        text = re.sub(r"\n{3,}", "\n\n", text)

        return text.strip()