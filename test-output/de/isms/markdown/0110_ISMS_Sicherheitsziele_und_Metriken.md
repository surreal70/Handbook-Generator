# Informationssicherheitsziele und Metriken

**Dokument-ID:** 0110
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



## 1. Informationssicherheitsziele

### 1.1 Strategische Ziele

Die **AdminSend GmbH** definiert folgende strategische Informationssicherheitsziele:

| Ziel-ID | Ziel | Beschreibung | KPI/Metrik | Zielwert | Messmethode | Owner | Frequenz | Status |
|---------|------|--------------|------------|----------|-------------|-------|----------|--------|
| **Z-001** | Compliance sicherstellen | Einhaltung aller gesetzlichen und vertraglichen Anforderungen | Anzahl Compliance-Verstöße | 0 | Audit-Berichte, Incident Reports | [TODO] | Quartalsweise | Aktiv |
| **Z-002** | Risiken minimieren | Reduzierung hoher und sehr hoher Risiken | Anzahl Risiken mit Score ≥ 13 | < 5 | Risikoregister | [TODO] | Quartalsweise | Aktiv |
| **Z-003** | Verfügbarkeit gewährleisten | Sicherstellung der Verfügbarkeit kritischer Systeme | Uptime kritischer Systeme | ≥ 99,5% | Monitoring-System | [TODO] | Monatlich | Aktiv |
| **Z-004** | Incidents reduzieren | Reduzierung der Anzahl Sicherheitsvorfälle | Anzahl Security Incidents | < 10 pro Quartal | Incident Management System | [TODO] | Quartalsweise | Aktiv |
| **Z-005** | Awareness erhöhen | Steigerung des Sicherheitsbewusstseins | Schulungsteilnahme-Quote | 100% | LMS, Schulungsnachweise | [TODO] | Jährlich | Aktiv |
| **Z-006** | Patch-Compliance | Zeitnahe Installation kritischer Patches | Durchschnittliche Zeit zur Patch-Installation (kritisch) | < 7 Tage | Vulnerability Management System | IT-Betrieb | Monatlich | Aktiv |

[TODO: Weitere organisationsspezifische Ziele hinzufügen]

### 1.2 Operative Ziele

| Ziel-ID | Ziel | KPI/Metrik | Zielwert | Owner | Frequenz |
|---------|------|------------|----------|-------|----------|
| **Z-010** | MFA-Rollout abschließen | MFA-Aktivierungsrate | 100% | IT-Betrieb | Monatlich |
| **Z-011** | Vulnerability Management | Durchschnittliche Zeit zur Behebung hoher Schwachstellen | < 30 Tage | IT-Betrieb | Monatlich |
| **Z-012** | Backup-Tests | Erfolgsrate Restore-Tests | 100% | IT-Betrieb | Quartalsweise |
| **Z-013** | Phishing-Resilienz | Phishing-Klickrate bei Simulationen | < 5% | [TODO] | Quartalsweise |

## 2. Key Performance Indicators (KPIs)

### 2.1 Sicherheits-KPIs

**Risikomanagement:**
- Anzahl identifizierter Risiken (nach Stufe)
- Anzahl behandelter Risiken pro Quartal
- Durchschnittliche Risikobehebungszeit
- Anzahl akzeptierter Risiken

**Incident Management:**
- Anzahl Security Incidents (nach Schweregrad)
- Mean Time to Detect (MTTD)
- Mean Time to Respond (MTTR)
- Mean Time to Recover (MTTR)

**Vulnerability Management:**
- Anzahl offener Schwachstellen (nach CVSS-Score)
- Durchschnittliche Zeit zur Patch-Installation
- Patch-Compliance-Rate

**Access Management:**
- Anzahl privilegierter Accounts
- MFA-Aktivierungsrate
- Rezertifizierungsrate
- Anzahl Zugriffsverletzungen

**Awareness und Training:**
- Schulungsteilnahme-Quote
- Phishing-Simulation-Ergebnisse
- Anzahl gemeldeter Sicherheitsvorfälle durch Mitarbeiter

### 2.2 Compliance-KPIs

- Anzahl Audit-Findings (nach Schweregrad)
- Durchschnittliche Zeit zur Behebung von Findings
- Compliance-Rate mit Policies
- Anzahl Compliance-Verstöße

### 2.3 Operational-KPIs

- Uptime kritischer Systeme
- Backup-Erfolgsrate
- Restore-Test-Erfolgsrate
- Anzahl Change-Requests mit Sicherheitsreview

## 3. Messmethoden und Datenquellen

### 3.1 Datenquellen

| KPI | Datenquelle | Verantwortlich | Automatisierung |
|-----|-------------|----------------|-----------------|
| Anzahl Incidents | Incident Management System | Security Team | Ja |
| Risikoscores | Risikoregister | ISMS Manager | Teilweise |
| Schwachstellen | Vulnerability Scanner | IT-Betrieb | Ja |
| Uptime | Monitoring-System | IT-Betrieb | Ja |
| Schulungsteilnahme | LMS | HR / CISO | Ja |
| Patch-Compliance | Patch Management System | IT-Betrieb | Ja |

### 3.2 Reporting-Dashboards

**Monatliches Dashboard:**
- Incident-Statistiken
- Vulnerability-Status
- Patch-Compliance
- Uptime-Statistiken

**Quartalsweises Dashboard:**
- Risiko-Übersicht
- Audit-Findings-Status
- Schulungs-Statistiken
- Trend-Analysen

**Jährliches Dashboard:**
- Zielerreichung
- Jahresvergleich
- Strategische Empfehlungen

## 4. Maßnahmen zur Zielerreichung

### 4.1 Verknüpfung zum Risikobehandlungsplan

Jedes Ziel ist mit Maßnahmen im Risikobehandlungsplan verknüpft:
- Siehe `0090_ISMS_Risikobehandlungsplan_RTP_Template.md`

**Beispiel:**
- **Ziel Z-002:** Risiken minimieren
- **Maßnahmen:** M-001 (Redundanter Switch), M-002 (Immutable Backups), M-003 (MFA-Rollout)

### 4.2 Kontinuierliche Verbesserung

**Verbesserungszyklus:**
1. Ziele definieren
2. Maßnahmen planen
3. Maßnahmen umsetzen
4. KPIs messen
5. Ergebnisse analysieren
6. Verbesserungen identifizieren
7. Ziele anpassen

## 5. Review und Anpassung

### 5.1 Regelmäßiger Review

**Quartalsweise:**
- Review der KPI-Werte
- Analyse von Abweichungen
- Anpassung von Maßnahmen

**Jährlich:**
- Vollständiger Review aller Ziele
- Anpassung der Zielwerte
- Definition neuer Ziele
- Im Rahmen des Management Reviews

### 5.2 Trigger für außerplanmäßigen Review

- Wesentliche Änderungen im ISMS-Scope
- Neue Compliance-Anforderungen
- Major Security Incidents
- Audit-Findings

## 6. Referenzen

### Interne Dokumente
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS Policy
- `0080_ISMS_Risikoregister_Template.md` - Risk Register
- `0090_ISMS_Risikobehandlungsplan_RTP_Template.md` - Risk Treatment Plan
- `0140_ISMS_Management_Review_Template.md` - Management Review

### Externe Standards
- **ISO/IEC 27001:2022** - Clause 6.2: Information security objectives
- **ISO/IEC 27001:2022** - Clause 9.1: Monitoring, measurement, analysis and evaluation

**Genehmigt durch:**  
[TODO], CISO  
{{ meta-handbook.management_ceo }}, Geschäftsführung  
Datum: [TODO]

**Nächster Review:** [TODO]

