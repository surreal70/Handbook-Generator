# Umsetzungssteuerung, Reporting und KPIs

**Dokument-ID:** 0110
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

<!-- 
TEMPLATE AUTHOR NOTE:
This template defines the governance model, KPIs, and reporting for ISMS implementation.
Reference: BSI Standard 200-1 (ISMS Monitoring and Measurement)
-->

## 1. Steuerungsmodell

### 1.1 Governance-Struktur

**ISMS-Steuerung erfolgt auf drei Ebenen:**

| Ebene | Gremium | Frequenz | Teilnehmer | Fokus |
|---|---|---|---|---|
| **Strategisch** | Management Review | Jährlich | Geschäftsführung, ISB, IT-Leitung | Strategische Ausrichtung, Ressourcen |
| **Taktisch** | ISMS-Team-Meeting | Monatlich | ISB, IT-Leitung, Informationsverbund-Verantwortliche | Maßnahmenplanung, Risiken |
| **Operativ** | Maßnahmen-Status-Update | Wöchentlich | ISB, IT-Leitung, Maßnahmen-Owner | Umsetzungsfortschritt |

### 1.2 Regeltermine

**Wöchentlich - Maßnahmen-Status-Update:**
- **Termin:** [TODO: z.B. Montag 10:00]
- **Dauer:** 30 Minuten
- **Teilnehmer:** ISB, IT-Leitung, aktuelle Maßnahmen-Owner
- **Agenda:** Status laufender Maßnahmen, Blocker, Eskalationen

**Monatlich - ISMS-Team-Meeting:**
- **Termin:** [TODO: z.B. erster Donnerstag im Monat, 14:00]
- **Dauer:** 2 Stunden
- **Teilnehmer:** ISMS-Team (siehe Dokument 0020)
- **Agenda:** 
  - KPI-Review
  - Maßnahmenfortschritt
  - Neue Risiken und Vorfälle
  - Compliance-Updates
  - Entscheidungen und Eskalationen

**Quartalsweise - Management-Review:**
- **Termin:** [TODO: z.B. letzter Freitag im Quartal]
- **Dauer:** 1 Stunde
- **Teilnehmer:** Geschäftsführung, ISB, IT-Leitung
- **Agenda:**
  - ISMS-Performance (KPIs)
  - Maßnahmenumsetzung
  - Risiko-Dashboard
  - Budget und Ressourcen
  - Strategische Entscheidungen

**Jährlich - Management Review (umfassend):**
- **Termin:** [TODO: z.B. Q4]
- **Dauer:** Halber Tag
- **Teilnehmer:** Geschäftsführung, ISB, IT-Leitung, ISMS-Team
- **Agenda:** Siehe Dokument 0140 (Management Review Template)

### 1.3 Reporting-Kanäle

| Bericht | Frequenz | Ersteller | Empfänger | Tool/Format |
|---|---|---|---|---|
| Maßnahmen-Status | Wöchentlich | ISB | IT-Leitung | [TODO: Ticketing-System] |
| ISMS-Status-Report | Monatlich | ISB | Geschäftsführung, ISMS-Team | [TODO: Dashboard/PDF] |
| Sicherheitsvorfälle | Monatlich | ISB | Geschäftsführung | [TODO: Incident-Tool] |
| Risiko-Dashboard | Quartalsweise | ISB | Geschäftsführung | [TODO: GRC-Tool] |
| Management Review | Jährlich | ISB | Geschäftsführung | Präsentation |

## 2. Key Performance Indicators (KPIs)

### 2.1 Maßnahmenumsetzung

| KPI | Definition | Ziel | Quelle | Frequenz | Owner |
|---|---|---|---|---|---|
| **Maßnahmenplan-Erfüllung** | % abgeschlossene Maßnahmen vs. geplant | 100% | Maßnahmenplan (Dokument 0100) | Monatlich | {{ meta-organisation-roles.role_CISO }} |
| **P1-Maßnahmen-Erfüllung** | % abgeschlossene P1-Maßnahmen | 100% in [TODO] Monaten | Maßnahmenplan | Wöchentlich | {{ meta-organisation-roles.role_CISO }} |
| **Maßnahmen-Verzögerung** | Durchschnittliche Verzögerung in Tagen | < 14 Tage | Maßnahmenplan | Monatlich | {{ meta-organisation-roles.role_CISO }} |
| **Budget-Einhaltung** | % genutztes Budget vs. geplant | 100% ± 10% | Finanzcontrolling | Monatlich | {{ meta-organisation-roles.role_CEO }} |

