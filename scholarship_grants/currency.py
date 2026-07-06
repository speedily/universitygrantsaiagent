"""Static FX rates to USD for eligibility (demo / MVP — not live trading rates)."""

from __future__ import annotations

# 1 unit of local currency → USD
TO_USD: dict[str, float] = {
    "USD": 1.0,
    "INR": 0.012,
    "NGN": 0.00063,
    "BRL": 0.18,
    "CNY": 0.138,
    "EGP": 0.021,
    "EUR": 1.08,
    "JPY": 0.0067,
    "PKR": 0.0036,
    "RON": 0.22,
    "GBP": 1.27,
    "MXN": 0.058,
    "KES": 0.0077,
    "VND": 0.000039,
    "ZAR": 0.055,
    "PHP": 0.017,
    "IDR": 0.000063,
    "TRY": 0.029,
    "KRW": 0.00072,
    "CAD": 0.73,
    "AUD": 0.65,
}

COUNTRY_CURRENCY: dict[str, str] = {
    "India": "INR",
    "Nigeria": "NGN",
    "Brazil": "BRL",
    "China": "CNY",
    "Egypt": "EGP",
    "Ireland": "EUR",
    "Italy": "EUR",
    "Japan": "JPY",
    "Pakistan": "PKR",
    "Romania": "RON",
    "USA": "USD",
    "United States": "USD",
    "Mexico": "MXN",
    "Kenya": "KES",
    "Vietnam": "VND",
    "South Africa": "ZAR",
    "Philippines": "PHP",
    "Indonesia": "IDR",
    "Turkey": "TRY",
    "South Korea": "KRW",
    "Canada": "CAD",
    "Australia": "AUD",
    "United Kingdom": "GBP",
    "Germany": "EUR",
    "France": "EUR",
    "Spain": "EUR",
}


def currency_for_country(country: str) -> str:
    key = country.strip()
    if key in COUNTRY_CURRENCY:
        return COUNTRY_CURRENCY[key]
    for name, code in COUNTRY_CURRENCY.items():
        if name.lower() == key.lower():
            return code
    return "USD"


def to_usd(amount_local: float, currency_code: str) -> float:
    code = (currency_code or "USD").strip().upper()
    rate = TO_USD.get(code, 1.0)
    return round(float(amount_local) * rate, 2)


def format_local_income(amount: float, currency_code: str) -> str:
    code = (currency_code or "USD").upper()
    symbols = {"USD": "$", "INR": "₹", "EUR": "€", "GBP": "£", "JPY": "¥", "NGN": "₦", "BRL": "R$"}
    sym = symbols.get(code, code + " ")
    if code in {"JPY", "VND", "KRW", "IDR"}:
        return f"{sym}{amount:,.0f}"
    return f"{sym}{amount:,.2f}"
