# CIS Controls – Überblick und Vorgehen

**Dokument-ID:** CIS-CONTROLS-0010
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

