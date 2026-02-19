# Statement of Applicability (SoA) – Template

**Dokument-ID:** 0100
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
The Statement of Applicability (SoA) is a mandatory ISO 27001 document that
declares which Annex A controls are applicable to the ISMS and provides
justification for inclusions and exclusions. This document demonstrates that
the organization has considered all controls and made informed decisions.

ISO 27001:2022 Reference: Clause 6.1.3 d) - Statement of Applicability
-->

## 1. Zweck und Geltungsbereich

### 1.1 Zweck

Das Statement of Applicability (SoA) der **{{ meta-organisation.name }}** dokumentiert:
- Welche Annex A Controls auf das ISMS anwendbar sind
- Begründung für die Auswahl oder Ausschluss von Controls
- Implementierungsstatus jedes Controls
- Verknüpfung zu Policies, Richtlinien und Evidence

Das SoA ist ein **Pflichtdokument** nach ISO/IEC 27001:2022 und dient als:
- Nachweis der systematischen Control-Auswahl
- Grundlage für Audits und Zertifizierungen
- Übersicht über den Implementierungsstatus
- Verknüpfung zwischen Risikoanalyse und Controls

### 1.2 Geltungsbereich

Dieses SoA gilt für den gesamten ISMS-Scope (siehe `0020_ISMS_Geltungsbereich_Scope.md`):
- Alle Standorte: [[ netbox.site.name ]] und weitere
- Alle IT-Systeme und Infrastruktur
- Alle Geschäftsprozesse im Scope
- Alle Informationswerte

### 1.3 Annex A Controls (ISO 27001:2022)

**ISO/IEC 27001:2022 Annex A** enthält 93 Controls in 4 Kategorien:
- **Organisational Controls (5.x):** 37 Controls
- **People Controls (6.x):** 8 Controls
- **Physical Controls (7.x):** 14 Controls
- **Technological Controls (8.x):** 34 Controls

**Amendment 1:2024:**
- Berücksichtigt Änderungen aus Amendment 1:2024
- Siehe `0710_Anhang_AnnexA_Mapping_Template.md` für vollständige Liste

## 2. Control-Auswahlkriterien

### 2.1 Auswahlprozess

Controls werden basierend auf folgenden Kriterien ausgewählt:

**1. Risikoanalyse:**
- Controls zur Behandlung identifizierter Risiken
- Siehe `0080_ISMS_Risikoregister_Template.md`

**2. Compliance-Anforderungen:**
- Gesetzliche Anforderungen (DSGVO, NIS2, etc.)
- Vertragliche Verpflichtungen
- Branchenstandards

**3. Best Practices:**
- Branchenübliche Sicherheitsmaßnahmen
- Empfehlungen von Sicherheitsexperten

**4. Organisatorische Anforderungen:**
- Geschäftsanforderungen
- Stakeholder-Erwartungen

### 2.2 Ausschlusskriterien

Controls können ausgeschlossen werden, wenn:
- Nicht relevant für den ISMS-Scope
- Risiko ist akzeptiert und Control nicht erforderlich
- Alternative Controls bieten gleichwertigen Schutz
- Technisch oder organisatorisch nicht umsetzbar (mit Begründung)

**Wichtig:** Ausschlüsse müssen begründet werden und dürfen die Fähigkeit der Organisation zur Erfüllung von Sicherheitsanforderungen nicht beeinträchtigen.

## 3. Statement of Applicability (SoA) - Übersicht

### 3.1 Implementierungsstatus

| Status | Anzahl Controls | Prozent |
|--------|-----------------|---------|
| Implementiert | [TODO] | [TODO]% |
| In Arbeit | [TODO] | [TODO]% |
| Geplant | [TODO] | [TODO]% |
| Nicht anwendbar | [TODO] | [TODO]% |
| **Gesamt** | **93** | **100%** |

**Ziel:** Mindestens 80% der anwendbaren Controls implementiert bis [TODO: Datum]

### 3.2 Implementierung nach Kategorie

