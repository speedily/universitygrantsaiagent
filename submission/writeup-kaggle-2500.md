# University Grants AI Agent — Kaggle Write-Up

**Track:** Agents for Good  
**GitHub:** https://github.com/speedily/universitygrantsaiagent  
**Live demo:** https://universitygrantsaiagent.vercel.app  
**Video:** [Add your YouTube URL]

---

## The Problem: Bias and Inconsistency in Scholarship Allocation

Every year, universities around the world distribute millions of dollars in scholarship and grant aid. For most institutions—especially smaller colleges in emerging economies—this process remains manual. Admissions staff read paper or PDF applications, compare academic marks against internal cutoffs, estimate whether a family's income qualifies as "low enough," and then debate who should receive limited funding. This workflow is slow, expensive, and deeply vulnerable to unconscious bias.

Research in behavioral economics shows that human reviewers introduce noise into high-stakes decisions. Reviewers may unconsciously favor applicants from familiar countries or names that sound similar to their own. Two students with identical marks and income can receive different outcomes depending on which committee member reads their file first. When budget is tight, tie-breaking becomes arbitrary: alphabetical order, informal "gut feel," or no reproducible audit trail if challenged by regulators.

Small universities in the Global South face an additional barrier: they often lack enterprise grant-management software entirely. Staff rely on spreadsheets, email threads, and handwritten notes. There is no single source of truth, no timestamped application order, and no standardized way to compare a student from Nigeria (income in Naira) with a student from Japan (income in Yen) against the same need threshold. The result is inconsistent rule application across countries and academic cycles—precisely the kind of inequity that **Agents for Good** projects should address.

Financial aid is also not a domain where "AI vibes" should decide outcomes. A large language model should never silently award or deny a scholarship based on probabilistic text generation. Students' futures are at stake; decisions must be auditable, reproducible, and explainable. Yet modern agent frameworks—including **Google Agent Development Kit (ADK)**—are extremely valuable for orchestrating the *surrounding* workflow: collecting applications, syncing records to external databases, explaining policy outcomes to administrators, and keeping humans in the loop for interviews and document verification.

**University Grants AI Agent** is my capstone submission for the Kaggle × Google 5-Day AI Agents Intensive Vibe Coding Course. It is a free, open-source pipeline that helps any university run a **fair, auditable scholarship program** under fixed, published rules. Critical financial decisions are made by tested Python code. **Google ADK multi-agents** with **OpenAI via LiteLLM** are used only to *explain* results to administrators—they never change who receives funding.

---

## Solution Overview

The system implements the complete lifecycle of a merit-and-need scholarship program:

**Student application.** A public web form collects name, email, phone, country, semester, marks (percentage), and family yearly income in local currency. Letter grades are computed automatically from marks using transparent rules: Grade A for marks ≥ 70%, Grade B for 50–69%, Grade C for 40–49%, and Fail below 40% (applications below 40% are rejected at submission and not accepted for admission). Proof of marks and tax documents is *not* collected on the public form; shortlisted students receive an email request before their online interview, mirroring how real universities handle sensitive documents.

**Deterministic allocation.** A pure Python rules engine evaluates every applicant with identical logic. A student is eligible if their family income converts to strictly less than **$12,000 USD per year** AND their marks are at least **50%**. Tier A awards (**$150,000 USD**) go to students with marks ≥ 70%. Tier B awards (**$50,000 USD**) go to students with marks between 50% and 69%. The university budget cap is **$1,000,000 USD** per cycle. When the budget is exhausted, eligible students who applied earlier (FIFO by server timestamp) receive funding first; later eligible students are placed on a **waitlist** (shown in orange on the dashboard). Students who fail eligibility—whether due to high income or low marks—are marked **ineligible** (grey).

**Administrator dashboard.** After allocation, staff see a sortable table with color-coded status, income in both local currency and USD equivalent, tier, award amount, and interview controls. Metrics at the top show selected count, waitlist count, total spent, and remaining budget with a visual progress bar.

