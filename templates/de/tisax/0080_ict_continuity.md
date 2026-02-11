---
Document-ID: tisax-0510
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# IKT-Kontinuität

## Zweck

Dieses Dokument beschreibt die IKT-Kontinuitätsmaßnahmen bei {{ source.organization_name }}.

## Kritische IT-Systeme

| System | Kritikalität | RTO | RPO | Wiederherstellungsstrategie |
|--------|--------------|-----|-----|----------------------------|
| {{ source.system_1 }} | {{ source.system_1_criticality }} | {{ source.system_1_rto }} | {{ source.system_1_rpo }} | {{ source.system_1_recovery }} |
| {{ source.system_2 }} | {{ source.system_2_criticality }} | {{ source.system_2_rto }} | {{ source.system_2_rpo }} | {{ source.system_2_recovery }} |

## Redundanz

- Redundante Server
- Redundante Netzwerkverbindungen
- Redundante Stromversorgung
- Redundante Datenspeicherung

## Disaster Recovery

**DR-Standort**: {{ source.dr_site }}
**Failover-Zeit**: {{ source.failover_time }}

## Wiederherstellungsprozess

1. Incident-Bewertung
2. Aktivierung des DR-Plans
3. Systemwiederherstellung
4. Datenwiederherstellung
5. Überprüfung
6. Rückkehr zum Normalbetrieb

<!-- Hinweis: Testen Sie DR-Prozesse -->

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |

<!-- Ende des Templates -->
