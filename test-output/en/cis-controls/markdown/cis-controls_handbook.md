# CIS Controls v8 Hardening Templates Handbook

**Document Metadata**

- **Created on:** 2026-02-05
- **Author:** Andreas Huemmer [andreas.huemmer@adminsend.de]
- **Version:** 0.0.3
- **Type:** CIS Controls v8 Hardening Handbook

---



# CIS Controls – Overview and Approach

**Document ID:** 0010  
**Document Type:** Foundation Document  
**Reference Framework:** CIS Controls v8 (Hardening Program; no benchmark texts)  
**Owner:** [TODO]  
**Version:** 0.1 (Draft)  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Updated:** 2026-01-31  
**Next Review:** [TODO]

---

> **Note:** Template. Replace all `[TODO]` placeholders and remove non-applicable sections.  
> **Important:** This template does not paraphrase CIS original texts. Use it to derive and demonstrably implement **internal baselines/standards**.

## 1. Objective
Describes how CIS Controls v8 is used as a framework to derive hardening baselines per platform/application.

## 2. Terms
- Baseline: Minimal, auditable configuration standard per platform.
- Standard: Specification for an application/component.
- Compliance: Degree of fulfillment (e.g., % systems compliant).

## 3. Derivation Logic (practical)
1. Define asset groups (servers, clients, cloud workloads, containers, network devices).
2. Classify protection needs & criticality (tiering).
3. Prioritize controls/safeguards (e.g., IG1/IG2/IG3) – organization-specific.
4. Define and parameterize baselines/standards.
5. Deploy automatically and monitor drift.
6. Measure, improve, manage exception-based.

## 4. Output Artifacts
- OS Baselines: 0110–0150
- Application Standards: 0210+
- Evidence/Reporting: 0410


# Scope, Asset Groups and Tiering

**Document ID:** 0020  
**Document Type:** Foundation Document  
**Reference Framework:** CIS Controls v8 (Hardening Program; no benchmark texts)  
**Owner:** [TODO]  
**Version:** 0.1 (Draft)  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Updated:** 2026-01-31  
**Next Review:** [TODO]

---

> **Note:** Template. Replace all `[TODO]` placeholders and remove non-applicable sections.  
> **Important:** This template does not paraphrase CIS original texts. Use it to derive and demonstrably implement **internal baselines/standards**.

## 1. Scope
- Organization/Locations/Cloud Accounts: [TODO]
- In-Scope Asset Types: [TODO]

## 2. Asset Groups (Examples)
| Group | Examples | Tooling/Source |
|---|---|---|
| Servers | Windows/Linux | CMDB/Cloud Inventory |
| Clients | Windows/macOS | MDM |
| Containers | Base Images / Runtimes | Registry/Scanner |
| Network | Firewalls/Switches | NMS |

## 3. Tiering / Criticality
> Classify baselines by tiers (e.g., Tier 0/1/2) or protection needs.
| Tier | Description | Minimum Requirements |
|---|---|---|
| T0 | Identity/Security Core (IAM, PKI, SIEM) | strictest baseline |
| T1 | Production-critical | high baseline |
| T2 | Standard | baseline |
| T3 | Dev/Test | potentially reduced baseline (risk-based) |

## 4. Responsibilities
- Asset Owner: [TODO]
- Platform Team: [TODO]
- Security/ISMS: [TODO]


# Hardening Lifecycle: Baselines, Change and Compliance

**Document ID:** 0030  
**Document Type:** Process Description  
**Reference Framework:** CIS Controls v8 (Hardening Program; no benchmark texts)  
**Owner:** [TODO]  
**Version:** 0.1 (Draft)  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Updated:** 2026-01-31  
**Next Review:** [TODO]

---

> **Note:** Template. Replace all `[TODO]` placeholders and remove non-applicable sections.  
> **Important:** This template does not paraphrase CIS original texts. Use it to derive and demonstrably implement **internal baselines/standards**.

## 1. Lifecycle (End-to-End)
- Definition -> Test -> Approval -> Rollout -> Operations -> Review

## 2. Change Management
- Baseline changes are changes: [TODO]
- Emergency changes: [TODO]
- Communication/Release Notes: [TODO]

## 3. Compliance Verification
- Measurement point (Agent/Scanner/Config): [TODO]
- Frequency: [TODO]
- Thresholds (e.g., <95% = escalation): [TODO]

## 4. Drift & Remediation
- Auto-remediation vs. ticket: [TODO]
- Exception handling: [TODO]


# Exception Process and Risk Acceptance

**Document ID:** 0040  
**Document Type:** Process/Template  
**Reference Framework:** CIS Controls v8 (Hardening Program; no benchmark texts)  
**Owner:** [TODO]  
**Version:** 0.1 (Draft)  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Updated:** 2026-01-31  
**Next Review:** [TODO]

---

> **Note:** Template. Replace all `[TODO]` placeholders and remove non-applicable sections.  
> **Important:** This template does not paraphrase CIS original texts. Use it to derive and demonstrably implement **internal baselines/standards**.

## 1. Objective
Enable risk-based, time-limited exceptions from hardening requirements, including tracking.

## 2. When is an Exception Permissible?
- Technical impossibility (legacy): [TODO]
- Business necessity with compensating controls: [TODO]

## 3. Process
1. Request (ticket/form): [TODO]
2. Risk analysis (impact, exposure, compensation): [TODO]
3. Approval (risk owner + security): [TODO]
4. Duration & review: [TODO]
5. Closure/remediation: [TODO]

## 4. Exception Register
| Exception ID | Asset/Scope | Requirement | Justification | Compensating Controls | Risk | Owner | Valid Until | Status |
|---|---|---|---|---|---|---|---|---|
| EX-001 | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | Open |


# Test and Validation Strategy

**Document ID:** 0050  
**Document Type:** Foundation Document  
**Reference Framework:** CIS Controls v8 (Hardening Program; no benchmark texts)  
**Owner:** [TODO]  
**Version:** 0.1 (Draft)  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Updated:** 2026-01-31  
**Next Review:** [TODO]

---

> **Note:** Template. Replace all `[TODO]` placeholders and remove non-applicable sections.  
> **Important:** This template does not paraphrase CIS original texts. Use it to derive and demonstrably implement **internal baselines/standards**.

## 1. Test Stages
- Unit/Config Test (e.g., linting, policy test): [TODO]
- Integration (pilot group): [TODO]
- Regression (critical apps): [TODO]
- Security Checks (scanner/config audit): [TODO]

## 2. Acceptance Criteria
- No critical operational disruptions: [TODO]
- Baseline compliance after rollout >= [TODO]%
- Documentation/evidence updated: [TODO]

## 3. Rollback
- Rollback method: [TODO]
- Max. rollback time: [TODO]


# Operating Systems – Overview

**Document ID:** 0100  
**Document Type:** Chapter  
**Reference Framework:** CIS Controls v8 (Hardening Program; no benchmark texts)  
**Owner:** [TODO]  
**Version:** 0.1 (Draft)  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Updated:** 2026-01-31  
**Next Review:** [TODO]

---

> **Note:** Template. Replace all `[TODO]` placeholders and remove non-applicable sections.  
> **Important:** This template does not paraphrase CIS original texts. Use it to derive and demonstrably implement **internal baselines/standards**.

This chapter contains **OS hardening baselines**.  
Recommendation: Create a **parameterized baseline** per OS version/edition and manage exceptions centrally.

- Windows Server: 0110
- Windows Client: 0120
- Linux (Generic): 0130
- macOS: 0140
- Container Base Images: 0150


# OS Hardening Baseline: Windows Server

**Document ID:** 0110  
**Document Type:** Baseline  
**Reference Framework:** CIS Controls v8 (Hardening Program; no benchmark texts)  
**Owner:** [TODO]  
**Version:** 0.1 (Draft)  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Updated:** 2026-01-31  
**Next Review:** [TODO]

---

