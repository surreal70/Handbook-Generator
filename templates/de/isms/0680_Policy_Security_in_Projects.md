# Policy: Security in Projects

**Dokument-ID:** 0680
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Genehmigt durch:** {{ meta-handbook.approver }}
**Revision:** [TODO]
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Klassifizierung:** {{ meta-handbook.classification }}
**Letzte Aktualisierung:** {{ meta-handbook.modifydate }}
**Template Version:** [TODO]

---

---

<!-- 
TEMPLATE AUTHOR NOTE:
This policy establishes requirements for integrating security into project management.
It ensures that security is considered throughout the project lifecycle.
Customize based on your organization's project management methodology and security requirements.

ISO 27001:2022 Annex A Reference: A.5.8, A.8.25, A.8.32
-->

## 1. Zweck

Diese Policy definiert die Anforderungen an die Integration von Informationssicherheit in Projekte der **{{ meta-organisation.name }}**. Sie stellt sicher, dass Sicherheitsanforderungen im gesamten Projektlebenszyklus berücksichtigt werden.

## 2. Geltungsbereich

Diese Policy gilt für:

- **Organisationseinheiten:** Alle Abteilungen und Standorte der {{ meta-organisation.name }}
- **Projekte:** Alle IT-Projekte, Infrastrukturprojekte, Softwareentwicklungsprojekte
- **Projektphasen:** Initiierung, Planung, Umsetzung, Abschluss
- **Projektarten:** Interne Projekte, externe Projekte, Partnerprojekte
- **Standorte:** [[ netbox.site.name ]] und alle weiteren Betriebsstandorte

**Ausnahmen:** Ausnahmen sind nur über den definierten Ausnahmenprozess (`0640_Policy_Ausnahmen_und_Risk_Waivers.md`) zulässig.

## 3. Grundsätze (Policy Statements)

### 3.1 Security by Design
Sicherheit wird von Anfang an in Projekte integriert (Security by Design). Sicherheitsanforderungen werden in der Projektinitiierung definiert.

### 3.2 Security Requirements
Für jedes Projekt werden Sicherheitsanforderungen definiert:
- Vertraulichkeit, Integrität, Verfügbarkeit
- Compliance-Anforderungen
- Datenschutzanforderungen
- Technische Sicherheitsanforderungen

### 3.3 Security Risk Assessment
Für jedes Projekt wird ein Security Risk Assessment durchgeführt. Risiken werden identifiziert, bewertet und behandelt.

### 3.4 Security Architecture Review
Projektarchitekturen werden auf Sicherheit überprüft. Security Architecture Review erfolgt vor Implementierung.

### 3.5 Security Testing
Projekte werden auf Sicherheit getestet:
- Security Testing (Penetration Tests, Vulnerability Scans)
- Code Reviews (SAST, DAST) für Softwareprojekte
- Configuration Reviews für Infrastrukturprojekte

### 3.6 Security Sign-Off
Projekte erhalten Security Sign-Off vor Go-Live. Security Sign-Off bestätigt, dass Sicherheitsanforderungen erfüllt sind.

### 3.7 Change Management Integration
Sicherheitsrelevante Änderungen folgen dem Change-Management-Prozess (siehe `0360_Policy_Change_und_Release_Management.md`).

### 3.8 Third-Party Security
Bei Projekten mit Drittparteien (Lieferanten, Partner) werden Sicherheitsanforderungen vertraglich vereinbart (siehe `0460_Policy_Lieferanten_und_Cloud_Sicherheit.md`).

### 3.9 Security Documentation
Sicherheitsrelevante Projektdokumentation wird erstellt:
- Security Requirements Specification
- Security Architecture Document
- Security Test Report
- Security Sign-Off Document

## 4. Rollen und Verantwortlichkeiten

### RACI-Matrix: Security in Projects

| Aktivität | CISO | Project Manager | Security Architect | IT-Betrieb | Business Owner |
|-----------|------|-----------------|-------------------|------------|----------------|
| Policy-Erstellung | R/A | C | R | C | C |
| Security Requirements | R | R/A | R | C | R |
| Security Risk Assessment | R/A | R | R | C | C |
| Security Architecture Review | R/A | C | R/A | C | C |
| Security Testing | R | R/A | R | R | C |
| Security Sign-Off | R/A | C | C | C | C |
| Change Management | C | R | C | R/A | C |
| Third-Party Security | R/A | R | C | C | R |

**Legende:** R = Responsible (Durchführung), A = Accountable (Verantwortlich), C = Consulted (Konsultiert), I = Informed (Informiert)

