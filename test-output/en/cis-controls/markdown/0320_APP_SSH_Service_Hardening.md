# APP Hardening Standard: SSH Service

**Document-ID:** [FRAMEWORK]-0320
**Organisation:** AdminSend GmbH
**Owner:** [TODO]
**Approved by:** [TODO]
**Revision:** [TODO]
**Author:** Handbook-Generator
**Status:** Draft
**Classification:** Internal
**Last Update:** [TODO]
**Template Version:** [TODO]

---

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

