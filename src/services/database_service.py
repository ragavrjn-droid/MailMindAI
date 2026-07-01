import sqlite3
from pathlib import Path


class DatabaseService:
    """
    Handles all SQLite operations.

    Responsibilities:
        - Create database
        - Create tables
        - Check processed emails
        - Save AI analysis
    """

    DATABASE_PATH = Path("database/mailmindai.db")

    def __init__(self):

        self.DATABASE_PATH.parent.mkdir(exist_ok=True)

        self.connection = sqlite3.connect(self.DATABASE_PATH)
        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):
        """
        Creates the processed_emails table.
        """

        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS processed_emails (

                message_id TEXT PRIMARY KEY,

                sender TEXT NOT NULL,

                subject TEXT NOT NULL,

                company TEXT,

                role TEXT,

                interview_date TEXT,

                action_required TEXT,

                confidence REAL,

                is_recruitment INTEGER,

                processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

            )
            """
        )

        self.connection.commit()

    def is_processed(self, message_id: str) -> bool:
        """
        Returns True if the email
        has already been analysed.
        """

        self.cursor.execute(
            """
            SELECT 1
            FROM processed_emails
            WHERE message_id = ?
            """,
            (message_id,),
        )

        return self.cursor.fetchone() is not None

    def mark_processed(self, email, result: dict):
        """
        Saves an analysed email.
        """

        self.cursor.execute(
            """
            INSERT OR IGNORE INTO processed_emails
            (

                message_id,

                sender,

                subject,

                company,

                role,

                interview_date,

                action_required,

                confidence,

                is_recruitment

            )

            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                email.message_id,
                email.sender,
                email.subject,
                result.get("company", ""),
                result.get("role", ""),
                result.get("interview_date", ""),
                result.get("action_required", ""),
                result.get("confidence", 0.0),
                int(result.get("is_recruitment", False)),
            ),
        )

        self.connection.commit()

    def get_all_processed(self):
        """
        Returns all processed emails.
        Useful later for dashboards.
        """

        self.cursor.execute(
            """
            SELECT *
            FROM processed_emails
            ORDER BY processed_at DESC
            """
        )

        return self.cursor.fetchall()

    def close(self):
        """
        Closes the SQLite connection.
        """

        self.connection.close()