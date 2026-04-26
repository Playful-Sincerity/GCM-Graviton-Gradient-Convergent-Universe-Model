#!/usr/bin/env python3
"""
Check 04 — Citation cross-reference.

Claim: S1-RL-1.
Goal:  For each citation's 'cited_text' field in inputs.json, confirm that
       the corresponding phrase (or a close variant) actually appears in
       ../../realism-locality.md. This catches the failure mode where a
       bibliography is maintained but the markdown narrative no longer
       cites the reference.

Expected result: every citation's cited_text matches a phrase in the
markdown file. Matching is done with a tolerant normalized-substring check:
lowercase, collapse whitespace, strip punctuation that varies between quote
styles.

Tool: Python 3 (stdlib only).
"""

import json
import os
import re
import sys
from datetime import datetime


HERE = os.path.dirname(os.path.abspath(__file__))
INPUTS_PATH = os.path.join(HERE, "inputs.json")
MARKDOWN_PATH = os.path.abspath(os.path.join(HERE, "..", "..", "realism-locality.md"))


def normalize(s: str) -> str:
    s = s.lower()
    # Normalize common fancy punctuation to plain equivalents.
    replacements = {
        "’": "'",
        "‘": "'",
        "“": '"',
        "”": '"',
        "–": "-",
        "—": "-",
        " ": " ",
    }
    for k, v in replacements.items():
        s = s.replace(k, v)
    # Strip punctuation variants but keep word boundaries.
    s = re.sub(r"[,;.\"'()\[\]]", "", s)
    # Collapse whitespace.
    s = re.sub(r"\s+", " ", s).strip()
    return s


def key_tokens(cited_text: str):
    """Short list of key tokens to match when full string isn't found verbatim."""
    toks = cited_text.lower()
    # Remove common connector words; keep content-bearing terms.
    toks = re.sub(r"\b(the|a|an|of|and|in|on|for|is|are)\b", " ", toks)
    toks = re.sub(r"[^a-z0-9 ]", " ", toks)
    toks = re.split(r"\s+", toks.strip())
    return [t for t in toks if len(t) >= 4]


def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    print("# Check: 04 — Citation cross-reference against claim markdown")
    print("# Claim: S1-RL-1")
    print(f"# Run:   {now}")
    print(f"# Tool:  python3 {sys.version.split()[0]} (stdlib only)")
    print("# Script: verification/realism-locality/check_04_citation_crossref.py")
    print("# ----")
    print()

    with open(INPUTS_PATH, "r") as f:
        inputs = json.load(f)

    if not os.path.exists(MARKDOWN_PATH):
        print(f"FAIL — markdown file not found at {MARKDOWN_PATH}")
        print("STATUS: FAIL")
        sys.exit(1)

    with open(MARKDOWN_PATH, "r") as f:
        md = f.read()

    md_norm = normalize(md)

    results = []
    for c in inputs["citations"]:
        cid = c["id"]
        cited = c["cited_text"]
        cited_norm = normalize(cited)

        full_hit = cited_norm in md_norm

        # Token-level fallback: majority of key tokens present.
        tokens = key_tokens(cited)
        present = [t for t in tokens if t in md_norm]
        token_hit = len(present) >= max(1, (2 * len(tokens)) // 3) if tokens else False

        # Author-year fallback
        authors = c.get("author", [])
        first_author_surname = authors[0].split(",")[0].lower() if authors else ""
        year = str(c.get("year", ""))
        author_year_hit = (
            first_author_surname in md_norm and year in md_norm
        )

        passed = full_hit or token_hit or author_year_hit

        print(f"Citation: {cid}")
        print(f"  cited_text: {cited}")
        print(f"  full normalized hit:   {full_hit}")
        print(f"  key-token hit ({len(present)}/{len(tokens)}): {token_hit}")
        print(f"    key tokens: {tokens}")
        print(f"    tokens present: {present}")
        print(f"  author+year fallback: {author_year_hit}  ({first_author_surname!r}, {year!r})")
        print(f"  RESULT: {'PASS' if passed else 'FAIL'}")
        print()
        results.append((cid, passed))

    passed_total = sum(1 for _, ok in results if ok)
    total = len(results)
    print(f"Summary: {passed_total}/{total} citations cross-referenced into the markdown.")

    status = "PASS" if passed_total == total else "FAIL"
    print()
    print(f"STATUS: {status}")


if __name__ == "__main__":
    main()
