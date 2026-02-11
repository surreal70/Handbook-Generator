---
Document-ID: tisax-0320
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Kapazitätsmanagement

## Zweck

Dieses Dokument beschreibt das Kapazitätsmanagement bei {{ source.organization_name }}.

## Überwachung

- CPU-Auslastung
- Speichernutzung
- Netzwerkbandbreite
- Speicherplatz

## Kapazitätsplanung

**Planungshorizont**: {{ source.capacity_planning_horizon }}
**Überprüfung**: {{ source.capacity_review_frequency }}

## Schwellenwerte

| Ressource | Warnung | Kritisch |
|-----------|---------|----------|
| CPU | {{ source.cpu_warning_threshold }}% | {{ source.cpu_critical_threshold }}% |
| Speicher | {{ source.memory_warning_threshold }}% | {{ source.memory_critical_threshold }}% |
| Festplatte | {{ source.disk_warning_threshold }}% | {{ source.disk_critical_threshold }}% |

<!-- Hinweis: Passen Sie die Schwellenwerte an -->

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |

<!-- Ende des Templates -->
