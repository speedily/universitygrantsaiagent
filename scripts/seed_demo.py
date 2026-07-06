#!/usr/bin/env python3
"""Seed demo applications for waitlist / budget demo."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scholarship_grants.seed_data import SEED
from scholarship_grants.storage import replace_all

if __name__ == "__main__":
    replace_all(SEED)
    print(f"Seeded {len(SEED)} applications → {ROOT / 'data' / 'applications.json'}")
