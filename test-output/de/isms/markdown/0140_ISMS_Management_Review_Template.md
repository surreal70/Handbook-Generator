# Management Review (Template)



**Dokument-ID:** 0140  
**Dokumenttyp:** ISMS-Nachweis/Template  
**Standard-Referenz:** ISO/IEC 27001:2022 Clause 9.3  
**Owner:** Thomas Weber  
**Version:** 1.0  
**Status:** Freigegeben  
**Klassifizierung:** Vertraulich  
**Letzte Aktualisierung:** {{ meta.document.date }}  
**Nächster Review:** {{ meta.document.next_review }}

---

## 1. Management Review-Übersicht

### 1.1 Teilnehmer und Zeitraum

**Review-Datum:** [TODO: Datum]  
**Review-Zeitraum:** [TODO: z.B. 01.01.2026 - 31.12.2026]  
**Nächster Review:** [TODO: Datum]

**Teilnehmer:**

| Name | Rolle | Anwesend |
|------|-------|----------|
| {{ meta.management.ceo }} | Geschäftsführung (Vorsitz) | ✓ / ✗ |
| Thomas Weber | CISO | ✓ / ✗ |
| Anna Schmidt | CIO | ✓ / ✗ |
| [TODO] | CFO | ✓ / ✗ |
| [TODO] | Vertreter Fachabteilungen | ✓ / ✗ |
| {{ meta.audit.manager }} | Internal Audit (beratend) | ✓ / ✗ |

### 1.2 Scope

Dieser Management Review umfasst:
- Gesamtes ISMS im Scope (siehe `0020_ISMS_Geltungsbereich_Scope.md`)
- Alle Standorte: {{ netbox.site.name }} und weitere
- Review-Zeitraum: [TODO]

## 2. Inputs (Clause 9.3.2)

### 2.1 Status der Maßnahmen aus vorherigem Review

**Maßnahmen aus letztem Review ([TODO: Datum]):**

| Maßnahme | Verantwortlich | Frist | Status | Bemerkungen |
|----------|----------------|-------|--------|-------------|
| [TODO] | [TODO] | [TODO] | Abgeschlossen / In Arbeit / Offen | [TODO] |

**Zusammenfassung:**
- Abgeschlossen: [TODO] von [TODO]
- In Arbeit: [TODO]
- Offen/Überfällig: [TODO]

### 2.2 Änderungen bei externen und internen Themen

**Externe Änderungen:**
- **Regulatorische Änderungen:** [TODO: z.B. NIS2-Umsetzung, DSGVO-Updates]
- **Bedrohungslage:** [TODO: z.B. Neue Ransomware-Varianten, APT-Aktivitäten]
- **Marktentwicklung:** [TODO: z.B. Neue Wettbewerber, Kundenanforderungen]
- **Technologietrends:** [TODO: z.B. Cloud-Migration, KI-Einsatz]

**Interne Änderungen:**
- **Organisatorisch:** [TODO: z.B. Merger, Akquisitionen, Umstrukturierungen]
- **Personell:** [TODO: z.B. Neue CISO, Teamvergrößerung]
- **Technologisch:** [TODO: z.B. Neue Systeme, Cloud-Migration]
- **Prozesse:** [TODO: z.B. DevOps-Einführung, Agile Transformation]

**Auswirkungen auf ISMS:**
- Scope-Änderungen erforderlich: Ja / Nein
- Risikoanalyse-Update erforderlich: Ja / Nein
- Policy-Updates erforderlich: Ja / Nein

### 2.3 Feedback zu Informationssicherheitsleistung

**KPI-Entwicklung:**

