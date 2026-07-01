from models.email import Email


class CandidateFilter:
    """
    Very lightweight pre-filter.

    Its only job is to remove emails that obviously
    cannot be useful before sending them to the AI.

    The AI is responsible for deciding whether an
    email is about recruitment.
    """

    MIN_BODY_LENGTH = 20

    @classmethod
    def is_candidate(cls, email: Email) -> bool:
        """
        Returns True if an email should be analysed by
        the AI model.
        """

        if not email:
            return False

        body = (email.body or "").strip()

        # Ignore completely empty emails
        if len(body) < cls.MIN_BODY_LENGTH:
            return False

        return True