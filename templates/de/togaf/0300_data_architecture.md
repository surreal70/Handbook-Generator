---
Document-ID: togaf-0300
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Daten-Architecture

## Zweck

Dieses Dokument beschreibt die Daten-Architecture für {{ source.organization_name }}, einschließlich Datenentitäten, Beziehungen, Lifecycle-Management und Governance.

## Geltungsbereich

- Datenentitäten und Beziehungen
- Daten-Lifecycle-Management
- Data Governance
- Datenqualität
- Datensicherheit und Datenschutz

## Datenentitäten

| Entität | Beschreibung | Eigentümer | Klassifizierung |
|---------|--------------|------------|-----------------|
| {{ source.entity_1 }} | {{ source.entity_1_desc }} | {{ source.entity_1_owner }} | {{ source.entity_1_class }} |
| {{ source.entity_2 }} | {{ source.entity_2_desc }} | {{ source.entity_2_owner }} | {{ source.entity_2_class }} |
| {{ source.entity_3 }} | {{ source.entity_3_desc }} | {{ source.entity_3_owner }} | {{ source.entity_3_class }} |

## Datenbeziehungen

{{ source.data_relationships }}

## Daten-Lifecycle

| Phase | Aktivitäten | Verantwortlich |
|-------|-------------|----------------|
| Erstellung | {{ source.creation_activities }} | {{ source.creation_responsible }} |
| Speicherung | {{ source.storage_activities }} | {{ source.storage_responsible }} |
| Nutzung | {{ source.usage_activities }} | {{ source.usage_responsible }} |
| Archivierung | {{ source.archival_activities }} | {{ source.archival_responsible }} |
| Löschung | {{ source.deletion_activities }} | {{ source.deletion_responsible }} |

## Data Governance

**Data Governance Framework**: {{ source.data_governance_framework }}

**Data Stewards**: {{ source.data_stewards }}

## Datenqualität

| Dimension | Ziel | Aktuell | Verbesserungsplan |
|-----------|------|---------|-------------------|
| Genauigkeit | {{ source.accuracy_target }} | {{ source.accuracy_current }} | {{ source.accuracy_plan }} |
| Vollständigkeit | {{ source.completeness_target }} | {{ source.completeness_current }} | {{ source.completeness_plan }} |
| Aktualität | {{ source.timeliness_target }} | {{ source.timeliness_current }} | {{ source.timeliness_plan }} |

<!-- Autorenhinweise: Daten-Architecture sollte Flexibilität und Kontrolle ausbalancieren -->

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|------|--------|---------|
| 0.1 | {{meta.document.last_updated}} | {{ meta.defaults.author }} | Initiale Erstellung |

<-  ( marked all subtasks complete End of template -->
