---
Document-ID: tisax-0310
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Change Management

## Zweck

Dieses Dokument beschreibt den Change Management Prozess gemäß TISAX-Anforderungen.

## Geltungsbereich

Dieses Dokument gilt für alle Änderungen an IT-Systemen und -Infrastruktur von {{ source.organization_name }}.

## Change Management Prozess

### Change-Typen

**Standard Changes:**
- Vorab genehmigte Änderungen
- Geringes Risiko
- Dokumentierte Verfahren
- Keine zusätzliche Genehmigung erforderlich

**Normal Changes:**
- Reguläre Änderungen
- Genehmigung durch Change Advisory Board
- Risk Assessment erforderlich
- Dokumentation und Testing

**Emergency Changes:**
- Dringende Änderungen
- Verkürzte Genehmigung
- Nachträgliche Dokumentation
- Post-Implementation Review

### Change-Prozess

**1. Request for Change (RFC):**
- Antragstellung mit Begründung
- Beschreibung der Änderung
- Risikoanalyse
- Rollback-Plan

**2. Bewertung:**
- Technische Bewertung
- Risikobewertung
- Impact-Analyse
- Ressourcenplanung

**3. Genehmigung:**
- Change Advisory Board (CAB)
- Genehmigungskriterien
- Dokumentation der Entscheidung

**4. Implementierung:**
- Geplante Durchführung
- Testing
- Dokumentation
- Kommunikation

**5. Review:**
- Post-Implementation Review
- Lessons Learned
- Dokumentation
- Prozessverbesserung

## Change Advisory Board (CAB)

### Zusammensetzung

**Mitglieder:**
- IT-Manager (Vorsitz)
- Vertreter betroffener Fachbereiche
- Informationssicherheitsbeauftragter
- Technische Experten

### Aufgaben

- Bewertung von Changes
- Genehmigung oder Ablehnung
- Priorisierung
- Überwachung der Implementierung

## Risikomanagement

### Risikoanalyse

**Bewertungskriterien:**
- Auswirkung auf Geschäftsprozesse
- Technische Komplexität
- Abhängigkeiten
- Sicherheitsrisiken

### Risikominimierung

**Maßnahmen:**
- Testing in Testumgebung
- Rollback-Plan
- Backup vor Änderung
- Überwachung nach Implementierung

## Dokumentation

### Change-Dokumentation

**Inhalte:**
- Change-ID
- Beschreibung
- Begründung
- Genehmigungen
- Implementierungsdetails
- Ergebnisse

### Change-Kalender

**Funktionen:**
- Planung von Changes
- Vermeidung von Konflikten
- Kommunikation
- Übersicht

## TISAX-spezifische Anforderungen

### VDA ISA Kontrollen

Dieses Dokument adressiert:
- **6.1**: Change Management

### Assessment-Nachweise

- Change Management Prozess
- Change-Dokumentation
- CAB-Protokolle
- Post-Implementation Reviews

## Kennzahlen

{{ source.organization_name }} misst:
- Anzahl Changes pro Monat
- Erfolgsrate von Changes
- Anzahl Emergency Changes
- Durchschnittliche Durchlaufzeit

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |

<!-- Ende des Templates -->