| Kategorie | Anwendbar | Implementiert | In Arbeit | Geplant | Nicht anwendbar |
|-----------|-----------|---------------|-----------|---------|-----------------|
| Organisational (5.x) | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| People (6.x) | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| Physical (7.x) | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| Technological (8.x) | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## 4. SoA-Tabelle: Organisational Controls (5.x)

### 4.1 Policies for Information Security (5.1-5.10)

| Control-ID | Control-Name | Anwendbar | Begründung (bei Nein) | Implementierungsstatus | Umsetzung/Beschreibung | Policy/Richtlinie | Evidence | Owner | Bemerkungen |
|------------|--------------|-----------|----------------------|------------------------|------------------------|-------------------|----------|-------|-------------|
| **A.5.1** | Policies for information security | Ja | - | Implementiert | ISMS-Leitlinie und themenspezifische Policies | `0010_ISMS_Informationssicherheitsleitlinie.md` | Policy-Dokumente | {{ meta-organisation-roles.role_CISO }} | Jährlicher Review |
| **A.5.2** | Information security roles and responsibilities | Ja | - | Implementiert | ISMS-Governance-Struktur definiert | `0040_ISMS_Governance_Rollen_und_Verantwortlichkeiten.md` | RACI-Matrizen | {{ meta-organisation-roles.role_CISO }} | - |
| **A.5.3** | Segregation of duties | Ja | - | In Arbeit | Rollentrennung in kritischen Prozessen | `0220_Policy_Zugriffssteuerung_und_Identitaetsmanagement.md` | IAM-Konfiguration | {{ meta-organisation-roles.role_CIO }} | 70% umgesetzt |
| **A.5.4** | Management responsibilities | Ja | - | Implementiert | Management-Commitment dokumentiert | `0010_ISMS_Informationssicherheitsleitlinie.md` | Management Review | {{ meta-handbook.management_ceo }} | - |
| **A.5.5** | Contact with authorities | Ja | - | Implementiert | Kontakte zu Behörden dokumentiert | `0050_Kontakte_und_Eskalation.md` (BCM) | Kontaktliste | {{ meta-organisation-roles.role_CISO }} | - |
| **A.5.6** | Contact with special interest groups | Ja | - | Implementiert | Mitgliedschaft in CERT, Branchenverbänden | [TODO: Dokument] | Mitgliedschaftsnachweise | {{ meta-organisation-roles.role_CISO }} | - |
| **A.5.7** | Threat intelligence | Ja | - | In Arbeit | Threat Intelligence Feeds abonniert | `0060_ISMS_Risikomanagement_Methodik.md` | TI-Feed-Konfiguration | Security Team | MITRE ATT&CK, CERT |
| **A.5.8** | Information security in project management | Ja | - | Geplant | Security in Projektlebenszyklus | `0680_Policy_Security_in_Projects.md` | Projekt-Checklisten | PMO | Rollout Q2 2026 |
| **A.5.9** | Inventory of information and other associated assets | Ja | - | In Arbeit | Asset-Inventar wird gepflegt | `0720_Anhang_Asset_und_Systeminventar_Template.md` | CMDB, NetBox | IT-Betrieb | 80% erfasst |
| **A.5.10** | Acceptable use of information and other associated assets | Ja | - | Implementiert | Acceptable Use Policy | `0200_Policy_Akzeptable_Nutzung_IT.md` | Signed Policies | HR | - |

<!-- 
Continue with remaining Organisational Controls (5.11-5.37)
Add your organization's specific implementation details, evidence, and status.
-->

[TODO: Vollständige Tabelle für alle 37 Organisational Controls erstellen]

## 5. SoA-Tabelle: People Controls (6.x)

