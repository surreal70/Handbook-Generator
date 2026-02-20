# Servicebeschreibung und Kritikalität

**Dokument-ID:** [FRAMEWORK]-0030
**Organisation:** AdminSend GmbH
**Owner:** [TODO]
**Genehmigt durch:** [TODO]
**Revision:** [TODO]
**Author:** Handbook-Generator
**Status:** Draft
**Klassifizierung:** Internal
**Letzte Aktualisierung:** [TODO]
**Template Version:** [TODO]

---

---

## Servicebeschreibung

### Basis-Informationen

- **Service-Name:** [TODO: Eindeutiger Service-Name]
- **Service-ID:** [TODO: Eindeutige Service-Identifikation]
- **Service-Owner:** [TODO]
- **Technischer Ansprechpartner:** [TODO: Name und Kontakt]
- **Organisation:** AdminSend GmbH

### Kurzbeschreibung

[TODO: Beschreiben Sie den Service in 2-3 Sätzen. Was macht der Service? Welche Hauptfunktionen bietet er?]

### Geschäftszweck

**Geschäftlicher Nutzen:**
[TODO: Welchen geschäftlichen Wert liefert dieser Service? Welche Geschäftsprozesse unterstützt er?]

**Strategische Bedeutung:**
[TODO: Wie wichtig ist dieser Service für die Unternehmensstrategie?]

### Kunden und Nutzergruppen

| Nutzergruppe | Anzahl Nutzer | Nutzungsart | Kritikalität |
|---|---:|---|---|
| [TODO: Gruppe 1] | [TODO] | [TODO: Primär/Sekundär] | [TODO: Hoch/Mittel/Niedrig] |
| [TODO: Gruppe 2] | [TODO] | [TODO: Primär/Sekundär] | [TODO: Hoch/Mittel/Niedrig] |
| [TODO: Gruppe 3] | [TODO] | [TODO: Primär/Sekundär] | [TODO: Hoch/Mittel/Niedrig] |

**Primäre Nutzergruppen:**
- [TODO: Beschreibung der Hauptnutzer]

**Sekundäre Nutzergruppen:**
- [TODO: Beschreibung der Nebennutzer]

### Abhängigkeiten zu anderen Services

#### Upstream-Abhängigkeiten (Services, von denen dieser Service abhängt)

| Service | Abhängigkeitstyp | Kritikalität | Auswirkung bei Ausfall |
|---|---|---|---|
| [TODO: Service 1] | [TODO: Hard/Soft] | [TODO: Hoch/Mittel/Niedrig] | [TODO: Beschreibung] |
| [TODO: Service 2] | [TODO: Hard/Soft] | [TODO: Hoch/Mittel/Niedrig] | [TODO: Beschreibung] |

#### Downstream-Abhängigkeiten (Services, die von diesem Service abhängen)

| Service | Abhängigkeitstyp | Kritikalität | Auswirkung bei Ausfall |
|---|---|---|---|
| [TODO: Service 1] | [TODO: Hard/Soft] | [TODO: Hoch/Mittel/Niedrig] | [TODO: Beschreibung] |
| [TODO: Service 2] | [TODO: Hard/Soft] | [TODO: Hoch/Mittel/Niedrig] | [TODO: Beschreibung] |

> **Hinweis:**
> - **Hard Dependency:** Service funktioniert nicht ohne Abhängigkeit
> - **Soft Dependency:** Service funktioniert eingeschränkt ohne Abhängigkeit

## Kritikalität und Schutzbedarf

### Kritikalitätsbewertung

Die Kritikalität wird nach den Dimensionen Verfügbarkeit, Integrität, Vertraulichkeit und Nachvollziehbarkeit bewertet.

| Dimension | Einstufung | Begründung | Maßnahmen |
|---|---|---|---|
| **Verfügbarkeit** | ☐ niedrig ☐ mittel ☐ hoch | [TODO: Begründung] | [TODO: Schutzmaßnahmen] |
| **Integrität** | ☐ niedrig ☐ mittel ☐ hoch | [TODO: Begründung] | [TODO: Schutzmaßnahmen] |
| **Vertraulichkeit** | ☐ niedrig ☐ mittel ☐ hoch | [TODO: Begründung] | [TODO: Schutzmaßnahmen] |
| **Nachvollziehbarkeit** | ☐ niedrig ☐ mittel ☐ hoch | [TODO: Begründung] | [TODO: Schutzmaßnahmen] |

### Kritikalitätsstufen

