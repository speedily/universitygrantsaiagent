# Airtable Omni prompt — full dashboard + form fields

Import **`airtable-applications-template.csv`** after creating the table.

---

## Omni prompt

```
Create a base called "University Grants AI Agent" for scholarship application tracking.

Create one table named exactly: Student Applications

Add ALL of these columns (names must match exactly — our API syncs every dashboard field):

| Column name            | Field type        | Notes |
|------------------------|-------------------|-------|
| Application ID         | Single line text  | UUID from app |
| Name                   | Single line text  | From application form |
| Email                  | Email             | From application form |
| Phone                  | Single line text  | From application form |
| Country                | Single line text  | From application form |
| Semester               | Single line text  | e.g. Fall 2026 |
| Academic Year          | Single line text  | e.g. 2026–2027 |
| Marks Pct              | Number            | 0–100 |
| Grade                  | Single select     | Options: A, B, C (allow empty) |
| Income Local           | Number            | Yearly family income in local currency |
| Currency               | Single line text  | INR, USD, NGN, EUR, etc. |
| Income USD             | Number            | USD equivalent (< $12,000 eligible) |
| Applied At             | Single line text  | Full ISO timestamp from server |
| Applied Date           | Single line text  | e.g. 2026-07-01 (server local) |
| Applied Time           | Single line text  | e.g. 13:30:00 (server local) |
| Status                 | Single select     | pending, eligible, selected, waitlist, ineligible, interview_confirmed, no_show, interview_rejected |
| Tier                   | Single select     | A, B (allow empty) |
| Award USD              | Number            | Scholarship amount in USD |
| Interview Outcome      | Single select     | unattended, attended_selected, attended_rejected (allow empty) |
| Interview              | Single line text  | Human label: Unattended, Attended — selected, etc. |
| Rejection Reason Code  | Single select     | grades_mismatch, income_mismatch, identity_mismatch, no_travel_budget, other (allow empty) |
| Rejection Reason       | Long text         | Full rejection text from interviewer |
| Notes                  | Long text         | System notes (FIFO, waitlist promotion) |

Import the CSV template with 2 sample rows.

Create views:
1. "All applications" — sort by Applied At ascending (FIFO)
2. "Screening list" — Status is selected OR waitlist OR interview_confirmed
3. "Final confirmed" — Status is interview_confirmed

Do NOT omit any column — the app writes all of them on every sync.
```

---

## If you already have a base

Add any **missing columns** from the table above (Omni: "Add these columns to Student Applications: …").

Then re-sync from the app: **Load demo students** → **Run fair allocation**.

Or run locally:

```bash
cd vibecert
python scripts/seed_demo.py
python -c "from dotenv import load_dotenv; load_dotenv('.env'); from scholarship_grants.seed_data import SEED; from scholarship_grants.storage import replace_all; replace_all(SEED); print('Synced', len(SEED), 'rows to Airtable')"
```
