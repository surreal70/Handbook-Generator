# Anhang A: Annex A Control Mapping

**Dokumenttyp:** Anhang  
**Version:** 1.0.0  
**Datum:** {{ meta.document.date }}  
**Klassifizierung:** internal

---

## Zweck

Dieses Dokument stellt das vollständige Mapping der ISO/IEC 27001:2022 Annex A Kontrollen auf die implementierten Policies und Richtlinien des ISMS dar. Es dient als zentrale Referenz für die Compliance-Nachweisführung und zeigt auf, wie jede Annex A Kontrolle in der Organisation umgesetzt wird.

Das Mapping berücksichtigt die Änderungen aus Amendment 1:2024 und stellt sicher, dass alle 93 Kontrollen der aktuellen Annex A Version abgedeckt sind.

## Geltungsbereich

**Organisation:** AdminSend GmbH  
**ISMS Scope:** {{ meta.isms.scope }}  
**Verantwortlich:** Thomas Weber (thomas.weber@adminsend.de)

---

## ISO/IEC 27001:2022 Annex A Struktur

Die Annex A Kontrollen sind in vier Hauptkategorien organisiert:

- **Organizational Controls (5.1-5.37):** 37 Kontrollen
- **People Controls (6.1-6.8):** 8 Kontrollen
- **Physical Controls (7.1-7.14):** 14 Kontrollen
- **Technological Controls (8.1-8.34):** 34 Kontrollen

**Gesamt:** 93 Kontrollen

---

## Annex A Control Mapping

### 5. Organizational Controls

#### 5.1 Policies for Information Security

**Control Statement:** Information security policy and topic-specific policies shall be defined, approved by management, published, communicated to and acknowledged by relevant personnel and relevant interested parties, and reviewed at planned intervals and if significant changes occur.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0010_ISMS_Informationssicherheitsleitlinie.md
- Policy: 0200-0680 (Alle Topic-Specific Policies)
- Prozess: 0050_ISMS_Dokumentenlenkung.md

**Verantwortlich:** Thomas Weber  
**Nachweis:** Genehmigte und veröffentlichte Policies, Schulungsnachweise

---

#### 5.2 Information Security Roles and Responsibilities

**Control Statement:** Information security roles and responsibilities shall be defined and allocated according to the organization needs.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Dokument: 0040_ISMS_Governance_Rollen_und_Verantwortlichkeiten.md
- RACI-Matrizen in allen relevanten Policies

**Verantwortlich:** Thomas Weber  
**Nachweis:** RACI-Matrizen, Stellenbeschreibungen, Organigramm

---

#### 5.3 Segregation of Duties

**Control Statement:** Conflicting duties and conflicting areas of responsibility shall be segregated.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0220_Policy_Zugriffssteuerung_und_Identitaetsmanagement.md
- Richtlinie: 0230_Richtlinie_IAM_Joiner_Mover_Leaver_und_Zugriffsantraege.md

**Verantwortlich:** Thomas Weber  
**Nachweis:** Berechtigungskonzept, Zugriffsreviews

---

#### 5.4 Management Responsibilities

**Control Statement:** Management shall require all personnel to apply information security in accordance with the established information security policy, topic-specific policies and procedures of the organization.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0010_ISMS_Informationssicherheitsleitlinie.md
- Dokument: 0120_ISMS_Schulung_Awareness_und_Kompetenz.md

**Verantwortlich:** Management, Thomas Weber  
**Nachweis:** Management-Commitment, Schulungsnachweise

---

#### 5.5 Contact with Authorities

**Control Statement:** The organization shall establish and maintain contact with relevant authorities.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Dokument: 0030_ISMS_Kontext_und_Interessierte_Parteien.md
- Policy: 0400_Policy_Incident_Management.md

**Verantwortlich:** Thomas Weber  
**Nachweis:** Kontaktlisten, Kommunikationsprotokolle

---

#### 5.6 Contact with Special Interest Groups

**Control Statement:** The organization shall establish and maintain contact with special interest groups or other specialist security forums and professional associations.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Dokument: 0030_ISMS_Kontext_und_Interessierte_Parteien.md

**Verantwortlich:** Thomas Weber  
**Nachweis:** Mitgliedschaften, Teilnahmebestätigungen

---

#### 5.7 Threat Intelligence

**Control Statement:** Information relating to information security threats shall be collected and analyzed to produce threat intelligence.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0340_Policy_Vulnerability_und_Patch_Management.md
- Richtlinie: 0350_Richtlinie_Vulnerability_Scans_Patching_und_Exploitation_Response.md

**Verantwortlich:** Security Operations Team  
**Nachweis:** Threat Intelligence Reports, Vulnerability Scans

---

#### 5.8 Information Security in Project Management

**Control Statement:** Information security shall be integrated into project management.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0680_Policy_Security_in_Projects.md
- Richtlinie: 0690_Richtlinie_Sicherheitsanforderungen_im_Projektlebenszyklus.md

**Verantwortlich:** Project Management Office, Thomas Weber  
**Nachweis:** Projektdokumentation, Security Reviews

---

#### 5.9 Inventory of Information and Other Associated Assets

**Control Statement:** An inventory of information and other associated assets, including owners, shall be developed and maintained.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0300_Policy_Asset_Management.md
- Richtlinie: 0310_Richtlinie_Asset_Inventory_Tagging_und_Entsorgung.md
- Anhang: 0720_Anhang_Asset_und_Systeminventar_Template.md

**Verantwortlich:** Asset Management Team  
**Nachweis:** Asset Inventory, CMDB

---

#### 5.10 Acceptable Use of Information and Other Associated Assets