> **Note:** Template. Replace all `[TODO]` placeholders and remove non-applicable sections.  
> **Important:** This template does not paraphrase CIS original texts. Use it to derive and demonstrably implement **internal baselines/standards**.

## 1. Purpose
[TODO] (e.g., attack surface reduction, uniform baseline, auditability)

## 2. Scope
- Target platform(s): [TODO]
- Versions/editions: [TODO]
- Environments: Prod / Test / Dev / End-user
- Exceptions: only via exception process (`0040_Exceptions_Risk_Acceptance.md`)

## 3. Target State and Principles
- Default-deny where appropriate (e.g., inbound firewall): [TODO]
- Least privilege / role-based admin: [TODO]
- Secure by default (new systems are compliant): [TODO]
- Automation preferred (IaC/config mgmt): [TODO]

## 4. CIS Control Mapping
> Enter the relevant CIS Controls/Safeguards that support this baseline.
| CIS Control | Safeguard/Intent (brief) | Baseline Requirement | Evidence |
|---|---|---|---|
| [TODO] | [TODO] | [TODO] | [TODO] |

## 5. Baseline Requirements (MUST)
> Formulate auditable requirements (not "should"), including responsibility and measurement criteria.
| Area | Requirement (MUST) | Default Value/Target | Responsible | Verification |
|---|---|---|---|---|
| Accounts | [TODO] | [TODO] | [TODO] | [TODO] |
| Network | [TODO] | [TODO] | [TODO] | [TODO] |
| Updates | [TODO] | [TODO] | [TODO] | [TODO] |
| Logging | [TODO] | [TODO] | [TODO] | [TODO] |
| Services | [TODO] | [TODO] | [TODO] | [TODO] |

## 6. Recommendations (SHOULD)
- [TODO]
- [TODO]

## 7. Implementation
### 7.1 Implementation Method
- Manual / GPO / MDM / Ansible / SCCM / Puppet / Chef / IaC: [TODO]
- Rollout strategy (pilot, stages, waves): [TODO]

### 7.2 Step Sequence (High-Level)
1. Define baseline parameters (parameter file): [TODO]
2. Define and test pilot group: [TODO]
3. Rollout with change management: [TODO]
4. Activate continuous compliance verification: [TODO]

## 8. Validation and Testing
- Smoke tests: [TODO]
- Regression tests: [TODO]
- Security tests (scan/config audit): [TODO]
- Acceptance criteria: [TODO]

## 9. Monitoring and Compliance
- Config drift detection: [TODO]
- Reporting (KPIs): [TODO]
- Remediation (auto-fix / ticket): [TODO]

## 10. Exceptions
- Reference: `0040_Exceptions_Risk_Acceptance.md`
- Document temporary deviations: [TODO]

## 11. Appendices
- Parameter list/example values: [TODO]
- Checklist: see `0410_Appendix_Checklists_and_Evidence.md`


## 12. Windows-Specific Areas (Examples)
### 12.1 Identity & Admin Tiering
- Tier model (e.g., Tier0/Tier1/Tier2): [TODO]
- Separate admin accounts: [TODO]
- Local admin password solution / privileged access: [TODO]

### 12.2 GPO/MDM Baselines
- Baseline GPOs (naming/OU): [TODO]
- Security templates: [TODO]

### 12.3 Services & Roles
- Disabled by default: [TODO]
- Remote management (WinRM/RDP) secured: [TODO]


# OS Hardening Baseline: Windows Client

**Document ID:** 0120  
**Document Type:** Baseline  
**Reference Framework:** CIS Controls v8 (Hardening Program; no benchmark texts)  
**Owner:** [TODO]  
**Version:** 0.1 (Draft)  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Updated:** 2026-01-31  
**Next Review:** [TODO]

---

> **Note:** Template. Replace all `[TODO]` placeholders and remove non-applicable sections.  
> **Important:** This template does not paraphrase CIS original texts. Use it to derive and demonstrably implement **internal baselines/standards**.

## 1. Purpose
[TODO] (e.g., attack surface reduction, uniform baseline, auditability)

## 2. Scope
- Target platform(s): [TODO]
- Versions/editions: [TODO]
- Environments: Prod / Test / Dev / End-user
- Exceptions: only via exception process (`0040_Exceptions_Risk_Acceptance.md`)

## 3. Target State and Principles
- Default-deny where appropriate (e.g., inbound firewall): [TODO]
- Least privilege / role-based admin: [TODO]
- Secure by default (new systems are compliant): [TODO]
- Automation preferred (IaC/config mgmt): [TODO]

## 4. CIS Control Mapping
> Enter the relevant CIS Controls/Safeguards that support this baseline.
| CIS Control | Safeguard/Intent (brief) | Baseline Requirement | Evidence |
|---|---|---|---|
| [TODO] | [TODO] | [TODO] | [TODO] |

## 5. Baseline Requirements (MUST)
> Formulate auditable requirements (not "should"), including responsibility and measurement criteria.
| Area | Requirement (MUST) | Default Value/Target | Responsible | Verification |
|---|---|---|---|---|
| Accounts | [TODO] | [TODO] | [TODO] | [TODO] |
| Network | [TODO] | [TODO] | [TODO] | [TODO] |
| Updates | [TODO] | [TODO] | [TODO] | [TODO] |
| Logging | [TODO] | [TODO] | [TODO] | [TODO] |
| Services | [TODO] | [TODO] | [TODO] | [TODO] |

## 6. Recommendations (SHOULD)
- [TODO]
- [TODO]

## 7. Implementation
### 7.1 Implementation Method
- Manual / GPO / MDM / Ansible / SCCM / Puppet / Chef / IaC: [TODO]
- Rollout strategy (pilot, stages, waves): [TODO]

### 7.2 Step Sequence (High-Level)
1. Define baseline parameters (parameter file): [TODO]
2. Define and test pilot group: [TODO]
3. Rollout with change management: [TODO]
4. Activate continuous compliance verification: [TODO]

## 8. Validation and Testing
- Smoke tests: [TODO]
- Regression tests: [TODO]
- Security tests (scan/config audit): [TODO]
- Acceptance criteria: [TODO]

## 9. Monitoring and Compliance
- Config drift detection: [TODO]
- Reporting (KPIs): [TODO]
- Remediation (auto-fix / ticket): [TODO]

## 10. Exceptions
- Reference: `0040_Exceptions_Risk_Acceptance.md`
- Document temporary deviations: [TODO]

## 11. Appendices
- Parameter list/example values: [TODO]
- Checklist: see `0410_Appendix_Checklists_and_Evidence.md`


## 12. Client-Specific Areas (Examples)
- MDM/Intune/SCCM baseline: [TODO]
- BitLocker/device encryption: [TODO]
- Browser hardening (policy): [TODO]
- USB/device control: [TODO]


# OS Hardening Baseline: Linux (Generic)

**Document ID:** 0130  
**Document Type:** Baseline  
**Reference Framework:** CIS Controls v8 (Hardening Program; no benchmark texts)  
**Owner:** [TODO]  
**Version:** 0.1 (Draft)  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Updated:** 2026-01-31  
**Next Review:** [TODO]

---

> **Note:** Template. Replace all `[TODO]` placeholders and remove non-applicable sections.  
> **Important:** This template does not paraphrase CIS original texts. Use it to derive and demonstrably implement **internal baselines/standards**.

## 1. Purpose
[TODO] (e.g., attack surface reduction, uniform baseline, auditability)

## 2. Scope
- Target platform(s): [TODO]
- Versions/editions: [TODO]
- Environments: Prod / Test / Dev / End-user
- Exceptions: only via exception process (`0040_Exceptions_Risk_Acceptance.md`)

## 3. Target State and Principles
- Default-deny where appropriate (e.g., inbound firewall): [TODO]
- Least privilege / role-based admin: [TODO]
- Secure by default (new systems are compliant): [TODO]
- Automation preferred (IaC/config mgmt): [TODO]

