# Account Management — Forward Motion Medical

Account data lives in Copper CRM. Use `copper.py` to look up contacts, companies, and opportunities. This file defines how to *think about* accounts — tiers, schemas, and CRM conventions.

---

## Account Tiers

| Tier | Definition | Touchpoint Cadence |
|------|------------|-------------------|
| **A** | High volume or high potential; strong relationship | Monthly minimum, ideally every 2 weeks |
| **B** | Moderate volume or early active accounts | Every 4–6 weeks |
| **C** | Low volume, dormant, or long-term nurture | Every 6–8 weeks or re-engage when triggered |

---

## Account Profile Schema

Use this template when you want to create a deep-dive note on a specific account (e.g., in a separate file or in conversation). Not every account needs one — just the ones where you want to track nuance Copper doesn't capture.

```
## [Practice Name]

### Office Info
- Practice Name:
- Address:
- Phone:
- Website:
- Copper CRM Company ID:
- # of Providers:
- Specialty Focus: (general podiatry / sports / wound care / pediatric / diabetic)

### Key Contacts
- Primary Contact:           [Name, Title]
- Decision Maker:            [Name, Title — if different from primary]
- Email:
- Phone:
- Best Contact Method:       (email / call / text)

### Relationship Status
- Pipeline:                  (Leads / Potential Provider / Current Provider)
- Stage:                     (see ONBOARDING.md for stage names per pipeline)
- Devices Ordered (lifetime):
- Last Contact Notes:
- Next Planned Touchpoint:

### Ordering Preferences
- Casting Method:            (scanning / plaster / biofoam)
- Scanning Device:           (iPhone model / iPad Pro / iPad + Structure Sensor)
- Portal Access Confirmed:   (yes / no)

### Objections / Blockers
- Objections raised:
- How addressed:
- Open concerns:

### Opportunities / Notes
- Upsell or expansion potential:
- Referrals given or expected:
- Other notes:
```

---

## Copper CRM Conventions

### Pipeline Stages
See ONBOARDING.md for full stage definitions and PIPELINE.md for stage IDs.

**Leads Pipeline (ID: 1133048):** New Lead → Attempting Contact → Engaged → Qualified → Nurture/Not Now → Lost/Not a Fit

**Potential Provider Pipeline (ID: 1126326):** Billing Received → Onboarding/1st Order → Trialing → Adopting → Stalled/At Risk

**Current Provider Pipeline (ID: 1133049):** New Provider → Active/Stable → Growth Focused → At Risk/Declining → Inactive

> Graduation trigger: $325 in orders = move from Potential Provider → Current Provider (New Provider)

### Tag Conventions
Tags observed in Copper data: `will's leads`, `will's lead list`
*(Add more as needed, e.g. "scanning", "re-engage", "referral-source", "high-volume")*

### Activity Logging Rules
- Log every call and email the same day in Copper
- Use the `log-activity` command: `python copper.py log-activity person <id> "<note>"`
- Note format: "[Date] — [What happened] — [Next step]"

### Task Cadence
- Leads: Follow up within 3–5 business days of last touch
- Potential Provider: Follow up within 7–14 days; flag stalled accounts immediately
- Current Provider (Active/Growth): Touch every 6 weeks
- Current Provider (At Risk): Follow up within 7 days
- Current Provider (Inactive): One re-engagement attempt; 90-day reminder if no response
