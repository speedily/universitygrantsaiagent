# Vibecert Capstone — Project Ideas

> **Deadline:** July 6, 2026, 11:59 PM PT (~July 7, 12:29 PM IST)  
> **Submit at:** [vibecoding-agents-capstone-project](https://www.kaggle.com/competitions/vibecoding-agents-capstone-project)

Use this doc to **select an idea against official min/max requirements** — not just visual appeal.

---

## Minimum vs maximum requirements (selection rubric)

There are **two different bars**. Pick your idea based on which bar you are aiming for.

### 🟢 MINIMUM — valid submission → badge + certificate

**Outcome:** Kaggle badge + certificate on your profile by **end of July 2026**.  
**Sources:** [Capstone #709721](https://www.kaggle.com/competitions/5-day-ai-agents-intensive-vibecoding-course-with-google/discussion/709721), [FAQs #708107](https://www.kaggle.com/competitions/5-day-ai-agents-intensive-vibecoding-course-with-google/discussion/708107)

| # | Requirement | Minimum (must have) | NOT required for certificate |
|---|---|---|---|
| 1 | **Join capstone** | Join [capstone competition](https://www.kaggle.com/competitions/vibecoding-agents-capstone-project) | Main course page only |
| 2 | **Kaggle write-up** | On capstone page; **≤ 2,500 words**; **cover image**; problem + features + tech + architecture | Perfect prose |
| 3 | **YouTube video** | **Public** (or unlisted); **≤ 5 min**; live agent demo + brief architecture | Pro video production |
| 4 | **GitHub repo** | **Public**; runnable code; **no secrets** | Cloud deployment |
| 5 | **Media gallery** | ≥1 image + YouTube link + GitHub link | Extra videos |
| 6 | **Track** | **Exactly one** of 4 tracks; problem fits track | Winning the track |
| 7 | **Team** | Solo or **≤ 4**; **one submission** only | — |
| 8 | **Course concepts** | **≥ 3** from list below (show in write-up + video) | All 5-day codelabs |
| 9 | **Working agent** | **ADK** agent runs locally; end-to-end demo | Antigravity, GCP, MCP server |
| 10 | **Deadline** | Before **July 6, 2026, 11:59 PM PT** | — |

**Minimum course concepts — need any 3+:**

| Concept | Minimum proof in project |
|---|---|
| **ADK** | Built with Google Agent Development Kit |
| **Multi-agent** | ≥2 agents or root + sub-agent flow |
| **Tools / MCP** | ≥1 custom `@tool` **or** MCP server hookup |
| **Agent skills** | `SKILL.md` or Agents CLI skill |
| **Security / eval** | HITL, guardrail, PII filter, or `tests/eval.py` |
| Spec-driven / production | Optional bonus only |

**Minimum agent quality:**

- Real problem tied to chosen track (narrow is OK)
- Video shows **≥3 scenarios** (happy path + edge + security/eval)
- README: run instructions + `GEMINI_API_KEY` or `OPENAI_API_KEY` in `.env.example`
- ~5 eval test cases in repo

**Explicitly NOT required for certificate:**

- Daily codelabs · Antigravity · Google Cloud/billing · MCP server · Top-3 placement

---

### 🔴 MAXIMUM — competitive → top 3 per track + swag + social feature

**Outcome:** Top **3 per track** (12 teams); Kaggle swag; social media feature.  
**Announced:** End of July 2026.

| # | Dimension | Maximum (judges weigh) | Minimum (certificate) |
|---|---|---|---|
| 1 | Problem impact | Strong real-world story for track | Plausible narrow use case |
| 2 | Architecture | Clean multi-agent design + diagram | 2 agents + tools |
| 3 | Code quality | Structure, tests, README, no secrets | Runs without crash |
| 4 | Security & eval | HITL + eval + guardrails **shown live** | One security/eval element |
| 5 | Course alignment | **4–5 concepts** named in video/write-up | **3 concepts** |
| 6 | Scalability | How it would scale in production (text OK) | Not needed |
| 7 | UI & demo | Polished UI; architecture segment in video | Basic UI OK |
| 8 | Presentation | Cover + screenshots + clear write-up | Cover image only |
| 9 | Deployment | Live URL (HF Spaces / Cloud Run) — bonus | Local demo OK |
| 10 | Track fit | Obviously belongs in chosen track | Kaggle may reassign |

**Hard caps (both min and max — do not exceed):**

| Item | Limit |
|---|---|
| Write-up | **≤ 2,500 words** |
| Video | **≤ 5 minutes** |
| Team size | **≤ 4** |
| Submissions | **1** per person/team |

---

## How to select an idea (match your goal)

| Your goal | Hit this bar | Best picks | Build |
|---|---|---|---|
| **Certificate, least time** | Minimum rows 1–10 + 3 concepts | **B, A, D, E** | 2.5–3h |
| **Certificate + good video** | Min + visual 8 + 3 demo scenarios | **A, C, F, H, J** | 3–4h |
| **Certificate + Good track** | Min + education/impact story | **C, I, E, M, N** | 3.5–4.5h |
| **Stretch for swag** | Max rows 1–8 + visual 9–10 | **G, I, L, H′, O** | 5–8h |

**All ideas A–O meet MINIMUM.** None guarantee MAXIMUM (winning) — that depends on execution and judge pool.

| Idea | Min concepts (of 5) | Max / judge strength |
|---|---|---|
| A, E, F, H | 5/5 | Business + security story |
| G, G′ | 5/5 | Multi-agent showcase |
| I, C | 5/5 | Good track + demo |
| B | 4/5 | Fastest min pass |
| O, L | 5/5 | Highest polish if time allows |

---

## Your checklist (minimum submission)

| You provide | Required? |
|---|---|
| `GEMINI_API_KEY` or `OPENAI_API_KEY` | One required (see below) |
| Join capstone on Kaggle | Yes |
| Record YouTube ≤5 min | Yes |
| Paste write-up + cover image | Yes (I draft) |
| Public GitHub repo | Yes |
| Mapbox token | Only idea **O** |

---

## Time budget (after idea is built)

| Deliverable | Who | Time |
|---|---|---|
| ADK agent + UI + GitHub | Me (after `plan.md` approved) | **2.5–8 h** |
| Kaggle write-up | Me drafts → you paste | **15–20 min** |
| YouTube demo | You record; I give script | **20–30 min** |
| Join capstone | You | **5 min** |

**Certificate total:** ~**3–5 h** (build + record + submit). Video is **mandatory** for both min and max.

### Course concepts we target (≥3 required, we aim for 4–5)

| Concept | How every MVP includes it |
|---|---|
| **ADK** | Python `google-adk` |
| **Multi-agent** | 2 agents (router + specialist) |
| **Tools** | 2–3 `@tool` functions |
| **Skills** | `skills/SKILL.md` |
| **Security / eval** | HITL or PII guard + `tests/eval.py` |

---

Optional: every MVP below includes a **recommended UI library** (not CLI-only unless noted).

---

## UI libraries we can use (Python ADK + frontend)

All agents stay **Python ADK** in the backend. UI is a thin layer on top — pick one tier per idea.

| Library | Best for | UI add-on time | Typical visual /10 | Notes |
|---|---|---|---|---|
| **CLI only** | Fastest certificate | +0 min | 3–4 | No UI — not recommended for video |
| **[Gradio](https://gradio.app)** | Forms, chat, file upload | +45–60 min | 6–7 | Fastest UI; custom CSS bump to 7 |
| **[Streamlit](https://streamlit.io)** | Dashboards, charts, wizards | +45–60 min | 6–7 | Great for gauges & metrics |
| **[NiceGUI](https://nicegui.io)** | Cards, grids, Tailwind-like layout | +60–75 min | **7–8** | Nicer than Gradio for dashboards |
| **[Chainlit](https://chainlit.io)** | Agent chat + tool steps visible | +50–70 min | **7–8** | Shows agent “thinking” steps in UI |
| **[Taipy](https://taipy.io)** | Business Kanban / pipeline views | +90 min | **8** | Expense & workflow ideas |
| **Gradio + Plotly** | Charts (carbon, health gauge) | +60 min | **8** | Data-viz ideas |
| **Next.js + [shadcn/ui](https://ui.shadcn.com) + Tailwind** | Production polish | +3–4 h | **9–10** | Best YouTube demo look |
| **+ [Tremor](https://tremor.so)** | KPI rings, bar lists, dashboards | (included above) | 9 | Resume/score ideas |
| **+ [React Flow](https://reactflow.dev)** | Agent pipeline / orchestration graph | +1–1.5 h | **9–10** | Agent Orchestra idea |
| **+ Mapbox GL JS** | Property map pins | +1.5–2 h | **10** | DealRoom idea only |

**Default for capstone MVP:** NiceGUI or Streamlit (good look, ~1h extra).  
**If you want “wow” video:** Next.js + shadcn (+3–4h).

---

## Complete comparison — pick · what it does · what you see · time · visual

**Total build** = ADK backend + UI + tests + README. All rows **meet minimum** capstone requirements.

| ID | Name | Track | **What it does** | **What user sees on screen** | UI | Time | Visual |
|---|---|---|---|---|---|---|---|
| **A** | Expense Triage | Business | User types an expense (amount, category, description). Triage agent parses it, scans for PII/fraud, checks policy. Low + safe → auto-approved. High or risky → sent to human review queue. | **Taipy pipeline board** with 4 columns (Submitted → Triage → Review → Approved). Expense cards slide across columns. Green “Approved” badge or amber “Needs review” banner. Red alert if credit card/PII detected. **Approve / Reject** buttons on review cards. | Taipy | **3h** | **8** |
| A′ | Expense Triage Premium | Business | Same as A — smarter layout and modal HITL flow. | **Polished web app**: input form at top, animated status cards, modal popup “Approve this ₹12,000 travel expense?” with agent reasoning bullets. Dark/light clean shadcn styling. | Next + shadcn | **5h** | **9** |
| **B** | Meeting → Actions | Business | User pastes meeting notes. Extractor agent pulls action items (owner, deadline). Prioritizer agent ranks by urgency and flags missing owners. | **Chainlit chat window** on left showing agent steps (“Extracting…”, “Prioritizing…”). Right panel renders a **markdown table** of tasks with priority chips (High/Med/Low) and owner tags. | Chainlit | **2.5h** | **7** |
| **C** | Study Quiz Coach | Good | User enters a topic. Generator agent creates 5 MCQs. User picks answers. Grader agent scores and explains wrong answers. Blocks unsafe topics. | **Gradio quiz UI**: topic text box → 5 question cards with radio buttons → **score banner** (e.g. 3/5). Wrong answers expand **red explanation cards**; correct ones show **green checkmarks**. | Gradio + CSS | **3.5h** | **8** |
| **D** | Errand Concierge | Concierge | User describes their day in plain English (“gym 7am, groceries, call mom”). Planner agent builds a timed schedule. Privacy guard strips phone/email from logs. | **NiceGUI vertical timeline**: hour slots down the left, **colored task chips** (fitness, errands, social) on a Saturday calendar strip. Grocery/errand list sidebar. “Session only — nothing saved” badge. | NiceGUI | **3h** | **8** |
| **E** | Grant Helper | Good | Student/club submits reimbursement (event, amount, receipt note). Policy agent checks caps and eligibility. Over cap → human approver must confirm. | Same **Taipy pipeline** as A but **education theme** (blue/green). Cards show “Club event”, “Amount”, “Policy OK?” tags. Review column for over-limit requests. | Taipy | **3h** | **8** |
| **F** | ExpenseFlow Command Center | Business | Same triage logic as A, plus running total of team spend and batch view of multiple expenses. | **Taipy Kanban** (like A) **plus Plotly bar chart** at top showing spend by category (Travel, Meals, Software). Cards stack in columns; chart updates as expenses approve. | Taipy + Plotly | **4h** | **8** |
| **G** | Agent Orchestra Live | Freestyle | User gives any task (“plan team offsite in Goa”). Three ADK agents run in sequence: **Scout** (research), **Planner** (schedule), **Critic** (security/eval check). Meta-demo of multi-agent orchestration. | **React Flow graph**: 3 connected nodes light up **idle → spinning → green** as each agent runs. Output panel below shows each agent’s result. Looks like **mission control / n8n-style** pipeline. | Next + shadcn + React Flow | **6h** | **10** |
| G′ | Agent Orchestra (budget) | Freestyle | Same 3-agent pipeline as G. | **3 agent cards** in a row with avatar icons and **progress bar** underneath. Status text: “Scout running…”, “Planner done ✓”. Less cinematic than G but clear. | NiceGUI | **4.5h** | **8** |
| **H** | ReceiptVision Triage | Business | User **uploads receipt photo**. Vision agent extracts merchant, date, amount. Policy agent checks limits. Over limit → human approval required. | **3-panel Gradio layout**: **left** = receipt image preview · **center** = extracted fields (editable) · **right** = approval gauge (green/yellow/red) + **Approve/Reject** button. | Gradio | **4h** | **8** |
| H′ | ReceiptVision Premium | Business | Same as H with drag-and-drop upload and cleaner extraction UX. | **Next.js dropzone** (“Drop receipt here”), animated field reveal, large approval status pill, agent reasoning accordion. | Next + shadcn | **6h** | **9** |
| **I** | StudyQuest XP Tutor | Good | Gamified quiz: topic → 5 questions → grade → earn XP and streaks. Wrong answers get tutor explanations. | **Streamlit dashboard**: **XP progress bar** at top, **streak flame icon**, **level badge**. Quiz cards below. On submit: bar animates, **+20 XP** popup, ring chart of score %. | Streamlit + Plotly | **4.5h** | **9** |
| **J** | EcoTrace Carbon Coach | Good | User describes weekly habits (driving, diet, energy). Calculator agent estimates CO₂ kg. Coach agent suggests lower-carbon swaps. | **Streamlit form** for habits → **before/after bar chart** (red vs green bars) showing kg CO₂ saved. Bulleted “Try this instead” tips from coach agent. | Streamlit + Plotly | **4h** | **8** |
| **K** | MealMind Weekly Board | Concierge | User sets family size, diet, budget. Planner agent fills 7 days of meals + compiles grocery list. No data stored after session. | **NiceGUI 7-column grid** (Mon–Sun) with **meal name cards** per slot (Breakfast/Lunch/Dinner). Scrollable **grocery list** on the right with checkboxes. | NiceGUI | **4h** | **8** |
| **L** | MatchPulse Resume Coach | Good / Freestyle | User pastes resume + job description. Matcher agent scores fit %. Gap agent lists missing skills and suggests improvements. | **Next.js dashboard**: large **circular match score** (e.g. 72%), **horizontal skill bars** (have vs need), gap list with “Add to resume” hints. Clean Tremor KPI styling. | Next + shadcn + Tremor | **6.5h** | **9** |
| **M** | HealthGuard Risk Meter | Good | User checks symptoms (not diagnosis). Triage agent assigns risk level and care guidance. Strong disclaimers; blocks medical advice beyond triage. | **Streamlit checklist** of symptoms → big **traffic-light gauge** (green/amber/red) + plain-English guidance card (“Monitor at home” / “Consider calling clinic”). Disclaimer banner at top. | Streamlit + Plotly | **4h** | **8** |
| **N** | GoalSprint Agent Board | Good | User enters a financial/life goal (e.g. “save ₹5L for car in 3 years”). Three agents (Planner, SIP hint, Insurance note) run and merge one plan. | **Chainlit** with **3 agent avatar cards** at top (🎯 Planner, 📈 SIP, 🛡 Insurance). Chat stream shows each agent contributing. Final **merged plan card** with monthly SIP amount and bullet tips. | Chainlit | **4.5h** | **8** |
| **O** | Mini DealRoom Scout | Business | User searches “2BHK under ₹80L in Whitefield”. Scout agent finds listings. Analyst agent scores buyer fit 0–100. | **Split screen**: **Mapbox map** with property pins on left · **listing cards** on right (photo placeholder, price, fit score badge). Click pin → card highlights. | Next + shadcn + Mapbox | **8h** | **10** |
| O′ | Mini DealRoom (no map) | Business | Same search + fit scoring without map. | **NiceGUI listing cards** in a grid with price, beds, **fit score badge** (0–100). Search bar at top. No map — faster to build. | NiceGUI | **5h** | **8** |

\* **O** needs free **Mapbox token** + Gemini.

### At-a-glance by visual score

| Visual | Ideas |
|---|---|
| **10/10** | G (React Flow orchestra), O (map + cards) |
| **9/10** | A′, H′, I, L |
| **8/10** | A, C, D, E, F, G′, H, J, K, M, N, O′ |
| **7/10** | B |

### At-a-glance by build time

| Time | Ideas |
|---|---|
| **≤3h** | A, D, E |
| **3–4.5h** | B, C, F, G′, H, J, K, M, N |
| **5–6.5h** | A′, G, H′, I, L, O′ |
| **8h** | O |

---

### ⭐ Idea A — Expense Triage Agent (RECOMMENDED)

| | |
|---|---|
| **Track** | Agents for Business |
| **What it does** | Parses expense text, checks policy & PII, auto-approves small safe claims, queues risky/high ones for human review. |
| **What user sees** | Taipy **4-column pipeline board**; cards move Submitted → Triage → Review → Approved; green/amber/red badges; Approve/Reject buttons. |
| **UI stack** | **Taipy** |
| **Total build time** | **~3 hours** |
| **Visual appeal** | **8/10** |
| **Meets minimum?** | **Yes** |
| **Premium variant (A′)** | Same logic → Next.js + shadcn modal HITL → **5h**, **9/10** |

---

### Idea B — Meeting Notes → Action Items Agent

| | |
|---|---|
| **Track** | Agents for Business |
| **One-liner** | Paste meeting notes → extract action items with owner, deadline, priority |
| **UI stack** | **Chainlit** — streaming agent steps + rendered task table |
| **Total build time** | **~2.5 hours** |
| **Visual appeal** | **7/10** |
| **Meets minimum?** | **Yes** |

**Architecture**
```
Notes text → Extractor Agent → structured JSON actions
          → Prioritizer Agent → ranks + flags missing owners
          → validate_output tool (schema check)
```

**Course concepts hit (4/5):** ADK, multi-agent, tools, eval — skill file added for compliance

**Demo:** Paste 1 sample standup note → get prioritized task list

**Trade-off:** Less flashy than expense agent; still valid for certificate.

---

### Idea C — 5-Minute Study Quiz Coach

| | |
|---|---|
| **Track** | Agents for Good (education) |
| **One-liner** | Topic in → 5 MCQs out → user answers → agent grades + explains mistakes |
| **UI stack** | **Gradio + custom CSS** — question cards, radio buttons, score header |
| **Total build time** | **~3.5 hours** |
| **Visual appeal** | **8/10** |
| **Meets minimum?** | **Yes** |

**Architecture**
```
Topic → Quiz Generator Agent → 5 questions (JSON)
     → Grader Agent → score + explanations
     → content_safety tool — block harmful topics
```

**Course concepts hit (5/5):** ADK, multi-agent, tools, skill (quiz format in SKILL.md), eval (fixed answer key tests)

**Demo:** “Photosynthesis” → quiz → answer 2 wrong → agent explains

---

### Idea D — Personal Errand Concierge (lightweight)

| | |
|---|---|
| **Track** | Concierge Agent |
| **One-liner** | “Plan my Saturday: gym, groceries, call mom” → structured schedule + reminders (in-memory) |
| **UI stack** | **NiceGUI** — vertical timeline + colored task chips |
| **Total build time** | **~3 hours** |
| **Visual appeal** | **8/10** |
| **Meets minimum?** | **Yes** |

**Architecture**
```
Natural language → Planner Agent → day plan JSON
                → Privacy guard — redact/strip phone & email from logs
                → Conflict checker tool
```

**Course concepts hit (4/5):** ADK, tools, security (privacy guard), skill — multi-agent is lightweight (planner + formatter)

**Trade-off:** Concierge track expects “personal data secure” — we satisfy with no persistence + redaction.

---

### Idea E — Grant / Reimbursement Helper (education nonprofit angle)

| | |
|---|---|
| **Track** | Agents for Good |
| **One-liner** | Student/club reimbursement request → policy check → HITL if over cap |
| **UI stack** | **Taipy** (Good-themed colors, same as Idea A) |
| **Total build time** | **~3 hours** |
| **Visual appeal** | **8/10** |
| **Meets minimum?** | **Yes** |

Same tech as Idea A, different problem statement for Good track. Pick only if you prefer Good over Business.

---

## E★ — University Scholarship Grants AI Agent (SELECTED / CUSTOM)

> **Status:** Approved concept — pending `plan.md` and build.  
> **Renamed from Idea E** · **Track:** Agents for Good · **LLM:** OpenAI via ADK LiteLLM (**no Gemini / no Google API keys**)

### Purpose

Remove human bias from scholarship grant allocation using a **rule-based, timestamp-fair AI agent system** — free to use for universities globally. Same eligibility rules applied to every applicant; waitlist ordered by **first application datetime** when budget is exhausted.

### What it does (system flow)

```
1. Student applies on dummy university scholarship website (public form)
2. MCP tool writes record → Airtable "Student Applications" (current year/semester)
3. Grants Agent Dashboard runs ADK agents + skills:
   a. Eligibility Agent — filter: marks ≥70% OR Grade A, family income < ₹5,00,000 INR
   b. Tier Agent — assign scholarship tier from grades/income rules
   c. Budget Agent — allocate until university budget cap ($1,000,000 USD)
   d. Waitlist Agent — overflow → "Waiting Students List" by entry datetime (FIFO)
4. Selected students → Airtable "Selected Sponsored Students List" (green)
5. Waitlisted students → Airtable "Waiting Students List" (orange)
6. If sponsored student no-shows interview → next waitlist student promoted (demo scenario)
```

### Scholarship tiers (deterministic — no LLM discretion on amounts)

| Tier | Condition | Award |
|---|---|---|
| **Tier B** | Grade B **or** marks ≥ 50%, income/tax doc threshold met | **$50,000 USD** |
| **Tier A** | Grade A **or** marks ≥ 70%, income/tax doc threshold met | **$150,000 USD** |

- **University budget cap:** **$1,000,000 USD** (system predefined)
- **Eligibility gate:** marks ≥ 70% **or** Grade A **and** family yearly income **< ₹500,000 INR**
- **Overflow:** when cumulative awards > budget, prioritize by **application entry datetime** (earliest first) → selected; rest → waitlist

> **Note:** Mark/grade proof + tax documents are **not uploaded in the form** — website states they are collected by **email before the online interview** (reduces MVP scope).

### Two user-facing interfaces

#### 1. Scholarship application website (dummy university portal)

Public form fields:
- Academic year & **semester name** (dropdown)
- **Application deadline** displayed on page (read-only banner for current cycle)
- Student name, email, phone, country
- Marks/grades (numeric out of total **or** letter grade)
- Family yearly income (INR textbox)
- Other required parameters for eligibility scoring
- Submit → MCP → Airtable

Footer/disclaimer on form:
- Proof of marks/grades and yearly tax filed document will be requested **via email** once student is shortlisted for **online interview** — not required at application time.

#### 2. Grants Scholarship Agent Dashboard (admin)

- Live table synced from Airtable
- **Agent skills** (`SKILL.md`) encode filter rules (grades, income, tiers, budget)
- Color status: **green** = Selected Sponsored · **orange** = Waiting List
- Run **Process applications** → agents batch-eligible, allocate budget, write both Airtable tables
- Summary cards: budget used / remaining, # selected, # waitlisted

### UI stack

| Interface | Library | Why |
|---|---|---|
| University application form | **NiceGUI** or **Streamlit** (public page) | Fast, clean form + deadline banner |
| Agent dashboard | **NiceGUI** or **Streamlit** (admin page) | Tables, green/orange badges, budget KPIs |

**Total build time (full):** **~6–7 hours**  
**Total build time (MVP cut):** **~3 hours** ← **recommended for deadline**  
**Visual appeal:** **8/10** full · **7/10** MVP (Streamlit)  
**Meets minimum capstone?** **Yes — exceeds** (both full and MVP)

### Course concepts (5/5 — no Gemini)

| Concept | Implementation |
|---|---|
| **ADK** | Python `google-adk` orchestration |
| **Multi-agent** | Eligibility → Tier → Budget → Waitlist agents |
| **MCP / tools** | MCP-style Airtable connector (create/read/update records) |
| **Agent skills** | `skills/SCHOLARSHIP_ALLOCATION.md` — rules, tiers, budget, FIFO |
| **Security / eval** | Deterministic rules (anti-bias); PII fields handled; `tests/eval.py` with fixed applicants |

**LLM:** OpenAI `gpt-4o-mini` via ADK `LiteLlm` — **no `GEMINI_API_KEY`**

### Keys required from you (not Google)

| Key | Purpose |
|---|---|
| `OPENAI_API_KEY` | ADK agent reasoning / orchestration |
| `AIRTABLE_API_KEY` | MCP student records |
| `AIRTABLE_BASE_ID` | Your base with 3 tables (see below) |

### Airtable tables (MVP)

| Table | Purpose | Status color |
|---|---|---|
| `Student Applications` | All form submissions + entry timestamp | — |
| `Selected Sponsored Students List` | Budget-approved grants | Green |
| `Waiting Students List` | FIFO waitlist when budget full | Orange |

### Minimum vs maximum fit

| Bar | This idea |
|---|---|
| **Minimum (certificate)** | ✓ Exceeds — Good track, ADK, MCP, skills, multi-agent, eval |
| **Maximum (swag)** | Strong story (bias removal + global education); needs polished video + architecture diagram |

### E★ MVP (3-hour cut) — what we build tonight

Full E★ above is **6–7h**. This is the **reduced MVP** that still earns the certificate.

| Full vision | 3-hour MVP (keep / cut) |
|---|---|
| Separate university website + dashboard | **CUT** → **one Streamlit app**, 2 tabs: `Apply` \| `Dashboard` |
| 3 Airtable tables | **CUT** → **1 table** with `Status`: Selected (green) / Waitlist (orange) / Ineligible |
| Real MCP server process | **CUT** → **Airtable REST tools** in ADK (same capstone “tools” concept) |
| 4 agents (Eligibility/Tier/Budget/Waitlist) | **CUT** → **2 agents**: Eligibility + Allocator |
| LLM decides who wins | **CUT** → **Python rules engine** decides; agents orchestrate + explain |
| No-show → promote waitlist | **CUT** → mentioned in README/write-up only |
| Phone + many extra fields | **CUT** → name, email, country, marks/grade, income, semester |
| Document upload / email flow | **KEEP** as static text on Apply tab only |
| Budget $1M + tiers $50k/$150k + FIFO datetime | **KEEP** (core demo) |
| OpenAI only (no Gemini) | **KEEP** |
| `SKILL.md` + `tests/eval.py` | **KEEP** (5 fixture students) |
| 10–15 seed applicants for waitlist demo | **KEEP** via `scripts/seed_demo.py` |

#### 3-hour MVP — what it does

1. **Apply tab** — dummy university form: semester dropdown, **deadline banner**, fields → save to Airtable (or local JSON if no Airtable key yet).
2. **Dashboard tab** — click **Run fair allocation** → eligibility rules → tier amounts → budget cap → FIFO waitlist → table with **green/orange** rows + budget used/remaining bar.
3. **Bias story** — every student judged by same numeric rules + timestamp order; no manual picking.

#### 3-hour MVP — what user sees

| Tab | On screen |
|---|---|
| **Apply** | University header, “Deadline: …”, semester, form fields, note “documents via email before interview” |
| **Dashboard** | KPI: budget left · table: Name, Tier, Award, Status (green/orange) · **Run allocation** button |

#### 3-hour MVP — scores

| Metric | Value |
|---|---|
| **Build time** | **~3 hours** |
| **Visual appeal** | **7/10** (Streamlit + color status — good enough for 5-min video) |
| **Meets minimum?** | **Yes** — ADK, 2 agents, tools, SKILL.md, eval, Good track |
| **Keys needed** | `OPENAI_API_KEY` + optional `AIRTABLE_*` (JSON fallback if Airtable not ready in hour 1) |

#### Eligibility rules (MVP — tier conflict fixed)

```
ELIGIBLE:  income < ₹500,000 AND marks ≥ 50% (or Grade B+)
TIER A:    marks ≥ 70% (or Grade A)  → $150,000
TIER B:    marks 50–69% (or Grade B)  → $50,000
BUDGET:    $1,000,000 USD cap, FIFO by application timestamp
```

#### Build order (3h)

| Min | Task |
|---|---|
| 0–40 | Python `allocate.py` rules + unit tests |
| 40–80 | ADK 2 agents + Airtable/JSON tools + OpenAI LiteLLM |
| 80–130 | Streamlit Apply + Dashboard tabs |
| 130–160 | Seed script, SKILL.md, README, `.env.example` |
| 160–180 | Smoke test 3 scenarios for your video script |

---

> See **Complete comparison** table at top of this file for all ideas with *what it does* and *what user sees*.

---

## What I will build (stack)

```
vibecert/
├── agent/           # ADK root + sub-agents (Python)
├── tools/           # policy, parse, approve, guard
├── skills/SKILL.md
├── tests/eval.py
├── ui/              # Taipy | NiceGUI | Streamlit | Chainlit | or web/
├── demo.py          # launch UI entrypoint
├── README.md
├── .env.example
└── submission/      # writeup draft + video script
```

If **Next.js** variant: `web/` subfolder with shadcn components calling FastAPI/ADK backend.

---

## What I need from YOU (before / during build)

| Item | Required? | Where to get | When |
|---|---|---|---|
| **Gemini API key** | **Recommended** (free tier, course-native) | [AI Studio](https://aistudio.google.com/app/apikey) | Default build |
| **OpenAI API key** | **Yes — supported** via ADK + LiteLLM | [platform.openai.com](https://platform.openai.com/api-keys) | If you prefer GPT-4o / already have key |
| OpenAI **without** ADK | **No** — fails minimum (must use ADK) | — | — |
| **Kaggle account** + join capstone | **Yes** | [Capstone page](https://www.kaggle.com/competitions/vibecoding-agents-capstone-project) | Before submit |
| **GitHub** (public repo) | **Yes** | Your account — I push code, you create repo or give me remote | After build |
| **YouTube** | **Yes** | Upload ≤5 min screen recording | After demo works |
| Google Cloud / Antigravity | No | — | Skip |
| OpenAI / other API keys | No | Gemini only | — |
| **Mapbox token** | Only Idea O | [mapbox.com](https://account.mapbox.com/) free tier | If picking O |

You will paste into `.env` (one or the other — or both):

```
# Option A — course default (free tier)
GEMINI_API_KEY=your_key_here

# Option B — OpenAI via ADK LiteLLM (if you prefer)
OPENAI_API_KEY=your_key_here
LLM_MODEL=openai/gpt-4o-mini   # or gpt-4o for vision (idea H)
```

---

## After you pick an idea

## After you pick an idea

Reply with e.g. **"Go with Idea A"**, **"G premium UI"**, or **"A′ Next.js"**.

I will create **`plan.md`** with build steps, UI wireframe, demo script, write-up outline, and submission checklist.

**I will not start coding until you approve `plan.md`.**

---

## My recommendation

**Pick Idea A with Taipy UI** — **3h total**, **visual 8/10**, Business track, all 5 course concepts.

If you have **6 hours** and want the best video: **Idea G** (Next.js + shadcn + React Flow) — **visual 10/10**.

---

## Part 2 — Idea details (UI already in master table above)

### Idea F — ExpenseFlow Command Center

| Field | Detail |
|---|---|
| **UI** | **Taipy** Kanban columns + **Plotly** monthly spend chart |
| **Total build** | **~4 h** · **Visual 8/10** · **Yes** |

Idea A upgraded: Gradio dashboard with **Kanban columns** (Submitted → Triage → Human Review → Approved/Rejected), color-coded cards, amount badges, PII warning banners. Same ADK multi-agent backend.

**Extra keys:** Gemini only.

---

### Idea G — Agent Orchestra Live ⭐ best “wow”

| Field | Detail |
|---|---|
| **UI (premium)** | **Next.js + shadcn/ui + React Flow** — animated agent graph |
| **Total build** | **~6 h** · **Visual 10/10** · **Yes** |
| **UI (budget)** | **NiceGUI** agent cards + progress — **4.5 h** · **Visual 8/10** |

Meta-demo: you pick a task (e.g. “plan a team offsite”), and a **live board** lights up as 3 ADK agents run in sequence — Scout (research), Planner (schedule), Critic (security/eval). Each agent card shows status: idle → running → done + output snippet. Looks like a mission control room.

**Why judges like it:** Pure showcase of multi-agent + tools + eval in one cinematic UI.

**Extra keys:** Gemini only.

---

### Idea H — ReceiptVision Triage

| Field | Detail |
|---|---|
| **UI** | **Gradio** 3-column split (image \| JSON fields \| approval gauge) |
| **Total build** | **~4 h** · **Visual 8/10** · **Yes** |
| **Premium (H′)** | Next.js + shadcn dropzone → **6 h** · **Visual 9/10** |

Upload a **receipt image** → Gemini vision extracts merchant/amount/date → Policy Agent checks rules → HITL panel if over limit. Side-by-side: image | extracted fields | approval gauge.

**Concepts:** ADK, multi-agent, tools, vision tool, HITL, eval on sample receipts.

**Extra keys:** Gemini only (vision included).

---

### Idea I — StudyQuest XP Tutor

| Field | Detail |
|---|---|
| **UI** | **Streamlit + Plotly** — XP bar, streak, level ring, answer feedback |
| **Total build** | **~4.5 h** · **Visual 9/10** · **Yes** |

Gamified quiz: **XP bar**, streak counter, level badge, progress ring. Quiz Generator + Grader agents. Wrong answers show explanation cards with green/red feedback.

**Extra keys:** Gemini only.

---

### Idea J — EcoTrace Carbon Coach

| Field | Detail |
|---|---|
| **UI** | **Streamlit + Plotly** — before/after CO₂ bar chart |
| **Total build** | **~4 h** · **Visual 8/10** · **Yes** |

Describe a week of habits (“drove 50km, 3 beef meals, AC all day”) → Calculator Agent estimates CO₂ → Coach Agent suggests swaps → **before/after bar chart** (Plotly in Gradio).

**Extra keys:** Gemini only.

---

### Idea K — MealMind Weekly Board

| Field | Detail |
|---|---|
| **UI** | **NiceGUI** — 7-day meal grid + grocery sidebar |
| **Total build** | **~4 h** · **Visual 8/10** · **Yes** |

“Family of 4, vegetarian, budget ₹500/day” → Planner Agent fills a **7-day grid** with meals + grocery list. Privacy: no account storage, session-only.

**Extra keys:** Gemini only.

---

### Idea L — MatchPulse Resume Coach

| Field | Detail |
|---|---|
| **UI** | **Next.js + shadcn/ui + Tremor** — radial match % + skill gap bars |
| **Total build** | **~6.5 h** · **Visual 9/10** · **Yes** |

Paste resume + job description → Matcher Agent scores fit → Gap Agent lists missing skills → **radial match score + horizontal skill bars**. Fresh ADK build (not a fork of your `resumeai` Next app — faster to ship clean in `vibecert/`).

**Extra keys:** Gemini only.

---

### Idea M — HealthGuard Risk Meter

| Field | Detail |
|---|---|
| **UI** | **Streamlit + Plotly indicator** — red/amber/green gauge |
| **Total build** | **~4 h** · **Visual 8/10** · **Yes** |

Symptom checklist (not diagnosis!) → Triage Agent → **traffic-light risk meter** + “seek care / self-care / monitor” with strong disclaimers. Safety guard blocks medical advice beyond triage.

**Extra keys:** Gemini only.

---

### Idea N — GoalSprint Agent Board

| Field | Detail |
|---|---|
| **UI** | **Chainlit** — 3 agent persona cards + merged plan output |
| **Total build** | **~4.5 h** · **Visual 8/10** · **Yes** |

Inspired by your `lakshya-coach` concept but **minimal ADK version**: goal input → parallel agent cards (Planner, SIP hint, Insurance note) merge into one plan card. Avatar icons per agent.

**Extra keys:** Gemini only (no Aurora/Airtable).

---

### Idea O — Mini DealRoom Scout

| Field | Detail |
|---|---|
| **UI (full)** | **Next.js + shadcn + Mapbox GL** — map pins + listing cards |
| **Total build** | **~8 h** · **Visual 10/10** · **Yes** (needs Mapbox token) |
| **Budget (O′)** | **NiceGUI** listing cards only → **5 h** · **Visual 8/10** |

Strip-down ADK version of your `dealroom-graph`: Scout + Analyst agents, **embedded map**, listing cards, fit score 0–100. Highest polish, highest setup cost.

**Extra keys:** Gemini + **Mapbox** *or* skip map and use listing cards only (~5h, visual 8/10).

---

## Quick pick guide

| Priority | Pick | What it does (1 line) | What user sees | Time | Visual |
|---|---|---|---|---|---|
| **Recommended** | **A** | Auto-triage expenses with HITL | Kanban pipeline + approve buttons | 3h | 8 |
| Fastest | **B** | Notes → ranked action items | Chat + task table | 2.5h | 7 |
| Best wow | **G** | 3 agents run a task live | Animated agent flow graph | 6h | 10 |
| Best Good + fun | **I** | Gamified quiz with XP | XP bar, streak, quiz cards | 4.5h | 9 |
| Receipt photo | **H** | Scan receipt → approve/deny | Image + fields + gauge | 4h | 8 |
| Max polish | **O** | Property search + fit score | Map pins + listing cards | 8h | 10 |

