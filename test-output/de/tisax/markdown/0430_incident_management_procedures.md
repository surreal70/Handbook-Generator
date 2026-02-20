
Document-ID: tisax-0430

Status: Draft
Classification: Internal

# Incident Management Verfahren

**Dokument-ID:** TISAX-0430
**Organisation:** AdminSend GmbH
**Owner:** [TODO]
**Genehmigt durch:** [TODO]
**Revision:** [TODO]
**Author:** Handbook-Generator
**Status:** Draft
**Klassifizierung:** Internal
**Letzte Aktualisierung:** [TODO]
**Template Version:** [TODO]

---

---

## Zweck

Dieses Dokument beschreibt die Verfahren für Incident Management gemäß TISAX-Anforderungen.

## Geltungsbereich

Dieses Dokument gilt für alle Sicherheitsvorfälle in [TODO].

## Incident-Definitionen

### Incident-Kategorien

**Sicherheitsvorfälle:**
- Unbefugter Zugriff
- Malware-Infektionen
- Datenverlust/-diebstahl
- Denial of Service
- Insider-Bedrohungen

**Schweregrade:**
- **Kritisch**: Schwerwiegende Auswirkungen, sofortige Aktion erforderlich
- **Hoch**: Erhebliche Auswirkungen, schnelle Reaktion erforderlich
- **Mittel**: Spürbare Auswirkungen, zeitnahe Reaktion
- **Niedrig**: Geringe Auswirkungen, normale Bearbeitung

## Incident Response Prozess

### 1. Erkennung und Meldung

**Erkennungsquellen:**
- Monitoring-Systeme
- Mitarbeiter
- Kunden
- Partner
- Externe Meldungen

**Meldewege:**
- Incident Response Hotline: [TODO]
- E-Mail: [TODO]
- Ticket-System
- Eskalation an Vorgesetzten

### 2. Klassifizierung und Priorisierung

**Bewertungskriterien:**
- Auswirkung auf Geschäftsprozesse
- Anzahl betroffener Systeme/Benutzer
- Vertraulichkeit betroffener Daten
- Regulatorische Anforderungen

**Priorisierung:**
- Kritisch: Sofortige Bearbeitung
- Hoch: Innerhalb [TODO] Stunden
- Mittel: Innerhalb [TODO] Stunden
- Niedrig: Innerhalb [TODO] Tagen

### 3. Eindämmung

**Sofortmaßnahmen:**
- Isolation betroffener Systeme
- Sperrung kompromittierter Konten
- Blockierung schädlicher Aktivitäten
- Sicherung von Beweismitteln

**Kurzfristige Eindämmung:**
- Temporäre Workarounds
- Notfall-Patches
- Erhöhte Überwachung

**Langfristige Eindämmung:**
- Dauerhafte Lösungen
- System-Härtung
- Prozessverbesserungen

### 4. Untersuchung

**Aktivitäten:**
- Ursachenanalyse
- Umfangsbestimmung
- Beweissicherung
- Dokumentation

**Forensik:**
- Sicherung von Logs
- Speicherabbilder
- Netzwerkverkehr-Analyse
- Malware-Analyse

### 5. Beseitigung

**Maßnahmen:**
- Entfernung von Malware
- Schließung von Sicherheitslücken
- Wiederherstellung der Integrität
- Validierung der Beseitigung

### 6. Wiederherstellung

**Aktivitäten:**
- Wiederherstellung von Systemen
- Wiederherstellung von Daten
- Validierung der Funktionalität
- Überwachung auf Wiederauftreten

### 7. Nachbereitung

**Post-Incident Review:**
- Lessons Learned
- Prozessverbesserungen
- Aktualisierung von Dokumentation
- Schulungsbedarf

## Incident Response Team

### Rollen und Verantwortlichkeiten

**Incident Response Manager:**
- Koordination der Response
- Entscheidungsfindung
- Kommunikation mit Management
- Dokumentation

**Technische Analysten:**
- Technische Untersuchung
- Eindämmung und Beseitigung
- Forensische Analyse
- Wiederherstellung

**Kommunikationsverantwortlicher:**
- Interne Kommunikation
- Externe Kommunikation
- Stakeholder-Management
- Medienarbeit

**Rechtsbeistand:**
- Rechtliche Bewertung
- Compliance-Anforderungen
- Meldepflichten
- Vertragsrechtliche Aspekte

## Kommunikation

### Interne Kommunikation

**Stakeholder:**
- Management
- Betroffene Abteilungen
- IT-Team
- Datenschutzbeauftragter

**Kommunikationsplan:**
- Regelmäßige Updates
- Eskalationspfade
- Dokumentation

### Externe Kommunikation

**Meldepflichten:**
- Aufsichtsbehörden (z.B. Datenschutzbehörde)
- Betroffene Personen
- Kunden und Partner
- Strafverfolgungsbehörden

**Fristen:**
- DSGVO: 72 Stunden bei Datenschutzverletzungen
- TISAX: Gemäß vertraglichen Vereinbarungen
- Andere regulatorische Anforderungen

## Dokumentation

### Incident-Dokumentation

**Inhalte:**
- Incident-ID
- Zeitstempel
- Beschreibung
- Klassifizierung
- Betroffene Systeme/Daten
- Durchgeführte Maßnahmen
- Beteiligte Personen
- Ergebnisse

### Incident-Datenbank

**Zweck:**
- Nachverfolgung
- Trend-Analyse
- Reporting
- Lessons Learned

## TISAX-spezifische Anforderungen

### VDA ISA Kontrollen

Dieses Dokument adressiert:
- **9.1**: Incident Management Verfahren
- **9.2**: Incident Response

### Assessment-Nachweise

- Incident Response Plan
- Incident-Dokumentation
- Post-Incident Reviews
- Schulungsnachweise

## Kennzahlen

[TODO] misst:
- Anzahl Incidents nach Kategorie
- Durchschnittliche Reaktionszeit
- Durchschnittliche Lösungszeit
- Anzahl wiederkehrender Incidents

