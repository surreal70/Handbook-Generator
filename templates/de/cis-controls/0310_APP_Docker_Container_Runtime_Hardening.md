# APP Hardening Standard: Docker/Container Runtime

**Dokument-ID:** 0310  
**Dokumenttyp:** Standard  
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

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |
