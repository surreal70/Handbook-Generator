# Policy: Data Classification and Information Handling

**Document-ID:** [FRAMEWORK]-0280
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
This policy establishes the principles for data classification and information handling.
It ensures that information is classified according to its sensitivity and handled
appropriately throughout its lifecycle. Customize based on your organization's
data classification scheme and regulatory requirements (GDPR, industry-specific).

ISO 27001:2022 Annex A Reference: A.5.12, A.5.13, A.5.14
-->

**Document ID:** 0280  
**Document Type:** Policy (abstract)  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.5.12-A.5.14 (incl. Amendment 1:2024)  
**Owner:** {{ meta.ciso.name }}  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** {{ meta-handbook.modifydate }}  
**Next Review:** {{ meta-handbook.next_review }}

## 1. Purpose

This policy defines the principles for data classification and information handling at **{{ meta-organisation.name }}**. It ensures that information is classified according to its sensitivity and protection requirements, labeled appropriately, and protected throughout its entire lifecycle.

## 2. Scope

This policy applies to:

- **Organizational Units:** All departments and locations of {{ meta-organisation.name }}
- **Information:** All information in any form (digital, physical, verbal)
- **Systems:** All IT systems, applications, databases, storage media
- **Persons:** All employees, contractors, suppliers, and third parties with access to information
- **Lifecycle:** Creation, storage, processing, transmission, archiving, destruction
- **Locations:** {{ netbox.site.name }} and all other operational sites

**Exceptions:** Exceptions are only permitted through the defined exception process (`0640_Policy_Ausnahmen_und_Risk_Waivers.md`).

## 3. Principles (Policy Statements)

### 3.1 Mandatory Classification
All organizational information must be classified. Classification is performed by the information owner based on confidentiality, integrity, and availability.

### 3.2 Classification Levels
The organization uses the following classification levels:
- **Public:** Information that is or may be publicly accessible
- **Internal:** Information for internal use, not intended for the public
- **Confidential:** Sensitive information whose disclosure could harm the organization
- **Highly Confidential:** Highly sensitive information with the highest protection requirements

### 3.3 Labeling and Marking
Classified information is labeled accordingly:
- Digital documents: Metadata, headers/footers, watermarks
- Physical documents: Stamps, stickers, cover sheets
- Emails: Subject prefix, banner
- Storage media: Labels

### 3.4 Handling Requirements
Specific handling requirements apply to each classification level:
- Access control and permissions
- Encryption (at rest, in transit)
- Storage and archiving
- Transmission and sharing
- Destruction and deletion

### 3.5 Information Owner Responsibility
Each piece of information has a defined information owner who is responsible for:
- Classifying the information
- Defining access rights
- Regular review of classification
- Approving access and sharing requests

### 3.6 Sharing and Distribution
Sharing of classified information follows the need-to-know principle:
- Internal sharing: After approval by information owner
- External sharing: After approval and with appropriate protective measures (NDA, encryption)
- Cloud storage: Only in approved cloud services with adequate security controls

### 3.7 Secure Destruction
Information is securely destroyed at the end of its lifecycle:
- Digital data: Secure deletion (overwriting, degaussing)
- Physical documents: Shredding, burning
- Storage media: Physical destruction for highly sensitive data

### 3.8 Data Protection Compliance
Classification and handling of personal data complies with GDPR and other data protection regulations.

## 4. Roles and Responsibilities

### RACI Matrix: Data Classification and Information Handling

| Activity | CISO | Information Owner | Employee | IT Operations | Data Protection Officer |
|----------|------|-------------------|----------|---------------|-------------------------|
| Policy Creation | R/A | C | I | C | C |
| Classification | C | R/A | I | I | C |
| Labeling | I | A | R | C | I |
| Access Approval | C | R/A | I | I | C |
| Handling Compliance | A | R | R | C | C |
| Sharing Approval | C | R/A | I | I | C |
| Secure Destruction | C | A | I | R | C |
| Monitoring and Audits | R/A | C | I | C | C |

**Legend:** R = Responsible (Execution), A = Accountable (Accountable), C = Consulted (Consulted), I = Informed (Informed)

### Key Roles

- **Policy Owner:** {{ meta.ciso.name }} (CISO)
- **Information Owners:** Department heads, system owners
- **Data Protection Officer:** {{ meta.dpo.name }}
- **Implementation Responsible:** All employees, IT operations
- **Control/Audit Function:** ISMS, internal audit, DPO

## 5. Derivations (Guidelines/Standards/Processes)

Implementation details are defined in subordinate documents:

### Related Guidelines
- **0290_Richtlinie_Datenklassifizierung_Labeling_und_Handling.md** - Detailed implementation guideline
- `0260_Policy_Kryptografie_und_Schluesselmanagement.md` - Cryptography policy
- `0560_Policy_Datenschutz_Schnittstellen.md` - Data protection policy
- `0580_Policy_Aufbewahrung_und_Loeschung.md` - Retention and deletion policy

### Related Standards/Baselines
- Classification scheme and handling matrix
- Labeling standards (digital and physical)
- Encryption requirements per classification level
- Destruction standards

### Related Processes
- Classification process
- Information owner assignment
- Sharing and distribution approval process
- Secure destruction process

## 6. Compliance, Monitoring, and Enforcement

### Metrics and KPIs
- Percentage of classified information (target: 100%)
- Percentage of correctly labeled documents
- Number of handling requirement violations
- Number of unauthorized disclosures
- Average time to classify new information
- Compliance rate with destruction requirements

### Evidence and Proof
- Classification register
- Information owner assignments
- Sharing approvals
- Destruction certificates
- DLP (Data Loss Prevention) logs
- Audit reports on classification and handling

### Consequences for Violations
Violations of this policy are handled according to applicable HR and compliance processes:
- **Missing classification:** Retraining, correction
- **Incorrect labeling:** Correction, retraining
- **Unauthorized disclosure:** Warning up to termination, possible legal action
- **Improper destruction:** Investigation, retraining
- **Repeated violations:** Employment law consequences

## 7. Exceptions

Exceptions to this policy are only permitted in justified exceptional cases:

- **Exception Process:** See `0640_Policy_Ausnahmen_und_Risk_Waivers.md`
- **Approval:** Exceptions must be approved by CISO and information owner
- **Documentation:** All exceptions are documented in the risk register
- **Time Limit:** Exceptions are generally time-limited and regularly reviewed
- **Compensating Controls:** Exceptions require alternative security measures

## 8. References

### Internal Documents
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS policy
- `0290_Richtlinie_Datenklassifizierung_Labeling_und_Handling.md` - Detailed guideline
- `0300_Policy_Asset_Management.md` - Asset management policy
- `0080_ISMS_Risikoregister_Template.md` - Risk register

### External Standards and Requirements
- **ISO/IEC 27001:2022 Annex A.5.12** - Classification of information
- **ISO/IEC 27001:2022 Annex A.5.13** - Labelling of information
- **ISO/IEC 27001:2022 Annex A.5.14** - Information transfer
- **ISO/IEC 27002:2022** - Information security controls
- **GDPR (EU 2016/679)** - General Data Protection Regulation
- **BSI IT-Grundschutz** - Module CON.6 Deletion and Destruction

**Approved by:**  
{{ meta.management.ceo }}, Management  
Date: {{ meta-handbook.modifydate }}

**Next Review:** {{ meta-handbook.next_review }} (annually or as needed)

