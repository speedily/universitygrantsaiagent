# University Grants AI Agent

**Project slug:** `universitygrantsaiagent`  
**Agents for Good** capstone — Kaggle × Google 5-Day AI Agents Vibe Coding Course.

Remove bias from scholarship grant allocation using **deterministic rules** orchestrated by **Google ADK** multi-agents and **OpenAI** (no Gemini API required).

## Live demo

- **Production:** https://universitygrantsaiagent.vercel.app
- **Local UI:** Streamlit or FastAPI static web

## Quick start (local)

```bash
cd vibecert
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # add OPENAI_API_KEY (optional) and AIRTABLE_* (optional)

python scripts/seed_demo.py
python -m pytest tests/ -q

# Option A — Streamlit
streamlit run streamlit_app.py

# Option B — FastAPI + web UI
uvicorn app.vercel_app:app --reload --port 8080
# open http://localhost:8080
```

## Deploy to Vercel

```bash
cd vibecert
vercel --prod
```

**Vercel env vars (optional):**

| Variable | Purpose |
|----------|---------|
| `OPENAI_API_KEY` | ADK agent explanation on allocate |
| `AIRTABLE_API_KEY` + `AIRTABLE_BASE_ID` | Persistent cloud storage |

**Demo on Vercel:** Dashboard → **Load demo students** (24 global applicants) → **Run fair allocation**.

## Push to GitHub

```bash
cd vibecert
git add .
git commit -m "University Grants AI Agent capstone"
gh repo create universitygrantsaiagent --public --source=. --push
```

## Architecture

```
Student Application Form → storage (JSON / Airtable MCP-style tools)
        ↓
Local income → USD conversion → eligibility check
        ↓
Eligibility + Allocator (Python rules — bias-free)
        ↓
ADK agents (OpenAI LiteLLM) explain results
        ↓
Dashboard: Selected (green) / Waitlist (orange) / Ineligible
```

## Scholarship rules

| Rule | Value |
|------|-------|
| Eligible | Income **< $12,000 USD/year** (converted from local currency) AND marks ≥ 50% |
| Tier A | ≥70% → **$150,000** |
| Tier B | 50–69% → **$50,000** |
| Budget | **$1,000,000 USD** FIFO by application time |

## Capstone concepts

- ADK · Multi-agent · Tools (Airtable) · Agent skill (`skills/`) · Eval tests

## Kaggle submission checklist

- [ ] Join [capstone competition](https://www.kaggle.com/competitions/vibecoding-agents-capstone-project)
- [ ] Public GitHub repo (`universitygrantsaiagent`)
- [ ] YouTube ≤5 min demo (form → allocate → green/orange table)
- [ ] Write-up ≤2500 words + cover image
- [ ] Link live Vercel URL in write-up

## Project structure

```
vibecert/
├── app/                 # FastAPI + Vercel entry + static web UI
├── agents/              # ADK + OpenAI LiteLLM
├── scholarship_grants/  # Core allocation engine + currency conversion
├── skills/              # SCHOLARSHIP_ALLOCATION.md
├── tests/
├── scripts/seed_demo.py
└── streamlit_app.py
```

## License

MIT — free for universities worldwide.
