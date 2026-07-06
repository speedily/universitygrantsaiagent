# University Grants AI Agent

**Track:** Agents for Good  
**Capstone:** [Kaggle × Google 5-Day AI Agents Intensive](https://www.kaggle.com/competitions/vibecoding-agents-capstone-project)  
**Live demo:** https://universitygrantsaiagent.vercel.app  
**GitHub:** https://github.com/speedily/universitygrantsaiagent

Bias-free scholarship allocation for universities worldwide. **Financial decisions are deterministic Python code** — **Google ADK multi-agents** (OpenAI via LiteLLM) only *explain* outcomes to administrators. No Gemini API required.

---

## Capstone minimum requirements — how this project meets them

| Requirement | Status | Where in this repo |
|-------------|--------|-------------------|
| **Google ADK** | ✅ | [`agents/runner.py`](agents/runner.py) — `LlmAgent`, `InMemoryRunner`, LiteLLM |
| **Multi-agent (≥2)** | ✅ | **eligibility_agent** + **allocator_agent** (see below) |
| **Tools / MCP-style** | ✅ | [`scholarship_grants/airtable_client.py`](scholarship_grants/airtable_client.py) — Airtable REST upsert/fetch/clear |
| **Agent skill** | ✅ | [`skills/SCHOLARSHIP_ALLOCATION.md`](skills/SCHOLARSHIP_ALLOCATION.md) |
| **Security / eval** | ✅ | **15 pytest tests** + no-LLM decision path + interview HITL |
| **Working end-to-end demo** | ✅ | [Live Vercel app](https://universitygrantsaiagent.vercel.app) + Streamlit local |
| **Public GitHub, no secrets** | ✅ | `.env` gitignored; [`.env.example`](.env.example) documents keys |
| **OpenAI in README** | ✅ | `OPENAI_API_KEY` in `.env.example` |
| **~5 eval tests** | ✅ | **15 tests** in [`tests/`](tests/) |
| **Agents for Good track** | ✅ | Equitable global scholarship access |

**All 5 course concept categories are demonstrated** (minimum required: 3).

---

## Two ADK agents (multi-agent design)

Implementation: [`agents/runner.py`](agents/runner.py)

After **Run fair allocation**, the deterministic engine produces a JSON summary (selected count, waitlist count, budget spent, etc.). Two ADK **LlmAgent** instances run sequentially via **InMemoryRunner** with **LiteLLM → OpenAI** (`gpt-4o-mini`):

| Agent | Name | Role |
|-------|------|------|
| 1 | **eligibility_agent** | Explains how many students passed income (< $12k USD/year) and marks (≥ 50%) rules; emphasizes bias-free, country-neutral filtering |
| 2 | **allocator_agent** | Explains budget usage, Tier A/B awards, FIFO waitlist when the $1M cap is reached, and remaining funds |

**Important design choice:** agents **never change** who receives funding. They only generate natural-language explanations for the dashboard. If `OPENAI_API_KEY` is missing, allocation still runs with a deterministic fallback message.

```python
# agents/runner.py (simplified)
eligibility_agent = LlmAgent(model=LiteLlm(model=OPENAI_MODEL), name="eligibility_agent", ...)
allocator_agent = LlmAgent(model=LiteLlm(model=OPENAI_MODEL), name="allocator_agent", ...)
# Both invoked via InMemoryRunner after allocate_applications() completes
```

---

## Tools: Airtable integration

[`scholarship_grants/airtable_client.py`](scholarship_grants/airtable_client.py) implements MCP-style external tool integration:

- **Upsert** records by Application ID after allocation and interview saves
- **Fetch** records for serverless cold-start recovery (merge with local JSON)
- **Clear all** for demo resets
- Resilient handling of missing columns / invalid single-select values

Auto-sync runs after **Run fair allocation** and on interview **Save**.

---

## Agent skill

[`skills/SCHOLARSHIP_ALLOCATION.md`](skills/SCHOLARSHIP_ALLOCATION.md) encodes university policy for agents and operators:

- Eligibility thresholds and tier awards ($150k / $50k)
- $1M budget cap and FIFO tie-breaking
- Document collection by email (not on public form)
- Online interview outcomes and waitlist promotion
- Anti-bias principles (no subjectivity in automated filter)

---

## Evaluations & security (15 pytest tests)

```bash
python -m pytest tests/ -q   # 15 passed
```

| File | What it tests |
|------|----------------|
| [`tests/test_allocate.py`](tests/test_allocate.py) | Income rejection, USD conversion, Tier A/B, FIFO waitlist under budget cap |
| [`tests/test_interview.py`](tests/test_interview.py) | No-show → waitlist promotion, rejection reasons, confirmation |
| [`tests/test_grading.py`](tests/test_grading.py) | Marks → grade boundaries (A/B/C/Fail) |

**Security & fairness guardrails:**

- **No LLM in the decision path** — awards computed by [`scholarship_grants/allocate.py`](scholarship_grants/allocate.py)
- **Human-in-the-loop (HITL)** — interview outcomes require administrator action in the dashboard
- **Mandatory rejection reasons** for attended-rejected interviews
- **Fail grade blocked** — marks below 40% rejected at form submission
- **No secrets committed** — see [`.gitignore`](.gitignore)

---

## Architecture

```
Student Application Form (FastAPI + static HTML)
        ↓
Storage (JSON locally · Airtable REST on Vercel)
        ↓
Deterministic rules engine (allocate.py — NO LLM)
        ↓
Google ADK: eligibility_agent + allocator_agent (explain only)
        ↓
Dashboard: Selected 🟢 / Waitlist 🟠 / Ineligible + Interview HITL + CSV
```

---

## Scholarship rules

| Rule | Value |
|------|-------|
| Eligible | Income **< $12,000 USD/year** (converted from local currency) AND marks **≥ 50%** |
| Tier A | Marks ≥ 70% → **$150,000 USD** |
| Tier B | Marks 50–69% → **$50,000 USD** |
| Budget | **$1,000,000 USD** — FIFO by application timestamp |
| Grades | A ≥70%, B 50–69%, C 40–49%, Fail <40% (not accepted) |

---

## Live demo walkthrough

Open https://universitygrantsaiagent.vercel.app

1. **Clear all data** — fresh demo
2. **Load demo data** — 24 global students (append; keeps form submissions)
3. **Run fair allocation** — spinner ~30s; ADK agents explain; Airtable auto-syncs
4. Record **interview** outcomes on selected students
5. **Save to Airtable & download CSV**

**Three video scenarios for judges:**

1. **Happy path** — form → allocate → green selected rows + ADK explanation
2. **Edge case** — ineligible high-income student (grey); Fail grade rejected on form
3. **Eval / security** — `pytest tests/ -q` + “decisions are Python, not LLM” + interview HITL

---

## Quick start (local)

```bash
git clone https://github.com/speedily/universitygrantsaiagent.git
cd universitygrantsaiagent
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

---

## Deploy to Vercel

```bash
vercel --prod
```

| Variable | Purpose |
|----------|---------|
| `OPENAI_API_KEY` | ADK agent explanations on allocate |
| `AIRTABLE_API_KEY` + `AIRTABLE_BASE_ID` | Persistent cloud storage |

---

## Project structure

```
├── app/                      # FastAPI + Vercel entry + static web UI
├── agents/runner.py          # ★ ADK multi-agent (eligibility + allocator)
├── scholarship_grants/       # allocate.py, currency, storage, Airtable tool
├── skills/                   # ★ SCHOLARSHIP_ALLOCATION.md agent skill
├── tests/                    # ★ 15 pytest eval tests
├── submission/               # Kaggle write-up + video script
├── scripts/seed_demo.py
└── streamlit_app.py
```

---

## Tech stack

- Python 3.11+, FastAPI, Pydantic, httpx, pytest
- **google-adk** + **litellm** → OpenAI (optional; no Gemini required)
- Vercel serverless + optional Airtable
- Streamlit for local demo

---

## Kaggle submission links

- **Write-up:** see [`submission/writeup-kaggle-2500.md`](submission/writeup-kaggle-2500.md)
- **Video script:** see [`submission/video-script.md`](submission/video-script.md)
- **Competition:** https://www.kaggle.com/competitions/vibecoding-agents-capstone-project

---

## License

MIT — free for universities worldwide.
