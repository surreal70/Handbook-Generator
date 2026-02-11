# DORA Metrics Framework Mapping

## Overview

This document maps the handbook templates to DORA Metrics and associated capabilities.

## DORA Metrics Mapping

### 1. Deployment Frequency

**Definition**: How often an organization successfully deploys code to production.

**Mapped Templates**:
- 0100_deployment_frequency_overview.md - Overview and definition
- 0110_deployment_frequency_measurement.md - Measurement methodology
- 0120_deployment_automation.md - Automation
- 0130_deployment_pipeline.md - Pipeline design
- 0140_deployment_frequency_improvement.md - Improvement strategies

**Supporting Capabilities**:
- Continuous Integration
- Continuous Delivery
- Deployment Automation
- Trunk-based Development
- Feature Flags

### 2. Lead Time for Changes

**Definition**: Time from code commit to successful execution in production.

**Mapped Templates**:
- 0200_lead_time_overview.md - Overview and definition
- 0210_lead_time_measurement.md - Measurement methodology
- 0220_value_stream_mapping.md - Value stream analysis
- 0230_bottleneck_identification.md - Bottleneck analysis
- 0240_lead_time_reduction_strategies.md - Reduction strategies

**Supporting Capabilities**:
- Value Stream Mapping
- Bottleneck Identification
- Process Optimization
- Batch Size Reduction
- Parallel Processing

### 3. Mean Time to Restore (MTTR)

**Definition**: Average time to restore service after an incident.

**Mapped Templates**:
- 0300_mttr_overview.md - Overview and definition
- 0310_mttr_measurement.md - Measurement methodology
- 0320_incident_detection.md - Incident detection
- 0330_incident_response_procedures.md - Response processes
- 0340_recovery_automation.md - Recovery automation
- 0350_mttr_improvement.md - Improvement strategies

**Supporting Capabilities**:
- Monitoring and Alerting
- Incident Management
- Recovery Automation
- Self-Healing Systems
- Rollback Automation

### 4. Change Failure Rate

**Definition**: Percentage of deployments that result in service degradation and require remediation.

**Mapped Templates**:
- 0400_change_failure_rate_overview.md - Overview and definition
- 0410_cfr_measurement.md - Measurement methodology
- 0420_quality_assurance_practices.md - QA practices
- 0430_testing_strategies.md - Testing strategies
- 0440_cicd_practices.md - CI/CD practices
- 0450_monitoring_observability.md - Monitoring and observability
- 0460_technical_debt_management.md - Technical debt management

**Supporting Capabilities**:
- Test Automation
- Code Review
- Quality Gates
- Continuous Testing
- Technical Debt Management

## Framework Components Mapping

### DORA Framework Overview (0010-0099)

| Template | DORA Component | Description |
|----------|----------------|-------------|
| 0010 | Framework Overview | Introduction to DORA Metrics |
| 0020 | Software Delivery Performance | Performance measurement |
| 0030 | Organizational Performance | Business outcomes |
| 0040 | Performance Benchmarking | Industry comparisons |
| 0050 | Maturity Assessment | Maturity evaluation |

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

| Capability | Templates | Description |
|------------|-----------|-------------|
| Westrum Organizational Culture | 0030 | Generative culture |
| Learning Culture | 0030, 0050 | Continuous improvement |
| Collaboration | 0030 | Team collaboration |
| Job Satisfaction | 0030 | Employee engagement |
| Transformational Leadership | 0030 | Leadership practices |

## Performance Level Mapping

| Performance Level | Deployment Frequency | Lead Time | MTTR | Change Failure Rate |
|-------------------|----------------------|-----------|------|---------------------|
| Elite | On-demand (multiple times daily) | < 1 hour | < 1 hour | 0-15% |
| High | Daily to weekly | 1 day to 1 week | < 1 day | 16-30% |
| Medium | Weekly to monthly | 1 month to 6 months | 1 day to 1 week | 31-45% |
| Low | Monthly to semi-annually | > 6 months | > 1 week | 46-60% |

## Improvement Paths

### From Low to Medium
- Focus: Basic automation and processes
- Templates: 0120, 0130, 0220, 0320, 0420

### From Medium to High
- Focus: Advanced automation and optimization
- Templates: 0140, 0240, 0340, 0430, 0440

### From High to Elite
- Focus: Complete automation and culture
- Templates: 0030, 0050, 0340, 0450, 0460

## References

- DORA State of DevOps Reports: https://dora.dev/
- Accelerate Book: https://itrevolution.com/product/accelerate/
- DORA Quick Check: https://dora.dev/quickcheck/
