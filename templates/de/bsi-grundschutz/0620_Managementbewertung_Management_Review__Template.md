# Managementbewertung (Management Review) – Template

**Dokument-ID:** 0620  
**Dokumenttyp:** Nachweis/Template  
**Referenzrahmen:** BSI IT-Grundschutz (BSI Standards 200-1/200-2)  
**Owner:** {{ meta.document.owner }}  
**Version:** {{ meta.document.version }}  
**Status:** {{ meta.document.status }}  
**Klassifizierung:** {{ meta.document.classification }}  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  
**Nächster Review:** {{ meta.document.next_review }}

---

<!-- 
TEMPLATE AUTHOR NOTE:
This template documents the annual management review of the ISMS.
Reference: BSI Standard 200-1 (Management Review)
-->

## 1. Teilnehmer, Zeitraum, Scope

**Datum:** [TODO]  
**Ort:** [TODO]  
**Dauer:** [TODO]

**Teilnehmer:**
- Geschäftsführung: {{ meta.ceo.name }}
- ISB: {{ meta.ciso.name }}
- IT-Leitung: {{ meta.cio.name }}
- [TODO: Weitere Teilnehmer]

**Informationsverbund(e):** [TODO: Siehe Dokument 0040]

## 2. Inputs für Management Review

### 2.1 Status Maßnahmenplan

**Maßnahmenumsetzung:** [TODO: % abgeschlossen]  
**Kritische Maßnahmen:** [TODO: Status]  
**Verzögerungen:** [TODO: Beschreibung und Gründe]

**Referenz:** Dokument 0100 (Maßnahmenplan)

### 2.2 Ergebnisse Audits und Checks

**Interne Audits:** [TODO: Zusammenfassung]  
**Basis-Sicherheitscheck:** [TODO: Erfüllungsgrad]  
**Externe Audits:** [TODO: falls durchgeführt]

**Referenz:** Dokument 0610 (Auditprogramm), Dokument 0080 (Basis-Check)

### 2.3 Sicherheitsvorfälle und Lessons Learned

**Anzahl Vorfälle:** [TODO]  
**Kritische Vorfälle:** [TODO: Beschreibung]  
**Lessons Learned:** [TODO: Erkenntnisse]  
**Präventivmaßnahmen:** [TODO]

**Referenz:** Dokument 0320/0330 (Incident Management)

### 2.4 Änderungen im Kontext

**Technologie:**
- [TODO: Neue Systeme, Cloud-Migration, etc.]

**Organisation:**
- [TODO: Umstrukturierungen, neue Standorte, etc.]

**Lieferanten:**
- [TODO: Neue Dienstleister, Vertragsänderungen]

**Rechtliche Anforderungen:**
- [TODO: Neue Gesetze, Regulierungen]

### 2.5 Risikolage und Top-Risiken

**Risiko-Exposition:** [TODO: Anzahl "Sehr hoch"/"Hoch"-Risiken]  
**Top 5 Risiken:** [TODO: Siehe Dokument 0090]  
**Neue Bedrohungen:** [TODO]

**Referenz:** Dokument 0090 (Risikoanalyse)

### 2.6 KPI-Performance

**IT-Grundschutz-Erfüllungsgrad:** [TODO: %]  
**Patch-Compliance:** [TODO: %]  
**Schulungsquote:** [TODO: %]  
**Weitere KPIs:** [TODO]

**Referenz:** Dokument 0110 (KPIs)

## 3. Outputs und Entscheidungen

### 3.1 Anpassung Leitlinie und Ziele

**Entscheidung:** [TODO: Leitlinie anpassen? Ja/Nein]  
**Begründung:** [TODO]  
**Neue Sicherheitsziele:** [TODO]

**Verantwortlich:** {{ meta.ceo.name }}

### 3.2 Ressourcen und Investitionen

**Budget-Anpassung:** [TODO: Erhöhung/Reduzierung]  
**Personalressourcen:** [TODO: Zusätzliche Stellen?]  
**Externe Unterstützung:** [TODO]

**Verantwortlich:** {{ meta.ceo.name }}

### 3.3 Risikoakzeptanzen

**Akzeptierte Risiken:** [TODO: Risiko-IDs]  
**Begründung:** [TODO]  
**Gültigkeitsdauer:** [TODO]

**Verantwortlich:** {{ meta.ceo.name }}

### 3.4 Verbesserungsmaßnahmen

| Maßnahme | Beschreibung | Owner | Zieltermin | Priorität |
|---|---|---|---|---|
| [TODO] | [TODO] | [TODO] | [TODO] | Hoch/Mittel/Niedrig |

### 3.5 Scope-Änderungen

**Scope-Erweiterung:** [TODO: Neue Systeme/Standorte]  
**Scope-Reduzierung:** [TODO: falls zutreffend]

**Referenz:** Dokument 0040 (Scope)

## 4. Zusammenfassung und Fazit

**Gesamtbewertung ISMS:** [TODO: Effektiv/Verbesserungsbedarf]  
**Haupterkenntnisse:** [TODO]  
**Nächste Schritte:** [TODO]

## 5. Freigabe

| Rolle | Name | Datum | Unterschrift |
|---|---|---|---|
| Geschäftsführung | {{ meta.ceo.name }} | [TODO] | [TODO] |
| ISB | {{ meta.ciso.name }} | [TODO] | [TODO] |

---

**Referenzen:**
- BSI Standard 200-1: ISMS (Management Review)
- Alle ISMS-Dokumente (0010-0630)

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |

<!-- End of template -->