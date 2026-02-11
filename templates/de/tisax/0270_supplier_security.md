---
Document-ID: tisax-0400
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Lieferantensicherheit

## Zweck

Dieses Dokument beschreibt die Sicherheitsanforderungen für Lieferanten bei {{ source.organization_name }}.

## Lieferantenbewertung

### Auswahlkriterien
- Sicherheitszertifizierungen
- Datenschutz-Compliance
- Finanzielle Stabilität
- Referenzen

### Risikobewertung
- Kritikalität der Dienstleistung
- Zugriff auf sensible Daten
- Standort des Lieferanten

## Sicherheitsanforderungen

### Mindestanforderungen
- Informationssicherheitsrichtlinie
- Zugriffskontrolle
- Verschlüsselung
- Incident Management
- Business Continuity

### TISAX-Anforderungen
Lieferanten mit Zugriff auf vertrauliche Informationen müssen TISAX-zertifiziert sein:
- Assessment Level: {{ source.supplier_tisax_level }}

## Lieferantenregister

| Lieferant | Dienstleistung | Risikostufe | TISAX-Status |
|-----------|----------------|-------------|--------------|
| {{ source.supplier_1 }} | {{ source.supplier_1_service }} | {{ source.supplier_1_risk }} | {{ source.supplier_1_tisax }} |
| {{ source.supplier_2 }} | {{ source.supplier_2_service }} | {{ source.supplier_2_risk }} | {{ source.supplier_2_tisax }} |

<!-- Hinweis: Pflegen Sie das Lieferantenregister -->

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |

<!-- Ende des Templates -->
