# Account Profiles — Forward Motion Medical

This file defines the schema for tracking podiatrist office accounts. Individual account entries can be added below the schema, or kept in separate files per account as the list grows.

---

## Account Tiers

| Tier | Definition | Touchpoint Cadence |
|------|------------|-------------------|
| **A** | High volume or high potential; strong relationship | Monthly minimum, ideally every 2 weeks |
| **B** | Moderate volume or early active accounts | Every 4–6 weeks |
| **C** | Low volume, dormant, or long-term nurture | Every 6–8 weeks or re-engage when triggered |

---

## Account Profile Schema

```
## [Practice Name]

### Office Info
- Practice Name:
- Address:
- Phone:
- Website:
- Copper CRM URL: https://app.copper.com/companies/[id]
- # of Providers:
- Specialty Focus: (general podiatry / sports / wound care / pediatric / diabetic)
- Patient Volume: (low / medium / high)

### Key Contacts
- Primary Contact:           [Name, Title]
- Decision Maker:            [Name, Title — if different from primary]
- Gatekeeper / Office Mgr:  [Name]
- Email:
- Phone:
- Best Contact Method:       (email / call / text)
- Best Time to Reach:

### Relationship Status
- Current Lab:               [name, or "Forward Motion" if active]
- Pipeline:                  (Leads / Potential Provider / Current Provider)
- Stage:                     (see ONBOARDING.md for stage names per pipeline)
- Devices Ordered (lifetime):
- First Contact Date:
- Last Contact Date:
- Last Contact Notes:
- Next Planned Touchpoint:

### Ordering Preferences
- Casting Method:            (scanning / plaster / biofoam)
- Scanning Device:           (iPhone model / iPad Pro / iPad + Structure Sensor)
- Portal Access Confirmed:   (yes / no)
- Average Orders/Month:
- Common Products Ordered:

### Order History
- First Order Date:
- Total Orders (lifetime):
- Last Order Date:
- Notes on fit preferences or common adjustments:

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
Run `python copper.py list-stages <pipeline_id>` for each pipeline and fill in the IDs. See ONBOARDING.md for the full stage mapping table.

**Leads Pipeline (ID: 1133048):** New Lead → Attempting Contact → Engaged → Qualified → Nurture/Not Now → Lost/Not a Fit

**Potential Provider Pipeline (ID: 1126326):** Billing Received → Onboarding/1st Order → Trialing → Adopting → Stalled/At Risk

**Current Provider Pipeline (ID: 1133049):** New Provider → Active/Stable → Growth Focused → At Risk/Declining → Inactive

> Graduation trigger: 4 devices ordered = move from Potential Provider → Current Provider (Active/Stable)

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
- Current Provider (Active/Growth): Touch every 2–4 weeks
- Current Provider (At Risk): Follow up within 7 days
- Current Provider (Inactive): One re-engagement attempt; 90-day reminder if no response

---

## Account Entries

Add individual accounts below. Copy the schema above for each new practice.

---

## Krista Goszkowicz (Tier: A)

### Office Info
- Practice Name: Krista Goszkowicz's Company
- Address: 10442 W Cermak Rd, Westchester, IL 60154
- Copper CRM URL: https://app.copper.com/companies/74404780
- Opp ID: 36322330

### Key Contacts
- Primary Contact: Krista Goszkowicz, Doctor
- Email: sfpinc@sbcglobal.net

### Relationship Status
- Pipeline: Current Provider
- Stage: Active/ Stable (5087467)
- Interactions: 55 (highest in book)
- Last Contact Date: 2026-03-04

---

## Spur Podiatry (Tier: A)

### Office Info
- Practice Name: Spur Podiatry
- Address: 625 Parkview Dr, Suite 102, Trophy Club, TX 76262
- Copper CRM URL: https://app.copper.com/companies/74381047
- Opp ID: 36599039

### Key Contacts
- Primary Contact: Timothy Fishman, Doctor/Owner
- Email: spurpodiatry@gmail.com
- Phone: (917) 667-4514

### Relationship Status
- Pipeline: Current Provider
- Stage: New Provider (5087466)
- Interactions: 44
- Last Contact Date: 2026-03-19

---

## Soley Podiatry (Tier: A)

### Office Info
- Practice Name: Soley Podiatry
- Address: 2901 Caballo Ranch Blvd, Suite 8A, Cedar Park, TX 78641
- Copper CRM URL: https://app.copper.com/companies/74381049
- Opp ID: 36484643

### Key Contacts
- Primary Contact: Anne Sharkey, Doctor/Owner
- Email: drsharkey@solelypodiatry.com
- Phone: (512) 222-6637

### Relationship Status
- Pipeline: Current Provider
- Stage: New Provider (5087466)
- Interactions: 39
- Last Contact Date: 2025-12-16
- **Note:** High engagement but no contact since Dec — needs re-engagement

---

## Athletics and Orthopedics Knee Center (Tier: A)

### Office Info
- Practice Name: Athletics and Orthopedics Knee Center
- Address: 9180 Katy Freeway, Suite 200, Houston, TX 77055
- Website: http://aokc.net
- Copper CRM URL: https://app.copper.com/companies/74381069
- Opp ID: 36380242

### Key Contacts
- Primary Contact: Jack Jensen, Doctor
- Email: alexander.castillo@aokc.net
- Phone: (783) 984-1400

### Relationship Status
- Pipeline: Current Provider
- Stage: Active/ Stable (5087467)
- Status: Won
- Interactions: 35
- Last Contact Date: 2026-01-08

---

## Premier Podiatry (Tier: B)

### Office Info
- Practice Name: Premier Podiatry
- Address: IL (full address needed)
- Copper CRM URL: https://app.copper.com/companies/75437530
- Opp ID: 36949434

### Key Contacts
- Primary Contact: Scott O'Connor, Doctor
- Email: scott.oconnor@icloud.com

### Relationship Status
- Pipeline: Current Provider
- Stage: New Provider (5087466)
- Interactions: 29
- Last Contact Date: 2026-03-17

---

## Scotto Podiatry (Tier: B)

### Office Info
- Practice Name: Scotto Podiatry
- Address: 106 Apple St, Suite 200A, Tinton Falls, NJ 07724
- Copper CRM URL: https://app.copper.com/companies/74870663
- Opp ID: 36584397

### Key Contacts
- Primary Contact: Michael Scotto, Doctor/Owner
- Email: drscotto@verizon.net

### Relationship Status
- Pipeline: Current Provider
- Stage: New Provider (5087466)
- Interactions: 26
- Last Contact Date: 2026-03-17

---

## Peoria Foot and Ankle (Tier: B)

### Office Info
- Practice Name: Peoria Foot and Ankle
- Address: 13660 N 94th Dr, Ste D1, Peoria, AZ 85381
- Copper CRM URL: https://app.copper.com/companies/74381056
- Opp ID: 36319762

### Key Contacts
- Primary Contact: Ryan Bangart
- Email: shannon@peoriapodiatrist.com
- Phone: (623) 974-0522

### Relationship Status
- Pipeline: Current Provider
- Stage: Active/ Stable (5087467)
- Interactions: 25
- Last Contact Date: 2026-02-02

---

## Patel Podiatry (Tier: B)

### Office Info
- Practice Name: Patel Podiatry
- Address: Hamden, CT (full address needed)
- Copper CRM URL: https://app.copper.com/companies/74873960
- Opp ID: 36591854

### Key Contacts
- Primary Contact: Ian Richter, Doctor
- Email: patelpodiatry@gmail.com

### Relationship Status
- Pipeline: Current Provider
- Stage: New Provider (5087466)
- Interactions: 24
- Last Contact Date: 2026-01-14

---

## Boston Common Podiatry (Tier: B — Potential Provider)

### Office Info
- Practice Name: Boston Common Podiatry
- Address: Billerica, MA (full address needed)
- Copper CRM URL: https://app.copper.com/companies/74381066
- Opp ID: 36945311

### Key Contacts
- Primary Contact: Maghan Francoeur, Office Manager
- Email: maghanf@gmail.com

### Relationship Status
- Pipeline: Potential Provider
- Stage: Billing Received (5087437)
- Interactions: 41 (very high for a Potential Provider)
- Last Contact Date: 2026-03-23
- **Note:** Contacted today — high engagement, push toward first order

---

## Podiatry Associates of Indiana (Tier: B — Potential Provider)

### Office Info
- Practice Name: Podiatry Associates of Indiana - Georgetown
- Address: Indianapolis, IN (full address needed)
- Website: https://infootandankle.com/
- Copper CRM URL: https://app.copper.com/companies/75688496
- Opp ID: 37142649

### Key Contacts
- Primary Contact: Trish Reed, Accounts Payable
- Email: treed@infootandankle.com
- Phone: (317) 502-2061

### Relationship Status
- Pipeline: Potential Provider
- Stage: Billing Received (5087437)
- Interactions: 28
- Last Contact Date: 2026-03-10

---

## Piedmont Health Care (Tier: B — Potential Provider)

### Office Info
- Practice Name: Piedmont Health Care
- Address: 137 Professional Park Dr, Mooresville, NC
- Website: http://piedmonthealthcare.com
- Copper CRM URL: https://app.copper.com/companies/75395193
- Opp ID: 36924381

### Key Contacts
- Primary Contact: Sanja Jones, Office Manager
- Email: sonja.jones@piedmonthealthcare.com
- Phone: (704) 662-8336

### Relationship Status
- Pipeline: Potential Provider
- Stage: Billing Received (5087437)
- Interactions: 26
- Last Contact Date: 2026-03-11

---

## Aire Podiatry Studio (Tier: B — Potential Provider)

### Office Info
- Practice Name: Aire Podiatry Studio
- Copper CRM URL: https://app.copper.com/companies/75449242
- Opp ID: 36959789

### Key Contacts
- Primary Contact: Lilli Oquendo, Director of Operations
- Email: admin@airepodiatry.com
- Phone: (917) 985-9082

### Relationship Status
- Pipeline: Potential Provider
- Stage: Billing Received (5087437)
- Interactions: 26
- Last Contact Date: 2026-03-12
