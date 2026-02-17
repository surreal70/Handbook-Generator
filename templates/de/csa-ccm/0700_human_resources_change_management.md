
Document-ID: csa-ccm-0700

Status: Draft
Classification: Internal

# Personalwesen und Änderungsmanagement

**Dokument-ID:** [FRAMEWORK]-0700
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Genehmigt durch:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Klassifizierung:** {{ meta-handbook.classification }}
**Letzte Aktualisierung:** {{ meta-handbook.modifydate }}

---

---

## Zweck

Dieses Dokument beschreibt die Personalwesen-Sicherheit, Schulungen, Änderungssteuerung und mobile Sicherheit für Cloud-Umgebungen in [TODO].

## Geltungsbereich

Dieses Dokument gilt für alle Mitarbeiter, Auftragnehmer, Änderungsprozesse und mobile Geräte.

## Personalwesen-Sicherheit (HRS)

### Hintergrundüberprüfungen

**Überprüfungstypen**:
- Identitätsprüfung
- Referenzprüfung
- Bildungsnachweis
- Strafregisterprüfung (wo gesetzlich zulässig)

**Überprüfungsumfang**:
- Alle Mitarbeiter
- Auftragnehmer mit Zugang zu sensiblen Daten
- Privilegierte Benutzer

**Überprüfungsfrequenz**:
- Bei Einstellung
- Bei Rollenwechsel
- Periodische Wiederholung (alle 3-5 Jahre)

### Arbeitsverträge und Vereinbarungen

**Vertragliche Anforderungen**:
- Vertraulichkeitsvereinbarungen (NDA)
- Acceptable Use Policy (AUP)
- Code of Conduct
- Sicherheitsrichtlinien

**Auftragnehmer-Vereinbarungen**:
- Service Level Agreements
- Sicherheitsanforderungen
- Datenschutzklauseln
- Haftungsregelungen

### Beendigung und Rollenwechsel

**Offboarding-Prozess**:
1. Benachrichtigung an IT und Sicherheit
2. Zugriffswiderruf
3. Rückgabe von Geräten und Zugangskarten
4. Exit-Interview
5. Dokumentation

**Rollenwechsel**:
- Überprüfung der Zugriffsrechte
- Anpassung der Berechtigungen
- Schulung für neue Rolle
- Dokumentation

## Sicherheitsbewusstsein und Schulung

### Schulungsprogramm

**Pflichtschulungen**:
- Security Awareness Training (jährlich)
- Data Protection Training (jährlich)
- Phishing Awareness Training (quartalsweise)
- Role-specific Training (bei Bedarf)

**Schulungsinhalte**:
- Informationssicherheit Grundlagen
- Datenschutz und DSGVO
- Phishing und Social Engineering
- Passwort-Sicherheit
- Mobile Device Security
- Cloud Security Best Practices
- Incident Reporting

### Schulungsmethoden

**Schulungsformate**:
- E-Learning
- Präsenzschulungen
- Webinare
- Phishing-Simulationen
- Security Awareness Kampagnen

**Schulungsverfolgung**:
- Teilnahmeregistrierung
- Abschlusstests
- Zertifikate
- Compliance-Reporting

### Phishing-Simulationen

**Simulationsprogramm**:
- Monatliche Phishing-Tests
- Verschiedene Schwierigkeitsgrade
- Realistische Szenarien

**Metriken**:
- Click-Rate
- Reporting-Rate
- Verbesserung über Zeit

## Änderungssteuerung und Konfigurationsmanagement (CCC)

### Change Management Prozess

**Change-Typen**:
- Standard Changes (vorab genehmigt)
- Normal Changes (Genehmigung erforderlich)
- Emergency Changes (beschleunigtes Verfahren)

**Change-Prozess**:
1. Change Request
2. Impact Assessment
3. Risk Assessment
4. Change Approval
5. Change Implementation
6. Change Verification
7. Change Documentation

### Change Advisory Board (CAB)

**CAB-Mitglieder**:
- Change Manager
- IT Operations
- Security Team
- Application Owners
- Business Representatives

**CAB-Meetings**:
- Wöchentliche Meetings
- Emergency CAB bei Bedarf
- Review aller Normal und Emergency Changes

