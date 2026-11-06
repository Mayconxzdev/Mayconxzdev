# ArsenalMind Universal

**MCP tooling and technology research for coding agents**

[Back to profile](../README.en.md) · [Português](ARSENALMIND.md) · [Desapega AI](DESAPEGA.en.md)

## Why I built it

I use Codex and Antigravity across different projects. New libraries, models and skills appear all the time, but coding agents tend to recommend tools they already know. I wanted a practical way to discover and compare alternatives instead of trusting the first suggestion.

ArsenalMind became my local MCP tooling and research setup. It is **not** an autonomous agent that builds everything for me.

## What is in it

- An MCP server for tool discovery, diagnostics and planning.
- A technology radar that collects and keeps track of public-source leads.
- Solution Scout for comparing candidate repositories and documentation.
- Reusable skills for discovery, critical review and delivery checks.

A search result is **not** an approved dependency. I still review licenses, compatibility, maintenance, security and whether a tool actually works.

## Used while building Desapega AI

On October 30, 2026, I used ArsenalMind to research local models and integration options for [Desapega AI](DESAPEGA.en.md), a resale assistant I built for my brother. I compared options and risks, then made the implementation decisions in Desapega itself.

That is a real example of research support, **not** a claim that ArsenalMind wrote the project by itself or improved its performance by a measured percentage.

## Runnable example

I published the [Capability Watch module](../samples/arsenalmind-capability-watch/README.md) from my personal ArsenalMind kit. It includes the real metadata radar code and offline tests. It does not include the complete private MCP setup.

## Technical decisions

I keep tool execution separate from reusable instructions, avoid automatically installing newly discovered code and retain research history so I can revisit decisions.

I use the personal 2.3.0 kit, which includes MCP runtime 2.2.1 plus newer research/skills modules. Parts have tests and integration records, but the complete private installation is not distributed here. My next goal is a reproducible comparison of an agent working on the same task with and without ArsenalMind.
