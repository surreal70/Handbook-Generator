# CIS Controls v8 Hardening Templates Handbuch

**Dokument-Metadaten**

- **Erstellt am:** 2026-02-05
- **Autor:** Andreas Huemmer [andreas.huemmer@adminsend.de]
- **Version:** 0.0.3
- **Typ:** CIS Controls v8 Hardening Handbuch

---



# CIS Controls – Überblick und Vorgehen

**Dokument-ID:** 0010  
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

## 1. Ziel
Beschreibt, wie CIS Controls v8 als Rahmen genutzt werden, um Hardening-Baselines je Plattform/Awendung abzuleiten.

## 2. Begriffe
- Baseline: Minimaler, prüfbarer Konfigurationsstandard pro Plattform.
- Standard: Konkretisierung für eine Anwendung/Komponente.
- Compliance: Erfüllungsgrad (z. B. % Systeme compliant).

## 3. Ableitungslogik (praxisnah)
1. Assetgruppen definieren (Server, Clients, Cloud Workloads, Container, Netzwerkgeräte).
2. Schutzbedarf & Kritikalität einordnen (Tiering).
3. Controls/Safeguards priorisieren (z. B. IG1/IG2/IG3) – organisationsspezifisch.
4. Baselines/Standards definieren und parameterisieren.
5. Automatisiert ausrollen und Drift überwachen.
6. Messen, verbessern, ausnahmenbasiert steuern.

## 4. Output-Artefakte
- OS Baselines: 0110–0150
- Applikationsstandards: 0210+
- Evidence/Reporting: 0410


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


# Hardening-Lifecycle: Baselines, Change und Compliance

**Dokument-ID:** 0030  
**Dokumenttyp:** Prozessbeschreibung  
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

## 1. Lifecycle (End-to-End)
- Definition -> Test -> Freigabe -> Rollout -> Betrieb -> Review

## 2. Change-Management
- Baseline-Änderungen sind Changes: [TODO]
- Notfalländerungen: [TODO]
- Kommunikation/Release Notes: [TODO]

## 3. Compliance-Prüfung
- Messpunkt (Agent/Scanner/Config): [TODO]
- Frequenz: [TODO]
- Schwellenwerte (z. B. <95% = Eskalation): [TODO]

## 4. Drift & Remediation
- Auto-Remediation vs. Ticket: [TODO]
- Ausnahmehandling: [TODO]


# Ausnahmenprozess und Risk Acceptance

**Dokument-ID:** 0040  
**Dokumenttyp:** Prozess/Template  
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

## 1. Ziel
Risikobasierte, zeitlich befristete Ausnahmen von Hardening-Anforderungen ermöglichen, inkl. Nachverfolgung.

## 2. Wann ist eine Ausnahme zulässig?
- Technische Unmöglichkeit (Legacy): [TODO]
- Business-Notwendigkeit mit Kompensationsmaßnahmen: [TODO]

## 3. Prozess
1. Antrag (Ticket/Formular): [TODO]
2. Risikoanalyse (Impact, Exposition, Kompensation): [TODO]
3. Genehmigung (Risikoeigner + Security): [TODO]
4. Laufzeit & Review: [TODO]
5. Abschluss/Remediation: [TODO]

## 4. Ausnahme-Register
| Ausnahme-ID | Asset/Scope | Requirement | Begründung | Kompensationsmaßnahmen | Risiko | Owner | Gültig bis | Status |
|---|---|---|---|---|---|---|---|---|
| EX-001 | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | Offen |


# Test- und Validierungsstrategie

**Dokument-ID:** 0050  
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

## 1. Teststufen
- Unit/Config Test (z. B. linting, policy test): [TODO]
- Integration (Pilotgruppe): [TODO]
- Regression (kritische Apps): [TODO]
- Security Checks (Scanner/Config Audit): [TODO]

## 2. Abnahmekriterien
- Keine kritischen Betriebsstörungen: [TODO]
- Baseline-Compliance nach Rollout >= [TODO]%
- Dokumentation/Evidence aktualisiert: [TODO]

## 3. Rollback
- Rollback-Methode: [TODO]
- Max. Rollback-Zeit: [TODO]


# Betriebssysteme – Übersicht

**Dokument-ID:** 0100  
**Dokumenttyp:** Kapitel  
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

Dieses Kapitel enthält **OS-Hardening-Baselines**.  
Empfehlung: Erstelle je OS-Version/Edition eine **parameterisierte Baseline** und verwalte Ausnahmen zentral.

- Windows Server: 0110
- Windows Client: 0120
- Linux (Generic): 0130
- macOS: 0140
- Container Base Images: 0150


# OS Hardening Baseline: Windows Server

**Dokument-ID:** 0110  
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


## 12. Windows-spezifische Bereiche (Beispiele)
### 12.1 Identity & Admin Tiering
- Tier-Model (z. B. Tier0/Tier1/Tier2): [TODO]
- Separate Admin-Konten: [TODO]
- Local Admin Password Solution / Privileged Access: [TODO]

### 12.2 GPO/MDM Baselines
- Baseline GPOs (Naming/OU): [TODO]
- Security Templates: [TODO]