### Konfigurationsmanagement

**Configuration Management Database (CMDB)**:
- Configuration Items (CIs)
- CI-Beziehungen
- CI-Attribute
- Change History

**Configuration Baselines**:
- Approved Configurations
- Security Baselines
- Compliance Baselines

**Configuration Audits**:
- Regelmäßige Audits
- Drift Detection
- Remediation

## Mobile Sicherheit (MOS)

### Mobile Device Management (MDM)

**MDM-Lösung**:
- Device Enrollment
- Policy Enforcement
- App Management
- Remote Wipe

**Unterstützte Plattformen**:
- iOS
- Android
- Windows Mobile

### Mobile Security Policies

**Geräterichtlinien**:
- Passcode-Anforderungen
- Verschlüsselung
- Automatische Sperre
- Jailbreak/Root Detection

**App-Richtlinien**:
- Approved App List
- App Blacklist
- App Permissions
- App Updates

**Datenrichtlinien**:
- Data Encryption
- Data Loss Prevention
- Backup Policies
- Data Wiping

### BYOD (Bring Your Own Device)

**BYOD-Richtlinie**:
- Zulässige Geräte
- Sicherheitsanforderungen
- Datentrennung (Containerization)
- Support-Umfang

**BYOD-Enrollment**:
- Geräteregistrierung
- Compliance-Check
- MDM-Installation
- Benutzervereinbarung

## Interoperabilität und Portabilität (IPY)

### Datenportabilität

**Portabilitätsanforderungen**:
- Standardformate
- API-Zugang
- Datenexport
- Datenmigration

**Portabilitätsprozess**:
- Datenextraktion
- Datenvalidierung
- Datentransformation
- Datenimport

### Cloud-Interoperabilität

**Interoperabilitätsstandards**:
- Open Standards
- Standard APIs
- Standard Protocols
- Standard Data Formats

**Multi-Cloud-Strategie**:
- Cloud-Anbieter-Auswahl
- Workload-Verteilung
- Datenreplikation
- Failover-Strategien

## CCM-Kontrollen

**HRS-01**: Human Resources Security
**HRS-02**: Human Resources - Asset Returns
**HRS-03**: Human Resources - Background Screening
**HRS-04**: Human Resources - Employment Agreements
**HRS-05**: Human Resources - Employment Termination
**HRS-06**: Human Resources - Mobile Device Management
**HRS-07**: Human Resources - Non-Disclosure Agreements
**HRS-08**: Human Resources - Roles / Responsibilities
**HRS-09**: Human Resources - Training / Awareness
**HRS-10**: Human Resources - User Responsibility
**HRS-11**: Human Resources - Workspace
**CCC-01**: Change Control & Configuration Management
**CCC-02**: Change Control - Change Detection
**CCC-03**: Change Control - Change Management
**CCC-04**: Change Control - Configuration Management
**CCC-05**: Change Control - New Development / Acquisition
**CCC-06**: Change Control - Outsourced Development
**CCC-07**: Change Control - Production Changes
**CCC-08**: Change Control - Quality Testing
**CCC-09**: Change Control - Unauthorized Software Installations
**MOS-01**: Mobile Security
**MOS-02**: Mobile Security - Anti-Malware
**MOS-03**: Mobile Security - Application Stores
**MOS-04**: Mobile Security - Approved Applications
**MOS-05**: Mobile Security - Approved Software
**MOS-06**: Mobile Security - Device Eligibility
**MOS-07**: Mobile Security - Device Inventory
**MOS-08**: Mobile Security - Device Management
**MOS-09**: Mobile Security - Jailbreaking and Rooting
**MOS-10**: Mobile Security - OS Versions
**MOS-11**: Mobile Security - Remote Wipe
**MOS-12**: Mobile Security - Security Patches
**MOS-13**: Mobile Security - User Awareness
**IPY-01**: Interoperability & Portability
**IPY-02**: Interoperability & Portability - APIs
**IPY-03**: Interoperability & Portability - Data Request
**IPY-04**: Interoperability & Portability - Policy & Legal
**IPY-05**: Interoperability & Portability - Standardized Network Protocols

<!-- Hinweis: Passen Sie HR-Prozesse und Änderungsmanagement an -->

