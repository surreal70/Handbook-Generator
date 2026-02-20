# Policy: Change and Release Management

**Document-ID:** ISMS-0360
**Organisation:** AdminSend GmbH
**Owner:** [TODO]
**Approved by:** [TODO]
**Revision:** [TODO]
**Author:** Handbook-Generator
**Status:** Draft
**Classification:** Internal
**Last Update:** [TODO]
**Template Version:** [TODO]

---

---



**Document ID:** 0360  
**Document Type:** Policy (abstract)  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.8.32 (incl. Amendment 1:2024)  
**Owner:** [TODO]  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** [TODO]  
**Next Review:** [TODO]

## 1. Purpose

This policy defines the principles for change and release management at **AdminSend GmbH**. It ensures that changes to IT systems are controlled, tested, and documented to minimize operational disruptions and security risks.

## 2. Scope

This policy applies to:

- **Organizational Units:** All departments and locations of AdminSend GmbH
- **Systems:** All IT systems, applications, infrastructure, networks, cloud services
- **Change Types:** Standard changes, normal changes, emergency changes
- **Environments:** Production, test, development
- **Locations:** [[ netbox.site.name ]] and all other operational sites

**Exceptions:** Exceptions are only permitted through the defined exception process (`0640_Policy_Exceptions_and_Risk_Waivers.md`).

## 3. Principles (Policy Statements)

### 3.1 Controlled Changes
All changes to production IT systems must be approved, documented, and tracked through the change management process.

### 3.2 Change Categorization
Changes are categorized by risk and impact:
- **Standard Changes:** Pre-approved, low-risk, recurring changes
- **Normal Changes:** Regular changes with CAB approval
- **Emergency Changes:** Urgent changes to resolve critical issues

### 3.3 Change Advisory Board (CAB)
A Change Advisory Board evaluates and approves normal and emergency changes. The CAB consists of representatives from IT, security, business, and change management.

### 3.4 Risk and Impact Analysis
A risk and impact analysis is performed before each change. Security risks are assessed and mitigation measures defined.

### 3.5 Testing and Validation
Changes are validated in test environments before being rolled out to production. Critical changes require comprehensive testing.

### 3.6 Rollback Planning
A rollback plan exists for every change to quickly return to the previous state in case of problems.

### 3.7 Documentation and Traceability
All changes are documented (description, justification, approval, execution, result). Changes are traceable and auditable.

### 3.8 Security Review
Changes with security relevance require a security review by the security team before approval.

## 4. Roles and Responsibilities

### RACI Matrix: Change and Release Management

| Activity | Change Manager | CAB | CISO | Change Requester | IT Operations |
|----------|----------------|-----|------|------------------|---------------|
| Policy creation | C | C | R/A | I | C |
| Change request | I | I | I | R | I |
| Risk analysis | R | C | C | C | C |
| CAB approval | R | A | C | I | I |
| Security review | C | C | R/A | I | I |
| Change implementation | C | I | I | I | R/A |
| Rollback | R | I | C | I | R/A |
| Post-implementation review | R/A | C | C | C | C |

**Legend:** R = Responsible (Execution), A = Accountable (Ownership), C = Consulted, I = Informed

### Key Roles

- **Policy Owner:** [TODO] (CISO)
- **Change Manager:** {{ meta-handbook.it_change_manager }}
- **CAB Chair:** {{ meta-handbook.it_cab_chair }}
- **Implementation Responsible:** IT Operations, Development
- **Control/Audit Function:** ISMS, Internal Audit

## 5. Derivations (Guidelines/Standards/Processes)

Implementation details are defined in subordinate documents:

### Related Guidelines
- **0370_Guideline_Change_Management_with_Security_Approvals.md** - Detailed implementation guideline
- `0340_Policy_Vulnerability_and_Patch_Management.md` - Patch Management Policy
- `0380_Policy_Secure_Development.md` - Secure Development Policy
- `0400_Policy_Incident_Management.md` - Incident Management Policy

### Related Standards/Baselines
- Change categorization and approval processes
- CAB composition and decision criteria
- Testing and validation requirements
- Rollback procedures

### Related Processes
- Change management process
- Emergency change process
- Release management process
- Post-implementation review

## 6. Compliance, Monitoring and Enforcement

### Metrics and KPIs
- Number of changes per category (standard, normal, emergency)
- Change success rate (target: >95%)
- Number of failed changes and rollbacks
- Average change lead time
- Number of unauthorized changes (target: 0)
- Security review coverage for security-relevant changes (target: 100%)

### Evidence and Proof
- Change tickets and approvals
- CAB meeting minutes
- Security review documentation
- Test results
- Rollback documentation
- Post-implementation review reports

### Consequences of Violations
Violations of this policy are handled according to applicable HR and compliance processes:
- **Unauthorized change:** Rollback, investigation, retraining
- **Missing documentation:** Completion, warning
- **Skipped security review:** Investigation, disciplinary action
- **Repeated violations:** Employment consequences

## 7. Exceptions

Exceptions to this policy are only permitted in justified cases:

- **Exception Process:** See `0640_Policy_Exceptions_and_Risk_Waivers.md`
- **Approval:** Exceptions must be approved by Change Manager and CISO
- **Documentation:** All exceptions are documented and discussed in post-implementation review
- **Time Limitation:** Exceptions are generally time-limited

## 8. References

### Internal Documents
- `0010_ISMS_Information_Security_Policy.md` - ISMS Policy
- `0370_Guideline_Change_Management_with_Security_Approvals.md` - Detailed Guideline
- `0340_Policy_Vulnerability_and_Patch_Management.md` - Patch Management Policy
- `0080_ISMS_Risk_Register_Template.md` - Risk Register

### External Standards and Requirements
- **ISO/IEC 27001:2022 Annex A.8.32** - Change management
- **ISO/IEC 27002:2022** - Information security controls
- **ITIL 4** - Change Enablement
- **ISO/IEC 20000** - IT Service Management

**Approved by:**  
{{ meta-handbook.management_ceo }}, Management  
Date: [TODO]

**Next Review:** [TODO] (annually or as needed)

