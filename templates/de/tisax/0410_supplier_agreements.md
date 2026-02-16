---
Document-ID: tisax-0410
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Lieferantenvereinbarungen

## Zweck

Dieses Dokument beschreibt die Anforderungen für Vereinbarungen mit Lieferanten gemäß TISAX-Anforderungen.

## Geltungsbereich

Dieses Dokument gilt für alle Verträge mit Lieferanten von {{ source.organization_name }}.

## Vertragsbestandteile

### Sicherheitsanforderungen

**Obligatorische Klauseln:**
- Vertraulichkeitsvereinbarung
- Datenschutzvereinbarung
- Informationssicherheitsanforderungen
- Audit-Rechte
- Incident-Meldepflicht
- Subunternehmer-Regelungen

### Service Level Agreements

**Inhalte:**
- Verfügbarkeit: {{ source.sla_availability }}%
- Response Time: {{ source.sla_response_time }}
- Resolution Time: {{ source.sla_resolution_time }}
- Reporting-Anforderungen

### Haftung und Versicherung

**Anforderungen:**
- Haftungsobergrenzen
- Versicherungsnachweis
- Schadensersatzregelungen
- Vertragsstrafen bei Verstößen

## Datenschutz

### Auftragsverarbeitung

**Bei Verarbeitung personenbezogener Daten:**
- Auftragsverarbeitungsvertrag (AVV) gemäß DSGVO
- Technische und organisatorische Maßnahmen (TOMs)
- Weisungsbefugnis
- Löschpflichten

### Datenübermittlung

**Anforderungen:**
- Verschlüsselte Übertragung
- Dokumentation
- Empfangsbestätigung
- Löschung nach Vertragsende

## Compliance

### Zertifizierungen

**Erforderlich für kritische Lieferanten:**
- ISO 27001
- TISAX (für Automotive-Lieferanten)
- Branchenspezifische Zertifizierungen

### Audit-Rechte

**Regelungen:**
- Recht auf Audits
- Ankündigungsfrist
- Häufigkeit
- Kosten

## Vertragsmanagement

### Vertragslaufzeit

**Regelungen:**
- Laufzeit
- Kündigungsfristen
- Verlängerungsoptionen
- Ausstiegsklauseln

### Vertragsänderungen

**Prozess:**
- Schriftliche Änderungsanträge
- Bewertung der Auswirkungen
- Genehmigung
- Dokumentation

## Vertragsbeendigung

### Beendigung

**Gründe:**
- Vertragsablauf
- Kündigung
- Vertragsverletzung
- Insolvenz

**Prozess:**
1. Benachrichtigung
2. Übergabe/Rückgabe von Daten
3. Entzug von Zugriffen
4. Löschung von Daten
5. Abschlussdokumentation

## TISAX-spezifische Anforderungen

### VDA ISA Kontrollen

Dieses Dokument adressiert:
- **8.2**: Lieferantenvereinbarungen

### Assessment-Nachweise

- Musterverträge
- Aktuelle Verträge
- AVVs
- Audit-Berichte

## Kennzahlen

{{ source.organization_name }} misst:
- Anzahl aktiver Lieferantenverträge
- Compliance-Rate
- Anzahl Vertragsverletzungen

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |

<!-- Ende des Templates -->
