<p align="center">
  <img src="assets/header.svg" alt="AI Skills, German Law" width="100%"/>
</p>

<h1 align="center">AI Skills, German Law</h1>
<p align="center"><b>Tested AI skills for German legal practice and EU compliance. Works with Claude, Gemini, and GPT.</b></p>

<p align="center">
  <a href="https://github.com/borghei/AI-Skills-German-Law/actions/workflows/validate.yml"><img src="https://img.shields.io/github/actions/workflow/status/borghei/AI-Skills-German-Law/validate.yml?branch=main&label=CI&logo=github" alt="CI Status"></a>
  <img src="https://img.shields.io/badge/Areas-23-brightgreen.svg" alt="23 Areas">
  <img src="https://img.shields.io/badge/Skills-28-success.svg" alt="28 Skills">
  <img src="https://img.shields.io/badge/Providers-Claude_%7C_Gemini_%7C_GPT-purple.svg" alt="Providers">
  <img src="https://img.shields.io/badge/Last_verified-2026--05--21-blue.svg" alt="Last verified">
  <img src="https://img.shields.io/badge/Compliance-DSGVO_%7C_KI--VO_%7C_NIS2_%7C_HinSchG_%7C_LkSG_%7C_DORA_%7C_DSA_%7C_CSRD-red.svg" alt="Compliance">
  <img src="https://img.shields.io/github/stars/borghei/AI-Skills-German-Law?style=social" alt="GitHub Stars">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache--2.0_OR_MIT-yellow.svg" alt="License"></a>
</p>

<p align="center">
  <a href="#install-in-60-seconds"><b>Install</b></a> ·
  <a href="#whats-inside"><b>Areas</b></a> ·
  <a href="#how-much-you-can-rely-on-it"><b>Trust</b></a> ·
  <a href="VERIFICATION_LOG.md"><b>Verification log</b></a> ·
  <a href="#compliance--berufsrecht"><b>Compliance</b></a> ·
  <a href="CONTRIBUTING.md"><b>Contribute</b></a>
</p>

---

## Disclaimer

> **This project is built with the assistance of AI tools (Claude, GPT, Gemini).** While every effort is made to ensure accuracy, AI-generated content (skill definitions, reference guides, citations, templates) may contain errors. **This is not legal advice.** Any output of these skills is a draft for review by a licensed Rechtsanwalt or Syndikusrechtsanwalt under § 43a BRAO and § 2 BORA. Always verify case-law citations independently in Beck-Online, juris, or openjur.net before client-facing or court-facing use. The author accepts no liability. **Use at your own risk.**

---

## The problem

A `[Modellwissen]`-Halluzination in einem Kündigungsschreiben ist kein Bug. Sie ist Haftungsexposure unter § 43a Abs. 2 BRAO. Most legal-AI repos are either a clever prompt with no sourcing, or a 100-skill experiment that nobody tested end-to-end. Neither belongs in a Kanzlei.

## The fix

A focused, **provider-agnostic** library: 23 areas, 28 skills, every statute citation linked to its authoritative source, every case-law citation explicitly marked verified or `[unverifiziert, prüfen]`. A built-in evaluation harness checks every skill against fact patterns. A dated [verification log](VERIFICATION_LOG.md) shows exactly what was checked, when, against which source.

It is **not legal advice**, **not a Beck-Online substitute**, and **not for Mandatsdaten without a § 203 StGB-compliant gateway**. It is a tested drafting aid with an honest paper trail.

---

## Install in 60 seconds

```bash
# Claude Code (native plugin marketplace)
/plugin marketplace add borghei/AI-Skills-German-Law

# Then enable an area
/plugin install arbeitsrecht
```

**Other providers, one Python command:**

