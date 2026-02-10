---
Document-ID: togaf-0210
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Business Capability Model

## Zweck

Dieses Dokument definiert das Business Capability Model für {{ source.organization_name }}, das die Fähigkeiten beschreibt, die die Organisation benötigt, um ihre Geschäftsziele zu erreichen.

## Geltungsbereich

- Capability-Hierarchie
- Capability-Definitionen
- Reifegrad-Bewertung
- Capability-Roadmap

## Capability-Hierarchie

### Level 1 Capabilities

| Capability | Beschreibung | Strategische Bedeutung |
|------------|--------------|------------------------|
| {{ source.l1_cap_1 }} | {{ source.l1_cap_1_desc }} | {{ source.l1_cap_1_importance }} |
| {{ source.l1_cap_2 }} | {{ source.l1_cap_2_desc }} | {{ source.l1_cap_2_importance }} |
| {{ source.l1_cap_3 }} | {{ source.l1_cap_3_desc }} | {{ source.l1_cap_3_importance }} |

### Level 2 Capabilities

**{{ source.l1_cap_1 }}**:
- {{ source.l2_cap_1_1 }}
- {{ source.l2_cap_1_2 }}
- {{ source.l2_cap_1_3 }}

## Reifegrad-Bewertung

| Capability | Aktueller Reifegrad | Ziel-Reifegrad | Gap |
|------------|---------------------|----------------|-----|
| {{ source.cap_1 }} | {{ source.cap_1_current }} | {{ source.cap_1_target }} | {{ source.cap_1_gap }} |
| {{ source.cap_2 }} | {{ source.cap_2_current }} | {{ source.cap_2_target }} | {{ source.cap_2_gap }} |

## Capability-Roadmap

{{ source.capability_roadmap }}

<!-- Autorenhinweise: Capability Model sollte stabil aber anpassbar sein -->

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial creation |

<-  ( marked all subtasks complete End of template -->
