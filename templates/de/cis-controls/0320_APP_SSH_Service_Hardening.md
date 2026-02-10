# APP Hardening Standard: SSH Service

**Dokument-ID:** 0320  
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

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |
