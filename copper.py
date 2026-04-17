#!/usr/bin/env python3
"""
copper.py — Copper CRM CLI for Forward Motion Medical
Usage: python copper.py <command> [args]

Commands:
  search-contact <name_or_email>
  get-contact <id>
  search-company <name>
  get-company <id>
  list-people [--tag <tag>]
  list-opportunities [--stage <stage_id>]
  update-stage <opportunity_id> <pipeline_stage_id>
  log-activity <entity_type> <entity_id> "<note>"
  create-task "<title>" <entity_type> <entity_id> <due_date YYYY-MM-DD>
  create-contact "<first> <last>" "<email>" "<phone>" "<company>" "<title>"
  list-tasks [--open-only] [--mine] [--assignee <user_id>]
  list-stages <pipeline_id>
"""

import sys
import os
import json
import argparse
from datetime import datetime

try:
    import requests
except ImportError:
    print("ERROR: 'requests' not installed. Run: pip install -r requirements.txt")
    sys.exit(1)

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("ERROR: 'python-dotenv' not installed. Run: pip install -r requirements.txt")
    sys.exit(1)

API_KEY = os.getenv("COPPER_API_KEY")
USER_EMAIL = os.getenv("COPPER_USER_EMAIL")
BASE_URL = "https://api.copper.com/developer_api/v1"

if not API_KEY or not USER_EMAIL:
    print("ERROR: Missing credentials. Copy .env.example to .env and fill in COPPER_API_KEY and COPPER_USER_EMAIL.")
    sys.exit(1)

HEADERS = {
    "X-PW-AccessToken": API_KEY,
    "X-PW-Application": "developer_api",
    "X-PW-UserEmail": USER_EMAIL,
    "Content-Type": "application/json",
}


def req(method, path, data=None):
    url = f"{BASE_URL}{path}"
    resp = requests.request(method, url, headers=HEADERS, json=data)
    if resp.status_code == 429:
        print("ERROR: Rate limit hit. Wait a moment and try again.")
        sys.exit(1)
    if not resp.ok:
        print(f"ERROR {resp.status_code}: {resp.text}")
        sys.exit(1)
    return resp.json() if resp.text else {}


def fmt_emails(emails):
    return ", ".join(e["email"] for e in emails) if emails else "—"


def fmt_phones(phones):
    return ", ".join(p["number"] for p in phones) if phones else "—"


def fmt_date(ts):
    if not ts:
        return "—"
    try:
        return datetime.fromtimestamp(ts).strftime("%Y-%m-%d")
    except Exception:
        return str(ts)


# --- LEADS ---

def list_leads(assignee_id=None):
    body = {"page_size": 25, "sort_by": "name"}
    if assignee_id:
        body["assignee_ids"] = [int(assignee_id)]
    data = req("POST", "/leads/search", body)
    results = data if isinstance(data, list) else []

    if not results:
        print("No leads found.")
        return

    print(f"\nLeads ({len(results)} results):\n")
    for l in results:
        print(f"  {l.get('name', '—')}  [ID: {l.get('id')}]")
        print(f"    Email:      {fmt_emails(l.get('emails', []))}")
        print(f"    Phone:      {fmt_phones(l.get('phone_numbers', []))}")
        print(f"    Company:    {l.get('company_name', '—')}")
        print(f"    Title:      {l.get('title', '—')}")
        print(f"    Status:     {l.get('status', '—')}")
        print(f"    Assignee:   {l.get('assignee_id', '—')}")
        print(f"    Created:    {fmt_date(l.get('date_created'))}")
        print()


def list_lead_assignees():
    """List all users in the Copper account so you can filter leads by assignee."""
    data = req("POST", "/users/search", {})
    results = data if isinstance(data, list) else []

    if not results:
        print("No users found.")
        return

    print(f"\nCopper Users ({len(results)}):\n")
    for u in results:
        print(f"  {u.get('name', '—')}  [User ID: {u.get('id')}]  Email: {u.get('email', '—')}")


# --- CONTACTS / PEOPLE ---

