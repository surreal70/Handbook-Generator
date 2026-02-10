# Statement of Applicability (SoA) – Template

<!-- 
TEMPLATE AUTHOR NOTE:
The Statement of Applicability (SoA) is a mandatory ISO 27001 document that
declares which Annex A controls are applicable to the ISMS and provides
justification for inclusions and exclusions. This document demonstrates that
the organization has considered all controls and made informed decisions.

ISO 27001:2022 Reference: Clause 6.1.3 d) - Statement of Applicability
-->

**Document ID:** 0100  
**Document Type:** ISMS Evidence/Template  
**Standard Reference:** ISO/IEC 27001:2022 Clause 6.1.3 d), Annex A  
**Owner:** {{ meta.ciso.name }}  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Confidential  
**Last Updated:** {{ meta.document.date }}  
**Next Review:** {{ meta.document.next_review }}

---

## 1. Purpose and Scope

### 1.1 Purpose

The Statement of Applicability (SoA) of **{{ meta.organization.name }}** documents:
- Which Annex A controls are applicable to the ISMS
- Justification for selection or exclusion of controls
- Implementation status of each control
- Linkage to policies, guidelines, and evidence

The SoA is a **mandatory document** according to ISO/IEC 27001:2022 and serves as:
- Evidence of systematic control selection
- Basis for audits and certifications
- Overview of implementation status
- Link between risk analysis and controls

### 1.2 Scope

This SoA applies to the entire ISMS scope (see `0020_ISMS_Scope.md`):
- All locations: {{ netbox.site.name }} and others
- All IT systems and infrastructure
- All business processes in scope
- All information assets

### 1.3 Annex A Controls (ISO 27001:2022)

**ISO/IEC 27001:2022 Annex A** contains 93 controls in 4 categories:
- **Organisational Controls (5.x):** 37 controls
- **People Controls (6.x):** 8 controls
- **Physical Controls (7.x):** 14 controls
- **Technological Controls (8.x):** 34 controls

**Amendment 1:2024:**
- Considers changes from Amendment 1:2024
- See `0710_Appendix_AnnexA_Mapping_Template.md` for complete list

## 2. Control Selection Criteria

### 2.1 Selection Process

Controls are selected based on the following criteria:

**1. Risk Analysis:**
- Controls to treat identified risks
- See `0080_ISMS_Risk_Register_Template.md`

**2. Compliance Requirements:**
- Legal requirements (GDPR, NIS2, etc.)
- Contractual obligations
- Industry standards

**3. Best Practices:**
- Industry-standard security measures
- Recommendations from security experts

**4. Organizational Requirements:**
- Business requirements
- Stakeholder expectations

### 2.2 Exclusion Criteria

Controls may be excluded when:
- Not relevant to the ISMS scope
- Risk is accepted and control not required
- Alternative controls provide equivalent protection
- Technically or organizationally not feasible (with justification)

**Important:** Exclusions must be justified and must not impair the organization's ability to meet security requirements.

## 3. Statement of Applicability (SoA) - Overview

### 3.1 Implementation Status

| Status | Number of Controls | Percentage |
|--------|-------------------|------------|
| Implemented | [TODO] | [TODO]% |
| In Progress | [TODO] | [TODO]% |
| Planned | [TODO] | [TODO]% |
| Not Applicable | [TODO] | [TODO]% |
| **Total** | **93** | **100%** |

**Target:** At least 80% of applicable controls implemented by [TODO: Date]

### 3.2 Implementation by Category

| Category | Applicable | Implemented | In Progress | Planned | Not Applicable |
|----------|-----------|-------------|-------------|---------|----------------|
| Organisational (5.x) | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| People (6.x) | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| Physical (7.x) | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| Technological (8.x) | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## 4. SoA Table: Organisational Controls (5.x)

### 4.1 Policies for Information Security (5.1-5.10)

