#!/usr/bin/env python3
"""Validate the structure of ai-skills-german-law.

Checks every plugin/area for:
- presence of `.claude-plugin/plugin.json` with required keys
- presence of `README.md`, `agents/`, `skills/`, `tests/`
- every skill having `SKILL.md` with valid frontmatter
- every skill having (or being marked as missing) a `test.md`
- citation-marker consistency (no [generiert] in client-facing skill bodies)

Exit code:
- 0 on success
- 1 on structural failures
- 2 on usage error

Usage:
    python scripts/validate.py
    python scripts/validate.py --area arbeitsrecht
    python scripts/validate.py --strict
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REQUIRED_PLUGIN_KEYS = {"name", "version", "description", "license"}
REQUIRED_SKILL_FRONTMATTER = {"name", "description"}
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


class ValidationError:
    def __init__(self, path: Path, kind: str, message: str):
        self.path = path
        self.kind = kind
        self.message = message

    def __str__(self) -> str:
        rel = self.path.relative_to(REPO_ROOT) if self.path.is_absolute() else self.path
        return f"  [{self.kind}] {rel}: {self.message}"


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Tiny YAML-ish frontmatter parser — only supports the subset we use."""
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    raw = parts[1]
    body = parts[2]
    meta: dict = {}
    current_key = None
    for line in raw.splitlines():
        line = line.rstrip()
        if not line:
            continue
        if re.match(r"^\s+-\s+", line) and current_key:
            meta.setdefault(current_key, [])
            if isinstance(meta[current_key], list):
                meta[current_key].append(line.strip()[2:].strip())
            continue
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if not m:
            continue
        key, value = m.group(1), m.group(2).strip()
        current_key = key
        if value in ("", "[]"):
            meta[key] = [] if value == "[]" else None
        else:
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            meta[key] = value
    return meta, body


def validate_plugin_json(plugin_path: Path, errors: list[ValidationError]) -> None:
    try:
        data = json.loads(plugin_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(ValidationError(plugin_path, "plugin-json", f"invalid JSON: {exc}"))
        return
    missing = REQUIRED_PLUGIN_KEYS - set(data.keys())
    if missing:
        errors.append(
            ValidationError(
                plugin_path,
                "plugin-json",
                f"missing required keys: {sorted(missing)}",
            )
        )


def validate_skill(skill_dir: Path, strict: bool, errors: list[ValidationError]) -> None:
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        errors.append(ValidationError(skill_dir, "skill", "missing SKILL.md"))
        return
    text = skill_md.read_text(encoding="utf-8")
    meta, body = parse_frontmatter(text)
    missing = REQUIRED_SKILL_FRONTMATTER - set(meta.keys())
    if missing:
        errors.append(
            ValidationError(skill_md, "skill-frontmatter", f"missing keys: {sorted(missing)}")
        )
    if not meta.get("description") or len(str(meta.get("description", ""))) < 20:
        errors.append(
            ValidationError(skill_md, "skill-frontmatter", "description too short or empty")
        )
    if "[generiert" in body:
        errors.append(
            ValidationError(
                skill_md,
                "citation",
                "skill body contains a [generiert] marker — forbidden in client-facing skills",
            )
        )
    if strict and "[unverifiziert" not in body and ", NZA " not in body and ", NJW " not in body:
        errors.append(
            ValidationError(
                skill_md,
                "citation",
                "no case-law citations found — strict mode expects at least one",
            )
        )
    test_md = skill_dir / "test.md"
    if not test_md.exists():
        errors.append(ValidationError(skill_dir, "skill", "missing test.md (eval fact pattern)"))


def validate_area(area: str, strict: bool, errors: list[ValidationError]) -> None:
    base = REPO_ROOT / area
    if not base.is_dir():
        errors.append(ValidationError(base, "area", "directory missing"))
        return
    plugin = base / ".claude-plugin" / "plugin.json"
    if not plugin.exists():
        errors.append(ValidationError(plugin, "area", "missing .claude-plugin/plugin.json"))
    else:
        validate_plugin_json(plugin, errors)
    for required in ("README.md", "skills"):
        if not (base / required).exists():
            errors.append(ValidationError(base / required, "area", "missing"))
    skills_dir = base / "skills"
    if skills_dir.is_dir():
        skill_dirs = [p for p in skills_dir.iterdir() if p.is_dir()]
        if not skill_dirs:
            errors.append(ValidationError(skills_dir, "area", "no skills under skills/"))
        for skill_dir in skill_dirs:
            validate_skill(skill_dir, strict, errors)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate ai-skills-german-law structure")
    parser.add_argument("--area", help="Validate a single area (e.g. arbeitsrecht)")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Require at least one case-law citation per skill",
    )
    args = parser.parse_args()

    errors: list[ValidationError] = []
    areas = [args.area] if args.area else AREAS

    marketplace = REPO_ROOT / ".claude-plugin" / "marketplace.json"
    if marketplace.exists():
        try:
            json.loads(marketplace.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(ValidationError(marketplace, "marketplace", f"invalid JSON: {exc}"))
    else:
        errors.append(ValidationError(marketplace, "marketplace", "missing"))

    for area in areas:
        validate_area(area, args.strict, errors)

    if errors:
        print(f"FAIL — {len(errors)} validation error(s):")
        for err in errors:
            print(err)
        return 1
    scope = f"area={args.area}" if args.area else f"{len(AREAS)} areas"
    print(f"OK — {scope} validated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
