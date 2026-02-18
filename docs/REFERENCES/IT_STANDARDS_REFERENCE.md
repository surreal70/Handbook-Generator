# IT Standards Reference Guide

**Document Version:** 1.0  
**Last Updated:** 2026-02-18  
**Purpose:** Reference guide for IT-related NIST and BSI publications with framework mappings

---

## Overview

This document provides a comprehensive reference to IT-related standards and publications from:
- **NIST** (National Institute of Standards and Technology, USA)
- **BSI** (Bundesamt für Sicherheit in der Informationstechnik, Germany)

Each standard includes references to existing framework templates where applicable.

---

## NIST Publications

### NIST Special Publications (SP) - Cybersecurity

#### NIST SP 800-53 Rev. 5 - Security and Privacy Controls

**Full Title:** Security and Privacy Controls for Information Systems and Organizations  
**Published:** September 2020  
**URL:** https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final

**Description:**
Comprehensive catalog of security and privacy controls for federal information systems and organizations. Provides a structured set of safeguards for protecting the confidentiality, integrity, and availability of information and systems.

**Control Families:**
- AC (Access Control)
- AT (Awareness and Training)
- AU (Audit and Accountability)
- CA (Assessment, Authorization, and Monitoring)
- CM (Configuration Management)
- CP (Contingency Planning)
- IA (Identification and Authentication)
- IR (Incident Response)
- MA (Maintenance)
- MP (Media Protection)
- PE (Physical and Environmental Protection)
- PL (Planning)
- PM (Program Management)
- PS (Personnel Security)
- PT (PII Processing and Transparency)
- RA (Risk Assessment)
- SA (System and Services Acquisition)
- SC (System and Communications Protection)
- SI (System and Information Integrity)
- SR (Supply Chain Risk Management)

**Framework Support:**
- ✅ **Implemented:** [templates/en/nist-800-53/](../templates/en/nist-800-53/)
- 📄 **Mapping:** [templates/en/nist-800-53/9999_Framework_Mapping.md](../templates/en/nist-800-53/9999_Framework_Mapping.md)
- 🔗 **Related:** NIST CSF, ISO 27001, FedRAMP

---

#### NIST SP 800-53B - Control Baselines

**Full Title:** Control Baselines for Information Systems and Organizations  
**Published:** December 2020  
**URL:** https://csrc.nist.gov/publications/detail/sp/800-53b/final

**Description:**
Provides security and privacy control baselines for federal information systems and organizations. Defines three impact levels: Low, Moderate, and High.

**Baselines:**
- **Low Impact:** Minimum security controls
- **Moderate Impact:** Standard security controls
- **High Impact:** Enhanced security controls

**Framework Support:**
- ✅ **Integrated in:** NIST 800-53 templates
- 📄 **Reference:** Control baseline selection documented in templates

---

#### NIST Cybersecurity Framework (CSF) 2.0

**Full Title:** Framework for Improving Critical Infrastructure Cybersecurity  
**Published:** February 2024  
**URL:** https://www.nist.gov/cyberframework

**Description:**
Voluntary framework for managing cybersecurity risk. Provides a common language for understanding, managing, and expressing cybersecurity risk.

**Core Functions:**
- **Govern (GV):** Organizational context, risk management strategy, roles and responsibilities
- **Identify (ID):** Asset management, risk assessment, improvement
- **Protect (PR):** Identity management, awareness, data security, platform security
- **Detect (DE):** Continuous monitoring, adverse event analysis
- **Respond (RS):** Incident management, analysis, mitigation, reporting, communication
- **Recover (RC):** Incident recovery planning, improvements, communications

**Framework Support:**
- ✅ **Implemented:** [templates/en/nist-csf/](../templates/en/nist-csf/)
- 📄 **Mapping:** [templates/en/nist-csf/9999_Framework_Mapping.md](../templates/en/nist-csf/9999_Framework_Mapping.md)
- 🔗 **Related:** NIST 800-53, ISO 27001, CIS Controls

---

#### NIST SP 800-37 Rev. 2 - Risk Management Framework