### 2.2 IT-Grundschutz-Compliance

| KPI | Definition | Ziel | Quelle | Frequenz | Owner |
|---|---|---|---|---|---|
| **Erfüllungsgrad IT-Grundschutz** | % erfüllte Anforderungen | > 80% | Basis-Sicherheitscheck (Dokument 0080) | Quartalsweise | {{ meta-organisation-roles.role_CISO }} |
| **Kritische Lücken** | Anzahl nicht erfüllter P1-Anforderungen | 0 | Basis-Sicherheitscheck | Monatlich | {{ meta-organisation-roles.role_CISO }} |
| **Baustein-Abdeckung** | % modellierte Bausteine mit Soll-Ist-Vergleich | 100% | Modellierung (Dokument 0070) | Quartalsweise | {{ meta-organisation-roles.role_CISO }} |

### 2.3 Risikomanagement

| KPI | Definition | Ziel | Quelle | Frequenz | Owner |
|---|---|---|---|---|---|
| **Risiko-Exposition** | Anzahl "Sehr hoch"-Risiken | 0 | Risikoregister (Dokument 0090) | Monatlich | {{ meta-organisation-roles.role_CISO }} |
| **Risikoreduktion** | % reduzierte Risiken vs. identifiziert | > 80% | Risikoregister | Quartalsweise | {{ meta-organisation-roles.role_CISO }} |
| **Risikoakzeptanz-Quote** | % akzeptierte Risiken (ohne Maßnahmen) | < 10% | Risikoregister | Quartalsweise | {{ meta-organisation-roles.role_CISO }} |

### 2.4 Patch- und Vulnerability Management

| KPI | Definition | Ziel | Quelle | Frequenz | Owner |
|---|---|---|---|---|---|
| **Patch-Compliance** | % Systeme mit aktuellen Patches | > 95% | Patch-Management-Tool | Monatlich | {{ meta-organisation-roles.role_CIO }} |
| **Kritische Patches (SLA)** | % kritische Patches innerhalb SLA (7 Tage) | 100% | Patch-Management-Tool | Wöchentlich | {{ meta-organisation-roles.role_CIO }} |
| **Vulnerability-Remediation** | Durchschnittliche Zeit bis Behebung (Tage) | < 30 Tage (Hoch), < 90 Tage (Mittel) | Vulnerability Scanner | Monatlich | {{ meta-organisation-roles.role_CIO }} |
| **Offene Schwachstellen** | Anzahl offener Schwachstellen (Kritisch/Hoch) | < 10 | Vulnerability Scanner | Wöchentlich | {{ meta-organisation-roles.role_CIO }} |

### 2.5 Backup und Recovery

| KPI | Definition | Ziel | Quelle | Frequenz | Owner |
|---|---|---|---|---|---|
| **Backup-Erfolgsrate** | % erfolgreiche Backups | > 99% | Backup-System | Täglich | {{ meta-organisation-roles.role_CIO }} |
| **Backup-Testquote** | % erfolgreiche Restore-Tests | 100% | Test-Protokolle | Quartalsweise | {{ meta-organisation-roles.role_CIO }} |
| **Recovery Time Actual (RTA)** | Tatsächliche Wiederherstellungszeit | < RTO | Test-Protokolle | Quartalsweise | {{ meta-organisation-roles.role_CIO }} |

### 2.6 Incident Management

