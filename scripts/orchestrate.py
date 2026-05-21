#!/usr/bin/env python3
"""Multi-skill workflow orchestrator.

Chain skills together in a deterministic order. The orchestrator does NOT
call an LLM. It assembles the prompts for a sequence of skills so a human
(or a downstream caller) can feed them to the model of their choice.

Use cases:
- A new Mandat starts with `mandat-triage` then `kuendigungs-pruefung` then
  `aufhebungsvertrag` then a reviewer pass.
- An insolvency case chains `liquiditaetsplanung-13-wochen` →
  `fortbestehensprognose` → `antragspflicht-15a-inso`.
- A compliance project chains `hochrisiko-klassifizierung` → `dpia` →
  `betreiberpflichten-art-26`.

The orchestrator reads each SKILL.md, strips its frontmatter, and prints
the canonical body wrapped in markers so the downstream model sees a clear
multi-step instruction.

Usage:
    python scripts/orchestrate.py \\
        --chain arbeitsrecht/kuendigungs-pruefung arbeitsrecht/aufhebungsvertrag \\
        --fact "Mandantin plant betriebsbedingte Kündigung von 3 von 12 AN ..."

    python scripts/orchestrate.py --list-chains
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

# Curated chains. Add new ones here as patterns emerge.
PRESET_CHAINS: dict[str, list[str]] = {
    "kuendigung-vollumfang": [
        "arbeitsrecht/kuendigungs-pruefung",
        "arbeitsrecht/abmahnung",
        "arbeitsrecht/aufhebungsvertrag",
    ],
    "krise-360": [
        "insolvenzrecht/liquiditaetsplanung-13-wochen",
        "insolvenzrecht/fortbestehensprognose",
        "insolvenzrecht/antragspflicht-15a-inso",
        "gesellschaftsrecht/gmbh-geschaeftsfuehrerhaftung",
    ],
    "starug-restructuring": [
        "insolvenzrecht/liquiditaetsplanung-13-wochen",
        "insolvenzrecht/starug-restrukturierungsplan",
    ],
    "ki-deployment-compliance": [
        "ki-vo-compliance/hochrisiko-klassifizierung",
        "datenschutzrecht/auskunftsersuchen-art-15",
        "it-recht/it-vertragspruefung",
    ],
    "dsgvo-datenpanne": [
        "datenschutzrecht/auskunftsersuchen-art-15",
        "nis2/meldepflicht-24h",
    ],
    "scheidung-full": [
        "familienrecht/scheidung-zugewinnausgleich",
    ],
}


def strip_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        return "", text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return "", text
    return parts[1].strip(), parts[2].lstrip("\n")


def find_skill(skill_path: str) -> Path:
    """skill_path is like 'arbeitsrecht/kuendigungs-pruefung'."""
    candidate = REPO_ROOT / skill_path.split("/")[0] / "skills" / skill_path.split("/")[1] / "SKILL.md"
    if not candidate.exists():
        sys.exit(f"skill not found: {candidate}")
    return candidate


def render_chain(chain: list[str], fact: str | None) -> str:
    lines: list[str] = []
    lines.append("ORCHESTRATED WORKFLOW")
    lines.append("=" * 60)
    lines.append(f"Steps: {len(chain)}")
    if fact:
        lines.append("")
        lines.append("Initial fact pattern:")
        lines.append(fact)
    lines.append("")
    for i, skill_path in enumerate(chain, 1):
        skill_md = find_skill(skill_path)
        text = skill_md.read_text(encoding="utf-8")
        _, body = strip_frontmatter(text)
        lines.append("=" * 60)
        lines.append(f"STEP {i} of {len(chain)}: {skill_path}")
        lines.append("=" * 60)
        lines.append("")
        lines.append(body)
        lines.append("")
        if i < len(chain):
            lines.append(f"--- end of step {i}; feed the output as input to step {i+1} ---")
            lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Multi-skill workflow orchestrator")
    parser.add_argument(
        "--chain",
        nargs="+",
        help="Explicit chain of skill paths, e.g. arbeitsrecht/kuendigungs-pruefung",
    )
    parser.add_argument("--preset", help="Use a curated chain by name (see --list-chains)")
    parser.add_argument("--fact", help="Initial fact pattern (free text)")
    parser.add_argument(
        "--list-chains", action="store_true", help="List the curated preset chains"
    )
    parser.add_argument("--out", help="Write to file instead of stdout")
    args = parser.parse_args()

    if args.list_chains:
        for name, steps in PRESET_CHAINS.items():
            print(f"{name}:")
            for step in steps:
                print(f"  - {step}")
            print()
        return 0

    if args.preset:
        if args.preset not in PRESET_CHAINS:
            sys.exit(f"unknown preset: {args.preset}. See --list-chains.")
        chain = PRESET_CHAINS[args.preset]
    elif args.chain:
        chain = args.chain
    else:
        sys.exit("provide --chain or --preset (or --list-chains)")

    rendered = render_chain(chain, args.fact)
    if args.out:
        Path(args.out).write_text(rendered, encoding="utf-8")
        print(f"wrote {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(rendered)
    return 0


if __name__ == "__main__":
    sys.exit(main())
