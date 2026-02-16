---
Document-ID: tisax-0230
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Physische Zutrittskontrolle

## Zweck

Dieses Dokument beschreibt die Maßnahmen zur physischen Zutrittskontrolle gemäß TISAX-Anforderungen.

## Geltungsbereich

Dieses Dokument gilt für alle kontrollierten Bereiche von {{ source.organization_name }}.

## Zutrittskontrollsysteme

### Elektronische Zutrittskontrolle

**Komponenten:**
- Kartenlesegeräte
- Biometrische Scanner
- PIN-Pads
- Zentrale Verwaltungssoftware

**Anforderungen:**
- Personalisierte Zutrittskarten
- Verschlüsselte Kommunikation
- Audit-Logging
- Redundante Stromversorgung

### Mechanische Sicherung

**Maßnahmen:**
- Hochsicherheitsschlösser
- Schließanlagen
- Schlüsselverwaltung
- Notfallzugang

## Zutrittsberechtigungen

### Berechtigungsvergabe

**Prozess:**
1. Antrag durch Vorgesetzten
2. Genehmigung durch Facility Management
3. Konfiguration im System
4. Ausgabe der Zutrittsmittel
5. Schulung des Mitarbeiters

**Kriterien:**
- Geschäftliche Notwendigkeit
- Need-to-Know-Prinzip
- Zeitliche Befristung
- Regelmäßige Überprüfung

### Berechtigungsentzug

**Gründe:**
- Austritt
- Rollenwechsel
- Ablauf der Befristung
- Sicherheitsvorfall

**Prozess:**
- Sofortige Deaktivierung im System
- Rückgabe der Zutrittsmittel
- Dokumentation
- Überprüfung der Vollständigkeit

## Besucherverwaltung

### Besucheranmeldung

**Prozess:**
1. Voranmeldung durch Gastgeber
2. Identitätsprüfung am Empfang
3. Ausgabe Besucherausweis
4. Einweisung in Sicherheitsregeln
5. Begleitung durch Mitarbeiter

**Dokumentation:**
- Name und Firma
- Besuchszweck
- Gastgeber
- Besuchsdauer
- Unterschrift

### Besucherbegleitung

**Anforderungen:**
- Ständige Begleitung in sensiblen Bereichen
- Sichtbarer Besucherausweis
- Keine unbeaufsichtigten Zugriffe
- Protokollierung der besuchten Bereiche

## Überwachung

### Protokollierung

**Ereignisse:**
- Erfolgreiche Zutritte
- Fehlgeschlagene Zutrittsversuche
- Türöffnungen außerhalb der Geschäftszeiten
- Alarmauslösungen

**Aufbewahrung:**
- Mindestens {{ source.access_log_retention_days }} Tage
- Regelmäßige Überprüfung
- Datenschutzkonforme Speicherung

### Monitoring

**Echtzeit-Überwachung:**
- Unberechtigte Zutrittsversuche
- Türen länger als {{ source.door_open_timeout }} Sekunden offen
- Zutritte außerhalb der Geschäftszeiten
- Mehrfache Kartennutzung (Tailgating-Erkennung)

## TISAX-spezifische Anforderungen

### VDA ISA Kontrollen

Dieses Dokument adressiert:
- **5.2**: Physische Zutrittskontrollen

### Assessment-Nachweise

- Zutrittskontrollsystem-Dokumentation
- Berechtigungskonzept
- Zutrittsprotokolle
- Besucherlisten

## Kennzahlen

{{ source.organization_name }} misst:
- Anzahl aktiver Zutrittsberechtigungen
- Anzahl fehlgeschlagener Zutrittsversuche
- Anzahl Besucher pro Monat
- Compliance-Rate bei Audits

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |

<!-- Ende des Templates -->
