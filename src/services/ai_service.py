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
You are an AI email extraction engine.

Your task is to analyse the email below.

Return ONLY valid JSON.

Do not explain your reasoning.

Do not use markdown.

Do not wrap the JSON inside triple backticks.

If the email is NOT related to recruitment, interviews, job applications, hiring, assessments, offers, recruiters or careers, return:

{{
    "is_recruitment": false,
    "company": "",
    "role": "",
    "interview_date": "",
    "action_required": "",
    "confidence": 0.0
}}

Otherwise return exactly this schema:

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
        """
        Sends an email to Ollama and returns
        a Python dictionary.
        """

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

            response = cls._clean_response(result.stdout)

            return json.loads(response)

        except Exception as ex:

            return {
                "is_recruitment": False,
                "company": "",
                "role": "",
                "interview_date": "",
                "action_required": "",
                "confidence": 0.0,
                "error": str(ex),
            }

    @staticmethod
    def _clean_response(response: str) -> str:
        """
        Cleans the response returned by the LLM
        before parsing it as JSON.
        """

        if not response:
            return "{}"

        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        # Sometimes the model writes text before or
        # after the JSON. Keep only the JSON object.
        start = response.find("{")
        end = response.rfind("}")

        if start != -1 and end != -1:
            response = response[start:end + 1]

        return response