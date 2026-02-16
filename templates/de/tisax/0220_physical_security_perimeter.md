---
Document-ID: tisax-0220
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Physische Sicherheitsperimeter

## Zweck

Dieses Dokument definiert die Anforderungen für physische Sicherheitsperimeter gemäß TISAX-Anforderungen.

## Geltungsbereich

Dieses Dokument gilt für alle Standorte und Einrichtungen von {{ source.organization_name }}.

## Sicherheitszonen

### Zoneneinteilung

**Zone 1: Öffentlicher Bereich**
- Empfang, Besucherbereiche
- Keine besonderen Schutzmaßnahmen
- Überwachung durch Empfangspersonal

**Zone 2: Allgemeiner Geschäftsbereich**
- Büros, Besprechungsräume
- Zutrittskontrolle für Mitarbeiter
- Besucherbegleitung erforderlich

**Zone 3: Eingeschränkter Bereich**
- Entwicklungsbereiche, Labore
- Erweiterte Zutrittskontrolle
- Protokollierung aller Zutritte

**Zone 4: Hochsicherheitsbereich**
- Rechenzentren, Serverräume
- Strenge Zutrittskontrolle
- Umfassende Überwachung

## Perimeterschutz

### Äußerer Perimeter

**Anforderungen:**
- Umzäunung des Geländes
- Kontrollierte Zugangspunkte
- Beleuchtung
- Videoüberwachung
- Regelmäßige Patrouillen

**Maßnahmen:**
- Zäune mit mindestens {{ source.fence_height }} Meter Höhe
- Automatische Tore mit Zutrittskontrolle
- Bewegungsmelder
- Alarmanlage

### Innerer Perimeter

**Anforderungen:**
- Abgrenzung sensibler Bereiche
- Zutrittskontrollsysteme
- Überwachung
- Alarmierung

**Maßnahmen:**
- Gesicherte Türen und Fenster
- Elektronische Zutrittskontrolle
- Videoüberwachung
- Einbruchmeldeanlage

## Zutrittskontrolle

### Mitarbeiter

**Anforderungen:**
- Personalisierte Zutrittskarten
- Berechtigungen nach Need-to-Know
- Regelmäßige Rezertifizierung
- Protokollierung

**Prozess:**
- Antrag durch Vorgesetzten
- Genehmigung durch Facility Management
- Ausgabe der Zutrittskarte
- Schulung vor Zugang zu sensiblen Bereichen

### Besucher

**Anforderungen:**
- Anmeldung im Voraus
- Identitätsprüfung
- Besucherausweis
- Begleitung durch Mitarbeiter
- Protokollierung

**Prozess:**
1. Voranmeldung durch Gastgeber
2. Registrierung am Empfang
3. Ausgabe Besucherausweis
4. Begleitung zu Zielbereichen
5. Rückgabe Ausweis bei Verlassen

### Externe Dienstleister

**Anforderungen:**
- Vertragliche Vereinbarung
- Sicherheitsüberprüfung
- Zeitlich begrenzte Zutritte
- Überwachung der Tätigkeiten

## Physische Sicherheitsmaßnahmen

### Türen und Fenster

**Anforderungen:**
- Einbruchhemmende Türen (RC2 oder höher)
- Gesicherte Fenster
- Automatische Verriegelung
- Alarmierung bei unbefugtem Öffnen

### Videoüberwachung

**Anforderungen:**
- Überwachung aller Zugangspunkte
- Aufzeichnung für mindestens {{ source.video_retention_days }} Tage
- Datenschutzkonforme Umsetzung
- Regelmäßige Überprüfung

### Alarmanlage

**Anforderungen:**
- Einbruchmeldeanlage
- Brandmeldeanlage
- Direkte Alarmierung von Sicherheitsdienst
- Regelmäßige Wartung und Tests

### Beleuchtung

**Anforderungen:**
- Ausreichende Beleuchtung aller Außenbereiche
- Notbeleuchtung
- Bewegungsgesteuerte Beleuchtung
- Regelmäßige Wartung

## Überwachung und Kontrolle

### Sicherheitsdienst

**Aufgaben:**
- Überwachung der Zugangspunkte
- Patrouillen
- Reaktion auf Alarme
- Besucherverwaltung

**Verfügbarkeit:**
- {{ source.security_service_hours }}
- Notfallkontakt 24/7

### Protokollierung

**Ereignisse:**
- Alle Zutritte
- Alarmauslösungen
- Sicherheitsvorfälle
- Wartungsarbeiten

### Audits

**Regelmäßig:**
- Monatliche Überprüfung der Zutrittsprotokolle
- Quartalsweise Sicherheitsaudits
- Jährliche Vollprüfung
- Ad-hoc bei Vorfällen

## TISAX-spezifische Anforderungen

### VDA ISA Kontrollen

Dieses Dokument adressiert:
- **5.1**: Physische Sicherheitsperimeter
- **5.2**: Physische Zutrittskontrollen

### Assessment-Nachweise

- Sicherheitskonzept
- Zutrittskontrollsystem-Dokumentation
- Audit-Berichte
- Sicherheitsvorfallsprotokolle

## Kennzahlen

{{ source.organization_name }} misst:
- Anzahl Sicherheitsvorfälle
- Anzahl unbefugter Zutrittsversuche
- Durchschnittliche Reaktionszeit auf Alarme
- Compliance-Rate bei Audits

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |

<!-- Ende des Templates -->