| KPI | Definition | Ziel | Quelle | Frequenz | Owner |
|---|---|---|---|---|---|
| **Sicherheitsvorfälle** | Anzahl Sicherheitsvorfälle | Trend abnehmend | Incident-Management-System | Monatlich | {{ meta-organisation-roles.role_CISO }} |
| **Mean Time to Detect (MTTD)** | Durchschnittliche Erkennungszeit | < 24 Stunden | SIEM | Monatlich | {{ meta-organisation-roles.role_CIO }} |
| **Mean Time to Respond (MTTR)** | Durchschnittliche Reaktionszeit | < 4 Stunden (Kritisch) | Incident-Management-System | Monatlich | {{ meta-organisation-roles.role_CISO }} |
| **Incident-Closure-Rate** | % geschlossene Incidents innerhalb SLA | > 95% | Incident-Management-System | Monatlich | {{ meta-organisation-roles.role_CISO }} |

### 2.7 Awareness und Schulung

| KPI | Definition | Ziel | Quelle | Frequenz | Owner |
|---|---|---|---|---|---|
| **Schulungsquote** | % Mitarbeitende mit Awareness-Schulung | 100% | HR-System | Quartalsweise | {{ meta-organisation-roles.role_CISO }} |
| **Phishing-Test-Erfolgsrate** | % Mitarbeitende, die Phishing-Test bestehen | > 90% | Phishing-Simulation | Quartalsweise | {{ meta-organisation-roles.role_CISO }} |
| **Security-Champion-Quote** | Anzahl Security Champions pro Abteilung | Min. 1 pro Abteilung | ISMS-Team | Jährlich | {{ meta-organisation-roles.role_CISO }} |

### 2.8 Access Management

| KPI | Definition | Ziel | Quelle | Frequenz | Owner |
|---|---|---|---|---|---|
| **Privileged Account Compliance** | % privilegierte Accounts mit MFA | 100% | IAM-System | Monatlich | {{ meta-organisation-roles.role_CIO }} |
| **Access Review Compliance** | % durchgeführte Zugriffsrezertifizierungen | 100% | IAM-System | Quartalsweise | {{ meta-organisation-roles.role_CIO }} |
| **Orphaned Accounts** | Anzahl verwaister Accounts | 0 | IAM-System | Monatlich | {{ meta-organisation-roles.role_CIO }} |

## 3. KPI-Dashboard

### 3.1 Ampel-Status

| KPI-Kategorie | Aktueller Wert | Ziel | Status | Trend |
|---|---|---|---|---|
| Maßnahmenumsetzung | [TODO: %] | 100% | 🟢/🟡/🔴 | ↗/→/↘ |
| IT-Grundschutz-Compliance | [TODO: %] | > 80% | 🟢/🟡/🔴 | ↗/→/↘ |
| Risikomanagement | [TODO] | 0 "Sehr hoch" | 🟢/🟡/🔴 | ↗/→/↘ |
| Patch-Compliance | [TODO: %] | > 95% | 🟢/🟡/🔴 | ↗/→/↘ |
| Backup-Erfolgsrate | [TODO: %] | > 99% | 🟢/🟡/🔴 | ↗/→/↘ |
| Sicherheitsvorfälle | [TODO] | Trend ↘ | 🟢/🟡/🔴 | ↗/→/↘ |
| Awareness-Schulung | [TODO: %] | 100% | 🟢/🟡/🔴 | ↗/→/↘ |

**Ampel-Logik:**
- 🟢 **Grün:** Ziel erreicht oder übertroffen
- 🟡 **Gelb:** Ziel nicht erreicht, aber akzeptabel (< 10% Abweichung)
- 🔴 **Rot:** Ziel deutlich verfehlt (> 10% Abweichung), Eskalation erforderlich

### 3.2 Trend-Analyse

[TODO: Diagramme und Trend-Visualisierungen einfügen]

## 4. Eskalationsregeln

### 4.1 Eskalationsstufen

| Stufe | Trigger | Eskalation an | Reaktionszeit | Maßnahmen |
|---|---|---|---|---|
| **Stufe 1** | KPI 🟡 für 1 Monat | IT-Leitung | 1 Woche | Ursachenanalyse, Korrekturmaßnahmen |
| **Stufe 2** | KPI 🔴 oder 🟡 für 2 Monate | ISB | 3 Tage | Eskalationsmeeting, Ressourcen prüfen |
| **Stufe 3** | KPI 🔴 für 1 Monat | Geschäftsführung | Sofort | Management-Entscheidung, Ressourcen freigeben |

