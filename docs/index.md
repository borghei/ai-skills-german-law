---
title: AI Skills, German Law
---

# AI Skills, German Law

**Tested AI skills for German legal practice and EU compliance.**

A focused, provider-agnostic skill library: 23 areas, 28 skills, every statute citation linked to its authoritative source, every case-law citation explicitly marked verified or `[unverifiziert, prüfen]`. Built-in evaluation harness, dated verification log, multi-provider adapters for Claude, Gemini, and GPT.

<div class="stats" markdown>
<div class="stat">
<div class="number">23</div>
<div class="label">Areas</div>
</div>
<div class="stat">
<div class="number">28</div>
<div class="label">Skills</div>
</div>
<div class="stat">
<div class="number">370+</div>
<div class="label">Assertions</div>
</div>
<div class="stat">
<div class="number">3</div>
<div class="label">Providers</div>
</div>
<div class="stat">
<div class="number">8</div>
<div class="label">Compliance Frameworks</div>
</div>
</div>

---

## Quick Install

```bash
# Claude Code (native plugin marketplace)
/plugin marketplace add borghei/AI-Skills-German-Law
/plugin install arbeitsrecht

# Or clone for Gemini / OpenAI / manual use
git clone https://github.com/borghei/AI-Skills-German-Law.git
cd AI-Skills-German-Law
python scripts/route_provider.py --provider gemini --skill arbeitsrecht/kuendigungs-pruefung
```

See [Installation](getting-started/installation.md) for per-provider setup and the [Quick Start](getting-started/quick-start.md) for a 60-second walkthrough.

---

## Areas

<div class="grid" markdown>

<div class="card" markdown>
### :material-gavel: Arbeitsrecht
**3 skills** &middot; KSchG, BetrVG, BGB

KSchG-Prüfung, § 102 BetrVG, Aufhebungsvertrag, Abmahnung, Sozialauswahl, Massenentlassung.

[:octicons-arrow-right-24: Browse](areas/german-law.md)
</div>

<div class="card" markdown>
### :material-shield-lock: Datenschutzrecht / GDPR
**1 skill** &middot; DSGVO / BDSG / TTDSG

AVV-Review, Art. 15 Auskunft, Art. 33/34 Datenpanne, DPIA, Drittlandtransfer + Schrems II.

[:octicons-arrow-right-24: Browse](areas/german-law.md)
</div>

<div class="card" markdown>
### :material-file-document-edit: Vertragsrecht
**1 skill** &middot; §§ 305-310 BGB

AGB-Kontrolle, Klauselgestaltung B2B/B2C, c.i.c., Leistungsstörung, Anfechtung.

[:octicons-arrow-right-24: Browse](areas/german-law.md)
</div>

<div class="card" markdown>
### :material-home-city: Mietrecht
**1 skill** &middot; BGB / BetrKV

Wohnraummiete, Mieterhöhung § 558 BGB, Kündigung §§ 573 ff., Betriebskostenabrechnung.

[:octicons-arrow-right-24: Browse](areas/german-law.md)
</div>

<div class="card" markdown>
### :material-domain: Gesellschaftsrecht
**1 skill** &middot; GmbHG / AktG

GmbH-Geschäftsführerhaftung §§ 43, 64, Gesellschafterbeschlüsse, AG-Grundzüge.

[:octicons-arrow-right-24: Browse](areas/german-law.md)
</div>

<div class="card" markdown>
### :material-handcuffs: Strafrecht
**1 skill** &middot; StPO / StGB / OWiG

Strafbefehl-Verteidigung §§ 407 ff. StPO, Akteneinsicht, OWi-Verkehrsrecht.

[:octicons-arrow-right-24: Browse](areas/german-law.md)
</div>

<div class="card" markdown>
### :material-account-cash: Insolvenzrecht
**4 skills** &middot; InsO / StaRUG

Antragspflicht § 15a InsO, StaRUG, 13-Wochen-Liquiditätsplanung, Fortbestehensprognose.

[:octicons-arrow-right-24: Browse](areas/german-law.md)
</div>

<div class="card" markdown>
### :material-court-hammer: Prozessrecht
**1 skill** &middot; ZPO

Klageschrift §§ 253 ff. ZPO, Streitgegenstand, Sachvortrag, Zuständigkeit, Rechtsmittel.

[:octicons-arrow-right-24: Browse](areas/german-law.md)
</div>

<div class="card" markdown>
### :material-account-multiple: Personal law
**3 skills** &middot; Erb-, Familien-, Betreuungsrecht

Testament, Zugewinnausgleich, Jahresbericht § 1863 BGB (Reform 2023).

[:octicons-arrow-right-24: Browse](areas/german-law.md)
</div>

<div class="card" markdown>
### :material-school: Fachanwaltschaften
**5 areas** &middot; IT, Bank, IP, Steuer, Verwaltung

Specialty practice areas mapped to bar Fachanwalt-Qualifikationen.

[:octicons-arrow-right-24: Browse](areas/fachanwaltschaften.md)
</div>

<div class="card" markdown>
### :material-flag: EU compliance
**7 areas** &middot; KI-VO, NIS2, HinSchG, LkSG, DORA, DSA, CSRD

Cross-cutting frameworks every European company touches.

[:octicons-arrow-right-24: Browse](areas/eu-compliance.md)
</div>

</div>

---

## What You Get

| | |
|---|---|
| **23 Areas** | 11 substantive German law areas + 5 Fachanwaltschaften + 7 EU compliance frameworks |
| **28 Skills** | Each with Researcher then Drafter then Reviewer sub-agent breakdown |
| **370+ Assertions** | Structural eval (`scripts/eval.py`) runs against every skill, 28/28 passing |
| **3 LLM providers** | Claude Code, Gemini Gems, OpenAI Custom GPTs. One canonical SKILL.md per skill, adapters generated on demand |
| **Verification log** | Dated source-verification record. Last pass 2026-05-21 |
| **Compliance scaffolding** | PII redaction script, gateway-routing walkthrough, § 203 / DSGVO / KI-VO checklist |

---

## Usage Examples

**Validate the repo and run the eval suite:**

```bash
python scripts/validate.py
python scripts/eval.py
```

```
OK -- 23 areas validated.
28/28 skills passing
```

**Render a skill for Gemini:**

```bash
python scripts/route_provider.py --provider gemini --skill arbeitsrecht/kuendigungs-pruefung
```

**Chain three skills for a full Kündigung pipeline:**

```bash
python scripts/orchestrate.py --preset kuendigung-vollumfang --fact "..."
```

**Redact German PII before sending to a model:**

```bash
python scripts/pii_redact.py --in mandat.txt --out mandat-redacted.txt
```

```
redacted: IBAN=1, PHONE_INTL=1, PLZ_ORT=1, DATE=2
```

---

## License

**Apache-2.0 OR MIT** at your option. See [LICENSE](https://github.com/borghei/AI-Skills-German-Law/blob/main/LICENSE) and [NOTICE](https://github.com/borghei/AI-Skills-German-Law/blob/main/NOTICE).

## Disclaimer

> **This project is built with the assistance of AI tools (Claude, GPT, Gemini).** AI-generated content may contain errors. **This is not legal advice.** Every output is a draft for review by a licensed Rechtsanwalt under § 43a BRAO and § 2 BORA. Verify case-law citations independently in Beck-Online, juris, or openjur.net before client-facing or court-facing use. The author accepts no liability. **Use at your own risk.**
