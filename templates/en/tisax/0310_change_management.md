---
Document-ID: tisax-0310
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Change Management

## Purpose

This document describes the change management process according to TISAX requirements.

## Scope

This document applies to all changes to IT systems and infrastructure of {{ source.organization_name }}.

## Change Management Process

### Change Types
**Standard Changes:** Pre-approved, low risk
**Normal Changes:** Regular changes, CAB approval required
**Emergency Changes:** Urgent changes, shortened approval

### Change Process
1. Request for Change (RFC)
2. Assessment
3. Approval
4. Implementation
5. Review

## Change Advisory Board (CAB)

### Composition
- IT Manager (Chair)
- Representatives of affected departments
- Information Security Officer
- Technical experts

### Tasks
- Assessment of changes
- Approval or rejection
- Prioritization
- Monitoring of implementation

## Risk Management

### Risk Analysis
- Impact on business processes
- Technical complexity
- Dependencies
- Security risks

### Risk Mitigation
- Testing in test environment
- Rollback plan
- Backup before change
- Monitoring after implementation

## Documentation

### Change Documentation
- Change ID
- Description
- Justification
- Approvals
- Implementation details
- Results

### Change Calendar
- Planning of changes
- Avoidance of conflicts
- Communication
- Overview

## TISAX-Specific Requirements

### VDA ISA Controls
- **6.1**: Change management

### Assessment Evidence
- Change management process
- Change documentation
- CAB minutes
- Post-implementation reviews

## Metrics

{{ source.organization_name }} measures:
- Number of changes per month
- Success rate of changes
- Number of emergency changes
- Average lead time

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Initial creation |

<!-- End of template -->