| KPI | Zielwert | Aktuell | Vorjahr | Trend | Status |
|-----|----------|---------|---------|-------|--------|
| Anzahl Security Incidents | < 10/Quartal | [TODO] | [TODO] | ↑ / → / ↓ | ✓ / ✗ |
| Risiken mit Score ≥ 13 | < 5 | [TODO] | [TODO] | ↑ / → / ↓ | ✓ / ✗ |
| Uptime kritischer Systeme | ≥ 99,5% | [TODO]% | [TODO]% | ↑ / → / ↓ | ✓ / ✗ |
| Patch-Compliance (kritisch) | < 7 Tage | [TODO] Tage | [TODO] Tage | ↑ / → / ↓ | ✓ / ✗ |
| Schulungsteilnahme | 100% | [TODO]% | [TODO]% | ↑ / → / ↓ | ✓ / ✗ |
| Phishing-Klickrate | < 5% | [TODO]% | [TODO]% | ↑ / → / ↓ | ✓ / ✗ |

**Zusammenfassung:**
- Ziele erreicht: [TODO] von [TODO]
- Verbesserungen: [TODO]
- Verschlechterungen: [TODO]

**Stakeholder-Feedback:**
- Kunden: [TODO]
- Mitarbeiter: [TODO]
- Aufsichtsbehörden: [TODO]
- Lieferanten: [TODO]

### 2.4 Ergebnisse interner und externer Audits

**Interne Audits:**

| Audit-Datum | Scope | Findings (Major/Minor/Obs) | Status | Bemerkungen |
|-------------|-------|----------------------------|--------|-------------|
| [TODO] | Access Management | 0 / 2 / 3 | Abgeschlossen | Alle Findings behoben |
| [TODO] | Vulnerability Management | 1 / 1 / 2 | In Arbeit | Major Finding in Bearbeitung |
| [TODO] | Vollständiges ISMS | 0 / 5 / 8 | Abgeschlossen | Verbesserungen umgesetzt |

**Externe Audits:**

| Audit-Datum | Auditor | Scope | Ergebnis | Zertifikat | Bemerkungen |
|-------------|---------|-------|----------|------------|-------------|
| [TODO] | [TODO: Zertifizierungsstelle] | ISO 27001:2022 | Bestanden | Gültig bis [TODO] | Rezertifizierung erfolgreich |

**Zusammenfassung:**
- Offene Major Findings: [TODO]
- Offene Minor Findings: [TODO]
- Durchschnittliche Behebungszeit: [TODO] Tage

### 2.5 Feedback von interessierten Parteien

**Kunden:**
- Sicherheitsanforderungen: [TODO]
- Zufriedenheit: [TODO]
- Incidents mit Kundenauswirkung: [TODO]

**Aufsichtsbehörden:**
- Meldepflichtige Vorfälle: [TODO]
- Compliance-Status: [TODO]

**Lieferanten:**
- Third-Party-Risiken: [TODO]
- Sicherheitsvorfälle bei Lieferanten: [TODO]

### 2.6 Ergebnisse der Risikobewertung

**Risiko-Übersicht:**

| Risikostufe | Anzahl Risiken | Vorjahr | Trend |
|-------------|----------------|---------|-------|
| Sehr hoch | [TODO] | [TODO] | ↑ / → / ↓ |
| Hoch | [TODO] | [TODO] | ↑ / → / ↓ |
| Mittel | [TODO] | [TODO] | ↑ / → / ↓ |
| Niedrig | [TODO] | [TODO] | ↑ / → / ↓ |

**Top 5 Risiken:**

| Risiko-ID | Beschreibung | Score | Behandlung | Status |
|-----------|--------------|-------|------------|--------|
| R-001 | [TODO] | [TODO] | [TODO] | [TODO] |
| R-002 | [TODO] | [TODO] | [TODO] | [TODO] |
| R-003 | [TODO] | [TODO] | [TODO] | [TODO] |
| R-004 | [TODO] | [TODO] | [TODO] | [TODO] |
| R-005 | [TODO] | [TODO] | [TODO] | [TODO] |

**Neue Risiken:**
- [TODO: Liste neuer Risiken seit letztem Review]

