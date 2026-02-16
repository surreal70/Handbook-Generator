---
Document-ID: soc1-0310
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# IT General Controls (ITGC)

## Zweck

Dieses Dokument beschreibt die IT General Controls (ITGC) der Serviceorganisation, die die Grundlage für die Zuverlässigkeit von IT-Systemen und Anwendungskontrollen bilden.

## Geltungsbereich

Dieses Dokument umfasst:
- Zugangskontrollen
- Änderungsmanagement
- Backup und Wiederherstellung
- IT-Betriebskontrollen
- Systemakquisition und -entwicklung

## Überblick

IT General Controls sind Kontrollen, die sich auf die IT-Umgebung als Ganzes beziehen und die Grundlage für die effektive Funktionsweise von Anwendungskontrollen bilden. Effektive ITGCs sind entscheidend für die Zuverlässigkeit der Finanzberichterstattung und die Einhaltung von SOC 1-Anforderungen.

## Zugangskontrollen

### Logische Zugangskontrollen

**Benutzerauthentifizierung**:
- Eindeutige Benutzer-IDs
- Starke Passwörter
- Multi-Faktor-Authentifizierung (MFA)
- Single Sign-On (SSO)

{{ source.authentication_controls }}

**Passwortrichtlinien**:
- Mindestlänge: {{ source.password_min_length }}
- Komplexitätsanforderungen: {{ source.password_complexity }}
- Ablaufzeitraum: {{ source.password_expiry }}
- Wiederverwendungseinschränkungen: {{ source.password_reuse }}
- Kontosperrung: {{ source.account_lockout }}

{{ source.password_policy }}

**Autorisierung**:
- Rollenbasierte Zugriffskontrolle (RBAC)
- Prinzip der geringsten Privilegien
- Funktionentrennung
- Zugriffsgenehmigungsprozess

{{ source.authorization_controls }}

### Privilegierte Zugriffsverwaltung

**Privilegierte Konten**:
- Administratorkonten
- Systemkonten
- Servicekonten
- Notfallzugangskonten

{{ source.privileged_accounts }}

**Verwaltung privilegierter Zugriffe**:
- Privileged Access Management (PAM) System
- Just-in-Time (JIT) Zugriff
- Sitzungsaufzeichnung
- Aktivitätsüberwachung

{{ source.pam_controls }}

**Überwachung privilegierter Aktivitäten**:
{{ source.privileged_activity_monitoring }}

### Benutzerzugangsverwaltung

**Zugangsprovisionierung**:
- Zugangsan Anforderungsprozess
- Genehmigungsworkflow
- Provisionierungsverfahren
- Dokumentation

{{ source.access_provisioning }}

**Zugangsänderungen**:
- Änderungsanforderungen
- Genehmigungsprozess
- Implementierung
- Überprüfung

{{ source.access_changes }}

**Zugangsentfernung**:
- Kündigungsprozess
- Sofortige Deaktivierung
- Zugangsüberprüfung
- Dokumentation

{{ source.access_removal }}

### Zugangsüberprüfungen

**Periodische Überprüfungen**:
- Frequenz: {{ source.access_review_frequency }}
- Geltungsbereich: {{ source.access_review_scope }}
- Verantwortlichkeiten: {{ source.access_review_responsibilities }}
- Dokumentation: {{ source.access_review_documentation }}

{{ source.access_reviews }}

**Überprüfungsprozess**:
1. Zugangsberichte generieren
2. Überprüfung durch Datenverantwortliche
3. Identifikation unangemessener Zugriffe
4. Behebung
5. Dokumentation

{{ source.review_process }}

## Änderungsmanagement

### Änderungsmanagement-Prozess

**Änderungsarten**:
- Standard-Änderungen
- Normale Änderungen
- Notfall-Änderungen

{{ source.change_types }}

**Änderungsworkflow**:
1. Änderungsantrag
2. Bewertung und Genehmigung
3. Planung und Testing
4. Implementierung
5. Überprüfung und Abschluss

