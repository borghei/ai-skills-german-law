# Quickstart

Get from zero to a working German legal AI skill in 60 seconds.

## Option 1: Claude Code (native)

```bash
# Add the marketplace
/plugin marketplace add borghei/AI-Skills-German-Law

# Install the area you need (replace with any of the 23 areas)
/plugin install arbeitsrecht

# Use it
/arbeitsrecht:kuendigungs-pruefung
```

## Option 2: Gemini (Gems)

```bash
git clone https://github.com/borghei/AI-Skills-German-Law.git
cd AI-Skills-German-Law

# Render the Gem instructions
python scripts/route_provider.py --provider gemini --skill arbeitsrecht/kuendigungs-pruefung
```

Open the generated file under `arbeitsrecht/skills/kuendigungs-pruefung/providers/gemini.md`, copy the content between the `BEGIN GEM INSTRUCTIONS` and `END GEM INSTRUCTIONS` markers, paste into a new Gem at [gemini.google.com](https://gemini.google.com).

## Option 3: OpenAI (Custom GPT or Assistants API)

```bash
python scripts/route_provider.py --provider openai --skill arbeitsrecht/kuendigungs-pruefung
```

For Custom GPTs: open the generated `providers/openai.md`, copy the instructions block, paste into the Configure tab of a new GPT at [chatgpt.com](https://chatgpt.com/gpts/editor).

For the Assistants API:

```python
from openai import OpenAI
client = OpenAI()
with open("arbeitsrecht/skills/kuendigungs-pruefung/providers/openai.md") as f:
    instructions = f.read()
assistant = client.beta.assistants.create(
    name="Arbeitsrecht: Kündigungs-Prüfung",
    instructions=instructions,
    model="gpt-4o",
)
```

## Option 4: Any AI chat (no setup)

Open any `SKILL.md` in the repo, copy the body (everything below the frontmatter), paste into Claude.ai, ChatGPT, or Gemini as the first message of a new conversation, then describe your Mandat.

## Pick an area

23 areas grouped by buyer persona:

**German legal practice** (everyday Kanzlei work):
`arbeitsrecht` · `datenschutzrecht` · `vertragsrecht` · `mietrecht` · `gesellschaftsrecht` · `strafrecht` · `insolvenzrecht` · `prozessrecht` · `erbrecht` · `familienrecht` · `betreuungsrecht`

**Fachanwaltschaften** (specialty practice):
`it-recht` · `bankrecht` · `gewerblicher-rechtsschutz` · `steuerrecht` · `verwaltungsrecht`

**EU / cross-cutting compliance** (every European company touches one of these):
`ki-vo-compliance` · `nis2` · `hinweisgeberschutz` · `lieferkettengesetz` · `dora` · `dsa-dma` · `csrd`

## Before any real Mandat

Three things, in order:

1. **Read [VERIFICATION_LOG.md](./VERIFICATION_LOG.md)**, last verified 2026-05-21
2. **Verify the case-law citations** in the SKILL.md you plan to use; replace `[unverifiziert, prüfen]` markers with sourced URLs (one PR per citation helps every user)
3. **Wire a § 203-compliant gateway** ([`references/gateway-setup.md`](./references/gateway-setup.md)) before sending any Mandatsdaten

Full conventions in [`CONVENTIONS.md`](./CONVENTIONS.md). Contribution flow in [`CONTRIBUTING.md`](./CONTRIBUTING.md).