| Control-ID | Control-Name | Anwendbar | Begründung (bei Nein) | Implementierungsstatus | Umsetzung/Beschreibung | Policy/Richtlinie | Evidence | Owner | Bemerkungen |
|------------|--------------|-----------|----------------------|------------------------|------------------------|-------------------|----------|-------|-------------|
| **A.6.1** | Screening | Ja | - | Implementiert | Background Checks für kritische Rollen | `0520_Policy_HR_Security.md` | HR-Prozess | HR | - |
| **A.6.2** | Terms and conditions of employment | Ja | - | Implementiert | Sicherheitsklauseln in Arbeitsverträgen | `0530_Richtlinie_HR_Onboarding_Rollenwechsel_Offboarding.md` | Arbeitsverträge | HR | - |
| **A.6.3** | Information security awareness, education and training | Ja | - | In Arbeit | Security Awareness Programm | `0120_ISMS_Schulung_Awareness_und_Kompetenz.md` | Schulungsnachweise | {{ meta-organisation-roles.role_CISO }} | Quartalsweise Training |
| **A.6.4** | Disciplinary process | Ja | - | Implementiert | Disziplinarverfahren bei Verstößen | `0520_Policy_HR_Security.md` | HR-Prozess | HR | - |
| **A.6.5** | Responsibilities after termination or change of employment | Ja | - | Implementiert | Offboarding-Prozess | `0530_Richtlinie_HR_Onboarding_Rollenwechsel_Offboarding.md` | Offboarding-Checkliste | HR | - |
| **A.6.6** | Confidentiality or non-disclosure agreements | Ja | - | Implementiert | NDAs für Mitarbeiter und Dritte | `0520_Policy_HR_Security.md` | Signed NDAs | HR | - |
| **A.6.7** | Remote working | Ja | - | Implementiert | Remote Work Policy | `0500_Policy_Mobile_Device_und_Remote_Work.md` | Remote Work Guidelines | {{ meta-organisation-roles.role_CIO }} | - |
| **A.6.8** | Information security event reporting | Ja | - | Implementiert | Incident Reporting Prozess | `0400_Policy_Incident_Management.md` | Incident Reports | {{ meta-organisation-roles.role_CISO }} | - |

## 6. SoA-Tabelle: Physical Controls (7.x)

| Control-ID | Control-Name | Anwendbar | Begründung (bei Nein) | Implementierungsstatus | Umsetzung/Beschreibung | Policy/Richtlinie | Evidence | Owner | Bemerkungen |
|------------|--------------|-----------|----------------------|------------------------|------------------------|-------------------|----------|-------|-------------|
| **A.7.1** | Physical security perimeters | Ja | - | Implementiert | Zutrittskontrollen am Standort [[ netbox.site.name ]] | `0480_Policy_Physische_Sicherheit.md` | Zutrittsprotokolle | Facility Mgmt | - |
| **A.7.2** | Physical entry | Ja | - | Implementiert | Zugangskarten, Besuchermanagement | `0490_Richtlinie_Zutritt_Besucher_und_Schutz_von_Equipment.md` | Besucherlisten | Facility Mgmt | - |
| **A.7.3** | Securing offices, rooms and facilities | Ja | - | Implementiert | Serverraum gesichert, Alarmanlagen | `0480_Policy_Physische_Sicherheit.md` | Sicherheitskonzept | Facility Mgmt | - |
| **A.7.4** | Physical security monitoring | Ja | - | Implementiert | Videoüberwachung, Alarmsysteme | `0480_Policy_Physische_Sicherheit.md` | Überwachungsprotokolle | Facility Mgmt | DSGVO-konform |
| **A.7.5** | Protecting against physical and environmental threats | Ja | - | Implementiert | Brandschutz, Klimatisierung, USV | `0480_Policy_Physische_Sicherheit.md` | Wartungsprotokolle | Facility Mgmt | - |
| **A.7.6** | Working in secure areas | Ja | - | Implementiert | Clean Desk Policy, Secure Areas | `0480_Policy_Physische_Sicherheit.md` | Audit-Berichte | Facility Mgmt | - |
| **A.7.7** | Clear desk and clear screen | Ja | - | In Arbeit | Clear Desk Policy kommuniziert | `0480_Policy_Physische_Sicherheit.md` | Awareness-Kampagne | {{ meta-organisation-roles.role_CISO }} | Rollout läuft |
| **A.7.8** | Equipment siting and protection | Ja | - | Implementiert | Equipment-Schutz, Diebstahlsicherung | `0490_Richtlinie_Zutritt_Besucher_und_Schutz_von_Equipment.md` | Asset-Register | IT-Betrieb | - |
| **A.7.9** | Security of assets off-premises | Ja | - | Implementiert | Laptop-Verschlüsselung, Mobile Device Policy | `0500_Policy_Mobile_Device_und_Remote_Work.md` | MDM-Konfiguration | IT-Betrieb | - |
| **A.7.10** | Storage media | Ja | - | Implementiert | Sichere Handhabung von Speichermedien | `0280_Policy_Datenklassifizierung_und_Informationshandling.md` | Handling-Procedures | IT-Betrieb | - |
| **A.7.11** | Supporting utilities | Ja | - | Implementiert | USV, Notstrom, Klimatisierung | `0480_Policy_Physische_Sicherheit.md` | Wartungsverträge | Facility Mgmt | - |
| **A.7.12** | Cabling security | Ja | - | Implementiert | Strukturierte Verkabelung, Schutz | `0480_Policy_Physische_Sicherheit.md` | Verkabelungsplan | IT-Betrieb | - |
| **A.7.13** | Equipment maintenance | Ja | - | Implementiert | Wartungsverträge, Wartungsprotokolle | `0480_Policy_Physische_Sicherheit.md` | Wartungsnachweise | IT-Betrieb | - |
| **A.7.14** | Secure disposal or re-use of equipment | Ja | - | Implementiert | Sichere Entsorgung, Data Wiping | `0580_Policy_Aufbewahrung_und_Loeschung.md` | Entsorgungsnachweise | IT-Betrieb | DSGVO-konform |

