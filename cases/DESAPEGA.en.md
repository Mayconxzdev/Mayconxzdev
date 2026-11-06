# Desapega AI

**A resale assistant I built for my brother**

[Back to profile](../README.en.md) · [Português](DESAPEGA.md) · [ArsenalMind research](ARSENALMIND.en.md)

## The problem

My brother resells used products. Preparing listings, checking prices and keeping up with interested buyers takes time. I wanted to make that work easier with a conversational assistant, without taking control of important sales decisions away from him.

## What I worked on

- Python and SQLite for product records, pending actions and conversation state.
- Telegram as a simple interaction channel.
- Deterministic checks for minimum prices, commercial rules and human approvals.
- Duplicate-message handling, state recovery and synthetic workflow tests.
- Marketplace/browser integrations developed across different versions.

I also used ArsenalMind to research local AI models and integration risks.

## Real use and limits

My brother has used the assistant for resale suggestions and publishing listings. He reports that some listings were published automatically, not merely drafted. I still need to match those publications with the exact integration versions and platform confirmations before describing the feature as fully validated.

Some older documentation covers earlier assisted or unapproved integration paths. Local tests cover specific sales policies and workflow states, **not** every external platform end to end.

The complete installation is private because it contains account sessions and personal data. I am not claiming verified sales revenue, time savings or permanently supported marketplace integrations.
