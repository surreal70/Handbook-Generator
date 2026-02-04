# Policy: Secure Development

<!-- 
TEMPLATE AUTHOR NOTE:
This policy establishes the principles for secure software development lifecycle (SDLC).
It ensures that security is integrated into all phases of software development.
Customize based on your organization's development practices (Agile, DevSecOps, etc.).

ISO 27001:2022 Annex A Reference: A.8.25, A.8.26, A.8.27, A.8.28
-->

**Document ID:** 0380  
**Document Type:** Policy (abstract)  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.8.25-A.8.28 (incl. Amendment 1:2024)  
**Owner:** {{ meta.ciso.name }}  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** {{ meta.document.date }}  
**Next Review:** {{ meta.document.next_review }}

---

## 1. Purpose

This policy defines the principles for secure software development (Secure SDLC) at **{{ meta.organization.name }}**. It ensures that security is integrated into all phases of the software development lifecycle and that applications are developed, tested, and operated securely.

## 2. Scope

This policy applies to:

- **Organizational Units:** All development teams and locations of {{ meta.organization.name }}
- **Applications:** All internally developed applications, APIs, microservices, mobile apps
- **Development Phases:** Requirements, design, implementation, testing, deployment, maintenance
- **Development Models:** Agile, Waterfall, DevOps, DevSecOps
- **Locations:** {{ netbox.site.name }} and all other development sites

**Exceptions:** Exceptions are only permitted through the defined exception process (`0640_Policy_Exceptions_and_Risk_Waivers.md`).

## 3. Principles (Policy Statements)

### 3.1 Security by Design
Security is integrated into the development process from the beginning (Shift Left). Security requirements are defined in the requirements phase and considered in design.

### 3.2 Secure Coding Standards
Developers follow recognized secure coding standards (OWASP, CERT, CWE). Code is developed according to best practices to avoid common vulnerabilities.

### 3.3 Code Reviews and Peer Reviews
All code changes undergo code reviews. Security-relevant code requires additional security reviews by the security team.

### 3.4 Automated Security Testing
Security testing is integrated into the CI/CD pipeline:
- **SAST (Static Application Security Testing):** Static code analysis
- **DAST (Dynamic Application Security Testing):** Dynamic security tests
- **SCA (Software Composition Analysis):** Analysis of dependencies and open-source components
- **Container Scanning:** Security review of container images

### 3.5 Secrets Management
Secrets (passwords, API keys, certificates) are never stored in code or repositories. Secrets are managed in dedicated secrets management systems.

### 3.6 Dependency Management
External libraries and dependencies are checked for known vulnerabilities. Outdated or insecure dependencies are updated promptly.

### 3.7 Security Testing Before Production Release
Comprehensive security tests are performed before production release:
- Penetration testing for critical applications
- Security acceptance testing
- Vulnerability assessment

### 3.8 Secure Deployment and Configuration
Applications are deployed with secure configurations. Default credentials are changed, unnecessary features disabled, hardening measures applied.

## 4. Roles and Responsibilities

### RACI Matrix: Secure Development

| Activity | CISO | Security Champion | Developer | DevOps | Security Team |
|----------|------|-------------------|-----------|--------|---------------|
| Policy creation | R/A | C | C | C | C |
| Security requirements | C | R | C | I | R/A |
| Secure coding | I | C | R/A | I | C |
| Code review | I | R | R | I | C |
| Security review | A | C | I | I | R |
| SAST/DAST/SCA | C | C | I | R | R/A |
| Penetration testing | A | I | I | I | R |
| Security training | A | C | R | R | R |

**Legend:** R = Responsible (Execution), A = Accountable (Ownership), C = Consulted, I = Informed

### Key Roles

- **Policy Owner:** {{ meta.ciso.name }} (CISO)
- **Security Champion:** Developer with security expertise in each team
- **Application Security Lead:** {{ meta.security.appsec_lead }}
- **Implementation Responsible:** Developers, DevOps, Security Team
- **Control/Audit Function:** ISMS, Internal Audit

## 5. Derivations (Guidelines/Standards/Processes)

Implementation details are defined in subordinate documents:

### Related Guidelines
- **0390_Guideline_Secure_SDLC_Coding_Review_and_Secrets.md** - Detailed implementation guideline
- `0360_Policy_Change_and_Release_Management.md` - Change Management Policy
- `0340_Policy_Vulnerability_and_Patch_Management.md` - Vulnerability Management Policy
- `0260_Policy_Cryptography_and_Key_Management.md` - Cryptography Policy

### Related Standards/Baselines
- Secure coding standards (OWASP, CERT)
- Code review checklists
- SAST/DAST/SCA tool configurations
- Secrets management standards

### Related Processes
- Secure SDLC process
- Code review process
- Security testing process
- Vulnerability disclosure process

## 6. Compliance, Monitoring and Enforcement

### Metrics and KPIs
- Number of security vulnerabilities per release (target: 50% annual reduction)
- Code review coverage (target: 100%)
- SAST/DAST/SCA coverage (target: 100% of critical applications)
- Mean time to remediate vulnerabilities (MTTR)
- Number of secrets in code (target: 0)
- Security training completion rate (target: 100% annually)

### Evidence and Proof
- Code review documentation
- SAST/DAST/SCA reports
- Penetration test reports
- Security acceptance test results
- Secrets scanning reports
- Security training evidence

### Consequences of Violations
Violations of this policy are handled according to applicable HR and compliance processes:
- **Secrets in code:** Immediate rotation, incident response, retraining
- **Skipped code reviews:** Rollback, completion, warning
- **Ignored security findings:** Remediation, retraining
- **Repeated violations:** Employment consequences

## 7. Exceptions

Exceptions to this policy are only permitted in justified cases:

- **Exception Process:** See `0640_Policy_Exceptions_and_Risk_Waivers.md`
- **Approval:** Exceptions must be approved by CISO and Application Security Lead
- **Documentation:** All exceptions are documented in the risk register
- **Time Limitation:** Exceptions are generally time-limited
- **Compensating Controls:** Exceptions require alternative security measures

## 8. References

### Internal Documents
- `0010_ISMS_Information_Security_Policy.md` - ISMS Policy
- `0390_Guideline_Secure_SDLC_Coding_Review_and_Secrets.md` - Detailed Guideline
- `0360_Policy_Change_and_Release_Management.md` - Change Management Policy
- `0080_ISMS_Risk_Register_Template.md` - Risk Register

### External Standards and Requirements
- **ISO/IEC 27001:2022 Annex A.8.25** - Secure development lifecycle
- **ISO/IEC 27001:2022 Annex A.8.26** - Application security requirements
- **ISO/IEC 27001:2022 Annex A.8.27** - Secure system architecture and engineering principles
- **ISO/IEC 27001:2022 Annex A.8.28** - Secure coding
- **OWASP Top 10** - Web Application Security Risks
- **OWASP ASVS** - Application Security Verification Standard
- **NIST SP 800-218** - Secure Software Development Framework (SSDF)
- **CWE Top 25** - Most Dangerous Software Weaknesses

---

**Approved by:**  
{{ meta.management.ceo }}, Management  
Date: {{ meta.document.approval_date }}

**Next Review:** {{ meta.document.next_review }} (annually or as needed)
