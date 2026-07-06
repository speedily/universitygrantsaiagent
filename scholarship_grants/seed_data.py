"""Demo seed data — global applicants with local-currency incomes."""

from scholarship_grants.models import Application

SEED: list[Application] = [
    Application(name="Ananya Sharma", email="ananya@uni.in", country="India", semester="Fall 2026", marks_pct=88, family_income_local=850000, currency_code="INR", applied_at="2026-07-01T08:00:00+00:00", grade="A"),
    Application(name="Rahul Mehta", email="rahul@uni.in", country="India", semester="Fall 2026", marks_pct=91, family_income_local=720000, currency_code="INR", applied_at="2026-07-01T09:00:00+00:00", grade="A"),
    Application(name="Priya Nair", email="priya@uni.in", country="India", semester="Fall 2026", marks_pct=85, family_income_local=680000, currency_code="INR", applied_at="2026-07-01T10:00:00+00:00", grade="A"),
    Application(name="James Okonkwo", email="james@uni.ng", country="Nigeria", semester="Fall 2026", marks_pct=78, family_income_local=14500000, currency_code="NGN", applied_at="2026-07-01T11:00:00+00:00", grade="A"),
    Application(name="Maria Silva", email="maria@uni.br", country="Brazil", semester="Fall 2026", marks_pct=82, family_income_local=58000, currency_code="BRL", applied_at="2026-07-01T12:00:00+00:00", grade="A"),
    Application(name="Chen Wei", email="chen@uni.cn", country="China", semester="Fall 2026", marks_pct=90, family_income_local=78000, currency_code="CNY", applied_at="2026-07-01T13:00:00+00:00", grade="A"),
    Application(name="Fatima Hassan", email="fatima@uni.eg", country="Egypt", semester="Fall 2026", marks_pct=86, family_income_local=420000, currency_code="EGP", applied_at="2026-07-01T14:00:00+00:00", grade="A"),
    Application(name="Liam O'Brien", email="liam@uni.ie", country="Ireland", semester="Fall 2026", marks_pct=58, family_income_local=9500, currency_code="EUR", applied_at="2026-07-01T15:00:00+00:00", grade="B"),
    Application(name="Sofia Rossi", email="sofia@uni.it", country="Italy", semester="Fall 2026", marks_pct=92, family_income_local=9800, currency_code="EUR", applied_at="2026-07-01T16:00:00+00:00", grade="A"),
    Application(name="Kenji Tanaka", email="kenji@uni.jp", country="Japan", semester="Fall 2026", marks_pct=89, family_income_local=1450000, currency_code="JPY", applied_at="2026-07-01T17:00:00+00:00", grade="A"),
    Application(name="Aisha Khan", email="aisha@uni.pk", country="Pakistan", semester="Fall 2026", marks_pct=87, family_income_local=2800000, currency_code="PKR", applied_at="2026-07-01T18:00:00+00:00", grade="A"),
    Application(name="Tom Rich", email="tom@rich.com", country="USA", semester="Fall 2026", marks_pct=95, family_income_local=95000, currency_code="USD", applied_at="2026-07-01T19:00:00+00:00", grade="A"),
    Application(name="Elena Popov", email="elena@uni.ro", country="Romania", semester="Fall 2026", marks_pct=55, family_income_local=42000, currency_code="RON", applied_at="2026-07-01T20:00:00+00:00", grade="B"),
    Application(name="Carlos Mendez", email="carlos@uni.mx", country="Mexico", semester="Fall 2026", marks_pct=76, family_income_local=185000, currency_code="MXN", applied_at="2026-07-01T21:00:00+00:00", grade="A"),
    Application(name="Grace Wanjiru", email="grace@uni.ke", country="Kenya", semester="Fall 2026", marks_pct=84, family_income_local=1350000, currency_code="KES", applied_at="2026-07-01T22:00:00+00:00", grade="A"),
    Application(name="Minh Nguyen", email="minh@uni.vn", country="Vietnam", semester="Fall 2026", marks_pct=79, family_income_local=280000000, currency_code="VND", applied_at="2026-07-01T23:00:00+00:00", grade="A"),
    Application(name="Thabo Molefe", email="thabo@uni.za", country="South Africa", semester="Fall 2026", marks_pct=73, family_income_local=195000, currency_code="ZAR", applied_at="2026-07-02T08:00:00+00:00", grade="A"),
    Application(name="Isabella Santos", email="isa@uni.ph", country="Philippines", semester="Fall 2026", marks_pct=81, family_income_local=620000, currency_code="PHP", applied_at="2026-07-02T09:00:00+00:00", grade="A"),
    Application(name="Yuki Sato", email="yuki@uni.jp", country="Japan", semester="Fall 2026", marks_pct=88, family_income_local=1580000, currency_code="JPY", applied_at="2026-07-02T10:00:00+00:00", grade="A"),
    Application(name="Oliver Wright", email="oliver@uni.uk", country="United Kingdom", semester="Fall 2026", marks_pct=90, family_income_local=9200, currency_code="GBP", applied_at="2026-07-02T11:00:00+00:00", grade="A"),
    Application(name="Victoria Chen", email="victoria@uni.ca", country="Canada", semester="Fall 2026", marks_pct=77, family_income_local=15000, currency_code="CAD", applied_at="2026-07-02T12:00:00+00:00", grade="A"),
    Application(name="Amara Diallo", email="amara@uni.ng", country="Nigeria", semester="Fall 2026", marks_pct=92, family_income_local=17000000, currency_code="NGN", applied_at="2026-07-02T13:00:00+00:00", grade="A"),
    Application(name="Hans Mueller", email="hans@uni.de", country="Germany", semester="Fall 2026", marks_pct=65, family_income_local=9500, currency_code="EUR", applied_at="2026-07-02T14:00:00+00:00", grade="B"),
    Application(name="Zara Al-Farsi", email="zara@rich.ae", country="UAE", semester="Fall 2026", marks_pct=94, family_income_local=55000, currency_code="USD", applied_at="2026-07-02T15:00:00+00:00", grade="A"),
]
