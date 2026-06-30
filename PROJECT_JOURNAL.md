# MailMindAI - AI Email Monitoring Agent

## Goal

Build an autonomous AI agent that:

- Monitors Gmail Inbox and Spam folders
- Uses a local LLM (Qwen via Ollama) to classify emails
- Extracts interview details into structured JSON
- Sends WhatsApp notifications
- Stores processed emails in SQLite
- Prevents duplicate notifications

---

## Tech Stack

- Python 3.14
- Gmail API
- Ollama
- Qwen
- SQLite
- Playwright
- APScheduler

---

## Architecture (Planned)

Scheduler
    ↓
Gmail Service
    ↓
Email Parser
    ↓
AI Classifier
    ↓
Guardrails
    ↓
Notification Service
    ↓
SQLite