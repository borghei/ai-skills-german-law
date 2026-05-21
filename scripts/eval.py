#!/usr/bin/env python3
"""Eval harness for ai-skills-german-law skills.

This script does NOT call any LLM. It performs structural assertions against
each skill's `test.md` file:

- the SKILL.md contains every "must_cite" anchor declared in test.md
- the SKILL.md "Ausgabeformat" template covers every "must_appear" section
- the SKILL.md flags every "must_flag" risk in its Risiken section

A full LLM-eval (sending the fact pattern to a model and comparing output) is
out of scope here — that requires a § 203-compliant gateway and a budget. The
structural eval still catches the most common failures: missing statute,
missing risk warning, missing output section.

Usage:
    python scripts/eval.py
    python scripts/eval.py --area arbeitsrecht
    python scripts/eval.py --skill arbeitsrecht/kuendigungs-pruefung
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
AREAS = [
    "arbeitsrecht",
    "datenschutzrecht",
    "vertragsrecht",
    "mietrecht",
    "gesellschaftsrecht",
    "strafrecht",
    "ki-vo-compliance",
    "nis2",
    "hinweisgeberschutz",
    "lieferkettengesetz",
    "dora",
    "dsa-dma",
    "csrd",
    "insolvenzrecht",
    "prozessrecht",
    "it-recht",
    "bankrecht",
    "erbrecht",
    "familienrecht",
    "betreuungsrecht",
    "gewerblicher-rechtsschutz",
    "steuerrecht",
    "verwaltungsrecht",
]


class EvalResult:
    def __init__(self, skill: str):
        self.skill = skill
        self.passes: list[str] = []
        self.failures: list[str] = []

    @property
    def ok(self) -> bool:
        return not self.failures

    def summary(self) -> str:
        status = "PASS" if self.ok else "FAIL"
        return (
            f"[{status}] {self.skill}: {len(self.passes)} ok, {len(self.failures)} failed"
        )


def parse_test(test_path: Path) -> dict:
    """Test files are markdown with a YAML-ish block at the top.

    Example test.md:
        ---
        fact_pattern: |
          Mandant plant betriebsbedingte Kündigung von 3 von 12 AN.
        must_cite:
          - "§ 1 KSchG"
          - "§ 102 BetrVG"
        must_appear:
          - "Sonderkündigungsschutz-Check"
          - "Sozialauswahl"
        must_flag:
          - "Massenentlassungsanzeige"
        ---
    """
    if not test_path.exists():
        return {}
    text = test_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}
    raw = parts[1]
    meta: dict = {}
    current_key = None
    for line in raw.splitlines():
        if not line.strip():
            continue
        if re.match(r"^\s+-\s+", line) and current_key:
            value = line.strip()[2:].strip()
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            meta.setdefault(current_key, [])
            if isinstance(meta[current_key], list):
                meta[current_key].append(value)
        else:
            m = re.match(r"^([a-z_]+):\s*(.*)$", line)
            if not m:
                continue
            key, value = m.group(1), m.group(2).strip()
            current_key = key
            if value == "":
                meta[key] = []
            elif value == "|":
                meta[key] = ""
            else:
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                meta[key] = value
    return meta


def evaluate(skill_dir: Path) -> EvalResult:
    rel = skill_dir.relative_to(REPO_ROOT).as_posix()
    result = EvalResult(rel)
    skill_md = skill_dir / "SKILL.md"
    test_md = skill_dir / "test.md"

    if not skill_md.exists():
        result.failures.append("SKILL.md missing")
        return result
    if not test_md.exists():
        result.failures.append("test.md missing")
        return result

    body = skill_md.read_text(encoding="utf-8")
    test = parse_test(test_md)

    for anchor in test.get("must_cite", []) or []:
        if anchor in body:
            result.passes.append(f"cites {anchor}")
        else:
            result.failures.append(f"missing citation: {anchor}")

    for section in test.get("must_appear", []) or []:
        if section in body:
            result.passes.append(f"section present: {section}")
        else:
            result.failures.append(f"missing section: {section}")

    for risk in test.get("must_flag", []) or []:
        if risk in body:
            result.passes.append(f"risk flagged: {risk}")
        else:
            result.failures.append(f"missing risk flag: {risk}")

    if not (test.get("must_cite") or test.get("must_appear") or test.get("must_flag")):
        result.failures.append("test.md has no assertions (must_cite / must_appear / must_flag)")

    return result


def find_skills(area: str | None, skill: str | None) -> list[Path]:
    if skill:
        skill_dir = REPO_ROOT / skill
        if not skill_dir.is_dir():
            sys.exit(f"skill directory not found: {skill_dir}")
        return [skill_dir]
    areas = [area] if area else AREAS
    found: list[Path] = []
    for a in areas:
        skills_dir = REPO_ROOT / a / "skills"
        if not skills_dir.is_dir():
            continue
        for p in sorted(skills_dir.iterdir()):
            if p.is_dir() and (p / "SKILL.md").exists():
                found.append(p)
    return found


def main() -> int:
    parser = argparse.ArgumentParser(description="Structural eval for ai-skills-german-law")
    parser.add_argument("--area", help="One area name")
    parser.add_argument("--skill", help="Skill path relative to repo root")
    parser.add_argument("--json", action="store_true", help="Output JSON to stdout")
    args = parser.parse_args()

    skills = find_skills(args.area, args.skill)
    if not skills:
        print("No skills found.")
        return 0

    results = [evaluate(s) for s in skills]
    failed = [r for r in results if not r.ok]

    if args.json:
        out = [
            {
                "skill": r.skill,
                "ok": r.ok,
                "passes": r.passes,
                "failures": r.failures,
            }
            for r in results
        ]
        print(json.dumps(out, indent=2, ensure_ascii=False))
    else:
        for r in results:
            print(r.summary())
            for f in r.failures:
                print(f"    - {f}")

    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main())
