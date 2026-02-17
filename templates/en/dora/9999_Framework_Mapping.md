# DORA Metrics Framework Mapping

**Document-ID:** [FRAMEWORK]-9999
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Approved by:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Classification:** {{ meta-handbook.classification }}
**Last Update:** {{ meta-handbook.modifydate }}

---

---

## Overview

This document maps the handbook templates to DORA Metrics and associated capabilities.

**Framework Status**: Complete Coverage (100% complete)
**Last Updated**: 2026-02-13

## DORA Metrics Mapping

### 1. Deployment Frequency

**Definition**: How often an organization successfully deploys code to production.

**DORA Metric**: **DORA-1** (Deployment Frequency)

**Existing Templates**:
- 0060_deployment_frequency_improvement.md ✓
- 0070_deployment_frequency_measurement.md ✓
- 0100_deployment_frequency_overview.md ✓
- 0110_deployment_frequency_measurement.md ✓
- 0120_deployment_automation.md ✓
- 0130_deployment_pipeline.md ✓

**Supporting Capabilities**:
- Continuous Integration
- Continuous Delivery
- Deployment Automation
- Trunk-based Development
- Feature Flags

### 2. Lead Time for Changes

**Definition**: Time from code commit to successful execution in production.

**DORA Metric**: **DORA-2** (Lead Time for Changes)

**Existing Templates**:
- 0080_lead_time_measurement.md ✓
- 0200_lead_time_overview.md ✓
- 0210_lead_time_measurement.md ✓
- 0220_value_stream_mapping.md ✓
- 0230_bottleneck_identification.md ✓
- 0240_lead_time_reduction_strategies.md ✓

**Supporting Capabilities**:
- Value Stream Mapping
- Bottleneck Identification
- Process Optimization
- Batch Size Reduction
- Parallel Processing

### 3. Mean Time to Restore (MTTR)

**Definition**: Average time to restore service after an incident.

**DORA Metric**: **DORA-3** (Mean Time to Restore)

**Existing Templates**:
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

**Supporting Capabilities**:
- Monitoring and Alerting
- Incident Management
- Recovery Automation
- Self-Healing Systems
- Rollback Automation

### 4. Change Failure Rate

**Definition**: Percentage of deployments that result in service degradation and require remediation.

**DORA Metric**: **DORA-4** (Change Failure Rate)

**Existing Templates**:
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

**Supporting Capabilities**:
- Test Automation
- Code Review
- Quality Gates
- Continuous Testing
- Technical Debt Management

## Framework Components Mapping

### DORA Framework Overview (0010-0099)

| Template | DORA Component | Description | Status |
|----------|----------------|-------------|--------|
| 0010 | Framework Overview | Introduction to DORA Metrics | ✓ |
| 0020 | Software Delivery Performance | Performance measurement | ✓ |
| 0030 | Organizational Performance | Business outcomes | ✓ |
| 0040 | Performance Benchmarking | Industry comparisons | ✓ |
| 0050 | Maturity Assessment | Maturity evaluation | ✓ |

## Coverage Matrix

| DORA Metric | Existing Templates | Coverage |
|-------------|-------------------|----------|
| Deployment Frequency | 6 templates | 100% |
| Lead Time for Changes | 6 templates | 100% |
| Mean Time to Restore | 10 templates | 100% |
| Change Failure Rate | 12 templates | 100% |
| **Overall** | **45 templates** | **100%** |

## Existing Templates Summary

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

## Planned Templates

All planned templates have been successfully implemented. The DORA Framework has now achieved 100% coverage.

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
- Existing Templates: 0060, 0070, 0080, 0180, 0150

### From Medium to High
- Focus: Advanced automation and optimization
- Existing Templates: 0060, 0250, 0260, 0270

### From High to Elite
- Focus: Complete automation and culture
- Existing Templates: 0030, 0050, 0270, 0280

## References

- DORA State of DevOps Reports: https://dora.dev/
- Accelerate Book: https://itrevolution.com/product/accelerate/
- DORA Quick Check: https://dora.dev/quickcheck/

