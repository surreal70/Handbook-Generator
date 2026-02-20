# APP Hardening Standard: SSH Service

**Dokument-ID:** CIS-CONTROLS-0320
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
Sichere Konfiguration des SSH-Dienstes für Administrationszugriffe.

## 2. Geltungsbereich
- Linux/Unix Hosts: [TODO]
- Jump/Bastion: [TODO]

## 3. Anforderungen (MUSS)
- Root-Login deaktiviert (oder streng kontrolliert): [TODO]
- Starke Authentisierung (Keys + ggf. MFA via Bastion): [TODO]
- Beschränkung auf Admin-Netze/Jump Hosts: [TODO]
- Logging/Auditing: [TODO]
- Key Lifecycle (Rotation/Revocation): [TODO]

## 4. Verifikation
- Config Audit (sshd_config): [TODO]
- Auth Logs / SIEM Use Cases: [TODO]

## 5. Ausnahmen
- Verweis: `0040_Ausnahmen_Risk_Acceptance.md`