| Control ID | Control Name | Applicable | Justification (if No) | Implementation Status | Implementation/Description | Policy/Guideline | Evidence | Owner | Remarks |
|------------|--------------|------------|----------------------|----------------------|---------------------------|------------------|----------|-------|---------|
| **A.5.1** | Policies for information security | Yes | - | Implemented | ISMS policy and topic-specific policies | `0010_ISMS_Information_Security_Policy.md` | Policy documents | {{ meta.ciso.name }} | Annual review |
| **A.5.2** | Information security roles and responsibilities | Yes | - | Implemented | ISMS governance structure defined | `0040_ISMS_Governance_Roles_and_Responsibilities.md` | RACI matrices | {{ meta.ciso.name }} | - |
| **A.5.3** | Segregation of duties | Yes | - | In Progress | Role separation in critical processes | `0220_Policy_Access_Control_and_Identity_Management.md` | IAM configuration | {{ meta.cio.name }} | 70% implemented |
| **A.5.4** | Management responsibilities | Yes | - | Implemented | Management commitment documented | `0010_ISMS_Information_Security_Policy.md` | Management review | {{ meta.management.ceo }} | - |
| **A.5.5** | Contact with authorities | Yes | - | Implemented | Contacts with authorities documented | `0050_Contacts_and_Escalation.md` (BCM) | Contact list | {{ meta.ciso.name }} | - |
| **A.5.6** | Contact with special interest groups | Yes | - | Implemented | Membership in CERT, industry associations | [TODO: Document] | Membership evidence | {{ meta.ciso.name }} | - |
| **A.5.7** | Threat intelligence | Yes | - | In Progress | Threat intelligence feeds subscribed | `0060_ISMS_Risk_Management_Methodology.md` | TI feed configuration | Security Team | MITRE ATT&CK, CERT |
| **A.5.8** | Information security in project management | Yes | - | Planned | Security in project lifecycle | `0680_Policy_Security_in_Projects.md` | Project checklists | PMO | Rollout Q2 2026 |
| **A.5.9** | Inventory of information and other associated assets | Yes | - | In Progress | Asset inventory maintained | `0720_Appendix_Asset_and_System_Inventory_Template.md` | CMDB, NetBox | IT Operations | 80% captured |
| **A.5.10** | Acceptable use of information and other associated assets | Yes | - | Implemented | Acceptable use policy | `0200_Policy_Acceptable_Use_of_IT.md` | Signed policies | HR | - |

<!-- 
Continue with remaining Organisational Controls (5.11-5.37)
Add your organization's specific implementation details, evidence, and status.
-->

[TODO: Create complete table for all 37 Organisational Controls]

## 5. SoA Table: People Controls (6.x)

| Control ID | Control Name | Applicable | Justification (if No) | Implementation Status | Implementation/Description | Policy/Guideline | Evidence | Owner | Remarks |
|------------|--------------|------------|----------------------|----------------------|---------------------------|------------------|----------|-------|---------|
| **A.6.1** | Screening | Yes | - | Implemented | Background checks for critical roles | `0520_Policy_HR_Security.md` | HR process | HR | - |
| **A.6.2** | Terms and conditions of employment | Yes | - | Implemented | Security clauses in employment contracts | `0530_Guideline_HR_Onboarding_Role_Change_Offboarding.md` | Employment contracts | HR | - |
| **A.6.3** | Information security awareness, education and training | Yes | - | In Progress | Security awareness program | `0120_ISMS_Training_Awareness_and_Competence.md` | Training records | {{ meta.ciso.name }} | Quarterly training |
| **A.6.4** | Disciplinary process | Yes | - | Implemented | Disciplinary procedures for violations | `0520_Policy_HR_Security.md` | HR process | HR | - |
| **A.6.5** | Responsibilities after termination or change of employment | Yes | - | Implemented | Offboarding process | `0530_Guideline_HR_Onboarding_Role_Change_Offboarding.md` | Offboarding checklist | HR | - |
| **A.6.6** | Confidentiality or non-disclosure agreements | Yes | - | Implemented | NDAs for employees and third parties | `0520_Policy_HR_Security.md` | Signed NDAs | HR | - |
| **A.6.7** | Remote working | Yes | - | Implemented | Remote work policy | `0500_Policy_Mobile_Device_and_Remote_Work.md` | Remote work guidelines | {{ meta.cio.name }} | - |
| **A.6.8** | Information security event reporting | Yes | - | Implemented | Incident reporting process | `0400_Policy_Incident_Management.md` | Incident reports | {{ meta.ciso.name }} | - |

## 6. SoA Table: Physical Controls (7.x)

