---
Document-ID: tisax-0500
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Business Continuity Planning

## Purpose

This document describes business continuity planning at {{ source.organization_name }}.

## Business Impact Analysis

### Critical Business Processes

| Process | RTO | RPO | Impact |
|---------|-----|-----|--------|
| {{ source.process_1 }} | {{ source.process_1_rto }} | {{ source.process_1_rpo }} | {{ source.process_1_impact }} |
| {{ source.process_2 }} | {{ source.process_2_rto }} | {{ source.process_2_rpo }} | {{ source.process_2_impact }} |

## BC Strategies

### Preventive Measures
- Redundant systems
- Regular backups
- Maintenance and updates

### Reactive Measures
- Emergency plans
- Alternate sites
- Emergency teams

## BC Organization

**BC Coordinator**: {{ source.bc_coordinator }}
**Emergency Team**: {{ source.emergency_team }}

## Tests and Exercises

- BC tests: {{ source.bc_test_frequency }}
- Tabletop exercises
- Full exercises

<!-- Note: Test BC plans regularly -->

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Initial creation |

<!-- End of template -->