#### Niedrig
- **Verfügbarkeit:** Ausfall tolerierbar für mehrere Tage
- **Integrität:** Datenverlust akzeptabel, einfache Wiederherstellung
- **Vertraulichkeit:** Öffentliche oder unkritische Informationen
- **Nachvollziehbarkeit:** Keine Audit-Anforderungen

#### Mittel
- **Verfügbarkeit:** Ausfall tolerierbar für Stunden bis 1 Tag
- **Integrität:** Datenverlust problematisch, Wiederherstellung erforderlich
- **Vertraulichkeit:** Interne Informationen, eingeschränkter Zugriff
- **Nachvollziehbarkeit:** Basis-Logging erforderlich

#### Hoch
- **Verfügbarkeit:** Ausfall nur für Minuten tolerierbar
- **Integrität:** Datenverlust inakzeptabel, sofortige Wiederherstellung
- **Vertraulichkeit:** Vertrauliche Daten, strenge Zugriffskontrolle
- **Nachvollziehbarkeit:** Vollständiges Audit-Trail erforderlich

### Gesamtkritikalität

**Kritikalitätseinstufung:** [TODO: Niedrig/Mittel/Hoch/Kritisch]

**Begründung:**
[TODO: Zusammenfassende Begründung der Gesamtkritikalität basierend auf den einzelnen Dimensionen]

## Servicezeiten und Betriebsfenster

### Servicezeiten

- **Verfügbarkeit:** [TODO: z.B. 24/7, Mo-Fr 08:00-18:00 CET, Business Hours]
- **Support-Zeiten:** [TODO: Wann ist Support verfügbar?]
- **Zeitzone:** [TODO: z.B. CET/CEST, UTC]

### Betriebsmodell

- **Betriebsmodell:** [TODO: 24/7, Business Hours, Follow-the-Sun]
- **On-Call-Bereitschaft:** [TODO: Ja/Nein, Zeiten]
- **Eskalationsstufen:** [TODO: Level 1/2/3 Support]

### Wartungsfenster

| Wartungstyp | Zeitfenster | Frequenz | Dauer | Ankündigung |
|---|---|---|---|---|
| **Geplante Wartung** | [TODO: z.B. So 02:00-06:00] | [TODO: Wöchentlich/Monatlich] | [TODO: Stunden] | [TODO: Tage im Voraus] |
| **Notfallwartung** | [TODO: Nach Bedarf] | [TODO: Ad-hoc] | [TODO: Variable] | [TODO: Sofort] |
| **Patch-Fenster** | [TODO: z.B. 2. Dienstag/Monat] | [TODO: Monatlich] | [TODO: Stunden] | [TODO: Tage im Voraus] |

### Geplante Downtimes

**Kommunikationsprozess:**
1. **Ankündigung:** Mindestens [TODO: X Tage] im Voraus
2. **Kanal:** [TODO: E-Mail, Portal, Ticket-System]
3. **Empfänger:** [TODO: Alle Nutzer, Key-Stakeholder]
4. **Inhalt:** Zeitfenster, Grund, Auswirkungen, Ansprechpartner

**Verantwortlich:** {{ meta-organisation-roles.role_IT_Operations_Manager }} ({{ meta-organisation-roles.role_IT_Operations_Manager_email }})

## Service Level Agreements (SLA)

### SLA-Übersicht

| Kennzahl | Zielwert | Messmethode | Messquelle | Reporting |
|---|---:|---|---|---|
| **Verfügbarkeit** | [TODO: z.B. 99.9%] | [TODO: Uptime-Monitoring] | [TODO: Monitoring-Tool] | [TODO: Monatlich] |
| **MTTR** | [TODO: z.B. 4h] | [TODO: Ticket-Analyse] | [TODO: ITSM-Tool] | [TODO: Monatlich] |
| **MTBF** | [TODO: z.B. 720h] | [TODO: Incident-Analyse] | [TODO: ITSM-Tool] | [TODO: Quartalsweise] |
| **Antwortzeit** | [TODO: z.B. < 200ms] | [TODO: APM] | [TODO: APM-Tool] | [TODO: Täglich] |
| **Durchsatz** | [TODO: z.B. 1000 TPS] | [TODO: Performance-Monitoring] | [TODO: Monitoring-Tool] | [TODO: Täglich] |

### Service Level Objectives (SLO)

#### Verfügbarkeit

- **Ziel:** [TODO: z.B. 99.9% Uptime pro Monat]
- **Berechnung:** (Gesamtzeit - Downtime) / Gesamtzeit × 100%
- **Ausnahmen:** Geplante Wartungsfenster
- **Messung:** Kontinuierliches Uptime-Monitoring