### 4.2 Eskalationsprozess

1. **Identifikation:** KPI-Abweichung wird erkannt
2. **Analyse:** Ursachenanalyse durch Owner
3. **Eskalation:** Eskalation gemäß Stufe
4. **Maßnahmen:** Korrekturmaßnahmen definieren und umsetzen
5. **Monitoring:** Engmaschiges Monitoring bis Zielerreichung
6. **Lessons Learned:** Dokumentation und Prozessverbesserung

## 5. Reporting-Templates

### 5.1 Monatlicher ISMS-Status-Report

**Berichtsstruktur:**
1. **Executive Summary:** Gesamtstatus (1 Seite)
2. **KPI-Dashboard:** Ampel-Status und Trends
3. **Maßnahmenfortschritt:** Top 10 Maßnahmen
4. **Sicherheitsvorfälle:** Zusammenfassung
5. **Risiken:** Top 5 Risiken
6. **Eskalationen:** Offene Eskalationen
7. **Nächste Schritte:** Geplante Aktivitäten

### 5.2 Quartalsweises Risiko-Dashboard

**Berichtsstruktur:**
1. **Risiko-Heatmap:** Visualisierung aller Risiken
2. **Top 10 Risiken:** Detailbeschreibung
3. **Risikoreduktion:** Fortschritt seit letztem Quartal
4. **Neue Risiken:** Identifizierte neue Risiken
5. **Risikoakzeptanz:** Akzeptierte Risiken mit Begründung

### 5.3 Jährliches Management Review

**Berichtsstruktur:** Siehe Dokument 0140 (Management Review Template)

## 6. Continuous Improvement

### 6.1 Verbesserungsprozess

**PDCA-Zyklus:**
1. **Plan:** Ziele und KPIs definieren
2. **Do:** Maßnahmen umsetzen
3. **Check:** KPIs messen und bewerten
4. **Act:** Verbesserungsmaßnahmen ableiten

### 6.2 Lessons Learned

Nach jedem größeren Vorfall oder Projekt:
1. **Retrospektive:** Was lief gut? Was nicht?
2. **Root Cause Analysis:** Ursachen identifizieren
3. **Verbesserungsmaßnahmen:** Konkrete Maßnahmen definieren
4. **Dokumentation:** Lessons Learned dokumentieren
5. **Kommunikation:** Erkenntnisse teilen

## 7. Tools und Systeme

| Tool/System | Zweck | Owner | Status |
|---|---|---|---|
| [TODO: GRC-Tool] | Risikomanagement, Compliance | {{ meta-organisation-roles.role_CISO }} | [TODO] |
| [TODO: Ticketing-System] | Maßnahmentracking | {{ meta-organisation-roles.role_CIO }} | [TODO] |
| [TODO: SIEM] | Security Monitoring | {{ meta-organisation-roles.role_CIO }} | [TODO] |
| [TODO: Vulnerability Scanner] | Schwachstellen-Management | {{ meta-organisation-roles.role_CIO }} | [TODO] |
| [TODO: Dashboard-Tool] | KPI-Visualisierung | {{ meta-organisation-roles.role_CISO }} | [TODO] |

## 8. Freigabe

| Rolle | Name | Datum | Freigabe |
|---|---|---|---|
| ISB | {{ meta-organisation-roles.role_CISO }} | {{ meta-handbook.modifydate }} | {{ meta-handbook.status }} |
| IT-Leitung | {{ meta-organisation-roles.role_CIO }} | {{ meta-handbook.modifydate }} | {{ meta-handbook.status }} |
| Geschäftsführung | {{ meta-organisation-roles.role_CEO }} | {{ meta-handbook.modifydate }} | {{ meta-handbook.status }} |

**Referenzen:**
- BSI Standard 200-1: Managementsysteme für Informationssicherheit (ISMS)
- BSI Standard 200-2: IT-Grundschutz-Methodik

<!-- End of template -->