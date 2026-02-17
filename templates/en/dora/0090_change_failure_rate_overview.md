
Document-ID: dora-0400

Status: Draft
Classification: Internal

# Change Failure Rate Overview

**Document-ID:** [FRAMEWORK]-0090
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

## Purpose

Description of the Change Failure Rate metric.

## Scope

- CFR definition
- Measurement methodology
- Current performance

## Definition

Change Failure Rate measures the percentage of deployments that result in service degradation and require remediation.

### Organization Context

- **Organization**: [TODO]
- **Current CFR**: [TODO]
- **Performance Level**: [TODO]

## Measurement Methodology

### Failure Definition

A deployment failure is:
- Rollback required
- Hotfix required
- Service degradation

### Calculation

```
CFR = (Number of failed deployments / Total deployments) * 100%
```

## Current Performance

### Overall Organization

- **CFR**: [TODO]
- **Performance Level**: [TODO]

### By Team

| Team | CFR | Performance Level |
|------|-----|-------------------|
| [TODO] | [TODO] | [TODO] |
| [TODO] | [TODO] | [TODO] |

<!-- Note: CFR is indicator of code quality and testing -->

<!-- End of template -->