**Control Statement:** Rules for the acceptable use of information and of assets associated with information and information processing facilities shall be identified, documented and implemented.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0200_Policy_Akzeptable_Nutzung_IT.md
- Richtlinie: 0210_Richtlinie_Akzeptable_Nutzung_IT.md

**Verantwortlich:** Thomas Weber  
**Nachweis:** Acceptable Use Policy, Mitarbeiterbestätigungen

---

#### 5.11 Return of Assets

**Control Statement:** Personnel and other interested parties as appropriate shall return all of the organization's assets in their possession upon change or termination of their employment, contract or agreement.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0520_Policy_HR_Security.md
- Richtlinie: 0530_Richtlinie_HR_Onboarding_Rollenwechsel_Offboarding.md

**Verantwortlich:** HR, IT Operations  
**Nachweis:** Offboarding-Checklisten, Asset-Rückgabeprotokolle

---

#### 5.12 Classification of Information

**Control Statement:** Information shall be classified according to the information security needs of the organization based on confidentiality, integrity, availability and relevant interested party requirements.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0280_Policy_Datenklassifizierung_und_Informationshandling.md
- Richtlinie: 0290_Richtlinie_Datenklassifizierung_Labeling_und_Handling.md

**Verantwortlich:** Data Owners, Thomas Weber  
**Nachweis:** Klassifizierungsschema, gelabelte Dokumente

---

#### 5.13 Labelling of Information

**Control Statement:** An appropriate set of procedures for information labelling shall be developed and implemented in accordance with the information classification scheme adopted by the organization.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Richtlinie: 0290_Richtlinie_Datenklassifizierung_Labeling_und_Handling.md

**Verantwortlich:** Data Owners  
**Nachweis:** Labelling-Richtlinien, gelabelte Assets

---

#### 5.14 Information Transfer

**Control Statement:** Information transfer rules, procedures, or agreements shall be in place for all types of transfer facilities within the organization and between the organization and other parties.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0660_Policy_Informationsuebertragung_und_Kommunikation.md
- Richtlinie: 0670_Richtlinie_Email_Sharing_und_Zusammenarbeitstools.md

**Verantwortlich:** Thomas Weber  
**Nachweis:** Transfer-Richtlinien, Verschlüsselungsnachweise

---

#### 5.15 Access Control

**Control Statement:** Rules to control physical and logical access to information and other associated assets shall be established and implemented based on business and information security requirements.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0220_Policy_Zugriffssteuerung_und_Identitaetsmanagement.md
- Richtlinie: 0230_Richtlinie_IAM_Joiner_Mover_Leaver_und_Zugriffsantraege.md

**Verantwortlich:** IAM Team, Thomas Weber  
**Nachweis:** Berechtigungskonzept, Access Reviews

---

#### 5.16 Identity Management

**Control Statement:** The full life cycle of identities shall be managed.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0220_Policy_Zugriffssteuerung_und_Identitaetsmanagement.md
- Richtlinie: 0230_Richtlinie_IAM_Joiner_Mover_Leaver_und_Zugriffsantraege.md

**Verantwortlich:** IAM Team  
**Nachweis:** Identity Lifecycle Prozesse, Joiner/Mover/Leaver Dokumentation

---

#### 5.17 Authentication Information

**Control Statement:** Allocation and management of authentication information shall be controlled by a management process, including advising personnel on appropriate handling of authentication information.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0240_Policy_Authentisierung_und_Passwoerter.md
- Richtlinie: 0250_Richtlinie_MFA_Passwortregeln_und_Session_Management.md

**Verantwortlich:** IAM Team  
**Nachweis:** Passwort-Richtlinien, MFA-Implementierung

---

#### 5.18 Access Rights

**Control Statement:** Access rights to information and other associated assets shall be provisioned, reviewed, modified and removed in accordance with the organization's topic-specific policy on and rules for access control.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Richtlinie: 0230_Richtlinie_IAM_Joiner_Mover_Leaver_und_Zugriffsantraege.md

**Verantwortlich:** IAM Team, Resource Owners  
**Nachweis:** Access Request Workflows, Rezertifizierungsprotokolle

---

#### 5.19 Information Security in Supplier Relationships

**Control Statement:** Processes and procedures shall be defined and implemented to manage the information security risks associated with the use of supplier's products or services.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0460_Policy_Lieferanten_und_Cloud_Sicherheit.md
- Richtlinie: 0470_Richtlinie_Third_Party_Risk_Assessment_und_Cloud_Controls.md

**Verantwortlich:** Procurement, Thomas Weber  
**Nachweis:** Supplier Security Assessments, Verträge

---

#### 5.20 Addressing Information Security within Supplier Agreements

**Control Statement:** Relevant information security requirements shall be established and agreed with each supplier based on the type of supplier relationship.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Richtlinie: 0470_Richtlinie_Third_Party_Risk_Assessment_und_Cloud_Controls.md

**Verantwortlich:** Procurement, Legal, Thomas Weber  
**Nachweis:** Vertragsklauseln, SLAs

---

#### 5.21 Managing Information Security in the ICT Supply Chain

**Control Statement:** Processes and procedures shall be defined and implemented to manage the information security risks associated with the ICT products and services supply chain.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Richtlinie: 0470_Richtlinie_Third_Party_Risk_Assessment_und_Cloud_Controls.md

**Verantwortlich:** Thomas Weber, IT Operations  
**Nachweis:** Supply Chain Risk Assessments

---

#### 5.22 Monitoring, Review and Change Management of Supplier Services

**Control Statement:** The organization shall regularly monitor, review, evaluate and manage change in supplier information security practices and service delivery.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Richtlinie: 0470_Richtlinie_Third_Party_Risk_Assessment_und_Cloud_Controls.md

**Verantwortlich:** Supplier Management, Thomas Weber  
**Nachweis:** Supplier Reviews, Performance Reports

---

#### 5.23 Information Security for Use of Cloud Services

**Control Statement:** Processes for acquisition, use, management and exit from cloud services shall be established in accordance with the organization's information security requirements.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0460_Policy_Lieferanten_und_Cloud_Sicherheit.md
- Richtlinie: 0470_Richtlinie_Third_Party_Risk_Assessment_und_Cloud_Controls.md

**Verantwortlich:** Cloud Governance Team, Thomas Weber  
**Nachweis:** Cloud Security Assessments, Cloud Contracts

---

#### 5.24 Information Security Incident Management Planning and Preparation

**Control Statement:** The organization shall plan and prepare for managing information security incidents by defining, establishing and communicating information security incident management processes, roles and responsibilities.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0400_Policy_Incident_Management.md
- Richtlinie: 0410_Richtlinie_Incident_Response_und_Major_Incident_Prozess.md

**Verantwortlich:** Incident Response Team, Thomas Weber  
**Nachweis:** Incident Response Plan, Runbooks

---

#### 5.25 Assessment and Decision on Information Security Events

**Control Statement:** The organization shall assess information security events and decide if they are to be categorized as information security incidents.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Richtlinie: 0410_Richtlinie_Incident_Response_und_Major_Incident_Prozess.md

**Verantwortlich:** Incident Response Team  
**Nachweis:** Event Classification Criteria, Incident Tickets

---

#### 5.26 Response to Information Security Incidents

**Control Statement:** Information security incidents shall be responded to in accordance with the documented procedures.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Richtlinie: 0410_Richtlinie_Incident_Response_und_Major_Incident_Prozess.md

**Verantwortlich:** Incident Response Team  
**Nachweis:** Incident Response Dokumentation, Post-Mortems

---

#### 5.27 Learning from Information Security Incidents

**Control Statement:** Knowledge gained from information security incidents shall be used to strengthen and improve the information security controls.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Richtlinie: 0410_Richtlinie_Incident_Response_und_Major_Incident_Prozess.md
- Dokument: 0160_ISMS_Kontinuierliche_Verbesserung.md

**Verantwortlich:** Incident Response Team, Thomas Weber  
**Nachweis:** Lessons Learned Dokumentation, Verbesserungsmaßnahmen

---

#### 5.28 Collection of Evidence

**Control Statement:** The organization shall establish and implement procedures for the identification, collection, acquisition and preservation of evidence related to information security events.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Richtlinie: 0410_Richtlinie_Incident_Response_und_Major_Incident_Prozess.md

**Verantwortlich:** Incident Response Team, Forensics Team  
**Nachweis:** Forensics Procedures, Chain of Custody Dokumentation

---

#### 5.29 Information Security During Disruption

**Control Statement:** The organization shall plan how to maintain information security at an appropriate level during disruption.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0440_Policy_Business_Continuity_ICT_Readiness.md
- Richtlinie: 0450_Richtlinie_ICT_DR_Schnittstellen_zu_BCM.md

**Verantwortlich:** BCM Team, Thomas Weber  
**Nachweis:** Business Continuity Plans, DR Tests

---

#### 5.30 ICT Readiness for Business Continuity

**Control Statement:** ICT readiness shall be planned, implemented, maintained and tested based on business continuity objectives and ICT continuity requirements.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0440_Policy_Business_Continuity_ICT_Readiness.md
- Richtlinie: 0450_Richtlinie_ICT_DR_Schnittstellen_zu_BCM.md

**Verantwortlich:** IT Operations, BCM Team  
**Nachweis:** DR Plans, BC Tests, RTO/RPO Dokumentation

---

#### 5.31 Legal, Statutory, Regulatory and Contractual Requirements

**Control Statement:** Legal, statutory, regulatory and contractual requirements relevant to information security and the organization's approach to meet these requirements shall be identified, documented and kept up to date.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Dokument: 0030_ISMS_Kontext_und_Interessierte_Parteien.md
- Policy: 0560_Policy_Datenschutz_Schnittstellen.md

**Verantwortlich:** Legal, Compliance, Thomas Weber  
**Nachweis:** Compliance Register, Legal Reviews

---

#### 5.32 Intellectual Property Rights

**Control Statement:** The organization shall implement appropriate procedures to protect intellectual property rights.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0200_Policy_Akzeptable_Nutzung_IT.md
- Richtlinie: 0290_Richtlinie_Datenklassifizierung_Labeling_und_Handling.md

**Verantwortlich:** Legal, Thomas Weber  
**Nachweis:** IP Protection Procedures, Lizenzmanagement

---

#### 5.33 Protection of Records

**Control Statement:** Records shall be protected from loss, destruction, falsification, unauthorized access and unauthorized release.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0580_Policy_Aufbewahrung_und_Loeschung.md
- Richtlinie: 0590_Richtlinie_Records_Retention_und_Sichere_Loeschung.md

**Verantwortlich:** Records Management, Thomas Weber  
**Nachweis:** Records Retention Policy, Archivierungssysteme

---

#### 5.34 Privacy and Protection of PII

**Control Statement:** The organization shall identify and meet the requirements regarding the preservation of privacy and protection of PII according to applicable laws and regulations and contractual requirements.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0560_Policy_Datenschutz_Schnittstellen.md
- Richtlinie: 0570_Richtlinie_Datenschutz_Anforderungen_und_Datenverarbeitung.md

**Verantwortlich:** Data Protection Officer, Thomas Weber  
**Nachweis:** DSGVO Compliance, Privacy Impact Assessments

---

