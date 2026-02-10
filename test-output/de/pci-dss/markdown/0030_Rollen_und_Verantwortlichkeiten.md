# Rollen und Verantwortlichkeiten

**Dokument-ID:** PCI-0030  
**Organisation:** AdminSend GmbH  
**Owner:** IT Operations Manager  
**Genehmigt durch:** CIO  
**Version:** 1.0.0  
**Status:** Entwurf / In Review / Freigegeben  
**Klassifizierung:** internal  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  

---



## 1. Zweck

Dieses Dokument definiert die Rollen, Verantwortlichkeiten und Zuständigkeiten für die PCI-DSS-Compliance bei AdminSend GmbH.

### 1.1 Ziele

- **Klare Verantwortlichkeiten:** Eindeutige Zuweisung von PCI-DSS-Aufgaben
- **Accountability:** Festlegung von Entscheidungsbefugnissen
- **Compliance:** Erfüllung von PCI-DSS Requirement 12.4
- **Kommunikation:** Transparente Kommunikationswege

## 2. Organisationsstruktur

### 2.1 Executive Management

**Chief Executive Officer (CEO):**
- **Name:** {{ meta.roles.ceo.name }}
- **E-Mail:** {{ meta.roles.ceo.email }}
- **Telefon:** {{ meta.roles.ceo.phone }}

**Verantwortlichkeiten:**
- Gesamtverantwortung für PCI-DSS-Compliance
- Genehmigung des PCI-DSS-Budgets
- Genehmigung der Informationssicherheitsrichtlinie
- Eskalationspunkt für kritische Compliance-Themen

**Chief Information Security Officer (CISO):**
- **Name:** {{ meta.roles.ciso.name }}
- **E-Mail:** {{ meta.roles.ciso.email }}
- **Telefon:** {{ meta.roles.ciso.phone }}

**Verantwortlichkeiten:**
- Leitung des PCI-DSS-Compliance-Programms
- Genehmigung von Sicherheitsrichtlinien und -standards
- Überwachung der Compliance-Aktivitäten
- Berichterstattung an Executive Management
- Genehmigung von Ausnahmen (Risk Acceptance)

### 2.2 PCI-DSS Program Management

**PCI-DSS Program Manager:**
- **Name:** [TODO: Name]
- **E-Mail:** [TODO: E-Mail]
- **Telefon:** [TODO: Telefon]

**Verantwortlichkeiten:**
- Tägliche Leitung des PCI-DSS-Programms
- Koordination aller Compliance-Aktivitäten
- Vorbereitung von Audits und Assessments
- Pflege der PCI-DSS-Dokumentation
- Schulungskoordination
- Liaison zu QSA und Acquiring Banks

**PCI-DSS Compliance Team:**
- **Mitglieder:** [TODO: Liste der Teammitglieder]

**Verantwortlichkeiten:**
- Unterstützung des Program Managers
- Durchführung von Compliance-Checks
- Dokumentation von Nachweisen
- Koordination mit Fachabteilungen

### 2.3 IT und Operations

**Chief Information Officer (CIO):**
- **Name:** {{ meta.roles.cio.name }}
- **E-Mail:** {{ meta.roles.cio.email }}
- **Telefon:** {{ meta.roles.cio.phone }}

**Verantwortlichkeiten:**
- Verantwortung für IT-Infrastruktur und -Systeme
- Genehmigung von IT-Änderungen im CDE
- Bereitstellung von Ressourcen für PCI-DSS-Compliance
- Eskalationspunkt für IT-bezogene Compliance-Themen

**IT Security Manager:**
- **Name:** [TODO: Name]
- **E-Mail:** [TODO: E-Mail]
- **Telefon:** [TODO: Telefon]

**Verantwortlichkeiten:**
- Implementation von Sicherheitskontrollen
- Verwaltung von Firewalls und Netzwerksegmentierung
- Patch Management und Vulnerability Management
- Incident Response
- Log-Monitoring und -Analyse

**System Administrators:**
- **Anzahl:** [TODO: Anzahl]
- **Kontakt:** [TODO: Team-E-Mail]

**Verantwortlichkeiten:**
- Administration von CDE-Systemen
- Durchführung von Sicherheitsupdates
- Backup und Recovery
- Einhaltung von Hardening-Standards

**Network Administrators:**
- **Anzahl:** [TODO: Anzahl]
- **Kontakt:** [TODO: Team-E-Mail]

**Verantwortlichkeiten:**
- Verwaltung von Netzwerkkomponenten
- Firewall-Konfiguration und -Wartung
- Netzwerksegmentierung
- VPN-Verwaltung

### 2.4 Application Development

**Development Manager:**
- **Name:** [TODO: Name]
- **E-Mail:** [TODO: E-Mail]
- **Telefon:** [TODO: Telefon]

