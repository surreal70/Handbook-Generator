# TOGAF Enterprise Architecture Handbook Templates

## Overview

This directory contains templates for creating TOGAF (The Open Group Architecture Framework) enterprise architecture documentation. The templates follow the TOGAF Architecture Development Method (ADM) and provide comprehensive coverage of all ADM phases.

## Framework Information

- **Framework**: The Open Group Architecture Framework (TOGAF)
- **Version**: TOGAF 9.2
- **Language**: English
- **Template Count**: 14+ templates covering all ADM phases

## Template Organization

Templates are organized by TOGAF ADM phases using a numeric prefix system:

### Preliminary Phase and Foundation (0010-0099)
- **0010**: Architecture Framework Setup
- **0020**: Architecture Principles
- **0030**: Governance Framework
- **0040**: Repository Structure
- **0050**: Stakeholder Management
- **0060**: Tools and Techniques

### Phase A - Architecture Vision (0100-0199)
- **0100**: Architecture Vision
- **0110**: Business Goals and Drivers

### Phase B - Business Architecture (0200-0299)
- **0200**: Business Architecture Overview
- **0210**: Business Capability Model

### Phase C - Information Systems Architecture (0300-0399)
- **0300**: Data Architecture
- **0330**: Application Architecture

### Phase D - Technology Architecture (0400-0499)
- **0400**: Technology Architecture Overview

### Phase E - Opportunities and Solutions (0500-0599)
- **0500**: Implementation Approach

### Phase F-H - Migration and Governance (0600-0699)
- **0600**: Migration Planning

### Requirements Management (0700-0799)
- **0700**: Requirements Management

## Template Structure

Each template follows a consistent structure:

```markdown
---
Document-ID: togaf-NNNN
Owner: {{ meta-handbook.author }}
Version: {{ meta-handbook.revision }}
Status: Draft
Classification: Internal
Last Update: {{ meta-handbook.modifydate }}
---

# Template Title

## Purpose
[Description of the template's purpose]

## Scope
[What is covered in this template]

## Content Sections
[Main content with placeholders]

<!-- Author notes: Guidance for template users -->
```

## Placeholder System

Templates use placeholders for organization-specific data:

- `{{ meta-handbook.author }}` - Document author
- `{{ meta-handbook.revision }}` - Document version
- `{{ meta-handbook.modifydate }}` - Document date
- `[TODO]` - Organization name
- `[TODO]` - Other organization-specific fields

## Customization Guide

### Step 1: Configure Metadata
Edit the metadata template (0000_metadata_en_togaf.md) with your organization's information.

### Step 2: Customize Templates
Review each template and:
- Fill in placeholder values
- Add organization-specific content
- Remove sections that don't apply
- Add additional sections as needed

### Step 3: Adapt to Your Context
- Adjust governance structures to match your organization
- Modify capability models for your business
- Tailor technology standards to your environment
- Align with existing processes and methodologies

### Step 4: Maintain and Update
- Review templates regularly
- Update based on architecture changes
- Incorporate lessons learned
- Keep aligned with TOGAF updates

## Usage Guidelines

### For Enterprise Architects
- Use templates as starting points for architecture documentation
- Customize based on stakeholder needs
- Maintain consistency across architecture artifacts
- Link related documents and artifacts

### For Architecture Teams
- Follow the ADM cycle systematically
- Document decisions using Architecture Decision Records (ADRs)
- Maintain traceability between requirements and architecture
- Engage stakeholders throughout the process

### For Project Teams
- Reference architecture templates for project planning
- Ensure project architectures align with enterprise architecture
- Submit architecture for compliance review
- Document deviations and exceptions

## Integration with TOGAF ADM

These templates support the complete TOGAF ADM cycle:

1. **Preliminary Phase**: Establish architecture capability
2. **Phase A**: Define architecture vision
3. **Phase B**: Develop business architecture
4. **Phase C**: Develop information systems architecture
5. **Phase D**: Develop technology architecture
6. **Phase E**: Identify opportunities and solutions
7. **Phase F**: Plan migration
8. **Phase G**: Implement governance
9. **Phase H**: Manage architecture change
10. **Requirements Management**: Continuous throughout

## Additional Resources

- **FRAMEWORK_MAPPING.md**: Maps templates to TOGAF ADM phases and deliverables
- **diagrams/**: Directory for architecture diagrams and visualizations
- **TOGAF Documentation**: https://www.opengroup.org/togaf

## Support and Feedback

For questions or suggestions about these templates:
- Contact the Enterprise Architecture team
- Submit feedback through the architecture repository
- Participate in architecture governance meetings

---

*These templates are based on TOGAF 9.2 and should be adapted to your organization's specific needs and context.*
