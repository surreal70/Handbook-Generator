# TOGAF Framework Mapping

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

This document maps the TOGAF handbook templates to specific TOGAF ADM phases, deliverables, and artifacts. It ensures comprehensive coverage of TOGAF requirements and provides traceability between templates and framework elements.

## TOGAF ADM Phase Mapping

### Preliminary Phase

**Purpose**: Prepare and initiate architecture activities

| Template | TOGAF Deliverable | Description |
|----------|-------------------|-------------|
| 0010_architecture_framework_setup.md | Architecture Framework | Customized TOGAF framework for the organization |
| 0020_architecture_principles.md | Architecture Principles | Guiding principles for architecture decisions |
| 0030_governance_framework.md | Architecture Governance Framework | Governance structure and processes |
| 0040_repository_structure.md | Architecture Repository | Repository organization and content |
| 0050_stakeholder_management.md | Stakeholder Map | Stakeholder identification and engagement |
| 0060_tools_and_techniques.md | Architecture Tools | Tool stack and techniques |

**Coverage**: Complete coverage of Preliminary Phase deliverables

### Phase A - Architecture Vision

**Purpose**: Define the scope and vision for the architecture initiative

| Template | TOGAF Deliverable | Description |
|----------|-------------------|-------------|
| 0100_architecture_vision.md | Architecture Vision | High-level aspirational view of target architecture |
| 0110_business_goals_and_drivers.md | Business Goals and Drivers | Business context and motivations |
| 0120_stakeholder_concerns.md | Stakeholder Concerns | Detailed stakeholder analysis and concerns |

**Key TOGAF Artifacts Covered**:
- Architecture Vision document
- Stakeholder Map Matrix
- Value propositions
- Architecture Definition Document (initial)

**Coverage**: Core Phase A deliverables covered

### Phase B - Business Architecture

**Purpose**: Develop the business architecture

| Template | TOGAF Deliverable | Description |
|----------|-------------------|-------------|
| 0200_business_architecture_overview.md | Business Architecture | Overall business architecture description |
| 0210_business_capability_model.md | Business Capability Model | Capability hierarchy and maturity |

**Key TOGAF Artifacts Covered**:
- Business Capability Assessment
- Value Stream Map
- Organization Map
- Business Process Models
- Business Function Catalog

**Coverage**: Core Phase B deliverables covered

### Phase C - Information Systems Architecture

**Purpose**: Develop data and application architectures

| Template | TOGAF Deliverable | Description |
|----------|-------------------|-------------|
| 0300_data_architecture.md | Data Architecture | Data entities, lifecycle, and governance |
| 0330_application_architecture.md | Application Architecture | Application portfolio and interfaces |

**Key TOGAF Artifacts Covered**:
- Data Entity/Business Function Matrix
- Application Portfolio Catalog
- Application/Function Matrix
- Interface Catalog
- Data Lifecycle Diagrams

**Coverage**: Core Phase C deliverables covered

### Phase D - Technology Architecture

**Purpose**: Develop the technology architecture

| Template | TOGAF Deliverable | Description |
|----------|-------------------|-------------|
| 0400_technology_architecture_overview.md | Technology Architecture | Technology platforms and infrastructure |

**Key TOGAF Artifacts Covered**:
- Technology Standards Catalog
- Technology Portfolio Catalog
- System/Technology Matrix
- Platform Decomposition Diagram
- Network Computing/Hardware Diagram

**Coverage**: Core Phase D deliverables covered

### Phase E - Opportunities and Solutions

**Purpose**: Identify delivery vehicles and plan implementation

| Template | TOGAF Deliverable | Description |
|----------|-------------------|-------------|
| 0500_implementation_approach.md | Implementation and Migration Strategy | ABBs, SBBs, gap analysis, transition architectures |

**Key TOGAF Artifacts Covered**:
- Architecture Building Blocks (ABBs)
- Solution Building Blocks (SBBs)
- Gap Analysis
- Transition Architecture
- Implementation Factor Assessment

**Coverage**: Core Phase E deliverables covered

### Phase F - Migration Planning

**Purpose**: Finalize implementation and migration plan

| Template | TOGAF Deliverable | Description |
|----------|-------------------|-------------|
| 0600_migration_planning.md | Implementation and Migration Plan | Detailed migration plan and roadmap |

**Key TOGAF Artifacts Covered**:
- Implementation and Migration Plan
- Architecture Roadmap
- Implementation Factor Assessment
- Transition Architecture (detailed)

**Coverage**: Core Phase F deliverables covered