## 4. CIS Control Mapping
> Enter the relevant CIS Controls/Safeguards that support this baseline.
| CIS Control | Safeguard/Intent (brief) | Baseline Requirement | Evidence |
|---|---|---|---|
| [TODO] | [TODO] | [TODO] | [TODO] |

## 5. Baseline Requirements (MUST)
> Formulate auditable requirements (not "should"), including responsibility and measurement criteria.
| Area | Requirement (MUST) | Default Value/Target | Responsible | Verification |
|---|---|---|---|---|
| Accounts | [TODO] | [TODO] | [TODO] | [TODO] |
| Network | [TODO] | [TODO] | [TODO] | [TODO] |
| Updates | [TODO] | [TODO] | [TODO] | [TODO] |
| Logging | [TODO] | [TODO] | [TODO] | [TODO] |
| Services | [TODO] | [TODO] | [TODO] | [TODO] |

## 6. Recommendations (SHOULD)
- [TODO]
- [TODO]

## 7. Implementation
### 7.1 Implementation Method
- Manual / GPO / MDM / Ansible / SCCM / Puppet / Chef / IaC: [TODO]
- Rollout strategy (pilot, stages, waves): [TODO]

### 7.2 Step Sequence (High-Level)
1. Define baseline parameters (parameter file): [TODO]
2. Define and test pilot group: [TODO]
3. Rollout with change management: [TODO]
4. Activate continuous compliance verification: [TODO]

## 8. Validation and Testing
- Smoke tests: [TODO]
- Regression tests: [TODO]
- Security tests (scan/config audit): [TODO]
- Acceptance criteria: [TODO]

## 9. Monitoring and Compliance
- Config drift detection: [TODO]
- Reporting (KPIs): [TODO]
- Remediation (auto-fix / ticket): [TODO]

## 10. Exceptions
- Reference: `0040_Exceptions_Risk_Acceptance.md`
- Document temporary deviations: [TODO]

## 11. Appendices
- Parameter list/example values: [TODO]
- Checklist: see `0410_Appendix_Checklists_and_Evidence.md`


## 12. Linux-Specific Areas (Examples)
- Package sources & signatures: [TODO]
- SSH hardening: reference `0320_APP_SSH_Service_Hardening.md`
- sudo/privileged access: [TODO]
- Kernel/sysctl baseline: [TODO]
- SELinux/AppArmor profile: [TODO]


# OS Hardening Baseline: macOS

**Document ID:** 0140  
**Document Type:** Baseline  
**Reference Framework:** CIS Controls v8 (Hardening Program; no benchmark texts)  
**Owner:** [TODO]  
**Version:** 0.1 (Draft)  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Updated:** 2026-01-31  
**Next Review:** [TODO]

---

> **Note:** Template. Replace all `[TODO]` placeholders and remove non-applicable sections.  
> **Important:** This template does not paraphrase CIS original texts. Use it to derive and demonstrably implement **internal baselines/standards**.

## 1. Purpose
[TODO] (e.g., attack surface reduction, uniform baseline, auditability)

## 2. Scope
- Target platform(s): [TODO]
- Versions/editions: [TODO]
- Environments: Prod / Test / Dev / End-user
- Exceptions: only via exception process (`0040_Exceptions_Risk_Acceptance.md`)

## 3. Target State and Principles
- Default-deny where appropriate (e.g., inbound firewall): [TODO]
- Least privilege / role-based admin: [TODO]
- Secure by default (new systems are compliant): [TODO]
- Automation preferred (IaC/config mgmt): [TODO]

## 4. CIS Control Mapping
> Enter the relevant CIS Controls/Safeguards that support this baseline.
| CIS Control | Safeguard/Intent (brief) | Baseline Requirement | Evidence |
|---|---|---|---|
| [TODO] | [TODO] | [TODO] | [TODO] |

## 5. Baseline Requirements (MUST)
> Formulate auditable requirements (not "should"), including responsibility and measurement criteria.
| Area | Requirement (MUST) | Default Value/Target | Responsible | Verification |
|---|---|---|---|---|
| Accounts | [TODO] | [TODO] | [TODO] | [TODO] |
| Network | [TODO] | [TODO] | [TODO] | [TODO] |
| Updates | [TODO] | [TODO] | [TODO] | [TODO] |
| Logging | [TODO] | [TODO] | [TODO] | [TODO] |
| Services | [TODO] | [TODO] | [TODO] | [TODO] |

## 6. Recommendations (SHOULD)
- [TODO]
- [TODO]

## 7. Implementation
### 7.1 Implementation Method
- Manual / GPO / MDM / Ansible / SCCM / Puppet / Chef / IaC: [TODO]
- Rollout strategy (pilot, stages, waves): [TODO]

### 7.2 Step Sequence (High-Level)
1. Define baseline parameters (parameter file): [TODO]
2. Define and test pilot group: [TODO]
3. Rollout with change management: [TODO]
4. Activate continuous compliance verification: [TODO]

## 8. Validation and Testing
- Smoke tests: [TODO]
- Regression tests: [TODO]
- Security tests (scan/config audit): [TODO]
- Acceptance criteria: [TODO]

## 9. Monitoring and Compliance
- Config drift detection: [TODO]
- Reporting (KPIs): [TODO]
- Remediation (auto-fix / ticket): [TODO]

## 10. Exceptions
- Reference: `0040_Exceptions_Risk_Acceptance.md`
- Document temporary deviations: [TODO]

## 11. Appendices
- Parameter list/example values: [TODO]
- Checklist: see `0410_Appendix_Checklists_and_Evidence.md`


## 12. macOS-Specific Areas (Examples)
- MDM profile: [TODO]
- FileVault: [TODO]
- Gatekeeper/XProtect: [TODO]
- Browser/privacy policies: [TODO]


# OS Hardening Baseline: Container Base Images

**Document ID:** 0150  
**Document Type:** Baseline  
**Reference Framework:** CIS Controls v8 (Hardening Program; no benchmark texts)  
**Owner:** [TODO]  
**Version:** 0.1 (Draft)  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Updated:** 2026-01-31  
**Next Review:** [TODO]

---

> **Note:** Template. Replace all `[TODO]` placeholders and remove non-applicable sections.  
> **Important:** This template does not paraphrase CIS original texts. Use it to derive and demonstrably implement **internal baselines/standards**.

## 1. Purpose
Secure default configuration for container base images to reduce attack surface and ensure supply chain security.

## 2. Scope
- Registries/namespaces: [TODO]
- Base images: distroless/alpine/debian/ubi: [TODO]

## 3. Requirements (MUST)
| Area | Requirement | Verification |
|---|---|---|
| Minimality | Only necessary packages/tools included | SBOM/scan |
| Non-root | Default user not root | Runtime policy |
| Updates | Regular rebuilds | Pipeline logs |
| Signing | Image signing/attestations | Registry policy |
| Secrets | No secrets in image | Secrets scan |
| Vulnerabilities | Critical findings = block | Scanner gate |

## 4. CIS Control Mapping
| CIS Control | Intent (brief) | Requirement | Evidence |
|---|---|---|---|
| [TODO] | Inventory/config/vuln mgmt | [TODO] | [TODO] |

## 5. CI/CD Implementation
- Build pipeline: [TODO]
- Scanning (SCA/image): [TODO]
- Promotion (dev->prod): [TODO]

## 6. Exceptions
- Reference: `0040_Exceptions_Risk_Acceptance.md`


# Applications – Overview

**Document ID:** 0200  
**Document Type:** Chapter  
**Reference Framework:** CIS Controls v8 (Hardening Program; no benchmark texts)  
**Owner:** [TODO]  
**Version:** 0.1 (Draft)  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Updated:** 2026-01-31  
**Next Review:** [TODO]

---

> **Note:** Template. Replace all `[TODO]` placeholders and remove non-applicable sections.  
> **Important:** This template does not paraphrase CIS original texts. Use it to derive and demonstrably implement **internal baselines/standards**.

This chapter contains **application-specific hardening standards**.  
Recommendation: First define a **baseline per application class** (web, DB, Kubernetes) and add product-specific standards.

- Webservers/Reverse Proxies: 0210–0240
- Application Runtime: 0250
- Databases: 0260–0290
- Container/Kubernetes: 0300–0310
- Infrastructure Services: 0320–0330


# APP Hardening Baseline: Webserver / Reverse Proxy (generic)

**Document ID:** 0210  
**Document Type:** Standard/Baseline  
**Reference Framework:** CIS Controls v8 (Hardening Program; no benchmark texts)  
**Owner:** [TODO]  
**Version:** 0.1 (Draft)  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Updated:** 2026-01-31  
**Next Review:** [TODO]

---

> **Note:** Template. Replace all `[TODO]` placeholders and remove non-applicable sections.  
> **Important:** This template does not paraphrase CIS original texts. Use it to derive and demonstrably implement **internal baselines/standards**.

## 1. Purpose
[TODO] (e.g., attack surface reduction, uniform baseline, auditability)

## 2. Scope
- Target platform(s): [TODO]
- Versions/editions: [TODO]
- Environments: Prod / Test / Dev / End-user
- Exceptions: only via exception process (`0040_Exceptions_Risk_Acceptance.md`)

## 3. Target State and Principles
- Default-deny where appropriate (e.g., inbound firewall): [TODO]
- Least privilege / role-based admin: [TODO]
- Secure by default (new systems are compliant): [TODO]
- Automation preferred (IaC/config mgmt): [TODO]

## 4. CIS Control Mapping
> Enter the relevant CIS Controls/Safeguards that support this baseline.
| CIS Control | Safeguard/Intent (brief) | Baseline Requirement | Evidence |
|---|---|---|---|
| [TODO] | [TODO] | [TODO] | [TODO] |

## 5. Baseline Requirements (MUST)
> Formulate auditable requirements (not "should"), including responsibility and measurement criteria.
| Area | Requirement (MUST) | Default Value/Target | Responsible | Verification |
|---|---|---|---|---|
| Accounts | [TODO] | [TODO] | [TODO] | [TODO] |
| Network | [TODO] | [TODO] | [TODO] | [TODO] |
| Updates | [TODO] | [TODO] | [TODO] | [TODO] |
| Logging | [TODO] | [TODO] | [TODO] | [TODO] |
| Services | [TODO] | [TODO] | [TODO] | [TODO] |

## 6. Recommendations (SHOULD)
- [TODO]
- [TODO]

## 7. Implementation
### 7.1 Implementation Method
- Manual / GPO / MDM / Ansible / SCCM / Puppet / Chef / IaC: [TODO]
- Rollout strategy (pilot, stages, waves): [TODO]

### 7.2 Step Sequence (High-Level)
1. Define baseline parameters (parameter file): [TODO]
2. Define and test pilot group: [TODO]
3. Rollout with change management: [TODO]
4. Activate continuous compliance verification: [TODO]

## 8. Validation and Testing
- Smoke tests: [TODO]
- Regression tests: [TODO]
- Security tests (scan/config audit): [TODO]
- Acceptance criteria: [TODO]

## 9. Monitoring and Compliance
- Config drift detection: [TODO]
- Reporting (KPIs): [TODO]
- Remediation (auto-fix / ticket): [TODO]

## 10. Exceptions
- Reference: `0040_Exceptions_Risk_Acceptance.md`
- Document temporary deviations: [TODO]

## 11. Appendices
- Parameter list/example values: [TODO]
- Checklist: see `0410_Appendix_Checklists_and_Evidence.md`


## 12. Webserver-Specific Areas (Examples)
- TLS configuration (protocols/ciphers): [TODO]
- Security headers (HSTS, CSP, etc.): [TODO]
- Request limits / rate limiting: [TODO]
- Logging (access/error + correlation IDs): [TODO]
- Admin interfaces not public: [TODO]
- WAF/reverse proxy integration: [TODO]


# APP Hardening Standard: Nginx

**Document ID:** 0220  
**Document Type:** Standard/Baseline  
**Reference Framework:** CIS Controls v8 (Hardening Program; no benchmark texts)  
**Owner:** [TODO]  
**Version:** 0.1 (Draft)  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Updated:** 2026-01-31  
**Next Review:** [TODO]

---

> **Note:** Template. Replace all `[TODO]` placeholders and remove non-applicable sections.  
> **Important:** This template does not paraphrase CIS original texts. Use it to derive and demonstrably implement **internal baselines/standards**.

## 1. Purpose
[TODO] (e.g., attack surface reduction, uniform baseline, auditability)

## 2. Scope
- Target platform(s): [TODO]
- Versions/editions: [TODO]
- Environments: Prod / Test / Dev / End-user
- Exceptions: only via exception process (`0040_Exceptions_Risk_Acceptance.md`)

## 3. Target State and Principles
- Default-deny where appropriate (e.g., inbound firewall): [TODO]
- Least privilege / role-based admin: [TODO]
- Secure by default (new systems are compliant): [TODO]
- Automation preferred (IaC/config mgmt): [TODO]

## 4. CIS Control Mapping
> Enter the relevant CIS Controls/Safeguards that support this baseline.
| CIS Control | Safeguard/Intent (brief) | Baseline Requirement | Evidence |
|---|---|---|---|
| [TODO] | [TODO] | [TODO] | [TODO] |

## 5. Baseline Requirements (MUST)
> Formulate auditable requirements (not "should"), including responsibility and measurement criteria.
| Area | Requirement (MUST) | Default Value/Target | Responsible | Verification |
|---|---|---|---|---|
| Accounts | [TODO] | [TODO] | [TODO] | [TODO] |
| Network | [TODO] | [TODO] | [TODO] | [TODO] |
| Updates | [TODO] | [TODO] | [TODO] | [TODO] |
| Logging | [TODO] | [TODO] | [TODO] | [TODO] |
| Services | [TODO] | [TODO] | [TODO] | [TODO] |

## 6. Recommendations (SHOULD)
- [TODO]
- [TODO]

## 7. Implementation
### 7.1 Implementation Method
- Manual / GPO / MDM / Ansible / SCCM / Puppet / Chef / IaC: [TODO]
- Rollout strategy (pilot, stages, waves): [TODO]

### 7.2 Step Sequence (High-Level)
1. Define baseline parameters (parameter file): [TODO]
2. Define and test pilot group: [TODO]
3. Rollout with change management: [TODO]
4. Activate continuous compliance verification: [TODO]

## 8. Validation and Testing
- Smoke tests: [TODO]
- Regression tests: [TODO]
- Security tests (scan/config audit): [TODO]
- Acceptance criteria: [TODO]

## 9. Monitoring and Compliance
- Config drift detection: [TODO]
- Reporting (KPIs): [TODO]
- Remediation (auto-fix / ticket): [TODO]

## 10. Exceptions
- Reference: `0040_Exceptions_Risk_Acceptance.md`
- Document temporary deviations: [TODO]

## 11. Appendices
- Parameter list/example values: [TODO]
- Checklist: see `0410_Appendix_Checklists_and_Evidence.md`


## 12. Nginx-Specific Requirements (Examples)
- `server_tokens off`: [TODO]
- TLS settings via central include file: [TODO]
- Logging format incl. request ID: [TODO]
- `limit_req` / `limit_conn`: [TODO]
- Access to status/stub internal only: [TODO]


# APP Hardening Standard: Apache HTTP Server

**Document ID:** 0230  
**Document Type:** Standard/Baseline  
**Reference Framework:** CIS Controls v8 (Hardening Program; no benchmark texts)  
**Owner:** [TODO]  
**Version:** 0.1 (Draft)  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Updated:** 2026-01-31  
**Next Review:** [TODO]

---

> **Note:** Template. Replace all `[TODO]` placeholders and remove non-applicable sections.  
> **Important:** This template does not paraphrase CIS original texts. Use it to derive and demonstrably implement **internal baselines/standards**.

## 1. Purpose
[TODO] (e.g., attack surface reduction, uniform baseline, auditability)

