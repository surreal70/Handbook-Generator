---
Document-ID: tisax-0450
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Beweissicherung

## Zweck

Dieses Dokument beschreibt die Verfahren zur Beweissicherung bei Sicherheitsvorfällen gemäß TISAX-Anforderungen.

## Geltungsbereich

Dieses Dokument gilt für alle Sicherheitsvorfälle in {{ source.organization_name }}.

## Beweissicherungsprozess

### Identifikation

**Potenzielle Beweismittel:**
- Logs und Protokolle
- Speicherabbilder (RAM, Festplatten)
- Netzwerkverkehr
- E-Mails
- Dokumente
- Physische Medien

### Sicherung

**Methoden:**
- Forensische Kopien
- Hash-Werte zur Integritätssicherung
- Write-Blocker für physische Medien
- Dokumentation aller Schritte

### Chain of Custody

**Dokumentation:**
- Wer hat Beweismittel gesammelt
- Wann wurde gesammelt
- Wo wurde gesammelt
- Wie wurde gesammelt
- Übergaben und Zugriffe

### Aufbewahrung

**Anforderungen:**
- Sichere Speicherung
- Zugriffskontrolle
- Unveränderbarkeit
- Aufbewahrungsfristen

## Forensische Tools

### Zugelassene Tools

**Software:**
- {{ source.forensic_tool_1 }}
- {{ source.forensic_tool_2 }}
- Open-Source-Tools (validiert)

**Hardware:**
- Write-Blocker
- Forensische Workstations
- Speichermedien

## Rechtliche Aspekte

### Compliance

**Anforderungen:**
- Datenschutz beachten
- Rechtliche Zulässigkeit
- Dokumentation
- Beweiskraft

### Zusammenarbeit mit Behörden

**Bei Bedarf:**
- Strafverfolgungsbehörden
- Datenschutzbehörden
- Andere Aufsichtsbehörden

## TISAX-spezifische Anforderungen

### VDA ISA Kontrollen

Dieses Dokument adressiert:
- **9.3**: Sammlung von Beweismitteln

### Assessment-Nachweise

- Beweissicherungsprozess
- Chain of Custody Dokumentation
- Forensische Berichte

## Kennzahlen

{{ source.organization_name }} misst:
- Anzahl Beweissicherungen
- Vollständigkeit der Dokumentation
- Erfolgsrate bei rechtlichen Verfahren

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |

<!-- Ende des Templates -->