**Geschlossene Risiken:**
- [TODO: Liste geschlossener Risiken]

### 2.7 Möglichkeiten zur kontinuierlichen Verbesserung

**Identifizierte Verbesserungsmöglichkeiten:**

| ID | Bereich | Verbesserung | Nutzen | Aufwand | Priorität |
|----|---------|--------------|--------|---------|-----------|
| V-001 | [TODO] | [TODO] | [TODO] | [TODO] | Hoch / Mittel / Niedrig |
| V-002 | [TODO] | [TODO] | [TODO] | [TODO] | Hoch / Mittel / Niedrig |

**Lessons Learned:**
- Aus Security Incidents: [TODO]
- Aus Audits: [TODO]
- Aus Projekten: [TODO]

### 2.8 Relevante Änderungen

**ISMS-Scope:**
- Änderungen: [TODO: Neue Standorte, Systeme, Prozesse]
- Auswirkungen: [TODO]

**Technologie:**
- Neue Systeme: [TODO]
- Cloud-Migration: [TODO]
- Technologie-Refresh: [TODO]

**Lieferanten:**
- Neue kritische Lieferanten: [TODO]
- Beendete Lieferantenbeziehungen: [TODO]

**Personal:**
- Neue Schlüsselpersonen: [TODO]
- Abgänge: [TODO]

### 2.9 Incidents und Lessons Learned

**Security Incidents:**

| Incident-ID | Datum | Schweregrad | Beschreibung | Auswirkung | Lessons Learned | Status |
|-------------|-------|-------------|--------------|------------|-----------------|--------|
| INC-001 | [TODO] | Hoch | [TODO] | [TODO] | [TODO] | Geschlossen |
| INC-002 | [TODO] | Mittel | [TODO] | [TODO] | [TODO] | Geschlossen |

**Zusammenfassung:**
- Anzahl Incidents: [TODO]
- Major Incidents: [TODO]
- MTTD (Mean Time to Detect): [TODO]
- MTTR (Mean Time to Respond): [TODO]

**Umgesetzte Verbesserungen:**
- [TODO: Maßnahmen aus Lessons Learned]

### 2.10 Ressourcen

**Budget:**
- Geplantes Budget: [TODO] €
- Tatsächliche Ausgaben: [TODO] €
- Abweichung: [TODO] € ([TODO]%)

**Personal:**
- Geplante FTE: [TODO]
- Tatsächliche FTE: [TODO]
- Engpässe: [TODO]

**Externe Unterstützung:**
- Berater: [TODO]
- Managed Services: [TODO]
- Schulungen: [TODO]

## 3. Outputs / Entscheidungen (Clause 9.3.3)

### 3.1 Anpassungen an ISMS-Leitlinie und Zielen

**ISMS-Leitlinie:**
- Änderungen erforderlich: Ja / Nein
- Beschreibung: [TODO]
- Verantwortlich: Thomas Weber
- Frist: [TODO]

**Sicherheitsziele:**
- Neue Ziele: [TODO]
- Anpassung bestehender Ziele: [TODO]
- Verantwortlich: Thomas Weber
- Frist: [TODO]

### 3.2 Ressourcen und Investitionen

**Genehmigte Investitionen:**

| Investition | Beschreibung | Budget | Verantwortlich | Frist | Priorität |
|-------------|--------------|--------|----------------|-------|-----------|
| [TODO] | [TODO] | [TODO] € | [TODO] | [TODO] | Hoch / Mittel / Niedrig |

**Personalressourcen:**
- Zusätzliche FTE: [TODO]
- Externe Unterstützung: [TODO]
- Schulungsbudget: [TODO] €

### 3.3 Verbesserungsmaßnahmen

**Beschlossene Maßnahmen:**

| Maßnahme-ID | Maßnahme | Ziel | Verantwortlich | Frist | Budget | Status |
|-------------|----------|------|----------------|-------|--------|--------|
| M-001 | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] € | Genehmigt |
| M-002 | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] € | Genehmigt |

