# Anhang: Checklisten und Evidence

**Dokument-ID:** 0410
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Genehmigt durch:** {{ meta-handbook.approver }}
**Revision:** [TODO]
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Klassifizierung:** {{ meta-handbook.classification }}
**Letzte Aktualisierung:** {{ meta-handbook.modifydate }}
**Template Version:** [TODO]

---

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

