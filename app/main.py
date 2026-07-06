"""FastAPI application — Vercel + local server."""

from __future__ import annotations

from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, Response
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from agents.runner import agent_explain_allocation
from scholarship_grants.allocate import allocate_applications
from scholarship_grants.config import (
    ACADEMIC_YEAR,
    APPLICATION_DEADLINE,
    BUDGET_USD,
    CURRENT_SEMESTER,
    MAX_INCOME_USD,
)
from scholarship_grants.currency import COUNTRY_CURRENCY, TO_USD, currency_for_country
from scholarship_grants.export import applications_to_csv
from scholarship_grants.interview import (
    INTERVIEW_OUTCOMES,
    REJECTION_REASONS,
    apply_interview_outcome,
    interview_summary,
)
from scholarship_grants.models import Application, format_applied_at, server_timezone_label
from scholarship_grants.storage import add_application, load_applications, replace_all


class ApplyRequest(BaseModel):
    name: str
    email: str
    country: str
    semester: str = CURRENT_SEMESTER
    academic_year: str = ACADEMIC_YEAR
    marks_pct: float = Field(ge=0, le=100)
    family_income_local: float = Field(ge=0)
    currency_code: str = ""
    grade: str = ""
    phone: str = ""


class InterviewUpdateRequest(BaseModel):
    interview_outcome: str
    rejection_reason_code: str = ""
    rejection_other: str = ""


def create_app() -> FastAPI:
    app = FastAPI(
        title="University Grants AI Agent",
        description="Bias-free scholarship allocation for universities worldwide.",
        version="1.0.0",
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )

    static_dir = Path(__file__).resolve().parent / "static"
    if static_dir.exists():
        app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")

    @app.get("/")
    async def index():
        index_file = static_dir / "index.html"
        if index_file.exists():
            return FileResponse(index_file)
        return {"message": "University Grants AI Agent API", "docs": "/docs"}

    @app.get("/api/meta")
    async def meta():
        return {
            "project": "University Grants AI Agent",
            "slug": "universitygrantsaiagent",
            "purpose": "Remove bias from grant allocation using deterministic AI-orchestrated rules",
            "deadline": APPLICATION_DEADLINE,
            "semester": CURRENT_SEMESTER,
            "academic_year": ACADEMIC_YEAR,
            "budget_usd": BUDGET_USD,
            "max_income_usd": MAX_INCOME_USD,
            "country_currencies": COUNTRY_CURRENCY,
            "currencies": list(TO_USD.keys()),
            "interview_outcomes": INTERVIEW_OUTCOMES,
            "rejection_reasons": REJECTION_REASONS,
            "server_timezone": server_timezone_label(),
            "document_note": "Proof of marks and tax documents collected by email before online interview.",
        }

    @app.get("/api/applications")
    async def list_applications():
        apps = load_applications()
        apps.sort(key=lambda a: a.applied_at)
        return {"applications": [a.to_dict() for a in apps]}

    @app.post("/api/applications")
    async def submit_application(body: ApplyRequest):
        code = (body.currency_code or currency_for_country(body.country)).upper()
        app_record = Application(
            name=body.name.strip(),
            email=body.email.strip(),
            country=body.country.strip(),
            semester=body.semester,
            academic_year=body.academic_year,
            marks_pct=body.marks_pct,
            family_income_local=body.family_income_local,
            currency_code=code,
            grade=body.grade.strip().upper(),
            phone=body.phone.strip(),
            status="pending",
        )
        saved = add_application(app_record)
        return {"ok": True, "application": saved.to_dict()}

    @app.post("/api/allocate")
    async def run_allocation():
        apps = load_applications()
        if not apps:
            raise HTTPException(status_code=400, detail="No applications to allocate")
        updated, summary = allocate_applications(apps)
        replace_all(updated)
        updated.sort(key=lambda a: a.applied_at)
        explanation = agent_explain_allocation(summary)
        return {
            "ok": True,
            "summary": summary,
            "explanation": explanation,
            "applications": [a.to_dict() for a in updated],
        }

    @app.post("/api/seed")
    async def seed_demo():
        from scholarship_grants.seed_data import SEED

        replace_all(SEED)
        return {"ok": True, "count": len(SEED), "message": "Demo students loaded"}

    @app.patch("/api/applications/{app_id}/interview")
    async def record_interview(app_id: str, body: InterviewUpdateRequest):
        apps = load_applications()
        try:
            updated, target, promoted = apply_interview_outcome(
                apps,
                app_id,
                body.interview_outcome.strip(),
                body.rejection_reason_code.strip(),
                body.rejection_other.strip(),
            )
        except ValueError as exc:
            raise HTTPException(status_code=400, detail=str(exc)) from exc
        replace_all(updated)
        updated.sort(key=lambda a: a.applied_at)
        return {
            "ok": True,
            "application": target.to_dict(),
            "promoted": promoted.to_dict() if promoted else None,
            "interview_summary": interview_summary(updated),
            "applications": [a.to_dict() for a in updated],
        }

    @app.get("/api/export/csv")
    async def export_csv(list: str = "screening"):
        """Download student list as CSV. list=screening|final|all"""
        if list not in {"screening", "final", "all"}:
            raise HTTPException(status_code=400, detail="list must be screening, final, or all")
        apps = load_applications()
        csv_body = applications_to_csv(apps, list_type=list)
        filename = f"scholarship_{list}_{CURRENT_SEMESTER.replace(' ', '_')}.csv"
        return Response(
            content=csv_body,
            media_type="text/csv",
            headers={"Content-Disposition": f'attachment; filename="{filename}"'},
        )

    @app.get("/api/health")
    async def health():
        return {"status": "ok", "project": "universitygrantsaiagent"}

    return app
