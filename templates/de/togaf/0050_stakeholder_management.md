---
Document-ID: togaf-0050
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Stakeholder-Management

## Zweck

Dieses Dokument definiert den Ansatz für Stakeholder-Management im Architecture-Prozess von {{ source.organization_name }}. Es identifiziert wichtige Stakeholder, ihre Anliegen und Strategien für effektives Engagement.

## Geltungsbereich

Dieses Dokument umfasst:
- Stakeholder-Identifikation und -Analyse
- Stakeholder-Anliegen und -Anforderungen
- Kommunikationsstrategien
- Engagement-Pläne
- Stakeholder-Management-Prozesse

## Stakeholder-Identifikation

### Stakeholder-Kategorien

| Kategorie | Beschreibung | Beispiele |
|-----------|--------------|-----------|
| Executive Leadership | C-Level und Senior Management | {{ source.executive_stakeholders }} |
| Business Units | Geschäftsbereiche und Abteilungen | {{ source.business_stakeholders }} |
| IT Organization | IT-Führung und -Teams | {{ source.it_stakeholders }} |
| External Partners | Lieferanten und Partner | {{ source.external_stakeholders }} |
| Regulators | Aufsichtsbehörden | {{ source.regulatory_stakeholders }} |

### Stakeholder-Register

| Stakeholder | Rolle | Organisation | Einfluss | Interesse | Kontakt |
|-------------|-------|--------------|----------|-----------|---------|
| {{ source.stakeholder_1_name }} | {{ source.stakeholder_1_role }} | {{ source.stakeholder_1_org }} | {{ source.stakeholder_1_influence }} | {{ source.stakeholder_1_interest }} | {{ source.stakeholder_1_contact }} |
| {{ source.stakeholder_2_name }} | {{ source.stakeholder_2_role }} | {{ source.stakeholder_2_org }} | {{ source.stakeholder_2_influence }} | {{ source.stakeholder_2_interest }} | {{ source.stakeholder_2_contact }} |
| {{ source.stakeholder_3_name }} | {{ source.stakeholder_3_role }} | {{ source.stakeholder_3_org }} | {{ source.stakeholder_3_influence }} | {{ source.stakeholder_3_interest }} | {{ source.stakeholder_3_contact }} |

## Stakeholder-Analyse

### Einfluss-Interesse-Matrix

```
Hoch │ Eng managen        │ Zufriedenstellen
     │                    │
E    │                    │
i    │                    │
n    │                    │
f    │                    │
l    │                    │
u    │                    │
s    │                    │
s    │                    │
     │ Beobachten         │ Informiert halten
Niedrig │                    │
     └────────────────────┴──────────────────
       Niedrig              Hoch
                Interesse
```

### Stakeholder-Anliegen

| Stakeholder | Primäre Anliegen | Erwartungen | Risiken |
|-------------|------------------|-------------|---------|
| CEO | {{ source.ceo_concerns }} | {{ source.ceo_expectations }} | {{ source.ceo_risks }} |
| CIO | {{ source.cio_concerns }} | {{ source.cio_expectations }} | {{ source.cio_risks }} |
| Business Leaders | {{ source.business_concerns }} | {{ source.business_expectations }} | {{ source.business_risks }} |
| IT Teams | {{ source.it_concerns }} | {{ source.it_expectations }} | {{ source.it_risks }} |

## Kommunikationsstrategie

### Kommunikationskanäle

| Kanal | Zweck | Zielgruppe | Häufigkeit |
|-------|-------|------------|------------|
| Architecture Board Meetings | Strategische Entscheidungen | Executive Leadership | {{ source.board_frequency }} |
| Architecture Reviews | Technische Reviews | Projektteams, Architects | {{ source.review_frequency }} |
| Town Halls | Breite Kommunikation | Alle Mitarbeiter | {{ source.townhall_frequency }} |
| Newsletter | Updates und Highlights | IT Organisation | {{ source.newsletter_frequency }} |
| Workshops | Kollaborative Planung | Stakeholder-Gruppen | {{ source.workshop_frequency }} |

