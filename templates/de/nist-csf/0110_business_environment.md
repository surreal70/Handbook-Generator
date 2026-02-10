---
Document-ID: nist-csf-0110
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Geschäftsumfeld (ID.BE)

## Zweck

Dieses Dokument beschreibt das Geschäftsumfeld der Organisation, einschließlich Mission, Ziele, Stakeholder und Aktivitäten, um Cybersecurity-Entscheidungen zu informieren.

## Geltungsbereich

{{ meta.scope }}

## Geschäftsmission und -ziele

### Mission
{{ meta.organization_mission }}

### Strategische Ziele
1. {{ meta.strategic_goal_1 }}
2. {{ meta.strategic_goal_2 }}
3. {{ meta.strategic_goal_3 }}

## Kritische Geschäftsprozesse

| Prozess | Beschreibung | Kritikalität | Abhängigkeiten |
|---------|--------------|--------------|----------------|
| {{ meta.process_1 }} | {{ meta.process_1_desc }} | Hoch | {{ meta.process_1_deps }} |
| {{ meta.process_2 }} | {{ meta.process_2_desc }} | Hoch | {{ meta.process_2_deps }} |
| {{ meta.process_3 }} | {{ meta.process_3_desc }} | Mittel | {{ meta.process_3_deps }} |

## Stakeholder

### Interne Stakeholder
- Vorstand und Geschäftsführung
- Mitarbeiter
- IT-Abteilung
- Compliance und Legal

### Externe Stakeholder
- Kunden
- Partner
- Lieferanten
- Regulierungsbehörden

## Geschäftsabhängigkeiten

### IT-Systeme
- ERP-System: {{ meta.erp_system }}
- CRM-System: {{ meta.crm_system }}
- Produktionssysteme: {{ meta.production_systems }}

### Externe Dienste
- Cloud-Provider: {{ meta.cloud_provider }}
- Managed Services: {{ meta.managed_services }}
- Zahlungsdienstleister: {{ meta.payment_provider }}

## Dokumentenverweise

- 0020_organizational_context.md (Govern)
- 0100_asset_management.md
- 0130_risk_assessment.md

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | {{ meta.date }} | {{ meta.author }} | Initiale Erstellung |

<!-- Autor-Hinweise: Aktualisieren Sie bei Geschäftsänderungen -->