### 3.4 Akzeptierte Risiken

**Risikoakzeptanz durch Geschäftsführung:**

| Risiko-ID | Beschreibung | Score | Begründung | Gültig bis | Kompensationsmaßnahmen |
|-----------|--------------|-------|------------|------------|------------------------|
| R-010 | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

### 3.5 Scope-Änderungen

**Beschlossene Scope-Änderungen:**
- [TODO: Neue Standorte, Systeme, Prozesse]
- Auswirkungen auf Risikoanalyse: [TODO]
- Auswirkungen auf SoA: [TODO]
- Verantwortlich: Thomas Weber
- Frist: [TODO]

### 3.6 Strategische Entscheidungen

**Strategische Ausrichtung:**
- [TODO: z.B. Cloud-First-Strategie, Zero-Trust-Architektur]

**Compliance-Strategie:**
- [TODO: z.B. NIS2-Vorbereitung, zusätzliche Zertifizierungen]

**Sicherheitskultur:**
- [TODO: z.B. Security Champions Program, Awareness-Kampagnen]

## 4. Zusammenfassung und Bewertung

### 4.1 Gesamtbewertung des ISMS

**Eignung (Suitability):**
- Das ISMS ist geeignet für die Organisation: Ja / Nein / Teilweise
- Begründung: [TODO]

**Angemessenheit (Adequacy):**
- Das ISMS ist angemessen für die Risiken: Ja / Nein / Teilweise
- Begründung: [TODO]

**Wirksamkeit (Effectiveness):**
- Das ISMS ist wirksam: Ja / Nein / Teilweise
- Begründung: [TODO]

**Gesamtbewertung:**
- [TODO: Zusammenfassende Bewertung durch Geschäftsführung]

### 4.2 Nächste Schritte

1. [TODO: Maßnahme 1]
2. [TODO: Maßnahme 2]
3. [TODO: Maßnahme 3]

**Nächster Management Review:** [TODO: Datum]

## 5. Anhänge

### 5.1 Unterstützende Dokumente

- Risikoregister (`0080_ISMS_Risikoregister_Template.md`)
- Risikobehandlungsplan (`0090_ISMS_Risikobehandlungsplan_RTP_Template.md`)
- Audit-Berichte (`0130_ISMS_Internes_Auditprogramm.md`)
- KPI-Dashboard (`0110_ISMS_Sicherheitsziele_und_Metriken.md`)
- Incident Reports (`0400_Policy_Incident_Management.md`)

### 5.2 Präsentationen

- [TODO: Link zu Management Review Präsentation]

## 6. Referenzen

### 6.1 Interne Dokumente

- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS Policy
- `0020_ISMS_Geltungsbereich_Scope.md` - ISMS Scope
- `0080_ISMS_Risikoregister_Template.md` - Risk Register
- `0090_ISMS_Risikobehandlungsplan_RTP_Template.md` - Risk Treatment Plan
- `0110_ISMS_Sicherheitsziele_und_Metriken.md` - Security Objectives
- `0130_ISMS_Internes_Auditprogramm.md` - Internal Audit Program

### 6.2 Externe Standards

- **ISO/IEC 27001:2022** - Clause 9.3: Management review
- **ISO/IEC 27002:2022** - Information security controls

---

## Änderungshistorie

| Version | Datum | Autor | Beschreibung | Genehmigt durch |
|---------|-------|-------|--------------|-----------------|
| 1.0 | {{ meta.document.date }} | Thomas Weber | Initiale Version | {{ meta.management.ceo }} |

---

**Protokolliert durch:**  
Thomas Weber, CISO  
Datum: [TODO]

**Genehmigt durch:**  
{{ meta.management.ceo }}, Geschäftsführung  
Datum: [TODO]

**Nächster Review:** [TODO: Datum] (Jährlich)
