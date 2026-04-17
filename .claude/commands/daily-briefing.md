Run a daily briefing for Will. Do the following:

1. **Open Copper tasks**: Run `python3 copper.py list-tasks --open-only` and highlight any that are overdue or due today.

2. **Unanswered emails**: Run `python3 gmail.py search "in:inbox after:$(date -v-1d +%Y/%m/%d) is:unread"` to find unread inbox messages from the last 24 hours. Filter out newsletters, marketing, and automated notifications — only flag messages from real people that look like they need a reply.

3. **Summary**: Present a short, scannable list:
   - Tasks due today or overdue
   - People waiting on a reply
   - Suggested next actions based on ONBOARDING.md stage guidance

Keep it concise — Will is busy and on the go.
