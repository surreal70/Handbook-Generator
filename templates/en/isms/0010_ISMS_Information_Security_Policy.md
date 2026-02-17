# ISMS Policy / Information Security Policy

**Document-ID:** [FRAMEWORK]-0010
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Approved by:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Classification:** {{ meta-handbook.classification }}
**Last Update:** {{ meta-handbook.modifydate }}

---

---

<!-- 
TEMPLATE AUTHOR NOTE:
This is the top-level information security policy document. It establishes the 
organization's commitment to information security and provides the foundation 
for the entire ISMS. Customize this template based on your organization's 
specific security objectives and risk appetite.

ISO 27001:2022 Reference: Clause 5.2 - Policy
-->

**Document ID:** 0010  
**Document Type:** Policy (abstract)  
**Standard Reference:** ISO/IEC 27001:2022 Clause 5.2 (incl. Amendment 1:2024)  
**Owner:** {{ meta.ciso.name }}  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** {{ meta-handbook.modifydate }}  
**Next Review:** {{ meta-handbook.next_review }}

## 1. Purpose

This Information Security Policy defines the strategic principles and commitments of **{{ meta-organisation.name }}** for protecting information assets. It forms the foundation for the Information Security Management System (ISMS) according to ISO/IEC 27001:2022 and ensures that information security is understood and implemented as an integral part of all business processes.

<!-- 
Customize the purpose statement to reflect your organization's specific 
security mission and strategic objectives.
-->

## 2. Scope

This policy applies to:

- **Organizational Units:** All departments and locations of {{ meta-organisation.name }}
- **Systems and Information:** All IT systems, applications, data, and information processing processes
- **Personnel:** All employees, contractors, suppliers, and third parties with access to information assets
- **Locations:** {{ netbox.site.name }} and all other operational sites

**Exceptions:** Exceptions to this policy are only permitted through the defined exception process (see `0640_Policy_Exceptions_and_Risk_Waivers.md`).

<!-- ISO 27001:2022 Reference: Clause 4.3 - Determining the scope of the ISMS -->

## 3. Principles (Policy Statements)

{{ meta-organisation.name }} commits to the following information security principles:

### 3.1 Confidentiality
Information is only made accessible to authorized persons, systems, and processes. Access follows the need-to-know principle and is protected by appropriate access controls.

### 3.2 Integrity
The accuracy, completeness, and timeliness of information is ensured through appropriate controls. Unauthorized or unintended modifications are prevented and detected.

### 3.3 Availability
Information and IT systems are available to authorized users when needed. Business-critical systems are protected through appropriate redundancy and recovery measures.

### 3.4 Compliance and Legal Requirements
The organization complies with all applicable legal, regulatory, and contractual information security requirements, including data protection (GDPR), industry standards, and customer requirements.

### 3.5 Risk-Based Approach
Information security measures are prioritized and implemented based on systematic risk analysis. Risks are identified, assessed, and treated according to defined criteria.

### 3.6 Continuous Improvement
The ISMS is continuously monitored, measured, and improved. Security incidents, audits, and reviews serve as the basis for improvement measures.

### 3.7 Awareness and Training
All employees are regularly trained on information security risks and their responsibilities. Security awareness is part of the corporate culture.

### 3.8 Supplier and Third-Party Management
Suppliers and third parties with access to information assets are evaluated according to security criteria and contractually obligated to comply with security requirements.

<!-- 
Add or modify policy statements based on your organization's specific 
security requirements and risk profile.
-->

## 4. Roles and Responsibilities

### RACI Matrix: ISMS Policy

| Activity | CISO | CIO | Management | IT Operations | Business Units |
|----------|------|-----|------------|---------------|----------------|
| Policy Creation | R/A | C | I | C | C |
| Policy Approval | C | C | A | I | I |
| Policy Communication | R | C | I | I | I |
| Policy Implementation | A | R | I | R | R |
| Policy Monitoring | R/A | C | I | C | C |
| Policy Review | R/A | C | C | I | I |