### 12.3 Services & Rollen
- Standardmäßig deaktiviert: [TODO]
- Remote Management (WinRM/RDP) abgesichert: [TODO]


# OS Hardening Baseline: Windows Client

**Dokument-ID:** 0120  
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


## 12. Client-spezifische Bereiche (Beispiele)
- MDM/Intune/SCCM Baseline: [TODO]
- BitLocker/Device Encryption: [TODO]
- Browser Hardening (Policy): [TODO]
- USB/Device Control: [TODO]


# OS Hardening Baseline: Linux (Generic)

**Dokument-ID:** 0130  
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


## 12. Linux-spezifische Bereiche (Beispiele)
- Paketquellen & Signaturen: [TODO]
- SSH Hardening: Verweis `0320_APP_SSH_Service_Hardening.md`
- sudo/privileged access: [TODO]
- Kernel/sysctl Baseline: [TODO]
- SELinux/AppArmor Profile: [TODO]


# OS Hardening Baseline: macOS

**Dokument-ID:** 0140  
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


## 12. macOS-spezifische Bereiche (Beispiele)
- MDM Profile: [TODO]
- FileVault: [TODO]
- Gatekeeper/XProtect: [TODO]
- Browser/Privacy Policies: [TODO]


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


# Applikationen – Übersicht

**Dokument-ID:** 0200  
**Dokumenttyp:** Kapitel  
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

Dieses Kapitel enthält **applikationsspezifische Hardening-Standards**.  
Empfehlung: Definiere zunächst eine **Baseline pro Anwendungsklasse** (Web, DB, Kubernetes) und ergänze produkt-spezifische Standards.

- Webserver/Reverse Proxies: 0210–0240
- Application Runtime: 0250
- Datenbanken: 0260–0290
- Container/Kubernetes: 0300–0310
- Infrastruktur-Dienste: 0320–0330


# APP Hardening Baseline: Webserver / Reverse Proxy (generisch)

**Dokument-ID:** 0210  
**Dokumenttyp:** Standard/Baseline  
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


## 12. Webserver-spezifische Bereiche (Beispiele)
- TLS-Konfiguration (Protokolle/Cipher): [TODO]
- Security Headers (HSTS, CSP, etc.): [TODO]
- Request Limits / Rate Limiting: [TODO]
- Logging (Access/Error + Correlation IDs): [TODO]
- Admin Interfaces nicht öffentlich: [TODO]
- WAF/Reverse Proxy Einbindung: [TODO]


# APP Hardening Standard: Nginx

**Dokument-ID:** 0220  
**Dokumenttyp:** Standard/Baseline  
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


## 12. Nginx-spezifische Anforderungen (Beispiele)
- `server_tokens off`: [TODO]
- TLS Settings via zentrale Include-Datei: [TODO]
- Logging Format inkl. Request-ID: [TODO]
- `limit_req` / `limit_conn`: [TODO]
- Zugriff auf Status/Stub nur intern: [TODO]


# APP Hardening Standard: Apache HTTP Server

**Dokument-ID:** 0230  
**Dokumenttyp:** Standard/Baseline  
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


## 12. Apache-spezifische Anforderungen (Beispiele)
- Banner/Versionen minimieren: [TODO]
- TLS Konfiguration zentral: [TODO]
- Unnötige Module deaktivieren: [TODO]
- Directory Listing aus: [TODO]
- Separate vHosts/Least Privilege: [TODO]


# APP Hardening Standard: Microsoft IIS

**Dokument-ID:** 0240  
**Dokumenttyp:** Standard/Baseline  
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


## 12. IIS-spezifische Anforderungen (Beispiele)
- TLS über OS Baseline + Schannel Policies: [TODO]
- App Pool Identity least privilege: [TODO]
- Unnötige Features/Rollen entfernen: [TODO]
- Request Filtering & Logging: [TODO]


# APP Hardening Standard: Java Runtime / Tomcat (generisch)

**Dokument-ID:** 0250  
**Dokumenttyp:** Standard/Baseline  
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


## 12. Java/Tomcat-spezifische Anforderungen (Beispiele)
- Management Interfaces schützen/deaktivieren: [TODO]
- Secure Defaults (HTTPS only): [TODO]
- JVM Security Flags (wo sinnvoll): [TODO]
- Dependencies/Libs regelmäßig patchen: [TODO]
- Secrets via Vault/Env, nicht im Code: [TODO]


# APP Hardening Baseline: Datenbanken (generisch)

**Dokument-ID:** 0260  
**Dokumenttyp:** Standard/Baseline  
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


## 12. DB-spezifische Bereiche (Beispiele)
- AuthN/AuthZ (Rollen, Least Privilege): [TODO]
- Network Exposure (nur App-Subnetze): [TODO]
- TLS in Transit: [TODO]
- At-Rest Encryption: [TODO]
- Auditing/DB Logs: [TODO]
- Backup/Restore + Test: [TODO]


# APP Hardening Standard: PostgreSQL

**Dokument-ID:** 0270  
**Dokumenttyp:** Standard/Baseline  
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


# APP Hardening Standard: MySQL / MariaDB

