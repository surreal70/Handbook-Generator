# APP Hardening Standard: Apache HTTP Server

**Document-ID:** [FRAMEWORK]-0230
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

