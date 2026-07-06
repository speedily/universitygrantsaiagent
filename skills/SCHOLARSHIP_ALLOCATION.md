# Scholarship Allocation Agent Skill

Use this skill when processing university scholarship grant applications.

## Eligibility (bias-free, same for all students)

- Family yearly income must convert to **strictly less than $12,000 USD** per year (from local currency)
- Marks **≥ 50%** OR Grade **B or A**

## Tier awards

| Tier | Condition | Scholarship |
|------|-----------|-------------|
| A | Marks ≥ 70% OR Grade A | **$150,000 USD** |
| B | Marks 50–69% OR Grade B | **$50,000 USD** |

## Budget

- University budget cap: **$1,000,000 USD**
- Allocate in **application timestamp order** (FIFO — first entry wins when budget tight)
- Overflow → **Waitlist** (orange); funded → **Selected** (green)

## Documents

- Marks proof and tax documents are **not** collected on the web form
- Shortlisted students receive email request before **online interview**

## Online interview (dashboard)

Interviewer records outcome per selected student:

| Outcome | Action |
|---------|--------|
| **Unattended** | Slot released; next waitlist student promoted (FIFO) |
| **Attended — selected** | Scholarship confirmed |
| **Attended — rejected** | Reason required: grades mismatch, income mismatch, identity mismatch, no travel budget, or other |

## Anti-bias principles

1. No human subjectivity in automated filter phase
2. Same numeric rules for every country — income compared only after USD conversion
3. Tie-break only by `applied_at` datetime — never by name or country
