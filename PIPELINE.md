# Pipeline Guide — Forward Motion Medical

**Last updated:** 2026-03-24

Three Copper pipelines track accounts at different relationship stages. Use `copper.py` to query live data — don't maintain static lists here.

---

## Pipelines at a Glance

| Pipeline | ID | Purpose | Graduation Trigger |
|----------|-----|---------|-------------------|
| Leads | 1133048 | New offices, not yet ordered | Billing received → move to Potential Provider |
| Potential Provider | 1126326 | Billing in, under $325 in orders | $325 in orders → move to Current Provider |
| Current Provider | 1133049 | Established, $325+ in orders | — |

---

## Quick-Reference Commands

```bash
# See all opportunities (first 25)
python3 copper.py list-opportunities

# Filter by stage
python3 copper.py list-opportunities --stage 5087437   # Billing Received
python3 copper.py list-opportunities --stage 5087466   # New Provider

# Search for a specific account
python3 copper.py search-company "Boston Common"

# Look up a contact
python3 copper.py search-contact "Dr. Smith"

# Move an account to a new stage
python3 copper.py update-stage <opportunity_id> <stage_id>

# Log an activity
python3 copper.py log-activity person <contact_id> "Called re: first order"

# Create a follow-up task
python3 copper.py create-task "Follow up on demo" person <contact_id> 2026-04-01

# See open tasks
python3 copper.py list-tasks --open-only
```

### Stage IDs (for filtering and updating)

**Leads (1133048):**
| Stage | ID |
|-------|----|
| New Lead | 5087460 |
| Attempting Contact | 5087461 |
| Engaged | 5087462 |
| Qualified | 5087463 |
| Nurture/ Not Now | 5087464 |
| Lost/ Not a Fit | 5087465 |

**Potential Provider (1126326):**
| Stage | ID |
|-------|----|
| Billing Received | 5087437 |
| Onboarding/ 1st Order | 5087438 |
| Trialing | 5087439 |
| Adopting | 5087440 |
| Stalled/ At Risk | 5087441 |

**Current Provider (1133049):**
| Stage | ID |
|-------|----|
| New Provider | 5087466 |
| Active/ Stable | 5087467 |
| Growth Focused | 5087468 |
| At Risk/ Declining | 5087469 |
| Inactive | 5087470 |

---

## This Week's Focus
*(Update each Monday)*

1.
2.
3.

---

## Data Quality Notes
*Potential duplicates to clean up in Copper:*
- Aire Podiatry Studio — two opps in Potential Provider (36959789, 36959792)
- Ashton / Ashton Podiatry — two opps, one has zero interactions (36736446, 36736450)
- Athletics and Orthopedics Knee Center — two opps in Current Provider (36380242, 36717299)
- Patel Podiatry / Patel podiatry — two opps in Current Provider (36591844, 36591854)
- Peoria Foot and Ankle — two opps in Current Provider (36319761, 36319762)
- Metropolitan Podiatry Associates — two opps in Potential Provider (36531835, 36535392)