**Online interview workflow.** Selected students proceed to an online interview (documents verified by email beforehand). Interviewers record outcomes directly in the dashboard: unattended (no-show), attended and confirmed, or attended and rejected. Rejections require a standardized reason (grades mismatch, income mismatch, identity mismatch, no travel budget, or a custom "other" explanation). If a selected student no-shows or is rejected, their slot is released and the next waitlisted student is **promoted automatically in FIFO order**—ensuring the budget is fully utilized without manual spreadsheet shuffling.

**Export and persistence.** After allocation, results auto-sync to **Airtable** so data survives serverless cold starts on Vercel. Administrators can perform a final **Save to Airtable & download CSV** to export the screening list for downstream systems.

The architectural principle is simple and non-negotiable: **no LLM participates in eligibility or award calculation.** Agents explain; code decides.

---

## Why This Fits the "Agents for Good" Track

Education funding is one of the highest-impact domains for equitable technology. A student who receives a scholarship may be the first in their family to attend university; a student who is unfairly denied may lose that opportunity permanently. This project targets **equitable access to education** by applying the same numeric rules to every applicant regardless of country, name, or background.

The demo dataset includes 24 synthetic students from India, Nigeria, Brazil, China, Egypt, Ireland, Italy, Japan, Pakistan, USA, Romania, Mexico, Kenya, Vietnam, South Africa, Philippines, United Kingdom, Canada, Germany, UAE, and more. Each submits income in local currency (INR, NGN, BRL, CNY, EGP, EUR, JPY, PKR, USD, etc.). The currency module converts all incomes to USD before comparison, so a student earning ₹850,000/year in India is evaluated on the same $12,000 threshold as a student earning €9,500/year in Ireland. This global inclusivity is essential for universities that recruit internationally.

The project is **free and open source** under the MIT license. Any institution can fork the repository at https://github.com/speedily/universitygrantsaiagent, adjust budget and tier constants via environment variables, and deploy to Vercel without Google Cloud billing or Gemini API keys. That lowers the barrier for schools that cannot afford commercial scholarship software—directly aligned with the public-good mission of this capstone track.

---

## Architecture

The pipeline follows a layered design that separates concerns clearly:

```
Student Application Form (FastAPI + static HTML)
        ↓
Storage layer (JSON locally · Airtable REST on Vercel)
        ↓
Deterministic rules engine (scholarship_grants/allocate.py)
        ↓
Google ADK multi-agents (OpenAI LiteLLM) — explain summary only
        ↓
Dashboard + Interview HITL + CSV export
```

**Backend:** Python 3.11+, FastAPI for REST APIs, Pydantic for request validation, httpx for Airtable HTTP calls, and pytest for evaluations.

**Production UI:** A responsive static HTML dashboard deployed on Vercel at https://universitygrantsaiagent.vercel.app. No frontend framework required—the page calls JSON APIs for all operations.

**Local development UI:** A Streamlit app with two tabs (Application form + Dashboard) for rapid iteration and video recording without deploying.

**Storage strategy:** Locally, applications persist in a JSON file. On Vercel serverless, JSON writes go to `/tmp` (ephemeral per instance). To solve cold-start data loss, the system merges local JSON with **Airtable** records on read and auto-syncs after allocation and interview saves. Airtable acts as the durable "reference point" for Application IDs across requests.

**Currency module:** `scholarship_grants/currency.py` maintains a reproducible conversion table from local currencies to USD. Eligibility always compares USD-equivalent income, never raw local numbers against an arbitrary cutoff. This design choice makes unit tests deterministic: the same input always produces the same output.

---

## Google ADK Multi-Agent Design

Implementation lives in `agents/runner.py`. Two **LlmAgent** instances are configured with **LiteLLM** pointed at OpenAI (`gpt-4o-mini` by default). Both run through ADK's **InMemoryRunner**, which manages session state and event streaming per the course's ADK patterns.

