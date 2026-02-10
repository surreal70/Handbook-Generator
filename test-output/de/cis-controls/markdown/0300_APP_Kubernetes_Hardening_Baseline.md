# APP Hardening Baseline: Kubernetes

**Dokument-ID:** 0300  
**Dokumenttyp:** Baseline  
**Referenzrahmen:** CIS Controls v8 (Hardening-Programm; keine Benchmarks-Texte)  
**Owner:** [TODO]  
**Version:** 0.1 (Entwurf)  
**Status:** Entwurf / In Review / Freigegeben  
**Klassifizierung:** Intern / Vertraulich / Streng vertraulich  
**Letzte Aktualisierung:** 2026-01-31  
**Nächster Review:** [TODO]

---

> **Hinweis:** Template. Ersetze alle `[TODO]`-Platzhalter und entferne nicht zutreffende Abschnitte.  
> **Wichtig:** Dieses Template paraphrasiert keine CIS-Originaltexte. Nutze es, um **interne Baselines/Standards** abzuleiten und nachweisbar umzusetzen.

## 1. Zweck
Sichere Baseline für Kubernetes-Cluster und Workloads (Control Plane, Nodes, RBAC, Netz, Policies).

## 2. Geltungsbereich
- Cluster/Namespaces: [TODO]
- Managed/On-Prem: [TODO]

## 3. CIS-Control-Bezug (Mapping)
| CIS Control | Intent (kurz) | Requirement | Evidence |
|---|---|---|---|
| [TODO] | Config/Vuln/Access | [TODO] | [TODO] |

## 4. Baseline-Anforderungen (MUSS) – Cluster
| Bereich | Requirement | Ziel | Verifikation |
|---|---|---|---|
| API Access | AuthN via zentralem IdP, RBAC least privilege | [TODO] | Audit Logs |
| Admission | Policy Enforcement (z. B. Pod Security) | [TODO] | Policy Reports |
| Secrets | Secrets Management, keine Klartext-Secrets | [TODO] | Scanner |
| Network | Network Policies default deny (wo möglich) | [TODO] | Netpol Tests |
| Logging | Audit + Cluster Logs zentral | [TODO] | SIEM Evidence |
| Updates | Regular Patch/Upgrade | [TODO] | Change Records |

## 5. Workload-Anforderungen (MUSS)
- Non-root, read-only filesystem, capabilities minimieren: [TODO]
- Resource limits/requests: [TODO]
- Image scanning/signing gates: [TODO]

## 6. Implementierung
- GitOps/Helm Policies: [TODO]
- Cluster Baseline as Code: [TODO]

## 7. Validierung
- Policy-Compliance Report: [TODO]
- PenTest/Attack Simulation: [TODO]

## 8. Ausnahmen
- Verweis: `0040_Ausnahmen_Risk_Acceptance.md`
