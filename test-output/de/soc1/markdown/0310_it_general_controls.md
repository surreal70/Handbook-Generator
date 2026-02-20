
Document-ID: soc1-0310

Status: Draft
Classification: Internal

# IT General Controls (ITGC)

**Dokument-ID:** [FRAMEWORK]-0310
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

[TODO]

**Passwortrichtlinien**:
- Mindestlänge: [TODO]
- Komplexitätsanforderungen: [TODO]
- Ablaufzeitraum: [TODO]
- Wiederverwendungseinschränkungen: [TODO]
- Kontosperrung: [TODO]

[TODO]

**Autorisierung**:
- Rollenbasierte Zugriffskontrolle (RBAC)
- Prinzip der geringsten Privilegien
- Funktionentrennung
- Zugriffsgenehmigungsprozess

[TODO]

### Privilegierte Zugriffsverwaltung

**Privilegierte Konten**:
- Administratorkonten
- Systemkonten
- Servicekonten
- Notfallzugangskonten

[TODO]

**Verwaltung privilegierter Zugriffe**:
- Privileged Access Management (PAM) System
- Just-in-Time (JIT) Zugriff
- Sitzungsaufzeichnung
- Aktivitätsüberwachung

[TODO]

**Überwachung privilegierter Aktivitäten**:
[TODO]

### Benutzerzugangsverwaltung

**Zugangsprovisionierung**:
- Zugangsan Anforderungsprozess
- Genehmigungsworkflow
- Provisionierungsverfahren
- Dokumentation

[TODO]

**Zugangsänderungen**:
- Änderungsanforderungen
- Genehmigungsprozess
- Implementierung
- Überprüfung

[TODO]

**Zugangsentfernung**:
- Kündigungsprozess
- Sofortige Deaktivierung
- Zugangsüberprüfung
- Dokumentation

[TODO]

### Zugangsüberprüfungen

**Periodische Überprüfungen**:
- Frequenz: [TODO]
- Geltungsbereich: [TODO]
- Verantwortlichkeiten: [TODO]
- Dokumentation: [TODO]

[TODO]

**Überprüfungsprozess**:
1. Zugangsberichte generieren
2. Überprüfung durch Datenverantwortliche
3. Identifikation unangemessener Zugriffe
4. Behebung
5. Dokumentation

[TODO]

## Änderungsmanagement

### Änderungsmanagement-Prozess

**Änderungsarten**:
- Standard-Änderungen
- Normale Änderungen
- Notfall-Änderungen

[TODO]

**Änderungsworkflow**:
1. Änderungsantrag
2. Bewertung und Genehmigung
3. Planung und Testing
4. Implementierung
5. Überprüfung und Abschluss

[TODO]

### Änderungsanträge

**Antragsformular**: [TODO]

**Erforderliche Informationen**:
- Änderungsbeschreibung
- Geschäftsbegründung
- Auswirkungsanalyse
- Risikobewertung
- Rollback-Plan
- Testplan

[TODO]

### Änderungsbewertung und -genehmigung

**Change Advisory Board (CAB)**:
- Zusammensetzung: [TODO]
- Sitzungsfrequenz: [TODO]
- Verantwortlichkeiten: [TODO]

[TODO]

**Genehmigungskriterien**:
- Geschäftswert
- Risikobewertung
- Ressourcenverfügbarkeit
- Zeitplanung
- Abhängigkeiten

[TODO]

**Notfall-Änderungen**: [TODO]

### Testing und Implementierung

**Testumgebungen**:
- Entwicklung
- Test/QA
- Staging
- Produktion

[TODO]

**Testanforderungen**:
- Unit-Tests
- Integrationstests
- Regressionstests
- User Acceptance Testing (UAT)

[TODO]

**Implementierungsverfahren**:
[TODO]

**Rollback-Verfahren**:
[TODO]

### Änderungsdokumentation

**Erforderliche Dokumentation**:
- Änderungsanträge
- Genehmigungen
- Testprotokolle
- Implementierungsprotokolle
- Post-Implementation Reviews

[TODO]

**Aufbewahrung**: [TODO]

## Backup und Wiederherstellung

### Backup-Strategie

**Backup-Typen**:
- Vollständige Backups
- Inkrementelle Backups
- Differentielle Backups