#### Performance

- **Antwortzeit (P95):** [TODO: z.B. < 200ms]
- **Antwortzeit (P99):** [TODO: z.B. < 500ms]
- **Durchsatz:** [TODO: z.B. min. 1000 Requests/Sekunde]
- **Fehlerrate:** [TODO: z.B. < 0.1%]

#### Wiederherstellung

- **RTO (Recovery Time Objective):** [TODO: z.B. 4 Stunden]
- **RPO (Recovery Point Objective):** [TODO: z.B. 1 Stunde]
- **MTTR (Mean Time To Repair):** [TODO: z.B. 4 Stunden]
- **MTBF (Mean Time Between Failures):** [TODO: z.B. 720 Stunden]

### SLA-Reporting

**Reporting-Frequenz:** [TODO: Monatlich/Quartalsweise]

**Empfänger:**
- Service Owner: [TODO]
- IT Operations Manager: {{ meta-organisation-roles.role_IT_Operations_Manager }}
- CIO: [TODO]
- [TODO: Weitere Stakeholder]

**Inhalt:**
- Verfügbarkeitsstatistiken
- Performance-Metriken
- Incident-Übersicht
- SLA-Einhaltung
- Verbesserungsmaßnahmen

### SLA-Verletzungen

**Eskalationsprozess bei SLA-Verletzung:**

1. **Automatische Benachrichtigung:** Monitoring-System
2. **Analyse:** IT Operations Team
3. **Eskalation Level 1:** IT Operations Manager
4. **Eskalation Level 2:** CIO
5. **Root-Cause-Analysis:** Innerhalb [TODO: X Tage]
6. **Maßnahmenplan:** Innerhalb [TODO: X Tage]

## Kapazitätsplanung

### Aktuelle Kapazität

| Ressource | Aktuell | Maximum | Auslastung | Schwellwert |
|---|---:|---:|---:|---:|
| [TODO: CPU] | [TODO] | [TODO] | [TODO]% | [TODO]% |
| [TODO: RAM] | [TODO] | [TODO] | [TODO]% | [TODO]% |
| [TODO: Storage] | [TODO] | [TODO] | [TODO]% | [TODO]% |
| [TODO: Netzwerk] | [TODO] | [TODO] | [TODO]% | [TODO]% |

### Wachstumsprognose

- **Nutzerwachstum:** [TODO: z.B. +10% pro Jahr]
- **Datenwachstum:** [TODO: z.B. +20% pro Jahr]
- **Transaktionswachstum:** [TODO: z.B. +15% pro Jahr]

### Skalierungsstrategien

- **Vertikale Skalierung:** [TODO: Beschreibung]
- **Horizontale Skalierung:** [TODO: Beschreibung]
- **Auto-Scaling:** [TODO: Ja/Nein, Konfiguration]

## Verantwortlichkeiten

| Rolle | Verantwortung | Person | Kontakt |
|---|---|---|---|
| **Service Owner** | Gesamtverantwortung | [TODO] | [TODO: E-Mail] |
| **Technical Lead** | Technische Umsetzung | [TODO: Name] | [TODO: E-Mail] |
| **Operations Manager** | Täglicher Betrieb | {{ meta-organisation-roles.role_IT_Operations_Manager }} | {{ meta-organisation-roles.role_IT_Operations_Manager_email }} |
| **Service Desk Lead** | First-Level-Support | {{ meta-organisation-roles.role_Service_Desk_Lead }} | {{ meta-organisation-roles.role_Service_Desk_Lead_email }} |

## Kontakte und Eskalation

**Bei Fragen zum Service:**
- **Service Owner:** [TODO]
- **IT Operations Manager:** {{ meta-organisation-roles.role_IT_Operations_Manager }} ({{ meta-organisation-roles.role_IT_Operations_Manager_email }})
- **Service Desk:** {{ meta-organisation-roles.role_Service_Desk_Lead }} ({{ meta-organisation-roles.role_Service_Desk_Lead_email }})

**Eskalationspfad:**
1. **Level 1:** Service Desk - {{ meta-organisation-roles.role_Service_Desk_Lead_email }}
2. **Level 2:** IT Operations - {{ meta-organisation-roles.role_IT_Operations_Manager_email }}
3. **Level 3:** CIO - {{ meta-organisation-roles.role_CIO_email }}

**Service Owner:** [TODO]  
**Genehmigt durch:** [TODO]  
**Version:** 0  
**Organisation:** AdminSend GmbH