**Full Title:** Risk Management Framework for Information Systems and Organizations  
**Published:** December 2018  
**URL:** https://csrc.nist.gov/publications/detail/sp/800-37/rev-2/final

**Description:**
Provides a disciplined, structured, and flexible process for managing security and privacy risk. Integrates security, privacy, and cyber supply chain risk management activities into the system development life cycle.

**RMF Steps:**
1. Prepare
2. Categorize
3. Select
4. Implement
5. Assess
6. Authorize
7. Monitor

**Framework Support:**
- 🔗 **Related:** NIST 800-53 (control selection), NIST CSF (risk management)
- 📝 **Guidance:** Risk management processes documented in ISMS and NIST frameworks

---

#### NIST SP 800-171 Rev. 2 - Protecting CUI

**Full Title:** Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations  
**Published:** February 2020  
**URL:** https://csrc.nist.gov/publications/detail/sp/800-171/rev-2/final

**Description:**
Provides recommended security requirements for protecting the confidentiality of Controlled Unclassified Information (CUI) in nonfederal systems and organizations.

**Control Families:** (Subset of 800-53)
- 14 families with 110 security requirements

**Framework Support:**
- 🔗 **Related:** NIST 800-53, CMMC
- 📝 **Guidance:** Controls can be mapped to NIST 800-53 templates

---

#### NIST SP 800-30 Rev. 1 - Risk Assessment

**Full Title:** Guide for Conducting Risk Assessments  
**Published:** September 2012  
**URL:** https://csrc.nist.gov/publications/detail/sp/800-30/rev-1/final

**Description:**
Provides guidance for conducting risk assessments of federal information systems and organizations. Amplifies the guidance in NIST SP 800-39.

**Framework Support:**
- 🔗 **Related:** ISO 31000, NIST CSF, ISO 27001
- 📝 **Guidance:** Risk assessment methodology in ISMS and risk management frameworks

---

#### NIST SP 800-61 Rev. 2 - Incident Handling

**Full Title:** Computer Security Incident Handling Guide  
**Published:** August 2012  
**URL:** https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final

**Description:**
Provides guidelines for incident handling, particularly for analyzing incident-related data and determining the appropriate response to each incident.

**Incident Response Lifecycle:**
1. Preparation
2. Detection and Analysis
3. Containment, Eradication, and Recovery
4. Post-Incident Activity

**Framework Support:**
- ✅ **Integrated in:** ISMS, BCM, NIST 800-53 templates
- 📝 **Guidance:** Incident response procedures in security frameworks

---

#### NIST SP 800-34 Rev. 1 - Contingency Planning

**Full Title:** Contingency Planning Guide for Federal Information Systems  
**Published:** May 2010  
**URL:** https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final

**Description:**
Provides instructions, recommendations, and considerations for federal information system contingency planning.

**Framework Support:**
- ✅ **Integrated in:** BCM templates
- 📄 **Reference:** [templates/en/bcm/](../templates/en/bcm/)
- 🔗 **Related:** ISO 22301, Business Continuity Management

---

#### NIST SP 800-137 - Information Security Continuous Monitoring

**Full Title:** Information Security Continuous Monitoring (ISCM) for Federal Information Systems and Organizations  
**Published:** September 2011  
**URL:** https://csrc.nist.gov/publications/detail/sp/800-137/final

**Description:**
Provides guidance for establishing, implementing, and maintaining an ISCM program.

**Framework Support:**
- 🔗 **Related:** NIST 800-53 (monitoring controls), NIST CSF (Detect function)
- 📝 **Guidance:** Monitoring processes in ISMS and security frameworks

---

#### NIST SP 800-160 Vol. 1 - Systems Security Engineering

**Full Title:** Systems Security Engineering: Considerations for a Multidisciplinary Approach  
**Published:** November 2016 (Updated March 2018)  
**URL:** https://csrc.nist.gov/publications/detail/sp/800-160/vol-1/final

**Description:**
Provides a basis for developing systems security engineering processes, practices, and techniques.

**Framework Support:**
- 🔗 **Related:** Secure SDLC, Common Criteria
- 📝 **Guidance:** Security engineering principles in development frameworks

---

### NIST Special Publications - Privacy

#### NIST Privacy Framework 1.0

