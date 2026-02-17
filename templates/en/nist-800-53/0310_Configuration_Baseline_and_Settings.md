# Configuration Baseline and Settings

**Document-ID:** [FRAMEWORK]-0310
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

## 1. Control Description

This document covers configuration baseline and settings controls:
- **CM-2:** Baseline Configuration
- **CM-6:** Configuration Settings
- **CM-7:** Least Functionality

## 2. Control Implementation

### 2.1 Baseline Configuration (CM-2)

**Baseline Components:**
- Operating system configurations
- Application configurations
- Network device configurations
- Security tool configurations
- Database configurations

[TODO: Define baseline components]

**Baseline Documentation:**
| System/Component | Baseline Version | Last Updated | Owner |
|------------------|------------------|--------------|-------|
| [TODO] | [TODO] | [TODO] | [TODO] |

**Baseline Review:**
- Review frequency: [TODO: e.g., Annually or upon significant changes]
- Approval authority: [TODO: Role/Committee]
- Update procedures: [TODO: Process]

### 2.2 Configuration Settings (CM-6)

**Mandatory Configuration Settings:**
| Setting Category | Requirement | Rationale |
|-----------------|-------------|-----------|
| Password policy | Minimum 12 characters, complexity required | Security best practice |
| Session timeout | 15 minutes inactivity | Prevent unauthorized access |
| Encryption | TLS 1.2 or higher | Data protection |
| Logging | All security events | Audit trail |
| [TODO] | [TODO] | [TODO] |

**Configuration Standards:**
- CIS Benchmarks
- DISA STIGs
- Vendor hardening guides
- Organization-specific standards

[TODO: Specify applicable standards]

**Configuration Verification:**
- Automated scanning tools
- Manual reviews
- Compliance checks

[TODO: Define verification procedures]

### 2.3 Least Functionality (CM-7)

**Prohibited Functions:**
- Unnecessary services
- Unused protocols
- Deprecated features
- Development tools on production systems
- Guest accounts

[TODO: List prohibited functions]

**Allowed Functions:**
[TODO: Define allowed functions and justification]

**Review Process:**
- Periodic functionality reviews
- Exception approval process
- Documentation requirements

[TODO: Define review process]

## 3. Control Enhancements

- **CM-2(1):** Reviews and Updates
- **CM-2(2):** Automation Support for Accuracy and Currency
- **CM-2(3):** Retention of Previous Configurations
- **CM-2(6):** Development and Test Environments
- **CM-2(7):** Configure Systems and Components for High-Risk Areas
- **CM-6(1):** Automated Management, Application, and Verification
- **CM-6(2):** Respond to Unauthorized Changes
- **CM-7(1):** Periodic Review
- **CM-7(2):** Prevent Program Execution
- **CM-7(5):** Authorized Software - Allow by Exception

[TODO: Mark applicable enhancements]

## 4. Implementation Status

**Status:** [TODO: Implemented / Partially Implemented / Planned / Not Applicable]  
**Implementation Date:** [TODO: Date]  
**Responsible:** [TODO: Name/Role]  

## 5. Assessment

**Assessment Method:** Examine, Interview, Test  
**Assessment Status:** [TODO: Satisfied / Other than Satisfied / Not Applicable]  
**Findings:** [TODO: Description]  

<!-- End of template -->
