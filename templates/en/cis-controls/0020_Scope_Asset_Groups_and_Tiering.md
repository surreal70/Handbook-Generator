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

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial Creation |
