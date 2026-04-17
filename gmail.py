#!/usr/bin/env python3
"""
gmail.py — Gmail CLI for Forward Motion Medical
Usage: python gmail.py <command> [args]

Commands:
  inbox [--max <n>]
  read <message_id>
  search "<query>" [--max <n>]
  send "<to>" "<subject>" "<body>" [--attach <file> ...]
  draft "<to>" "<subject>" "<body>" [--attach <file> ...]
  reply <message_id> "<body>" [--attach <file> ...]
  list-drafts [--max <n>]
  list-labels

Attachments:
  Use --attach to add files to a draft. Pass filenames (looked up in
  attachments/ folder) or full paths. Multiple files supported.
  Creates draft only — never auto-sends.
"""

import sys
import os
import json
import base64
import mimetypes
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

ATTACHMENTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "attachments")

try:
    from google.oauth2.credentials import Credentials
    from google.auth.transport.requests import Request
    from googleapiclient.discovery import build
except ImportError:
    print("ERROR: Google API packages not installed. Run: pip3 install google-auth google-auth-oauthlib google-api-python-client")
    sys.exit(1)

SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]
CREDS_DIR = os.path.expanduser("~/.gmail-mcp")
OAUTH_KEYS = os.path.join(CREDS_DIR, "gcp-oauth.keys.json")
TOKEN_FILE = os.path.join(CREDS_DIR, "credentials.json")


def get_service():
    """Authenticate and return a Gmail API service object."""
    if not os.path.exists(TOKEN_FILE):
        print("ERROR: No credentials found. Expected token at:", TOKEN_FILE)
        sys.exit(1)

    with open(TOKEN_FILE) as f:
        token_data = json.load(f)

    with open(OAUTH_KEYS) as f:
        keys_data = json.load(f)
    installed = keys_data.get("installed", {})

    creds = Credentials(
        token=token_data.get("access_token"),
        refresh_token=token_data.get("refresh_token"),
        token_uri=installed.get("token_uri", "https://oauth2.googleapis.com/token"),
        client_id=installed.get("client_id"),
        client_secret=installed.get("client_secret"),
        scopes=SCOPES,
    )

    if creds.expired or not creds.valid:
        creds.refresh(Request())
        # Save refreshed token
        new_token = {
            "access_token": creds.token,
            "refresh_token": creds.refresh_token,
            "scope": " ".join(SCOPES),
            "token_type": "Bearer",
        }
        with open(TOKEN_FILE, "w") as f:
            json.dump(new_token, f)

    return build("gmail", "v1", credentials=creds)


def fmt_date(timestamp_ms):
    """Format epoch milliseconds to readable date."""
    if not timestamp_ms:
        return "—"
    try:
        return datetime.fromtimestamp(int(timestamp_ms) / 1000).strftime("%Y-%m-%d %H:%M")
    except Exception:
        return str(timestamp_ms)


def get_header(headers, name):
    """Extract a header value from message headers list."""
    for h in headers:
        if h["name"].lower() == name.lower():
            return h["value"]
    return "—"


def get_body_text(payload):
    """Extract plain text body from message payload. Ignores attachments."""
    if payload.get("mimeType") == "text/plain" and "data" in payload.get("body", {}):
        return base64.urlsafe_b64decode(payload["body"]["data"]).decode("utf-8", errors="replace")

    parts = payload.get("parts", [])
    for part in parts:
        # Skip attachments entirely
        if part.get("filename"):
            continue
        if part.get("mimeType") == "text/plain" and "data" in part.get("body", {}):
            return base64.urlsafe_b64decode(part["body"]["data"]).decode("utf-8", errors="replace")
        # Recurse into multipart
        if part.get("mimeType", "").startswith("multipart/"):
            result = get_body_text(part)
            if result:
                return result

    return "(no plain text body)"


# --- INBOX ---

def inbox(max_results=15):
    service = get_service()
    results = service.users().messages().list(
        userId="me", labelIds=["INBOX"], maxResults=max_results
    ).execute()
    messages = results.get("messages", [])

    if not messages:
        print("Inbox is empty.")
        return

    print(f"\nInbox ({len(messages)} messages):\n")
    for msg_info in messages:
        msg = service.users().messages().get(
            userId="me", id=msg_info["id"], format="metadata",
            metadataHeaders=["From", "Subject", "Date"]
        ).execute()
        headers = msg.get("payload", {}).get("headers", [])
        snippet = msg.get("snippet", "")[:80]
        print(f"  [{msg_info['id']}]")
        print(f"    From:    {get_header(headers, 'From')}")
        print(f"    Subject: {get_header(headers, 'Subject')}")
        print(f"    Date:    {get_header(headers, 'Date')}")
        print(f"    Preview: {snippet}")
        print()


# --- READ ---

def read_message(message_id):
    service = get_service()
    msg = service.users().messages().get(
        userId="me", id=message_id, format="full"
    ).execute()
    headers = msg.get("payload", {}).get("headers", [])
    body = get_body_text(msg.get("payload", {}))

    print(f"\nMessage: {message_id}")
    print(f"  From:    {get_header(headers, 'From')}")
    print(f"  To:      {get_header(headers, 'To')}")
    print(f"  Subject: {get_header(headers, 'Subject')}")
    print(f"  Date:    {get_header(headers, 'Date')}")
    print(f"\n{body}")


# --- SEARCH ---

def search(query, max_results=10):
    service = get_service()
    results = service.users().messages().list(
        userId="me", q=query, maxResults=max_results
    ).execute()
    messages = results.get("messages", [])

    if not messages:
        print(f"No messages found for: {query}")
        return

    print(f"\nSearch results for '{query}' ({len(messages)} messages):\n")
    for msg_info in messages:
        msg = service.users().messages().get(
            userId="me", id=msg_info["id"], format="metadata",
            metadataHeaders=["From", "Subject", "Date"]
        ).execute()
        headers = msg.get("payload", {}).get("headers", [])
        snippet = msg.get("snippet", "")[:80]
        print(f"  [{msg_info['id']}]")
        print(f"    From:    {get_header(headers, 'From')}")
        print(f"    Subject: {get_header(headers, 'Subject')}")
        print(f"    Date:    {get_header(headers, 'Date')}")
        print(f"    Preview: {snippet}")
        print()


# --- DRAFT / SEND (always creates draft, never sends) ---

def resolve_attachment(path):
    """Resolve an attachment path. Bare filenames are looked up in attachments/ folder."""
    if os.path.isabs(path) or os.sep in path:
        full = path
    else:
        full = os.path.join(ATTACHMENTS_DIR, path)
    if not os.path.isfile(full):
        print(f"ERROR: Attachment not found: {full}")
        sys.exit(1)
    return full


def build_message(to, subject, body, attachments=None):
    """Build a MIME message, with optional attachments."""
    if not attachments:
        msg = MIMEText(body)
        msg["to"] = to
        msg["subject"] = subject
        return msg

    msg = MIMEMultipart("mixed")
    msg["to"] = to
    msg["subject"] = subject
    msg.attach(MIMEText(body))

    for filepath in attachments:
        filepath = resolve_attachment(filepath)
        content_type, _ = mimetypes.guess_type(filepath)
        if content_type is None:
            content_type = "application/octet-stream"
        main_type, sub_type = content_type.split("/", 1)
        with open(filepath, "rb") as f:
            part = MIMEBase(main_type, sub_type)
            part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", "attachment", filename=os.path.basename(filepath))
        msg.attach(part)

    return msg


def create_draft(to, subject, body, attachments=None):
    service = get_service()
    message = build_message(to, subject, body, attachments)
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    draft = service.users().drafts().create(
        userId="me", body={"message": {"raw": raw}}
    ).execute()
    print(f"Draft created (ID: {draft['id']})")
    print(f"  To:      {to}")
    print(f"  Subject: {subject}")
    if attachments:
        for a in attachments:
            print(f"  Attach:  {os.path.basename(resolve_attachment(a))}")
    print("  >> Open Gmail to review and send.")


# --- REPLY (creates draft reply, never sends) ---

