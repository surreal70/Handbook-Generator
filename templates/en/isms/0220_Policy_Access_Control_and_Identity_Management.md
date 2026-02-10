# Policy: Access Control and Identity Management

<!-- 
TEMPLATE AUTHOR NOTE:
This policy establishes the principles for access control and identity management.
It ensures that access to information and systems is granted based on business need
and the principle of least privilege. Customize based on your organization's
access control requirements and IAM maturity.

ISO 27001:2022 Annex A Reference: A.5.15, A.5.16, A.5.17, A.5.18
-->

**Document ID:** 0220  
**Document Type:** Policy (abstract)  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.5.15-A.5.18 (incl. Amendment 1:2024)  
**Owner:** {{ meta.ciso.name }}  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** {{ meta.document.date }}  
**Next Review:** {{ meta.document.next_review }}

---

## 1. Purpose

This policy defines the principles for access control and identity management (IAM) at **{{ meta.organization.name }}**. It ensures that access to information and IT systems is granted exclusively to authorized persons based on the need-to-know principle and least privilege.

## 2. Scope

This policy applies to:

- **Organizational Units:** All departments and locations of {{ meta.organization.name }}
- **Systems:** All IT systems, applications, databases, networks, cloud services
- **Persons:** All employees, contractors, suppliers, and third parties with access to IT resources
- **Access Methods:** Local access, remote access, privileged access, API access
- **Locations:** {{ netbox.site.name }} and all other operational sites

**Exceptions:** Exceptions are only permitted through the defined exception process (`0640_Policy_Ausnahmen_und_Risk_Waivers.md`).

## 3. Principles (Policy Statements)

### 3.1 Least Privilege
Users receive only the minimum access rights required to fulfill their duties. Privileged access is granted restrictively and reviewed regularly.

### 3.2 Need-to-Know Principle
Access to information is only granted when there is a business necessity. Access is granted based on roles and responsibilities.

### 3.3 Identity Lifecycle (Joiner-Mover-Leaver)
Identities are managed throughout their entire lifecycle:
- **Joiner:** Access rights are granted upon entry based on role and function
- **Mover:** Access rights are adjusted during role changes (revoke old rights, grant new ones)
- **Leaver:** All access rights are immediately revoked upon departure

### 3.4 Role-Based Access Control (RBAC)
Access rights are primarily granted through roles and groups, not through individual permissions. Role models are regularly reviewed and updated.

### 3.5 Segregation of Duties
Critical functions are divided so that no single person can perform all steps of a sensitive process. This prevents fraud and errors.

### 3.6 Regular Recertification
Access rights are regularly reviewed and recertified (at least annually). Rights that are no longer needed are revoked.

### 3.7 Privileged Access Management (PAM)
Privileged accounts (administrators, root, service accounts) are subject to special controls:
- Separate accounts for privileged activities
- Just-in-Time (JIT) access where possible
- Comprehensive logging and monitoring

### 3.8 Access Approval and Documentation
All access grants must be approved and documented by the resource owner. Access decisions are traceable and auditable.

## 4. Roles and Responsibilities

### RACI Matrix: Access Control and IAM

| Activity | CISO | IT Operations | Resource Owner | HR | Employee |
|----------|------|---------------|----------------|-----|----------|
| Policy Creation | R/A | C | C | C | I |
| IAM System Operations | C | R/A | I | I | I |
| Request Access | I | I | C | I | R |
| Approve Access | C | I | R/A | C | I |
| Provision Access | I | R | I | I | I |
| Recertification | C | C | R/A | C | I |
| Revoke Access (Leaver) | C | R | I | R/A | I |
| Monitoring and Audits | R/A | C | C | I | I |

**Legend:** R = Responsible (Execution), A = Accountable (Accountable), C = Consulted (Consulted), I = Informed (Informed)

### Key Roles

- **Policy Owner:** {{ meta.ciso.name }} (CISO)
- **IAM Manager:** {{ meta.it.iam_manager }}
- **Resource Owners:** Department heads, system owners
- **Implementation Responsible:** IT operations, HR
- **Control/Audit Function:** ISMS, internal audit

## 5. Derivations (Guidelines/Standards/Processes)

Implementation details are defined in subordinate documents:

### Related Guidelines
- **0230_Richtlinie_IAM_Joiner_Mover_Leaver_und_Zugriffsantraege.md** - Detailed IAM guideline
- `0240_Policy_Authentisierung_und_Passwoerter.md` - Authentication policy
- `0520_Policy_HR_Security.md` - HR security policy
- `0640_Policy_Ausnahmen_und_Risk_Waivers.md` - Exception policy

### Related Standards/Baselines
- Role model and RBAC matrix
- Privileged Access Management (PAM) standard
- Recertification process
- Service account management

### Related Processes
- Joiner-Mover-Leaver process
- Access approval process
- Recertification process
- Incident response for unauthorized access

## 6. Compliance, Monitoring, and Enforcement

### Metrics and KPIs
- Number of open access requests and average processing time
- Recertification rate (target: 100% annually)
- Number of non-recertified accounts
- Number of privileged accounts and their usage frequency
- Number of least privilege violations
- Average time to deactivate leaver accounts (target: < 1 day)

### Evidence and Proof
- IAM system logs and audit trails
- Access approvals and requests
- Recertification evidence
- Joiner-Mover-Leaver documentation
- Privileged access logs
- Audit reports on access rights

### Consequences for Violations
Violations of this policy are handled according to applicable HR and compliance processes:
- **Unauthorized access grants:** Immediate suspension, investigation, possible disciplinary action
- **Non-recertified accounts:** Automatic deactivation after deadline
- **Abuse of privileged access:** Immediate suspension, employment law consequences
- **Sharing of credentials:** Warning up to termination

## 7. Exceptions

Exceptions to this policy are only permitted in justified exceptional cases:

- **Exception Process:** See `0640_Policy_Ausnahmen_und_Risk_Waivers.md`
- **Approval:** Exceptions must be approved by CISO and resource owner
- **Documentation:** All exceptions are documented in the risk register
- **Time Limit:** Exceptions are generally time-limited and regularly reviewed

## 8. References

### Internal Documents
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS policy
- `0230_Richtlinie_IAM_Joiner_Mover_Leaver_und_Zugriffsantraege.md` - Detailed IAM guideline
- `0080_ISMS_Risikoregister_Template.md` - Risk register
- `0530_Richtlinie_HR_Onboarding_Rollenwechsel_Offboarding.md` - HR security guideline

### External Standards and Requirements
- **ISO/IEC 27001:2022 Annex A.5.15** - Identity management
- **ISO/IEC 27001:2022 Annex A.5.16** - Access rights
- **ISO/IEC 27001:2022 Annex A.5.17** - Authentication information
- **ISO/IEC 27001:2022 Annex A.5.18** - Access rights review
- **ISO/IEC 27002:2022** - Information security controls
- **NIST SP 800-63** - Digital Identity Guidelines

---

**Approved by:**  
{{ meta.management.ceo }}, Management  
Date: {{ meta.document.approval_date }}

**Next Review:** {{ meta.document.next_review }} (annually or as needed)

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial Creation |
