# IDW PS 951 IT Audit Handbook Templates

## Overview

This directory contains templates for IT audits according to IDW Auditing Standard 951 "Principles for the Proper Auditing of Compliance Management Systems". The templates support the systematic audit of IT systems, IT processes, and IT controls in the context of annual financial statement audits and other business audits.

## IDW PS 951 Reference

IDW Auditing Standard 951 was published by the Institut der Wirtschaftsprüfer in Deutschland e.V. (IDW - Institute of Public Auditors in Germany) and defines the principles for auditing IT systems in the context of financial statement audits. The standard addresses:

- IT strategy and IT organization
- IT processes and IT service management
- IT systems and applications
- IT infrastructure and IT operations
- IT security and data protection
- IT governance and IT risk management

## Template Organization

### Numbering Scheme

The templates follow a structured numbering scheme with 4-digit prefixes:

- **0000**: Metadata
- **0010-0099**: Audit Planning and Preparation
- **0100-0199**: IT Strategy and IT Organization
- **0200-0299**: IT Processes
- **0300-0399**: IT Systems and Applications
- **0400-0499**: IT Infrastructure and IT Operations
- **0500-0599**: IT Security and Data Protection

### Template Structure

Each template follows a standardized structure:

```markdown
# Template Title

**Document-ID:** idw-ps-951-NNNN
**Owner:** {{ meta-organisation-roles.role_Internal_Auditor }}
**Version:** {{ meta-handbook.revision }}
**Status:** {{ meta-handbook.status }}
**Classification:** {{ meta-handbook.classification }}
**Last Update:** {{ meta-handbook.modifydate }}

---

## 1. Purpose
## 2. Audit Subject
## 3. Audit Procedures
## 4. Audit Criteria
## 5. Findings
## 6. Recommendations
## 7. References
```

## Audit Areas

### 1. Audit Planning (0010-0099)

- **0010**: Audit Planning Overview
- **0020**: Audit Scope Definition
- **0030**: Risk Assessment and Risk Analysis
- **0040**: Audit Team and Resources
- **0050**: Timeline and Milestones

### 2. IT Strategy and Organization (0100-0199)

- **0100**: IT Strategy Evaluation
- **0110**: IT Governance Structure
- **0120**: IT Organization and Roles
- **0130**: IT Steering Committees
- **0140**: IT Service Management

### 3. IT Processes (0200-0299)

- **0200**: IT Processes Overview
- **0210**: Change Management
- **0220**: Incident Management
- **0230**: Problem Management
- **0240**: Release Management
- **0250**: Configuration Management

### 4. IT Systems and Applications (0300-0399)

- **0300**: IT Systems and Applications Overview
- **0310**: System Architecture
- **0320**: Application Controls
- **0330**: Interface Management
- **0340**: Data Integrity Controls

### 5. IT Infrastructure and Operations (0400-0499)

- **0400**: IT Infrastructure and Operations Overview
- **0410**: Server and Storage
- **0420**: Network Infrastructure
- **0430**: Database Systems
- **0440**: Backup and Recovery
- **0450**: Operations Procedures

### 6. IT Security and Data Protection (0500-0599)

- **0500**: IT Security and Data Protection Overview
- **0510**: Access Control
- **0520**: Encryption and Key Management
- **0530**: Security Monitoring
- **0540**: Data Protection Compliance
- **0550**: Privacy Controls

## Placeholder System

The templates use a placeholder system for organization-specific data:

### Metadata Placeholders
- `{{ meta-organisation-roles.role_Internal_Auditor }}` - Audit Lead
- `{{ meta-handbook.revision }}` - Document Version
- `{{ meta-handbook.status }}` - Document Status
- `{{ meta-handbook.modifydate }}` - Date

### Source Placeholders
- `[TODO]` - Organization Name
- `[TODO]` - Audit Period
- `[TODO]` - Systems in Scope
- Additional context-specific placeholders

## Customizing Templates

### 1. Adjust Metadata

Customize the metadata template file:
- `0000_metadata_en_idw-ps-951.md`

### 2. Organization-Specific Data

Replace placeholders with your data:
- Manually in the templates
- Via the Handbook Generator's placeholder system
- Via data sources (e.g., NetBox)

### 3. Adjust Audit Scope

Adapt templates to your specific audit scope:
- Remove non-relevant sections
- Add additional audit areas
- Adjust audit criteria

### 4. Adjust Audit Depth

Adapt the level of detail to your requirements:
- Detailed audit: Complete all sections fully
- Standard audit: Focus on core areas
- Overview audit: Summary assessments

## Usage

### 1. Generate Handbook

```bash
python handbook-generator --template idw-ps-951 --language en --output-format html
```

### 2. Output Formats

- **HTML**: Interactive website with navigation
- **PDF**: Printable document with table of contents
- **Markdown**: Editable individual files

### 3. Audit Documentation

The generated handbooks serve as:
- Audit guide
- Documentation template
- Reporting basis
- Evidence documentation

## Best Practices

### Audit Planning
1. Start with risk analysis (0030)
2. Define scope clearly (0020)
3. Plan sufficient resources (0040)
4. Create a realistic timeline (0050)

### Audit Execution
1. Document all audit procedures
2. Collect sufficient evidence
3. Conduct structured interviews
4. Test controls systematically

### Reporting
1. Structure findings by severity
2. Formulate concrete recommendations
3. Prioritize actions
4. Define implementation deadlines

## Compliance and Standards

The templates consider:
- **IDW PS 951**: Auditing Standard for IT Systems
- **IDW PS 340**: Risk Early Warning System
- **ISO/IEC 27001**: Information Security
- **GDPR**: General Data Protection Regulation
- **BSI IT-Grundschutz**: IT Security Standards
- **COBIT 2019**: IT Governance Framework
- **ITIL 4**: IT Service Management

## Support and Documentation

Further information:
- **FRAMEWORK_MAPPING.md**: Mapping to IDW PS 951 requirements
- **Handbook Generator Documentation**: General usage instructions
- **IDW Website**: https://www.idw.de

## License and Disclaimer

These templates serve as guidance and must be adapted to the specific requirements of your organization. They do not replace professional judgment by qualified auditors.

---

**Template Version:** 1.0  
**Last Update:** 2026-02-10  
**Language:** English

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1 | {{meta.document.last_updated}} | Initial creation |
