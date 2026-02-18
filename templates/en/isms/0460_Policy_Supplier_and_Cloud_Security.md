# Policy: Supplier and Cloud Security

**Document-ID:** [FRAMEWORK]-0460
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
This policy establishes the principles for third-party and cloud security management.
It ensures that suppliers, vendors, and cloud providers meet security requirements
and are managed throughout their lifecycle. Customize based on your organization's
supply chain and cloud adoption.

ISO 27001:2022 Annex A Reference: A.5.19, A.5.20, A.5.21, A.5.22, A.5.23
-->

**Document ID:** 0460  
**Document Type:** Policy (abstract)  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.5.19-A.5.23 (incl. Amendment 1:2024)  
**Owner:** {{ meta.ciso.name }}  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** {{ meta-handbook.modifydate }}  
**Next Review:** {{ meta-handbook.next_review }}

## 1. Purpose

This policy defines the principles for supplier and cloud security management at **{{ meta-organisation.name }}**. It ensures that suppliers, service providers, and cloud providers meet security requirements and are securely managed throughout their entire lifecycle.

## 2. Scope

This policy applies to:

- **Organizational Units:** All departments and locations of {{ meta-organisation.name }}
- **Supplier Types:** IT service providers, cloud providers, SaaS vendors, outsourcing partners, subcontractors
- **Services:** IaaS, PaaS, SaaS, managed services, outsourcing
- **Lifecycle:** Selection, onboarding, operation, monitoring, offboarding
- **Locations:** {{ netbox.site.name }} and all other operational sites

**Exceptions:** Exceptions are only permitted through the defined exception process (`0640_Policy_Exceptions_and_Risk_Waivers.md`).

## 3. Principles (Policy Statements)

### 3.1 Third-Party Risk Assessment
All suppliers undergo a security risk assessment before contract signing. The assessment considers data access, criticality, and compliance requirements.

### 3.2 Contractual Security Requirements
Contracts with suppliers contain binding security requirements:
- Information security clauses
- Data protection requirements (GDPR)
- Audit rights and evidence obligations
- Incident notification obligations
- Subcontractor regulations

### 3.3 Cloud Security Assessment
Cloud providers are evaluated according to recognized standards (ISO 27001, SOC 2, CSA STAR). The shared responsibility model is documented and understood.

### 3.4 Data Classification and Cloud Usage
Storage and processing of data in the cloud is based on data classification:
- **Public:** All cloud services permitted
- **Internal:** Approved cloud services with appropriate controls
- **Confidential:** Only certified cloud services with encryption
- **Strictly Confidential:** Only on-premise or dedicated cloud with enhanced controls

### 3.5 Supplier Lifecycle Management
Suppliers are managed throughout their entire lifecycle:
- **Onboarding:** Security assessment, contract negotiation
- **Operation:** Continuous monitoring, regular reviews
- **Offboarding:** Secure data return/deletion, access revocation

### 3.6 Regular Supplier Reviews
Critical suppliers are reviewed annually. Reviews include security compliance, incident history, certifications, and performance.

### 3.7 Supply Chain Security
The security of the entire supply chain is considered. Suppliers must pass security requirements to their subcontractors.

### 3.8 Cloud Data Residency and Compliance
Data locations (data residency) are documented and comply with regulatory requirements (GDPR, Schrems II).

## 4. Roles and Responsibilities

### RACI Matrix: Supplier and Cloud Security

| Activity | CISO | Procurement | Legal | DPO | Business Owner | IT Operations |
|----------|------|-------------|-------|-----|----------------|---------------|
| Policy creation | R/A | C | C | C | I | C |
| Risk assessment | R/A | C | C | C | C | C |
| Contract negotiation | C | R | R/A | C | C | I |
| Security review | R/A | I | I | C | C | C |
| Supplier monitoring | A | C | I | I | C | R |
| Cloud security assessment | R/A | C | I | C | C | C |
| Offboarding | C | C | I | C | C | R/A |

