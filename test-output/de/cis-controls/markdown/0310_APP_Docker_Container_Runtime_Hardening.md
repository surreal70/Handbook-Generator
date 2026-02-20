# APP Hardening Standard: Docker/Container Runtime

**Dokument-ID:** CIS-CONTROLS-0310
**Organisation:** AdminSend GmbH
**Owner:** [TODO]
**Genehmigt durch:** [TODO]
**Revision:** [TODO]
**Author:** Handbook-Generator
**Status:** Draft
**Klassifizierung:** Internal
**Letzte Aktualisierung:** [TODO]
**Template Version:** [TODO]

---

---

> **Hinweis:** Template. Ersetze alle `[TODO]`-Platzhalter und entferne nicht zutreffende Abschnitte.  
> **Wichtig:** Dieses Template paraphrasiert keine CIS-Originaltexte. Nutze es, um **interne Baselines/Standards** abzuleiten und nachweisbar umzusetzen.

## 1. Zweck
Absicherung der Container-Runtime und Host-Integration (Daemon, Permissions, Namespaces, Logging).

## 2. Geltungsbereich
- Hosts/Cluster: [TODO]
- Runtime: Docker/containerd: [TODO]

## 3. Anforderungen (MUSS)
| Bereich | Requirement | Verifikation |
|---|---|---|
| Daemon | Zugriff nur via RBAC/Socket geschützt | [TODO] |
| Rootless | Wo möglich rootless Runtime | [TODO] |
| Logging | Zentralisierung & Retention | [TODO] |
| Images | Nur signierte/approved Images | [TODO] |
| Isolation | seccomp/apparmor/selinux Profile | [TODO] |

## 4. CIS-Control-Bezug (Mapping)
| CIS Control | Intent (kurz) | Requirement | Evidence |
|---|---|---|---|
| [TODO] | Inventory/Config | [TODO] | [TODO] |

## 5. Betrieb
- Updates: [TODO]
- Monitoring: [TODO]

