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

Dieses Dokument beschreibt das Kapazitätsmanagement gemäß TISAX-Anforderungen.

## Geltungsbereich

Dieses Dokument gilt für alle IT-Ressourcen von {{ source.organization_name }}.

## Kapazitätsplanung

### Überwachung

**Ressourcen:**
- CPU-Auslastung
- Speicherauslastung
- Netzwerkbandbreite
- Speicherplatz

**Schwellwerte:**
- Warnung bei {{ source.capacity_warning_threshold }}%
- Kritisch bei {{ source.capacity_critical_threshold }}%

### Prognose

**Methoden:**
- Trendanalyse
- Wachstumsprognosen
- Saisonale Muster
- Geschäftsentwicklung

### Maßnahmen

**Bei Kapazitätsengpässen:**
- Ressourcenerweiterung
- Optimierung
- Lastverteilung
- Priorisierung

## TISAX-spezifische Anforderungen

### VDA ISA Kontrollen

Dieses Dokument adressiert:
- **6.2**: Kapazitätsmanagement

### Assessment-Nachweise

- Kapazitätsberichte
- Überwachungsdaten
- Maßnahmenpläne

## Kennzahlen

{{ source.organization_name }} misst:
- Durchschnittliche Ressourcenauslastung
- Anzahl Kapazitätsengpässe
- Reaktionszeit auf Engpässe

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |

<!-- Ende des Templates -->
