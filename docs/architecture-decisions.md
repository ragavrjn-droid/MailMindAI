# ADR-001

## Decision

Use polling instead of Gmail Push Notifications for Version 1.

## Reason

- Simpler setup
- Easier local development
- Faster MVP
- Allows isolated testing of the Gmail pipeline

## Future

Replace with Gmail Push Notifications once the core system is stable.

# ADR-004: OAuth Credentials Storage

## Decision

OAuth credentials will be stored locally during development.

client_secret.json is ignored by Git.

token.json will be generated after first authentication and also ignored.

## Reason

Prevents accidental credential leaks.

Allows local development while keeping secrets out of source control.

## Future

Production deployments will use secure secret management.

## One Responsibility Per File

Each module should have a single, clear responsibility.

Examples:

- gmail_service.py → Gmail authentication and email retrieval
- ollama_service.py → Communication with Ollama
- notification_service.py → Sending WhatsApp notifications
- database_service.py → SQLite operations

Business logic should be orchestrated from `main.py`, not embedded inside service modules.