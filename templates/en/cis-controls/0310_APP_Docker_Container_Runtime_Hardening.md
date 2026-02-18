# APP Hardening Standard: Docker/Container Runtime

**Document-ID:** [FRAMEWORK]-0310
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

