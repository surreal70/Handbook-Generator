# Policy: Secure Development

<!-- 
TEMPLATE AUTHOR NOTE:
This policy establishes the principles for secure software development lifecycle (SDLC).
It ensures that security is integrated into all phases of software development.
Customize based on your organization's development practices (Agile, DevSecOps, etc.).

ISO 27001:2022 Annex A Reference: A.8.25, A.8.26, A.8.27, A.8.28
-->

**Dokument-ID:** 0380  
**Dokumenttyp:** Policy (abstrakt)  
**Standard-Referenz:** ISO/IEC 27001:2022 Annex A.8.25-A.8.28 (inkl. Amendment 1:2024)  
**Owner:** {{ meta.ciso.name }}  
**Version:** 1.0  
**Status:** Freigegeben  
**Klassifizierung:** Intern  
**Letzte Aktualisierung:** {{ meta.document.date }}  
**Nächster Review:** {{ meta.document.next_review }}

---

## 1. Zweck

Diese Policy definiert die Grundsätze für sichere Softwareentwicklung (Secure SDLC) der **{{ meta.organization.name }}**. Sie stellt sicher, dass Sicherheit in alle Phasen des Software Development Lifecycle integriert wird und Anwendungen sicher entwickelt, getestet und betrieben werden.

## 2. Geltungsbereich

Diese Policy gilt für:

- **Organisationseinheiten:** Alle Entwicklungsteams und Standorte der {{ meta.organization.name }}
- **Anwendungen:** Alle intern entwickelten Anwendungen, APIs, Microservices, Mobile Apps
- **Entwicklungsphasen:** Requirements, Design, Implementation, Testing, Deployment, Maintenance
- **Entwicklungsmodelle:** Agile, Waterfall, DevOps, DevSecOps
- **Standorte:** {{ netbox.site.name }} und alle weiteren Entwicklungsstandorte

**Ausnahmen:** Ausnahmen sind nur über den definierten Ausnahmenprozess (`0640_Policy_Ausnahmen_und_Risk_Waivers.md`) zulässig.

## 3. Grundsätze (Policy Statements)

### 3.1 Security by Design
Sicherheit wird von Anfang an in den Entwicklungsprozess integriert (Shift Left). Sicherheitsanforderungen werden in der Requirements-Phase definiert und im Design berücksichtigt.

### 3.2 Secure Coding Standards
Entwickler folgen anerkannten Secure Coding Standards (OWASP, CERT, CWE). Code wird nach Best Practices entwickelt, um häufige Schwachstellen zu vermeiden.

### 3.3 Code Reviews und Peer Reviews
Alle Code-Änderungen durchlaufen Code Reviews. Sicherheitsrelevanter Code erfordert zusätzliche Security Reviews durch das Security Team.

### 3.4 Automatisierte Security Testing
Security Testing ist in die CI/CD-Pipeline integriert:
- **SAST (Static Application Security Testing):** Statische Code-Analyse
- **DAST (Dynamic Application Security Testing):** Dynamische Sicherheitstests
- **SCA (Software Composition Analysis):** Analyse von Abhängigkeiten und Open-Source-Komponenten
- **Container Scanning:** Sicherheitsprüfung von Container-Images

### 3.5 Secrets Management
Secrets (Passwörter, API-Keys, Zertifikate) werden niemals im Code oder in Repositories gespeichert. Secrets werden in dedizierten Secrets Management Systemen verwaltet.

### 3.6 Dependency Management
Externe Bibliotheken und Abhängigkeiten werden auf bekannte Schwachstellen überprüft. Veraltete oder unsichere Abhängigkeiten werden zeitnah aktualisiert.

### 3.7 Security Testing vor Produktionsfreigabe
Vor der Produktionsfreigabe werden umfassende Sicherheitstests durchgeführt:
- Penetration Testing für kritische Anwendungen
- Security Acceptance Testing
- Vulnerability Assessment

### 3.8 Secure Deployment und Configuration
Anwendungen werden mit sicheren Konfigurationen deployed. Default-Credentials werden geändert, unnötige Features deaktiviert, Hardening-Maßnahmen angewendet.

## 4. Rollen und Verantwortlichkeiten

### RACI-Matrix: Secure Development

| Aktivität | CISO | Security Champion | Entwickler | DevOps | Security Team |
|-----------|------|-------------------|------------|--------|---------------|
| Policy-Erstellung | R/A | C | C | C | C |
| Security Requirements | C | R | C | I | R/A |
| Secure Coding | I | C | R/A | I | C |
| Code Review | I | R | R | I | C |
| Security Review | A | C | I | I | R |
| SAST/DAST/SCA | C | C | I | R | R/A |
| Penetration Testing | A | I | I | I | R |
| Security Training | A | C | R | R | R |

