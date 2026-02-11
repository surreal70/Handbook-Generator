# DORA Metrics Framework Mapping

## Übersicht

Dieses Dokument mappt die Handbook-Templates zu den DORA Metrics und zugehörigen Capabilities.

## DORA Metrics Mapping

### 1. Deployment Frequency

**Definition**: Wie oft eine Organisation erfolgreich Code in Produktion deployed.

**Zugeordnete Templates**:
- 0100_deployment_frequency_overview.md - Übersicht und Definition
- 0110_deployment_frequency_measurement.md - Messmethodik
- 0120_deployment_automation.md - Automatisierung
- 0130_deployment_pipeline.md - Pipeline-Design
- 0140_deployment_frequency_improvement.md - Verbesserungsstrategien

**Unterstützende Capabilities**:
- Continuous Integration
- Continuous Delivery
- Deployment Automation
- Trunk-based Development
- Feature Flags

### 2. Lead Time for Changes

**Definition**: Zeit von Code-Commit bis zur erfolgreichen Ausführung in Produktion.

**Zugeordnete Templates**:
- 0200_lead_time_overview.md - Übersicht und Definition
- 0210_lead_time_measurement.md - Messmethodik
- 0220_value_stream_mapping.md - Value Stream Analyse
- 0230_bottleneck_identification.md - Bottleneck-Analyse
- 0240_lead_time_reduction_strategies.md - Reduktionsstrategien

**Unterstützende Capabilities**:
- Value Stream Mapping
- Bottleneck Identification
- Process Optimization
- Batch Size Reduction
- Parallel Processing

### 3. Mean Time to Restore (MTTR)

**Definition**: Durchschnittliche Zeit zur Wiederherstellung des Service nach einem Incident.

**Zugeordnete Templates**:
- 0300_mttr_overview.md - Übersicht und Definition
- 0310_mttr_measurement.md - Messmethodik
- 0320_incident_detection.md - Incident-Erkennung
- 0330_incident_response_procedures.md - Response-Prozesse
- 0340_recovery_automation.md - Recovery-Automatisierung
- 0350_mttr_improvement.md - Verbesserungsstrategien

**Unterstützende Capabilities**:
- Monitoring und Alerting
- Incident Management
- Recovery Automation
- Self-Healing Systems
- Rollback Automation

### 4. Change Failure Rate

**Definition**: Prozentsatz der Deployments, die zu Service-Degradation führen und Remediation erfordern.

**Zugeordnete Templates**:
- 0400_change_failure_rate_overview.md - Übersicht und Definition
- 0410_cfr_measurement.md - Messmethodik
- 0420_quality_assurance_practices.md - QA-Praktiken
- 0430_testing_strategies.md - Testing-Strategien
- 0440_cicd_practices.md - CI/CD-Praktiken
- 0450_monitoring_observability.md - Monitoring und Observability
- 0460_technical_debt_management.md - Technical Debt Management

**Unterstützende Capabilities**:
- Test Automation
- Code Review
- Quality Gates
- Continuous Testing
- Technical Debt Management

## Framework-Komponenten Mapping

### DORA Framework Übersicht (0010-0099)

| Template | DORA-Komponente | Beschreibung |
|----------|-----------------|--------------|
| 0010 | Framework Overview | Einführung in DORA Metrics |
| 0020 | Software Delivery Performance | Performance-Messung |
| 0030 | Organizational Performance | Business-Outcomes |
| 0040 | Performance Benchmarking | Industrie-Vergleiche |
| 0050 | Maturity Assessment | Reifegrad-Bewertung |

### Technical Capabilities Mapping

| Capability | Templates | DORA Metrics Impact |
|------------|-----------|---------------------|
| Continuous Integration | 0120, 0440 | Deployment Frequency, CFR |
| Continuous Delivery | 0120, 0130, 0440 | Deployment Frequency, Lead Time |
| Test Automation | 0420, 0430 | Change Failure Rate |
| Monitoring | 0320, 0450 | MTTR |
| Deployment Automation | 0120, 0130 | Deployment Frequency, Lead Time |
| Incident Management | 0320, 0330 | MTTR |
| Value Stream Mapping | 0220, 0230 | Lead Time |
| Recovery Automation | 0340 | MTTR |
| Quality Assurance | 0420, 0430 | Change Failure Rate |
| Technical Debt Management | 0460 | Change Failure Rate |

## Cultural Capabilities Mapping

| Capability | Templates | Beschreibung |
|------------|-----------|--------------|
| Westrum Organizational Culture | 0030 | Generative Kultur |
| Learning Culture | 0030, 0050 | Kontinuierliche Verbesserung |
| Collaboration | 0030 | Team-Zusammenarbeit |
| Job Satisfaction | 0030 | Mitarbeiter-Engagement |
| Transformational Leadership | 0030 | Leadership-Praktiken |

## Performance-Level Mapping

| Performance-Level | Deployment Frequency | Lead Time | MTTR | Change Failure Rate |
|-------------------|----------------------|-----------|------|---------------------|
| Elite | On-demand (mehrmals täglich) | < 1 Stunde | < 1 Stunde | 0-15% |
| High | Täglich bis wöchentlich | 1 Tag bis 1 Woche | < 1 Tag | 16-30% |
| Medium | Wöchentlich bis monatlich | 1 Monat bis 6 Monate | 1 Tag bis 1 Woche | 31-45% |
| Low | Monatlich bis halbjährlich | > 6 Monate | > 1 Woche | 46-60% |

## Verbesserungspfade

### Von Low zu Medium
- Fokus: Grundlegende Automatisierung und Prozesse
- Templates: 0120, 0130, 0220, 0320, 0420

### Von Medium zu High
- Fokus: Erweiterte Automatisierung und Optimierung
- Templates: 0140, 0240, 0340, 0430, 0440

### Von High zu Elite
- Fokus: Vollständige Automatisierung und Kultur
- Templates: 0030, 0050, 0340, 0450, 0460

## Referenzen

- DORA State of DevOps Reports: https://dora.dev/
- Accelerate Book: https://itrevolution.com/product/accelerate/
- DORA Quick Check: https://dora.dev/quickcheck/