**Verantwortlichkeiten:**
- Sichere Softwareentwicklung (Secure SDLC)
- Code Reviews und Security Testing
- Einhaltung von Secure Coding Standards
- Vulnerability Management in Anwendungen

**Developers:**
- **Anzahl:** [TODO: Anzahl]
- **Kontakt:** [TODO: Team-E-Mail]

**Verantwortlichkeiten:**
- Entwicklung sicherer Anwendungen
- Teilnahme an Security Training
- Behebung von Sicherheitslücken
- Dokumentation von Anwendungen

### 2.5 Business Operations

**Operations Manager:**
- **Name:** [TODO: Name]
- **E-Mail:** [TODO: E-Mail]
- **Telefon:** [TODO: Telefon]

**Verantwortlichkeiten:**
- Geschäftsprozesse mit Karteninhaberdaten
- Schulung von Mitarbeitern
- Einhaltung von Betriebsverfahren
- Incident Reporting

**Store/Branch Managers:**
- **Anzahl:** [TODO: Anzahl]
- **Kontakt:** [TODO: Kontaktliste]

**Verantwortlichkeiten:**
- Physische Sicherheit an Standorten
- Schulung von Kassierern/POS-Bedienern
- Einhaltung von PCI-DSS-Verfahren
- Meldung von Sicherheitsvorfällen

### 2.6 Human Resources

**HR Manager:**
- **Name:** [TODO: Name]
- **E-Mail:** [TODO: E-Mail]
- **Telefon:** [TODO: Telefon]

**Verantwortlichkeiten:**
- Background Checks für Mitarbeiter mit CDE-Zugriff
- Onboarding und Offboarding
- Schulungskoordination
- Vertraulichkeitsvereinbarungen (NDAs)

### 2.7 Legal und Compliance

**Legal Counsel:**
- **Name:** [TODO: Name]
- **E-Mail:** [TODO: E-Mail]
- **Telefon:** [TODO: Telefon]

**Verantwortlichkeiten:**
- Rechtliche Beratung zu PCI-DSS
- Vertragsüberprüfung (Dienstleister)
- Datenschutz und Compliance
- Breach Notification (rechtliche Aspekte)

**Data Protection Officer (DPO):**
- **Name:** [TODO: Name]
- **E-Mail:** [TODO: E-Mail]
- **Telefon:** [TODO: Telefon]

**Verantwortlichkeiten:**
- Datenschutz-Compliance (DSGVO)
- Schnittstelle zwischen PCI-DSS und Datenschutz
- Datenschutz-Folgenabschätzungen
- Meldung von Datenschutzverletzungen

## 3. Externe Rollen

### 3.1 Qualified Security Assessor (QSA)

**Firma:** [TODO: QSA-Firma]  
**Ansprechpartner:** [TODO: Name]  
**E-Mail:** [TODO: E-Mail]  
**Telefon:** [TODO: Telefon]  
**QSA-ID:** [TODO: QSA-ID]  

**Verantwortlichkeiten:**
- Durchführung des jährlichen PCI-DSS-Assessments
- Erstellung des Report on Compliance (ROC)
- Beratung zu Compliance-Fragen
- Validierung von Sicherheitskontrollen

### 3.2 Approved Scanning Vendor (ASV)

**Firma:** [TODO: ASV-Firma]  
**Ansprechpartner:** [TODO: Name]  
**E-Mail:** [TODO: E-Mail]  
**Telefon:** [TODO: Telefon]  
**ASV-ID:** [TODO: ASV-ID]  

**Verantwortlichkeiten:**
- Quartalsweise Vulnerability Scans
- Erstellung von Scan-Berichten
- Validierung von Remediation
- Passing Scan Attestation

### 3.3 Penetration Testing Firm

**Firma:** [TODO: Pentest-Firma]  
**Ansprechpartner:** [TODO: Name]  
**E-Mail:** [TODO: E-Mail]  
**Telefon:** [TODO: Telefon]  

**Verantwortlichkeiten:**
- Jährliche Penetrationstests
- Segmentierungsvalidierung
- Erstellung von Pentest-Berichten
- Retest nach Remediation

### 3.4 Service Providers

| Dienstleister | Kontakt | Rolle | PCI-DSS-Status |
|---------------|---------|-------|----------------|
| [TODO: Payment Processor] | [TODO: Kontakt] | Zahlungsabwicklung | AOC vorhanden |
| [TODO: Hosting Provider] | [TODO: Kontakt] | Server-Hosting | AOC vorhanden |
| [TODO: Managed Security] | [TODO: Kontakt] | SIEM/SOC | AOC vorhanden |

## 4. RACI-Matrizen

### 4.1 PCI-DSS Requirement 1: Firewall Configuration