**Full Title:** NIST Privacy Framework: A Tool for Improving Privacy through Enterprise Risk Management  
**Published:** January 2020  
**URL:** https://www.nist.gov/privacy-framework

**Description:**
Voluntary tool to help organizations identify and manage privacy risk and build innovative products and services while protecting individuals' privacy.

**Core Functions:**
- Identify-P
- Govern-P
- Control-P
- Communicate-P
- Protect-P

**Framework Support:**
- 🔗 **Related:** GDPR, HIPAA, NIST CSF
- 📝 **Guidance:** Privacy controls in GDPR and privacy frameworks

---

### NIST Cybersecurity White Papers

#### NIST Cybersecurity Supply Chain Risk Management (C-SCRM)

**URL:** https://csrc.nist.gov/projects/cyber-supply-chain-risk-management

**Framework Support:**
- 🔗 **Related:** NIST 800-53 (SR family), ISO 27001
- 📝 **Guidance:** Supply chain risk in security frameworks

---

## BSI Publications

### BSI Standards

#### BSI Standard 200-1 - Information Security Management Systems (ISMS)

**Full Title:** Management Systems for Information Security (ISMS)  
**Version:** 1.0 (October 2017)  
**URL:** https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/BSI-Standards/bsi-standards_node.html

**Description:**
Describes general requirements for an information security management system (ISMS) based on IT-Grundschutz. Provides the foundation for establishing, implementing, operating, monitoring, reviewing, maintaining, and improving an ISMS.

**Content:**
- ISMS organization and responsibilities
- Security process
- Resource management
- ISMS documentation
- Management review

**Framework Support:**
- ✅ **Implemented:** [templates/de/bsi-grundschutz/](../templates/de/bsi-grundschutz/)
- 📄 **Mapping:** [templates/de/bsi-grundschutz/9999_Framework_Mapping.md](../templates/de/bsi-grundschutz/9999_Framework_Mapping.md)
- 🔗 **Related:** ISO 27001, ISMS

---

#### BSI Standard 200-2 - IT-Grundschutz Methodology

**Full Title:** IT-Grundschutz Methodology  
**Version:** 2.0 (September 2017)  
**URL:** https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/BSI-Standards/bsi-standards_node.html

**Description:**
Describes the IT-Grundschutz methodology for establishing and maintaining information security. Provides step-by-step guidance for implementing IT-Grundschutz.

**Methodology Steps:**
1. Initiation of the security process
2. Creation of a security concept
3. Implementation of the security concept
4. Maintenance and continuous improvement

**Core Activities:**
- Scope definition
- Asset identification
- Protection requirements assessment
- Modeling (mapping to IT-Grundschutz Compendium)
- Base security check
- Risk analysis (for high protection requirements)
- Implementation planning

**Framework Support:**
- ✅ **Implemented:** BSI Grundschutz templates
- 📝 **Guidance:** Methodology documented in templates 0040-0090

---

#### BSI Standard 200-3 - Risk Analysis

**Full Title:** Risk Analysis based on IT-Grundschutz  
**Version:** 1.0 (September 2017)  
**URL:** https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/BSI-Standards/bsi-standards_node.html

**Description:**
Describes how to perform a risk analysis for assets with high or very high protection requirements that go beyond standard IT-Grundschutz safeguards.

**Risk Analysis Process:**
1. Preparation
2. Threat and vulnerability identification
3. Risk determination
4. Risk treatment
5. Consolidation

**Framework Support:**
- ✅ **Implemented:** BSI Grundschutz templates
- 📝 **Guidance:** Template 0090_Risikoanalyse_nach_BSI_200_3_Template.md

---

#### BSI Standard 200-4 - Business Continuity Management

**Full Title:** Business Continuity Management  
**Version:** 1.0 (October 2017)  
**URL:** https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/BSI-Standards/bsi-standards_node.html

**Description:**
Describes requirements and recommendations for establishing a Business Continuity Management (BCM) system. Complements ISO 22301.

**BCM Process:**
- BCM organization
- Business impact analysis
- BCM strategy
- Emergency management
- Tests and exercises
- Awareness and training

