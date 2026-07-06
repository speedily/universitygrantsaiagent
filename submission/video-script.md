# YouTube demo script (≤ 5 minutes)

**Title:** University Grants AI Agent — Bias-Free ADK Capstone

## 0:00 — Hook (30s)

- "Scholarship committees are biased. This free agent allocates $1M fairly using rules + FIFO — built with Google ADK and OpenAI."
- Show dashboard with green Selected and orange Waitlist rows.

## 0:30 — Problem (30s)

- Manual review → inconsistent rules, unconscious bias
- Small universities can't afford enterprise systems
- **Agents for Good:** free, open source, global

## 1:00 — Live demo: Application form (45s)

- Tab: **Scholarship Application**
- Fill sample student (marks 72%, income ₹350k, India)
- Submit → "saved to student records"
- Mention docs collected by email before interview

## 1:45 — Load demo + allocate (90s)

- Switch to **Grants Agent Dashboard**
- Click **Load demo students** (24 applicants, global currencies)
- Click **Run fair allocation**
- Point out metrics: Selected / Waitlist / Spent / Remaining
- Budget progress bar hits $1M cap
- Scroll table:
  - 🟢 Tier A $150k selected
  - 🟠 waitlisted (FIFO — applied later)
  - Tom Rich ineligible (income too high)

## 3:15 — Architecture (60s)

- Screen share `scholarship_grants/allocate.py` — "decisions are Python, not LLM"
- Quick peek at `agents/runner.py` — ADK + LiteLLM OpenAI explains summary
- `skills/SCHOLARSHIP_ALLOCATION.md` — agent policy skill
- `tests/test_allocate.py` — pytest evals

## 4:15 — Capstone + links (45s)

- GitHub repo URL (public)
- Vercel live URL
- Kaggle competition submission
- "No Gemini key required — OpenAI optional for explanation only"

## 4:45 — Close (15s)

- "Deterministic fairness + agent orchestration = trustworthy grants for any university."

---

**Recording tips**

- Record at 1080p; browser zoom 110%
- Use seeded demo on Vercel: Load demo → Allocate (no local setup on video)
- Optional: split screen terminal running `pytest tests/ -q` for 3 seconds
