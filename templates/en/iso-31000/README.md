# ISO 31000 Risk Management Handbook Templates

## Overview

This directory contains templates for creating an ISO 31000 Risk Management Handbook. The templates cover all aspects of risk management: the eight principles, the framework, the risk management process, and monitoring and continual improvement.

## ISO 31000 Structure

ISO 31000 is the international standard for risk management. It provides principles, a framework, and a process for managing risks in any organization.

### The Eight Risk Management Principles

1. **Integrated**: Risk management is part of all organizational activities
2. **Structured and comprehensive**: Systematic approach for consistent results
3. **Customized**: Risk management is aligned with context and objectives
4. **Inclusive**: Involvement of stakeholders for relevant insights
5. **Dynamic**: Risk management responds to changes
6. **Best available information**: Decisions based on current data
7. **Human and cultural factors**: Consideration of human behavior
8. **Continual improvement**: Ongoing development of risk management

### Risk Management Framework

- **Leadership and commitment**: Top management support
- **Integration**: Embedding in organizational processes
- **Design**: Adaptation to organizational context
- **Implementation**: Framework deployment
- **Evaluation**: Effectiveness review
- **Improvement**: Continual adaptation

### Risk Management Process

- **Communication and consultation**: Stakeholder engagement
- **Establishing the context**: Define framework conditions
- **Risk assessment**: Identification, analysis, evaluation
- **Risk treatment**: Risk mitigation measures
- **Monitoring and review**: Continuous control
- **Recording and reporting**: Documentation and communication

## Template Organization

Templates are thematically organized using a numeric prefix system:

### Risk Management Principles (0010-0099)
- `0010_risk_management_overview.md` - Risk Management Overview
- `0020_integrated_principle.md` - Principle 1: Integrated
- `0030_structured_comprehensive_principle.md` - Principle 2: Structured and comprehensive
- `0040_customized_principle.md` - Principle 3: Customized
- `0050_inclusive_dynamic_principle.md` - Principle 4 & 5: Inclusive and Dynamic
- `0060_best_information_principle.md` - Principle 6: Best available information
- `0070_human_cultural_factors_principle.md` - Principle 7: Human and cultural factors
- `0080_continual_improvement_principle.md` - Principle 8: Continual improvement

### Risk Management Framework (0100-0199)
- `0100_framework_overview.md` - Framework Overview
- `0110_leadership_commitment.md` - Leadership and Commitment
- `0120_integration.md` - Integration
- `0130_framework_design.md` - Framework Design
- `0140_framework_implementation.md` - Framework Implementation
- `0150_framework_evaluation.md` - Framework Evaluation
- `0160_framework_improvement.md` - Framework Improvement

### Risk Assessment Process (0200-0299)
- `0200_risk_assessment_overview.md` - Risk Assessment Overview
- `0210_scope_context.md` - Establishing the Context
- `0220_risk_identification.md` - Risk Identification
- `0230_risk_analysis.md` - Risk Analysis
- `0240_risk_evaluation.md` - Risk Evaluation

### Risk Treatment and Communication (0300-0399)
- `0300_risk_treatment_overview.md` - Risk Treatment Overview
- `0310_treatment_options.md` - Treatment Options
- `0320_treatment_plans.md` - Treatment Plans
- `0330_treatment_implementation.md` - Treatment Implementation
- `0340_communication_consultation.md` - Communication and Consultation
- `0350_recording_reporting.md` - Recording and Reporting

### Monitoring and Review (0400-0499)
- `0400_monitoring_review_overview.md` - Monitoring and Review Overview
- `0410_performance_monitoring.md` - Performance Monitoring
- `0420_risk_register_maintenance.md` - Risk Register Maintenance
- `0430_review_processes.md` - Review Processes
- `0440_lessons_learned.md` - Lessons Learned

## Numbering Scheme

- Templates use 4-digit prefixes (e.g., 0010, 0020, 0030)
- Increments of 10 allow for future insertions
- Topics are grouped in hundred ranges (0000-0099, 0100-0199, etc.)

## Placeholder System

Templates use placeholders for organization-specific data:

### Metadata Placeholders
- `{{ meta.owner }}` - Document owner
- `{{ meta.version }}` - Version number
- `{{ meta.date }}` - Date
- `{{ meta.organization }}` - Organization name
- `{{ meta.ceo }}` - CEO name
- `{{ meta.cro }}` - Chief Risk Officer name

### Data Source Placeholders
- `{{ source.organization_name }}` - Organization name from data source
- `{{ source.author }}` - Author from data source
- Additional organization-specific fields

## Customizing Templates

### 1. Update Metadata
Start with the file `0000_metadata_en_iso-31000.md` and fill in the metadata.

### 2. Replace Placeholders
Replace all `{{ placeholder }}` with your organization-specific information.

### 3. Adapt Content
Customize templates to your specific requirements:
- Add organization-specific risk categories
- Define your risk appetite and risk tolerance
- Adapt assessment criteria
- Expand sections as needed

### 4. Update Document References
Ensure all cross-references between documents are correct.

## Using with Handbook Generator

These templates are designed for use with the handbook generator system:

```bash
python handbook-generator --template iso-31000 --language en --output-format html
```

Supported output formats:
- HTML (mini-website with navigation)
- PDF (with table of contents)
- Markdown (combined or separate files)

## Framework Reference

More information about ISO 31000:
- [ISO 31000:2018](https://www.iso.org/standard/65694.html)
- ISO 31000:2018 - Risk management — Guidelines

## Framework Mapping

See `FRAMEWORK_MAPPING.md` for a detailed mapping of templates to ISO 31000 components and clauses.

## License

These templates are based on ISO 31000:2018. The standard itself is copyrighted.

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2024 | Initial version based on ISO 31000:2018 |