[TODO]

**Backup-Zeitplan**:
[TODO]

**Backup-Aufbewahrung**:
[TODO]

### Backup-Verfahren

**Backup-Prozess**:
1. Backup-Job-Scheduling
2. Backup-Ausführung
3. Verifizierung
4. Offsite-Speicherung
5. Überwachung und Berichterstattung

[TODO]

**Backup-Überwachung**:
[TODO]

**Backup-Fehlerbehandlung**:
[TODO]

### Wiederherstellungsverfahren

**Wiederherstellungsprozess**:
[TODO]

**Recovery Time Objective (RTO)**: [TODO]

**Recovery Point Objective (RPO)**: [TODO]

### Wiederherstellungstests

**Testfrequenz**: [TODO]

**Testszenarien**:
- Dateiwiederherstellung
- Datenbankwiederherstellung
- Systemwiederherstellung
- Disaster Recovery

[TODO]

**Testdokumentation**: [TODO]

## IT-Betriebskontrollen

### Job-Scheduling und -Überwachung

**Batch-Job-Management**:
- Job-Scheduling
- Job-Abhängigkeiten
- Job-Überwachung
- Fehlerbehandlung

[TODO]

**Überwachungstools**: [TODO]

**Alarmierung**: [TODO]

### Incident Management

**Incident-Kategorien**:
- Kritisch
- Hoch
- Mittel
- Niedrig

[TODO]

**Incident-Prozess**:
1. Erkennung und Aufzeichnung
2. Kategorisierung und Priorisierung
3. Untersuchung und Diagnose
4. Lösung und Wiederherstellung
5. Abschluss und Dokumentation

[TODO]

**Eskalationsverfahren**: [TODO]

### Problem Management

**Problem-Identifikation**: [TODO]

**Root Cause Analysis**: [TODO]

**Problem-Lösung**: [TODO]

**Known Error Database**: [TODO]

### Kapazitätsmanagement

**Kapazitätsplanung**: [TODO]

**Leistungsüberwachung**: [TODO]

**Kapazitätsprognosen**: [TODO]

## Systemakquisition und -entwicklung

### System Development Life Cycle (SDLC)

**SDLC-Phasen**:
1. Anforderungsanalyse
2. Design
3. Entwicklung
4. Testing
5. Implementierung
6. Wartung

[TODO]

**SDLC-Methodik**: [TODO]

### Anforderungsmanagement

**Anforderungsdefinition**: [TODO]

**Anforderungsverfolgung**: [TODO]

**Änderungsmanagement**: [TODO]

### Entwicklungskontrollen

**Code-Entwicklungsstandards**: [TODO]

**Code-Reviews**: [TODO]

**Versionskontrolle**: [TODO]

**Funktionentrennung**: [TODO]

### Testing

**Teststrategie**: [TODO]

**Testarten**:
- Unit-Tests
- Integrationstests
- Systemtests
- Akzeptanztests
- Sicherheitstests

[TODO]

**Testdokumentation**: [TODO]

## Physische und Umgebungskontrollen

### Rechenzentrum-Sicherheit

**Physische Zugangskontrollen**:
- Zutrittskontrollsysteme
- Biometrische Authentifizierung
- Besucherverwaltung
- Überwachungskameras

[TODO]

**Umgebungskontrollen**:
- Klimatisierung
- Brandschutz
- Stromversorgung (USV)
- Überwachung

[TODO]

### Geräte- und Mediensicherheit

**Geräteverwaltung**: [TODO]

**Medienverwaltung**: [TODO]

**Sichere Entsorgung**: [TODO]

## Überwachung und Berichterstattung

### ITGC-Überwachung

**Überwachungsaktivitäten**:
- Automatisierte Überwachung
- Manuelle Überprüfungen
- Interne Audits
- Externe Audits

[TODO]

**Key Performance Indicators (KPIs)**:
[TODO]

### Berichterstattung

**Interne Berichte**: [TODO]

**Management-Berichte**: [TODO]

**Audit-Berichte**: [TODO]

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

[TODO]

### Aufbewahrungsfristen

[TODO]

## Referenzen

- COBIT 2019 Framework
- ITIL v4
- ISO/IEC 27001:2022
- NIST SP 800-53
- CIS Controls
- AICPA Trust Services Criteria



