# Policy: Data Protection Interfaces

**Document-ID:** [FRAMEWORK]-0560
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Approved by:** {{ meta-handbook.approver }}
**Revision:** [TODO]
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Classification:** {{ meta-handbook.classification }}
**Last Update:** {{ meta-handbook.modifydate }}
**Template Version:** [TODO]

---

---

<!-- 
TEMPLATE AUTHOR NOTE:
This policy establishes the interface between information security and data protection.
It ensures that ISMS and data protection requirements are aligned and coordinated.
Customize based on your organization's data protection framework and GDPR requirements.

ISO 27001:2022 Annex A Reference: A.5.31, A.5.32, A.5.33, A.5.34
-->

**Document ID:** 0560  
**Document Type:** Policy (abstract)  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.5.31-A.5.34 (incl. Amendment 1:2024)  
**Owner:** {{ meta-organisation-roles.role_CISO }}  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** {{ meta-handbook.modifydate }}  
**Next Review:** {{ meta-handbook.next_review }}

## 1. Purpose

This policy defines the interfaces between information security and data protection at **{{ meta-organisation.name }}**. It ensures that ISMS and data protection requirements are aligned and coordinated.

## 2. Scope

This policy applies to:

- **Organizational Units:** All departments and locations of {{ meta-organisation.name }}
- **Data:** All personal data according to GDPR
- **Processes:** All processing activities of personal data
- **Interfaces:** ISMS ↔ Data Protection Management System
- **Locations:** [[ netbox.site.name ]] and all other operational sites

**Exceptions:** Exceptions are only permitted through the defined exception process (`0640_Policy_Exceptions_and_Risk_Waivers.md`).

## 3. Principles (Policy Statements)

### 3.1 Coordination of ISMS and Data Protection
ISMS and data protection management are coordinated. CISO and DPO work closely together and align measures.

### 3.2 Privacy by Design and by Default
Data protection is integrated into systems and processes from the beginning (Privacy by Design). Privacy-friendly default settings are standard (Privacy by Default).

### 3.3 Data Protection Impact Assessment (DPIA)
Data Protection Impact Assessments are conducted for high-risk processing. DPIA is coordinated with ISMS risk analysis.

### 3.4 Data Subject Rights
Processes for fulfilling data subject rights are established:
- Right of access (Art. 15 GDPR)
- Right to rectification (Art. 16 GDPR)
- Right to erasure (Art. 17 GDPR)
- Right to data portability (Art. 20 GDPR)
- Right to object (Art. 21 GDPR)

### 3.5 Record of Processing Activities
A record of processing activities (RoPA) is maintained and kept current. RoPA is aligned with ISMS asset inventory.

### 3.6 Data Processing
Data processors are engaged according to GDPR Art. 28. Data Processing Agreements (DPA) contain required security measures.

### 3.7 Data Breaches
Data breaches are handled according to GDPR Art. 33/34. Notification obligations to supervisory authorities and data subjects are met (72-hour deadline).

### 3.8 International Data Transfers
International data transfers only occur with appropriate safeguards (adequacy decision, standard contractual clauses, BCR).

## 4. Roles and Responsibilities

### RACI Matrix: Data Protection Interfaces

| Activity | CISO | DPO | IT Operations | Business Owner | Legal |
|----------|------|-----|---------------|----------------|-------|
| Policy Creation | R/A | R/A | C | C | C |
| DPIA Execution | C | R/A | C | R | C |
| Data Subject Rights | I | R/A | C | C | C |
| RoPA Maintenance | C | R/A | C | R | I |
| DPA Negotiation | C | R/A | I | C | R |
| Data Breach Notification | R/A | R/A | C | C | C |
| Privacy by Design | R | R/A | R | R | I |

**Legend:** R = Responsible (Execution), A = Accountable (Ownership), C = Consulted, I = Informed

### Key Roles

- **Policy Owner:** {{ meta-organisation-roles.role_CISO }} (CISO) and {{ meta-handbook.dpo_name }} (DPO)
- **Data Protection Officer:** {{ meta-handbook.dpo_name }}
- **Privacy Officer:** {{ meta-handbook.privacy_officer }}
- **Implementation Responsible:** IT Operations, Business Owner
- **Control/Audit Function:** ISMS, Internal Audit, Data Protection Authority

## 5. Derivatives (Guidelines/Standards/Processes)

Implementation details are defined in subordinate documents:

### Associated Guidelines
- **0570_Guideline_Data_Protection_Requirements_and_Data_Processing.md** - Detailed implementation guideline
- `0280_Policy_Data_Classification_and_Information_Handling.md` - Data Classification Policy
- `0400_Policy_Incident_Management.md` - Incident Management Policy (data breaches)
- `0460_Policy_Supplier_and_Cloud_Security.md` - Supplier Security Policy (DPA)

### Associated Standards/Baselines
- DPIA methodology
- Data subject rights processes
- DPA templates
- Data breach notification process

### Associated Processes
- Data Protection Impact Assessment (DPIA)
- Data subject rights process
- Data breach notification process
- Privacy by Design review

## 6. Compliance, Monitoring and Enforcement

### Metrics and KPIs
- Number of DPIAs conducted
- Average processing time for data subject rights (Target: < 30 days)
- Number of data breaches and notifications
- RoPA currency (Target: quarterly update)
- Number of DPAs with current security measures (Target: 100%)
- Privacy by Design review coverage

### Evidence and Proof
- DPIA documentation
- Record of processing activities (RoPA)
- Data subject rights requests and responses
- Data Processing Agreements (DPA)
- Data breach notifications
- Privacy by Design reviews

### Consequences of Violations
Violations of this policy are handled according to applicable HR and compliance processes:
- **GDPR Violations:** Incident response, notification to supervisory authority, potential fines
- **Unreported Data Breaches:** Compliance investigation, disciplinary action
- **Missing DPIAs:** Completion, processing suspension
- **Repeated Violations:** Employment consequences, fines

## 7. Exceptions

Exceptions to this policy are only permitted in justified exceptional cases:

- **Exception Process:** See `0640_Policy_Exceptions_and_Risk_Waivers.md`
- **Approval:** Exceptions must be approved by CISO and DPO
- **Documentation:** All exceptions are documented in the risk register
- **Time Limitation:** Exceptions are generally time-limited

## 8. References

### Internal Documents
- `0010_ISMS_Information_Security_Policy.md` - ISMS Policy
- `0570_Guideline_Data_Protection_Requirements_and_Data_Processing.md` - Detailed Guideline
- `0280_Policy_Data_Classification_and_Information_Handling.md` - Data Classification Policy
- `0080_ISMS_Risk_Register_Template.md` - Risk Register

### External Standards and Requirements
- **ISO/IEC 27001:2022 Annex A.5.31** - Legal, statutory, regulatory and contractual requirements
- **ISO/IEC 27001:2022 Annex A.5.32** - Intellectual property rights
- **ISO/IEC 27001:2022 Annex A.5.33** - Protection of records
- **ISO/IEC 27001:2022 Annex A.5.34** - Privacy and protection of PII
- **GDPR (EU 2016/679)** - General Data Protection Regulation
- **ISO/IEC 27701** - Privacy Information Management System
- **BDSG** - German Federal Data Protection Act

**Approved by:**  
{{ meta-handbook.management_ceo }}, Management  
Date: {{ meta-handbook.modifydate }}

**Next Review:** {{ meta-handbook.next_review }} (annually or as needed)

