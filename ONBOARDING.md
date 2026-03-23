# Onboarding & Account Stages — Forward Motion Medical

Accounts move through three separate Copper pipelines. Before drafting any outreach, check PIPELINE.md for the office's current pipeline and stage, then use this file to determine the right next action.

---

## Pipeline 1: Leads
*Offices that haven't ordered yet. Goal: qualify them into billing.*

### Stage 1 — New Lead
**Goal:** Identify the office as a potential account.
**Criteria to advance:** Will has decided to reach out.
**Next action:** Send cold outreach email or make first call.
**Email to offer:** Cold outreach template (EMAILS.md — Cold Outreach)
**Copper stage ID:** 5087460

---

### Stage 2 — Attempting Contact
**Goal:** Make first contact.
**Criteria to advance:** Outreach sent; waiting for response.
**Next action:** Follow up in 3–5 business days if no response. Try a different channel (call vs. email).
**Email to offer:** Follow-up Day 3 or Day 7 template (EMAILS.md — Follow-Up Sequences)
**Copper stage ID:** 5087461

---

### Stage 3 — Engaged
**Goal:** Establish two-way conversation; confirm interest.
**Criteria to advance:** Doctor or office manager has responded and shown interest.
**Next action:** Answer questions, offer a demo or sample, begin talking about billing setup.
**Email to offer:** Engagement / product intro (EMAILS.md — Follow-Up Sequences)
**Copper stage ID:** 5087462

---

### Stage 4 — Qualified
**Goal:** Office is ready to move to billing and first order.
**Criteria to advance:** Decision-maker is on board; billing info collected or in process.
**Next action:** Get them set up on the Doctor Portal and move to Potential Provider pipeline.
**Email to offer:** Order confirmation / welcome (EMAILS.md — Order-Related)
**Copper stage ID:** 5087463

---

### Stage 5 — Nurture / Not Now
**Goal:** Keep warm — they're not ready but haven't said no.
**Criteria:** Interested but timing isn't right (seasonal, budget, etc.).
**Next action:** Set a 30–60 day follow-up reminder. Light touch outreach.
**Copper stage ID:** 5087464

---

### Stage 6 — Lost / Not a Fit
**Goal:** Document and move on.
**Criteria:** Office has declined or is clearly not a fit.
**Next action:** Log reason in Copper. Set a 6-month re-engagement reminder if appropriate.
**Copper stage ID:** 5087465

> **Next pipeline:** Once billing is received, create opportunity in **Potential Provider** pipeline at "Billing Received."

---

## Pipeline 2: Potential Provider
*Billing received, fewer than 4 devices ordered. Goal: build the ordering habit.*

> **Graduation rule:** 4 devices ordered = move to **Current Provider (Active/Stable)**. Hard trigger — not a judgment call.

---

### Stage 1 — Billing Received
**Goal:** Get the first order placed.
**Criteria to advance:** First order submitted through Doctor Portal or scanning app.
**Next action:** Confirm portal access, walk through first order if needed, set turnaround expectation.
**Email to offer:** Order confirmation / thank you (EMAILS.md — Order-Related)
**Copper stage ID:** 5087437

---

### Stage 2 — Onboarding / 1st Order
*(Copper name: "Onboarding/ 1st Order")*
**Goal:** Deliver a great first experience.
**Criteria to advance:** First order delivered; office confirms it went well.
**Next action:** Check-in call or email after delivery. Ask how the device turned out. Encourage second order.
**Email to offer:** First order check-in (EMAILS.md — Follow-Up Sequences)
**Copper stage ID:** 5087438

---

### Stage 3 — Trialing
*(Copper name: "Trialing")*
**Goal:** Make ordering a routine.
**Criteria to advance:** 3 total devices ordered.
**Next action:** Keep touchpoints light but consistent. Mention scanning if not using it. Ask for referrals.
**Email to offer:** After second order template (EMAILS.md — Follow-Up Sequences)
**Copper stage ID:** 5087439

---

### Stage 4 — Adopting
*(Copper name: "Adopting")*
**Goal:** Office has hit 4 devices — graduate them.
**Criteria to advance:** 4 devices ordered (hard rule).
**Next action:** Move opportunity to Current Provider pipeline (Active/Stable). Log the graduation in Copper.
**Copper stage ID:** 5087440

> **Action:** `python copper.py update-stage <opportunity_id> <current_provider_active_stage_id>`
> Then log: `python copper.py log-activity opportunity <id> "Graduated to Current Provider — 4 devices ordered"`

---

### Stage 5 — Stalled / At Risk
**Goal:** Re-engage before losing the account.
**Criteria:** No new orders for 30+ days after first order.
**Next action:** Personal outreach — call first, then email. Find out what's blocking them.
**Email to offer:** Re-engagement template (EMAILS.md — Re-Engagement)
**Copper stage ID:** 5087441

