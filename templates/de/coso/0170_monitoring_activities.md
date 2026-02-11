---
Document-ID: coso-0400
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Überwachungsaktivitäten

## Zweck

Dieses Dokument beschreibt die Überwachungsaktivitäten bei {{ source.organization_name }} gemäß COSO Framework.

## Geltungsbereich

- Laufende und separate Bewertungen (Prinzip 16)
- Bewertung und Kommunikation von Mängeln (Prinzip 17)

## Prinzip 16: Laufende und separate Bewertungen

### Laufende Überwachung

**Management-Überwachung**: {{ source.management_monitoring }}
**Operative Überwachung**: {{ source.operational_monitoring }}
**Automatisierte Kontrollen**: {{ source.automated_monitoring }}

### Separate Bewertungen

**Interne Revision**: {{ source.internal_audit }}
**Externe Prüfung**: {{ source.external_audit }}
**Selbstbewertungen**: {{ source.self_assessments }}

### Überwachungsplan

{{ source.monitoring_plan }}

## Prinzip 17: Bewertung und Kommunikation von Mängeln

### Mängelidentifikation

{{ source.deficiency_identification }}

### Mängelbewertung

**Schweregrad-Klassifizierung**:
- Kritisch: {{ source.critical_deficiency }}
- Wesentlich: {{ source.significant_deficiency }}
- Geringfügig: {{ source.minor_deficiency }}

### Eskalationsprozess

{{ source.escalation_process }}

### Berichterstattung

**An Management**: {{ source.management_reporting }}
**An Board**: {{ source.board_reporting }}
**An Aufsichtsbehörden**: {{ source.regulatory_reporting }}

## Überwachungsmethoden

### Key Control Indicators (KCI)

{{ source.key_control_indicators }}

### Kontrolltest

{{ source.control_testing }}

### Trendanalyse

{{ source.trend_analysis }}

## Abhilfemaßnahmen

### Maßnahmenplan

{{ source.remediation_plan }}

### Verfolgung

{{ source.remediation_tracking }}

### Wirksamkeitsprüfung

{{ source.effectiveness_testing }}

## Kontinuierliche Verbesserung

### Verbesserungsprozess

{{ source.improvement_process }}

### Lessons Learned

{{ source.lessons_learned_process }}

## Verantwortlichkeiten

**Erste Verteidigungslinie**: {{ source.first_line_responsibilities }}
**Zweite Verteidigungslinie**: {{ source.second_line_responsibilities }}
**Dritte Verteidigungslinie**: {{ source.third_line_responsibilities }}

## Referenzen

- Überwachungsrichtlinie {{ source.organization_name }}
- Interne Revisionsplan
- Mängelmanagement-Prozess

<!-- Hinweise für Autoren: Überwachung ist ein kontinuierlicher Prozess -->

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |

<!-- Ende des Templates -->