## 2. Scope
- Target platform(s): [TODO]
- Versions/editions: [TODO]
- Environments: Prod / Test / Dev / End-user
- Exceptions: only via exception process (`0040_Exceptions_Risk_Acceptance.md`)

## 3. Target State and Principles
- Default-deny where appropriate (e.g., inbound firewall): [TODO]
- Least privilege / role-based admin: [TODO]
- Secure by default (new systems are compliant): [TODO]
- Automation preferred (IaC/config mgmt): [TODO]

## 4. CIS Control Mapping
> Enter the relevant CIS Controls/Safeguards that support this baseline.
| CIS Control | Safeguard/Intent (brief) | Baseline Requirement | Evidence |
|---|---|---|---|
| [TODO] | [TODO] | [TODO] | [TODO] |

## 5. Baseline Requirements (MUST)
> Formulate auditable requirements (not "should"), including responsibility and measurement criteria.
| Area | Requirement (MUST) | Default Value/Target | Responsible | Verification |
|---|---|---|---|---|
| Accounts | [TODO] | [TODO] | [TODO] | [TODO] |
| Network | [TODO] | [TODO] | [TODO] | [TODO] |
| Updates | [TODO] | [TODO] | [TODO] | [TODO] |
| Logging | [TODO] | [TODO] | [TODO] | [TODO] |
| Services | [TODO] | [TODO] | [TODO] | [TODO] |

## 6. Recommendations (SHOULD)
- [TODO]
- [TODO]

## 7. Implementation
### 7.1 Implementation Method
- Manual / GPO / MDM / Ansible / SCCM / Puppet / Chef / IaC: [TODO]
- Rollout strategy (pilot, stages, waves): [TODO]

### 7.2 Step Sequence (High-Level)
1. Define baseline parameters (parameter file): [TODO]
2. Define and test pilot group: [TODO]
3. Rollout with change management: [TODO]
4. Activate continuous compliance verification: [TODO]

## 8. Validation and Testing
- Smoke tests: [TODO]
- Regression tests: [TODO]
- Security tests (scan/config audit): [TODO]
- Acceptance criteria: [TODO]

## 9. Monitoring and Compliance
- Config drift detection: [TODO]
- Reporting (KPIs): [TODO]
- Remediation (auto-fix / ticket): [TODO]

## 10. Exceptions
- Reference: `0040_Exceptions_Risk_Acceptance.md`
- Document temporary deviations: [TODO]

## 11. Appendices
- Parameter list/example values: [TODO]
- Checklist: see `0410_Appendix_Checklists_and_Evidence.md`


## 12. Apache-Specific Requirements (Examples)
- Minimize banner/versions: [TODO]
- TLS configuration centralized: [TODO]
- Disable unnecessary modules: [TODO]
- Directory listing off: [TODO]
- Separate vHosts/least privilege: [TODO]


# APP Hardening Standard: Microsoft IIS

**Document ID:** 0240  
**Document Type:** Standard/Baseline  
**Reference Framework:** CIS Controls v8 (Hardening Program; no benchmark texts)  
**Owner:** [TODO]  
**Version:** 0.1 (Draft)  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Updated:** 2026-01-31  
**Next Review:** [TODO]

---

> **Note:** Template. Replace all `[TODO]` placeholders and remove non-applicable sections.  
> **Important:** This template does not paraphrase CIS original texts. Use it to derive and demonstrably implement **internal baselines/standards**.

## 1. Purpose
[TODO] (e.g., attack surface reduction, uniform baseline, auditability)

## 2. Scope
- Target platform(s): [TODO]
- Versions/editions: [TODO]
- Environments: Prod / Test / Dev / End-user
- Exceptions: only via exception process (`0040_Exceptions_Risk_Acceptance.md`)

## 3. Target State and Principles
- Default-deny where appropriate (e.g., inbound firewall): [TODO]
- Least privilege / role-based admin: [TODO]
- Secure by default (new systems are compliant): [TODO]
- Automation preferred (IaC/config mgmt): [TODO]

## 4. CIS Control Mapping
> Enter the relevant CIS Controls/Safeguards that support this baseline.
| CIS Control | Safeguard/Intent (brief) | Baseline Requirement | Evidence |
|---|---|---|---|
| [TODO] | [TODO] | [TODO] | [TODO] |

## 5. Baseline Requirements (MUST)
> Formulate auditable requirements (not "should"), including responsibility and measurement criteria.
| Area | Requirement (MUST) | Default Value/Target | Responsible | Verification |
|---|---|---|---|---|
| Accounts | [TODO] | [TODO] | [TODO] | [TODO] |
| Network | [TODO] | [TODO] | [TODO] | [TODO] |
| Updates | [TODO] | [TODO] | [TODO] | [TODO] |
| Logging | [TODO] | [TODO] | [TODO] | [TODO] |
| Services | [TODO] | [TODO] | [TODO] | [TODO] |

## 6. Recommendations (SHOULD)
- [TODO]
- [TODO]

## 7. Implementation
### 7.1 Implementation Method
- Manual / GPO / MDM / Ansible / SCCM / Puppet / Chef / IaC: [TODO]
- Rollout strategy (pilot, stages, waves): [TODO]

### 7.2 Step Sequence (High-Level)
1. Define baseline parameters (parameter file): [TODO]
2. Define and test pilot group: [TODO]
3. Rollout with change management: [TODO]
4. Activate continuous compliance verification: [TODO]

## 8. Validation and Testing
- Smoke tests: [TODO]
- Regression tests: [TODO]
- Security tests (scan/config audit): [TODO]
- Acceptance criteria: [TODO]

## 9. Monitoring and Compliance
- Config drift detection: [TODO]
- Reporting (KPIs): [TODO]
- Remediation (auto-fix / ticket): [TODO]

## 10. Exceptions
- Reference: `0040_Exceptions_Risk_Acceptance.md`
- Document temporary deviations: [TODO]

## 11. Appendices
- Parameter list/example values: [TODO]
- Checklist: see `0410_Appendix_Checklists_and_Evidence.md`


## 12. IIS-Specific Requirements (Examples)
- TLS via OS baseline + Schannel policies: [TODO]
- App pool identity least privilege: [TODO]
- Remove unnecessary features/roles: [TODO]
- Request filtering & logging: [TODO]


# APP Hardening Standard: Java Runtime / Tomcat (generic)

**Document ID:** 0250  
**Document Type:** Standard/Baseline  
**Reference Framework:** CIS Controls v8 (Hardening Program; no benchmark texts)  
**Owner:** [TODO]  
**Version:** 0.1 (Draft)  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Updated:** 2026-01-31  
**Next Review:** [TODO]

---

> **Note:** Template. Replace all `[TODO]` placeholders and remove non-applicable sections.  
> **Important:** This template does not paraphrase CIS original texts. Use it to derive and demonstrably implement **internal baselines/standards**.

## 1. Purpose
[TODO] (e.g., attack surface reduction, uniform baseline, auditability)

## 2. Scope
- Target platform(s): [TODO]
- Versions/editions: [TODO]
- Environments: Prod / Test / Dev / End-user
- Exceptions: only via exception process (`0040_Exceptions_Risk_Acceptance.md`)

## 3. Target State and Principles
- Default-deny where appropriate (e.g., inbound firewall): [TODO]
- Least privilege / role-based admin: [TODO]
- Secure by default (new systems are compliant): [TODO]
- Automation preferred (IaC/config mgmt): [TODO]

## 4. CIS Control Mapping
> Enter the relevant CIS Controls/Safeguards that support this baseline.
| CIS Control | Safeguard/Intent (brief) | Baseline Requirement | Evidence |
|---|---|---|---|
| [TODO] | [TODO] | [TODO] | [TODO] |

