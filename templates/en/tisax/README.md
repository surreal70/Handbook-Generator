# TISAX Handbook Templates

## Overview

This directory contains templates for a TISAX (Trusted Information Security Assessment Exchange) handbook. TISAX is an information security assessment standard for the automotive industry based on the VDA ISA catalog.

## Template Organization

The templates are organized by TISAX control areas and use a numeric prefix system:

### 0010-0099: Information Security Management
- 0010: TISAX Framework Overview
- 0020: Information Security Policy
- 0030: Organization of Information Security
- 0040: Risk Management
- 0050: Security Objectives and Planning

### 0100-0199: Asset Management and Access Control
- 0100: Asset Management Overview
- 0110: Asset Inventory
- 0120: Information Classification
- 0130: Media Handling
- 0140: Access Control Policy
- 0150: User Access Management
- 0160: System and Application Access Control

### 0200-0299: Cryptography and Physical Security
- 0200: Cryptographic Controls
- 0210: Key Management
- 0220: Physical Security Perimeter
- 0230: Physical Entry Controls
- 0240: Securing Offices and Facilities
- 0250: Equipment Security

### 0300-0399: Operations and Communications Security
- 0300: Operations Security Overview
- 0310: Change Management
- 0320: Capacity Management
- 0330: Malware Protection
- 0340: Backup and Recovery
- 0350: Logging and Monitoring
- 0360: Network Security Management
- 0370: Information Transfer

### 0400-0499: Supplier Relationships and Incident Management
- 0400: Supplier Security
- 0410: Supplier Agreements
- 0420: Supplier Monitoring
- 0430: Incident Management Procedures
- 0440: Incident Response
- 0450: Evidence Collection

### 0500-0599: Business Continuity and Compliance
- 0500: Business Continuity Planning
- 0510: ICT Continuity
- 0520: Compliance with Legal Requirements
- 0530: Intellectual Property Rights
- 0540: Protection of Records
- 0550: Privacy and Personal Data Protection

## Using the Templates

### Placeholders

The templates use placeholders in the format `{{ source.field }}` for organization-specific data:

- `{{ source.organization_name }}` - Your organization name
- `{{ source.author }}` - Document author
- `{{ meta.version }}` - Version number
- `{{ meta.date }}` - Date

### Customization

1. Copy the templates to your project directory
2. Replace placeholders with your organization-specific information
3. Adapt the content to your specific requirements
4. Remove non-applicable sections
5. Add additional organization-specific sections

### TISAX Assessment Levels

TISAX defines three assessment levels:

- **AL1**: Basic assessment (self-disclosure)
- **AL2**: Detailed assessment with on-site audit
- **AL3**: Very detailed assessment with comprehensive on-site audit

Adapt the level of detail in your documentation to the target assessment level.

## TISAX Requirements

The templates cover the following TISAX areas:

1. **Information Security**: Protection of information and IT systems
2. **Prototype Protection**: Protection of prototypes and development information
3. **Data Protection**: Protection of personal data according to GDPR

## Framework Mapping

See FRAMEWORK_MAPPING.md for a detailed mapping of templates to specific TISAX assessment objectives and VDA ISA controls.

## Additional Resources

- VDA ISA Catalog
- TISAX Participant Handbook
- ENX Association (TISAX operator)
- GDPR and national data protection laws

## Notes

- These templates serve as a starting point and must be adapted to your specific requirements
- Consult information security and data protection experts as needed
- Keep documentation current and review regularly
- Prepare thoroughly for TISAX assessments

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1 | {{meta.document.last_updated}} | Initial creation |
