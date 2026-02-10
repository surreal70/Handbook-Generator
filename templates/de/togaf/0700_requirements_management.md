---
Document-ID: togaf-0700
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Requirements Management

## Zweck

Dieses Dokument beschreibt den Requirements Management-Prozess für {{ source.organization_name }}, einschließlich Requirements Repository, Traceability und Priorisierung.

## Geltungsbereich

- Requirements Management-Prozess
- Requirements Repository
- Requirements Traceability
- Requirements Priorisierung

## Requirements Management-Prozess

**Prozessübersicht**: {{ source.requirements_process }}

**Prozessschritte**:
1. Requirements-Identifikation
2. Requirements-Analyse
3. Requirements-Dokumentation
4. Requirements-Validierung
5. Requirements-Management

## Requirements Repository

**Repository-Struktur**:
- Business Requirements
- Stakeholder Requirements
- Architecture Requirements
- Functional Requirements
- Non-Functional Requirements

| Requirement-ID | Typ | Beschreibung | Priorität | Status |
|----------------|-----|--------------|-----------|--------|
| {{ source.req_1_id }} | {{ source.req_1_type }} | {{ source.req_1_desc }} | {{ source.req_1_priority }} | {{ source.req_1_status }} |
| {{ source.req_2_id }} | {{ source.req_2_type }} | {{ source.req_2_desc }} | {{ source.req_2_priority }} | {{ source.req_2_status }} |
| {{ source.req_3_id }} | {{ source.req_3_type }} | {{ source.req_3_desc }} | {{ source.req_3_priority }} | {{ source.req_3_status }} |

## Requirements Traceability

**Traceability-Matrix**:

| Requirement | Business Goal | Architecture Component | Implementation |
|-------------|---------------|------------------------|----------------|
| {{ source.trace_req_1 }} | {{ source.trace_goal_1 }} | {{ source.trace_component_1 }} | {{ source.trace_impl_1 }} |
| {{ source.trace_req_2 }} | {{ source.trace_goal_2 }} | {{ source.trace_component_2 }} | {{ source.trace_impl_2 }} |

## Requirements Priorisierung

**Priorisierungskriterien**:
- Business Value
- Technische Machbarkeit
- Risiko
- Abhängigkeiten
- Kosten

**Priorisierungsmethode**: {{ source.prioritization_method }}

<!-- Autorenhinweise: Requirements Management ist kontinuierlich während des gesamten ADM-Zyklus -->

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial creation |

<-  ( marked all subtasks complete End of template -->