### Schlüsselrollen

- **Policy Owner:** {{ meta-organisation-roles.role_CISO }} (CISO)
- **Security Architect:** {{ meta-handbook.security_architect }}
- **Project Manager:** Projektverantwortliche
- **IT Operations Manager:** {{ meta-handbook.it_operations_manager }}
- **Business Owner:** Fachbereichsverantwortliche
- **Kontroll-/Prüfinstanz:** ISMS, Internal Audit

## 5. Ableitungen (Richtlinien/Standards/Prozesse)

Details zur Umsetzung werden in nachgelagerten Dokumenten geregelt:

### Zugehörige Richtlinien
- **0690_Richtlinie_Sicherheitsanforderungen_im_Projektlebenszyklus.md** - Detaillierte Implementierungsrichtlinie
- `0380_Policy_Secure_Development.md` - Secure Development Policy
- `0360_Policy_Change_und_Release_Management.md` - Change Management Policy
- `0460_Policy_Lieferanten_und_Cloud_Sicherheit.md` - Supplier Security Policy

### Zugehörige Standards/Baselines
- Security Requirements Template
- Security Risk Assessment Template
- Security Architecture Review Checklist
- Security Testing Standards
- Security Sign-Off Template

### Zugehörige Prozesse
- Project Security Review Prozess
- Security Risk Assessment Prozess
- Security Architecture Review Prozess
- Security Testing Prozess
- Security Sign-Off Prozess

## 6. Compliance, Monitoring und Durchsetzung

### Messgrößen und KPIs
- Anzahl Projekte mit Security Requirements (Ziel: 100%)
- Anzahl durchgeführter Security Risk Assessments (Ziel: 100% aller Projekte)
- Anzahl Security Architecture Reviews (Ziel: 100% kritischer Projekte)
- Anzahl Security Tests (Ziel: 100% vor Go-Live)
- Anzahl Security Sign-Offs (Ziel: 100% vor Go-Live)
- Durchschnittliche Zeit für Security Review (Ziel: < 5 Tage)
- Anzahl Projekte ohne Security Sign-Off (Ziel: 0)

### Nachweise und Evidence
- Security Requirements Specifications
- Security Risk Assessments
- Security Architecture Review Reports
- Security Test Reports (Penetration Tests, Vulnerability Scans)
- Security Sign-Off Documents
- Project Security Checklists
- Change Management Records

### Konsequenzen bei Verstößen
Verstöße gegen diese Policy werden nach den geltenden HR- und Compliance-Prozessen behandelt:
- **Projekte ohne Security Requirements:** Projektstopp bis Requirements definiert
- **Fehlende Security Risk Assessments:** Nachholung vor Fortsetzung
- **Go-Live ohne Security Sign-Off:** Projektstopp, Eskalation an Management
- **Wiederholte Verstöße:** Arbeitsrechtliche Konsequenzen, Projektverantwortung entzogen

## 7. Ausnahmen

Ausnahmen von dieser Policy sind nur in begründeten Ausnahmefällen zulässig:

- **Ausnahmenprozess:** Siehe `0640_Policy_Ausnahmen_und_Risk_Waivers.md`
- **Genehmigung:** Ausnahmen müssen vom CISO und CIO genehmigt werden
- **Dokumentation:** Alle Ausnahmen werden im Risikoregister dokumentiert
- **Befristung:** Ausnahmen sind grundsätzlich zeitlich befristet

## 8. Referenzen

### Interne Dokumente
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS Policy
- `0690_Richtlinie_Sicherheitsanforderungen_im_Projektlebenszyklus.md` - Detailed Guideline
- `0380_Policy_Secure_Development.md` - Secure Development Policy
- `0080_ISMS_Risikoregister_Template.md` - Risk Register

### Externe Standards und Vorgaben
- **ISO/IEC 27001:2022 Annex A.5.8** - Information security in project management
- **ISO/IEC 27001:2022 Annex A.8.25** - Secure development life cycle
- **ISO/IEC 27001:2022 Annex A.8.32** - Change management
- **NIST SP 800-64** - Security Considerations in the System Development Life Cycle
- **OWASP SAMM** - Software Assurance Maturity Model
- **BSIMM** - Building Security In Maturity Model
- **ISO/IEC 27034** - Application Security

**Genehmigt durch:**  
{{ meta-handbook.management_ceo }}, Geschäftsführung  
Datum: {{ meta-handbook.modifydate }}

**Nächster Review:** {{ meta-handbook.next_review }} (jährlich oder anlassbezogen)

