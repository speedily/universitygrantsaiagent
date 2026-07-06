# University Grants AI Agent

**Track:** Agents for Good  
**Course:** 5-Day AI Agents — Intensive Vibe Coding with Google  
**Author:** [Your Name]  
**GitHub:** [YOUR_REPO_URL]  
**Live demo:** https://universitygrantsaiagent.vercel.app  
**Video:** [YOUR_YOUTUBE_URL]

---

## Problem

Universities worldwide distribute scholarship funds manually. Human reviewers introduce unconscious bias (country, name, school prestige) and inconsistent rule application. Small institutions lack budget for fair review systems.

## Solution

**University Scholarship Grants AI Agent** is a free, open-source pipeline that:

1. Collects student applications via a web form
2. Applies **deterministic eligibility rules** (no LLM in the decision path)
3. Allocates grants under a fixed **$1M USD budget** using **FIFO** timestamps
4. Uses **Google ADK multi-agents** with **OpenAI (LiteLLM)** only to *explain* outcomes to administrators — not to decide awards

This separates **fair computation** from **human-readable narrative**, reducing bias while keeping transparency.

## Scholarship rules (fixed, auditable)

| Rule | Value |
|------|-------|
| Eligible | Family income **< $12,000 USD/year** (converted from local currency) **and** marks ≥ 50% (or Grade B+) |
| Tier A | ≥ 70% or Grade A → **$150,000 USD** |
| Tier B | 50–69% or Grade B → **$50,000 USD** |
| Budget cap | **$1,000,000 USD** total |
| Tie-break | **FIFO** by `applied_at` when budget exceeded → Selected (green) vs Waitlist (orange) |

Documents (marks proof, tax filings) are requested by email after shortlisting — not on the public form — mirroring real university workflows.

## Architecture

```
Student form (FastAPI + static HTML / Streamlit)
        ↓
Storage layer (JSON file locally · Airtable REST on Vercel)
        ↓
Deterministic rules engine (Python — eligibility + tiers + FIFO)
        ↓
ADK agents (OpenAI via LiteLLM) — explain allocation summary
        ↓
Dashboard — Selected 🟢 / Waitlist 🟠 / Ineligible
```

### Why deterministic core?

LLMs should not decide who receives financial aid. The allocation engine is pure Python with unit tests. Agents add value by summarizing results for deans and documenting policy compliance.

## Capstone concepts demonstrated

| Concept | Implementation |
|---------|----------------|
| **ADK** | `agents/runner.py` — `LlmAgent` + `InMemoryRunner` |
| **Multi-agent** | Eligibility explainer + Allocator explainer agents |
| **Tools** | Airtable REST client + JSON storage fallback |
| **Agent skill** | `skills/SCHOLARSHIP_ALLOCATION.md` — policy rules for agents |
| **Evaluations** | `tests/test_allocate.py` — 5 pytest cases (eligibility, tiers, FIFO waitlist) |

## Demo walkthrough

1. Open live URL → **Grants Agent Dashboard**
2. Click **Load demo students** (24 global applicants, multiple currencies)
3. Click **Run fair allocation**
4. Observe: 8 selected, 4 waitlist, 1 ineligible; budget bar at $1M cap
5. Read ADK agent explanation (with `OPENAI_API_KEY`) or deterministic fallback text

## Tech stack

- **Python 3.11+**, FastAPI, Uvicorn
- **Google ADK** + **LiteLLM** → OpenAI (`gpt-4o-mini`)
- **Streamlit** for local recording
- **Vercel** serverless deploy (`/tmp` storage + seed API)
- Optional **Airtable** for persistent cloud storage

## Future work

- Interview scheduling agent + no-show → waitlist promotion
- Per-university policy packs as additional skills
- Audit log export for compliance

## Conclusion

This project shows how agent frameworks can orchestrate **transparent, bias-resistant public-good workflows** when critical decisions stay in tested code and agents handle explanation and ops tooling.

---

*Word count target: ≤ 2,500 words. Expand Future work / ethics section before submit. Add cover image (dashboard screenshot with green/orange rows).*