| Aktivität | CISO | PCI Mgr | IT Sec | Network | QSA |
|-----------|------|---------|--------|---------|-----|
| Firewall-Richtlinie erstellen | A | R | C | C | I |
| Firewall-Regeln konfigurieren | C | I | A | R | I |
| Quartalsweise Regelüberprüfung | A | R | C | C | I |
| Änderungen genehmigen | A | C | R | I | I |

### 4.2 PCI-DSS Requirement 3: Protect Stored Data

| Aktivität | CISO | PCI Mgr | IT Sec | Dev Mgr | QSA |
|-----------|------|---------|--------|---------|-----|
| Verschlüsselungsrichtlinie | A | R | C | C | I |
| Key Management | C | I | A | R | I |
| Datenlöschung | C | R | A | C | I |
| Tokenisierung | C | R | C | A | I |

### 4.3 PCI-DSS Requirement 6: Secure Development

| Aktivität | CISO | PCI Mgr | IT Sec | Dev Mgr | Developers |
|-----------|------|---------|--------|---------|------------|
| Secure Coding Standards | A | C | C | R | I |
| Code Reviews | C | I | C | A | R |
| Vulnerability Scanning | C | R | A | C | I |
| Patch Deployment | C | R | A | R | C |

### 4.4 PCI-DSS Requirement 8: Authentication

| Aktivität | CISO | PCI Mgr | IT Sec | HR | QSA |
|-----------|------|---------|--------|-----|-----|
| Authentifizierungsrichtlinie | A | R | C | C | I |
| Benutzerverwaltung | C | I | A | R | I |
| MFA-Implementation | C | R | A | I | I |
| Zugriffsentfernung (Offboarding) | C | R | A | R | I |

### 4.5 PCI-DSS Requirement 10: Logging

| Aktivität | CISO | PCI Mgr | IT Sec | Ops Mgr | QSA |
|-----------|------|---------|--------|---------|-----|
| Logging-Richtlinie | A | R | C | C | I |
| Log-Konfiguration | C | I | A | R | I |
| Tägliche Log-Überprüfung | C | R | A | C | I |
| Log-Retention | A | R | C | I | I |

### 4.6 PCI-DSS Requirement 12: Security Policy

| Aktivität | CEO | CISO | PCI Mgr | Legal | QSA |
|-----------|-----|------|---------|-------|-----|
| Sicherheitsrichtlinie genehmigen | A | R | C | C | I |
| Jährliche Risikobewertung | C | A | R | I | I |
| Schulungsprogramm | C | A | R | C | I |
| Incident Response Plan | C | A | R | C | I |

**Legende:**
- **R** (Responsible): Durchführungsverantwortung
- **A** (Accountable): Gesamtverantwortung, Entscheidungsbefugnis (nur eine Person pro Aktivität)
- **C** (Consulted): Konsultiert, Fachexpertise
- **I** (Informed): Informiert

## 5. Eskalationspfade

### 5.1 Compliance-Eskalation

**Level 1:** PCI-DSS Program Manager  
**Level 2:** CISO  
**Level 3:** CEO  

**Eskalationskriterien:**
- Kritische Compliance-Lücken
- Fehlgeschlagene Audits
- Datenschutzverletzungen
- Nicht behebbare Schwachstellen

### 5.2 Security Incident-Eskalation

**Level 1:** IT Security Manager (24/7 Bereitschaft)  
**Level 2:** CISO  
**Level 3:** CEO + Legal Counsel  

**Eskalationskriterien:**
- Verdacht auf Datenschutzverletzung
- Kompromittierung von CDE-Systemen
- Malware-Infektion im CDE
- Unautorisierten Zugriff auf Karteninhaberdaten

### 5.3 Kontaktinformationen für Notfälle

**24/7 Security Hotline:** [TODO: Telefonnummer]  
**Security E-Mail:** [TODO: security@organization.com]  
**Incident Response Team:** [TODO: Kontaktliste]  

## 6. Schulung und Awareness

### 6.1 Schulungsanforderungen

| Rolle | Schulungsthemen | Häufigkeit | Verantwortlich |
|-------|-----------------|------------|----------------|
| Alle Mitarbeiter | Security Awareness | Jährlich | HR + PCI Mgr |
| CDE-Administratoren | PCI-DSS Deep Dive | Jährlich | PCI Mgr |
| Entwickler | Secure Coding | Jährlich | Dev Mgr |
| Kassierer/POS | PCI-DSS Basics | Bei Einstellung + jährlich | Ops Mgr |

### 6.2 Schulungsdokumentation

**Schulungsnachweis erforderlich:**
- Teilnehmerliste
- Schulungsmaterialien
- Bestätigungen der Teilnehmer
- Testergebnisse (falls zutreffend)

**Aufbewahrungsfrist:** [TODO: 3 Jahre]

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |


