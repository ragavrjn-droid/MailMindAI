<p align="center">
  <img src="assets/banner.png" alt="MailMindAI Banner" width="100%">
</p>

# MailMindAI 🤖

> A privacy-first AI agent that monitors Gmail, detects recruitment emails using a local Large Language Model (LLM), extracts interview details, and instantly notifies you via WhatsApp.

MailMindAI runs entirely on your own computer using **Ollama** and **Gemma 3**, allowing recruitment email monitoring without sending your personal emails to cloud AI providers.

The project explores how local Large Language Models can be combined with workflow automation to build practical AI applications while keeping user data private.

> **Current Release:** v0.1.0

---

# Why MailMindAI?

MailMindAI demonstrates an end-to-end AI automation workflow.

It continuously monitors Gmail, identifies genuine recruitment emails, extracts interview information, stores processing history, and instantly sends WhatsApp notifications.

The entire pipeline runs locally, combining traditional software engineering with modern Large Language Models.

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

A visual architecture diagram is shown below.

<p align="center">
  <img src="assets/architecture.png" alt="Architecture Diagram" width="95%">
</p>

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

# Installation

Clone the repository:

```bash
git clone https://github.com/ragavrjn-droid/MailMindAI.git
cd MailMindAI
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure your Gmail OAuth credentials, Twilio credentials, and install Ollama with the Gemma 3 model before running the application.

---

# Current Release (v0.1.0)

Included in this release:

- ✅ Continuous Gmail monitoring
- ✅ Local AI email classification
- ✅ AI guardrails
- ✅ Interview detail extraction
- ✅ SQLite persistence
- ✅ WhatsApp notifications
- ✅ Duplicate email prevention
- ✅ Background polling

---

# Contributing

Contributions are welcome.

If you'd like to improve the project, feel free to:

- Open an Issue
- Submit a Pull Request
- Start a discussion

---

# License

This project is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**.

See the `LICENSE` file for details.

---

# Project Status

MailMindAI is under active development.

The focus is on building practical, privacy-first AI automation using local Large Language Models.

---

# Support

If you found this project interesting:

- ⭐ Star the repository
- 🐛 Report bugs
- 💡 Suggest improvements
- 📢 Share it with others

---

Built with ❤️ using Python, Ollama and Local AI.