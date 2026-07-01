class GuardrailService:
    """
    Validates AI output before MailMindAI
    performs any automation.

    Responsibility:
        AI JSON -> Safe decision
    """

    MIN_CONFIDENCE = 0.70

    @classmethod
    def validate(cls, result: dict) -> tuple[bool, str]:
        """
        Returns:

            (True, "Valid")

        or

            (False, "Reason")
        """

        if "error" in result:
            return False, "AI returned an error."

        if not result.get("is_recruitment", False):
            return False, "Not a recruitment email."

        confidence = float(result.get("confidence", 0.0))

        if confidence < cls.MIN_CONFIDENCE:
            return False, "Confidence below threshold."

        company = result.get("company", "").strip()

        if not company:
            return False, "Company not detected."

        return True, "Valid"