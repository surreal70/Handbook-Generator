---
Document-ID: dora-0400
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Change Failure Rate Übersicht

## Zweck

Beschreibung der Change Failure Rate Metrik.

## Umfang

- CFR-Definition
- Messmethodik
- Aktuelle Performance

## Definition

Change Failure Rate misst den Prozentsatz der Deployments, die zu Service-Degradation führen und Remediation erfordern.

### Organisationskontext

- **Organisation**: {{ source.organization_name }}
- **Aktuelle CFR**: {{ source.current_cfr }}
- **Performance-Level**: {{ source.cfr_level }}

## Messmethodik

### Failure-Definition

Ein Deployment-Failure ist:
- Rollback erforderlich
- Hotfix erforderlich
- Service-Degradation

### Berechnung

```
CFR = (Anzahl fehlgeschlagener Deployments / Gesamtzahl Deployments) * 100%
```

## Aktuelle Performance

### Gesamtorganisation

- **CFR**: {{ source.org_cfr }}
- **Performance-Level**: {{ source.cfr_performance_level }}

### Nach Team

| Team | CFR | Performance-Level |
|------|-----|-------------------|
| {{ source.team_1_name }} | {{ source.team_1_cfr }} | {{ source.team_1_cfr_level }} |
| {{ source.team_2_name }} | {{ source.team_2_cfr }} | {{ source.team_2_cfr_level }} |

<!-- Hinweis: CFR ist Indikator für Code-Qualität und Testing -->

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |

<!-- Ende des Templates -->