## 7. SoA-Tabelle: Technological Controls (8.x)

| Control-ID | Control-Name | Anwendbar | Begründung (bei Nein) | Implementierungsstatus | Umsetzung/Beschreibung | Policy/Richtlinie | Evidence | Owner | Bemerkungen |
|------------|--------------|-----------|----------------------|------------------------|------------------------|-------------------|----------|-------|-------------|
| **A.8.1** | User endpoint devices | Ja | - | Implementiert | Endpoint Protection (EDR/AV) | `0620_Policy_Endpoint_Security.md` | EDR-Konfiguration | IT-Betrieb | - |
| **A.8.2** | Privileged access rights | Ja | - | In Arbeit | PAM-Lösung wird implementiert | `0220_Policy_Zugriffssteuerung_und_Identitaetsmanagement.md` | PAM-System | IT-Betrieb | Rollout Q2 2026 |
| **A.8.3** | Information access restriction | Ja | - | Implementiert | Zugriffskontrollen, RBAC | `0220_Policy_Zugriffssteuerung_und_Identitaetsmanagement.md` | IAM-Konfiguration | IT-Betrieb | - |
| **A.8.4** | Access to source code | Ja | - | Implementiert | Git-Zugriffskontrollen, Code Review | `0360_Policy_Secure_Development.md` | Git-Permissions | Dev-Lead | - |
| **A.8.5** | Secure authentication | Ja | - | In Arbeit | MFA-Rollout | `0240_Policy_Authentisierung_und_Passwoerter.md` | MFA-Konfiguration | IT-Betrieb | 80% abgeschlossen |
| **A.8.6** | Capacity management | Ja | - | In Arbeit | Monitoring, Kapazitätsplanung | [TODO: Policy] | Monitoring-Dashboards | IT-Betrieb | - |
| **A.8.7** | Protection against malware | Ja | - | Implementiert | Antivirus, EDR, Email-Filtering | `0620_Policy_Endpoint_Security.md` | AV/EDR-Reports | IT-Betrieb | - |
| **A.8.8** | Management of technical vulnerabilities | Ja | - | In Arbeit | Vulnerability Management Prozess | `0340_Policy_Vulnerability_und_Patch_Management.md` | Scan-Reports | IT-Betrieb | - |

<!-- 
Continue with remaining Technological Controls (8.9-8.34)
Add your organization's specific implementation details.
-->

[TODO: Vollständige Tabelle für alle 34 Technological Controls erstellen]

## 8. Nicht anwendbare Controls

### 8.1 Ausgeschlossene Controls mit Begründung

