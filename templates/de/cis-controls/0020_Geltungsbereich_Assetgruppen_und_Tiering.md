# Geltungsbereich, Assetgruppen und Tiering

**Dokument-ID:** 0020  
**Dokumenttyp:** Grundlagendokument  
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

## 1. Geltungsbereich
- Organisation/Standorte/Cloud-Accounts: [TODO]
- In Scope Assettypen: [TODO]

## 2. Assetgruppen (Beispiele)
| Gruppe | Beispiele | Tooling/Quelle |
|---|---|---|
| Server | Windows/Linux | CMDB/Cloud Inventory |
| Clients | Windows/macOS | MDM |
| Container | Base Images / Runtimes | Registry/Scanner |
| Netzwerk | Firewalls/Switches | NMS |

## 3. Tiering / Kritikalität
> Ordne Baselines nach Tiers (z. B. Tier 0/1/2) oder Schutzbedarf.
| Tier | Beschreibung | Mindestanforderungen |
|---|---|---|
| T0 | Identitäts-/Security-Kern (IAM, PKI, SIEM) | strengste Baseline |
| T1 | Produktionskritisch | hohe Baseline |
| T2 | Standard | Baseline |
| T3 | Dev/Test | ggf. reduzierte Baseline (risikobasiert) |

## 4. Verantwortlichkeiten
- Asset Owner: [TODO]
- Plattform-Team: [TODO]
- Security/ISMS: [TODO]
