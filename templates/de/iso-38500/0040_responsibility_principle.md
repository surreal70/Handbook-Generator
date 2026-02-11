---
Document-ID: iso-38500-0040
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Prinzip 1: Verantwortung (Responsibility)

## Zweck

Dieses Dokument beschreibt die Anwendung des Verantwortungs-Prinzips in der IT-Governance der Organisation.

## Geltungsbereich

Dieses Dokument gilt für:
- {{ meta.organization }}
- Alle IT-bezogenen Verantwortlichkeiten
- Vorstand, Geschäftsführung, IT-Management und Mitarbeiter

## Prinzip-Definition

Einzelpersonen und Gruppen innerhalb der Organisation verstehen und akzeptieren ihre Verantwortlichkeiten in Bezug auf Angebot und Nachfrage von IT. Diejenigen mit Verantwortung haben die Autorität, diese zu erfüllen.

## Evaluate (Bewerten)

### Bewertung der Verantwortlichkeiten

- Sind IT-Verantwortlichkeiten klar definiert und dokumentiert?
- Verstehen alle Beteiligten ihre IT-Verantwortlichkeiten?
- Haben Verantwortliche die notwendige Autorität?
- Gibt es Lücken oder Überschneidungen in Verantwortlichkeiten?

### Bewertungskriterien

| Kriterium | Ziel | Aktueller Status |
|-----------|------|------------------|
| Klarheit der Verantwortlichkeiten | 100% dokumentiert | {{ meta.responsibility_clarity }}% |
| Autoritätsübereinstimmung | 100% | {{ meta.authority_alignment }}% |
| Verantwortungsbewusstsein | >90% | {{ meta.responsibility_awareness }}% |

## Direct (Steuern)

### Verantwortlichkeitszuweisung

**Vorstand:**
- Gesamtverantwortung für IT-Governance
- Genehmigung der IT-Strategie
- Überwachung der IT-Leistung
- Risikotoleranz festlegen

**Geschäftsführung:**
- Umsetzung der IT-Strategie
- Ressourcenzuweisung
- IT-Investitionsentscheidungen
- Eskalationsmanagement

**{{ meta.cio }}:**
- IT-Betrieb und -Services
- IT-Sicherheit und Compliance
- IT-Projektportfolio
- Lieferantenmanagement

**IT-Management:**
- Tägliche IT-Operationen
- Service Delivery
- Technische Implementierung
- Incident Management

**Mitarbeiter:**
- Verantwortungsvolle IT-Nutzung
- Einhaltung von IT-Richtlinien
- Meldung von Vorfällen
- Datenschutz

### RACI-Matrix

| Aktivität | Vorstand | Geschäftsführung | CIO | IT-Management | Mitarbeiter |
|-----------|----------|------------------|-----|---------------|-------------|
| IT-Strategie | A | R | C | I | I |
| IT-Investitionen | A | R | C | I | - |
| IT-Betrieb | I | C | A | R | I |
| IT-Sicherheit | I | C | A | R | C |
| IT-Nutzung | I | I | C | C | R |

*R=Responsible, A=Accountable, C=Consulted, I=Informed*

## Monitor (Überwachen)

### Überwachungsmaßnahmen

1. **Regelmäßige Reviews**: Quartalsweise Überprüfung der Verantwortlichkeiten
2. **Leistungsbewertung**: Bewertung der Verantwortungserfüllung
3. **Feedback-Mechanismen**: Rückmeldungen zu Verantwortlichkeiten sammeln
4. **Anpassungen**: Verantwortlichkeiten bei Bedarf anpassen

### KPIs

- Anteil klar definierter Verantwortlichkeiten: {{ meta.defined_responsibilities }}%
- Verantwortungsbewusstsein (Umfrage): {{ meta.responsibility_score }}/10
- Anzahl Verantwortlichkeitskonflikte: {{ meta.responsibility_conflicts }}
- Zeit zur Konfliktlösung: {{ meta.conflict_resolution_time }} Tage

## Umsetzung

### Maßnahmen

1. Erstellung einer Verantwortlichkeitsmatrix
2. Kommunikation an alle Beteiligten
3. Schulungen zu Verantwortlichkeiten
4. Regelmäßige Überprüfung und Aktualisierung

### Zeitplan

| Maßnahme | Verantwortlich | Frist |
|----------|----------------|-------|
| Verantwortlichkeitsmatrix erstellen | {{ meta.cio }} | {{ meta.responsibility_matrix_date }} |
| Kommunikation | HR & IT | {{ meta.communication_date }} |
| Schulungen | IT-Training | {{ meta.training_date }} |
| Erste Überprüfung | Governance-Komitee | {{ meta.first_review_date }} |

## Dokumentenverweise

- 0010_governance_framework.md
- 0020_governance_model.md
- 0200_governance_roles.md

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | {{ meta.date }} | {{ meta.author }} | Initiale Erstellung |

<!-- 
Autor-Hinweise: 
- Verantwortlichkeiten müssen mit Autorität einhergehen
- Dokumentieren Sie Eskalationswege bei Verantwortlichkeitskonflikten
-->

