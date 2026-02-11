---
Document-ID: tisax-0030
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Organisation der Informationssicherheit

## Zweck

Dieses Dokument beschreibt die organisatorische Struktur für Informationssicherheit bei {{ source.organization_name }}.

## Geltungsbereich

Dieses Dokument gilt für alle Organisationseinheiten und Rollen im Zusammenhang mit Informationssicherheit.

## Organisationsstruktur

### Informationssicherheitskomitee

**Vorsitz**: {{ source.security_committee_chair }}
**Mitglieder**:
- {{ source.committee_member_1 }}
- {{ source.committee_member_2 }}
- {{ source.committee_member_3 }}

**Aufgaben**:
- Strategische Ausrichtung der Informationssicherheit
- Genehmigung von Sicherheitsrichtlinien
- Überwachung der Sicherheitslage

### Informationssicherheitsbeauftragter (ISB)

**Name**: {{ source.information_security_officer }}
**Verantwortlichkeiten**:
- Entwicklung und Pflege des ISMS
- Koordination von Sicherheitsmaßnahmen
- Risikomanagement
- Incident Response Koordination
- TISAX-Koordination

### Datenschutzbeauftragter (DSB)

**Name**: {{ source.data_protection_officer }}
**Verantwortlichkeiten**:
- Überwachung der DSGVO-Compliance
- Beratung zu Datenschutzfragen
- Zusammenarbeit mit Aufsichtsbehörden

### Abteilungsverantwortliche

Jede Abteilung benennt einen Sicherheitsverantwortlichen:

| Abteilung | Verantwortlicher |
|-----------|------------------|
| {{ source.department_1 }} | {{ source.dept_1_security_contact }} |
| {{ source.department_2 }} | {{ source.dept_2_security_contact }} |
| {{ source.department_3 }} | {{ source.dept_3_security_contact }} |

## Kommunikationswege

### Interne Kommunikation

- Regelmäßige Sicherheitsmeetings: {{ source.security_meeting_frequency }}
- Sicherheitsberichte: {{ source.security_report_frequency }}
- Incident-Meldungen: {{ source.incident_reporting_channel }}

### Externe Kommunikation

- Kontakt zu Aufsichtsbehörden
- Kommunikation mit Kunden und Lieferanten
- Meldung von Datenschutzverletzungen

## Aufgabentrennung

Kritische Aufgaben werden getrennt, um Interessenkonflikte zu vermeiden:

- Entwicklung und Betrieb
- Genehmigung und Ausführung
- Überwachung und Durchführung

<!-- Hinweis: Passen Sie die Organisationsstruktur an Ihre Gegebenheiten an -->

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |

<!-- Ende des Templates -->