### Kommunikationsplan

| Stakeholder-Gruppe | Botschaft | Medium | Häufigkeit | Verantwortlich |
|-------------------|-----------|--------|------------|----------------|
| Executive Leadership | Strategische Ausrichtung, ROI | {{ source.exec_medium }} | {{ source.exec_frequency }} | Chief Architect |
| Business Units | Business Value, Roadmap | {{ source.business_medium }} | {{ source.business_frequency }} | Domain Architects |
| IT Teams | Technische Standards, Guidance | {{ source.it_medium }} | {{ source.it_frequency }} | Technical Leads |
| Project Teams | Architecture-Anforderungen | {{ source.project_medium }} | {{ source.project_frequency }} | Domain Architects |

## Engagement-Strategien

### Engagement-Ansätze nach Stakeholder-Typ

**Executive Leadership**:
- Fokus auf Business Value und strategische Ausrichtung
- Hochrangige Visualisierungen und Dashboards
- Kurze, prägnante Updates
- Einbindung in wichtige Entscheidungen

**Business Units**:
- Demonstration von Business-Nutzen
- Einbindung in Architecture Vision und Roadmap
- Regelmäßige Feedback-Sitzungen
- Gemeinsame Priorisierung

**IT Organization**:
- Technische Details und Standards
- Hands-on Workshops und Training
- Kollaborative Design-Sitzungen
- Regelmäßige technische Updates

**External Partners**:
- Klare Schnittstellen-Definitionen
- Gemeinsame Governance
- Regelmäßige Abstimmungsmeetings
- Dokumentierte Integrationsmuster

## Stakeholder-Management-Prozesse

### Stakeholder-Onboarding

Neue Stakeholder werden eingebunden durch:
1. Einführung in Architecture-Funktion und -Prozesse
2. Überblick über aktuelle Architecture-Initiativen
3. Klärung von Rollen und Erwartungen
4. Zugang zu Architecture Repository und Werkzeugen

### Feedback-Management

Stakeholder-Feedback wird gesammelt durch:
- Regelmäßige Umfragen
- Feedback-Sitzungen nach Reviews
- Offene Sprechstunden
- Retrospektiven nach Projekten

### Konfliktlösung

Bei Stakeholder-Konflikten:
1. Identifikation der zugrunde liegenden Anliegen
2. Facilitation von Diskussionen
3. Suche nach Win-Win-Lösungen
4. Eskalation an Architecture Board bei Bedarf
5. Dokumentation von Entscheidungen und Begründungen

## Stakeholder-Metriken

### Engagement-Metriken

| Metrik | Ziel | Aktuell | Trend |
|--------|------|---------|-------|
| Stakeholder-Zufriedenheit | {{ source.satisfaction_target }} | {{ source.satisfaction_current }} | {{ source.satisfaction_trend }} |
| Meeting-Teilnahme | {{ source.attendance_target }} | {{ source.attendance_current }} | {{ source.attendance_trend }} |
| Feedback-Response-Rate | {{ source.feedback_target }} | {{ source.feedback_current }} | {{ source.feedback_trend }} |
| Architecture-Awareness | {{ source.awareness_target }} | {{ source.awareness_current }} | {{ source.awareness_trend }} |

## Kontinuierliche Verbesserung

Das Stakeholder-Management wird verbessert durch:
- Regelmäßige Bewertung der Engagement-Effektivität
- Anpassung der Kommunikationsstrategien basierend auf Feedback
- Identifikation neuer Stakeholder bei organisatorischen Änderungen
- Lessons Learned aus Projekten und Initiativen

<!-- Autorenhinweise: Passen Sie Stakeholder-Management-Ansätze an die Kultur Ihrer Organisation an -->

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial creation |

<-  ( marked all subtasks complete End of template -->
