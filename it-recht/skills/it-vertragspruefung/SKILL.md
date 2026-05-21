---
name: it-vertragspruefung
description: "Prüfung typischer IT-Verträge (SaaS, Cloud, Outsourcing, Werkvertrag/Dienstvertrag-Abgrenzung) auf AGB-Konformität, DSGVO-Verzahnung (Art. 28 AVV), Leistungsstandards (SLA), Haftungsbegrenzung, Migrations- und Beendigungsklauseln, Open-Source-Compliance. Use when ein IT-Dienstleistungsvertrag bewertet oder verhandelt wird."
language: de
provider_variants: [claude, gemini, openai]
test: ./test.md
---

# /it-recht:it-vertragspruefung

## Zweck

IT-Verträge enthalten regelmäßig Klauseln, die in der AGB-Inhaltskontrolle (§§ 305 ff. BGB) scheitern, DSGVO-Pflichten missachten oder unverhältnismäßige Haftungsverteilungen schaffen. Dieser Skill identifiziert die typischen Bruchstellen entlang eines strukturierten Prüfschemas.

## Eingaben

- Vertragstyp (SaaS, Cloud-Hosting, Outsourcing, Individual-Software-Entwicklung, Wartung)
- Vertragsrolle (Anbieter / Kunde)
- Größenklasse (B2B / B2C)
- DSGVO-relevant (personenbezogene Daten verarbeitet?)
- Vorhandene Vorlagen (EVB-IT, BVB, BITKOM, eigene)

## Ablauf

### 1. Vertragstyp-Einordnung

Maßgeblich für anwendbares Recht:

| Vertragstyp | Rechtsnatur | Schwerpunkt |
|---|---|---|
| **SaaS / Cloud-Hosting** | Miet- oder Pachtvertrag (§§ 535 ff. BGB), str. | Verfügbarkeit, Datenherausgabe |
| **Software-Entwicklung individuell** | Werkvertrag (§ 631 BGB) | Abnahme, Mängelhaftung |
| **Wartung / Support** | Dienstvertrag (§ 611 BGB) | Reaktionszeiten, kein Erfolg geschuldet |
| **IT-Outsourcing** | Mischvertrag (Dienst + Werk + Miete) | Vereinbarte Service-Level |
| **Lizenzvertrag** | atypischer Vertrag (§§ 311a, 631 analog) | Reichweite der Lizenz |

### 2. AGB-Kontrolle (§§ 305 ff. BGB)

Vorlagen aus einer Mehrzahl an Verträgen sind AGB. **Auch im B2B** gelten § 305c, § 307 BGB (über § 310 Abs. 1 S. 2 BGB).

Typische problematische Klauseln:

- **Haftungsausschluss für einfache Fahrlässigkeit** in Bezug auf vertragstypische Kardinalpflichten → § 307 BGB, unwirksam.
- **Pauschalierung auf Jahresvergütung** → grundsätzlich zulässig, aber sorgfältig im Verhältnis.
- **Vertragsanpassung durch Anbieter** ohne Widerspruchsrecht → § 308 Nr. 5 BGB.
- **„Wir haften nur, soweit gesetzlich zwingend"** → Transparenzgebot § 307 Abs. 1 S. 2.

### 3. DSGVO-Verzahnung

#### Auftragsverarbeitungsvertrag (Art. 28 DSGVO)

Wenn personenbezogene Daten verarbeitet werden: AVV nach Art. 28 Abs. 3 DSGVO verpflichtend. Pflichtinhalte:

- Gegenstand und Dauer der Verarbeitung
- Art und Zweck der Verarbeitung
- Datenkategorien und Betroffenenkategorien
- Pflichten und Rechte des Verantwortlichen
- Maßnahmen nach Art. 32 DSGVO
- Sub-Auftragsverarbeiter
- Unterstützung bei Betroffenenanfragen
- Löschung / Rückgabe nach Beendigung
- Audit-Rechte des Verantwortlichen

#### Drittlandtransfer

US-Cloud-Anbieter: TIA + SCC + ggf. EU-US Data Privacy Framework. Beachte: Schrems II-Lage.

### 4. Service-Level-Agreements (SLA)

