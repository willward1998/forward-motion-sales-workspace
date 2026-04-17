# Onboarding & Account Stages — Forward Motion Medical

Accounts move through three separate Copper pipelines. Before drafting any outreach, check PIPELINE.md for the office's current pipeline and stage, then use this file to determine the right next action.

---

## Pipeline 1: Leads
*Offices that haven't committed to using Forward Motion. Goal: commit them to switching labs and getting billing information.*

Contains cold and warm leads. Warm leads are providers reviewing labs and moving to switch. Cold leads are providers being contacted to sell on switching custom orthotic labs.

### Stage 1 — New Lead
**Goal:** Acquire lead information and identify the office as a potential account.
**Information to capture:**
- Physician Name(s)
- Primary Contact (Office manager / Dr.)
- Email
- Phone
- Current Lab
- Pain points and desired outcome
- Source

**Source types:** Inbound, Organic, Show Lead, Cold, Referral
**Criteria to advance:** Outreach has been made by phone or email.
**Next action:** Send outreach based on source — email or first call.
**Email to offer:** Cold outreach template (EMAILS.md — Cold Outreach)
**Copper stage ID:** 5087460

---

### Stage 2 — Attempting Contact
**Goal:** Show them FM's value; start an email campaign based on source.
**Criteria to advance:** Outreach sent; waiting for response.
**Next action:** Follow up in 3–5 business days if no response. Try a different channel (call vs. email).
**Email to offer:** Follow-up Day 3 or Day 7 template (EMAILS.md — Follow-Up Sequences)
**Copper stage ID:** 5087461

---

### Stage 3 — Engaged
**Goal:** Establish two-way conversation; confirm interest and move toward action.
**Criteria to advance:** Doctor or office manager has responded and shown interest.
**Call to Action options** (choose from these based on the conversation):
- Video Call
- Confirm Casting Method
- Download App
- Trial Order
- Sample Box

**Next action:** Drive toward one or more of the above actions. Begin getting them to commit to using Forward Motion and providing billing information.
**Email to offer:** Engagement / product intro (EMAILS.md — Follow-Up Sequences)
**Copper stage ID:** 5087462

---

### Stage 4 — Qualified
**Goal:** Close — get required info and progress to Potential Provider pipeline.
**Criteria to advance:** Decision-maker is on board; billing info collected or in process.
**Next action:** Collect required info, get New Provider Form, and move to Potential Provider pipeline.
**Copper stage ID:** 5087463

---

### Stage 5 — Stalled
**Goal:** Keep warm — stopped responding and not progressing. They're not ready but haven't said no.
**Criteria:** No longer progressing after 3 weeks.
**Next action:** Contact and verify reason for delay. Light touch outreach.
**Copper stage ID:** 5087464

---

### Leads Check List
*Complete these before progressing an account to Potential Provider:*
- [ ] Lab Offers Understood (2.5 week turnaround, $99 Orthotics, Free Shipping, 6 Month Adjustment Policy, Free Accommodations, Free App)
- [ ] Chosen Casting Method
- [ ] New Provider Form
- [ ] Samples

> **Next pipeline:** Once billing is received, create opportunity in **Potential Provider** pipeline at "Billing Received."

---

## Pipeline 2: Potential Provider
*Billing received, under $325 in orders. Goal: build the ordering habit.*

> **Graduation rule:** $325 in orders = move to **Current Provider (New Provider)**. Hard trigger — not a judgment call.

---

### Stage 1 — Billing Received
**Goal:** Get the first order placed. Make a positive first interaction.
**Cover these topics:** Price, Lab Standards, Turnaround, Adjustment Policy.
**Criteria to advance:** First order submitted on the Forward Motion app or physical cast shipped.
**Next action:** Confirm portal access, app download, and walk through first order if needed. Set turnaround expectation.
**Email to offer:** Order confirmation / thank you (EMAILS.md — Order-Related)
**Copper stage ID:** 5087437

---

### Stage 2 — Onboarding / 1st Order
*(Copper name: "Onboarding/ 1st Order")*
**Goal:** Deliver a great first experience.
**Order type:** Scanned or Physical Cast Sent.
**Order follow-up process:**
1. Review Rx Form
2. Review Scans
3. Order email confirmation
4. Follow-up email: Update upon Shipment
5. Follow-up email: Follow up on 1st order

**If disliked:** Verify desired outcome. Remake if needed.
**Criteria to advance:** First order delivered; office confirms it went well.
**Next action:** Check-in call or email after delivery. Ask how the device turned out. Encourage second order.
**Email to offer:** First order check-in (EMAILS.md — Follow-Up Sequences)
**Copper stage ID:** 5087438

---

### Stage 3 — Trialing
*(Copper name: "Trialing")*
**Goal:** Continuously provide results. Drive home satisfaction and make ordering routine.
**Criteria to advance:** 2–3 total devices ordered; physician satisfaction verified after each order.
**Next action:** Keep touchpoints consistent. Mention scanning if not using it. Ask for referrals.
**Satisfaction & marketing actions:**
- Display Stand
- Logo
- Marketing Materials
- Doctor Locator
- Banners
- Introduce Tracy and Eli (FM team)
- Video Tutorials