def list_people(tag=None):
    body = {"page_size": 25, "sort_by": "name"}
    if tag:
        body["tags"] = [tag]
    data = req("POST", "/people/search", body)
    results = data if isinstance(data, list) else []

    if not results:
        tag_msg = f' with tag "{tag}"' if tag else ''
        print(f"No people found{tag_msg}.")
        return

    header = f'People tagged "{tag}"' if tag else 'All People'
    print(f"\n{header} ({len(results)} results):\n")
    for p in results:
        print(f"  {p.get('name', '—')}  [ID: {p.get('id')}]")
        print(f"    Email:   {fmt_emails(p.get('emails', []))}")
        print(f"    Phone:   {fmt_phones(p.get('phone_numbers', []))}")
        print(f"    Company: {p.get('company_name', '—')}")
        print(f"    Title:   {p.get('title', '—')}")
        tags = p.get('tags', [])
        if tags:
            print(f"    Tags:    {', '.join(tags)}")
        print()


def search_contact(query):
    # Try email search first, then name search
    results = []
    if "@" in query:
        data = req("POST", "/people/fetch_by_email", {"email": query})
        if data:
            results = [data] if isinstance(data, dict) else data
    if not results:
        data = req("POST", "/people/search", {"name": query, "page_size": 10})
        results = data if isinstance(data, list) else []

    if not results:
        print(f"No contacts found for '{query}'.")
        return

    for p in results:
        print(f"\nContact: {p.get('name', '—')}  [ID: {p.get('id')}]")
        print(f"  Email:   {fmt_emails(p.get('emails', []))}")
        print(f"  Phone:   {fmt_phones(p.get('phone_numbers', []))}")
        print(f"  Company: {p.get('company_name', '—')}")
        print(f"  Title:   {p.get('title', '—')}")


def get_contact(contact_id):
    p = req("GET", f"/people/{contact_id}")
    print(f"\nContact: {p.get('name', '—')}  [ID: {p.get('id')}]")
    print(f"  Email:      {fmt_emails(p.get('emails', []))}")
    print(f"  Phone:      {fmt_phones(p.get('phone_numbers', []))}")
    print(f"  Company:    {p.get('company_name', '—')}")
    print(f"  Title:      {p.get('title', '—')}")
    print(f"  Created:    {fmt_date(p.get('date_created'))}")
    print(f"  Modified:   {fmt_date(p.get('date_modified'))}")


# --- COMPANIES ---

def search_company(name):
    data = req("POST", "/companies/search", {"name": name, "page_size": 10})
    results = data if isinstance(data, list) else []

    if not results:
        print(f"No companies found for '{name}'.")
        return

    for c in results:
        print(f"\nCompany: {c.get('name', '—')}  [ID: {c.get('id')}]")
        print(f"  Phone:    {fmt_phones(c.get('phone_numbers', []))}")
        print(f"  Address:  {fmt_address(c.get('address', {}))}")
        print(f"  Website:  {c.get('websites', [{}])[0].get('url', '—') if c.get('websites') else '—'}")


def get_company(company_id):
    c = req("GET", f"/companies/{company_id}")
    print(f"\nCompany: {c.get('name', '—')}  [ID: {c.get('id')}]")
    print(f"  Phone:    {fmt_phones(c.get('phone_numbers', []))}")
    print(f"  Address:  {fmt_address(c.get('address', {}))}")
    print(f"  Website:  {c.get('websites', [{}])[0].get('url', '—') if c.get('websites') else '—'}")
    print(f"  Created:  {fmt_date(c.get('date_created'))}")


def fmt_address(addr):
    if not addr:
        return "—"
    parts = [addr.get("street"), addr.get("city"), addr.get("state"), addr.get("postal_code")]
    return ", ".join(p for p in parts if p) or "—"


# --- OPPORTUNITIES ---

def get_stage_lookup():
    """Build a lookup dict from stage_id -> (pipeline_name, stage_name)."""
    pipelines = req("GET", "/pipelines")
    lookup = {}
    for p in (pipelines if isinstance(pipelines, list) else []):
        for s in p.get("stages", []):
            lookup[s["id"]] = (p["name"], s["name"])
    return lookup


