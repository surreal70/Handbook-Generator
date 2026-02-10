---
Document-ID: togaf-0200
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Business Architecture Übersicht

## Zweck

Dieses Dokument bietet eine Übersicht über die Business Architecture von {{ source.organization_name }}, einschließlich Geschäftsfähigkeiten, Wertströme, Organisationsstruktur und Geschäftsprozesse.

## Geltungsbereich

- Business Capability Model
- Value Streams
- Organisationsstruktur
- Geschäftsprozesse
- Geschäftsfunktionen

## Business Capability Model

### Capability-Kategorien

| Kategorie | Beschreibung | Reifegrad | Strategische Bedeutung |
|-----------|--------------|-----------|------------------------|
| {{ source.capability_cat_1 }} | {{ source.capability_cat_1_desc }} | {{ source.capability_cat_1_maturity }} | {{ source.capability_cat_1_importance }} |
| {{ source.capability_cat_2 }} | {{ source.capability_cat_2_desc }} | {{ source.capability_cat_2_maturity }} | {{ source.capability_cat_2_importance }} |
| {{ source.capability_cat_3 }} | {{ source.capability_cat_3_desc }} | {{ source.capability_cat_3_maturity }} | {{ source.capability_cat_3_importance }} |

## Value Streams

### Value Stream 1: {{ source.value_stream_1_name }}

**Beschreibung**: {{ source.value_stream_1_description }}

**Stufen**:
1. {{ source.value_stream_1_stage_1 }}
2. {{ source.value_stream_1_stage_2 }}
3. {{ source.value_stream_1_stage_3 }}

**Beteiligte Capabilities**: {{ source.value_stream_1_capabilities }}

## Organisationsstruktur

{{ source.organization_structure }}

## Geschäftsprozesse

| Prozess | Eigentümer | Reifegrad | Automatisierungsgrad |
|---------|------------|-----------|----------------------|
| {{ source.process_1 }} | {{ source.process_1_owner }} | {{ source.process_1_maturity }} | {{ source.process_1_automation }} |
| {{ source.process_2 }} | {{ source.process_2_owner }} | {{ source.process_2_maturity }} | {{ source.process_2_automation }} |

<!-- Autorenhinweise: Aktualisieren Sie regelmäßig basierend auf Geschäftsänderungen -->

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial creation |

<-  ( marked all subtasks complete End of template -->
