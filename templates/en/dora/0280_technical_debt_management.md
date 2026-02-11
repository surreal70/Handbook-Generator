---
Document-ID: dora-0460
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Technical Debt Management

## Purpose

Description of technical debt management.

## Scope

- Technical debt definition
- Tracking and prioritization
- Reduction strategies

## Technical Debt Definition

### Types of Technical Debt

- **Code Debt**: Poor code quality, missing tests
- **Architecture Debt**: Outdated architecture decisions
- **Infrastructure Debt**: Outdated infrastructure, missing automation
- **Documentation Debt**: Missing or outdated documentation

### Current State

- **Estimated Technical Debt**: {{ source.estimated_technical_debt }}
- **Debt Ratio**: {{ source.debt_ratio }}

## Tracking and Prioritization

### Tracking Methods

- **Debt Backlog**: {{ source.debt_backlog_location }}
- **Debt Metrics**: {{ source.debt_metrics }}

### Prioritization

Criteria:
- Impact on delivery performance
- Risk level
- Effort to resolve

## Reduction Strategies

### Continuous Reduction

- **Debt Budget**: {{ source.debt_budget }}
- **Refactoring Time**: {{ source.refactoring_time_allocation }}

### Debt Reduction Goals

- **Short-term**: {{ source.debt_reduction_short_term }}
- **Long-term**: {{ source.debt_reduction_long_term }}

<!-- Note: Uncontrolled technical debt increases CFR -->

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Initial creation |

<!-- End of template -->
