---
Document-ID: dora-0330
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Incident-Response-Prozeduren

## Zweck

Beschreibung der Incident-Response-Prozesse.

## Umfang

- Response-Prozess
- Rollen und Verantwortlichkeiten
- Kommunikation

## Response-Prozess

### Phasen

1. **Detection**: Incident erkennen
2. **Triage**: Schweregrad bewerten
3. **Response**: Maßnahmen einleiten
4. **Resolution**: Problem lösen
5. **Recovery**: Service wiederherstellen
6. **Post-Mortem**: Analyse und Lernen

### Zeitvorgaben

- **Triage**: {{ source.triage_time_target }}
- **Initial Response**: {{ source.initial_response_time_target }}
- **Resolution**: {{ source.resolution_time_target }}

## Rollen und Verantwortlichkeiten

### Incident Commander

- **Verantwortlich**: {{ source.incident_commander_role }}
- **Aufgaben**: Koordination, Entscheidungen, Kommunikation

### Technical Lead

- **Verantwortlich**: {{ source.technical_lead_role }}
- **Aufgaben**: Technische Analyse, Lösungsfindung

### Communications Lead

- **Verantwortlich**: {{ source.communications_lead_role }}
- **Aufgaben**: Stakeholder-Kommunikation, Status-Updates

## Kommunikation

### Interne Kommunikation

- **Incident-Channel**: {{ source.incident_channel }}
- **Status-Updates**: {{ source.status_update_frequency }}

### Externe Kommunikation

- **Status-Page**: {{ source.status_page_url }}
- **Customer-Communication**: {{ source.customer_communication_process }}

<!-- Hinweis: Klare Prozesse reduzieren MTTR signifikant -->

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |

<!-- Ende des Templates -->