#### 5.35 Independent Review of Information Security

**Control Statement:** The organization's approach to managing information security and its implementation including people, processes and technologies shall be reviewed independently at planned intervals, or when significant changes occur.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Dokument: 0130_ISMS_Internes_Auditprogramm.md

**Verantwortlich:** Internal Audit, Thomas Weber  
**Nachweis:** Audit Reports, Audit Plans

---

#### 5.36 Compliance with Policies, Rules and Standards for Information Security

**Control Statement:** Compliance with the organization's information security policy, topic-specific policies, rules and standards shall be regularly reviewed.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Dokument: 0130_ISMS_Internes_Auditprogramm.md
- Dokument: 0140_ISMS_Management_Review_Template.md

**Verantwortlich:** Compliance Team, Thomas Weber  
**Nachweis:** Compliance Reviews, Audit Findings

---

#### 5.37 Documented Operating Procedures

**Control Statement:** Operating procedures for information processing facilities shall be documented and made available to personnel who need them.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Alle Richtlinien (0210-0690)
- Dokument: 0050_ISMS_Dokumentenlenkung.md

**Verantwortlich:** IT Operations, Process Owners  
**Nachweis:** Betriebsdokumentation, SOPs, Runbooks

---

### 6. People Controls

#### 6.1 Screening

**Control Statement:** Background verification checks on all candidates for employment shall be carried out prior to joining the organization and on an ongoing basis taking into consideration applicable laws, regulations and ethics and be proportional to the business requirements, the classification of the information to be accessed and the perceived risks.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0520_Policy_HR_Security.md
- Richtlinie: 0530_Richtlinie_HR_Onboarding_Rollenwechsel_Offboarding.md

**Verantwortlich:** HR, Thomas Weber  
**Nachweis:** Background Check Procedures, Screening Records

---

#### 6.2 Terms and Conditions of Employment

**Control Statement:** The employment contractual agreements shall state the personnel's and the organization's responsibilities for information security.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0520_Policy_HR_Security.md
- Richtlinie: 0530_Richtlinie_HR_Onboarding_Rollenwechsel_Offboarding.md

**Verantwortlich:** HR, Legal  
**Nachweis:** Arbeitsverträge, NDA Templates

---

#### 6.3 Information Security Awareness, Education and Training

**Control Statement:** Personnel of the organization and relevant interested parties shall receive appropriate information security awareness, education and training and regular updates of the organization's information security policy, topic-specific policies and procedures, as relevant for their job function.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Dokument: 0120_ISMS_Schulung_Awareness_und_Kompetenz.md

**Verantwortlich:** Thomas Weber, HR  
**Nachweis:** Schulungspläne, Teilnahmebestätigungen, Awareness Kampagnen

---

#### 6.4 Disciplinary Process

**Control Statement:** A disciplinary process shall be formalized and communicated to take actions against personnel and other relevant interested parties who have committed an information security policy violation.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0520_Policy_HR_Security.md
- Dokument: 0150_ISMS_Nichtkonformitaeten_und_Korrekturmassnahmen.md

**Verantwortlich:** HR, Management  
**Nachweis:** Disziplinarverfahren, Dokumentierte Verstöße

---

#### 6.5 Responsibilities After Termination or Change of Employment

**Control Statement:** Information security responsibilities and duties that remain valid after termination or change of employment shall be defined, enforced and communicated to relevant personnel and other interested parties.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0520_Policy_HR_Security.md
- Richtlinie: 0530_Richtlinie_HR_Onboarding_Rollenwechsel_Offboarding.md

**Verantwortlich:** HR, IT Operations  
**Nachweis:** Offboarding Checklisten, Exit Interviews

---

#### 6.6 Confidentiality or Non-Disclosure Agreements

**Control Statement:** Confidentiality or non-disclosure agreements reflecting the organization's needs for the protection of information shall be identified, documented, regularly reviewed and signed by personnel and other relevant interested parties.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0520_Policy_HR_Security.md

**Verantwortlich:** Legal, HR  
**Nachweis:** Unterzeichnete NDAs, Vertraulichkeitsvereinbarungen

---

#### 6.7 Remote Working

**Control Statement:** Security measures shall be implemented when personnel are working remotely to protect information accessed, processed or stored outside the organization's premises.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0500_Policy_Mobile_Device_und_Remote_Work.md
- Richtlinie: 0510_Richtlinie_MDM_BringYourOwnDevice_und_Remote_Access.md

**Verantwortlich:** IT Operations, Thomas Weber  
**Nachweis:** Remote Work Policy, VPN Logs, Endpoint Security

---

#### 6.8 Information Security Event Reporting

**Control Statement:** The organization shall provide a mechanism for personnel to report observed or suspected information security events through appropriate channels in a timely manner.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0400_Policy_Incident_Management.md
- Richtlinie: 0410_Richtlinie_Incident_Response_und_Major_Incident_Prozess.md

**Verantwortlich:** All Personnel, Incident Response Team  
**Nachweis:** Incident Reporting Channels, Event Reports

---

### 7. Physical Controls

#### 7.1 Physical Security Perimeters

**Control Statement:** Security perimeters shall be defined and used to protect areas that contain information and other associated assets.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0480_Policy_Physische_Sicherheit.md
- Richtlinie: 0490_Richtlinie_Zutritt_Besucher_und_Schutz_von_Equipment.md

**Verantwortlich:** Facility Management, Thomas Weber  
**Nachweis:** Sicherheitszonen, Zutrittskontrollsysteme

---

#### 7.2 Physical Entry

**Control Statement:** Secure areas shall be protected by appropriate entry controls and access points.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Richtlinie: 0490_Richtlinie_Zutritt_Besucher_und_Schutz_von_Equipment.md