| Control ID | Control Name | Applicable | Justification (if No) | Implementation Status | Implementation/Description | Policy/Guideline | Evidence | Owner | Remarks |
|------------|--------------|------------|----------------------|----------------------|---------------------------|------------------|----------|-------|---------|
| **A.7.1** | Physical security perimeters | Yes | - | Implemented | Access controls at {{ netbox.site.name }} location | `0480_Policy_Physical_Security.md` | Access logs | Facility Mgmt | - |
| **A.7.2** | Physical entry | Yes | - | Implemented | Access cards, visitor management | `0490_Guideline_Access_Visitors_and_Equipment_Protection.md` | Visitor lists | Facility Mgmt | - |
| **A.7.3** | Securing offices, rooms and facilities | Yes | - | Implemented | Server room secured, alarm systems | `0480_Policy_Physical_Security.md` | Security concept | Facility Mgmt | - |
| **A.7.4** | Physical security monitoring | Yes | - | Implemented | Video surveillance, alarm systems | `0480_Policy_Physical_Security.md` | Monitoring logs | Facility Mgmt | GDPR-compliant |
| **A.7.5** | Protecting against physical and environmental threats | Yes | - | Implemented | Fire protection, climate control, UPS | `0480_Policy_Physical_Security.md` | Maintenance logs | Facility Mgmt | - |
| **A.7.6** | Working in secure areas | Yes | - | Implemented | Clean desk policy, secure areas | `0480_Policy_Physical_Security.md` | Audit reports | Facility Mgmt | - |
| **A.7.7** | Clear desk and clear screen | Yes | - | In Progress | Clear desk policy communicated | `0480_Policy_Physical_Security.md` | Awareness campaign | {{ meta.ciso.name }} | Rollout ongoing |
| **A.7.8** | Equipment siting and protection | Yes | - | Implemented | Equipment protection, theft prevention | `0490_Guideline_Access_Visitors_and_Equipment_Protection.md` | Asset register | IT Operations | - |
| **A.7.9** | Security of assets off-premises | Yes | - | Implemented | Laptop encryption, mobile device policy | `0500_Policy_Mobile_Device_and_Remote_Work.md` | MDM configuration | IT Operations | - |
| **A.7.10** | Storage media | Yes | - | Implemented | Secure handling of storage media | `0280_Policy_Data_Classification_and_Information_Handling.md` | Handling procedures | IT Operations | - |
| **A.7.11** | Supporting utilities | Yes | - | Implemented | UPS, emergency power, climate control | `0480_Policy_Physical_Security.md` | Maintenance contracts | Facility Mgmt | - |
| **A.7.12** | Cabling security | Yes | - | Implemented | Structured cabling, protection | `0480_Policy_Physical_Security.md` | Cabling plan | IT Operations | - |
| **A.7.13** | Equipment maintenance | Yes | - | Implemented | Maintenance contracts, maintenance logs | `0480_Policy_Physical_Security.md` | Maintenance evidence | IT Operations | - |
| **A.7.14** | Secure disposal or re-use of equipment | Yes | - | Implemented | Secure disposal, data wiping | `0580_Policy_Retention_and_Deletion.md` | Disposal evidence | IT Operations | GDPR-compliant |

## 7. SoA Table: Technological Controls (8.x)

| Control ID | Control Name | Applicable | Justification (if No) | Implementation Status | Implementation/Description | Policy/Guideline | Evidence | Owner | Remarks |
|------------|--------------|------------|----------------------|----------------------|---------------------------|------------------|----------|-------|---------|
| **A.8.1** | User endpoint devices | Yes | - | Implemented | Endpoint protection (EDR/AV) | `0620_Policy_Endpoint_Security.md` | EDR configuration | IT Operations | - |
| **A.8.2** | Privileged access rights | Yes | - | In Progress | PAM solution being implemented | `0220_Policy_Access_Control_and_Identity_Management.md` | PAM system | IT Operations | Rollout Q2 2026 |
| **A.8.3** | Information access restriction | Yes | - | Implemented | Access controls, RBAC | `0220_Policy_Access_Control_and_Identity_Management.md` | IAM configuration | IT Operations | - |
| **A.8.4** | Access to source code | Yes | - | Implemented | Git access controls, code review | `0360_Policy_Secure_Development.md` | Git permissions | Dev Lead | - |
| **A.8.5** | Secure authentication | Yes | - | In Progress | MFA rollout | `0240_Policy_Authentication_and_Passwords.md` | MFA configuration | IT Operations | 80% complete |
| **A.8.6** | Capacity management | Yes | - | In Progress | Monitoring, capacity planning | [TODO: Policy] | Monitoring dashboards | IT Operations | - |
| **A.8.7** | Protection against malware | Yes | - | Implemented | Antivirus, EDR, email filtering | `0620_Policy_Endpoint_Security.md` | AV/EDR reports | IT Operations | - |
| **A.8.8** | Management of technical vulnerabilities | Yes | - | In Progress | Vulnerability management process | `0340_Policy_Vulnerability_and_Patch_Management.md` | Scan reports | IT Operations | - |

