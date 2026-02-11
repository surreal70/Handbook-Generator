---
Document-ID: soc1-0450
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Testverfahren

## Zweck

Dieses Dokument beschreibt die Testverfahren für die Bewertung der Betriebswirksamkeit der Kontrollen (SOC 1 Type II).

## Geltungsbereich

- Testplanung
- Testmethoden
- Stichprobenauswahl
- Testdokumentation
- Testergebnisse

## Testplanung

### Testumfang

**Kontrollziele**: {{ source.test_scope_objectives }}
**Testzeitraum**: {{ source.test_period }}
**Testfrequenz**: {{ source.test_frequency }}

### Testverantwortlichkeiten

**Service Auditor**: {{ source.auditor_test_responsibilities }}
**Serviceorganisation**: {{ source.service_org_test_responsibilities }}

## Testmethoden

### Inspektion

**Beschreibung**: Prüfung von Aufzeichnungen, Dokumenten oder physischen Vermögenswerten.

**Anwendung**: {{ source.inspection_application }}

**Beispiele**:
- Prüfung von Genehmigungsdokumenten
- Überprüfung von Systemkonfigurationen
- Inspektion von Zugangsprotokollen

### Beobachtung

**Beschreibung**: Beobachtung der Ausführung einer Kontrolle durch Mitarbeiter.

**Anwendung**: {{ source.observation_application }}

**Beispiele**:
- Beobachtung von Zugangskontrollen
- Beobachtung von Backup-Verfahren
- Beobachtung von Genehmigungsprozessen

### Befragung

**Beschreibung**: Befragung von Mitarbeitern über die Ausführung von Kontrollen.

**Anwendung**: {{ source.inquiry_application }}

**Beispiele**:
- Befragung zu Kontrollverfahren
- Befragung zu Ausnahmebehandlung
- Befragung zu Eskalationsprozessen

### Wiederholung

**Beschreibung**: Unabhängige Ausführung der Kontrolle durch den Prüfer.

**Anwendung**: {{ source.reperformance_application }}

**Beispiele**:
- Wiederholung von Berechnungen
- Wiederholung von Abstimmungen
- Wiederholung von Zugriffsprüfungen

## Stichprobenauswahl

### Stichprobenmethoden

**Statistische Stichproben**: {{ source.statistical_sampling }}
**Nicht-statistische Stichproben**: {{ source.non_statistical_sampling }}

### Stichprobenumfang

**Faktoren**:
- Kontrollfrequenz
- Risikobewertung
- Komplexität der Kontrolle
- Automatisierungsgrad

**Stichprobengrößen**:
{{ source.sample_sizes }}

### Stichprobenauswahl

{{ source.sample_selection }}

## Testdokumentation

### Testarbeitsblätter

**Inhalt**:
- Kontrollbeschreibung
- Testverfahren
- Stichprobenauswahl
- Testergebnisse
- Abweichungen
- Schlussfolgerungen

**Vorlage**: {{ source.test_worksheet_template }}

### Nachweisdokumentation

{{ source.evidence_documentation }}

### Aufbewahrung

{{ source.test_documentation_retention }}

## Testergebnisse

### Bewertung der Ergebnisse

**Erfolgskriterien**: {{ source.test_success_criteria }}
**Abweichungsbewertung**: {{ source.deviation_assessment }}

### Klassifizierung von Abweichungen

**Keine Abweichung**: Kontrolle funktioniert wie entworfen
**Geringfügige Abweichung**: {{ source.minor_deviation }}
**Wesentliche Abweichung**: {{ source.material_deviation }}

### Testergebnismatrix

| Kontrolle | Testverfahren | Stichprobe | Ergebnis | Abweichungen | Bewertung |
|-----------|---------------|------------|----------|--------------|-----------|
| {{ source.test_results_matrix_rows }} |

## Ausnahmebehandlung

### Identifikation von Ausnahmen

{{ source.exception_identification }}

### Untersuchung von Ausnahmen

{{ source.exception_investigation }}

### Dokumentation von Ausnahmen

{{ source.exception_documentation }}

## Berichterstattung

### Testberichte

**Inhalt**:
- Zusammenfassung der Tests
- Testergebnisse
- Identifizierte Abweichungen
- Auswirkungen auf Kontrollziele
- Empfehlungen

### Kommunikation mit Management

{{ source.test_results_communication }}

### Kommunikation mit Service Auditor

{{ source.auditor_test_communication }}

## Qualitätssicherung

### Review-Prozess

{{ source.test_quality_review }}

### Unabhängige Überprüfung

{{ source.independent_test_review }}

## Referenzen

- SSAE 18 Testing Requirements
- SOC 1 Reporting Guide - Testing Procedures
- Audit Sampling Guide (AICPA)

<!-- Hinweise für Autoren: Dokumentieren Sie alle Testverfahren detailliert und nachvollziehbar -->

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |

<!-- Ende des Templates -->
