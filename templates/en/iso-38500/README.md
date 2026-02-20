# ISO/IEC 38500 IT Governance Handbook Templates

## Overview

This directory contains templates for creating an ISO/IEC 38500 IT Governance Handbook. The templates cover all aspects of IT governance: the six principles, the EDM model, roles and responsibilities, and implementation and continuous improvement.

## ISO/IEC 38500 Structure

ISO/IEC 38500 is the international standard for Corporate Governance of IT. It defines a framework for effective, efficient, and acceptable use of IT in organizations.

### The Six Governance Principles

1. **Responsibility**: Clear responsibilities for IT decisions
2. **Strategy**: IT strategy supports business strategy
3. **Acquisition**: IT acquisitions are appropriately justified
4. **Performance**: IT delivers required performance
5. **Conformance**: IT meets all obligations
6. **Human Behavior**: IT respects human needs

### The EDM Model

- **Evaluate**: Assessment of current and future IT use
- **Direct**: Preparation and communication of plans and policies
- **Monitor**: Monitoring of compliance and performance

## Template Organization

Templates are organized thematically using a numeric prefix system:

### Governance Framework and Principles (0010-0099)
- `0010_governance_framework.md` - IT Governance Framework Overview
- `0020_governance_model.md` - IT Governance Model
- `0030_principles_overview.md` - Overview of Six Principles
- `0040_responsibility_principle.md` - Principle 1: Responsibility
- `0050_strategy_principle.md` - Principle 2: Strategy
- `0060_acquisition_principle.md` - Principle 3: Acquisition
- `0070_performance_principle.md` - Principle 4: Performance
- `0080_conformance_principle.md` - Principle 5: Conformance
- `0090_human_behavior_principle.md` - Principle 6: Human Behavior

### Evaluate-Direct-Monitor Model (0100-0199)
- `0100_edm_model.md` - EDM Model Overview
- `0110_evaluation_processes.md` - Evaluation Processes
- `0120_direction_processes.md` - Direction Processes
- `0130_monitoring_processes.md` - Monitoring Processes
- `0140_performance_measurement.md` - Performance Measurement

### Roles and Responsibilities (0200-0299)
- `0200_governance_roles.md` - IT Governance Roles
- `0210_board_responsibilities.md` - Board Responsibilities
- `0220_executive_responsibilities.md` - Executive Management Responsibilities
- `0230_it_management_responsibilities.md` - IT Management Responsibilities
- `0240_stakeholder_engagement.md` - Stakeholder Engagement

### Implementation and Improvement (0300-0399)
- `0300_governance_implementation.md` - IT Governance Implementation
- `0310_policy_framework.md` - Policy Framework
- `0320_decision_making.md` - Decision-Making Processes
- `0330_communication.md` - Communication
- `0340_continuous_improvement.md` - Continuous Improvement

## Numbering Scheme

- Templates use 4-digit prefixes (e.g., 0010, 0020, 0030)
- Increments of 10 allow for future insertions
- Topics are grouped in hundred ranges (0000-0099, 0100-0199, etc.)

## Placeholder System

Templates use placeholders for organization-specific data:

### Metadata Placeholders
- `{{ meta-handbook.owner }}` - Document owner
- `{{ meta-handbook.revision }}` - Version number
- `{{ meta-handbook.modifydate }}` - Date
- `{{ meta-organisation.name }}` - Organization name
- `{{ meta-organisation-roles.role_CIO }}` - CIO name
- `{{ meta-organisation-roles.role_CISO }}` - CISO name

### Data Source Placeholders
- `[TODO]` - Organization name from data source
- `[TODO]` - Author from data source
- Additional organization-specific fields

## Customizing Templates

### 1. Update Metadata
Start with the file `0000_metadata_en_iso-38500.md` and fill in the metadata.

### 2. Replace Placeholders
Replace all `{{ placeholder }}` with your organization-specific information.

### 3. Adapt Content
Customize templates to your specific requirements:
- Add organization-specific governance structures
- Remove non-applicable sections
- Expand sections as needed

### 4. Update Document References
Ensure all cross-references between documents are correct.

## Using with Handbook Generator

These templates are designed for use with the handbook generator system:

```bash
python handbook-generator --template iso-38500 --language en --output-format html
```

Supported output formats:
- HTML (mini-website with navigation)
- PDF (with table of contents)
- Markdown (combined or separate files)

## Framework Reference

More information about ISO/IEC 38500:
- [ISO/IEC 38500:2015](https://www.iso.org/standard/62816.html)
- ISO/IEC 38500:2015 - Information technology — Governance of IT for the organization

## Framework Mapping

See `FRAMEWORK_MAPPING.md` for detailed mapping of templates to ISO/IEC 38500 principles and practices.

## License

These templates are based on ISO/IEC 38500:2015. The standard itself is copyrighted.
