"""ADK multi-agent orchestration (OpenAI via LiteLLM — no Gemini)."""

from __future__ import annotations

import asyncio
import json
import os
from concurrent.futures import ThreadPoolExecutor
from typing import Any

from scholarship_grants.allocate import allocate_applications
from scholarship_grants.config import OPENAI_API_KEY, OPENAI_MODEL
from scholarship_grants.storage import load_applications, replace_all, sync_to_airtable


def run_allocation_pipeline() -> dict[str, Any]:
    """Deterministic allocation — agents wrap this for capstone ADK demo."""
    apps = load_applications()
    updated, summary = allocate_applications(apps)
    replace_all(updated, sync_airtable=False)
    sync_to_airtable(updated)
    return {"summary": summary, "applications": [a.to_dict() for a in updated]}


async def _run_agent_async(agent: Any, prompt: str, user_id: str = "admin") -> str:
    from google.adk.runners import InMemoryRunner
    from google.genai import types

    os.environ.setdefault("OPENAI_API_KEY", OPENAI_API_KEY)
    runner = InMemoryRunner(agent=agent, app_name="scholarship_grants")
    session = await runner.session_service.create_session(
        app_name="scholarship_grants", user_id=user_id
    )
    events = runner.run(
        user_id=user_id,
        session_id=session.id,
        new_message=types.Content(role="user", parts=[types.Part(text=prompt)]),
    )
    text_parts: list[str] = []
    for event in events:
        if event.content and event.content.parts:
            for part in event.content.parts:
                if part.text:
                    text_parts.append(part.text)
    return " ".join(text_parts).strip()


def _run_agent(agent: Any, prompt: str, user_id: str = "admin") -> str:
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        return asyncio.run(_run_agent_async(agent, prompt, user_id))
    with ThreadPoolExecutor(max_workers=1) as pool:
        return pool.submit(asyncio.run, _run_agent_async(agent, prompt, user_id)).result()


def agent_explain_allocation(summary: dict[str, Any]) -> str:
    """OpenAI explanation via ADK LiteLLM (eligibility + allocator agents)."""
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

        eligibility_agent = LlmAgent(
            model=LiteLlm(model=OPENAI_MODEL),
            name="eligibility_agent",
            instruction=(
                "You explain scholarship eligibility outcomes. Rules: family income under 12000 USD "
                "equivalent per year (converted from local currency), marks at least 50 percent. "
                "Be concise (2 sentences) and mention bias-free deterministic rules."
            ),
        )
        allocator_agent = LlmAgent(
            model=LiteLlm(model=OPENAI_MODEL),
            name="allocator_agent",
            instruction=(
                "You explain budget allocation and FIFO waitlist when the 1000000 USD cap is reached. "
                "Be concise (2 sentences) for university administrators."
            ),
        )
        payload = json.dumps(summary, indent=2)
        eligibility_text = _run_agent(
            eligibility_agent,
            f"Explain eligibility results for this allocation run:\n{payload}",
        )
        allocator_text = _run_agent(
            allocator_agent,
            f"Explain budget and waitlist results for this allocation run:\n{payload}",
        )
        return f"Eligibility agent: {eligibility_text} Allocator agent: {allocator_text}"
    except ImportError:
        return (
            f"Allocation complete. Selected: {summary.get('selected_count', 0)}, "
            f"Waitlist: {summary.get('waitlist_count', 0)}. "
            "(ADK package not installed on this server — deterministic rules applied.)"
        )
    except Exception as exc:
        return f"Allocation complete (agent explain unavailable: {exc})"
