# CIS Controls v8 Templates

## Overview

This directory contains English templates for CIS Controls v8 Hardening. The handbook comprises 27 structured documents covering hardening baselines for operating systems and applications according to the **CIS Controls v8** framework.

## Template Structure

### Foundation (0010-0050) - 5 Templates
- **0010**: CIS Controls Overview and Approach
- **0020**: Scope, Asset Groups and Tiering
- **0030**: Hardening Lifecycle and Processes
- **0040**: Exceptions and Risk Acceptance
- **0050**: Testing and Validation

### Operating Systems (0100-0150) - 6 Templates
- **0100**: Windows Server Hardening Baseline
- **0110**: Windows Client Hardening Baseline
- **0120**: Linux Hardening Baseline
- **0130**: macOS Hardening Baseline
- **0140**: Container Base Images Hardening
- **0150**: Mobile Device Hardening

### Applications (0200-0330) - 14 Templates
- **0200**: Nginx Webserver Hardening
- **0210**: Apache Webserver Hardening
- **0220**: IIS Webserver Hardening
- **0230**: Tomcat Application Server Hardening
- **0240**: PostgreSQL Database Hardening
- **0250**: MySQL/MariaDB Database Hardening
- **0260**: MS SQL Server Database Hardening
- **0270**: MongoDB Database Hardening
- **0280**: Kubernetes Cluster Hardening
- **0290**: Docker Engine Hardening
- **0300**: SSH Service Hardening
- **0310**: Active Directory Hardening
- **0320**: Identity Provider Hardening
- **0330**: Cloud Platform Hardening

### Appendices (0400-0410) - 2 Templates
- **0400**: Control Mapping Template
- **0410**: Checklists and Evidence

## Numbering Scheme

- Templates use 4-digit numbers with 10-step increments (0010, 0020, 0030, ...)
- This allows for later insertions between existing templates
- Number ranges group related topics

## Usage

1. **Preparation**: Determine asset groups and tiering levels
2. **Baseline Selection**: Choose relevant hardening baselines
3. **Customization**: Adapt templates to your environment
4. **Placeholders**: Replace all `[TODO]` markers
5. **Testing**: Validate hardening measures in test environment
6. **Rollout**: Implement gradually in production

## Placeholders

Templates support two types of placeholders:

- **Manual Placeholders**: `[TODO: Description]` - must be replaced manually
- **Automatic Placeholders**: `[TODO]` - populated from data sources

Examples of automatic placeholders:
- `{{ meta-organisation.name }}` - Organization name
- `{{ meta-handbook.author }}` - Author
- `{{ meta-handbook.revision }}` - Version number
- `{{ meta-handbook.modifydate }}` - Date

## CIS Controls v8 Framework

The templates are based on the CIS Controls v8 framework with 18 Controls:

- **CIS Control 1**: Inventory and Control of Enterprise Assets
- **CIS Control 2**: Inventory and Control of Software Assets
- **CIS Control 3**: Data Protection
- **CIS Control 4**: Secure Configuration of Enterprise Assets and Software
- **CIS Control 5**: Account Management

For the German version, see: `templates/de/cis-controls/`

## Version

Version 1.0 - Initial template set

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | [TODO] | {{ meta.defaults.author }} | Initial Creation |

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1 | {{meta.document.last_updated}} | Initial creation |