{{ source.change_workflow }}

### Änderungsanträge

**Antragsformular**: {{ source.change_request_form }}

**Erforderliche Informationen**:
- Änderungsbeschreibung
- Geschäftsbegründung
- Auswirkungsanalyse
- Risikobewertung
- Rollback-Plan
- Testplan

{{ source.change_request_info }}

### Änderungsbewertung und -genehmigung

**Change Advisory Board (CAB)**:
- Zusammensetzung: {{ source.cab_composition }}
- Sitzungsfrequenz: {{ source.cab_frequency }}
- Verantwortlichkeiten: {{ source.cab_responsibilities }}

{{ source.cab_details }}

**Genehmigungskriterien**:
- Geschäftswert
- Risikobewertung
- Ressourcenverfügbarkeit
- Zeitplanung
- Abhängigkeiten

{{ source.approval_criteria }}

**Notfall-Änderungen**: {{ source.emergency_changes }}

### Testing und Implementierung

**Testumgebungen**:
- Entwicklung
- Test/QA
- Staging
- Produktion

{{ source.test_environments }}

**Testanforderungen**:
- Unit-Tests
- Integrationstests
- Regressionstests
- User Acceptance Testing (UAT)

{{ source.testing_requirements }}

**Implementierungsverfahren**:
{{ source.implementation_procedures }}

**Rollback-Verfahren**:
{{ source.rollback_procedures }}

### Änderungsdokumentation

**Erforderliche Dokumentation**:
- Änderungsanträge
- Genehmigungen
- Testprotokolle
- Implementierungsprotokolle
- Post-Implementation Reviews

{{ source.change_documentation }}

**Aufbewahrung**: {{ source.change_retention }}

## Backup und Wiederherstellung

### Backup-Strategie

**Backup-Typen**:
- Vollständige Backups
- Inkrementelle Backups
- Differentielle Backups

{{ source.backup_types }}

**Backup-Zeitplan**:
{{ source.backup_schedule }}

**Backup-Aufbewahrung**:
{{ source.backup_retention }}

### Backup-Verfahren

**Backup-Prozess**:
1. Backup-Job-Scheduling
2. Backup-Ausführung
3. Verifizierung
4. Offsite-Speicherung
5. Überwachung und Berichterstattung

{{ source.backup_procedures }}

**Backup-Überwachung**:
{{ source.backup_monitoring }}

**Backup-Fehlerbehandlung**:
{{ source.backup_error_handling }}

### Wiederherstellungsverfahren

**Wiederherstellungsprozess**:
{{ source.recovery_procedures }}

**Recovery Time Objective (RTO)**: {{ source.rto }}

**Recovery Point Objective (RPO)**: {{ source.rpo }}

### Wiederherstellungstests

**Testfrequenz**: {{ source.recovery_test_frequency }}

**Testszenarien**:
- Dateiwiederherstellung
- Datenbankwiederherstellung
- Systemwiederherstellung
- Disaster Recovery

{{ source.recovery_test_scenarios }}

**Testdokumentation**: {{ source.recovery_test_documentation }}

## IT-Betriebskontrollen

### Job-Scheduling und -Überwachung

**Batch-Job-Management**:
- Job-Scheduling
- Job-Abhängigkeiten
- Job-Überwachung
- Fehlerbehandlung

{{ source.batch_job_management }}

**Überwachungstools**: {{ source.monitoring_tools }}

**Alarmierung**: {{ source.alerting }}

### Incident Management

**Incident-Kategorien**:
- Kritisch
- Hoch
- Mittel
- Niedrig

{{ source.incident_categories }}

**Incident-Prozess**:
1. Erkennung und Aufzeichnung
2. Kategorisierung und Priorisierung
3. Untersuchung und Diagnose
4. Lösung und Wiederherstellung
5. Abschluss und Dokumentation

