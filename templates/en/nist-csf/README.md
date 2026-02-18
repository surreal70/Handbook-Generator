# NIST Cybersecurity Framework 2.0 Handbook Templates

## Overview

This directory contains templates for creating a NIST Cybersecurity Framework (CSF) 2.0 handbook. The templates cover all six core functions of the framework: Govern, Identify, Protect, Detect, Respond, and Recover.

## NIST CSF 2.0 Structure

The NIST Cybersecurity Framework 2.0 is a voluntary framework consisting of standards, guidelines, and best practices to manage cybersecurity risks. Version 2.0 introduces the new **Govern** function, which provides the foundation for all other functions.

### The Six Core Functions

1. **Govern (GV)**: Establishes and monitors the organization's cybersecurity risk management strategy
2. **Identify (ID)**: Develops organizational understanding to manage cybersecurity risks
3. **Protect (PR)**: Develops and implements protective measures
4. **Detect (DE)**: Develops and implements activities to detect cybersecurity events
5. **Respond (RS)**: Develops and implements activities to respond to detected cybersecurity incidents
6. **Recover (RC)**: Develops and implements activities to restore capabilities after cybersecurity incidents

## Template Organization

Templates are organized by function and use a numeric prefix system:

### Govern Function (0010-0099)
- `0010_govern_overview.md` - Overview of the Govern function
- `0020_organizational_context.md` - Organizational Context (GV.OC)
- `0030_risk_management_strategy.md` - Risk Management Strategy (GV.RM)
- `0040_roles_responsibilities.md` - Roles and Responsibilities (GV.RR)
- `0050_policy_framework.md` - Policy Framework (GV.PO)
- `0060_oversight.md` - Oversight and Monitoring (GV.OV)
- `0070_supply_chain_risk_management.md` - Supply Chain Risk Management (GV.SC)

### Identify Function (0100-0199)
- `0100_asset_management.md` - Asset Management (ID.AM)
- `0110_business_environment.md` - Business Environment (ID.BE)
- `0120_governance.md` - Governance (ID.GV)
- `0130_risk_assessment.md` - Risk Assessment (ID.RA)
- `0140_risk_management_strategy.md` - Risk Management Strategy (ID.RM)
- `0150_supply_chain_risk_management.md` - Supply Chain Risk Management (ID.SC)

### Protect Function (0200-0299)
- `0200_identity_access_control.md` - Identity Management and Access Control (PR.AA)
- `0210_awareness_training.md` - Awareness and Training (PR.AT)
- `0220_data_security.md` - Data Security (PR.DS)
- `0230_information_protection_processes.md` - Information Protection Processes (PR.IP)
- `0240_maintenance.md` - Maintenance (PR.MA)
- `0250_protective_technology.md` - Protective Technology (PR.PT)

### Detect Function (0300-0399)
- `0300_anomalies_events.md` - Anomalies and Events (DE.AE)
- `0310_security_monitoring.md` - Security Continuous Monitoring (DE.CM)
- `0320_detection_processes.md` - Detection Processes (DE.DP)

### Respond Function (0400-0499)
- `0400_response_planning.md` - Response Planning (RS.RP)
- `0410_communications.md` - Communications (RS.CO)
- `0420_analysis.md` - Analysis (RS.AN)
- `0430_mitigation.md` - Mitigation (RS.MI)
- `0440_improvements.md` - Improvements (RS.IM)

### Recover Function (0500-0599)
- `0500_recovery_planning.md` - Recovery Planning (RC.RP)
- `0510_improvements.md` - Improvements (RC.IM)
- `0520_communications.md` - Communications (RC.CO)

### Implementation and Assessment (0600-0699)
- `0600_implementation_tiers.md` - Implementation Tiers
- `0610_current_profile.md` - Current Profile
- `0620_target_profile.md` - Target Profile
- `0630_gap_analysis.md` - Gap Analysis
- `0640_action_plan.md` - Action Plan

## Numbering Scheme

- Templates use 4-digit prefixes (e.g., 0010, 0020, 0030)
- Increments of 10 allow for future insertions
- Functions are grouped in hundred ranges (0000-0099, 0100-0199, etc.)

## Placeholder System

Templates use placeholders for organization-specific data:

### Metadata Placeholders
- `{{ meta-handbook.owner }}` - Document owner
- `{{ meta-handbook.revision }}` - Version number
- `{{ meta-handbook.modifydate }}` - Date
- `{{ meta-organisation.name }}` - Organization name
- `{{ meta-organisation-roles.role_CISO }}` - CISO name
- `{{ meta-organisation-roles.role_Risk_Manager }}` - CRO name

### Data Source Placeholders
- `[TODO]` - Organization name from data source
- `[TODO]` - Author from data source
- Additional organization-specific fields

## Customizing Templates

### 1. Update Metadata
Start with the `0000_metadata_en_nist-csf.md` file and fill in the metadata.

### 2. Replace Placeholders
Replace all `{{ placeholder }}` with your organization-specific information.

### 3. Adapt Content
Customize templates to your specific requirements:
- Add organization-specific processes
- Remove non-applicable sections
- Expand sections as needed

### 4. Update Document References
Ensure all cross-references between documents are correct.

## Using with Handbook Generator

These templates are designed for use with the handbook generator system:

```bash
python handbook-generator --template nist-csf --language en --output-format html
```

Supported output formats:
- HTML (mini-website with navigation)
- PDF (with table of contents)
- Markdown (combined or separate files)

## Framework Reference

For more information about NIST Cybersecurity Framework 2.0:
- [NIST CSF 2.0 Website](https://www.nist.gov/cyberframework)
- [NIST CSF 2.0 Framework](https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.29.pdf)

## Framework Mapping

See `FRAMEWORK_MAPPING.md` for detailed mapping of templates to NIST CSF 2.0 categories and subcategories.

## License

These templates are based on the NIST Cybersecurity Framework 2.0, which is in the public domain.
||---|
| 1.0 | 2024 | Initial version based on NIST CSF 2.0 |