**Dokument-ID:** 0280  
**Dokumenttyp:** Standard/Baseline  
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


## 12. MySQL/MariaDB-spezifische Anforderungen (Beispiele)
- `skip_symbolic_links`: [TODO]
- Netzwerkbindung/Bind-Address: [TODO]
- Audit/General Log (risikobasiert): [TODO]
- Nutzer/Grants minimal: [TODO]
- Backup: [TODO]


# APP Hardening Standard: Microsoft SQL Server

**Dokument-ID:** 0290  
**Dokumenttyp:** Standard/Baseline  
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


## 12. MSSQL-spezifische Anforderungen (Beispiele)
- Auth (AD integrierte Anmeldung): [TODO]
- Verschlüsselung (TDE/TLS): [TODO]
- Auditing: [TODO]
- Service Account least privilege: [TODO]


# APP Hardening Baseline: Kubernetes

**Dokument-ID:** 0300  
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
Sichere Baseline für Kubernetes-Cluster und Workloads (Control Plane, Nodes, RBAC, Netz, Policies).

## 2. Geltungsbereich
- Cluster/Namespaces: [TODO]
- Managed/On-Prem: [TODO]

## 3. CIS-Control-Bezug (Mapping)
| CIS Control | Intent (kurz) | Requirement | Evidence |
|---|---|---|---|
| [TODO] | Config/Vuln/Access | [TODO] | [TODO] |

## 4. Baseline-Anforderungen (MUSS) – Cluster
| Bereich | Requirement | Ziel | Verifikation |
|---|---|---|---|
| API Access | AuthN via zentralem IdP, RBAC least privilege | [TODO] | Audit Logs |
| Admission | Policy Enforcement (z. B. Pod Security) | [TODO] | Policy Reports |
| Secrets | Secrets Management, keine Klartext-Secrets | [TODO] | Scanner |
| Network | Network Policies default deny (wo möglich) | [TODO] | Netpol Tests |
| Logging | Audit + Cluster Logs zentral | [TODO] | SIEM Evidence |
| Updates | Regular Patch/Upgrade | [TODO] | Change Records |

## 5. Workload-Anforderungen (MUSS)
- Non-root, read-only filesystem, capabilities minimieren: [TODO]
- Resource limits/requests: [TODO]
- Image scanning/signing gates: [TODO]

## 6. Implementierung
- GitOps/Helm Policies: [TODO]
- Cluster Baseline as Code: [TODO]

## 7. Validierung
- Policy-Compliance Report: [TODO]
- PenTest/Attack Simulation: [TODO]

## 8. Ausnahmen
- Verweis: `0040_Ausnahmen_Risk_Acceptance.md`


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


# APP Hardening Baseline: Identity (AD/Azure AD/Entra ID)

**Dokument-ID:** 0330  
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
Absicherung von Identitätsdiensten als Tier-0-Komponente (AuthN/AuthZ, MFA, Conditional Access, Admin Roles).

## 2. Geltungsbereich
- Tenants/Domains: [TODO]
- Admin Rollen: [TODO]

## 3. Anforderungen (MUSS)
- MFA für Admins und sensible Aktionen: [TODO]
- Break-Glass Accounts streng reglementiert und auditiert: [TODO]
- Privileged Access Workflows (PIM/PAM): [TODO]
- Conditional Access Baseline: [TODO]
- Logging/Audit an SIEM: [TODO]
- Regelmäßige Rezertifizierung privilegierter Rollen: [TODO]

## 4. Evidence
- CA Policies Export: [TODO]
- Role Assignments Report: [TODO]
- Audit Log Samples: [TODO]


# Anhang: CIS-Control Mapping Template

**Dokument-ID:** 0400  
**Dokumenttyp:** Anhang/Template  
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
Einheitliches Mapping von Baseline-Anforderungen zu CIS Controls/Safeguards sowie Nachweisen.

## 2. Mapping-Tabelle
| Dokument | Requirement-ID | Requirement (kurz) | CIS Control | Safeguard/Intent (kurz) | Evidence | Owner | Review |
|---|---|---|---|---|---|---|---|
| 0110 | WS-001 | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |


# Anhang: Checklisten und Evidence

**Dokument-ID:** 0410  
**Dokumenttyp:** Anhang  
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

## A) Go-Live Checkliste für neue Baseline
- [ ] Baseline-Requirements definiert und versioniert
- [ ] Pilot erfolgreich (keine kritischen Findings)
- [ ] Rollout-Plan und Kommunikation vorhanden
- [ ] Compliance-Messung aktiv (Dashboards)
- [ ] Ausnahmeprozess etabliert
- [ ] Evidence-Quellen dokumentiert

## B) Evidence Beispiele (typisch)
- Config Export (GPO/MDM/Ansible run logs)
- Scanner Reports (Vuln/Config)
- SIEM Dashboards/Alerts
- Change Tickets / CAB Freigaben
- Systeminventar / Tagging

## C) KPI Vorschläge
- Baseline Compliance pro Assetgruppe (%)
- Mean Time to Remediate (Config Drift)
- Anzahl aktiver Ausnahmen & Alter
- Patch Compliance (kritische Systeme)
