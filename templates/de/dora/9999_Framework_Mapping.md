# DORA Metrics Framework Mapping

**Dokument-ID:** [FRAMEWORK]-9999
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

## Übersicht

Dieses Dokument mappt die Handbook-Templates zu den DORA Metrics und zugehörigen Capabilities.

**Framework-Status**: Vollständige Abdeckung (100% vollständig)
**Letzte Aktualisierung**: 2026-02-13

## DORA Metrics Mapping

### 1. Deployment Frequency

**Definition**: Wie oft eine Organisation erfolgreich Code in Produktion deployed.

**DORA Metric**: **DORA-1** (Deployment Frequency)

**Vorhandene Templates**:
- 0060_deployment_frequency_improvement.md ✓
- 0070_deployment_frequency_measurement.md ✓
- 0100_deployment_frequency_overview.md ✓
- 0110_deployment_frequency_measurement.md ✓
- 0120_deployment_automation.md ✓
- 0130_deployment_pipeline.md ✓

**Unterstützende Capabilities**:
- Continuous Integration
- Continuous Delivery
- Deployment Automation
- Trunk-based Development
- Feature Flags

### 2. Lead Time for Changes

**Definition**: Zeit von Code-Commit bis zur erfolgreichen Ausführung in Produktion.

**DORA Metric**: **DORA-2** (Lead Time for Changes)

**Vorhandene Templates**:
- 0080_lead_time_measurement.md ✓
- 0200_lead_time_overview.md ✓
- 0210_lead_time_measurement.md ✓
- 0220_value_stream_mapping.md ✓
- 0230_bottleneck_identification.md ✓
- 0240_lead_time_reduction_strategies.md ✓

**Unterstützende Capabilities**:
- Value Stream Mapping
- Bottleneck Identification
- Process Optimization
- Batch Size Reduction
- Parallel Processing

### 3. Mean Time to Restore (MTTR)

**Definition**: Durchschnittliche Zeit zur Wiederherstellung des Service nach einem Incident.

**DORA Metric**: **DORA-3** (Mean Time to Restore)

**Vorhandene Templates**:
- 0160_mttr_overview.md ✓
- 0170_mttr_measurement.md ✓
- 0180_incident_detection.md ✓
- 0190_incident_response_procedures.md ✓
- 0300_mttr_overview.md ✓
- 0310_mttr_measurement.md ✓
- 0320_incident_detection.md ✓
- 0330_incident_response_procedures.md ✓
- 0340_recovery_automation.md ✓
- 0350_mttr_improvement.md ✓

**Unterstützende Capabilities**:
- Monitoring und Alerting
- Incident Management
- Recovery Automation
- Self-Healing Systems
- Rollback Automation

### 4. Change Failure Rate

**Definition**: Prozentsatz der Deployments, die zu Service-Degradation führen und Remediation erfordern.

**DORA Metric**: **DORA-4** (Change Failure Rate)

**Vorhandene Templates**:
- 0090_change_failure_rate_overview.md ✓
- 0150_quality_assurance_practices.md ✓
- 0250_testing_strategies.md ✓
- 0260_cicd_practices.md ✓
- 0270_monitoring_observability.md ✓
- 0280_technical_debt_management.md ✓
- 0400_change_failure_rate_overview.md ✓
- 0410_cfr_measurement.md ✓
- 0430_testing_strategies.md ✓
- 0440_cicd_practices.md ✓
- 0450_monitoring_observability.md ✓
- 0460_technical_debt_management.md ✓

**Unterstützende Capabilities**:
- Test Automation
- Code Review
- Quality Gates
- Continuous Testing
- Technical Debt Management

## Framework-Komponenten Mapping

### DORA Framework Übersicht (0010-0099)