**Legende:** R = Responsible (Durchführung), A = Accountable (Verantwortlich), C = Consulted (Konsultiert), I = Informed (Informiert)

### Schlüsselrollen

- **Policy Owner:** {{ meta.ciso.name }} (CISO)
- **Security Champion:** Entwickler mit Security-Expertise in jedem Team
- **Application Security Lead:** {{ meta.security.appsec_lead }}
- **Umsetzungsverantwortliche:** Entwickler, DevOps, Security Team
- **Kontroll-/Prüfinstanz:** ISMS, Internal Audit

## 5. Ableitungen (Richtlinien/Standards/Prozesse)

Details zur Umsetzung werden in nachgelagerten Dokumenten geregelt:

### Zugehörige Richtlinien
- **0390_Richtlinie_Secure_SDLC_Coding_Review_und_Secrets.md** - Detaillierte Implementierungsrichtlinie
- `0360_Policy_Change_und_Release_Management.md` - Change Management Policy
- `0340_Policy_Vulnerability_und_Patch_Management.md` - Vulnerability Management Policy
- `0260_Policy_Kryptografie_und_Schluesselmanagement.md` - Cryptography Policy

### Zugehörige Standards/Baselines
- Secure Coding Standards (OWASP, CERT)
- Code Review Checklists
- SAST/DAST/SCA Tool-Konfigurationen
- Secrets Management Standards

### Zugehörige Prozesse
- Secure SDLC Prozess
- Code Review Prozess
- Security Testing Prozess
- Vulnerability Disclosure Prozess

## 6. Compliance, Monitoring und Durchsetzung

### Messgrößen und KPIs
- Anzahl Sicherheitsschwachstellen pro Release (Ziel: Reduktion um 50% jährlich)
- Code Review Coverage (Ziel: 100%)
- SAST/DAST/SCA Coverage (Ziel: 100% kritischer Anwendungen)
- Durchschnittliche Zeit zur Behebung von Schwachstellen (MTTR)
- Anzahl Secrets im Code (Ziel: 0)
- Security Training Completion Rate (Ziel: 100% jährlich)

### Nachweise und Evidence
- Code Review Dokumentation
- SAST/DAST/SCA Reports
- Penetration Test Reports
- Security Acceptance Test Results
- Secrets Scanning Reports
- Security Training Nachweise

### Konsequenzen bei Verstößen
Verstöße gegen diese Policy werden nach den geltenden HR- und Compliance-Prozessen behandelt:
- **Secrets im Code:** Sofortige Rotation, Incident Response, Nachschulung
- **Übersprungene Code Reviews:** Rollback, Nachholung, Verwarnung
- **Ignorierte Security Findings:** Remediation, Nachschulung
- **Wiederholte Verstöße:** Arbeitsrechtliche Konsequenzen

## 7. Ausnahmen

Ausnahmen von dieser Policy sind nur in begründeten Ausnahmefällen zulässig:

- **Ausnahmenprozess:** Siehe `0640_Policy_Ausnahmen_und_Risk_Waivers.md`
- **Genehmigung:** Ausnahmen müssen vom CISO und Application Security Lead genehmigt werden
- **Dokumentation:** Alle Ausnahmen werden im Risikoregister dokumentiert
- **Befristung:** Ausnahmen sind grundsätzlich zeitlich befristet
- **Kompensationsmaßnahmen:** Ausnahmen erfordern alternative Sicherheitsmaßnahmen

## 8. Referenzen

### Interne Dokumente
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS Policy
- `0390_Richtlinie_Secure_SDLC_Coding_Review_und_Secrets.md` - Detailed Guideline
- `0360_Policy_Change_und_Release_Management.md` - Change Management Policy
- `0080_ISMS_Risikoregister_Template.md` - Risk Register

### Externe Standards und Vorgaben
- **ISO/IEC 27001:2022 Annex A.8.25** - Secure development lifecycle
- **ISO/IEC 27001:2022 Annex A.8.26** - Application security requirements
- **ISO/IEC 27001:2022 Annex A.8.27** - Secure system architecture and engineering principles
- **ISO/IEC 27001:2022 Annex A.8.28** - Secure coding
- **OWASP Top 10** - Web Application Security Risks
- **OWASP ASVS** - Application Security Verification Standard
- **NIST SP 800-218** - Secure Software Development Framework (SSDF)
- **CWE Top 25** - Most Dangerous Software Weaknesses

---

**Genehmigt durch:**  
{{ meta.management.ceo }}, Geschäftsführung  
Datum: {{ meta.document.approval_date }}

**Nächster Review:** {{ meta.document.next_review }} (jährlich oder anlassbezogen)

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |
