---
Document-ID: togaf-0700
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Requirements Management

## Purpose

This document describes the requirements management process for {{ source.organization_name }}, including requirements repository, traceability, and prioritization.

## Scope

- Requirements management process
- Requirements repository
- Requirements traceability
- Requirements prioritization

## Requirements Management Process

**Process Overview**: {{ source.requirements_process }}

**Process Steps**:
1. Requirements identification
2. Requirements analysis
3. Requirements documentation
4. Requirements validation
5. Requirements management

## Requirements Repository

**Repository Structure**:
- Business requirements
- Stakeholder requirements
- Architecture requirements
- Functional requirements
- Non-functional requirements

| Requirement ID | Type | Description | Priority | Status |
|----------------|------|-------------|----------|--------|
| {{ source.req_1_id }} | {{ source.req_1_type }} | {{ source.req_1_desc }} | {{ source.req_1_priority }} | {{ source.req_1_status }} |
| {{ source.req_2_id }} | {{ source.req_2_type }} | {{ source.req_2_desc }} | {{ source.req_2_priority }} | {{ source.req_2_status }} |
| {{ source.req_3_id }} | {{ source.req_3_type }} | {{ source.req_3_desc }} | {{ source.req_3_priority }} | {{ source.req_3_status }} |

## Requirements Traceability

**Traceability Matrix**:

| Requirement | Business Goal | Architecture Component | Implementation |
|-------------|---------------|------------------------|----------------|
| {{ source.trace_req_1 }} | {{ source.trace_goal_1 }} | {{ source.trace_component_1 }} | {{ source.trace_impl_1 }} |
| {{ source.trace_req_2 }} | {{ source.trace_goal_2 }} | {{ source.trace_component_2 }} | {{ source.trace_impl_2 }} |

## Requirements Prioritization

**Prioritization Criteria**:
- Business value
- Technical feasibility
- Risk
- Dependencies
- Cost

**Prioritization Method**: {{ source.prioritization_method }}

<!-- Author notes: Requirements management is continuous throughout the ADM cycle -->

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{meta.document.last_updated}} | {{ meta.defaults.author }} | Initial creation |

<-  ( marked all subtasks complete End of template -->