```bash
git clone https://github.com/borghei/AI-Skills-German-Law.git
cd AI-Skills-German-Law

# Gemini Gems
python scripts/route_provider.py --provider gemini --skill arbeitsrecht/kuendigungs-pruefung

# OpenAI (Custom GPT / Assistants API)
python scripts/route_provider.py --provider openai --skill arbeitsrecht/kuendigungs-pruefung
```

**Manual, any AI chat:** open any `SKILL.md`, copy the body, paste into Claude.ai, ChatGPT, or Gemini.

---

## Who this is for

| Role | What you get |
|---|---|
| **Kanzlei-Anwält:innen / Syndikus** | A structured drafting aid for Kündigung, Aufhebungsvertrag, Abmahnung, AGB-Prüfung, Mieterhöhung, Strafbefehl, with the sources you'd cite anyway |
| **In-house counsel / Mittelstand-GC** | Compliance scaffolding for KI-VO, NIS2, HinSchG, LkSG, DORA, DSA/DMA, CSRD, the EU frameworks every European company touches |
| **Compliance Officer / DSB** | DSGVO Art. 15-Workflows, Datenpannen-Meldung, AVV-Review, DPIA, primary sources, EuGH-Verzahnung |
| **Legal-tech builder** | A clean plugin architecture (researcher then drafter then reviewer), a router that emits Claude / Gemini / GPT adapters from one SKILL.md, a CI-tested eval harness |

---

## What's inside

**23 areas: 11 substantive areas of German law plus 5 Fachanwaltschaften plus 7 EU/cross-cutting compliance frameworks** that affect virtually every European company. Each area ships as its own installable plugin.

### German legal practice

| Area | Plugin | Coverage |
|---|---|---|
| **Arbeitsrecht** | [`arbeitsrecht/`](./arbeitsrecht/) | KSchG-Prüfung, § 102 BetrVG, Aufhebungsvertrag, Abmahnung, Sozialauswahl, Massenentlassung |
| **Datenschutzrecht / GDPR** | [`datenschutzrecht/`](./datenschutzrecht/) | DSGVO/BDSG, AVV-Review, Art. 15 Auskunft, Art. 33/34 Datenpanne, DPIA, Drittlandtransfer |
| **Vertragsrecht** | [`vertragsrecht/`](./vertragsrecht/) | AGB-Kontrolle §§ 305 ff. BGB, Klauselgestaltung, c.i.c., Leistungsstörung, Anfechtung |
| **Mietrecht** | [`mietrecht/`](./mietrecht/) | Wohnraummiete, Mieterhöhung § 558 BGB, Kündigung §§ 573 ff., Betriebskostenabrechnung, WEG |
| **Gesellschaftsrecht** | [`gesellschaftsrecht/`](./gesellschaftsrecht/) | GmbH-Recht (GmbHG), Geschäftsführerhaftung, Gesellschafterbeschlüsse, AG-Grundzüge |
| **Strafrecht** | [`strafrecht/`](./strafrecht/) | Strafbefehl-Verteidigung, Akteneinsicht, OWi-Verkehrsrecht, Beschuldigtenbelehrung |
| **Insolvenzrecht** | [`insolvenzrecht/`](./insolvenzrecht/) | Antragspflicht § 15a InsO, StaRUG, 13-Wochen-Liquiditätsplanung, Fortbestehensprognose |
| **Prozessrecht** | [`prozessrecht/`](./prozessrecht/) | Klageschrift §§ 253 ff. ZPO, Streitgegenstand, Sachvortrag, Zuständigkeit, Rechtsmittel |
| **Erbrecht** | [`erbrecht/`](./erbrecht/) | Testament, Erbvertrag, Pflichtteil §§ 2303 ff. BGB, Erbschein, Erbengemeinschaft |
| **Familienrecht** | [`familienrecht/`](./familienrecht/) | Scheidung, Zugewinnausgleich §§ 1372 ff. BGB, Unterhalt, Sorge- und Umgangsrecht |
| **Betreuungsrecht** | [`betreuungsrecht/`](./betreuungsrecht/) | Reform 2023 (§§ 1814 ff. BGB), Jahresbericht § 1863 BGB, Vermögenssorge, Genehmigungspflicht |