**Verantwortlich:** Facility Management  
**Nachweis:** Zutrittskontrollsystem, Access Logs

---

#### 7.3 Securing Offices, Rooms and Facilities

**Control Statement:** Physical security for offices, rooms and facilities shall be designed and implemented.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0480_Policy_Physische_Sicherheit.md
- Richtlinie: 0490_Richtlinie_Zutritt_Besucher_und_Schutz_von_Equipment.md

**Verantwortlich:** Facility Management  
**Nachweis:** Sicherheitskonzept Gebäude, Raumschutzmaßnahmen

---

#### 7.4 Physical Security Monitoring

**Control Statement:** Premises shall be continuously monitored for unauthorized physical access.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Richtlinie: 0490_Richtlinie_Zutritt_Besucher_und_Schutz_von_Equipment.md

**Verantwortlich:** Security Operations, Facility Management  
**Nachweis:** Videoüberwachung, Alarmsysteme, Security Logs

---

#### 7.5 Protecting Against Physical and Environmental Threats

**Control Statement:** Protection against physical and environmental threats, such as natural disasters and other intentional or unintentional physical threats to infrastructure shall be designed and implemented.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0480_Policy_Physische_Sicherheit.md
- Policy: 0440_Policy_Business_Continuity_ICT_Readiness.md

**Verantwortlich:** Facility Management, BCM Team  
**Nachweis:** Umweltschutzmaßnahmen, Brandschutz, Klimatisierung

---

#### 7.6 Working in Secure Areas

**Control Statement:** Security measures for working in secure areas shall be designed and implemented.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Richtlinie: 0490_Richtlinie_Zutritt_Besucher_und_Schutz_von_Equipment.md

**Verantwortlich:** Facility Management, Thomas Weber  
**Nachweis:** Clean Desk Policy, Secure Area Procedures

---

#### 7.7 Clear Desk and Clear Screen

**Control Statement:** Clear desk rules for papers and removable storage media and clear screen rules for information processing facilities shall be defined and appropriately enforced.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0480_Policy_Physische_Sicherheit.md
- Policy: 0200_Policy_Akzeptable_Nutzung_IT.md

**Verantwortlich:** All Personnel, Management  
**Nachweis:** Clear Desk Policy, Awareness Training

---

#### 7.8 Equipment Siting and Protection

**Control Statement:** Equipment shall be sited securely and protected.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Richtlinie: 0490_Richtlinie_Zutritt_Besucher_und_Schutz_von_Equipment.md

**Verantwortlich:** IT Operations, Facility Management  
**Nachweis:** Serverraum-Sicherheit, Equipment Protection Measures

---

#### 7.9 Security of Assets Off-Premises

**Control Statement:** Off-site assets shall be protected.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0500_Policy_Mobile_Device_und_Remote_Work.md
- Richtlinie: 0510_Richtlinie_MDM_BringYourOwnDevice_und_Remote_Access.md

**Verantwortlich:** IT Operations, Thomas Weber  
**Nachweis:** Mobile Device Management, Encryption Policies

---

#### 7.10 Storage Media

**Control Statement:** Storage media shall be managed through their life cycle of acquisition, use, transportation and disposal in accordance with the organization's classification scheme and handling requirements.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0300_Policy_Asset_Management.md
- Richtlinie: 0310_Richtlinie_Asset_Inventory_Tagging_und_Entsorgung.md

**Verantwortlich:** IT Operations  
**Nachweis:** Media Handling Procedures, Disposal Records

---

#### 7.11 Supporting Utilities

**Control Statement:** Information processing facilities shall be protected from power failures and other disruptions caused by failures in supporting utilities.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0440_Policy_Business_Continuity_ICT_Readiness.md
- Richtlinie: 0450_Richtlinie_ICT_DR_Schnittstellen_zu_BCM.md

**Verantwortlich:** IT Operations, Facility Management  
**Nachweis:** USV-Systeme, Redundante Stromversorgung

---

#### 7.12 Cabling Security

**Control Statement:** Cables carrying power, data or supporting information services shall be protected from interception, interference or damage.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0480_Policy_Physische_Sicherheit.md
- Policy: 0600_Policy_Netzwerksicherheit.md

**Verantwortlich:** IT Operations, Facility Management  
**Nachweis:** Kabelschutzmaßnahmen, Netzwerkdokumentation

---

#### 7.13 Equipment Maintenance

**Control Statement:** Equipment shall be maintained correctly to ensure availability, integrity and confidentiality of information.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0300_Policy_Asset_Management.md
- Richtlinie: 0310_Richtlinie_Asset_Inventory_Tagging_und_Entsorgung.md

**Verantwortlich:** IT Operations  
**Nachweis:** Wartungspläne, Maintenance Records

---

#### 7.14 Secure Disposal or Re-use of Equipment

**Control Statement:** Items of equipment containing storage media shall be verified to ensure that any sensitive data and licensed software has been removed or securely overwritten prior to disposal or re-use.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Richtlinie: 0310_Richtlinie_Asset_Inventory_Tagging_und_Entsorgung.md
- Policy: 0580_Policy_Aufbewahrung_und_Loeschung.md

**Verantwortlich:** IT Operations  
**Nachweis:** Secure Disposal Procedures, Wiping Certificates

---

### 8. Technological Controls

#### 8.1 User Endpoint Devices

**Control Statement:** Information stored on, processed by or accessible via user endpoint devices shall be protected.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0620_Policy_Endpoint_Security.md
- Richtlinie: 0630_Richtlinie_EDR_AV_Host_Firewall_und_Device_Compliance.md

