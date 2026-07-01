import json
import subprocess

from models.email import Email


class AIService:
    """
    Connects MailMindAI to the local Ollama model.

    Responsibility:
        Email -> AI -> JSON -> Python dictionary
    """

    MODEL = "gemma3:4b"

    PROMPT_TEMPLATE = """
You are an AI email classifier.

Return ONLY valid JSON.

Do not explain.

Do not think aloud.

Do not use markdown.

Do not output any text before or after the JSON.

IMPORTANT:

A recruitment email is a PERSONAL communication regarding a job application.

Examples:

- Interview invitation
- Recruiter outreach
- HR communication
- Assessment invitation
- Coding challenge
- Offer letter
- Application status update

These are NOT recruitment emails:

- Job alerts
- Job recommendations
- Career newsletters
- Marketing emails
- Company newsletters
- Promotional emails

If the email is NOT a recruitment email, return:

{{
    "is_recruitment": false,
    "company": "",
    "role": "",
    "interview_date": "",
    "action_required": "",
    "confidence": 0.0
}}

Otherwise return:

{{
    "is_recruitment": true,
    "company": "",
    "role": "",
    "interview_date": "",
    "action_required": "",
    "confidence": 0.0
}}

Email

From:
{sender}

Subject:
{subject}

Body:
{body}
"""

    @classmethod
    def analyze_email(cls, email: Email) -> dict:

        prompt = cls.PROMPT_TEMPLATE.format(
            sender=email.sender,
            subject=email.subject,
            body=email.body,
        )

        try:

            result = subprocess.run(
                [
                    "ollama",
                    "run",
                    cls.MODEL,
                ],
                input=prompt,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="ignore",
            )

            if result.returncode != 0:
                return cls._default_response(result.stderr.strip())

            response = cls._clean_response(result.stdout)

            return json.loads(response)

        except Exception as ex:

            return cls._default_response(str(ex))

    @staticmethod
    def _clean_response(response: str) -> str:

        if not response:
            return "{}"

        response = response.replace("```json", "")
        response = response.replace("```", "")

        response = response.replace("<think>", "")
        response = response.replace("</think>", "")

        response = response.replace("\x00", "")

        response = response.strip()

        start = response.find("{")
        end = response.rfind("}")

        if start == -1 or end == -1:
            return "{}"

        response = response[start:end + 1]

        return response

    @staticmethod
    def _default_response(error: str = "") -> dict:

        return {
            "is_recruitment": False,
            "company": "",
            "role": "",
            "interview_date": "",
            "action_required": "",
            "confidence": 0.0,
            "error": error,
        }