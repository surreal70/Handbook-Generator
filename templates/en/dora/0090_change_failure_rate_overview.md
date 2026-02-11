---
Document-ID: dora-0400
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Change Failure Rate Overview

## Purpose

Description of the Change Failure Rate metric.

## Scope

- CFR definition
- Measurement methodology
- Current performance

## Definition

Change Failure Rate measures the percentage of deployments that result in service degradation and require remediation.

### Organization Context

- **Organization**: {{ source.organization_name }}
- **Current CFR**: {{ source.current_cfr }}
- **Performance Level**: {{ source.cfr_level }}

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

- **CFR**: {{ source.org_cfr }}
- **Performance Level**: {{ source.cfr_performance_level }}

### By Team

| Team | CFR | Performance Level |
|------|-----|-------------------|
| {{ source.team_1_name }} | {{ source.team_1_cfr }} | {{ source.team_1_cfr_level }} |
| {{ source.team_2_name }} | {{ source.team_2_cfr }} | {{ source.team_2_cfr_level }} |

<!-- Note: CFR is indicator of code quality and testing -->

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Initial creation |

<!-- End of template -->
