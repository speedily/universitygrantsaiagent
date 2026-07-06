"""Demo seed data — global applicants with local-currency incomes."""

import uuid

from scholarship_grants.models import Application


def _seed_id(email: str) -> str:
    """Stable ID per email — survives server restarts and Airtable sync."""
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"scholarship-grants:{email}"))


_STUDENTS = [
    {"name": "Ananya Sharma", "email": "ananya@uni.in", "phone": "+91 98765 43210", "country": "India", "semester": "Fall 2026", "marks_pct": 88, "family_income_local": 850000, "currency_code": "INR", "applied_at": "2026-07-01T08:00:00+00:00"},
    {"name": "Rahul Mehta", "email": "rahul@uni.in", "phone": "+91 98123 45678", "country": "India", "semester": "Fall 2026", "marks_pct": 91, "family_income_local": 720000, "currency_code": "INR", "applied_at": "2026-07-01T09:00:00+00:00"},
    {"name": "Priya Nair", "email": "priya@uni.in", "phone": "+91 99887 76655", "country": "India", "semester": "Fall 2026", "marks_pct": 85, "family_income_local": 680000, "currency_code": "INR", "applied_at": "2026-07-01T10:00:00+00:00"},
    {"name": "James Okonkwo", "email": "james@uni.ng", "phone": "+234 803 456 7890", "country": "Nigeria", "semester": "Fall 2026", "marks_pct": 78, "family_income_local": 14500000, "currency_code": "NGN", "applied_at": "2026-07-01T11:00:00+00:00"},
    {"name": "Maria Silva", "email": "maria@uni.br", "phone": "+55 11 98765 4321", "country": "Brazil", "semester": "Fall 2026", "marks_pct": 82, "family_income_local": 58000, "currency_code": "BRL", "applied_at": "2026-07-01T12:00:00+00:00"},
    {"name": "Chen Wei", "email": "chen@uni.cn", "phone": "+86 138 0013 8000", "country": "China", "semester": "Fall 2026", "marks_pct": 90, "family_income_local": 78000, "currency_code": "CNY", "applied_at": "2026-07-01T13:00:00+00:00"},
    {"name": "Fatima Hassan", "email": "fatima@uni.eg", "phone": "+20 100 123 4567", "country": "Egypt", "semester": "Fall 2026", "marks_pct": 86, "family_income_local": 420000, "currency_code": "EGP", "applied_at": "2026-07-01T14:00:00+00:00"},
    {"name": "Liam O'Brien", "email": "liam@uni.ie", "phone": "+353 87 123 4567", "country": "Ireland", "semester": "Fall 2026", "marks_pct": 58, "family_income_local": 9500, "currency_code": "EUR", "applied_at": "2026-07-01T15:00:00+00:00"},
    {"name": "Sofia Rossi", "email": "sofia@uni.it", "phone": "+39 347 123 4567", "country": "Italy", "semester": "Fall 2026", "marks_pct": 92, "family_income_local": 9800, "currency_code": "EUR", "applied_at": "2026-07-01T16:00:00+00:00"},
    {"name": "Kenji Tanaka", "email": "kenji@uni.jp", "phone": "+81 90 1234 5678", "country": "Japan", "semester": "Fall 2026", "marks_pct": 89, "family_income_local": 1450000, "currency_code": "JPY", "applied_at": "2026-07-01T17:00:00+00:00"},
    {"name": "Aisha Khan", "email": "aisha@uni.pk", "phone": "+92 300 1234567", "country": "Pakistan", "semester": "Fall 2026", "marks_pct": 87, "family_income_local": 2800000, "currency_code": "PKR", "applied_at": "2026-07-01T18:00:00+00:00"},
    {"name": "Tom Rich", "email": "tom@rich.com", "phone": "+1 415 555 0101", "country": "USA", "semester": "Fall 2026", "marks_pct": 95, "family_income_local": 95000, "currency_code": "USD", "applied_at": "2026-07-01T19:00:00+00:00"},
    {"name": "Elena Popov", "email": "elena@uni.ro", "phone": "+40 722 123 456", "country": "Romania", "semester": "Fall 2026", "marks_pct": 55, "family_income_local": 42000, "currency_code": "RON", "applied_at": "2026-07-01T20:00:00+00:00"},
    {"name": "Carlos Mendez", "email": "carlos@uni.mx", "phone": "+52 55 1234 5678", "country": "Mexico", "semester": "Fall 2026", "marks_pct": 76, "family_income_local": 185000, "currency_code": "MXN", "applied_at": "2026-07-01T21:00:00+00:00"},
    {"name": "Grace Wanjiru", "email": "grace@uni.ke", "phone": "+254 712 345678", "country": "Kenya", "semester": "Fall 2026", "marks_pct": 84, "family_income_local": 1350000, "currency_code": "KES", "applied_at": "2026-07-01T22:00:00+00:00"},
    {"name": "Minh Nguyen", "email": "minh@uni.vn", "phone": "+84 912 345 678", "country": "Vietnam", "semester": "Fall 2026", "marks_pct": 79, "family_income_local": 280000000, "currency_code": "VND", "applied_at": "2026-07-01T23:00:00+00:00"},
    {"name": "Thabo Molefe", "email": "thabo@uni.za", "phone": "+27 82 123 4567", "country": "South Africa", "semester": "Fall 2026", "marks_pct": 73, "family_income_local": 195000, "currency_code": "ZAR", "applied_at": "2026-07-02T08:00:00+00:00"},
    {"name": "Isabella Santos", "email": "isa@uni.ph", "phone": "+63 917 123 4567", "country": "Philippines", "semester": "Fall 2026", "marks_pct": 81, "family_income_local": 620000, "currency_code": "PHP", "applied_at": "2026-07-02T09:00:00+00:00"},
    {"name": "Yuki Sato", "email": "yuki@uni.jp", "phone": "+81 80 9876 5432", "country": "Japan", "semester": "Fall 2026", "marks_pct": 88, "family_income_local": 1580000, "currency_code": "JPY", "applied_at": "2026-07-02T10:00:00+00:00"},
    {"name": "Oliver Wright", "email": "oliver@uni.uk", "phone": "+44 7700 900123", "country": "United Kingdom", "semester": "Fall 2026", "marks_pct": 90, "family_income_local": 9200, "currency_code": "GBP", "applied_at": "2026-07-02T11:00:00+00:00"},
    {"name": "Victoria Chen", "email": "victoria@uni.ca", "phone": "+1 604 555 0199", "country": "Canada", "semester": "Fall 2026", "marks_pct": 77, "family_income_local": 15000, "currency_code": "CAD", "applied_at": "2026-07-02T12:00:00+00:00"},
    {"name": "Amara Diallo", "email": "amara@uni.ng", "phone": "+234 701 234 5678", "country": "Nigeria", "semester": "Fall 2026", "marks_pct": 92, "family_income_local": 17000000, "currency_code": "NGN", "applied_at": "2026-07-02T13:00:00+00:00"},
    {"name": "Hans Mueller", "email": "hans@uni.de", "phone": "+49 151 23456789", "country": "Germany", "semester": "Fall 2026", "marks_pct": 65, "family_income_local": 9500, "currency_code": "EUR", "applied_at": "2026-07-02T14:00:00+00:00"},
    {"name": "Zara Al-Farsi", "email": "zara@rich.ae", "phone": "+971 50 123 4567", "country": "UAE", "semester": "Fall 2026", "marks_pct": 94, "family_income_local": 55000, "currency_code": "USD", "applied_at": "2026-07-02T15:00:00+00:00"},
]

SEED: list[Application] = [
    Application(id=_seed_id(row["email"]), **{k: v for k, v in row.items()})
    for row in _STUDENTS
]
