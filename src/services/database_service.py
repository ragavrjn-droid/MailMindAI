import sqlite3
from pathlib import Path


class DatabaseService:
    """
    Handles all SQLite operations.

    Responsibilities:
        - Create database
        - Create tables
        - Check whether an email has already been processed
        - Save processed emails
    """

    DATABASE_PATH = Path("database/mailmindai.db")

    def __init__(self):

        self.DATABASE_PATH.parent.mkdir(exist_ok=True)

        self.connection = sqlite3.connect(self.DATABASE_PATH)
        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):
        """
        Creates the processed_emails table
        if it does not already exist.
        """

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS processed_emails (

                message_id TEXT PRIMARY KEY,

                sender TEXT,

                subject TEXT,

                processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

            )
        """)

        self.connection.commit()

    def is_processed(self, message_id: str) -> bool:
        """
        Returns True if this Gmail message
        has already been analysed.
        """

        self.cursor.execute(
            """
            SELECT 1
            FROM processed_emails
            WHERE message_id = ?
            """,
            (message_id,)
        )

        return self.cursor.fetchone() is not None

    def mark_processed(self, email):
        """
        Saves an email as processed.
        """

        self.cursor.execute(
            """
            INSERT OR IGNORE INTO processed_emails
            (
                message_id,
                sender,
                subject
            )
            VALUES (?, ?, ?)
            """,
            (
                email.message_id,
                email.sender,
                email.subject,
            )
        )

        self.connection.commit()

    def close(self):
        """
        Close database connection.
        """

        self.connection.close()