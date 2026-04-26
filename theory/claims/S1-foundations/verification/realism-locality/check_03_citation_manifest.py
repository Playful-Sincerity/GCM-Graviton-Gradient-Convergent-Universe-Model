#!/usr/bin/env python3
"""
Check 03 — Citation manifest structural validation.

Claim: S1-RL-1.
Goal:  Verify that every citation in inputs.json has the required fields
       (id, author, year, title, venue, identifier_type, identifier,
       load_bearing_for) and that id values are unique. This is structural
       validation only — it does not attempt network resolution.

Expected result: all 6 citations pass schema validation; no duplicate ids.
Tool:            Python 3 (stdlib only).
"""

import json
import os
import sys
from datetime import datetime


HERE = os.path.dirname(os.path.abspath(__file__))
INPUTS_PATH = os.path.join(HERE, "inputs.json")

REQUIRED_FIELDS = [
    "id",
    "cited_text",
    "author",
    "year",
    "title",
    "venue",
    "identifier_type",
    "identifier",
    "load_bearing_for",
]


def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    print("# Check: 03 — Citation manifest structural validation")
    print("# Claim: S1-RL-1")
    print(f"# Run:   {now}")
    print(f"# Tool:  python3 {sys.version.split()[0]} (stdlib only)")
    print("# Script: verification/realism-locality/check_03_citation_manifest.py")
    print("# ----")
    print()

    with open(INPUTS_PATH, "r") as f:
        inputs = json.load(f)

    citations = inputs.get("citations", [])
    print(f"Found {len(citations)} citations in inputs.json.")
    print()

    errors = []
    ids_seen = set()

    for idx, c in enumerate(citations, start=1):
        print(f"Citation {idx}: id={c.get('id', '???')}")
        # Required fields
        for field in REQUIRED_FIELDS:
            if field not in c or c[field] in (None, "", []):
                err = f"  MISSING FIELD: {field}"
                print(err)
                errors.append(f"citation[{idx}] id={c.get('id')}: {err.strip()}")
        # Year sanity
        year = c.get("year")
        if isinstance(year, int) and not (1800 <= year <= 2100):
            err = f"  SUSPICIOUS YEAR: {year}"
            print(err)
            errors.append(f"citation[{idx}] id={c.get('id')}: year {year} out of range")
        # Author must be a list
        if not isinstance(c.get("author"), list):
            err = f"  AUTHOR FIELD NOT A LIST: {type(c.get('author')).__name__}"
            print(err)
            errors.append(f"citation[{idx}] id={c.get('id')}: {err.strip()}")
        # Identifier type
        id_type = c.get("identifier_type")
        if id_type not in ("DOI", "ISBN", "arXiv", "URL"):
            err = f"  UNUSUAL identifier_type: {id_type}"
            print(err)
            errors.append(f"citation[{idx}] id={c.get('id')}: identifier_type {id_type}")
        # Duplicate id
        cid = c.get("id")
        if cid in ids_seen:
            err = f"  DUPLICATE id: {cid}"
            print(err)
            errors.append(f"citation[{idx}]: {err.strip()}")
        else:
            ids_seen.add(cid)
        # Summary line
        print(f"  {c.get('author', ['?'])[0]} ({c.get('year', '?')}) — {c.get('title', '?')}")
        print(f"    {id_type}: {c.get('identifier', '?')}")
        print(f"    load-bearing for: {c.get('load_bearing_for', '?')[:80]}...")
        print()

    print(f"Unique ids:  {len(ids_seen)}")
    print(f"Errors:      {len(errors)}")
    if errors:
        status = "FAIL"
        print()
        print("Errors found:")
        for e in errors:
            print(f"  - {e}")
    else:
        status = "PASS"

    print()
    print(f"STATUS: {status}")


if __name__ == "__main__":
    main()
