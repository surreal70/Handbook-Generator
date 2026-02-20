
Document-ID: tisax-0350

Status: Draft
Classification: Internal

# Protokollierung und Überwachung

**Dokument-ID:** TISAX-0350
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

Dieses Dokument beschreibt die Anforderungen für Protokollierung und Überwachung gemäß TISAX-Anforderungen.

## Geltungsbereich

Dieses Dokument gilt für alle IT-Systeme von [TODO].

## Protokollierung

### Protokollierte Ereignisse

**Sicherheitsrelevant:**
- Anmeldungen (erfolgreich/fehlgeschlagen)
- Berechtigungsänderungen
- Zugriffe auf sensible Daten
- Administrative Aktionen
- Sicherheitsvorfälle

**Systemrelevant:**
- Systemstarts/-stops
- Fehler und Warnungen
- Konfigurationsänderungen
- Performance-Daten

### Log-Management

**Anforderungen:**
- Zentrale Log-Sammlung
- Sichere Speicherung
- Schutz vor Manipulation
- Aufbewahrung: [TODO] Tage

**SIEM-System:**
- [TODO]
- Korrelation von Ereignissen
- Automatische Alarmierung
- Reporting

## Überwachung

### Echtzeit-Monitoring

**Überwachte Systeme:**
- Server und Infrastruktur
- Netzwerkgeräte
- Anwendungen
- Sicherheitssysteme

**Metriken:**
- Verfügbarkeit
- Performance
- Sicherheitsereignisse
- Kapazität

### Alarmierung

**Schwellwerte:**
- Warnung: Potenzielle Probleme
- Kritisch: Sofortige Aktion erforderlich

**Eskalation:**
- Automatische Benachrichtigung
- Eskalationsstufen
- 24/7 Bereitschaft für kritische Systeme

## Log-Analyse

### Regelmäßige Überprüfung

**Täglich:**
- Sicherheitsereignisse
- Kritische Fehler
- Anomalien

**Wöchentlich:**
- Trend-Analysen
- Compliance-Checks
- Performance-Analysen

**Monatlich:**
- Umfassende Auswertung
- Reporting an Management
- Verbesserungsmaßnahmen

## TISAX-spezifische Anforderungen

### VDA ISA Kontrollen

Dieses Dokument adressiert:
- **6.5**: Protokollierung und Überwachung

### Assessment-Nachweise

- Logging-Konfiguration
- SIEM-Berichte
- Incident-Dokumentation

## Kennzahlen

[TODO] misst:
- Anzahl protokollierter Ereignisse
- Anzahl Sicherheitsvorfälle
- Durchschnittliche Reaktionszeit auf Alarme