def reply(message_id, body_text, attachments=None):
    service = get_service()
    original = service.users().messages().get(
        userId="me", id=message_id, format="metadata",
        metadataHeaders=["From", "Subject", "Message-ID", "To"]
    ).execute()
    headers = original.get("payload", {}).get("headers", [])
    thread_id = original.get("threadId")

    original_from = get_header(headers, "From")
    original_subject = get_header(headers, "Subject")
    message_id_header = get_header(headers, "Message-ID")

    reply_subject = original_subject if original_subject.startswith("Re:") else f"Re: {original_subject}"

    message = build_message(original_from, reply_subject, body_text, attachments)
    if message_id_header != "—":
        message["In-Reply-To"] = message_id_header
        message["References"] = message_id_header

    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    draft = service.users().drafts().create(
        userId="me", body={"message": {"raw": raw, "threadId": thread_id}}
    ).execute()
    print(f"Draft reply created (ID: {draft['id']})")
    print(f"  To:      {original_from}")
    print(f"  Subject: {reply_subject}")
    if attachments:
        for a in attachments:
            print(f"  Attach:  {os.path.basename(resolve_attachment(a))}")
    print("  >> Open Gmail to review and send.")


# --- SEND DRAFT ---

def send_draft(draft_id):
    service = get_service()
    result = service.users().drafts().send(
        userId="me", body={"id": draft_id}
    ).execute()
    print(f"Sent (message ID: {result['id']})")


# --- LIST DRAFTS ---

def list_drafts(max_results=10):
    service = get_service()
    results = service.users().drafts().list(userId="me", maxResults=max_results).execute()
    drafts = results.get("drafts", [])

    if not drafts:
        print("No drafts found.")
        return

    print(f"\nDrafts ({len(drafts)}):\n")
    for d in drafts:
        draft = service.users().drafts().get(userId="me", id=d["id"], format="metadata").execute()
        headers = draft.get("message", {}).get("payload", {}).get("headers", [])
        print(f"  [{d['id']}]")
        print(f"    To:      {get_header(headers, 'To')}")
        print(f"    Subject: {get_header(headers, 'Subject')}")
        print()


# --- LIST LABELS ---

def list_labels():
    service = get_service()
    results = service.users().labels().list(userId="me").execute()
    labels = results.get("labels", [])

    if not labels:
        print("No labels found.")
        return

    print(f"\nLabels ({len(labels)}):\n")
    for label in sorted(labels, key=lambda l: l["name"]):
        print(f"  {label['name']}  [ID: {label['id']}]")


# --- CLI DISPATCH ---

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    cmd = sys.argv[1]
    args = sys.argv[2:]

    def get_max(default=10):
        if "--max" in args:
            idx = args.index("--max")
            return int(args[idx + 1])
        return default

    def get_attachments():
        """Extract --attach values from args. Returns (remaining_args, attachments)."""
        remaining = []
        attach_list = []
        i = 0
        a = list(args)
        while i < len(a):
            if a[i] == "--attach":
                i += 1
                while i < len(a) and not a[i].startswith("--"):
                    attach_list.append(a[i])
                    i += 1
            else:
                remaining.append(a[i])
                i += 1
        return remaining, attach_list or None

    if cmd == "inbox":
        inbox(get_max(15))

    elif cmd == "read":
        if not args:
            print("Usage: python gmail.py read <message_id>")
            sys.exit(1)
        read_message(args[0])

    elif cmd == "search":
        if not args:
            print('Usage: python gmail.py search "<query>"')
            sys.exit(1)
        query = args[0] if "--max" not in args else args[0]
        search(query, get_max(10))

    elif cmd in ("send", "draft"):
        clean_args, attachments = get_attachments()
        if len(clean_args) < 3:
            print('Usage: python gmail.py send "<to>" "<subject>" "<body>" [--attach <file> ...]')
            sys.exit(1)
        create_draft(clean_args[0], clean_args[1], " ".join(clean_args[2:]), attachments)

    elif cmd == "reply":
        clean_args, attachments = get_attachments()
        if len(clean_args) < 2:
            print('Usage: python gmail.py reply <message_id> "<body>" [--attach <file> ...]')
            sys.exit(1)
        reply(clean_args[0], " ".join(clean_args[1:]), attachments)

    elif cmd == "send-draft":
        if not args:
            print("Usage: python gmail.py send-draft <draft_id>")
            sys.exit(1)
        send_draft(args[0])

    elif cmd == "list-drafts":
        list_drafts(get_max(10))

    elif cmd == "list-labels":
        list_labels()

    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
