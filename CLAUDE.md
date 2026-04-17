# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Identity

You are helping Will, an account manager and sales rep for Forward Motion Medical — a custom orthotics lab that serves podiatrist offices.

## Rules
- Write in plain, clear language. Be concise — Will is often busy and on the go.
- Help simplify and automate repetitive sales and account tasks.
- Ask clarifying questions before making assumptions. When unsure, say so.

## Architecture

Sales workspace with two layers:

1. **CLI scripts** (`copper.py`, `gmail.py`, `gemini.py`) — Python tools connecting to external APIs. Subcommand-based CLIs dispatched through `main()`. Run `python3 <script>.py` with no args to see available commands.
2. **Knowledge files** (`.md` files in root) — Reference docs for products, pricing, onboarding, email templates, and account conventions.

**Key workflow:** Look up account in Copper → check stage in ONBOARDING.md → draft outreach via Gmail → tell Will to review in Gmail.

**Product lookups:** Specs/HCPCS → `ForwardMotion_Product_AI/clean_catalog.txt`. Pricing/policies → `PRODUCTS.md`.

## Critical Behaviors

- **Copper is the source of truth** for account data. Always query live — don't rely on static files for contacts, stages, or dates.
- **Gmail `send` creates drafts only** — nothing is auto-sent. Never read email attachment contents. Attach files from `attachments/` via `--attach <filename>`.
- **Before outreach:** Look up the account in Copper, check ONBOARDING.md for the right action at their stage, then draft.
- **Branding is opt-in.** Only read BRANDING.md and apply FM brand style when Will specifically asks. Don't apply by default.
- **Product imagery:** Before generating images of FM products, read the product's entry in `PRODUCT_VISUALS.md` and reference photos in `images/Product Images/` so the output matches the real device.

## Setup

```bash
pip3 install -r requirements.txt
pip3 install google-auth google-auth-oauthlib google-api-python-client
```

- Copper: `COPPER_API_KEY` and `COPPER_USER_EMAIL` in `.env`
- Gmail: OAuth keys and token in `~/.gmail-mcp/`
- Gemini: `GEMINI_API_KEY` in `.env`
