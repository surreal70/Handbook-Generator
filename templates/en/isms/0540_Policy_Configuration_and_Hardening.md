# Policy: Configuration and Hardening

**Document-ID:** [FRAMEWORK]-0540
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
This policy establishes the principles for secure configuration and system hardening.
It ensures that systems are configured securely and hardened against attacks.
Customize based on your organization's infrastructure and security baselines.

ISO 27001:2022 Annex A Reference: A.8.9, A.8.10
-->

**Document ID:** 0540  
**Document Type:** Policy (abstract)  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.8.9, A.8.10 (incl. Amendment 1:2024)  
**Owner:** {{ meta.ciso.name }}  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** {{ meta-handbook.modifydate }}  
**Next Review:** {{ meta-handbook.next_review }}

## 1. Purpose

This policy defines the principles for secure configuration and system hardening at **{{ meta-organisation.name }}**. It ensures that IT systems are securely configured and hardened against attacks.

## 2. Scope

This policy applies to:

- **Organizational Units:** All departments and locations of {{ meta-organisation.name }}
- **Systems:** All servers, workstations, network devices, applications, cloud resources
- **Environments:** Production, test, development
- **Locations:** {{ netbox.site.name }} and all other operational sites

**Exceptions:** Exceptions are only permitted through the defined exception process (`0640_Policy_Exceptions_and_Risk_Waivers.md`).

## 3. Principles (Policy Statements)

### 3.1 Security Baselines
Security baselines exist for all system types, defining minimum requirements for secure configuration. Baselines are based on recognized standards (CIS Benchmarks, BSI, vendor best practices).

### 3.2 Secure by Default
Systems are deployed with secure default configurations. Insecure default settings are changed, unnecessary features disabled.

### 3.3 Hardening Measures
Systems are hardened:
- Removal of unnecessary software and services
- Disabling of unneeded ports and protocols
- Changing default credentials
- Minimizing attack surface

### 3.4 Configuration Management
Configurations are centrally managed and versioned (Infrastructure as Code, configuration management tools). Changes are controlled through change management.

### 3.5 Configuration Drift Detection
Deviations from security baselines (configuration drift) are automatically detected and reported. Unauthorized changes are rolled back.

### 3.6 Least Functionality
Systems are configured according to the principle of least functionality. Only required functions and services are enabled.

### 3.7 Secure Configuration Reviews
Configurations are regularly reviewed:
- **Critical Systems:** Quarterly
- **Important Systems:** Semi-annually
- **Standard Systems:** Annually

### 3.8 Documentation
All configuration deviations from baselines are documented and justified. Documentation is current and traceable.

## 4. Roles and Responsibilities

### RACI Matrix: Configuration and Hardening

| Activity | CISO | IT Operations | System Owner | Security Team | Change Management |
|----------|------|---------------|--------------|---------------|-------------------|
| Policy Creation | R/A | C | C | C | I |
| Baseline Creation | A | C | C | R | I |
| System Hardening | C | R/A | C | C | I |
| Configuration Management | C | R/A | C | I | C |
| Drift Detection | A | C | I | R | I |
| Configuration Reviews | A | C | R | R | I |
| Compliance Review | R/A | C | C | C | I |

**Legend:** R = Responsible (Execution), A = Accountable (Ownership), C = Consulted, I = Informed

### Key Roles

- **Policy Owner:** {{ meta.ciso.name }} (CISO)
- **Configuration Manager:** {{ meta.it.config_manager }}
- **Security Architect:** {{ meta.security.architect }}
- **Implementation Responsible:** IT Operations, System Owner
- **Control/Audit Function:** ISMS, Internal Audit

## 5. Derivatives (Guidelines/Standards/Processes)

Implementation details are defined in subordinate documents:

### Associated Guidelines
- **0550_Guideline_Security_Baselines_Hardening_and_Config_Changes.md** - Detailed implementation guideline
- `0360_Policy_Change_and_Release_Management.md` - Change Management Policy
- `0340_Policy_Vulnerability_and_Patch_Management.md` - Vulnerability Management Policy

### Associated Standards/Baselines
- Security baselines (Windows, Linux, network devices, cloud)
- Hardening guides
- Configuration management standards
- Drift detection rules

### Associated Processes
- Configuration management process
- Hardening process
- Configuration review process
- Drift remediation process

## 6. Compliance, Monitoring and Enforcement

### Metrics and KPIs
- Baseline compliance rate (Target: 95%)
- Number of configuration drift findings
- Average time to drift remediation
- Configuration review completion rate (Target: 100%)
- Number of systems with default credentials (Target: 0)
- Hardening coverage (Target: 100% of critical systems)

### Evidence and Proof
- Security baselines documentation
- Configuration management logs
- Drift detection reports
- Configuration review reports
- Hardening checklists
- Audit reports on configuration compliance

### Consequences of Violations
Violations of this policy are handled according to applicable HR and compliance processes:
- **Non-hardened Systems:** Immediate remediation, production block
- **Configuration Drift:** Remediation by priority
- **Default Credentials:** Immediate change, incident response
- **Repeated Violations:** Employment consequences

## 7. Exceptions

Exceptions to this policy are only permitted in justified exceptional cases:

- **Exception Process:** See `0640_Policy_Exceptions_and_Risk_Waivers.md`
- **Approval:** Exceptions must be approved by CISO and System Owner
- **Documentation:** All exceptions are documented in the risk register
- **Time Limitation:** Exceptions are generally time-limited
- **Compensating Controls:** Exceptions require alternative security measures

## 8. References

### Internal Documents
- `0010_ISMS_Information_Security_Policy.md` - ISMS Policy
- `0550_Guideline_Security_Baselines_Hardening_and_Config_Changes.md` - Detailed Guideline
- `0360_Policy_Change_and_Release_Management.md` - Change Management Policy
- `0080_ISMS_Risk_Register_Template.md` - Risk Register

### External Standards and Requirements
- **ISO/IEC 27001:2022 Annex A.8.9** - Configuration management
- **ISO/IEC 27001:2022 Annex A.8.10** - Information deletion
- **CIS Benchmarks** - Center for Internet Security Configuration Benchmarks
- **NIST SP 800-123** - Guide to General Server Security
- **BSI IT-Grundschutz** - Security requirements

**Approved by:**  
{{ meta.management.ceo }}, Management  
Date: {{ meta-handbook.modifydate }}

**Next Review:** {{ meta-handbook.next_review }} (annually or as needed)