**Legend:** R = Responsible (Execution), A = Accountable (Ownership), C = Consulted, I = Informed

### Key Roles

- **Policy Owner:** {{ meta.ciso.name }} (CISO)
- **Third-Party Risk Manager:** {{ meta.security.tprm_manager }}
- **Cloud Security Architect:** {{ meta.security.cloud_architect }}
- **Data Protection Officer:** {{ meta.dpo.name }}
- **Implementation Responsible:** Procurement, Legal, IT Operations
- **Control/Audit Function:** ISMS, Internal Audit

## 5. Derivations (Guidelines/Standards/Processes)

Implementation details are defined in subordinate documents:

### Related Guidelines
- **0470_Guideline_Third_Party_Risk_Assessment_and_Cloud_Controls.md** - Detailed implementation guideline
- `0280_Policy_Data_Classification_and_Information_Handling.md` - Data Classification Policy
- `0560_Policy_Data_Protection_Interfaces.md` - Data Protection Policy
- `0440_Policy_Business_Continuity_ICT_Readiness.md` - Business Continuity Policy

### Related Standards/Baselines
- Third-party risk assessment framework
- Cloud security assessment criteria
- Contractual security clauses (templates)
- Supplier security scorecard

### Related Processes
- Third-party risk management process
- Cloud service approval process
- Supplier review process
- Supplier offboarding process

## 6. Compliance, Monitoring and Enforcement

### Metrics and KPIs
- Number of suppliers with current security assessment (target: 100% of critical suppliers)
- Average supplier security score
- Number of supplier security incidents
- Cloud service approval rate
- Supplier review completion rate (target: 100% annually)
- Number of unapproved cloud services (shadow IT)

### Evidence and Proof
- Third-party risk assessments
- Supplier security scorecards
- Contracts with security clauses
- Cloud security assessments
- Supplier review reports
- Supplier security audit reports

### Consequences of Violations
Violations of this policy are handled according to applicable HR and compliance processes:
- **Use of unapproved cloud services:** Immediate deactivation, investigation
- **Missing risk assessments:** Completion, contract suspension
- **Supplier security incidents:** Incident response, contract review
- **Repeated violations:** Contract termination, employment consequences

## 7. Exceptions

Exceptions to this policy are only permitted in justified cases:

- **Exception Process:** See `0640_Policy_Exceptions_and_Risk_Waivers.md`
- **Approval:** Exceptions must be approved by CISO and Business Owner
- **Documentation:** All exceptions are documented in the risk register
- **Time Limitation:** Exceptions are generally time-limited
- **Compensating Controls:** Exceptions require alternative security measures

## 8. References

### Internal Documents
- `0010_ISMS_Information_Security_Policy.md` - ISMS Policy
- `0470_Guideline_Third_Party_Risk_Assessment_and_Cloud_Controls.md` - Detailed Guideline
- `0280_Policy_Data_Classification_and_Information_Handling.md` - Data Classification Policy
- `0080_ISMS_Risk_Register_Template.md` - Risk Register

### External Standards and Requirements
- **ISO/IEC 27001:2022 Annex A.5.19** - Information security in supplier relationships
- **ISO/IEC 27001:2022 Annex A.5.20** - Addressing information security within supplier agreements
- **ISO/IEC 27001:2022 Annex A.5.21** - Managing information security in the ICT supply chain
- **ISO/IEC 27001:2022 Annex A.5.22** - Monitoring, review and change management of supplier services
- **ISO/IEC 27001:2022 Annex A.5.23** - Information security for use of cloud services
- **ISO/IEC 27017** - Cloud Security Controls
- **ISO/IEC 27018** - Cloud Privacy
- **CSA STAR** - Cloud Security Alliance Security, Trust & Assurance Registry
- **GDPR (EU 2016/679)** - Art. 28 - Data processing

**Approved by:**  
{{ meta.management.ceo }}, Management  
Date: {{ meta-handbook.modifydate }}

**Next Review:** {{ meta-handbook.next_review }} (annually or as needed)