- Verfügbarkeit: Prozentangabe (z. B. 99,5 %) mit Berechnungsmethodik
- Reaktionszeit / Wiederherstellungszeit
- Wartungsfenster (geplant / ungeplant)
- Sanktionen bei Unterschreitung (Gutschriften, Sonderkündigungsrecht)
- Reporting / Monitoring

### 5. Migrations- und Beendigungsklauseln

Kritisch bei Cloud-/SaaS-Verträgen:

- **Datenherausgabe** in maschinenlesbarem Format, ohne Zusatzkosten
- **Übergangszeitraum** mit Mitwirkung des Anbieters
- **Löschung der Daten** nach Vertragsende mit Nachweis
- **Vendor Lock-in-Vermeidung** (Datenexport-Schnittstellen)

### 6. Open-Source-Compliance

- Inventarisierung verwendeter OSS-Komponenten (SBOM)
- Lizenz-Verträglichkeit (GPL vs. MIT vs. Apache)
- Copyleft-Risiko bei Distribution

### 7. Haftung und Versicherung

- Kardinalpflichten klar definieren
- Cap auf Jahresvergütung (typisch 1 bis 2 x)
- Ausnahmen für Vorsatz, grobe Fahrlässigkeit, Leib/Leben, ProdHaftG
- Versicherungsnachweis (Cyber, Berufshaftpflicht)

## Quellen

### Statute

- [§§ 305–310 BGB](https://www.gesetze-im-internet.de/bgb/__305.html)
- [§ 611 BGB](https://www.gesetze-im-internet.de/bgb/__611.html), [§ 631 BGB](https://www.gesetze-im-internet.de/bgb/__631.html), [§ 535 BGB](https://www.gesetze-im-internet.de/bgb/__535.html)
- [Art. 28 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679)
- [Art. 32 DSGVO](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32016R0679), Art. 44 ff.
- [UrhG](https://www.gesetze-im-internet.de/urhg/) (Lizenzen)

### Vorlagen / Standards

- **EVB-IT** (Ergänzende Vertragsbedingungen IT) – öffentliche Beschaffung
- **BITKOM-Musterverträge**
- **BVB** (Besondere Vertragsbedingungen)

### Rechtsprechung

- BGH, Urt. v. 15.11.2006 – XII ZR 120/04, NJW 2007, 2394 (SaaS = Miete) `[unverifiziert – prüfen]`
- BGH, Urt. v. 18.12.2009 – V ZR 130/08, NJW 2010, 1962 (Cloud-Haftung) `[unverifiziert – prüfen]`

## Ausgabeformat

```
IT-VERTRAGSPRÜFUNG — <Vertragsbezeichnung> — <Datum>

I.    Vertragstyp                    [SaaS / Werkvertrag / Outsourcing / …]
      Anwendbares Recht:              <…>
II.   AGB-Kontrolle                   [✓ / ⚠️ / ❌]
      Problemklauseln:                <…>
III.  DSGVO
      AVV vorhanden + vollständig:    [✓ / 🔴 lückenhaft]
      Drittlandtransfer:              [N/A / SCC / DPF — TIA-Status]
IV.   SLA
      Verfügbarkeit, Reaktionszeit:   <…>
      Sanktionen:                     <…>
V.    Migration / Beendigung
      Datenherausgabe:                [✓ / 🔴]
      Löschnachweis:                  [✓ / 🔴]
VI.   Open Source
      SBOM:                           [vorhanden / fehlt]
      Lizenz-Verträglichkeit:         [✓ / ⚠️]
VII.  Haftung
      Cap:                            <EUR oder x Jahresvergütung>
      Ausnahmen:                      [vollständig / unvollständig]

Verhandlungsstrategie:                <…>
```

## Risiken / typische Fehler

- **SaaS ohne AVV** — DSGVO-Verstoß, Bußgeldrisiko Art. 83 DSGVO.
- **Drittlandtransfer ohne TIA** — Schrems II-Risiko.
- **Haftungsausschluss zu weit** — § 309 Nr. 7 BGB, § 307 BGB.
- **Datenherausgabe-Klausel fehlt** — Vendor Lock-in als Verhandlungshebel des Anbieters.
- **Open Source ohne Compliance-Prüfung** — Copyleft-Risiko bei späterer Distribution.
- **„Wir nutzen den Vendor-Standard"** — ohne eigene Prüfung kein Vertrauensschutz.