## 5. Baseline Requirements (MUST)
> Formulate auditable requirements (not "should"), including responsibility and measurement criteria.
| Area | Requirement (MUST) | Default Value/Target | Responsible | Verification |
|---|---|---|---|---|
| Accounts | [TODO] | [TODO] | [TODO] | [TODO] |
| Network | [TODO] | [TODO] | [TODO] | [TODO] |
| Updates | [TODO] | [TODO] | [TODO] | [TODO] |
| Logging | [TODO] | [TODO] | [TODO] | [TODO] |
| Services | [TODO] | [TODO] | [TODO] | [TODO] |

## 6. Recommendations (SHOULD)
- [TODO]
- [TODO]

## 7. Implementation
### 7.1 Implementation Method
- Manual / GPO / MDM / Ansible / SCCM / Puppet / Chef / IaC: [TODO]
- Rollout strategy (pilot, stages, waves): [TODO]

### 7.2 Step Sequence (High-Level)
1. Define baseline parameters (parameter file): [TODO]
2. Define and test pilot group: [TODO]
3. Rollout with change management: [TODO]
4. Activate continuous compliance verification: [TODO]

## 8. Validation and Testing
- Smoke tests: [TODO]
- Regression tests: [TODO]
- Security tests (scan/config audit): [TODO]
- Acceptance criteria: [TODO]

## 9. Monitoring and Compliance
- Config drift detection: [TODO]
- Reporting (KPIs): [TODO]
- Remediation (auto-fix / ticket): [TODO]

## 10. Exceptions
- Reference: `0040_Exceptions_Risk_Acceptance.md`
- Document temporary deviations: [TODO]

## 11. Appendices
- Parameter list/example values: [TODO]
- Checklist: see `0410_Appendix_Checklists_and_Evidence.md`


## 12. Java/Tomcat-Specific Requirements (Examples)
- Protect/disable management interfaces: [TODO]
- Secure defaults (HTTPS only): [TODO]
- JVM security flags (where appropriate): [TODO]
- Patch dependencies/libs regularly: [TODO]
- Secrets via vault/env, not in code: [TODO]


# APP Hardening Baseline: Databases (generic)

**Document ID:** 0260  
**Document Type:** Standard/Baseline  
**Reference Framework:** CIS Controls v8 (Hardening Program; no benchmark texts)  
**Owner:** [TODO]  
**Version:** 0.1 (Draft)  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Updated:** 2026-01-31  
**Next Review:** [TODO]

---

> **Note:** Template. Replace all `[TODO]` placeholders and remove non-applicable sections.  
> **Important:** This template does not paraphrase CIS original texts. Use it to derive and demonstrably implement **internal baselines/standards**.

## 1. Purpose
[TODO] (e.g., attack surface reduction, uniform baseline, auditability)

## 2. Scope
- Target platform(s): [TODO]
- Versions/editions: [TODO]
- Environments: Prod / Test / Dev / End-user
- Exceptions: only via exception process (`0040_Exceptions_Risk_Acceptance.md`)

## 3. Target State and Principles
- Default-deny where appropriate (e.g., inbound firewall): [TODO]
- Least privilege / role-based admin: [TODO]
- Secure by default (new systems are compliant): [TODO]
- Automation preferred (IaC/config mgmt): [TODO]

## 4. CIS Control Mapping
> Enter the relevant CIS Controls/Safeguards that support this baseline.
| CIS Control | Safeguard/Intent (brief) | Baseline Requirement | Evidence |
|---|---|---|---|
| [TODO] | [TODO] | [TODO] | [TODO] |

## 5. Baseline Requirements (MUST)
> Formulate auditable requirements (not "should"), including responsibility and measurement criteria.
| Area | Requirement (MUST) | Default Value/Target | Responsible | Verification |
|---|---|---|---|---|
| Accounts | [TODO] | [TODO] | [TODO] | [TODO] |
| Network | [TODO] | [TODO] | [TODO] | [TODO] |
| Updates | [TODO] | [TODO] | [TODO] | [TODO] |
| Logging | [TODO] | [TODO] | [TODO] | [TODO] |
| Services | [TODO] | [TODO] | [TODO] | [TODO] |

## 6. Recommendations (SHOULD)
- [TODO]
- [TODO]

## 7. Implementation
### 7.1 Implementation Method
- Manual / GPO / MDM / Ansible / SCCM / Puppet / Chef / IaC: [TODO]
- Rollout strategy (pilot, stages, waves): [TODO]

### 7.2 Step Sequence (High-Level)
1. Define baseline parameters (parameter file): [TODO]
2. Define and test pilot group: [TODO]
3. Rollout with change management: [TODO]
4. Activate continuous compliance verification: [TODO]

## 8. Validation and Testing
- Smoke tests: [TODO]
- Regression tests: [TODO]
- Security tests (scan/config audit): [TODO]
- Acceptance criteria: [TODO]

## 9. Monitoring and Compliance
- Config drift detection: [TODO]
- Reporting (KPIs): [TODO]
- Remediation (auto-fix / ticket): [TODO]

## 10. Exceptions
- Reference: `0040_Exceptions_Risk_Acceptance.md`
- Document temporary deviations: [TODO]

## 11. Appendices
- Parameter list/example values: [TODO]
- Checklist: see `0410_Appendix_Checklists_and_Evidence.md`


## 12. DB-Specific Areas (Examples)
- AuthN/AuthZ (roles, least privilege): [TODO]
- Network exposure (app subnets only): [TODO]
- TLS in transit: [TODO]
- At-rest encryption: [TODO]
- Auditing/DB logs: [TODO]
- Backup/restore + test: [TODO]


# APP Hardening Standard: PostgreSQL

**Document ID:** 0270  
**Document Type:** Standard/Baseline  
**Reference Framework:** CIS Controls v8 (Hardening Program; no benchmark texts)  
**Owner:** [TODO]  
**Version:** 0.1 (Draft)  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Updated:** 2026-01-31  
**Next Review:** [TODO]

---

> **Note:** Template. Replace all `[TODO]` placeholders and remove non-applicable sections.  
> **Important:** This template does not paraphrase CIS original texts. Use it to derive and demonstrably implement **internal baselines/standards**.

## 1. Purpose
[TODO] (e.g., attack surface reduction, uniform baseline, auditability)

## 2. Scope
- Target platform(s): [TODO]
- Versions/editions: [TODO]
- Environments: Prod / Test / Dev / End-user
- Exceptions: only via exception process (`0040_Exceptions_Risk_Acceptance.md`)

## 3. Target State and Principles
- Default-deny where appropriate (e.g., inbound firewall): [TODO]
- Least privilege / role-based admin: [TODO]
- Secure by default (new systems are compliant): [TODO]
- Automation preferred (IaC/config mgmt): [TODO]

## 4. CIS Control Mapping
> Enter the relevant CIS Controls/Safeguards that support this baseline.
| CIS Control | Safeguard/Intent (brief) | Baseline Requirement | Evidence |
|---|---|---|---|
| [TODO] | [TODO] | [TODO] | [TODO] |

## 5. Baseline Requirements (MUST)
> Formulate auditable requirements (not "should"), including responsibility and measurement criteria.
| Area | Requirement (MUST) | Default Value/Target | Responsible | Verification |
|---|---|---|---|---|
| Accounts | [TODO] | [TODO] | [TODO] | [TODO] |
| Network | [TODO] | [TODO] | [TODO] | [TODO] |
| Updates | [TODO] | [TODO] | [TODO] | [TODO] |
| Logging | [TODO] | [TODO] | [TODO] | [TODO] |
| Services | [TODO] | [TODO] | [TODO] | [TODO] |

## 6. Recommendations (SHOULD)
- [TODO]
- [TODO]

## 7. Implementation
### 7.1 Implementation Method
- Manual / GPO / MDM / Ansible / SCCM / Puppet / Chef / IaC: [TODO]
- Rollout strategy (pilot, stages, waves): [TODO]

### 7.2 Step Sequence (High-Level)
1. Define baseline parameters (parameter file): [TODO]
2. Define and test pilot group: [TODO]
3. Rollout with change management: [TODO]
4. Activate continuous compliance verification: [TODO]

