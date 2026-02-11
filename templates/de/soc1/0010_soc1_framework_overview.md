---
Document-ID: soc1-0010
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# SOC 1 Framework Übersicht

## Zweck

Dieses Dokument bietet einen Überblick über das SOC 1 / SSAE 18 Framework und dessen Anwendung in der Serviceorganisation {{ source.organization_name }}.

## Geltungsbereich

Dieses Dokument beschreibt:
- SOC 1 Type II Berichtsanforderungen
- SSAE 18 Attestierungsstandards
- COSO Internal Control Framework Integration
- Berichtszeitraum und Systemgrenzen

## SOC 1 Framework

### Überblick

SOC 1 (Service Organization Control 1) Berichte sind Attestierungsberichte über die Kontrollen einer Serviceorganisation, die für die Finanzberichterstattung der Nutzerorganisationen relevant sind.

### SSAE 18 Standard

SSAE 18 (Statement on Standards for Attestation Engagements No. 18) ist der Attestierungsstandard, der die Anforderungen für SOC 1 Berichte definiert.

**Kernelemente**:
- Management Assertion
- Service Auditor's Report
- System Description
- Control Objectives and Related Controls
- Tests of Controls and Results

### Berichtstypen

**Type I Report**:
- Beschreibung des Systems zu einem bestimmten Zeitpunkt
- Bewertung der Angemessenheit des Kontrolldesigns
- Keine Tests der Betriebswirksamkeit

**Type II Report**:
- Beschreibung des Systems über einen Zeitraum (mindestens 6 Monate)
- Bewertung der Angemessenheit des Kontrolldesigns
- Tests der Betriebswirksamkeit der Kontrollen
- Detaillierte Testergebnisse

### COSO Framework Integration

SOC 1 Berichte basieren auf dem COSO Internal Control Framework mit fünf Komponenten:

1. **Kontrollumgebung** (Control Environment)
2. **Risikobewertung** (Risk Assessment)
3. **Kontrollaktivitäten** (Control Activities)
4. **Information und Kommunikation** (Information and Communication)
5. **Überwachungsaktivitäten** (Monitoring Activities)

## Serviceorganisation

### Organisationsbeschreibung

**Name**: {{ source.organization_name }}
**Adresse**: {{ source.organization_address }}
**Kontakt**: {{ source.contact_email }}

### Bereitgestellte Services

{{ source.services_description }}

### Berichtszeitraum

**Type II Berichtszeitraum**: {{ source.reporting_period }}
**Stichtag**: {{ source.report_date }}

## Systemgrenzen

### Im Geltungsbereich

Die folgenden Systeme und Prozesse sind im Geltungsbereich des SOC 1 Berichts enthalten:

{{ source.in_scope_systems }}

### Außerhalb des Geltungsbereichs

Die folgenden Systeme und Prozesse sind nicht im Geltungsbereich:

{{ source.out_of_scope_systems }}

### Subservice-Organisationen

{{ source.subservice_organizations }}

## Kontrollziele

Die Kontrollziele für diesen SOC 1 Bericht sind:

1. {{ source.control_objective_1 }}
2. {{ source.control_objective_2 }}
3. {{ source.control_objective_3 }}
4. {{ source.control_objective_4 }}
5. {{ source.control_objective_5 }}

## Komplementäre Nutzerorganisationskontrollen

Bestimmte Kontrollziele können nur erreicht werden, wenn komplementäre Kontrollen bei den Nutzerorganisationen vorhanden sind und effektiv funktionieren.

### Erforderliche Nutzerkontrollen

{{ source.complementary_user_controls }}

## Änderungen im Berichtszeitraum

### Wesentliche Änderungen

{{ source.significant_changes }}

### Auswirkungen auf Kontrollen

{{ source.control_impacts }}

## Verantwortlichkeiten

### Management der Serviceorganisation

Das Management ist verantwortlich für:
- Design und Implementierung der Kontrollen
- Aufrechterhaltung der Kontrollwirksamkeit
- Bereitstellung der Systembeschreibung
- Management Assertion

### Service Auditor

Der Service Auditor ist verantwortlich für:
- Prüfung der Systembeschreibung
- Bewertung des Kontrolldesigns
- Tests der Betriebswirksamkeit
- Attestierungsbericht

### Nutzerorganisationen

Nutzerorganisationen sind verantwortlich für:
- Verständnis der Systembeschreibung
- Implementierung komplementärer Kontrollen
- Bewertung der Auswirkungen auf eigene Kontrollen

## Referenzen

- SSAE 18 (AT-C Section 320)
- COSO Internal Control - Integrated Framework
- SOC 1 Reporting Guide (AICPA)

<!-- Hinweise für Autoren: Passen Sie die Kontrollziele und Systemgrenzen an Ihre spezifische Serviceorganisation an -->

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |

<!-- Ende des Templates -->