### Fachanwaltschaften

| Area | Plugin | Coverage |
|---|---|---|
| **IT-Recht** | [`it-recht/`](./it-recht/) | SaaS-Verträge, Outsourcing, Softwarelizenz, Open Source Compliance, Cloud-AVV |
| **Bank- und Kapitalmarktrecht** | [`bankrecht/`](./bankrecht/) | Verbraucherdarlehen §§ 491 ff. BGB, MiFID II, Wertpapierprospekt, Anlageberatung |
| **Gewerblicher Rechtsschutz** | [`gewerblicher-rechtsschutz/`](./gewerblicher-rechtsschutz/) | Marken (MarkenG), Patente (PatG), Designs (DesignG), UWG, Abmahnungswesen |
| **Steuerrecht** | [`steuerrecht/`](./steuerrecht/) | Außenprüfung, Einspruchsverfahren §§ 347 ff. AO, Selbstanzeige § 371 AO, FGO |
| **Verwaltungsrecht** | [`verwaltungsrecht/`](./verwaltungsrecht/) | Widerspruchsverfahren §§ 68 ff. VwGO, Anfechtungs-/Verpflichtungsklage, § 80 VwGO |

### EU / cross-cutting compliance

| Area | Plugin | Triggers when |
|---|---|---|
| **EU KI-VO / AI Act** | [`ki-vo-compliance/`](./ki-vo-compliance/) | Any company deploying AI in the EU |
| **NIS2** | [`nis2/`](./nis2/) | ~30,000 German entities (essential plus important) |
| **HinSchG** | [`hinweisgeberschutz/`](./hinweisgeberschutz/) | Every employer with 50 or more EE |
| **LkSG** | [`lieferkettengesetz/`](./lieferkettengesetz/) | Companies over 1,000 EE in DE (CSDDD soon broader) |
| **DORA** | [`dora/`](./dora/) | Banks, insurers, investment firms, crypto, CASPs |
| **DSA / DMA** | [`dsa-dma/`](./dsa-dma/) | Hosting providers, online platforms, VLOPs, gatekeepers |
| **CSRD / ESRS** | [`csrd/`](./csrd/) | Large companies, phased 2024 to 2028 (Omnibus pending) |

Each area includes a researcher sub-agent (Quellensuche), drafter sub-agent (Entwurf nach Gutachtenstil), reviewer sub-agent (Risiko- und Berufsrechts-Check), conventions per [`CONVENTIONS.md`](./CONVENTIONS.md), and at least one runnable test under `<area>/tests/`.

---

## What's different from other German legal-AI repos

