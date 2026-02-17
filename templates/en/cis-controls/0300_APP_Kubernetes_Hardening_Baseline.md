# APP Hardening Baseline: Kubernetes

**Document-ID:** [FRAMEWORK]-0300
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

