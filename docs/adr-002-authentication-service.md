# ADR-002: Dedicated Gmail Service Layer

## Decision

All Gmail API interactions will be isolated inside gmail_service.py.

## Reason

Separating Gmail logic from application logic makes the code easier to maintain, test, and replace.

The main application should orchestrate workflows instead of containing API-specific implementation.

## Benefits

- Easier testing
- Better maintainability
- Cleaner architecture
- Supports future migration to Microsoft Outlook or IMAP without changing the application workflow