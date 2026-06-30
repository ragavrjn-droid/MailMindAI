# Security Design

## Authentication

Uses OAuth 2.0.

The application never stores the user's Gmail password.

Google issues temporary access tokens after user consent.

---

## Permissions

The application follows the Principle of Least Privilege.

Only the minimum Gmail permissions required are requested.

---

## Credentials

OAuth credentials are stored locally.

credentials/

This directory is excluded from Git.

---

## AI

The LLM runs locally through Ollama.

No email content is sent to external AI providers.

---

## Notifications

WhatsApp messages contain only summarized interview information.

Sensitive email content is not transmitted unless explicitly configured.