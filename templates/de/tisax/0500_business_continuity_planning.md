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

Dieses Dokument beschreibt die Business Continuity Planung gemäß TISAX-Anforderungen.

## Geltungsbereich

Dieses Dokument gilt für alle geschäftskritischen Prozesse von {{ source.organization_name }}.

## Business Impact Analysis

### Kritische Prozesse

**Identifikation:**
- Geschäftsprozesse bewerten
- Abhängigkeiten analysieren
- Kritikalität bestimmen
- Prioritäten festlegen

**Bewertungskriterien:**
- Finanzielle Auswirkungen
- Reputationsschäden
- Regulatorische Anforderungen
- Kundenzufriedenheit

### Recovery-Ziele

**RTO (Recovery Time Objective):**
- Kritische Prozesse: {{ source.critical_rto }} Stunden
- Wichtige Prozesse: {{ source.important_rto }} Stunden
- Standard-Prozesse: {{ source.standard_rto }} Tage

**RPO (Recovery Point Objective):**
- Kritische Daten: {{ source.critical_rpo }} Stunden
- Wichtige Daten: {{ source.important_rpo }} Stunden
- Standard-Daten: {{ source.standard_rpo }} Tage

## Business Continuity Strategie

### Präventive Maßnahmen

**Redundanz:**
- Redundante Systeme
- Redundante Standorte
- Redundante Personal
- Redundante Lieferanten

**Backup:**
- Regelmäßige Backups
- Offsite-Speicherung
- Getestete Wiederherstellung

### Reaktive Maßnahmen

**Notfallpläne:**
- Disaster Recovery Pläne
- Incident Response Pläne
- Kommunikationspläne
- Evakuierungspläne

## Business Continuity Pläne

### Plan-Struktur

**Inhalte:**
- Geltungsbereich
- Rollen und Verantwortlichkeiten
- Notfallkontakte
- Wiederherstellungsverfahren
- Kommunikationspläne
- Ressourcen

### Plan-Typen

**Nach Szenario:**
- IT-Ausfall
- Standortausfall
- Personalausfall
- Lieferantenausfall
- Cyberangriff
- Naturkatastrophe

## Notfallorganisation

### Krisenteam

**Zusammensetzung:**
- Krisenmanager
- Fachbereichsvertreter
- IT-Vertreter
- Kommunikationsverantwortlicher
- Weitere nach Bedarf

**Aufgaben:**
- Lagebeurteilung
- Entscheidungsfindung
- Koordination
- Kommunikation

### Kommunikation

**Intern:**
- Mitarbeiter
- Management
- Betriebsrat

**Extern:**
- Kunden
- Lieferanten
- Behörden
- Medien

## Testing und Übungen

### Test-Typen

**Desktop-Übungen:**
- Durchsprache der Pläne
- Identifikation von Lücken
- Regelmäßig (quartalsweise)

**Simulationen:**
- Realistische Szenarien
- Teilweise Aktivierung
- Halbjährlich

**Volltest:**
- Komplette Aktivierung
- Alle Prozesse
- Jährlich

### Nachbereitung

**Nach jedem Test:**
- Lessons Learned
- Aktualisierung der Pläne
- Schulungsbedarf
- Verbesserungsmaßnahmen

## Wartung und Aktualisierung

### Regelmäßige Überprüfung

**Jährlich:**
- Vollständige Überprüfung aller Pläne
- Aktualisierung von Kontakten
- Anpassung an Änderungen
- Management-Review

**Bei Änderungen:**
- Neue Systeme
- Organisationsänderungen
- Neue Risiken
- Lessons Learned

## TISAX-spezifische Anforderungen

### VDA ISA Kontrollen

Dieses Dokument adressiert:
- **10.1**: Business Continuity Planning

### Assessment-Nachweise

- Business Continuity Pläne
- Business Impact Analysis
- Test-Berichte
- Schulungsnachweise

## Kennzahlen

{{ source.organization_name }} misst:
- Anzahl durchgeführter Tests
- Erfolgsrate der Tests
- Aktualität der Pläne
- Schulungsteilnahme

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |

<!-- Ende des Templates -->