| Control-ID | Control-Name | Begründung für Ausschluss | Alternative Maßnahmen | Genehmigt durch |
|------------|--------------|---------------------------|----------------------|-----------------|
| [TODO] | [TODO] | [TODO: Nicht im Scope, Risiko akzeptiert, etc.] | [TODO: Falls vorhanden] | {{ meta-organisation-roles.role_CISO }} |

**Wichtig:** Ausschlüsse müssen dokumentiert und genehmigt werden. Sie dürfen die Fähigkeit zur Erfüllung von Sicherheitsanforderungen nicht beeinträchtigen.

## 9. Verknüpfungen und Referenzen

### 9.1 Verknüpfung zu ISMS-Dokumenten

**Risikoanalyse:**
- Controls sind basierend auf Risikoanalyse ausgewählt
- Siehe `0080_ISMS_Risikoregister_Template.md`

**Risikobehandlungsplan:**
- Implementierung von Controls ist im RTP getrackt
- Siehe `0090_ISMS_Risikobehandlungsplan_RTP_Template.md`

**Policies und Richtlinien:**
- Jedes Control ist mit Policy/Richtlinie verknüpft
- Siehe ISMS-Dokumentenstruktur (0200-0690)

**Evidence:**
- Nachweise für Control-Implementierung
- Siehe `0700_Anhang_Nachweisregister_Evidence.md`

### 9.2 Vollständiges Annex A Mapping

Für eine vollständige Übersicht aller 93 Annex A Controls siehe:
- `0710_Anhang_AnnexA_Mapping_Template.md`

## 10. Review und Aktualisierung

### 10.1 Regelmäßiger Review

**Jährlich:**
- Vollständiger SoA-Review
- Überprüfung der Anwendbarkeit aller Controls
- Aktualisierung des Implementierungsstatus

**Quartalsweise:**
- Review des Implementierungsstatus
- Tracking der Maßnahmen aus RTP

### 10.2 Trigger für außerplanmäßigen Review

**Änderungen am ISMS-Scope:**
- Neue Standorte, Systeme, Prozesse
- Siehe `0020_ISMS_Geltungsbereich_Scope.md`

**Neue Risiken:**
- Wesentliche Änderungen im Risikoregister
- Siehe `0080_ISMS_Risikoregister_Template.md`

**Neue Compliance-Anforderungen:**
- Neue Gesetze, Regulierungen, Verträge

**Audit-Findings:**
- Interne oder externe Audit-Findings

## 11. Referenzen

### 11.1 Interne Dokumente

- `0020_ISMS_Geltungsbereich_Scope.md` - ISMS Scope
- `0060_ISMS_Risikomanagement_Methodik.md` - Risk Management
- `0080_ISMS_Risikoregister_Template.md` - Risk Register
- `0090_ISMS_Risikobehandlungsplan_RTP_Template.md` - Risk Treatment Plan
- `0710_Anhang_AnnexA_Mapping_Template.md` - Complete Annex A Mapping
- Alle Policies (0200-0680) und Richtlinien (0210-0690)

### 11.2 Externe Standards

- **ISO/IEC 27001:2022** - Clause 6.1.3 d): Statement of Applicability
- **ISO/IEC 27001:2022** - Annex A: Information security controls
- **ISO/IEC 27001:2022/Amd 1:2024** - Amendment 1 (Annex A updates)
- **ISO/IEC 27002:2022** - Information security controls (detailed guidance)

## Änderungshistorie

| Version | Datum | Autor | Beschreibung | Genehmigt durch |
|---------|-------|-------|--------------|-----------------|
| 1.0 | {{ meta-handbook.modifydate }} | {{ meta-organisation-roles.role_CISO }} | Initiale Version | {{ meta-handbook.management_ceo }} |

**Genehmigt durch:**  
{{ meta-organisation-roles.role_CISO }}, CISO  
{{ meta-handbook.management_ceo }}, Geschäftsführung  
Datum: {{ meta-handbook.modifydate }}

**Nächster Review:** {{ meta-handbook.next_review }} (Jährlich)