**eligibility_agent** receives the allocation summary JSON and explains how many students passed income and marks rules. Its system instruction emphasizes bias-free deterministic filtering: same rules for every country, income compared only after USD conversion, no subjective judgment in the automated phase.

**allocator_agent** receives the same summary and explains budget utilization: how many Tier A vs Tier B awards were granted, how much of the $1M cap was spent, why waitlisted students were not funded (FIFO timestamp order), and how many remain ineligible due to income or marks.

When an administrator clicks **Run fair allocation**, the pipeline executes in strict order:

1. Load all applications from merged JSON + Airtable storage
2. Run `allocate_applications()` — pure Python, fully deterministic
3. Save updated records locally and sync to Airtable
4. Pass the summary statistics JSON to both ADK agents sequentially
5. Display their natural-language explanation below the budget metrics on the dashboard

If `OPENAI_API_KEY` is not configured, a deterministic fallback message is returned—allocation still completes successfully. This graceful degradation demonstrates responsible agent deployment: the core public-good function never depends on LLM availability.

I chose **OpenAI via LiteLLM** rather than Gemini so the project runs with a single API key many developers already have, while still satisfying the ADK requirement.

---

## Agent Skill

File: `skills/SCHOLARSHIP_ALLOCATION.md`

Skills encode the full university scholarship policy: eligibility thresholds, tier awards, FIFO budget rules, document collection policy, interview outcomes, waitlist promotion, and anti-bias principles (no subjectivity in automated filter; tie-break only by timestamp).

---

## Tools Integration: Airtable as External Data Store

The Airtable REST client in `scholarship_grants/airtable_client.py` implements MCP-style external tool integration:

- **Upsert** records by stable Application ID (UUID v5 derived from email for demo students)
- **Fetch** all records for serverless cold-start recovery
- **Clear all** records in batches for demo resets
- **Resilient error handling** — unknown column names and invalid single-select values are skipped automatically so partial Airtable bases still sync

The schema maps every dashboard field: name, email, phone, country, marks, grade, income local/USD, applied date/time, status, tier, award, interview outcome, rejection reason, and system notes. This satisfies the capstone **Tools / MCP-style integration** requirement: the agent pipeline reads and writes external state through a defined tool interface, not hard-coded in-memory-only storage.

---

## Evaluations, Security, and Fairness

The project includes **15 pytest evaluation tests** across three files—well above the ~5 cases recommended in the capstone guidelines:

- **tests/test_allocate.py** — high-income rejection, USD conversion accuracy, Tier A and Tier B award assignment, FIFO waitlist ordering when budget is exceeded across seven competing applicants
- **tests/test_interview.py** — no-show triggers waitlist promotion, rejection requires reason, attended-selected confirms scholarship, custom "other" rejection text is stored
- **tests/test_grading.py** — marks-to-grade boundary tests for A (≥70), B (50–69), C (40–49), and Fail (<40)

These tests function as the project's **eval suite**: any change to allocation logic must pass before deployment. They provide reproducible evidence that the system behaves correctly on happy paths and edge cases—exactly what judges look for when evaluating agent quality.

**Security and fairness design choices:**

- **No LLM in the decision path** — the primary guardrail against biased or hallucinated awards
- **Human-in-the-loop (HITL)** — interview outcomes require explicit administrator action; nothing is auto-rejected by AI
- **Mandatory rejection reasons** — attended-rejected cases must specify why, creating an audit trail
- **Fail grade blocked at submission** — marks below 40% cannot enter the pipeline
- **No secrets in GitHub** — `.env` is gitignored; `.env.example` documents all keys without values
- **Deterministic FX conversion** — same inputs always produce same USD equivalent for testing and audits

---

## Live Demo Walkthrough

Open **https://universitygrantsaiagent.vercel.app** and follow this sequence (also shown in the demo video):

**Step 1 — Application form.** On the Scholarship Application tab, submit a student (for example: 72% marks, India, ₹850,000 family income). The form auto-calculates Grade B. After submit, the dashboard opens with the new pending row.

