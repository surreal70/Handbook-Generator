---
Document-ID: dora-0300
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Mean Time to Restore (MTTR) Übersicht

## Zweck

Beschreibung der MTTR-Metrik und ihrer Bedeutung für Service-Stabilität.

## Umfang

- MTTR-Definition
- Messmethodik
- Aktuelle Performance
- Verbesserungsansätze

## Definition

MTTR misst die durchschnittliche Zeit zur Wiederherstellung des Service nach einem Incident oder Ausfall.

### Organisationskontext

- **Organisation**: {{ source.organization_name }}
- **Aktuelle MTTR**: {{ source.current_mttr }}
- **Performance-Level**: {{ source.mttr_level }}

## Messmethodik

### Incident-Definition

Ein Incident ist:
- Service-Degradation
- Service-Ausfall
- Kritischer Fehler in Produktion

### Zeiterfassung

- **Start**: Incident-Erkennung
- **Ende**: Service vollständig wiederhergestellt

### Datenquellen

- **Incident-Management**: {{ source.incident_management_system }}
- **Monitoring**: {{ source.monitoring_system }}
- **Alerting**: {{ source.alerting_system }}

## Aktuelle Performance

### Gesamtorganisation

- **Median MTTR**: {{ source.median_mttr }}
- **95th Percentile**: {{ source.p95_mttr }}
- **Performance-Level**: {{ source.mttr_performance_level }}

### Nach Service

| Service | Median MTTR | Performance-Level |
|---------|-------------|-------------------|
| {{ source.service_1_name }} | {{ source.service_1_mttr }} | {{ source.service_1_mttr_level }} |
| {{ source.service_2_name }} | {{ source.service_2_mttr }} | {{ source.service_2_mttr_level }} |
| {{ source.service_3_name }} | {{ source.service_3_mttr }} | {{ source.service_3_mttr_level }} |

## Verbesserungsansätze

### Kurzfristig

1. {{ source.mttr_short_term_1 }}
2. {{ source.mttr_short_term_2 }}

### Langfristig

1. {{ source.mttr_long_term_1 }}
2. {{ source.mttr_long_term_2 }}

<!-- Hinweis: MTTR ist Indikator für Resilienz und Recovery-Fähigkeit -->

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |

<!-- Ende des Templates -->