<!-- 
Continue with remaining Technological Controls (8.9-8.34)
Add your organization's specific implementation details.
-->

[TODO: Create complete table for all 34 Technological Controls]

## 8. Non-Applicable Controls

### 8.1 Excluded Controls with Justification

| Control ID | Control Name | Justification for Exclusion | Alternative Measures | Approved By |
|------------|--------------|----------------------------|---------------------|-------------|
| [TODO] | [TODO] | [TODO: Not in scope, risk accepted, etc.] | [TODO: If available] | {{ meta.ciso.name }} |

**Important:** Exclusions must be documented and approved. They must not impair the ability to meet security requirements.

## 9. Linkages and References

### 9.1 Linkage to ISMS Documents

**Risk Analysis:**
- Controls are selected based on risk analysis
- See `0080_ISMS_Risk_Register_Template.md`

**Risk Treatment Plan:**
- Implementation of controls is tracked in RTP
- See `0090_ISMS_Risk_Treatment_Plan_RTP_Template.md`

**Policies and Guidelines:**
- Each control is linked to policy/guideline
- See ISMS document structure (0200-0690)

**Evidence:**
- Evidence for control implementation
- See `0700_Appendix_Evidence_Register.md`

### 9.2 Complete Annex A Mapping

For a complete overview of all 93 Annex A controls see:
- `0710_Appendix_AnnexA_Mapping_Template.md`

## 10. Review and Update

### 10.1 Regular Review

**Annually:**
- Complete SoA review
- Review of applicability of all controls
- Update of implementation status

**Quarterly:**
- Review of implementation status
- Tracking of measures from RTP

### 10.2 Triggers for Unscheduled Review

**Changes to ISMS Scope:**
- New locations, systems, processes
- See `0020_ISMS_Scope.md`

**New Risks:**
- Significant changes in risk register
- See `0080_ISMS_Risk_Register_Template.md`

**New Compliance Requirements:**
- New laws, regulations, contracts

**Audit Findings:**
- Internal or external audit findings

## 11. References

### 11.1 Internal Documents

- `0020_ISMS_Scope.md` - ISMS Scope
- `0060_ISMS_Risk_Management_Methodology.md` - Risk Management
- `0080_ISMS_Risk_Register_Template.md` - Risk Register
- `0090_ISMS_Risk_Treatment_Plan_RTP_Template.md` - Risk Treatment Plan
- `0710_Appendix_AnnexA_Mapping_Template.md` - Complete Annex A Mapping
- All Policies (0200-0680) and Guidelines (0210-0690)

### 11.2 External Standards

- **ISO/IEC 27001:2022** - Clause 6.1.3 d): Statement of Applicability
- **ISO/IEC 27001:2022** - Annex A: Information security controls
- **ISO/IEC 27001:2022/Amd 1:2024** - Amendment 1 (Annex A updates)
- **ISO/IEC 27002:2022** - Information security controls (detailed guidance)

---

## Change History

| Version | Date | Author | Description | Approved By |
|---------|------|--------|-------------|-------------|
| 1.0 | {{ meta.document.date }} | {{ meta.ciso.name }} | Initial version | {{ meta.management.ceo }} |

---

**Approved by:**  
{{ meta.ciso.name }}, CISO  
{{ meta.management.ceo }}, Management  
Date: {{ meta.document.approval_date }}

**Next Review:** {{ meta.document.next_review }} (Annually)

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial Creation |
