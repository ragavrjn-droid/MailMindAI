from services.polling_service import PollingService


def main():
    """
    MailMindAI application entry point.
    """

    polling_service = PollingService()
    polling_service.start()


if __name__ == "__main__":
    main()