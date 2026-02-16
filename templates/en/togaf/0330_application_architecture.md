---
Document-ID: togaf-0330
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Application Architecture

## Purpose

This document describes the application architecture for {{ source.organization_name }}, including application portfolio, interfaces, and integration patterns.

## Scope

- Application portfolio
- Application interfaces
- Integration patterns
- Application lifecycle

## Application Portfolio

| Application | Category | Business Capability | Status | Strategic Value |
|-------------|----------|---------------------|--------|-----------------|
| {{ source.app_1 }} | {{ source.app_1_category }} | {{ source.app_1_capability }} | {{ source.app_1_status }} | {{ source.app_1_value }} |
| {{ source.app_2 }} | {{ source.app_2_category }} | {{ source.app_2_capability }} | {{ source.app_2_status }} | {{ source.app_2_value }} |
| {{ source.app_3 }} | {{ source.app_3_category }} | {{ source.app_3_capability }} | {{ source.app_3_status }} | {{ source.app_3_value }} |

## Application Interfaces

| Interface | Source | Target | Protocol | Data Format |
|-----------|--------|--------|----------|-------------|
| {{ source.interface_1 }} | {{ source.interface_1_source }} | {{ source.interface_1_target }} | {{ source.interface_1_protocol }} | {{ source.interface_1_format }} |
| {{ source.interface_2 }} | {{ source.interface_2_source }} | {{ source.interface_2_target }} | {{ source.interface_2_protocol }} | {{ source.interface_2_format }} |

## Integration Patterns

**Primary Integration Pattern**: {{ source.primary_integration_pattern }}

**Supported Patterns**:
- {{ source.pattern_1 }}
- {{ source.pattern_2 }}
- {{ source.pattern_3 }}

<!-- Author notes: Application architecture should support business agility -->

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{meta.document.last_updated}} | {{ meta.defaults.author }} | Initial creation |

<-  ( marked all subtasks complete End of template -->