def list_opportunities(stage_id=None):
    body = {"page_size": 200, "sort_by": "name"}
    if stage_id:
        body["pipeline_stage_ids"] = [int(stage_id)]
    data = req("POST", "/opportunities/search", body)
    results = data if isinstance(data, list) else []

    if not results:
        print("No opportunities found.")
        return

    lookup = get_stage_lookup()

    for o in results:
        stage_id_val = o.get("pipeline_stage_id")
        pipeline_name, stage_name = lookup.get(stage_id_val, ("—", "—"))
        print(f"\nOpportunity: {o.get('name', '—')}  [ID: {o.get('id')}]")
        print(f"  Company:  {o.get('company_name', '—')}")
        print(f"  Pipeline: {pipeline_name}")
        print(f"  Stage:    {stage_name}  [Stage ID: {stage_id_val or '—'}]")
        print(f"  Status:   {o.get('status', '—')}")
        print(f"  Value:    ${o.get('monetary_value') or 0:,.0f}")
        print(f"  Close:    {fmt_date(o.get('close_date'))}")


def update_stage(opportunity_id, pipeline_stage_id):
    req("PUT", f"/opportunities/{opportunity_id}", {"pipeline_stage_id": int(pipeline_stage_id)})
    print(f"Opportunity {opportunity_id} moved to stage {pipeline_stage_id}.")


# --- CREATE CONTACT ---

def create_contact(name, email=None, phone=None, company=None, title=None):
    body = {"name": name}
    if email:
        body["emails"] = [{"email": email, "category": "work"}]
    if phone:
        body["phone_numbers"] = [{"number": phone, "category": "work"}]
    if company:
        body["company_name"] = company
    if title:
        body["title"] = title
    result = req("POST", "/people", body)
    print(f"Contact created (ID: {result.get('id', '?')}): {name}")
    if email:
        print(f"  Email:   {email}")
    if phone:
        print(f"  Phone:   {phone}")
    if company:
        print(f"  Company: {company}")
    if title:
        print(f"  Title:   {title}")
    return result.get("id")


# --- ACTIVITIES ---

def log_activity(entity_type, entity_id, note):
    valid_types = {"person", "company", "opportunity", "lead", "task"}
    if entity_type not in valid_types:
        print(f"ERROR: entity_type must be one of: {', '.join(valid_types)}")
        sys.exit(1)

    body = {
        "parent": {"type": entity_type, "id": int(entity_id)},
        "type": {"category": "user", "id": 0},
        "details": note,
    }
    result = req("POST", "/activities", body)
    print(f"Activity logged (ID: {result.get('id', '?')}): {note[:80]}")


# --- TASKS ---

def create_task(title, entity_type, entity_id, due_date_str):
    try:
        due_dt = datetime.strptime(due_date_str, "%Y-%m-%d")
        due_ts = int(due_dt.timestamp())
    except ValueError:
        print("ERROR: due_date must be in YYYY-MM-DD format.")
        sys.exit(1)

    body = {
        "name": title,
        "related_resource": {"type": entity_type, "id": int(entity_id)},
        "due_date": due_ts,
        "status": "Open",
    }
    result = req("POST", "/tasks", body)
    print(f"Task created (ID: {result.get('id', '?')}): {title}  Due: {due_date_str}")


def resolve_entity_name(entity_type, entity_id):
    if not entity_type or not entity_id:
        return None
    type_to_path = {
        "person": f"/people/{entity_id}",
        "lead": f"/leads/{entity_id}",
        "company": f"/companies/{entity_id}",
        "opportunity": f"/opportunities/{entity_id}",
    }
    path = type_to_path.get(entity_type)
    if not path:
        return None
    try:
        data = req("GET", path)
        return data.get("name") or data.get("full_name")
    except Exception:
        return None


def list_tasks(open_only=False, assignee_id=None):
    body = {"page_size": 200, "sort_by": "due_date", "sort_direction": "asc"}
    if open_only:
        body["statuses"] = ["Open"]
    if assignee_id:
        body["assignee_ids"] = [int(assignee_id)]
    data = req("POST", "/tasks/search", body)
    results = data if isinstance(data, list) else []

    if not results:
        print("No tasks found.")
        return

    for t in results:
        related = t.get("related_resource", {}) or {}
        entity_type = related.get("type")
        entity_id = related.get("id")
        name = resolve_entity_name(entity_type, entity_id)
        related_str = f"{entity_type} — {name} (ID: {entity_id})" if name else f"{entity_type} {entity_id}" if entity_type else "—"
        print(f"\nTask: {t.get('name', '—')}  [ID: {t.get('id')}]")
        print(f"  Status:   {t.get('status', '—')}")
        print(f"  Due:      {fmt_date(t.get('due_date'))}")
        print(f"  Related:  {related_str}")