### Phase G - Implementation Governance

**Purpose**: Provide architecture oversight during implementation

**Covered in**: 0600_migration_planning.md (Implementation Governance section)

**Key TOGAF Artifacts Covered**:
- Architecture Contract
- Compliance Assessments
- Change Requests

**Coverage**: Implementation governance processes covered

### Phase H - Architecture Change Management

**Purpose**: Manage changes to the architecture

**Covered in**: 0600_migration_planning.md (Architecture Change Management section)

**Key TOGAF Artifacts Covered**:
- Change Request
- Architecture Updates
- Architecture Compliance Reviews

**Coverage**: Change management processes covered

### Requirements Management

**Purpose**: Manage architecture requirements throughout ADM

| Template | TOGAF Deliverable | Description |
|----------|-------------------|-------------|
| 0700_requirements_management.md | Requirements Repository | Requirements management process and repository |

**Key TOGAF Artifacts Covered**:
- Requirements Impact Assessment
- Requirements Repository
- Requirements Traceability Matrix

**Coverage**: Requirements management process covered

## TOGAF Content Framework Mapping

### Architecture Principles

**Template**: 0020_architecture_principles.md

**TOGAF Content Framework Elements**:
- Business Principles
- Data Principles
- Application Principles
- Technology Principles

### Architecture Vision

**Template**: 0100_architecture_vision.md

**TOGAF Content Framework Elements**:
- Business Capability Assessment
- Stakeholder Map Matrix
- Value Chain Diagram

### Business Architecture

**Templates**: 0200_business_architecture_overview.md, 0210_business_capability_model.md

**TOGAF Content Framework Elements**:
- Organization/Actor Catalog
- Business Capability Catalog
- Value Stream Catalog
- Business Process Catalog
- Business Function Catalog

### Data Architecture

**Template**: 0300_data_architecture.md

**TOGAF Content Framework Elements**:
- Data Entity/Data Component Catalog
- Data Entity/Business Function Matrix
- System/Data Matrix

### Application Architecture

**Template**: 0330_application_architecture.md

**TOGAF Content Framework Elements**:
- Application Portfolio Catalog
- Interface Catalog
- Application/Organization Matrix
- Application/Function Matrix

### Technology Architecture

**Template**: 0400_technology_architecture_overview.md

**TOGAF Content Framework Elements**:
- Technology Standards Catalog
- Technology Portfolio Catalog
- System/Technology Matrix

## Gap Analysis Coverage

**Template**: 0500_implementation_approach.md

**Gap Analysis Dimensions**:
- Business Architecture gaps
- Data Architecture gaps
- Application Architecture gaps
- Technology Architecture gaps

## Architecture Governance Coverage

**Templates**: 0030_governance_framework.md, 0600_migration_planning.md

**Governance Elements**:
- Architecture Board
- Architecture Compliance
- Architecture Contracts
- Dispensation Requests
- Compliance Assessments

## Completeness Assessment

### Fully Covered TOGAF Elements
- ✓ Preliminary Phase deliverables
- ✓ Architecture Vision (Phase A)
- ✓ Business Architecture (Phase B)
- ✓ Data Architecture (Phase C)
- ✓ Application Architecture (Phase C)
- ✓ Technology Architecture (Phase D)
- ✓ Opportunities and Solutions (Phase E)
- ✓ Migration Planning (Phase F)
- ✓ Requirements Management
- ✓ Architecture Governance

### Partially Covered TOGAF Elements
- ◐ Implementation Governance (Phase G) - Covered in migration planning template
- ◐ Architecture Change Management (Phase H) - Covered in migration planning template

### Optional Extensions
Organizations may add additional templates for:
- Detailed business process models
- Detailed data models
- Detailed application designs
- Detailed infrastructure designs
- Security architecture
- Integration architecture

## Usage Recommendations

1. **Start with Preliminary Phase**: Establish foundation before proceeding
2. **Follow ADM Sequence**: Progress through phases systematically
3. **Iterate as Needed**: ADM is iterative; revisit phases as requirements evolve
4. **Maintain Traceability**: Link requirements to architecture decisions
5. **Document Decisions**: Use Architecture Decision Records (ADRs)
6. **Engage Stakeholders**: Involve stakeholders throughout the process

## References

- TOGAF Standard, Version 9.2
- TOGAF Series Guide: Architecture Content Framework
- TOGAF Series Guide: Architecture Governance

*This mapping ensures that the template set provides comprehensive coverage of TOGAF ADM phases and deliverables.*

