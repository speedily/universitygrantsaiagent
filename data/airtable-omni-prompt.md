# Airtable Omni prompt — University Grants AI Agent

Copy the prompt below into **Airtable Omni** (or use **Import CSV** with `airtable-applications-template.csv`).

---

## Omni prompt

```
Create a base called "University Grants AI Agent" for scholarship application tracking.

Create one table named exactly: Student Applications

Use these columns with these field types (names must match exactly — our API writes to these headers):

| Column name           | Field type        | Notes |
|-----------------------|-------------------|-------|
| Application ID        | Single line text  | Primary identifier (UUID from app) |
| Name                  | Single line text  | Student full name |
| Email                 | Email             | |
| Country               | Single line text  | |
| Semester              | Single line text  | e.g. Fall 2026 |
| Academic Year         | Single line text  | e.g. 2026–2027 |
| Marks Pct             | Number            | Decimal, 0–100 |
| Grade                 | Single select     | Options: A, B, C (allow empty) |
| Family Income Local   | Number            | Yearly income in local currency |
| Currency              | Single line text  | ISO code: INR, USD, NGN, EUR, etc. |
| Family Income USD     | Number            | USD equivalent for eligibility |
| Applied At            | Single line text  | ISO datetime when form submitted |
| Status                | Single select     | Options: pending, eligible, selected, waitlist, ineligible, interview_confirmed, no_show, interview_rejected |
| Tier                  | Single select     | Options: A, B (allow empty) |
| Award USD             | Number            | Scholarship amount in USD |
| Interview Outcome     | Single select     | Options: unattended, attended_selected, attended_rejected (allow empty) |
| Rejection Reason      | Long text         | Interviewer reason if rejected |
| Notes                 | Long text         | System notes (FIFO, promotion, etc.) |

After creating the table, import the sample CSV I provide (2 demo rows).

Create a grid view sorted by "Applied At" ascending (FIFO order).

Add a filtered view "Screening list" showing Status is any of: selected, interview_confirmed, waitlist.

Add a filtered view "Final confirmed" showing Status is interview_confirmed.
```

---

## After Omni creates the base

1. Open the base → **Help → API documentation** (or base URL) and copy **Base ID** (`appXXXXXXXXXXXXXX`).
2. Create a Personal Access Token at https://airtable.com/create/tokens with scopes:
   - `data.records:read`
   - `data.records:write`
   - Access to this base only
3. Put secrets in **`.env`** (local), **not** `.env.example`:

```bash
cp .env.example .env
# Edit .env — paste your real keys there
```

4. For **Vercel**: Project → Settings → Environment Variables → add the same three vars.
5. Redeploy: `vercel --prod`

Table name must be exactly: `Student Applications` (or set `AIRTABLE_APPLICATIONS_TABLE` in env).
