# Richtlinie: Secure SDLC, Code Reviews und Secrets Management

**Dokument-ID:** 0390
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

## 1. Zweck und Geltungsbereich

Diese Richtlinie konkretisiert die `0380_Policy_Secure_Development.md` und definiert:
- Secure Software Development Lifecycle (SSDLC)
- Code-Review-Prozesse und Security-Checks
- Secrets Management und sichere Konfiguration

**Geltungsbereich:** Alle Softwareentwicklung bei **{{ meta-organisation.name }}**

## 2. Secure SDLC Phasen

### 2.1 Requirements Phase
- Security Requirements definieren
- Threat Modeling durchführen
- Compliance-Anforderungen identifizieren

### 2.2 Design Phase
- Security Architecture Review
- Data Flow Diagrams
- Authentication/Authorization-Design

### 2.3 Development Phase
- Secure Coding Standards befolgen
- SAST (Static Application Security Testing)
- Dependency Scanning

### 2.4 Testing Phase
- DAST (Dynamic Application Security Testing)
- Penetration Testing
- Security Test Cases

### 2.5 Deployment Phase
- Security Configuration Review
- Secrets Management
- Deployment-Checkliste

### 2.6 Maintenance Phase
- Vulnerability Management
- Security Patches
- Incident Response

## 3. Secure Coding Standards

### 3.1 OWASP Top 10

**Pflicht-Prävention:**
1. Broken Access Control
2. Cryptographic Failures
3. Injection
4. Insecure Design
5. Security Misconfiguration
6. Vulnerable Components
7. Authentication Failures
8. Software and Data Integrity Failures
9. Security Logging Failures
10. Server-Side Request Forgery (SSRF)

### 3.2 Input Validation
- Alle Eingaben validieren (Whitelist-Ansatz)
- Parameterisierte Queries (SQL-Injection-Prävention)
- Output-Encoding (XSS-Prävention)

### 3.3 Authentication & Authorization
- Keine eigene Krypto implementieren
- Etablierte Frameworks nutzen (OAuth 2.0, OpenID Connect)
- Least Privilege Principle

### 3.4 Error Handling
- Keine sensitiven Informationen in Fehlermeldungen
- Zentrale Error-Logging
- Graceful Degradation

## 4. Code Reviews

### 4.1 Peer Code Review

**Prozess:**
- Jeder Code-Change benötigt mindestens 1 Approval
- Review vor Merge in Main Branch
- Checkliste für Security-Aspekte

**Security-Review-Checkliste:**
- [ ] Input-Validierung vorhanden?
- [ ] Keine Secrets im Code?
- [ ] Sichere Kryptografie verwendet?
- [ ] Error-Handling korrekt?
- [ ] Logging implementiert?

### 4.2 Security Champion Review

**Bei sicherheitskritischen Changes:**
- Zusätzliches Review durch Security Champion
- Security Champion: Entwickler mit Security-Training
- Mindestens 1 Security Champion pro Team

### 4.3 Automated Code Review

**Tools:**
- **SAST:** {{ meta.security.sast_tool }} (z.B. SonarQube, Checkmarx)
- **Dependency Check:** {{ meta.security.dependency_tool }} (z.B. Snyk, Dependabot)
- **Secrets Scanning:** {{ meta.security.secrets_scanner }} (z.B. GitGuardian, TruffleHog)

**Integration:**
- CI/CD-Pipeline
- Automatische Scans bei jedem Commit
- Blockierung bei Critical/High Findings

## 5. Secrets Management

### 5.1 Verbotene Praktiken

**Niemals:**
- Secrets in Git committen
- Secrets in Konfigurationsdateien (Klartext)
- Secrets in Environment Variables (Produktion)
- Secrets in Logs oder Error Messages

### 5.2 Secrets-Management-System

**System:** {{ meta.security.secrets_manager }} (z.B. HashiCorp Vault, Azure Key Vault, AWS Secrets Manager)

**Funktionen:**
- Zentrale Secrets-Speicherung (verschlüsselt)
- Dynamische Secrets (kurzlebig)
- Audit-Logging aller Zugriffe
- Rotation von Secrets

### 5.3 Secrets-Rotation