| | Most repos | This repo |
|---|---|---|
| **Source citations** | Free-form, often hallucinated | Statutes link to [gesetze-im-internet.de](https://www.gesetze-im-internet.de); case law explicitly marked verified or `[unverifiziert]` |
| **Architecture** | One monolithic prompt | Researcher then drafter then reviewer split per skill |
| **Testing** | A README disclaimer | Fact-pattern eval harness with 110+ structural assertions, runs on every CI build |
| **Compliance** | A warning paragraph | PII redaction script, gateway-routing walkthrough, dated [verification log](VERIFICATION_LOG.md), DSGVO/§203/KI-VO checklist |
| **Provider lock-in** | Claude only | Provider-agnostic canonical SKILL.md plus Claude Code / Gemini Gems / OpenAI adapters generated by `scripts/route_provider.py` |

---

## How much you can rely on it

We are unsentimental about trust. Here is what is verified today, what is in active improvement, and what is the user's responsibility.

### Production-grade today

- **Repo structure plus CI.** Every plugin manifest validates. CI runs `validate.py` on every push to catch structural drift. Locally, `python scripts/eval.py` adds 370+ fact-pattern assertions across 28 skills (28/28 passing).
- **Statute citations.** Every `§ X` links to the **authoritative public source**, [gesetze-im-internet.de](https://www.gesetze-im-internet.de) and [EUR-Lex](https://eur-lex.europa.eu). One click, verifiable.
- **Methodology.** Gutachtenstil, Anspruchsgrundlagen-Reihenfolge, BGH/Beck-Zitierweise, no Präjudizienbindungs-Argumente, textbook-correct conventions, documented in [`CONVENTIONS.md`](./CONVENTIONS.md) and enforced by the reviewer sub-agent.
- **Compliance scaffolding.** PII redaction ([`scripts/pii_redact.py`](./scripts/pii_redact.py)), gateway setup guide ([`references/gateway-setup.md`](./references/gateway-setup.md)), § 203 / DSGVO / KI-VO checklist ([`references/compliance-checklist.md`](./references/compliance-checklist.md)).
- **Multi-provider parity.** One canonical `SKILL.md` per skill; the router regenerates Claude / Gemini / OpenAI adapters on demand, no drift.

### In active improvement (contributions welcome)

- **Case-law verification.** Every BAG / BGH / EuGH citation the model could not independently confirm carries `[unverifiziert, prüfen]`. The verification path is one PR per citation with a Beck-Online / juris / openjur URL. **Highest-leverage contribution.**
- **Legal-accuracy eval.** Today eval is structural (does the workflow mention § 1 KSchG). The next layer compares actual model output to expert-drafted gold answers.
- **Rechtsanwalt review.** Each area gets stronger after a 2-hour pass by a licensed Anwalt in that Rechtsgebiet. Reviews are credited per area.

### Hard limitations

- **No real Mandatsdaten without a § 203-compliant gateway.** Anthropic, Google, OpenAI do not sign Verschwiegenheitserklärungen directly for German lawyers. Route through Langdock, deepset Cloud, or comparable before processing privileged data. Setup walkthrough: [`references/gateway-setup.md`](./references/gateway-setup.md).
- **Every output is a draft.** No skill produces signature-ready text. The Berufspflicht under § 43a Abs. 2 BRAO and § 2 BORA stays with the licensed Anwalt.

### Verification path

```
1. Open the area you need (e.g. arbeitsrecht/)
2. Read the SKILL.md. Identify every [unverifiziert] citation.
3. Verify each in Beck-Online or juris (~30 sec/each). Open a PR removing the marker.
4. Run the skill against an anonymized historical Mandat you already know.
5. Wire a § 203-compliant gateway.
6. Use on live Mandate only after 1 to 5 plus your own Berufsrechts-Freigabe.
```

The full audit trail lives in [`VERIFICATION_LOG.md`](./VERIFICATION_LOG.md), last pass 2026-05-21.

---

## Quickstart

```bash
# Validate the repo structure
python scripts/validate.py
# OK, 13 areas validated.

# Run the eval suite (structural smoke check)
python scripts/eval.py
# 15/15 skills passing

# Redact German PII from a document before sending it to a model
python scripts/pii_redact.py --in mandat.txt --out mandat-redacted.txt
# redacted: IBAN=1, PHONE_INTL=1, PLZ_ORT=1, DATE=2

# Generate provider-specific bundles
python scripts/route_provider.py --provider claude --out dist/claude
python scripts/route_provider.py --provider gemini --out dist/gemini
python scripts/route_provider.py --provider openai --out dist/openai

# Chain multiple skills (e.g., full Kündigungs-Workflow)
python scripts/orchestrate.py --preset kuendigung-vollumfang --fact "..."
python scripts/orchestrate.py --list-chains
```

---

## Compliance & Berufsrecht

This repo is a **technical skill collection**. It certifies nothing about your deployment. The following obligations stay with you:

| Topic | Norm | Who decides |
|---|---|---|
| Mandatsgeheimnis | §§ 203, 204 StGB · § 43e BRAO · § 2 BORA | Kanzlei / Compliance |
| DSGVO / BDSG | Art. 28 AVV · Art. 35 DPIA · Art. 44 ff. Drittlandtransfer | DSB |
| Drittlandtransfer | EU-US DPF · Standardvertragsklauseln · TIA (Schrems II) | Datenschutzkonferenz / EuGH |
| EU KI-VO | Art. 6 plus Anhang III · Art. 26 Betreiberpflichten · Art. 50 Transparenz | Compliance / Geschäftsleitung |
| Beschlagnahmeverbote | §§ 97, 160a StPO vs. US Cloud Act / FISA § 702 | Mandantenanwalt |

Built-in helpers: [`references/compliance-checklist.md`](./references/compliance-checklist.md) · [`references/gateway-setup.md`](./references/gateway-setup.md) · [`scripts/pii_redact.py`](./scripts/pii_redact.py)

---

## Documentation

| Document | What's in it |
|---|---|
| [`QUICKSTART.md`](./QUICKSTART.md) | 60-second install + use guide for Claude / Gemini / GPT |
| [`CONVENTIONS.md`](./CONVENTIONS.md) | Provider-neutral conventions: language, methodology, citation, skill format |
| [`CODE_OF_CONDUCT.md`](./CODE_OF_CONDUCT.md) | Contributor Covenant 2.1 |
| [`VERIFICATION_LOG.md`](./VERIFICATION_LOG.md) | Dated source-verification record, last pass 2026-05-21 |
| [`references/zitierweise.md`](./references/zitierweise.md) | BGH/Beck-Zitierweise (verbindlich) |
| [`references/methodik.md`](./references/methodik.md) | Gutachtenstil, Anspruchsgrundlagen-Reihenfolge, Auslegungsmethoden |
| [`references/primary-sources.md`](./references/primary-sources.md) | Verified URLs to gesetze-im-internet.de plus EUR-Lex |
| [`references/compliance-checklist.md`](./references/compliance-checklist.md) | § 203 / DSGVO / KI-VO checklist before deployment |
| [`references/gateway-setup.md`](./references/gateway-setup.md) | Routing through a § 203-compliant gateway |
| [`CONTRIBUTING.md`](./CONTRIBUTING.md) | How to add skills, verify citations, run tests |

---

## Contribute

The highest-leverage thing you can do is **verify one case-law citation**. It takes 30 seconds in Beck-Online or juris, and the resulting PR helps every future user.

Also welcome:

- **Verified citations**, replace `[unverifiziert, prüfen]` markers with a Beck-Online / juris / openjur URL
- **New areas**, agrar-, bau-, erbe-, familien-, sozial-, steuer-, verwaltungsrecht; or EU frameworks like eIDAS 2.0, CRA, MiCA. Start by copying `arbeitsrecht/` as a template
- **Test cases**, anonymized fact patterns are the most valuable contribution
- **Provider adapters**, Mistral, DeepSeek, Llama
- **Compliance corrections**, § 203, § 43e BRAO, KI-VO, Drittlandtransfer

See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for the PR workflow.

---

## License

Dual-licensed: **Apache-2.0** ([LICENSE-APACHE](./LICENSE-APACHE)) **OR** **MIT** ([LICENSE-MIT](./LICENSE-MIT)) at your option. Attribution: [`NOTICE`](./NOTICE).

---

<p align="center">
  <strong>23 areas · 28 skills · 3 LLM providers · Researcher then Drafter then Reviewer · DSGVO / KI-VO / NIS2 / HinSchG / LkSG / DORA / DSA / CSRD scaffolding</strong><br>
  Verified <strong>2026-05-21</strong> · <a href="https://borghei.me">borghei.me</a>
</p>

<p align="center">
  <a href="https://buymeacoffee.com/borghei"><img src="https://img.shields.io/badge/Buy%20Me%20a%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me a Coffee"></a>
</p>
