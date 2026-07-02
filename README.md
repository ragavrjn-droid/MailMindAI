<p align="center">
  <img src="assets/banner.png" alt="MailMindAI Banner" width="100%">
</p>

# MailMindAI 🤖

> A privacy-first AI agent that monitors Gmail, detects recruitment emails using a local Large Language Model (LLM), extracts interview details, and instantly notifies you via WhatsApp.

MailMindAI runs entirely on your own computer using **Ollama** and **Gemma 3**, allowing you to automate recruitment email monitoring without sending your personal emails to cloud AI providers.

This project is the first building block of a much larger vision: **Career Assistant AI** — an open-source AI career companion designed to help people throughout their entire job search journey.

---

# Why MailMindAI?

Searching for a job is difficult enough without worrying about missing important recruiter emails.

MailMindAI automatically:

- Detects genuine recruitment emails
- Filters out newsletters and job alerts
- Extracts interview information
- Tracks processed emails
- Sends instant WhatsApp notifications

No more repeatedly checking Gmail or worrying about missing an interview invitation.

---

# Features

- 📧 Continuous Gmail monitoring
- 🧠 Local AI email classification (Ollama + Gemma 3)
- 🛡 AI guardrails to reduce false positives
- 📅 Interview detail extraction
- 💬 WhatsApp notifications via Twilio
- 🗄 SQLite database for processed email tracking
- 🔄 Background polling service
- ⚙ Modular service-based architecture
- 🔒 Privacy-first (runs locally)

---

# Architecture

```
                    Gmail API
                        │
                        ▼
                 GmailService
                        │
                        ▼
                  AIService
             (Ollama + Gemma 3)
                        │
                        ▼
              GuardrailService
                        │
          ┌─────────────┴─────────────┐
          ▼                           ▼
 DatabaseService             NotificationService
    (SQLite)                         │
                                     ▼
                              TwilioService
                                     │
                                     ▼
                                WhatsApp
```

---

# Workflow

```
New Gmail Email
        │
        ▼
MailMindAI Polling Service
        │
        ▼
AI Classification
        │
        ▼
Guardrail Validation
        │
        ▼
Save Processing State
        │
        ▼
WhatsApp Notification
```

---

# Tech Stack

- Python
- Gmail API
- Ollama
- Gemma 3
- SQLite
- Twilio WhatsApp API
- Git
- GitHub

---

# Project Structure

```
src/
│
├── models/
│   └── email.py
│
├── services/
│   ├── ai_service.py
│   ├── database_service.py
│   ├── gmail_service.py
│   ├── guardrail_service.py
│   ├── notification_service.py
│   ├── pipeline_service.py
│   ├── polling_service.py
│   └── twilio_service.py
│
├── utils/
│
└── main.py
```

---

# Current Capabilities

- ✅ Detect recruitment emails
- ✅ Ignore newsletters and marketing emails
- ✅ Extract interview information
- ✅ Prevent duplicate processing
- ✅ Persist processed emails using SQLite
- ✅ Send WhatsApp notifications
- ✅ Run continuously in the background

---

# Roadmap

## Version 0.1 (Current)

- ✅ Gmail Monitoring
- ✅ Local AI Classification
- ✅ AI Guardrails
- ✅ SQLite Persistence
- ✅ WhatsApp Notifications
- ✅ Background Polling

---

## Version 0.2

- 📅 Google Calendar Integration
- ⏰ Automatic Interview Scheduling
- 🔔 Interview Reminders

---

## Version 0.3

- 📄 Resume Parsing
- 🎯 AI Resume-to-Job Matching
- 📊 Match Scoring

---

## Version 0.4

- 🌍 Multi-source Job Search
- 💼 Job Recommendation Engine
- 📥 Job Deduplication

---

## Version 0.5

- 📝 Cover Letter Generation
- 📄 Resume Tailoring
- 📧 Follow-up Email Generation

---

## Version 1.0

### Career Assistant AI

An open-source AI assistant that helps job seekers throughout their career journey.

Features planned include:

- Job discovery
- AI-powered job matching
- Application tracking
- Recruitment email monitoring
- Interview scheduling
- Calendar integration
- Resume optimization
- Cover letter generation
- Interview preparation
- Career knowledge base (RAG)

---

# Vision

MailMindAI is the first module of a larger project called **Career Assistant AI**.

The long-term goal is to build a privacy-first, open-source AI career operating system that helps people from their first job search all the way to receiving an offer.

Everything will continue to run locally whenever possible, giving users complete control over their personal data.

---

# Contributing

Contributions are welcome.

If you have ideas, improvements, or bug fixes, feel free to:

- Open an Issue
- Submit a Pull Request
- Start a discussion

Every contribution helps improve the project.

---

# License

A license will be selected before the first stable release (v1.0).

Until then, the project remains under active development.

---

# Support the Project

If MailMindAI helps you during your job search, please consider:

- ⭐ Starring the repository
- 🐛 Reporting bugs
- 💡 Suggesting new features
- 📢 Sharing the project with others

Your support helps make the project better for everyone.

---

Built with ❤️ using Python, Ollama and Local AI.