**Frequenz:**
- API-Keys: Alle 90 Tage
- Database-Credentials: Alle 180 Tage
- Service-Account-Passwords: Alle 180 Tage

**Automatisierung:**
- Automatische Rotation wo möglich
- Benachrichtigung vor Ablauf

### 5.4 Development vs. Production

**Separate Secrets:**
- Dev/Test: Separate Secrets (niedrigere Privilegien)
- Produktion: Produktions-Secrets (höhere Privilegien)
- Keine Wiederverwendung zwischen Umgebungen

## 6. Dependency Management

### 6.1 Third-Party-Libraries

**Anforderungen:**
- Nur genehmigte Libraries verwenden
- Regelmäßige Updates
- Vulnerability-Scanning

**Genehmigungsprozess:**
- Antrag über Ticketsystem
- Security-Review der Library
- Lizenz-Compliance-Prüfung
- Genehmigung durch Security-Team

### 6.2 Software Composition Analysis (SCA)

**Tools:** {{ meta.security.sca_tool }} (z.B. Snyk, WhiteSource)

**Prozess:**
- Automatisches Scanning bei Build
- Identifikation bekannter Schwachstellen (CVEs)
- Alerts bei kritischen Schwachstellen
- Remediation-Empfehlungen

### 6.3 Dependency Updates

**Strategie:**
- Security-Updates: Sofort
- Minor-Updates: Monatlich
- Major-Updates: Nach Testing

## 7. CI/CD Security

### 7.1 Pipeline Security

**Security Gates:**
1. **Commit:** Secrets Scanning
2. **Build:** SAST, Dependency Check
3. **Test:** Unit Tests, Security Tests
4. **Deploy:** DAST, Configuration Review

**Blockierung bei:**
- Critical/High SAST Findings
- Known Exploited Vulnerabilities
- Secrets im Code

### 7.2 Container Security

**Image Scanning:**
- Scan aller Container-Images
- Nur signierte Images deployen
- Regelmäßige Re-Scans

**Best Practices:**
- Minimal Base Images
- Non-Root User
- Read-Only Filesystem

### 7.3 Infrastructure as Code (IaC)

**Security Scanning:**
- Terraform, CloudFormation, etc.
- Tools: Checkov, Terrascan
- Prüfung auf Misconfigurations

## 8. Security Testing

### 8.1 SAST (Static Application Security Testing)

**Frequenz:** Bei jedem Commit  
**Tool:** {{ meta.security.sast_tool }}  
**Abdeckung:** Alle Programmiersprachen

### 8.2 DAST (Dynamic Application Security Testing)

**Frequenz:** Wöchentlich (Staging), vor jedem Release  
**Tool:** {{ meta.security.dast_tool }}  
**Scope:** Web-Anwendungen, APIs

### 8.3 Penetration Testing

**Frequenz:**
- Neue Anwendungen: Vor Go-Live
- Bestehende Anwendungen: Jährlich
- Nach kritischen Änderungen: Ad-hoc

**Durchführung:**
- Intern oder externe Pentester
- Scope-Definition
- Remediation aller Findings
- Re-Test nach Fixes

## 9. Compliance und Audit

### 9.1 Messgrößen (KPIs)

| Metrik | Zielwert |
|--------|----------|
| Code-Review-Coverage | 100% |
| SAST-Scan-Coverage | 100% |
| Critical/High Findings (Open) | 0 |
| Secrets in Code | 0 |

### 9.2 Audit-Nachweise

- Code-Review-Logs
- SAST/DAST-Berichte
- Penetration-Test-Berichte
- Secrets-Rotation-Logs

## 10. Referenzen

### Interne Dokumente
- `0380_Policy_Secure_Development.md`
- `0340_Policy_Vulnerability_und_Patch_Management.md`

### Externe Standards
- **ISO/IEC 27001:2022 Annex A.8.25** - Secure development lifecycle
- **ISO/IEC 27001:2022 Annex A.8.26** - Application security requirements
- **OWASP ASVS** - Application Security Verification Standard
- **NIST SP 800-218** - Secure Software Development Framework

**Genehmigt durch:** {{ meta.ciso.name }}, CISO  
**Nächster Review:** {{ meta-handbook.next_review }}

