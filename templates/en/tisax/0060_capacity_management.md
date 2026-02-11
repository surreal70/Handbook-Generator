---
Document-ID: tisax-0320
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Capacity Management

## Purpose

This document describes capacity management at {{ source.organization_name }}.

## Monitoring

- CPU utilization
- Memory usage
- Network bandwidth
- Storage space

## Capacity Planning

**Planning Horizon**: {{ source.capacity_planning_horizon }}
**Review**: {{ source.capacity_review_frequency }}

## Thresholds

| Resource | Warning | Critical |
|----------|---------|----------|
| CPU | {{ source.cpu_warning_threshold }}% | {{ source.cpu_critical_threshold }}% |
| Memory | {{ source.memory_warning_threshold }}% | {{ source.memory_critical_threshold }}% |
| Disk | {{ source.disk_warning_threshold }}% | {{ source.disk_critical_threshold }}% |

<!-- Note: Adapt the thresholds -->

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Initial creation |

<!-- End of template -->
