---
Document-ID: togaf-0330
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Anwendungs-Architecture

## Zweck

Dieses Dokument beschreibt die Anwendungs-Architecture für {{ source.organization_name }}, einschließlich Anwendungsportfolio, Schnittstellen und Integrationsmuster.

## Geltungsbereich

- Anwendungsportfolio
- Anwendungsschnittstellen
- Integrationsmuster
- Anwendungs-Lifecycle

## Anwendungsportfolio

| Anwendung | Kategorie | Geschäftsfähigkeit | Status | Strategischer Wert |
|-----------|-----------|-------------------|--------|-------------------|
| {{ source.app_1 }} | {{ source.app_1_category }} | {{ source.app_1_capability }} | {{ source.app_1_status }} | {{ source.app_1_value }} |
| {{ source.app_2 }} | {{ source.app_2_category }} | {{ source.app_2_capability }} | {{ source.app_2_status }} | {{ source.app_2_value }} |
| {{ source.app_3 }} | {{ source.app_3_category }} | {{ source.app_3_capability }} | {{ source.app_3_status }} | {{ source.app_3_value }} |

## Anwendungsschnittstellen

| Schnittstelle | Quelle | Ziel | Protokoll | Datenformat |
|---------------|--------|------|-----------|-------------|
| {{ source.interface_1 }} | {{ source.interface_1_source }} | {{ source.interface_1_target }} | {{ source.interface_1_protocol }} | {{ source.interface_1_format }} |
| {{ source.interface_2 }} | {{ source.interface_2_source }} | {{ source.interface_2_target }} | {{ source.interface_2_protocol }} | {{ source.interface_2_format }} |

## Integrationsmuster

**Primäres Integrationsmuster**: {{ source.primary_integration_pattern }}

**Unterstützte Muster**:
- {{ source.pattern_1 }}
- {{ source.pattern_2 }}
- {{ source.pattern_3 }}

<!-- Autorenhinweise: Anwendungs-Architecture sollte Business-Agilität unterstützen -->

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|------|--------|---------|
| 0.1 | {{meta.document.last_updated}} | {{ meta.defaults.author }} | Initiale Erstellung |

<-  ( marked all subtasks complete End of template -->
