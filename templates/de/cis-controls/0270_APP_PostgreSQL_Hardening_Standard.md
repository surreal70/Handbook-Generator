# APP Hardening Standard: PostgreSQL

**Dokument-ID:** 0270
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Genehmigt durch:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Klassifizierung:** {{ meta-handbook.classification }}
**Letzte Aktualisierung:** {{ meta-handbook.modifydate }}

---

---

> **Hinweis:** Template. Ersetze alle `[TODO]`-Platzhalter und entferne nicht zutreffende Abschnitte.  
> **Wichtig:** Dieses Template paraphrasiert keine CIS-Originaltexte. Nutze es, um **interne Baselines/Standards** abzuleiten und nachweisbar umzusetzen.

## 1. Zweck
[TODO] (z. B. Reduktion Angriffsfläche, einheitliche Baseline, Auditierbarkeit)

## 2. Geltungsbereich
- Zielplattform(en): [TODO]
- Versionen/Editionen: [TODO]
- Umgebungen: Prod / Test / Dev / Enduser
- Ausnahmen: nur über Ausnahmenprozess (`0040_Ausnahmen_Risk_Acceptance.md`)

## 3. Zielbild und Prinzipien
- Default-Deny wo sinnvoll (z. B. eingehende Firewall): [TODO]
- Least Privilege / Role Based Admin: [TODO]
- Secure by Default (neue Systeme sind compliant): [TODO]
- Automatisierung (IaC/Config Mgmt) bevorzugt: [TODO]

## 4. CIS-Control-Bezug (Mapping)
> Trage die relevanten CIS Controls/Safeguards ein, die diese Baseline stützt.
| CIS Control | Safeguard/Intent (kurz) | Baseline-Anforderung | Nachweis/Evidence |
|---|---|---|---|
| [TODO] | [TODO] | [TODO] | [TODO] |

## 5. Baseline-Anforderungen (MUSS)
> Formuliere prüfbare Anforderungen (nicht „sollte“), inkl. Verantwortlichkeit und Messkriterium.
| Bereich | Requirement (MUSS) | Standardwert/Ziel | Verantwortlich | Verifikation |
|---|---|---|---|---|
| Accounts | [TODO] | [TODO] | [TODO] | [TODO] |
| Netzwerk | [TODO] | [TODO] | [TODO] | [TODO] |
| Updates | [TODO] | [TODO] | [TODO] | [TODO] |
| Logging | [TODO] | [TODO] | [TODO] | [TODO] |
| Services | [TODO] | [TODO] | [TODO] | [TODO] |

## 6. Empfehlungen (SOLL)
- [TODO]
- [TODO]

## 7. Implementierung
### 7.1 Umsetzungsmethode
- Manuell / GPO / MDM / Ansible / SCCM / Puppet / Chef / IaC: [TODO]
- Rollout-Strategie (Pilot, Stufen, Wellen): [TODO]

### 7.2 Schrittfolge (High-Level)
1. Baseline-Parameter festlegen (Parameterdatei): [TODO]
2. Pilotgruppe definieren und testen: [TODO]
3. Rollout mit Change-Management: [TODO]
4. Kontinuierliche Compliance-Prüfung aktivieren: [TODO]

## 8. Validierung und Tests
- Smoke Tests: [TODO]
- Regressionstests: [TODO]
- Security Tests (Scan/Config Audit): [TODO]
- Abnahmekriterien: [TODO]

## 9. Monitoring und Compliance
- Config-Drift Detection: [TODO]
- Reporting (KPIs): [TODO]
- Remediation (Auto-Fix / Ticket): [TODO]

## 10. Ausnahmen
- Verweis: `0040_Ausnahmen_Risk_Acceptance.md`
- Temporäre Abweichungen dokumentieren: [TODO]

## 11. Anhänge
- Parameterliste/Beispielwerte: [TODO]
- Checkliste: siehe `0410_Anhang_Checklisten_und_Evidence.md`

## 12. PostgreSQL-spezifische Anforderungen (Beispiele)
- `pg_hba.conf` restriktiv: [TODO]
- `log_statement`/`log_line_prefix`: [TODO]
- Rollen & Schemas: [TODO]
- Extensions Whitelist: [TODO]
- Backup & PITR: [TODO]

