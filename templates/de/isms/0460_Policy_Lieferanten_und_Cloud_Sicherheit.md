# Policy: Lieferanten und Cloud Sicherheit

**Dokument-ID:** 0460
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
This policy establishes the principles for third-party and cloud security management.
It ensures that suppliers, vendors, and cloud providers meet security requirements
and are managed throughout their lifecycle. Customize based on your organization's
supply chain and cloud adoption.

ISO 27001:2022 Annex A Reference: A.5.19, A.5.20, A.5.21, A.5.22, A.5.23
-->

## 1. Zweck

Diese Policy definiert die Grundsätze für Lieferanten- und Cloud-Sicherheitsmanagement der **{{ meta-organisation.name }}**. Sie stellt sicher, dass Lieferanten, Dienstleister und Cloud-Provider Sicherheitsanforderungen erfüllen und über ihren gesamten Lebenszyklus sicher verwaltet werden.

## 2. Geltungsbereich

Diese Policy gilt für:

- **Organisationseinheiten:** Alle Abteilungen und Standorte der {{ meta-organisation.name }}
- **Lieferanten-Typen:** IT-Dienstleister, Cloud-Provider, SaaS-Anbieter, Outsourcing-Partner, Subunternehmer
- **Services:** IaaS, PaaS, SaaS, Managed Services, Outsourcing
- **Lebenszyklus:** Auswahl, Onboarding, Betrieb, Monitoring, Offboarding
- **Standorte:** [[ netbox.site.name ]] und alle weiteren Betriebsstandorte

**Ausnahmen:** Ausnahmen sind nur über den definierten Ausnahmenprozess (`0640_Policy_Ausnahmen_und_Risk_Waivers.md`) zulässig.

## 3. Grundsätze (Policy Statements)

### 3.1 Third-Party Risk Assessment
Alle Lieferanten werden vor Vertragsabschluss einem Sicherheits-Risk-Assessment unterzogen. Das Assessment berücksichtigt Datenzugriff, Kritikalität und Compliance-Anforderungen.

### 3.2 Vertragliche Sicherheitsanforderungen
Verträge mit Lieferanten enthalten verbindliche Sicherheitsanforderungen:
- Informationssicherheits-Klauseln
- Datenschutz-Anforderungen (DSGVO)
- Audit-Rechte und Nachweispflichten
- Incident-Notification-Pflichten
- Subunternehmer-Regelungen

### 3.3 Cloud Security Assessment
Cloud-Provider werden nach anerkannten Standards bewertet (ISO 27001, SOC 2, CSA STAR). Shared Responsibility Model wird dokumentiert und verstanden.

### 3.4 Datenklassifizierung und Cloud-Nutzung
Die Speicherung und Verarbeitung von Daten in der Cloud richtet sich nach der Datenklassifizierung:
- **Öffentlich:** Alle Cloud-Services erlaubt
- **Intern:** Genehmigte Cloud-Services mit angemessenen Kontrollen
- **Vertraulich:** Nur zertifizierte Cloud-Services mit Verschlüsselung
- **Streng Vertraulich:** Nur On-Premise oder dedizierte Cloud mit erweiterten Kontrollen

### 3.5 Supplier Lifecycle Management
Lieferanten werden über ihren gesamten Lebenszyklus verwaltet:
- **Onboarding:** Security Assessment, Vertragsverhandlung
- **Betrieb:** Kontinuierliches Monitoring, regelmäßige Reviews
- **Offboarding:** Sichere Datenrückgabe/-löschung, Zugriffsentzug

### 3.6 Regelmäßige Supplier Reviews
Kritische Lieferanten werden jährlich überprüft. Reviews umfassen Sicherheits-Compliance, Incident-Historie, Zertifizierungen und Performance.

### 3.7 Supply Chain Security
Die Sicherheit der gesamten Lieferkette wird berücksichtigt. Lieferanten müssen Sicherheitsanforderungen an ihre Subunternehmer weitergeben.

### 3.8 Cloud Data Residency und Compliance
Datenstandorte (Data Residency) werden dokumentiert und entsprechen regulatorischen Anforderungen (DSGVO, Schrems II).

## 4. Rollen und Verantwortlichkeiten

### RACI-Matrix: Lieferanten und Cloud Sicherheit

| Aktivität | CISO | Procurement | Legal | DPO | Business Owner | IT-Betrieb |
|-----------|------|-------------|-------|-----|----------------|------------|
| Policy-Erstellung | R/A | C | C | C | I | C |
| Risk Assessment | R/A | C | C | C | C | C |
| Vertragsverhandlung | C | R | R/A | C | C | I |
| Security Review | R/A | I | I | C | C | C |
| Supplier Monitoring | A | C | I | I | C | R |
| Cloud Security Assessment | R/A | C | I | C | C | C |
| Offboarding | C | C | I | C | C | R/A |

**Legende:** R = Responsible (Durchführung), A = Accountable (Verantwortlich), C = Consulted (Konsultiert), I = Informed (Informiert)

### Schlüsselrollen

- **Policy Owner:** {{ meta-organisation-roles.role_CISO }} (CISO)
- **Third-Party Risk Manager:** {{ meta-handbook.security_tprm_manager }}
- **Cloud Security Architect:** {{ meta-handbook.security_cloud_architect }}
- **Data Protection Officer:** {{ meta-handbook.dpo_name }}
- **Umsetzungsverantwortliche:** Procurement, Legal, IT-Betrieb
- **Kontroll-/Prüfinstanz:** ISMS, Internal Audit

## 5. Ableitungen (Richtlinien/Standards/Prozesse)

Details zur Umsetzung werden in nachgelagerten Dokumenten geregelt:

### Zugehörige Richtlinien
- **0470_Richtlinie_Third_Party_Risk_Assessment_und_Cloud_Controls.md** - Detaillierte Implementierungsrichtlinie
- `0280_Policy_Datenklassifizierung_und_Informationshandling.md` - Data Classification Policy
- `0560_Policy_Datenschutz_Schnittstellen.md` - Data Protection Policy
- `0440_Policy_Business_Continuity_ICT_Readiness.md` - Business Continuity Policy

### Zugehörige Standards/Baselines
- Third-Party Risk Assessment Framework
- Cloud Security Assessment Criteria
- Vertragliche Sicherheitsklauseln (Templates)
- Supplier Security Scorecard

### Zugehörige Prozesse
- Third-Party Risk Management Prozess
- Cloud Service Approval Prozess
- Supplier Review Prozess
- Supplier Offboarding Prozess

## 6. Compliance, Monitoring und Durchsetzung

### Messgrößen und KPIs
- Anzahl Lieferanten mit aktuellem Security Assessment (Ziel: 100% kritischer Lieferanten)
- Durchschnittlicher Supplier Security Score
- Anzahl Supplier Security Incidents
- Cloud Service Approval Rate
- Supplier Review Completion Rate (Ziel: 100% jährlich)
- Anzahl nicht-genehmigter Cloud-Services (Shadow IT)

### Nachweise und Evidence
- Third-Party Risk Assessments
- Supplier Security Scorecards
- Verträge mit Sicherheitsklauseln
- Cloud Security Assessments
- Supplier Review Reports
- Audit-Berichte zu Supplier Security

### Konsequenzen bei Verstößen
Verstöße gegen diese Policy werden nach den geltenden HR- und Compliance-Prozessen behandelt:
- **Nutzung nicht-genehmigter Cloud-Services:** Sofortige Deaktivierung, Untersuchung
- **Fehlende Risk Assessments:** Nachholung, Vertragsaussetzung
- **Supplier Security Incidents:** Incident Response, Vertragsüberprüfung
- **Wiederholte Verstöße:** Vertragsbeendigung, arbeitsrechtliche Konsequenzen

## 7. Ausnahmen

Ausnahmen von dieser Policy sind nur in begründeten Ausnahmefällen zulässig:

- **Ausnahmenprozess:** Siehe `0640_Policy_Ausnahmen_und_Risk_Waivers.md`
- **Genehmigung:** Ausnahmen müssen vom CISO und Business Owner genehmigt werden
- **Dokumentation:** Alle Ausnahmen werden im Risikoregister dokumentiert
- **Befristung:** Ausnahmen sind grundsätzlich zeitlich befristet
- **Kompensationsmaßnahmen:** Ausnahmen erfordern alternative Sicherheitsmaßnahmen

## 8. Referenzen

### Interne Dokumente
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS Policy
- `0470_Richtlinie_Third_Party_Risk_Assessment_und_Cloud_Controls.md` - Detailed Guideline
- `0280_Policy_Datenklassifizierung_und_Informationshandling.md` - Data Classification Policy
- `0080_ISMS_Risikoregister_Template.md` - Risk Register

### Externe Standards und Vorgaben
- **ISO/IEC 27001:2022 Annex A.5.19** - Information security in supplier relationships
- **ISO/IEC 27001:2022 Annex A.5.20** - Addressing information security within supplier agreements
- **ISO/IEC 27001:2022 Annex A.5.21** - Managing information security in the ICT supply chain
- **ISO/IEC 27001:2022 Annex A.5.22** - Monitoring, review and change management of supplier services
- **ISO/IEC 27001:2022 Annex A.5.23** - Information security for use of cloud services
- **ISO/IEC 27017** - Cloud Security Controls
- **ISO/IEC 27018** - Cloud Privacy
- **CSA STAR** - Cloud Security Alliance Security, Trust & Assurance Registry
- **DSGVO (EU 2016/679)** - Art. 28 - Auftragsverarbeitung

**Genehmigt durch:**  
{{ meta-handbook.management_ceo }}, Geschäftsführung  
Datum: {{ meta-handbook.modifydate }}

**Nächster Review:** {{ meta-handbook.next_review }} (jährlich oder anlassbezogen)