**Verantwortlich:** IT Operations, Thomas Weber  
**Nachweis:** Endpoint Protection, Device Compliance Policies

---

#### 8.2 Privileged Access Rights

**Control Statement:** The allocation and use of privileged access rights shall be restricted and managed.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0220_Policy_Zugriffssteuerung_und_Identitaetsmanagement.md
- Richtlinie: 0230_Richtlinie_IAM_Joiner_Mover_Leaver_und_Zugriffsantraege.md

**Verantwortlich:** IAM Team, Thomas Weber  
**Nachweis:** Privileged Access Management, PAM Logs

---

#### 8.3 Information Access Restriction

**Control Statement:** Access to information and other associated assets shall be restricted in accordance with the established topic-specific policy on access control.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0220_Policy_Zugriffssteuerung_und_Identitaetsmanagement.md
- Richtlinie: 0230_Richtlinie_IAM_Joiner_Mover_Leaver_und_Zugriffsantraege.md

**Verantwortlich:** IAM Team, Data Owners  
**Nachweis:** Access Control Lists, Authorization Policies

---

#### 8.4 Access to Source Code

**Control Statement:** Read and write access to source code, development tools and software libraries shall be appropriately managed.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0380_Policy_Secure_Development.md
- Richtlinie: 0390_Richtlinie_Secure_SDLC_Coding_Review_und_Secrets.md

**Verantwortlich:** Development Team, Thomas Weber  
**Nachweis:** Source Code Access Controls, Git Permissions

---

#### 8.5 Secure Authentication

**Control Statement:** Secure authentication technologies and procedures shall be implemented based on information access restrictions and the topic-specific policy on access control.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0240_Policy_Authentisierung_und_Passwoerter.md
- Richtlinie: 0250_Richtlinie_MFA_Passwortregeln_und_Session_Management.md

**Verantwortlich:** IAM Team  
**Nachweis:** MFA Implementation, Authentication Logs

---

#### 8.6 Capacity Management

**Control Statement:** The use of resources shall be monitored and adjusted in line with current and expected capacity requirements.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0320_Policy_Logging_und_Monitoring.md
- Richtlinie: 0330_Richtlinie_Logging_SIEM_und_Audit_Trails.md

**Verantwortlich:** IT Operations  
**Nachweis:** Capacity Monitoring, Performance Reports

---

#### 8.7 Protection Against Malware

**Control Statement:** Protection against malware shall be implemented and supported by appropriate user awareness.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0620_Policy_Endpoint_Security.md
- Richtlinie: 0630_Richtlinie_EDR_AV_Host_Firewall_und_Device_Compliance.md

**Verantwortlich:** IT Operations, Thomas Weber  
**Nachweis:** Antivirus/EDR Deployment, Malware Detection Logs

---

#### 8.8 Management of Technical Vulnerabilities

**Control Statement:** Information about technical vulnerabilities of information systems in use shall be obtained, the organization's exposure to such vulnerabilities shall be evaluated and appropriate measures shall be taken.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0340_Policy_Vulnerability_und_Patch_Management.md
- Richtlinie: 0350_Richtlinie_Vulnerability_Scans_Patching_und_Exploitation_Response.md

**Verantwortlich:** Security Operations, IT Operations  
**Nachweis:** Vulnerability Scans, Patch Management Reports

---

#### 8.9 Configuration Management

**Control Statement:** Configurations, including security configurations, of hardware, software, services and networks shall be established, documented, implemented, monitored and reviewed.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0540_Policy_Konfiguration_und_Hardening.md
- Richtlinie: 0550_Richtlinie_Sicherheitsbaselines_Hardening_und_Konfig_Aenderungen.md

**Verantwortlich:** IT Operations, Thomas Weber  
**Nachweis:** Configuration Management Database, Baseline Configurations

---

#### 8.10 Information Deletion

**Control Statement:** Information stored in information systems, devices or in any other storage media shall be deleted when no longer required.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0580_Policy_Aufbewahrung_und_Loeschung.md
- Richtlinie: 0590_Richtlinie_Records_Retention_und_Sichere_Loeschung.md

**Verantwortlich:** Data Owners, IT Operations  
**Nachweis:** Data Retention Policy, Deletion Logs

---

#### 8.11 Data Masking

**Control Statement:** Data masking shall be used in accordance with the organization's topic-specific policy on access control and other related topic-specific policies, and business requirements, taking applicable legislation into consideration.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0560_Policy_Datenschutz_Schnittstellen.md
- Richtlinie: 0570_Richtlinie_Datenschutz_Anforderungen_und_Datenverarbeitung.md

**Verantwortlich:** Development Team, Data Protection Officer  
**Nachweis:** Data Masking Procedures, Test Data Management

---

#### 8.12 Data Leakage Prevention

**Control Statement:** Data leakage prevention measures shall be applied to systems, networks and any other devices that process, store or transmit sensitive information.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0280_Policy_Datenklassifizierung_und_Informationshandling.md
- Richtlinie: 0290_Richtlinie_Datenklassifizierung_Labeling_und_Handling.md

**Verantwortlich:** Security Operations, Thomas Weber  
**Nachweis:** DLP Implementation, DLP Alerts

---

#### 8.13 Information Backup

**Control Statement:** Backup copies of information, software and systems shall be maintained and regularly tested in accordance with the agreed topic-specific policy on backup.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0420_Policy_Backup_und_Wiederherstellung.md
- Richtlinie: 0430_Richtlinie_Backup_Restore_und_Regelmaessige_Tests.md

**Verantwortlich:** IT Operations  
**Nachweis:** Backup Policies, Restore Tests, Backup Logs

---

#### 8.14 Redundancy of Information Processing Facilities

**Control Statement:** Information processing facilities shall be implemented with redundancy sufficient to meet availability requirements.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0440_Policy_Business_Continuity_ICT_Readiness.md
- Richtlinie: 0450_Richtlinie_ICT_DR_Schnittstellen_zu_BCM.md

**Verantwortlich:** IT Operations, IT Architecture  
**Nachweis:** High Availability Designs, Redundancy Documentation

---

#### 8.15 Logging

**Control Statement:** Logs that record activities, exceptions, faults and other relevant events shall be produced, stored, protected and analyzed.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0320_Policy_Logging_und_Monitoring.md
- Richtlinie: 0330_Richtlinie_Logging_SIEM_und_Audit_Trails.md

**Verantwortlich:** IT Operations, Security Operations  
**Nachweis:** Logging Standards, SIEM Implementation, Log Retention

---

#### 8.16 Monitoring Activities

**Control Statement:** Networks, systems and applications shall be monitored for anomalous behaviour and appropriate actions taken to evaluate potential information security incidents.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0320_Policy_Logging_und_Monitoring.md
- Richtlinie: 0330_Richtlinie_Logging_SIEM_und_Audit_Trails.md

**Verantwortlich:** Security Operations  
**Nachweis:** SIEM Use Cases, Monitoring Dashboards, Alerts

---

#### 8.17 Clock Synchronization

**Control Statement:** The clocks of information processing systems used by the organization shall be synchronized to approved time sources.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0540_Policy_Konfiguration_und_Hardening.md
- Richtlinie: 0550_Richtlinie_Sicherheitsbaselines_Hardening_und_Konfig_Aenderungen.md

**Verantwortlich:** IT Operations  
**Nachweis:** NTP Configuration, Time Synchronization Logs

---

#### 8.18 Use of Privileged Utility Programs

**Control Statement:** The use of utility programs that can be capable of overriding system and application controls shall be restricted and tightly controlled.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0220_Policy_Zugriffssteuerung_und_Identitaetsmanagement.md
- Richtlinie: 0230_Richtlinie_IAM_Joiner_Mover_Leaver_und_Zugriffsantraege.md

**Verantwortlich:** IT Operations, Thomas Weber  
**Nachweis:** Privileged Access Controls, Utility Program Restrictions

---

#### 8.19 Installation of Software on Operational Systems

**Control Statement:** Procedures and measures shall be implemented to securely manage software installation on operational systems.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0360_Policy_Change_und_Release_Management.md
- Richtlinie: 0370_Richtlinie_Change_Management_mit_Sicherheitsfreigaben.md

**Verantwortlich:** IT Operations, Change Management  
**Nachweis:** Software Installation Procedures, Change Records

---

#### 8.20 Networks Security

**Control Statement:** Networks and network devices shall be secured, managed and controlled to protect information in systems and applications.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0600_Policy_Netzwerksicherheit.md
- Richtlinie: 0610_Richtlinie_Segmentierung_Firewalling_und_Network_Access_Control.md

**Verantwortlich:** Network Team, Thomas Weber  
**Nachweis:** Network Security Architecture, Firewall Rules

---

#### 8.21 Security of Network Services

**Control Statement:** Security mechanisms, service levels and service requirements of network services shall be identified, implemented and monitored.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0600_Policy_Netzwerksicherheit.md
- Richtlinie: 0610_Richtlinie_Segmentierung_Firewalling_und_Network_Access_Control.md

**Verantwortlich:** Network Team  
**Nachweis:** Network Service SLAs, Security Monitoring

---

#### 8.22 Segregation of Networks

**Control Statement:** Groups of information services, users and information systems shall be segregated in the organization's networks.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Richtlinie: 0610_Richtlinie_Segmentierung_Firewalling_und_Network_Access_Control.md

**Verantwortlich:** Network Team, Thomas Weber  
**Nachweis:** Network Segmentation Design, VLAN Configuration

---

#### 8.23 Web Filtering

**Control Statement:** Access to external websites shall be managed to reduce exposure to malicious content.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0600_Policy_Netzwerksicherheit.md
- Policy: 0620_Policy_Endpoint_Security.md

**Verantwortlich:** Security Operations, IT Operations  
**Nachweis:** Web Filtering Solution, Blocked Content Logs

---

#### 8.24 Use of Cryptography

**Control Statement:** Rules for the effective use of cryptography, including cryptographic key management, shall be defined and implemented.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0260_Policy_Kryptografie_und_Schluesselmanagement.md
- Richtlinie: 0270_Richtlinie_Key_Management_und_Verschluesselung.md

**Verantwortlich:** Thomas Weber, IT Operations  
**Nachweis:** Cryptography Policy, Key Management Procedures

---

#### 8.25 Secure Development Life Cycle

**Control Statement:** Rules for the secure development of software and systems shall be established and applied.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0380_Policy_Secure_Development.md
- Richtlinie: 0390_Richtlinie_Secure_SDLC_Coding_Review_und_Secrets.md

**Verantwortlich:** Development Team, Thomas Weber  
**Nachweis:** Secure SDLC Procedures, Code Review Records

---

#### 8.26 Application Security Requirements

**Control Statement:** Information security requirements shall be identified, specified and approved when developing or acquiring applications.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0380_Policy_Secure_Development.md
- Richtlinie: 0390_Richtlinie_Secure_SDLC_Coding_Review_und_Secrets.md

**Verantwortlich:** Development Team, Security Architecture  
**Nachweis:** Security Requirements Specifications, Threat Models

---

#### 8.27 Secure System Architecture and Engineering Principles

**Control Statement:** Principles for engineering secure systems shall be established, documented, maintained and applied to any information system development activities.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0380_Policy_Secure_Development.md
- Richtlinie: 0390_Richtlinie_Secure_SDLC_Coding_Review_und_Secrets.md

