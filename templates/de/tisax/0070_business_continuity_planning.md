---
Document-ID: tisax-0500
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Business Continuity Planning

## Zweck

Dieses Dokument beschreibt die Business-Continuity-Planung bei {{ source.organization_name }}.

## Business Impact Analysis

### Kritische Geschäftsprozesse

| Prozess | RTO | RPO | Auswirkung |
|---------|-----|-----|------------|
| {{ source.process_1 }} | {{ source.process_1_rto }} | {{ source.process_1_rpo }} | {{ source.process_1_impact }} |
| {{ source.process_2 }} | {{ source.process_2_rto }} | {{ source.process_2_rpo }} | {{ source.process_2_impact }} |

## BC-Strategien

### Präventive Maßnahmen
- Redundante Systeme
- Regelmäßige Backups
- Wartung und Updates

### Reaktive Maßnahmen
- Notfallpläne
- Ausweichstandorte
- Notfallteams

## BC-Organisation

**BC-Koordinator**: {{ source.bc_coordinator }}
**Notfallteam**: {{ source.emergency_team }}

## Tests und Übungen

- BC-Tests: {{ source.bc_test_frequency }}
- Tischübungen
- Vollständige Übungen

<!-- Hinweis: Testen Sie BC-Pläne regelmäßig -->

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |

<!-- Ende des Templates -->
