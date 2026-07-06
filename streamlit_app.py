"""Streamlit local demo — Apply + Dashboard tabs."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import streamlit as st

from agents.runner import agent_explain_allocation, run_allocation_pipeline
from scholarship_grants.config import (
    ACADEMIC_YEAR,
    APPLICATION_DEADLINE,
    BUDGET_USD,
    CURRENT_SEMESTER,
    MAX_INCOME_USD,
)
from scholarship_grants.currency import COUNTRY_CURRENCY, TO_USD, currency_for_country
from scholarship_grants.interview import (
    INTERVIEW_OUTCOMES,
    REJECTION_REASONS,
    apply_interview_outcome,
)
from scholarship_grants.models import Application, format_applied_at, server_timezone_label
from scholarship_grants.storage import add_application, load_applications, replace_all

st.set_page_config(
    page_title="University Grants AI Agent",
    page_icon="🎓",
    layout="wide",
)

st.title("University Grants AI Agent")
st.caption("Bias-free grant allocation · Free for universities worldwide · ADK + OpenAI")

tab_apply, tab_dash = st.tabs(["Scholarship Application", "Grants Agent Dashboard"])

with tab_apply:
    st.warning(f"Application deadline: **{APPLICATION_DEADLINE}** · {ACADEMIC_YEAR} · **{CURRENT_SEMESTER}**")
    st.info(
        "Proof of marks/grades and yearly tax filed documents will be requested **by email** "
        "once you are shortlisted for an **online interview** — not required on this form."
    )
    countries = sorted(COUNTRY_CURRENCY.keys())
    with st.form("apply_form"):
        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input("Full name *")
            email = st.text_input("Email *")
            phone = st.text_input("Phone")
            country = st.selectbox("Country *", countries, index=countries.index("India"))
        with c2:
            semester = st.selectbox("Semester", [CURRENT_SEMESTER, "Spring 2027", "Fall 2025"])
            marks_pct = st.number_input("Marks (%) *", min_value=0.0, max_value=100.0, value=72.0)
            grade = st.selectbox("Letter grade (optional)", ["", "A", "B", "C"])
            default_currency = currency_for_country(country)
            currency = st.selectbox("Income currency", sorted(TO_USD.keys()), index=sorted(TO_USD.keys()).index(default_currency))
            income = st.number_input(f"Family yearly income ({currency}) *", min_value=0.0, value=850000.0 if currency == "INR" else 10000.0, step=1000.0)
        submitted = st.form_submit_button("Submit application")
        if submitted:
            if not name or not email or not country:
                st.error("Name, email, and country are required.")
            else:
                app = Application(
                    name=name,
                    email=email,
                    phone=phone,
                    country=country,
                    semester=semester,
                    academic_year=ACADEMIC_YEAR,
                    marks_pct=marks_pct,
                    family_income_local=income,
                    currency_code=currency,
                    grade=grade,
                )
                add_application(app)
                applied_date, applied_time = format_applied_at(app.applied_at)
                st.success(
                    f"Application submitted for {name} on **{applied_date}** at **{applied_time}** (server time). "
                    f"Income ≈ ${app.family_income_usd:,.2f} USD equivalent."
                )

with tab_dash:
    st.subheader("Grants Scholarship Agent Dashboard")
    st.write(
        f"Budget cap: **${BUDGET_USD:,.0f} USD** · "
        f"Eligibility: income **< ${MAX_INCOME_USD:,.0f} USD/year** (converted from local currency) · marks ≥ 50%"
    )
    st.caption(
        f"Table sorted by **form submission date & time** (FIFO, **{server_timezone_label()}** server time). "
        "Record **online interview** outcomes below for selected students."
    )
    if st.button("Run fair allocation (ADK pipeline)", type="primary"):
        result = run_allocation_pipeline()
        explanation = agent_explain_allocation(result["summary"])
        st.session_state["last_summary"] = result["summary"]
        st.session_state["last_explanation"] = explanation

    if "last_summary" in st.session_state:
        s = st.session_state["last_summary"]
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Selected", s["selected_count"])
        m2.metric("Waitlist", s["waitlist_count"])
        m3.metric("Spent", f"${s['spent_usd']:,.0f}")
        m4.metric("Remaining", f"${s['remaining_usd']:,.0f}")
        st.progress(min(1.0, s["spent_usd"] / s["budget_usd"]))
        st.write(st.session_state.get("last_explanation", ""))

    apps = sorted(load_applications(), key=lambda a: a.applied_at)
    if not apps:
        st.info("No applications yet. Use the Application tab or run `python scripts/seed_demo.py`.")
    else:
        rows = []
        for a in apps:
            color = {"selected": "🟢", "waitlist": "🟠", "ineligible": "⚪", "no_show": "🟤", "interview_rejected": "🔴", "interview_confirmed": "🟢"}.get(a.status, "⚫")
            applied_date, applied_time = format_applied_at(a.applied_at)
            interview_label = INTERVIEW_OUTCOMES.get(a.interview_outcome, "—") if a.interview_outcome else "—"
            rows.append(
                {
                    "": color,
                    "Name": a.name,
                    "Country": a.country,
                    "Applied date": applied_date,
                    "Applied time": applied_time,
                    "Marks %": a.marks_pct,
                    "Income (local)": f"{a.family_income_local:,.0f} {a.currency_code}",
                    "Income (USD)": f"${a.family_income_usd:,.2f}",
                    "Tier": a.tier,
                    "Award USD": f"${a.award_usd:,.0f}" if a.award_usd else "—",
                    "Status": a.status,
                    "Interview": interview_label,
                    "Rejection reason": a.rejection_reason or "—",
                }
            )
        st.dataframe(rows, use_container_width=True, hide_index=True)

        interview_students = [
            a for a in apps if a.status in {"selected", "interview_confirmed", "no_show", "interview_rejected"}
        ]
        if interview_students:
            st.subheader("Record online interview")
            for a in interview_students:
                with st.expander(f"{a.name} — {a.status}", expanded=False):
                    outcome = st.selectbox(
                        "Interview outcome",
                        options=list(INTERVIEW_OUTCOMES.keys()),
                        format_func=lambda k: INTERVIEW_OUTCOMES[k],
                        index=list(INTERVIEW_OUTCOMES.keys()).index(a.interview_outcome or ""),
                        key=f"outcome_{a.id}",
                    )
                    reason_code = ""
                    other = ""
                    if outcome == "attended_rejected":
                        reason_code = st.selectbox(
                            "Rejection reason",
                            options=list(REJECTION_REASONS.keys()),
                            format_func=lambda k: REJECTION_REASONS[k],
                            index=max(0, list(REJECTION_REASONS.keys()).index(a.rejection_reason_code or "")),
                            key=f"reason_{a.id}",
                        )
                        if reason_code == "other":
                            other = st.text_input(
                                "Specify reason",
                                value=a.rejection_reason if a.rejection_reason_code == "other" else "",
                                key=f"other_{a.id}",
                            )
                    if st.button("Save interview", key=f"save_{a.id}"):
                        try:
                            updated, target, promoted = apply_interview_outcome(
                                apps, a.id, outcome, reason_code, other
                            )
                            replace_all(updated)
                            if promoted:
                                st.success(f"Saved. {promoted.name} promoted from waitlist.")
                            else:
                                st.success("Interview outcome saved.")
                            st.rerun()
                        except ValueError as exc:
                            st.error(str(exc))
