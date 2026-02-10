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

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial Creation |
