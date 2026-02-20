# Policy: Security in Projects

**Document-ID:** [FRAMEWORK]-0680
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



**Document ID:** 0680  
**Document Type:** Policy (abstract)  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.5.8, A.8.25, A.8.32 (incl. Amendment 1:2024)  
**Owner:** [TODO]  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** [TODO]  
**Next Review:** [TODO]

## 1. Purpose

This policy defines the requirements for integrating information security into projects of **AdminSend GmbH**. It ensures that security requirements are considered throughout the entire project lifecycle.

## 2. Scope

This policy applies to:

- **Organizational Units:** All departments and locations of AdminSend GmbH
- **Projects:** All IT projects, infrastructure projects, software development projects
- **Project Phases:** Initiation, planning, implementation, closure
- **Project Types:** Internal projects, external projects, partner projects
- **Locations:** [[ netbox.site.name ]] and all other operational sites

**Exceptions:** Exceptions are only permitted through the defined exception process (`0640_Policy_Exceptions_and_Risk_Waivers.md`).

## 3. Policy Statements

### 3.1 Security by Design
Security is integrated into projects from the beginning (security by design). Security requirements are defined during project initiation.

### 3.2 Security Requirements
Security requirements are defined for each project:
- Confidentiality, integrity, availability
- Compliance requirements
- Data protection requirements
- Technical security requirements

### 3.3 Security Risk Assessment
A security risk assessment is conducted for each project. Risks are identified, evaluated, and treated.

### 3.4 Security Architecture Review
Project architectures are reviewed for security. Security architecture review occurs before implementation.

### 3.5 Security Testing
Projects are tested for security:
- Security testing (penetration tests, vulnerability scans)
- Code reviews (SAST, DAST) for software projects
- Configuration reviews for infrastructure projects

### 3.6 Security Sign-Off
Projects receive security sign-off before go-live. Security sign-off confirms that security requirements are met.

### 3.7 Change Management Integration
Security-relevant changes follow the change management process (see `0360_Policy_Change_and_Release_Management.md`).

### 3.8 Third-Party Security
For projects with third parties (suppliers, partners), security requirements are contractually agreed (see `0460_Policy_Supplier_and_Cloud_Security.md`).

### 3.9 Security Documentation
Security-relevant project documentation is created:
- Security Requirements Specification
- Security Architecture Document
- Security Test Report
- Security Sign-Off Document

## 4. Roles and Responsibilities

### RACI Matrix: Security in Projects

| Activity | CISO | Project Manager | Security Architect | IT Operations | Business Owner |
|----------|------|-----------------|-------------------|---------------|----------------|
| Policy Creation | R/A | C | R | C | C |
| Security Requirements | R | R/A | R | C | R |
| Security Risk Assessment | R/A | R | R | C | C |
| Security Architecture Review | R/A | C | R/A | C | C |
| Security Testing | R | R/A | R | R | C |
| Security Sign-Off | R/A | C | C | C | C |
| Change Management | C | R | C | R/A | C |
| Third-Party Security | R/A | R | C | C | R |

**Legend:** R = Responsible (Execution), A = Accountable (Ownership), C = Consulted, I = Informed

### Key Roles

- **Policy Owner:** [TODO] (CISO)
- **Security Architect:** {{ meta-handbook.security_architect }}
- **Project Manager:** Project responsible persons
- **IT Operations Manager:** {{ meta-handbook.it_operations_manager }}
- **Business Owner:** Department responsible persons
- **Control/Audit Function:** ISMS, Internal Audit

## 5. Derived Documents (Guidelines/Standards/Processes)

Implementation details are defined in subordinate documents:

### Related Guidelines
- **0690_Guideline_Security_Requirements_in_Project_Lifecycle.md** - Detailed implementation guideline
- `0380_Policy_Secure_Development.md` - Secure Development Policy
- `0360_Policy_Change_and_Release_Management.md` - Change Management Policy
- `0460_Policy_Supplier_and_Cloud_Security.md` - Supplier Security Policy

### Related Standards/Baselines
- Security Requirements Template
- Security Risk Assessment Template
- Security Architecture Review Checklist
- Security Testing Standards
- Security Sign-Off Template

### Related Processes
- Project Security Review Process
- Security Risk Assessment Process
- Security Architecture Review Process
- Security Testing Process
- Security Sign-Off Process

## 6. Compliance, Monitoring and Enforcement

### Metrics and KPIs
- Number of projects with security requirements (Target: 100%)
- Number of security risk assessments conducted (Target: 100% of all projects)
- Number of security architecture reviews (Target: 100% of critical projects)
- Number of security tests (Target: 100% before go-live)
- Number of security sign-offs (Target: 100% before go-live)
- Average time for security review (Target: < 5 days)
- Number of projects without security sign-off (Target: 0)

### Evidence and Proof
- Security Requirements Specifications
- Security Risk Assessments
- Security Architecture Review Reports
- Security Test Reports (Penetration Tests, Vulnerability Scans)
- Security Sign-Off Documents
- Project Security Checklists
- Change Management Records

### Consequences of Violations
Violations of this policy are handled according to applicable HR and compliance processes:
- **Projects Without Security Requirements:** Project stop until requirements defined
- **Missing Security Risk Assessments:** Remediation before continuation
- **Go-Live Without Security Sign-Off:** Project stop, escalation to management
- **Repeated Violations:** Employment consequences, project responsibility removed

## 7. Exceptions

Exceptions to this policy are only permitted in justified exceptional cases:

- **Exception Process:** See `0640_Policy_Exceptions_and_Risk_Waivers.md`
- **Approval:** Exceptions must be approved by CISO and CIO
- **Documentation:** All exceptions are documented in the risk register
- **Time Limitation:** Exceptions are generally time-limited

## 8. References

### Internal Documents
- `0010_ISMS_Information_Security_Policy.md` - ISMS Policy
- `0690_Guideline_Security_Requirements_in_Project_Lifecycle.md` - Detailed Guideline
- `0380_Policy_Secure_Development.md` - Secure Development Policy
- `0080_ISMS_Risk_Register_Template.md` - Risk Register

### External Standards and Regulations
- **ISO/IEC 27001:2022 Annex A.5.8** - Information security in project management
- **ISO/IEC 27001:2022 Annex A.8.25** - Secure development life cycle
- **ISO/IEC 27001:2022 Annex A.8.32** - Change management
- **NIST SP 800-64** - Security Considerations in the System Development Life Cycle
- **OWASP SAMM** - Software Assurance Maturity Model
- **BSIMM** - Building Security In Maturity Model
- **ISO/IEC 27034** - Application Security

**Approved by:**  
{{ meta-handbook.management_ceo }}, Executive Management  
Date: [TODO]

**Next Review:** [TODO] (annually or as needed)