**Legend:** R = Responsible (Execution), A = Accountable (Ownership), C = Consulted, I = Informed

### Key Roles

- **CISO (Chief Information Security Officer):** {{ meta.ciso.name }} ({{ meta.ciso.email }})
  - Responsible for developing, implementing, and monitoring the ISMS
  - Reports to: {{ meta.cio.name }}

- **CIO (Chief Information Officer):** {{ meta.cio.name }} ({{ meta.cio.email }})
  - Responsible for IT strategy and IT operations
  - Supports ISMS implementation

- **Management:** {{ meta.management.ceo }}
  - Approves ISMS policy and provides resources
  - Bears overall responsibility for information security

<!-- ISO 27001:2022 Reference: Clause 5.3 - Organizational roles, responsibilities and authorities -->

## 5. Derivations (Policies/Standards/Processes)

This abstract policy is detailed through the following documents:

### Basis ISMS Documents
- `0020_ISMS_Scope.md` - ISMS Scope Definition
- `0030_ISMS_Context_and_Interested_Parties.md` - Context of Organization
- `0040_ISMS_Governance_Roles_and_Responsibilities.md` - ISMS Governance
- `0060_ISMS_Risk_Management_Methodology.md` - Risk Management Methodology

### Topic-Specific Policies (Abstract)
- `0220_Policy_Access_Control_and_Identity_Management.md`
- `0240_Policy_Authentication_and_Passwords.md`
- `0260_Policy_Cryptography_and_Key_Management.md`
- `0280_Policy_Data_Classification_and_Information_Handling.md`
- [Additional policies see ISMS document structure]

### Detailed Guidelines
- See corresponding guideline documents (0210-0690, odd numbers)

<!-- 
Link to your organization's specific policy and guideline documents.
The three-tier structure (Policy → Abstract Policy → Detailed Guideline) 
ensures clear separation of strategic and operational documentation.
-->

## 6. Compliance, Monitoring, and Enforcement

### Metrics and KPIs
- Number of security incidents per quarter
- Average time to remediate critical vulnerabilities
- Training participation rate (Target: 100% annually)
- Audit findings and remediation rate
- Compliance rate with security policies

### Evidence and Documentation
- ISMS documentation and records
- Audit reports (internal and external)
- Risk register and risk treatment plans
- Training records and awareness campaigns
- Incident reports and lessons learned

### Consequences of Violations
Violations of this policy are handled according to applicable HR and compliance processes and may result in disciplinary action, including:
- Warning and retraining
- Revocation of access rights
- Employment consequences
- Legal action for intentional or grossly negligent violations

<!-- ISO 27001:2022 Reference: Clause 9 - Performance evaluation -->

## 7. Exceptions

Exceptions to this policy are only permitted in justified exceptional cases and must be requested through the defined exception process:

- **Exception Process:** See `0640_Policy_Exceptions_and_Risk_Waivers.md`
- **Approval:** Exceptions must be approved by the CISO and, if applicable, management
- **Documentation:** All exceptions are documented in the risk register and regularly reviewed
- **Time Limitation:** Exceptions are generally time-limited and must be renewed regularly

## 8. References

### Internal Documents
- ISMS Document Structure (see README.md)
- Risk Register (`0080_ISMS_Risk_Register_Template.md`)
- Statement of Applicability (`0100_ISMS_Statement_of_Applicability_SoA_Template.md`)
- Internal Audit Program (`0130_ISMS_Internal_Audit_Program.md`)

### External Standards and Regulations
- **ISO/IEC 27001:2022** - Information security management systems - Requirements
- **ISO/IEC 27001:2022/Amd 1:2024** - Amendment 1 (Annex A updates)
- **ISO/IEC 27002:2022** - Information security controls
- **GDPR (EU 2016/679)** - General Data Protection Regulation
- **BSI IT-Grundschutz** - German Federal Office for Information Security

**Approved by:**  
{{ meta.management.ceo }}, Management  
Date: {{ meta-handbook.modifydate }}

**Next Review:** {{ meta-handbook.next_review }} (annually or as needed)

