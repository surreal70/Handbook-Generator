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

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |
