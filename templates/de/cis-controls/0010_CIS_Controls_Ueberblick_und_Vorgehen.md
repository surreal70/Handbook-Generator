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