**Framework Support:**
- ✅ **Implemented:** [templates/de/bcm/](../templates/de/bcm/)
- 📄 **Mapping:** [templates/de/bcm/9999_Framework_Mapping.md](../templates/de/bcm/9999_Framework_Mapping.md)
- 🔗 **Related:** ISO 22301

---

### IT-Grundschutz Compendium

#### IT-Grundschutz Compendium (Edition 2024)

**Full Title:** IT-Grundschutz Compendium  
**Version:** Edition 2024  
**URL:** https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Compendium/it-grundschutz-compendium_node.html

**Description:**
Collection of IT-Grundschutz modules (formerly "catalogues") containing security requirements for typical IT systems, components, and processes.

**Module Structure:**
- **ISMS Modules:** Organization and management
- **ORP Modules:** Organization and personnel
- **CON Modules:** Concepts and procedures
- **OPS Modules:** Operations
- **DER Modules:** Detection and reaction
- **APP Modules:** Applications
- **SYS Modules:** IT systems
- **IND Modules:** Industrial IT
- **NET Modules:** Networks and communication
- **INF Modules:** Infrastructure

**Framework Support:**
- ✅ **Implemented:** BSI Grundschutz templates reference modules
- 📝 **Guidance:** Module mapping in BSI Grundschutz framework

---

### BSI Technical Guidelines (TR)

#### BSI TR-02102 - Cryptographic Mechanisms

**Full Title:** Cryptographic Mechanisms: Recommendations and Key Lengths  
**URL:** https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr02102/tr02102_node.html

**Description:**
Provides recommendations for cryptographic mechanisms and key lengths for various security levels and application scenarios.

**Parts:**
- Part 1: Cryptographic Mechanisms - Recommendations and Key Lengths
- Part 2: Use of Transport Layer Security (TLS)
- Part 3: Use of Internet Protocol Security (IPsec) and Internet Key Exchange (IKEv2)
- Part 4: Use of Secure Shell (SSH)

**Framework Support:**
- 🔗 **Related:** ISO 27001 (A.8.24 Cryptography), NIST 800-53 (SC family)
- 📝 **Guidance:** Cryptography policies in security frameworks

---

#### BSI TR-03116 - eCard-API-Framework

**Full Title:** eCard-API-Framework  
**URL:** https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr03116/TR-03116_node.html

**Description:**
Specifies interfaces for electronic identity cards and signature cards.

**Framework Support:**
- 🔗 **Related:** Identity management, authentication
- 📝 **Guidance:** IAM frameworks

---

#### BSI TR-03148 - Secure Broadband Router

**Full Title:** Secure Broadband Router  
**URL:** https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr03148/TR-03148_node.html

**Description:**
Security requirements for broadband routers.

**Framework Support:**
- 🔗 **Related:** Network security, CIS Controls
- 📝 **Guidance:** Network device hardening

---

### BSI Cloud Computing Compliance Controls Catalogue (C5)

#### Cloud Computing Compliance Criteria Catalogue (C5:2020)

**Full Title:** Cloud Computing Compliance Criteria Catalogue  
**Version:** 2020  
**URL:** https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Cloud-Computing/Kriterienkatalog-C5/kriterienkatalog-c5_node.html

**Description:**
Attestation scheme for cloud service providers. Defines minimum security requirements for cloud computing.

**Control Areas:**
- Organization of Information Security
- Compliance
- Human Resources Security
- Asset Management
- Access Control
- Cryptography
- Physical and Environmental Security
- Operations Security
- Communications Security
- System Acquisition, Development and Maintenance
- Supplier Relationships
- Information Security Incident Management
- Business Continuity Management
- Identity and Access Management
- Data Protection
- Cloud-specific Controls
- Threat Defense

**Framework Support:**
- 🔗 **Related:** CSA CCM, ISO 27001, SOC 2
- 📝 **Guidance:** Cloud security controls in CSA CCM framework

---

### BSI Minimum Standards

#### Minimum Standard for Web Browsers

**URL:** https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Mindeststandards/mindeststandards_node.html

**Framework Support:**
- 🔗 **Related:** CIS Controls, endpoint security
- 📝 **Guidance:** Browser hardening in CIS Controls templates

