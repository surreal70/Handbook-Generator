---
Document-ID: iso-38500-0140
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Leistungsmessung

## Zweck

Dieses Dokument beschreibt die Leistungsmessung im Rahmen der IT-Governance.

## Geltungsbereich

Dieses Dokument gilt für:
- {{ meta.organization }}
- Alle IT-Leistungsmessungen

## Leistungskennzahlen (KPIs)

### Strategische KPIs

| KPI | Ziel | Aktuell | Trend |
|-----|------|---------|-------|
| IT-Strategieumsetzung | >90% | {{ meta.strategy_implementation }}% | {{ meta.strategy_trend }} |
| Business-IT-Alignment | >8/10 | {{ meta.alignment_score }}/10 | {{ meta.alignment_trend }} |
| IT-ROI | >15% | {{ meta.it_roi }}% | {{ meta.roi_trend }} |
| Innovationsrate | >10% | {{ meta.innovation_rate }}% | {{ meta.innovation_trend }} |

### Operative KPIs

| KPI | Ziel | Aktuell | Trend |
|-----|------|---------|-------|
| System-Verfügbarkeit | >99.5% | {{ meta.system_availability }}% | {{ meta.availability_trend }} |
| Incident-Resolution-Time | <4h | {{ meta.incident_resolution }}h | {{ meta.incident_trend }} |
| User-Satisfaction | >85% | {{ meta.user_satisfaction }}% | {{ meta.satisfaction_trend }} |
| Change-Success-Rate | >95% | {{ meta.change_success }}% | {{ meta.change_trend }} |

### Finanz-KPIs

| KPI | Ziel | Aktuell | Trend |
|-----|------|---------|-------|
| IT-Kosten/Umsatz | <5% | {{ meta.it_cost_ratio }}% | {{ meta.cost_trend }} |
| Projekt-Budget-Einhaltung | >90% | {{ meta.budget_compliance }}% | {{ meta.budget_trend }} |
| TCO-Optimierung | -5% p.a. | {{ meta.tco_optimization }}% | {{ meta.tco_trend }} |

## Messmethoden

### Automatisierte Messung

- System-Monitoring-Tools
- Performance-Dashboards
- Log-Analyse
- Automatische Berichte

### Manuelle Messung

- Umfragen
- Interviews
- Audits
- Reviews

## Berichterstattung

### Dashboard

- Echtzeit-Visualisierung
- Drill-Down-Funktionen
- Trend-Analysen
- Vergleiche

### Berichte

- Monatliche Leistungsberichte
- Quartalsweise Management-Berichte
- Jährliche Governance-Berichte

## Dokumentenverweise

- 0100_edm_model.md
- 0130_monitoring_processes.md

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | {{ meta.date }} | {{ meta.author }} | Initiale Erstellung |