Common stall reasons and responses:
| Reason | Response |
|--------|---------|
| Forgot / busy | Simple nudge, offer to help place next order |
| Bad first experience | Apologize, fix it fast, offer adjustment under 6-month policy |
| Staff turnover | Re-train new staff, re-send scanning tutorial |
| Switched back to old lab | Ask what happened; address it directly |

---

## Pipeline 3: Current Provider
*Established accounts with 4+ devices. Goal: grow and protect the relationship.*

---

### Stage 1 — New Provider
**Goal:** Smooth transition from Potential Provider pipeline.
**Criteria to advance:** First few weeks as a Current Provider; confirm they're ordering consistently.
**Next action:** Welcome to Current Provider status. Ensure they know ongoing support is available.
**Copper stage ID:** 5087466

---

### Stage 2 — Active / Stable
**Goal:** Maintain a consistent, healthy relationship.
**Next action:** Regular check-ins based on order volume. Watch for order gaps.
**Copper stage ID:** 5087467

---

### Stage 3 — Growth Focused
**Goal:** Actively grow order volume or referrals.
**Criteria:** Office has high potential — multiple providers, high patient volume, or referral history.
**Next action:** Identify what's limiting growth. More scanning adoption? More providers in office using FM?
**Copper stage ID:** 5087468

---

### Stage 4 — At Risk / Declining
**Goal:** Prevent churn.
**Criteria:** Orders have dropped noticeably compared to their normal pattern.
**Next action:** Personal outreach — call first. Find out what changed. Offer something concrete.
**Email to offer:** Re-engagement template (EMAILS.md — Re-Engagement)
**Copper stage ID:** 5087469

---

### Stage 5 — Inactive / Churned
**Goal:** Document and attempt win-back if appropriate.
**Criteria:** No orders for 60+ days with no explanation.
**Next action:** One honest re-engagement attempt. If no response, tag in Copper and set a 90-day reminder.
**Email to offer:** Gone dark re-engagement (EMAILS.md — Re-Engagement)
**Copper stage ID:** 5087470

---

## Drop-Off Points and Re-Engagement

| Where They Stall | Why It Happens | What to Do |
|-----------------|---------------|------------|
| Leads — no response to outreach | Busy office, email buried | Try call instead of email; mention a referrer if possible |
| Leads — engaged but no billing | Decision-maker not involved | Ask who handles vendor decisions and loop them in |
| Potential — billing but no 1st order | Portal confusion, inertia | Offer to walk them through the first order live |
| Potential — 1st order but no 2nd | Bad experience or just forgot | Check-in call; if issue, fix it fast under the 6-month policy |
| Potential — stalled at 2–3 devices | Not a priority, or scanning not set up | Bring up scanning; make it easier to order |
| Current — declining orders | Lab switch, staff turnover, seasonal | Personal outreach; find out what changed |

---

## New Account Onboarding Checklist

Use this when bringing on a new account from the Leads pipeline:

- [ ] Office added to Copper CRM (company + key contacts)
- [ ] Opportunity created in Leads pipeline at correct stage
- [ ] Ordering method confirmed (scanning, plaster, biofoam)
- [ ] If scanning: device confirmed, app downloaded, tutorial sent
- [ ] Doctor Portal access set up: https://orthoticsportal.com/
- [ ] Pricing confirmed ($99, free shipping, no taxes)
- [ ] 6-month adjustment policy explained
- [ ] Billing received → move to Potential Provider pipeline
- [ ] First order placed → move to 1st Order Placed stage
- [ ] First delivery → check-in completed

---

## Copper CRM Stage Mapping

Run `python copper.py list-stages <pipeline_id>` for each pipeline and fill in the IDs below.

### Leads Pipeline (Pipeline ID: 1133048)
| Stage | Copper Stage Name | Copper Stage ID |
|-------|-----------------|----------------|
| New Lead | New Lead | 5087460 |
| Attempting Contact | Attempting Contact | 5087461 |
| Engaged | Engaged | 5087462 |
| Qualified | Qualified | 5087463 |
| Nurture / Not Now | Nurture/ Not Now | 5087464 |
| Lost / Not a Fit | Lost/ Not a Fit | 5087465 |

### Potential Provider Pipeline (Pipeline ID: 1126326)
| Stage | Copper Stage Name | Copper Stage ID |
|-------|-----------------|----------------|
| Billing Received | Billing Received | 5087437 |
| Onboarding / 1st Order | Onboarding/ 1st Order | 5087438 |
| Trialing | Trialing | 5087439 |
| Adopting | Adopting | 5087440 |
| Stalled / At Risk | Stalled/ At Risk | 5087441 |

### Current Provider Pipeline (Pipeline ID: 1133049)
| Stage | Copper Stage Name | Copper Stage ID |
|-------|-----------------|----------------|
| New Provider | New Provider | 5087466 |
| Active / Stable | Active/ Stable | 5087467 |
| Growth Focused | Growth Focused | 5087468 |
| At Risk / Declining | At Risk/ Declining | 5087469 |
| Inactive / Churned | Inactive | 5087470 |