**Verantwortlich:** Security Architecture, Development Team  
**Nachweis:** Secure Architecture Principles, Design Reviews

---

#### 8.28 Secure Coding

**Control Statement:** Secure coding principles shall be applied to software development.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Richtlinie: 0390_Richtlinie_Secure_SDLC_Coding_Review_und_Secrets.md

**Verantwortlich:** Development Team  
**Nachweis:** Secure Coding Guidelines, SAST/DAST Results

---

#### 8.29 Security Testing in Development and Acceptance

**Control Statement:** Security testing processes shall be defined and implemented in the development life cycle.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Richtlinie: 0390_Richtlinie_Secure_SDLC_Coding_Review_und_Secrets.md

**Verantwortlich:** Development Team, Security Team  
**Nachweis:** Security Test Plans, Penetration Test Reports

---

#### 8.30 Outsourced Development

**Control Statement:** The organization shall direct, monitor and review the activities related to outsourced system development.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0460_Policy_Lieferanten_und_Cloud_Sicherheit.md
- Richtlinie: 0470_Richtlinie_Third_Party_Risk_Assessment_und_Cloud_Controls.md

**Verantwortlich:** Development Team, Thomas Weber  
**Nachweis:** Supplier Contracts, Development Oversight Records

---

#### 8.31 Separation of Development, Test and Production Environments

**Control Statement:** Development, testing and production environments shall be separated and secured.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0380_Policy_Secure_Development.md
- Richtlinie: 0390_Richtlinie_Secure_SDLC_Coding_Review_und_Secrets.md

**Verantwortlich:** Development Team, IT Operations  
**Nachweis:** Environment Separation, Access Controls per Environment

---

#### 8.32 Change Management

**Control Statement:** Changes to information processing facilities and information systems shall be subject to change management procedures.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0360_Policy_Change_und_Release_Management.md
- Richtlinie: 0370_Richtlinie_Change_Management_mit_Sicherheitsfreigaben.md

**Verantwortlich:** Change Management, IT Operations  
**Nachweis:** Change Management Process, Change Records

---

#### 8.33 Test Information

**Control Statement:** Test information shall be appropriately selected, protected and managed.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Policy: 0560_Policy_Datenschutz_Schnittstellen.md
- Richtlinie: 0570_Richtlinie_Datenschutz_Anforderungen_und_Datenverarbeitung.md

**Verantwortlich:** Development Team, Data Protection Officer  
**Nachweis:** Test Data Management, Data Masking Procedures

---

#### 8.34 Protection of Information Systems During Audit Testing

**Control Statement:** Audit tests and other assurance activities involving assessment of operational systems shall be planned and agreed between the tester and appropriate management.

**Implementierungsstatus:** ☑ Implementiert  
**Umsetzung in ISMS:**
- Dokument: 0130_ISMS_Internes_Auditprogramm.md

**Verantwortlich:** Internal Audit, IT Operations  
**Nachweis:** Audit Plans, Test Approvals, Audit Protocols

---

## Amendment 1:2024 Änderungen

**Hinweis:** ISO/IEC 27001:2022 Amendment 1:2024 führt keine neuen Kontrollen ein, sondern präzisiert bestehende Kontrollen und aktualisiert Referenzen. Die wichtigsten Änderungen betreffen:

- **5.7 Threat Intelligence:** Erweiterte Anforderungen an Threat Intelligence Prozesse
- **5.23 Information Security for Use of Cloud Services:** Aktualisierte Cloud Security Anforderungen
- **8.11 Data Masking:** Neue Kontrolle für Datenmaskierung (bereits in 2022 enthalten)
- **8.12 Data Leakage Prevention:** Neue Kontrolle für DLP (bereits in 2022 enthalten)

Alle Änderungen sind in diesem Mapping bereits berücksichtigt.

---

## Zusammenfassung

### Implementierungsstatus Übersicht

| Kategorie | Anzahl Kontrollen | Implementiert | Teilweise | Nicht implementiert |
|-----------|-------------------|---------------|-----------|---------------------|
| Organizational Controls (5.x) | 37 | 37 | 0 | 0 |
| People Controls (6.x) | 8 | 8 | 0 | 0 |
| Physical Controls (7.x) | 14 | 14 | 0 | 0 |
| Technological Controls (8.x) | 34 | 34 | 0 | 0 |
| **Gesamt** | **93** | **93** | **0** | **0** |

**Implementierungsgrad:** 100%

---

## Verwendung dieses Mappings

Dieses Mapping dient als:

1. **Compliance-Nachweis:** Zeigt auf, wie jede Annex A Kontrolle umgesetzt wird
2. **Audit-Vorbereitung:** Ermöglicht schnelle Identifikation relevanter Dokumente
3. **Gap-Analyse:** Identifiziert fehlende oder unvollständige Implementierungen
4. **Wartung:** Unterstützt bei der Aktualisierung des ISMS

**Aktualisierung:** Dieses Dokument sollte bei jeder Änderung an Policies, Richtlinien oder Kontrollen aktualisiert werden.

---

## Referenzen

- ISO/IEC 27001:2022 Information Security Management Systems - Requirements
- ISO/IEC 27001:2022/Amd 1:2024 Amendment 1
- ISO/IEC 27002:2022 Information Security Controls
- Statement of Applicability (SoA): 0100_ISMS_Statement_of_Applicability_SoA_Template.md

---

**Dokumentverantwortlicher:** Thomas Weber  
**Genehmigt durch:** {{ meta.management.name }}  
**Nächste Überprüfung:** {{ meta.document.next_review }}