## 8. Validation and Testing
- Smoke tests: [TODO]
- Regression tests: [TODO]
- Security tests (scan/config audit): [TODO]
- Acceptance criteria: [TODO]

## 9. Monitoring and Compliance
- Config drift detection: [TODO]
- Reporting (KPIs): [TODO]
- Remediation (auto-fix / ticket): [TODO]

## 10. Exceptions
- Reference: `0040_Exceptions_Risk_Acceptance.md`
- Document temporary deviations: [TODO]

## 11. Appendices
- Parameter list/example values: [TODO]
- Checklist: see `0410_Appendix_Checklists_and_Evidence.md`


## 12. PostgreSQL-Specific Requirements (Examples)
- `pg_hba.conf` restrictive: [TODO]
- `log_statement`/`log_line_prefix`: [TODO]
- Roles & schemas: [TODO]
- Extensions whitelist: [TODO]
- Backup & PITR: [TODO]


# APP Hardening Standard: MySQL / MariaDB

**Document ID:** 0280  
**Document Type:** Standard/Baseline  
**Reference Framework:** CIS Controls v8 (Hardening Program; no benchmark texts)  
**Owner:** [TODO]  
**Version:** 0.1 (Draft)  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Updated:** 2026-01-31  
**Next Review:** [TODO]

---

> **Note:** Template. Replace all `[TODO]` placeholders and remove non-applicable sections.  
> **Important:** This template does not paraphrase CIS original texts. Use it to derive and demonstrably implement **internal baselines/standards**.

## 1. Purpose
[TODO] (e.g., attack surface reduction, uniform baseline, auditability)

## 2. Scope
- Target platform(s): [TODO]
- Versions/editions: [TODO]
- Environments: Prod / Test / Dev / End-user
- Exceptions: only via exception process (`0040_Exceptions_Risk_Acceptance.md`)

## 3. Target State and Principles
- Default-deny where appropriate (e.g., inbound firewall): [TODO]
- Least privilege / role-based admin: [TODO]
- Secure by default (new systems are compliant): [TODO]
- Automation preferred (IaC/config mgmt): [TODO]

## 4. CIS Control Mapping
> Enter the relevant CIS Controls/Safeguards that support this baseline.
| CIS Control | Safeguard/Intent (brief) | Baseline Requirement | Evidence |
|---|---|---|---|
| [TODO] | [TODO] | [TODO] | [TODO] |

## 5. Baseline Requirements (MUST)
> Formulate auditable requirements (not "should"), including responsibility and measurement criteria.
| Area | Requirement (MUST) | Default Value/Target | Responsible | Verification |
|---|---|---|---|---|
| Accounts | [TODO] | [TODO] | [TODO] | [TODO] |
| Network | [TODO] | [TODO] | [TODO] | [TODO] |
| Updates | [TODO] | [TODO] | [TODO] | [TODO] |
| Logging | [TODO] | [TODO] | [TODO] | [TODO] |
| Services | [TODO] | [TODO] | [TODO] | [TODO] |

## 6. Recommendations (SHOULD)
- [TODO]
- [TODO]

## 7. Implementation
### 7.1 Implementation Method
- Manual / GPO / MDM / Ansible / SCCM / Puppet / Chef / IaC: [TODO]
- Rollout strategy (pilot, stages, waves): [TODO]

### 7.2 Step Sequence (High-Level)
1. Define baseline parameters (parameter file): [TODO]
2. Define and test pilot group: [TODO]
3. Rollout with change management: [TODO]
4. Activate continuous compliance verification: [TODO]

## 8. Validation and Testing
- Smoke tests: [TODO]
- Regression tests: [TODO]
- Security tests (scan/config audit): [TODO]
- Acceptance criteria: [TODO]

## 9. Monitoring and Compliance
- Config drift detection: [TODO]
- Reporting (KPIs): [TODO]
- Remediation (auto-fix / ticket): [TODO]

## 10. Exceptions
- Reference: `0040_Exceptions_Risk_Acceptance.md`
- Document temporary deviations: [TODO]

## 11. Appendices
- Parameter list/example values: [TODO]
- Checklist: see `0410_Appendix_Checklists_and_Evidence.md`


## 12. MySQL/MariaDB-Specific Requirements (Examples)
- `skip_symbolic_links`: [TODO]
- Network binding/bind-address: [TODO]
- Audit/general log (risk-based): [TODO]
- Users/grants minimal: [TODO]
- Backup: [TODO]


# APP Hardening Standard: Microsoft SQL Server

**Document ID:** 0290  
**Document Type:** Standard/Baseline  
**Reference Framework:** CIS Controls v8 (Hardening Program; no benchmark texts)  
**Owner:** [TODO]  
**Version:** 0.1 (Draft)  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Updated:** 2026-01-31  
**Next Review:** [TODO]

---

> **Note:** Template. Replace all `[TODO]` placeholders and remove non-applicable sections.  
> **Important:** This template does not paraphrase CIS original texts. Use it to derive and demonstrably implement **internal baselines/standards**.

## 1. Purpose
[TODO] (e.g., attack surface reduction, uniform baseline, auditability)

## 2. Scope
- Target platform(s): [TODO]
- Versions/editions: [TODO]
- Environments: Prod / Test / Dev / End-user
- Exceptions: only via exception process (`0040_Exceptions_Risk_Acceptance.md`)

## 3. Target State and Principles
- Default-deny where appropriate (e.g., inbound firewall): [TODO]
- Least privilege / role-based admin: [TODO]
- Secure by default (new systems are compliant): [TODO]
- Automation preferred (IaC/config mgmt): [TODO]

## 4. CIS Control Mapping
> Enter the relevant CIS Controls/Safeguards that support this baseline.
| CIS Control | Safeguard/Intent (brief) | Baseline Requirement | Evidence |
|---|---|---|---|
| [TODO] | [TODO] | [TODO] | [TODO] |

## 5. Baseline Requirements (MUST)
> Formulate auditable requirements (not "should"), including responsibility and measurement criteria.
| Area | Requirement (MUST) | Default Value/Target | Responsible | Verification |
|---|---|---|---|---|
| Accounts | [TODO] | [TODO] | [TODO] | [TODO] |
| Network | [TODO] | [TODO] | [TODO] | [TODO] |
| Updates | [TODO] | [TODO] | [TODO] | [TODO] |
| Logging | [TODO] | [TODO] | [TODO] | [TODO] |
| Services | [TODO] | [TODO] | [TODO] | [TODO] |

## 6. Recommendations (SHOULD)
- [TODO]
- [TODO]

## 7. Implementation
### 7.1 Implementation Method
- Manual / GPO / MDM / Ansible / SCCM / Puppet / Chef / IaC: [TODO]
- Rollout strategy (pilot, stages, waves): [TODO]

### 7.2 Step Sequence (High-Level)
1. Define baseline parameters (parameter file): [TODO]
2. Define and test pilot group: [TODO]
3. Rollout with change management: [TODO]
4. Activate continuous compliance verification: [TODO]

## 8. Validation and Testing
- Smoke tests: [TODO]
- Regression tests: [TODO]
- Security tests (scan/config audit): [TODO]
- Acceptance criteria: [TODO]

## 9. Monitoring and Compliance
- Config drift detection: [TODO]
- Reporting (KPIs): [TODO]
- Remediation (auto-fix / ticket): [TODO]

## 10. Exceptions
- Reference: `0040_Exceptions_Risk_Acceptance.md`
- Document temporary deviations: [TODO]

## 11. Appendices
- Parameter list/example values: [TODO]
- Checklist: see `0410_Appendix_Checklists_and_Evidence.md`


## 12. MSSQL-Specific Requirements (Examples)
- Auth (AD integrated login): [TODO]
- Encryption (TDE/TLS): [TODO]
- Auditing: [TODO]
- Service account least privilege: [TODO]


# APP Hardening Baseline: Kubernetes

**Document ID:** 0300  
**Document Type:** Baseline  
**Reference Framework:** CIS Controls v8 (Hardening Program; no benchmark texts)  
**Owner:** [TODO]  
**Version:** 0.1 (Draft)  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Updated:** 2026-01-31  
**Next Review:** [TODO]

