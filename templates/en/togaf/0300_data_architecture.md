---
Document-ID: togaf-0300
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Data Architecture

## Purpose

This document describes the data architecture for {{ source.organization_name }}, including data entities, relationships, lifecycle management, and governance.

## Scope

- Data entities and relationships
- Data lifecycle management
- Data governance
- Data quality
- Data security and privacy

## Data Entities

| Entity | Description | Owner | Classification |
|--------|-------------|-------|----------------|
| {{ source.entity_1 }} | {{ source.entity_1_desc }} | {{ source.entity_1_owner }} | {{ source.entity_1_class }} |
| {{ source.entity_2 }} | {{ source.entity_2_desc }} | {{ source.entity_2_owner }} | {{ source.entity_2_class }} |
| {{ source.entity_3 }} | {{ source.entity_3_desc }} | {{ source.entity_3_owner }} | {{ source.entity_3_class }} |

## Data Relationships

{{ source.data_relationships }}

## Data Lifecycle

| Phase | Activities | Responsible |
|-------|------------|-------------|
| Creation | {{ source.creation_activities }} | {{ source.creation_responsible }} |
| Storage | {{ source.storage_activities }} | {{ source.storage_responsible }} |
| Usage | {{ source.usage_activities }} | {{ source.usage_responsible }} |
| Archival | {{ source.archival_activities }} | {{ source.archival_responsible }} |
| Deletion | {{ source.deletion_activities }} | {{ source.deletion_responsible }} |

## Data Governance

**Data Governance Framework**: {{ source.data_governance_framework }}

**Data Stewards**: {{ source.data_stewards }}

## Data Quality

| Dimension | Target | Current | Improvement Plan |
|-----------|--------|---------|------------------|
| Accuracy | {{ source.accuracy_target }} | {{ source.accuracy_current }} | {{ source.accuracy_plan }} |
| Completeness | {{ source.completeness_target }} | {{ source.completeness_current }} | {{ source.completeness_plan }} |
| Timeliness | {{ source.timeliness_target }} | {{ source.timeliness_current }} | {{ source.timeliness_plan }} |

<!-- Author notes: Data architecture should balance flexibility and control -->

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{meta.document.last_updated}} | {{ meta.defaults.author }} | Initial creation |

<-  ( marked all subtasks complete End of template -->