| Template | DORA-Komponente | Beschreibung | Status |
|----------|-----------------|--------------|--------|
| 0010 | Framework Overview | Einführung in DORA Metrics | ✓ |
| 0020 | Software Delivery Performance | Performance-Messung | ✓ |
| 0030 | Organizational Performance | Business-Outcomes | ✓ |
| 0040 | Performance Benchmarking | Industrie-Vergleiche | ✓ |
| 0050 | Maturity Assessment | Reifegrad-Bewertung | ✓ |

## Abdeckungsmatrix

| DORA Metric | Vorhandene Templates | Abdeckung |
|-------------|---------------------|----------|
| Deployment Frequency | 6 Templates | 100% |
| Lead Time for Changes | 6 Templates | 100% |
| Mean Time to Restore | 10 Templates | 100% |
| Change Failure Rate | 12 Templates | 100% |
| **Gesamt** | **45 Templates** | **100%** |

## Zusammenfassung vorhandener Templates

1. 0010_dora_framework_overview.md
2. 0020_software_delivery_performance.md
3. 0030_organizational_performance.md
4. 0040_performance_benchmarking.md
5. 0050_maturity_assessment.md
6. 0060_deployment_frequency_improvement.md
7. 0070_deployment_frequency_measurement.md
8. 0080_lead_time_measurement.md
9. 0090_change_failure_rate_overview.md
10. 0100_deployment_frequency_overview.md
11. 0110_deployment_frequency_measurement.md
12. 0120_deployment_automation.md
13. 0130_deployment_pipeline.md
14. 0150_quality_assurance_practices.md
15. 0160_mttr_overview.md
16. 0170_mttr_measurement.md
17. 0180_incident_detection.md
18. 0190_incident_response_procedures.md
19. 0200_lead_time_overview.md
20. 0210_lead_time_measurement.md
21. 0220_value_stream_mapping.md
22. 0230_bottleneck_identification.md
23. 0240_lead_time_reduction_strategies.md
24. 0250_testing_strategies.md
25. 0260_cicd_practices.md
26. 0270_monitoring_observability.md
27. 0280_technical_debt_management.md
28. 0300_mttr_overview.md
29. 0310_mttr_measurement.md
30. 0320_incident_detection.md
31. 0330_incident_response_procedures.md
32. 0340_recovery_automation.md
33. 0350_mttr_improvement.md
34. 0400_change_failure_rate_overview.md
35. 0410_cfr_measurement.md
36. 0430_testing_strategies.md
37. 0440_cicd_practices.md
38. 0450_monitoring_observability.md
39. 0460_technical_debt_management.md
40. 9999_Framework_Mapping.md

## Geplante Templates

Alle geplanten Templates wurden erfolgreich implementiert. Das DORA Framework hat nun 100% Abdeckung erreicht.

## Performance Level Mapping

| Performance Level | Deployment Frequency | Lead Time | MTTR | Change Failure Rate |
|-------------------|----------------------|-----------|------|---------------------|
| Elite | On-demand (mehrmals täglich) | < 1 Stunde | < 1 Stunde | 0-15% |
| High | Täglich bis wöchentlich | 1 Tag bis 1 Woche | < 1 Tag | 16-30% |
| Medium | Wöchentlich bis monatlich | 1 Monat bis 6 Monate | 1 Tag bis 1 Woche | 31-45% |
| Low | Monatlich bis halbjährlich | > 6 Monate | > 1 Woche | 46-60% |

## Verbesserungspfade

### Von Low zu Medium
- Fokus: Basis-Automatisierung und Prozesse
- Vorhandene Templates: 0060, 0070, 0080, 0180, 0150

### Von Medium zu High
- Fokus: Erweiterte Automatisierung und Optimierung
- Vorhandene Templates: 0060, 0250, 0260, 0270

### Von High zu Elite
- Fokus: Vollständige Automatisierung und Kultur
- Vorhandene Templates: 0030, 0050, 0270, 0280

## Referenzen

- DORA State of DevOps Reports: https://dora.dev/
- Accelerate Book: https://itrevolution.com/product/accelerate/
- DORA Quick Check: https://dora.dev/quickcheck/

