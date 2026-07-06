# Plan — University Scholarship Grants AI Agent (E★ MVP)

**Approved:** July 6, 2026 · **Build target:** ~3 hours · **Deploy:** Vercel + GitHub

## Goal

Bias-free scholarship allocation for universities — **Agents for Good** capstone.

## Stack

| Layer | Choice |
|---|---|
| Rules engine | Python `allocate.py` (deterministic) |
| Agents | Google **ADK** + **OpenAI** LiteLLM (2 agents) |
| Storage | Airtable (optional) + JSON fallback |
| Local UI | Streamlit 2 tabs |
| Production UI | **FastAPI** on **Vercel** |
| LLM | `OPENAI_API_KEY` only — no Gemini |

## Capstone concepts (≥3)

1. ADK · 2. Multi-agent · 3. Tools (Airtable) · 4. eval tests · 5. SKILL.md (bonus)

## Rules

- Eligible: income < ₹500,000 AND marks ≥ 50%
- Tier A (≥70%): $150,000 · Tier B (50–69%): $50,000
- Budget: $1,000,000 USD · FIFO by `applied_at`
- Status: Selected (green) / Waitlist (orange) / Ineligible

## User keys needed

- `OPENAI_API_KEY` (optional for agent explain; allocation works without)
- `AIRTABLE_API_KEY` + `AIRTABLE_BASE_ID` (optional; JSON fallback)