---

#### Minimum Standard for Email Security

**URL:** https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Mindeststandards/mindeststandards_node.html

**Framework Support:**
- 🔗 **Related:** Email security policies
- 📝 **Guidance:** Email security in ISMS and BSI Grundschutz

---

## Cross-Reference: NIST ↔ BSI

### Equivalent Standards

| NIST Publication | BSI Equivalent | Notes |
|---|---|---|
| NIST SP 800-53 | IT-Grundschutz Compendium | Control catalogs |
| NIST CSF | BSI Standard 200-2 | Framework/Methodology |
| NIST SP 800-37 (RMF) | BSI Standard 200-3 | Risk management |
| NIST SP 800-34 | BSI Standard 200-4 | Business continuity |
| NIST SP 800-61 | IT-Grundschutz DER modules | Incident response |
| NIST Privacy Framework | GDPR compliance (BSI guidance) | Privacy |

### Framework Alignment

**ISO 27001 as Bridge:**
- NIST 800-53 controls map to ISO 27001 Annex A
- BSI IT-Grundschutz aligns with ISO 27001
- Both NIST and BSI can be mapped through ISO 27001

**Implementation Approach:**
1. Choose primary framework (NIST or BSI)
2. Use ISO 27001 as common language
3. Map additional requirements from other framework
4. Document deviations and additional controls

---

## Framework Selection Guide

### When to Use NIST Standards

**Best For:**
- US federal agencies (mandatory)
- US contractors and suppliers
- FedRAMP cloud services
- International organizations preferring US standards
- Organizations with US compliance requirements

**Advantages:**
- Comprehensive control catalog (800-53)
- Flexible framework approach (CSF)
- Strong privacy integration
- Extensive guidance documents
- Free and publicly available

---

### When to Use BSI Standards

**Best For:**
- German government agencies (mandatory)
- German organizations
- Organizations operating in Germany
- EU organizations preferring German standards
- IT-Grundschutz certification

**Advantages:**
- Structured methodology (200-2)
- Detailed implementation guidance
- German language support
- EU/German legal alignment
- Modular approach (Compendium)

---

### Combined Approach

**Recommended for:**
- International organizations
- Multi-national compliance
- Comprehensive security program

**Strategy:**
1. Implement ISO 27001 as foundation
2. Add NIST CSF for risk management framework
3. Use BSI IT-Grundschutz for detailed implementation
4. Map NIST 800-53 controls for US requirements
5. Document compliance with both standards

---

## Implementation Resources

### NIST Resources

- **NIST Cybersecurity Framework Tools:** https://www.nist.gov/cyberframework/framework
- **OSCAL (Open Security Controls Assessment Language):** https://pages.nist.gov/OSCAL/
- **National Vulnerability Database:** https://nvd.nist.gov/
- **NIST Risk Management Framework:** https://csrc.nist.gov/projects/risk-management

### BSI Resources

- **IT-Grundschutz Portal:** https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/it-grundschutz_node.html
- **BSI for Citizens:** https://www.bsi-fuer-buerger.de/
- **CERT-Bund:** https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Cyber-Sicherheitslage/Reaktion/CERT-Bund/cert-bund_node.html
- **BSI Publications:** https://www.bsi.bund.de/EN/Service-Navi/Publikationen/publikationen_node.html

---

## Template Framework Support Summary

| Standard | Framework Templates | Status | Language |
|---|---|---|---|
| NIST 800-53 | ✅ nist-800-53 | Complete | EN, DE |
| NIST CSF | ✅ nist-csf | Complete | EN, DE |
| BSI 200-1/2/3 | ✅ bsi-grundschutz | Complete | EN, DE |
| BSI 200-4 | ✅ bcm | Complete | EN, DE |
| ISO 27001 | ✅ isms | Complete | EN, DE |
| ISO 22301 | ✅ bcm | Complete | EN, DE |

---

## Document Maintenance

**Update Schedule:**
- Review quarterly for new NIST publications
- Review quarterly for new BSI standards
- Update framework mappings as needed
- Track standard version changes

**Change Log:**

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-18 | Initial IT Standards Reference Guide |

---

**End of Document**
