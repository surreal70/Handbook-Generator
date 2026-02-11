---
Document-ID: tisax-0420
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Lieferantenüberwachung

## Zweck

Dieses Dokument beschreibt die Überwachung von Lieferanten bei {{ source.organization_name }}.

## Überwachungsaktivitäten

### Regelmäßige Überprüfung
- Sicherheitsnachweise
- Zertifizierungen
- Incident-Berichte
- SLA-Compliance

### Audits
- Häufigkeit: {{ source.supplier_audit_frequency }}
- Vor-Ort-Audits bei kritischen Lieferanten
- Remote-Audits

## Performance-Messung

| KPI | Ziel | Aktuell |
|-----|------|---------|
| SLA-Einhaltung | {{ source.sla_target }}% | {{ source.sla_actual }}% |
| Incident-Response-Zeit | < {{ source.incident_response_target }} | {{ source.incident_response_actual }} |
| Verfügbarkeit | {{ source.availability_target }}% | {{ source.availability_actual }}% |

## Eskalation

Bei Nichteinhaltung:
1. Benachrichtigung des Lieferanten
2. Korrekturmaßnahmen
3. Eskalation an Management
4. Vertragskündigung (letztes Mittel)

<!-- Hinweis: Überwachen Sie Lieferanten kontinuierlich -->

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |

<!-- Ende des Templates -->
