"""ADK multi-agent orchestration (OpenAI via LiteLLM — no Gemini)."""

from __future__ import annotations

import json
import os
from typing import Any

from scholarship_grants.allocate import allocate_applications
from scholarship_grants.config import OPENAI_API_KEY, OPENAI_MODEL
from scholarship_grants.models import Application
from scholarship_grants.storage import load_applications, replace_all


def run_allocation_pipeline() -> dict[str, Any]:
    """Deterministic allocation — agents wrap this for capstone ADK demo."""
    apps = load_applications()
    updated, summary = allocate_applications(apps)
    replace_all(updated)
    return {"summary": summary, "applications": [a.to_dict() for a in updated]}


def agent_explain_allocation(summary: dict[str, Any]) -> str:
    """Optional OpenAI explanation via ADK LiteLLM when key is set."""
    if not OPENAI_API_KEY:
        return (
            "Allocation complete using deterministic rules: income under $12,000 USD equivalent per year, "
            "marks at least 50 percent. "
            f"FIFO timestamp. Selected: {summary.get('selected_count', 0)}, "
            f"Waitlist: {summary.get('waitlist_count', 0)}."
        )
    try:
        from google.adk.agents import LlmAgent
        from google.adk.models.lite_llm import LiteLlm
        from google.adk.runners import InMemoryRunner
        from google.genai import types

        os.environ.setdefault("OPENAI_API_KEY", OPENAI_API_KEY)

        eligibility_agent = LlmAgent(
            model=LiteLlm(model=OPENAI_MODEL),
            name="eligibility_agent",
            instruction=(
                "You explain scholarship eligibility outcomes. Rules: family income under 12000 USD "
                "equivalent per year (converted from local currency), marks at least 50 percent. "
                "Be concise and mention bias-free deterministic rules."
            ),
        )
        allocator_agent = LlmAgent(
            model=LiteLlm(model=OPENAI_MODEL),
            name="allocator_agent",
            instruction=(
                "You explain budget allocation and FIFO waitlist when the 1000000 USD cap is reached. "
                "Be concise for university administrators."
            ),
        )

        prompt = (
            "Summarize this fair scholarship allocation run in 3 sentences for a university dean:\n"
            + json.dumps(summary, indent=2)
        )
        runner = InMemoryRunner(agent=allocator_agent, app_name="scholarship_grants")
        session = runner.session_service.create_session(
            app_name="scholarship_grants", user_id="admin"
        ).blocking_result()

        events = runner.run(
            user_id="admin",
            session_id=session.id,
            new_message=types.Content(
                role="user", parts=[types.Part(text=prompt)]
            ),
        )
        text_parts: list[str] = []
        for event in events:
            if event.content and event.content.parts:
                for part in event.content.parts:
                    if part.text:
                        text_parts.append(part.text)
        return " ".join(text_parts) or eligibility_agent.name
    except Exception as exc:
        return f"Allocation complete (agent explain unavailable: {exc})"
