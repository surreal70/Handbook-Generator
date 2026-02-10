# OS Hardening Baseline: Container Base Images

**Dokument-ID:** 0150  
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
Sichere Standardkonfiguration für Container-Base-Images zur Reduktion der Angriffsfläche und zur Supply-Chain-Sicherheit.

## 2. Geltungsbereich
- Registries/Namespaces: [TODO]
- Base Images: distroless/alpine/debian/ubi: [TODO]

## 3. Anforderungen (MUSS)
| Bereich | Requirement | Verifikation |
|---|---|---|
| Minimalität | Nur notwendige Pakete/Tools enthalten | SBOM/Scan |
| Non-root | Standard-User nicht root | Runtime Policy |
| Updates | Regelmäßige Rebuilds | Pipeline Logs |
| Signing | Image Signierung/Attestations | Registry Policy |
| Secrets | Keine Secrets im Image | Secrets Scan |
| Vulnerabilities | Kritische Findings = Block | Scanner Gate |

## 4. CIS-Control-Bezug (Mapping)
| CIS Control | Intent (kurz) | Requirement | Evidence |
|---|---|---|---|
| [TODO] | Inventory/Config/Vuln Mgmt | [TODO] | [TODO] |

## 5. CI/CD Umsetzung
- Build-Pipeline: [TODO]
- Scanning (SCA/Image): [TODO]
- Promotion (dev->prod): [TODO]

## 6. Ausnahmen
- Verweis: `0040_Ausnahmen_Risk_Acceptance.md`

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |
