# Add missing columns to existing Airtable base

Paste into **Airtable Omni** if your table already exists but is missing dashboard fields:

```
In the "Student Applications" table, ADD these missing columns (do not rename existing ones):

| Column name            | Field type        |
|------------------------|-------------------|
| Phone                  | Single line text  |
| Income Local           | Number            |
| Income USD             | Number            |
| Applied Date           | Single line text  |
| Applied Time           | Single line text  |
| Interview Outcome      | Single select — options: unattended, attended_selected, attended_rejected |
| Interview              | Single line text  |
| Rejection Reason Code  | Single select — options: grades_mismatch, income_mismatch, identity_mismatch, no_travel_budget, other |
| Rejection Reason       | Long text         |

Keep existing columns: Application ID, Name, Email, Country, Semester, Academic Year, Marks Pct, Grade, Currency, Applied At, Status, Tier, Award USD, Notes, Family Income Local, Family Income USD.

After adding columns, I will re-sync from the app (Load demo students → Run allocation).
```