**Email to offer:** After second order template (EMAILS.md — Follow-Up Sequences)
**Copper stage ID:** 5087439

---

### Stage 4 — Adopting
*(Copper name: "Adopting")*
**Goal:** Hit $325 in orders — then graduate to Current Provider.
**Criteria to advance:** $325 in orders (hard rule).
**Next action:** Move opportunity to Current Provider pipeline (New Provider). Log the graduation in Copper.
**Copper stage ID:** 5087440

> **Action:** `python copper.py update-stage <opportunity_id> <current_provider_new_provider_stage_id>`
> Then log: `python copper.py log-activity opportunity <id> "Graduated to Current Provider — hit \$325 threshold"`

---

### Stage 5 — Stalled / At Risk
**Goal:** Re-engage before losing the account.
**Criteria:** No longer progressing after 3 weeks.
**Next action:** Contact and verify reason for delay. Personal outreach — call first, then email.
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

### Potential Provider Check List
*Practices and physicians should understand these before moving to Current Provider:*
- [ ] Competent at Scanning
- [ ] Lab Standards (Shoe size, Arch Height, Device width, Shell Placement)
- [ ] Understands Adjustment Submission
- [ ] Video Tutorials

---

## Pipeline 3: Current Provider
*Established accounts with $325+ in orders. Goal: manage the relationship, grow revenue.*

---

### Stage 1 — New Provider
**Goal:** Smooth transition from Potential Provider pipeline.
**Criteria to advance:** First few weeks as a Current Provider; confirm they're ordering consistently.
**Next action:**
- Congratulate on first 5 orders
- Check in monthly
- Verify understanding of features

**Copper stage ID:** 5087466

---

### Stage 2 — Active / Stable
**Goal:** Maintain a consistent, healthy ordering relationship.
**Next action:** Track for the next 2–3 months focusing on consistency. Monthly review task for all providers in this stage — check in on satisfaction and any assistance required.
**Copper stage ID:** 5087467

---

### Stage 3 — Growth Focused
**Goal:** Increase revenue — grow order volume or referrals.
**Criteria:** Office has high potential — multiple providers, high patient volume, or referral history.
**Next action:**
- Introduce additional products
- Fall Prevention Program
- Nick and Prefabs

**Copper stage ID:** 5087468

---

### Stage 4 — At Risk / Declining
**Goal:** Prevent churn.
**Criteria:** Orders have dropped noticeably compared to their normal pattern.
**Next action:** Contact and verify reason for decline. Call first. Offer something concrete.
**Email to offer:** Re-engagement template (EMAILS.md — Re-Engagement)
**Copper stage ID:** 5087469

---

### Stage 5 — Inactive / Churned
**Goal:** Document and attempt win-back if appropriate.
**Criteria:** No orders for 60+ days with no explanation.
**Next action:** Contact and find the problem. Have they switched labs? If no response, tag in Copper and set a 90-day reminder.
**Email to offer:** Gone dark re-engagement (EMAILS.md — Re-Engagement)
**Copper stage ID:** 5087470

---

### Current Provider Check List
*Things providers should fully understand:*
- [ ] Had formal intro to Tracy and Eli
- [ ] Familiar with Desktop Portal
- [ ] Understands Order Form
- [ ] Had introduction to all FM Products
- [ ] Video Tutorials

---

## Drop-Off Points and Re-Engagement

| Where They Stall | Why It Happens | What to Do |
|-----------------|---------------|------------|
| Leads — no response to outreach | Busy office, email buried | Try call instead of email; mention a referrer if possible |
| Leads — engaged but no billing | Decision-maker not involved | Ask who handles vendor decisions and loop them in |
| Potential — billing but no 1st order | Portal confusion, inertia | Offer to walk them through the first order live |
| Potential — 1st order but no 2nd | Bad experience or just forgot | Check-in call; if issue, fix it fast under the 6-month policy |
| Potential — stalled under $325 | Not a priority, or scanning not set up | Bring up scanning; make it easier to order |
| Current — declining orders | Lab switch, staff turnover, seasonal | Personal outreach; find out what changed |

---

## New Account Onboarding Checklist

Use this when bringing on a new account from the Leads pipeline:

- [ ] Office added to Copper CRM (company + key contacts)
- [ ] Opportunity created in Leads pipeline at correct stage
- [ ] Lab offers understood (2.5 week turnaround, $99 Orthotics, Free Shipping, 6 Month Adjustment Policy, Free Accommodations, Free App)
- [ ] Casting method chosen (scanning, plaster, biofoam)
- [ ] If scanning: device confirmed, app downloaded, tutorial sent
- [ ] Doctor Portal access set up: https://orthoticsportal.com/
- [ ] New Provider Form collected
- [ ] Samples sent
- [ ] Billing received → move to Potential Provider pipeline
- [ ] First order placed → move to Onboarding / 1st Order stage
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