def close_task(task_id):
    req("PUT", f"/tasks/{task_id}", {"status": "Completed"})
    print(f"Task {task_id} closed.")


# --- PIPELINE STAGES ---

def list_stages(pipeline_id):
    data = req("GET", f"/pipeline_stages/pipeline/{pipeline_id}")
    stages = data if isinstance(data, list) else []

    if not stages:
        print(f"No stages found for pipeline {pipeline_id}.")
        return

    print(f"\nStages for pipeline {pipeline_id}:")
    for s in stages:
        print(f"  [{s.get('id')}] {s.get('name', '—')}  (win probability: {s.get('win_probability', '—')}%)")


# --- CLI DISPATCH ---

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    cmd = sys.argv[1]
    args = sys.argv[2:]

    if cmd == "list-leads":
        assignee_id = None
        if "--assignee" in args:
            idx = args.index("--assignee")
            assignee_id = args[idx + 1]
        list_leads(assignee_id)

    elif cmd == "list-users":
        list_lead_assignees()

    elif cmd == "list-people":
        tag = None
        if "--tag" in args:
            idx = args.index("--tag")
            tag = args[idx + 1]
        list_people(tag)

    elif cmd == "search-contact":
        if not args:
            print("Usage: python copper.py search-contact <name_or_email>")
            sys.exit(1)
        search_contact(" ".join(args))

    elif cmd == "get-contact":
        if not args:
            print("Usage: python copper.py get-contact <id>")
            sys.exit(1)
        get_contact(args[0])

    elif cmd == "search-company":
        if not args:
            print("Usage: python copper.py search-company <name>")
            sys.exit(1)
        search_company(" ".join(args))

    elif cmd == "get-company":
        if not args:
            print("Usage: python copper.py get-company <id>")
            sys.exit(1)
        get_company(args[0])

    elif cmd == "create-contact":
        if not args:
            print('Usage: python copper.py create-contact "<name>" "<email>" "<phone>" "<company>" "<title>"')
            sys.exit(1)
        name = args[0]
        email = args[1] if len(args) > 1 else None
        phone = args[2] if len(args) > 2 else None
        company = args[3] if len(args) > 3 else None
        title = args[4] if len(args) > 4 else None
        create_contact(name, email, phone, company, title)

    elif cmd == "list-opportunities":
        stage_id = None
        if "--stage" in args:
            idx = args.index("--stage")
            stage_id = args[idx + 1]
        list_opportunities(stage_id)

    elif cmd == "update-stage":
        if len(args) < 2:
            print("Usage: python copper.py update-stage <opportunity_id> <pipeline_stage_id>")
            sys.exit(1)
        update_stage(args[0], args[1])

    elif cmd == "log-activity":
        if len(args) < 3:
            print('Usage: python copper.py log-activity <entity_type> <entity_id> "<note>"')
            sys.exit(1)
        log_activity(args[0], args[1], " ".join(args[2:]))

    elif cmd == "create-task":
        if len(args) < 4:
            print('Usage: python copper.py create-task "<title>" <entity_type> <entity_id> <due_date YYYY-MM-DD>')
            sys.exit(1)
        create_task(args[0], args[1], args[2], args[3])

    elif cmd == "list-tasks":
        open_only = "--open-only" in args
        assignee_id = None
        if "--mine" in args:
            me = req("GET", "/users/me")
            assignee_id = me.get("id")
        elif "--assignee" in args:
            idx = args.index("--assignee")
            if idx + 1 < len(args):
                assignee_id = args[idx + 1]
        list_tasks(open_only, assignee_id)

    elif cmd == "close-task":
        if not args:
            print("Usage: python copper.py close-task <task_id>")
            sys.exit(1)
        close_task(args[0])

    elif cmd == "list-stages":
        if not args:
            print("Usage: python copper.py list-stages <pipeline_id>")
            sys.exit(1)
        list_stages(args[0])

    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