---

> **Note:** Template. Replace all `[TODO]` placeholders and remove non-applicable sections.  
> **Important:** This template does not paraphrase CIS original texts. Use it to derive and demonstrably implement **internal baselines/standards**.

## 1. Purpose
Secure baseline for Kubernetes clusters and workloads (control plane, nodes, RBAC, network, policies).

## 2. Scope
- Clusters/namespaces: [TODO]
- Managed/on-prem: [TODO]

## 3. CIS Control Mapping
| CIS Control | Intent (brief) | Requirement | Evidence |
|---|---|---|---|
| [TODO] | Config/vuln/access | [TODO] | [TODO] |

## 4. Baseline Requirements (MUST) – Cluster
| Area | Requirement | Target | Verification |
|---|---|---|---|
| API Access | AuthN via central IdP, RBAC least privilege | [TODO] | Audit logs |
| Admission | Policy enforcement (e.g., pod security) | [TODO] | Policy reports |
| Secrets | Secrets management, no plaintext secrets | [TODO] | Scanner |
| Network | Network policies default deny (where possible) | [TODO] | Netpol tests |
| Logging | Audit + cluster logs centralized | [TODO] | SIEM evidence |
| Updates | Regular patch/upgrade | [TODO] | Change records |

## 5. Workload Requirements (MUST)
- Non-root, read-only filesystem, minimize capabilities: [TODO]
- Resource limits/requests: [TODO]
- Image scanning/signing gates: [TODO]

## 6. Implementation
- GitOps/Helm policies: [TODO]
- Cluster baseline as code: [TODO]

## 7. Validation
- Policy compliance report: [TODO]
- PenTest/attack simulation: [TODO]

## 8. Exceptions
- Reference: `0040_Exceptions_Risk_Acceptance.md`


# APP Hardening Standard: Docker/Container Runtime

**Document ID:** 0310  
**Document Type:** Standard  
**Reference Framework:** CIS Controls v8 (Hardening Program; no benchmark texts)  
**Owner:** [TODO]  
**Version:** 0.1 (Draft)  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Updated:** 2026-01-31  
**Next Review:** [TODO]

---

> **Note:** Template. Replace all `[TODO]` placeholders and remove non-applicable sections.  
> **Important:** This template does not paraphrase CIS original texts. Use it to derive and demonstrably implement **internal baselines/standards**.

## 1. Purpose
Secure container runtime and host integration (daemon, permissions, namespaces, logging).

## 2. Scope
- Hosts/clusters: [TODO]
- Runtime: Docker/containerd: [TODO]

## 3. Requirements (MUST)
| Area | Requirement | Verification |
|---|---|---|
| Daemon | Access only via RBAC/protected socket | [TODO] |
| Rootless | Rootless runtime where possible | [TODO] |
| Logging | Centralization & retention | [TODO] |
| Images | Only signed/approved images | [TODO] |
| Isolation | seccomp/apparmor/selinux profiles | [TODO] |

## 4. CIS Control Mapping
| CIS Control | Intent (brief) | Requirement | Evidence |
|---|---|---|---|
| [TODO] | Inventory/config | [TODO] | [TODO] |

## 5. Operations
- Updates: [TODO]
- Monitoring: [TODO]


# APP Hardening Standard: SSH Service

**Document ID:** 0320  
**Document Type:** Standard  
**Reference Framework:** CIS Controls v8 (Hardening Program; no benchmark texts)  
**Owner:** [TODO]  
**Version:** 0.1 (Draft)  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Updated:** 2026-01-31  
**Next Review:** [TODO]

---

> **Note:** Template. Replace all `[TODO]` placeholders and remove non-applicable sections.  
> **Important:** This template does not paraphrase CIS original texts. Use it to derive and demonstrably implement **internal baselines/standards**.

## 1. Purpose
Secure configuration of SSH service for administrative access.

## 2. Scope
- Linux/Unix hosts: [TODO]
- Jump/bastion: [TODO]

## 3. Requirements (MUST)
- Root login disabled (or strictly controlled): [TODO]
- Strong authentication (keys + MFA via bastion if applicable): [TODO]
- Restriction to admin networks/jump hosts: [TODO]
- Logging/auditing: [TODO]
- Key lifecycle (rotation/revocation): [TODO]

## 4. Verification
- Config audit (sshd_config): [TODO]
- Auth logs / SIEM use cases: [TODO]

## 5. Exceptions
- Reference: `0040_Exceptions_Risk_Acceptance.md`


# APP Hardening Baseline: Identity (AD/Azure AD/Entra ID)

**Document ID:** 0330  
**Document Type:** Baseline  
**Reference Framework:** CIS Controls v8 (Hardening Program; no benchmark texts)  
**Owner:** [TODO]  
**Version:** 0.1 (Draft)  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Updated:** 2026-01-31  
**Next Review:** [TODO]

---

> **Note:** Template. Replace all `[TODO]` placeholders and remove non-applicable sections.  
> **Important:** This template does not paraphrase CIS original texts. Use it to derive and demonstrably implement **internal baselines/standards**.

## 1. Purpose
Secure identity services as Tier-0 component (AuthN/AuthZ, MFA, conditional access, admin roles).

## 2. Scope
- Tenants/domains: [TODO]
- Admin roles: [TODO]

## 3. Requirements (MUST)
- MFA for admins and sensitive actions: [TODO]
- Break-glass accounts strictly regulated and audited: [TODO]
- Privileged access workflows (PIM/PAM): [TODO]
- Conditional access baseline: [TODO]
- Logging/audit to SIEM: [TODO]
- Regular recertification of privileged roles: [TODO]

## 4. Evidence
- CA policies export: [TODO]
- Role assignments report: [TODO]
- Audit log samples: [TODO]


# Appendix: CIS Control Mapping Template

**Document ID:** 0400  
**Document Type:** Appendix/Template  
**Reference Framework:** CIS Controls v8 (Hardening Program; no benchmark texts)  
**Owner:** [TODO]  
**Version:** 0.1 (Draft)  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Updated:** 2026-01-31  
**Next Review:** [TODO]

---

> **Note:** Template. Replace all `[TODO]` placeholders and remove non-applicable sections.  
> **Important:** This template does not paraphrase CIS original texts. Use it to derive and demonstrably implement **internal baselines/standards**.

## 1. Purpose
Uniform mapping of baseline requirements to CIS Controls/Safeguards and evidence.

## 2. Mapping Table
| Document | Requirement ID | Requirement (brief) | CIS Control | Safeguard/Intent (brief) | Evidence | Owner | Review |
|---|---|---|---|---|---|---|---|
| 0110 | WS-001 | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |


# Appendix: Checklists and Evidence

**Document ID:** 0410  
**Document Type:** Appendix  
**Reference Framework:** CIS Controls v8 (Hardening Program; no benchmark texts)  
**Owner:** [TODO]  
**Version:** 0.1 (Draft)  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Updated:** 2026-01-31  
**Next Review:** [TODO]

---

> **Note:** Template. Replace all `[TODO]` placeholders and remove non-applicable sections.  
> **Important:** This template does not paraphrase CIS original texts. Use it to derive and demonstrably implement **internal baselines/standards**.

## A) Go-Live Checklist for New Baseline
- [ ] Baseline requirements defined and versioned
- [ ] Pilot successful (no critical findings)
- [ ] Rollout plan and communication available
- [ ] Compliance measurement active (dashboards)
- [ ] Exception process established
- [ ] Evidence sources documented

## B) Evidence Examples (typical)
- Config export (GPO/MDM/Ansible run logs)
- Scanner reports (vuln/config)
- SIEM dashboards/alerts
- Change tickets / CAB approvals
- System inventory / tagging

## C) KPI Suggestions
- Baseline compliance per asset group (%)
- Mean time to remediate (config drift)
- Number of active exceptions & age
- Patch compliance (critical systems)
