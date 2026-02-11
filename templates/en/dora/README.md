# DORA Metrics Handbook Templates

## Overview

This directory contains templates for a DORA (DevOps Research and Assessment) Metrics Handbook. DORA Metrics are scientifically validated performance indicators for software delivery performance.

## The Four Key Metrics

1. **Deployment Frequency** - How often code is deployed to production
2. **Lead Time for Changes** - Time from commit to production
3. **Mean Time to Restore (MTTR)** - Time to recover from incidents
4. **Change Failure Rate** - Percentage of failed deployments

## Template Organization

Templates are organized by topic in number ranges:

### 0010-0099: DORA Framework Overview
- 0010: DORA Framework Overview
- 0020: Software Delivery Performance
- 0030: Organizational Performance
- 0040: Performance Benchmarking
- 0050: Maturity Assessment

### 0100-0199: Deployment Frequency
- 0100: Deployment Frequency Overview
- 0110: Deployment Frequency Measurement
- 0120: Deployment Automation
- 0130: Deployment Pipeline
- 0140: Deployment Frequency Improvement

### 0200-0299: Lead Time for Changes
- 0200: Lead Time Overview
- 0210: Lead Time Measurement
- 0220: Value Stream Mapping
- 0230: Bottleneck Identification
- 0240: Lead Time Reduction Strategies

### 0300-0399: Mean Time to Restore (MTTR)
- 0300: MTTR Overview
- 0310: MTTR Measurement
- 0320: Incident Detection
- 0330: Incident Response Procedures
- 0340: Recovery Automation
- 0350: MTTR Improvement

### 0400-0499: Change Failure Rate and Technical Practices
- 0400: Change Failure Rate Overview
- 0410: CFR Measurement
- 0420: Quality Assurance Practices
- 0430: Testing Strategies
- 0440: CI/CD Practices
- 0450: Monitoring and Observability
- 0460: Technical Debt Management

## Usage

### Generate Handbook

```bash
python handbook-generator --template dora --language en --output test-output/en/dora/
```

### Placeholders

Templates use placeholders in the format `{{ source.field }}` for organization-specific data:

- `{{ source.organization_name }}` - Organization name
- `{{ source.dora_owner }}` - Responsible for DORA implementation
- `{{ source.current_deployment_frequency }}` - Current Deployment Frequency
- `{{ source.current_lead_time }}` - Current Lead Time
- `{{ source.current_mttr }}` - Current MTTR
- `{{ source.current_cfr }}` - Current Change Failure Rate

### Customization

1. Copy templates to your project
2. Adapt placeholders to your organization
3. Add organization-specific content
4. Generate the handbook

## Performance Levels

DORA defines four performance levels:

- **Elite**: Top performers (e.g., Deployment Frequency: On-demand)
- **High**: Above-average performance
- **Medium**: Average performance
- **Low**: Below-average performance

## References

- [DORA State of DevOps Reports](https://dora.dev/)
- [Accelerate: The Science of Lean Software and DevOps](https://itrevolution.com/product/accelerate/)
- [DORA Metrics Guide](https://cloud.google.com/blog/products/devops-sre/using-the-four-keys-to-measure-your-devops-performance)

## License

These templates are part of the Handbook-Generator project.
