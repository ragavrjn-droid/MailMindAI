# MailMindAI - System Architecture

## Project Goal

MailMindAI is an autonomous AI agent that monitors Gmail for job-related emails, understands them using a local Large Language Model (LLM), extracts structured interview information, and sends WhatsApp notifications.

---

# High-Level Architecture

                     Gmail
                        │
                        ▼
              Gmail Authentication
                        │
                        ▼
               Email Collector
          (Inbox + Spam/Junk)
                        │
                        ▼
           Lightweight Rule Filter
        (Keywords + Sender Analysis)
                        │
            ┌───────────┴────────────┐
            │                        │
      Ignore Email            Possible Job Email
            │                        │
            ▼                        ▼
        Save State             Local AI (Qwen)
                                    │
                                    ▼
                        Structured JSON Extraction
                                    │
                                    ▼
                           Guardrails Validation
                                    │
                    ┌───────────────┴───────────────┐
                    │                               │
                Ignore                        Valid Interview
                    │                               │
                    ▼                               ▼
              Save Result                 WhatsApp Notification
                    │                               │
                    └───────────────┬───────────────┘
                                    ▼
                              SQLite Database

---

# Components

## Gmail Service

Responsible for:

- OAuth Authentication
- Reading Inbox
- Reading Spam/Junk
- Downloading email contents

---

## Rule Engine

Before using AI, perform inexpensive checks.

Examples:

- Recruiter domains
- Keywords
- Careers emails

Purpose:

Reduce unnecessary AI processing.

---

## AI Service

Uses a local LLM through Ollama.

Responsibilities:

- Understand email
- Extract structured information
- Determine interview relevance
- Generate JSON output

---

## Guardrails

Validate AI output before taking action.

Checks include:

- Valid JSON
- Required fields
- Confidence threshold
- Interview category

---

## Notification Service

Initially:

- WhatsApp

Future:

- Telegram
- Slack
- Discord
- Email

---

## Database

SQLite stores:

- Processed Email IDs
- AI Results
- Processing Time
- Notification Status

Purpose:

Prevent duplicate processing.

---

# Design Principles

- Modular Architecture
- Single Responsibility Principle
- Loose Coupling
- AI as a Decision Layer
- Configuration Driven
- Local First

## Authentication

MailMindAI authenticates using Google's OAuth Desktop Application flow.

The first run opens a browser for user consent.

Google returns an OAuth token.

Subsequent runs reuse the saved token until it expires.

No passwords are stored.

                    MailMindAI v1

                +------------------+
                |     Scheduler    |
                +---------+--------+
                          |
                          v
                +------------------+
                |   Gmail Service  |
                +---------+--------+
                          |
                          v
                +------------------+
                |   Email Parser   |
                +---------+--------+
                          |
                          v
                +------------------+
                | Candidate Filter |
                +---------+--------+
                          |
                          v
                +------------------+
                | Ollama (Qwen)    |
                +---------+--------+
                          |
                          v
                +------------------+
                |   Guardrails     |
                +---------+--------+
                          |
                          v
                +------------------+
                |     SQLite       |
                +---------+--------+
                          |
                          v
                +------------------+
                | WhatsApp Service |
                +------------------+