{{ source.incident_process }}

**Eskalationsverfahren**: {{ source.escalation_procedures }}

### Problem Management

**Problem-Identifikation**: {{ source.problem_identification }}

**Root Cause Analysis**: {{ source.root_cause_analysis }}

**Problem-Lösung**: {{ source.problem_resolution }}

**Known Error Database**: {{ source.known_error_database }}

### Kapazitätsmanagement

**Kapazitätsplanung**: {{ source.capacity_planning }}

**Leistungsüberwachung**: {{ source.performance_monitoring }}

**Kapazitätsprognosen**: {{ source.capacity_forecasting }}

## Systemakquisition und -entwicklung

### System Development Life Cycle (SDLC)

**SDLC-Phasen**:
1. Anforderungsanalyse
2. Design
3. Entwicklung
4. Testing
5. Implementierung
6. Wartung

{{ source.sdlc_phases }}

**SDLC-Methodik**: {{ source.sdlc_methodology }}

### Anforderungsmanagement

**Anforderungsdefinition**: {{ source.requirements_definition }}

**Anforderungsverfolgung**: {{ source.requirements_traceability }}

**Änderungsmanagement**: {{ source.requirements_change_management }}

### Entwicklungskontrollen

**Code-Entwicklungsstandards**: {{ source.coding_standards }}

**Code-Reviews**: {{ source.code_reviews }}

**Versionskontrolle**: {{ source.version_control }}

**Funktionentrennung**: {{ source.development_segregation }}

### Testing

**Teststrategie**: {{ source.test_strategy }}

**Testarten**:
- Unit-Tests
- Integrationstests
- Systemtests
- Akzeptanztests
- Sicherheitstests

{{ source.test_types }}

**Testdokumentation**: {{ source.test_documentation }}

## Physische und Umgebungskontrollen

### Rechenzentrum-Sicherheit

**Physische Zugangskontrollen**:
- Zutrittskontrollsysteme
- Biometrische Authentifizierung
- Besucherverwaltung
- Überwachungskameras

{{ source.physical_access }}

**Umgebungskontrollen**:
- Klimatisierung
- Brandschutz
- Stromversorgung (USV)
- Überwachung

{{ source.environmental_controls }}

### Geräte- und Mediensicherheit

**Geräteverwaltung**: {{ source.equipment_management }}

**Medienverwaltung**: {{ source.media_management }}

**Sichere Entsorgung**: {{ source.secure_disposal }}

## Überwachung und Berichterstattung

### ITGC-Überwachung

**Überwachungsaktivitäten**:
- Automatisierte Überwachung
- Manuelle Überprüfungen
- Interne Audits
- Externe Audits

{{ source.itgc_monitoring }}

**Key Performance Indicators (KPIs)**:
{{ source.itgc_kpis }}

### Berichterstattung

**Interne Berichte**: {{ source.internal_reporting }}

**Management-Berichte**: {{ source.management_reporting }}

**Audit-Berichte**: {{ source.audit_reporting }}

## Dokumentation und Nachweise

### Erforderliche Dokumentation

1. **Richtlinien und Verfahren**:
   - Zugangskontrollrichtlinie
   - Änderungsmanagement-Verfahren
   - Backup-Verfahren
   - Incident-Management-Verfahren

2. **Nachweise**:
   - Zugangsüberprüfungen
   - Änderungsprotokolle
   - Backup-Protokolle
   - Wiederherstellungstests
   - Incident-Tickets

{{ source.required_documentation }}

### Aufbewahrungsfristen

{{ source.retention_requirements }}

## Referenzen

- COBIT 2019 Framework
- ITIL v4
- ISO/IEC 27001:2022
- NIST SP 800-53
- CIS Controls
- AICPA Trust Services Criteria

<!-- Hinweise für Autoren: Aktualisieren Sie ITGC-Dokumentation bei Systemänderungen -->

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |

<!-- Ende des Templates -->
