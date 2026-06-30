# ADR-001

## Title

Use Smart Polling for Version 1

## Status

Accepted

## Context

The application needs to detect new Gmail messages.

There are two approaches:

1. Poll Gmail periodically
2. Gmail Push Notifications

## Decision

Version 1 will use Smart Polling.

Polling will occur every 5 minutes.

Only emails newer than the previous check will be retrieved.

Only potential job-related emails will be sent to the AI.

## Why

- Easier local development
- No webhook required
- No Google Pub/Sub
- Easier debugging
- Faster MVP

## Future

Replace polling with Gmail Push Notifications in Version 2 without changing the AI pipeline.