**Step 2 — Load demo data.** Click **Load demo data** to append 24 global demo students with phone numbers and varied currencies. Existing form submissions are preserved (append, not replace).

**Step 3 — Run fair allocation.** Click **Run fair allocation**. A loading spinner appears (~30 seconds) while the deterministic engine runs, ADK agents generate explanations, and Airtable syncs. Results: approximately 8 selected (green), 14 waitlist (orange), 2 ineligible (grey—e.g., applicants whose USD-equivalent income exceeds $12,000). The budget progress bar reaches the $1M cap.

**Step 4 — Interview.** On a selected student, choose an interview outcome. For rejection, select a reason or enter custom "other" text and click Save. A no-show or rejection promotes the next waitlisted student in FIFO order.

**Step 5 — Export.** Click **Save to Airtable & download CSV** for the final screening export.

**Reset for a clean take:** **Clear all data** wipes both local storage and Airtable.

---

## Three Demo Scenarios (Video)

The demo video shows three scenarios as required by capstone guidelines:

1. **Happy path** — form submission → load demo → allocate → green selected rows with Tier A/B awards and ADK explanation text
2. **Edge case** — ineligible high-income applicant (e.g., Tom Rich, $95,000 USD income) stays grey; marks below 40% rejected at form submission
3. **Eval / security** — terminal runs `pytest tests/ -q` (15 passed); narration explains "decisions are Python, not LLM" and shows interview HITL controls

---

## Repository and Tech Stack

**GitHub:** https://github.com/speedily/universitygrantsaiagent

Key directories:

- `app/` — FastAPI routes, Vercel entrypoint, static web UI
- `agents/runner.py` — ADK + OpenAI LiteLLM (2 agents)
- `scholarship_grants/` — allocate.py, currency.py, storage.py, airtable_client.py, grading.py
- `skills/SCHOLARSHIP_ALLOCATION.md` — agent policy skill
- `tests/` — 15 pytest eval cases
- `streamlit_app.py` — local two-tab demo UI

**Stack:** Python 3.11+, FastAPI, google-adk, litellm, httpx, pydantic, pytest, Vercel serverless, optional Airtable. No Gemini API key required.

---

## Course Concepts Demonstrated

- **ADK** — LlmAgent, InMemoryRunner, LiteLLM model binding, async session handling
- **Multi-agent** — eligibility_agent + allocator_agent sequential explain flow
- **Tools** — Airtable REST client with upsert, fetch, clear, resilient 422 handling
- **Agent skills** — SCHOLARSHIP_ALLOCATION.md policy file
- **Evaluations** — 15 pytest tests covering allocation, interviews, and grading boundaries

All five course concept categories are demonstrated—exceeding the minimum requirement of three.

---

## Ethics, Limitations, and Future Work

**Ethics:** Scholarship decisions affect real lives. This project intentionally keeps award logic in auditable, tested code. Agents assist administrators with explanation and operational sync—not with authority over who receives aid. Income conversion uses static demo rates for reproducibility; a production deployment would integrate a certified FX API with dated rate snapshots for regulatory compliance.

**Limitations:** Vercel `/tmp` storage is ephemeral; Airtable sync after allocation is required for reliable persistence across serverless instances. The demo uses synthetic students—not real PII.

**Future work:** Per-university policy packs as agent skills; interview scheduling with calendar integration; audit log export; certified FX provider; multilingual forms.

---

## Conclusion

University Grants AI Agent demonstrates how **Google ADK** and multi-agent orchestration can serve the public good when paired with **deterministic, tested business logic**. The system gives universities worldwide a fair, transparent, globally inclusive scholarship workflow—free to deploy, open to inspect, and designed so agents **explain** rather than **decide**.

**Live demo:** https://universitygrantsaiagent.vercel.app  
**Source code:** https://github.com/speedily/universitygrantsaiagent
