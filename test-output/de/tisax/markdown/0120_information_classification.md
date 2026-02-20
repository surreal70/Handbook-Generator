
Document-ID: tisax-0120

Status: Draft
Classification: Internal

# Informationsklassifizierung

**Dokument-ID:** [FRAMEWORK]-0120
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

Dieses Dokument definiert das Klassifizierungsschema für Informationen und Assets sowie die damit verbundenen Schutzanforderungen gemäß TISAX-Anforderungen.

## Geltungsbereich

Dieses Dokument gilt für alle Informationen und Assets von [TODO], die klassifiziert werden müssen.

## Klassifizierungsschema

### Vertraulichkeitsstufen

[TODO] verwendet folgende Vertraulichkeitsstufen:

#### Stufe 1: Öffentlich

**Definition:**
- Informationen, die für die Öffentlichkeit bestimmt sind
- Keine negativen Auswirkungen bei Offenlegung

**Beispiele:**
- Öffentliche Pressemitteilungen
- Marketing-Materialien
- Veröffentlichte Produktinformationen
- Öffentliche Website-Inhalte

**Schutzanforderungen:**
- Keine besonderen Schutzmaßnahmen erforderlich
- Integritätsschutz zur Vermeidung von Manipulation

#### Stufe 2: Intern

**Definition:**
- Informationen für den internen Gebrauch
- Geringe negative Auswirkungen bei Offenlegung

**Beispiele:**
- Interne Mitteilungen
- Allgemeine Prozessdokumentation
- Organisationsstrukturen
- Interne Richtlinien

**Schutzanforderungen:**
- Zugriff nur für Mitarbeiter und autorisierte Dienstleister
- Grundlegende Zugriffskontrolle
- Keine Weitergabe an Dritte ohne Genehmigung

#### Stufe 3: Vertraulich

**Definition:**
- Sensible Geschäftsinformationen
- Erhebliche negative Auswirkungen bei Offenlegung

**Beispiele:**
- Geschäftspläne und Strategien
- Finanzinformationen
- Kundendaten
- Lieferantenverträge
- Technische Spezifikationen

**Schutzanforderungen:**
- Zugriff nur nach Need-to-Know-Prinzip
- Verschlüsselung bei Übertragung und Speicherung
- Vertraulichkeitsvereinbarungen (NDAs)
- Protokollierung von Zugriffen
- Sichere Entsorgung

#### Stufe 4: Streng Vertraulich

**Definition:**
- Höchst sensible Informationen
- Schwerwiegende negative Auswirkungen bei Offenlegung

**Beispiele:**
- Prototypen und Entwicklungsdaten
- Geschäftsgeheimnisse
- Strategische Partnerschaften
- Personenbezogene Daten besonderer Kategorien
- Sicherheitsrelevante Informationen

**Schutzanforderungen:**
- Strenge Zugriffskontrolle mit Genehmigungsprozess
- Starke Verschlüsselung (AES-256 oder höher)
- Multi-Faktor-Authentifizierung
- Umfassende Protokollierung und Überwachung
- Physische Sicherheitsmaßnahmen
- Sichere Vernichtung nach Aufbewahrungsfrist

### Integritätsstufen

Klassifizierung nach Integritätsanforderungen:

#### Niedrig
- Fehler haben geringe Auswirkungen
- Manuelle Korrektur möglich
- Beispiel: Interne Notizen

#### Mittel
- Fehler haben spürbare Auswirkungen
- Korrektur erfordert Aufwand
- Beispiel: Prozessdokumentation

#### Hoch
- Fehler haben erhebliche Auswirkungen
- Korrektur ist aufwändig oder kritisch
- Beispiel: Finanzdaten, Verträge

#### Sehr Hoch
- Fehler haben schwerwiegende Auswirkungen
- Korrektur ist sehr aufwändig oder unmöglich
- Beispiel: Produktionsdaten, Sicherheitskonfigurationen

### Verfügbarkeitsstufen

Klassifizierung nach Verfügbarkeitsanforderungen:

#### Niedrig
- Ausfall tolerierbar für mehrere Tage
- Keine zeitkritischen Prozesse betroffen
- Beispiel: Archivdaten

#### Mittel
- Ausfall tolerierbar für Stunden
- Beeinträchtigung von Geschäftsprozessen
- Beispiel: Interne Kommunikationssysteme

#### Hoch
- Ausfall tolerierbar für Minuten
- Erhebliche Beeinträchtigung von Geschäftsprozessen
- Beispiel: E-Mail-System, ERP-System

#### Kritisch
- Ausfall nicht tolerierbar
- Geschäftskritische Prozesse betroffen
- Beispiel: Produktionssysteme, Notfallsysteme

## Klassifizierungsprozess

### 1. Verantwortlichkeit

**Information Owner:**
- Verantwortlich für Klassifizierung
- Bestimmt Schutzbedarf
- Genehmigt Zugriffe
- Überprüft Klassifizierung regelmäßig

**Information Custodian:**
- Implementiert Schutzmaßnahmen
- Stellt technische Kontrollen bereit
- Überwacht Einhaltung

### 2. Klassifizierungskriterien

Bei der Klassifizierung werden berücksichtigt:

**Geschäftswert:**
- Strategische Bedeutung
- Finanzieller Wert
- Wettbewerbsrelevanz

**Regulatorische Anforderungen:**
- Gesetzliche Vorgaben (DSGVO, etc.)
- Vertragliche Verpflichtungen
- Branchenstandards (TISAX, ISO 27001)

**Schadensauswirkungen:**
- Finanzielle Schäden
- Reputationsschäden
- Rechtliche Konsequenzen
- Betriebliche Auswirkungen

### 3. Klassifizierungsverfahren

**Schritt 1: Identifikation**
- Information oder Asset identifizieren
- Information Owner bestimmen
- Kontext und Nutzung analysieren

**Schritt 2: Bewertung**
- Vertraulichkeit bewerten
- Integrität bewerten
- Verfügbarkeit bewerten
- Höchste Stufe bestimmt Gesamtklassifizierung

**Schritt 3: Dokumentation**
- Klassifizierung dokumentieren
- Begründung festhalten
- In Asset-Inventar eintragen

**Schritt 4: Kennzeichnung**
- Informationen entsprechend markieren
- Metadaten setzen
- Physische Kennzeichnung anbringen

**Schritt 5: Schutzmaßnahmen**
- Erforderliche Kontrollen implementieren
- Zugriffsberechtigung festlegen
- Technische Schutzmaßnahmen aktivieren

## Kennzeichnung von Informationen

### Elektronische Dokumente

Kennzeichnung in:
- Dokumenten-Header/Footer
- Datei-Metadaten
- E-Mail-Betreffzeilen
- Wasserzeichen

**Format:**
```
KLASSIFIZIERUNG: [STUFE]
Beispiel: KLASSIFIZIERUNG: VERTRAULICH
```

### Physische Dokumente

Kennzeichnung durch:
- Stempel oder Aufkleber
- Farbcodierung
- Spezielle Umschläge
- Sichtbare Markierung auf jeder Seite

### Digitale Assets

Kennzeichnung durch:
- Metadaten-Tags
- Dateinamenskonventionen
- Zugriffskontroll-Labels
- Verschlüsselungs-Flags

## Schutzmaßnahmen nach Klassifizierung

### Technische Maßnahmen

| Klassifizierung | Zugriffskontrolle | Verschlüsselung | Backup | Protokollierung |
|----------------|-------------------|-----------------|--------|-----------------|
| Öffentlich | Keine | Optional | Standard | Keine |
| Intern | Basis | Bei Übertragung | Standard | Basis |
| Vertraulich | Erweitert | Immer | Täglich | Erweitert |
| Streng Vertraulich | Streng | Stark (AES-256) | Mehrfach täglich | Umfassend |

### Organisatorische Maßnahmen

**Öffentlich:**
- Keine besonderen Maßnahmen

**Intern:**
- Mitarbeiter-Zugriff
- Grundlegende Awareness

**Vertraulich:**
- Need-to-Know-Prinzip
- NDAs erforderlich
- Schulung erforderlich
- Sichere Entsorgung

**Streng Vertraulich:**
- Genehmigungsprozess
- Spezielle NDAs
- Intensive Schulung
- Clean-Desk-Policy
- Überwachte Entsorgung

### Handhabungsrichtlinien

**Speicherung:**
- Öffentlich: Beliebig
- Intern: Genehmigte Systeme
- Vertraulich: Verschlüsselte Systeme
- Streng Vertraulich: Hochsichere, verschlüsselte Systeme

**Übertragung:**
- Öffentlich: Beliebig
- Intern: Interne Netzwerke
- Vertraulich: Verschlüsselte Kanäle
- Streng Vertraulich: Stark verschlüsselte, überwachte Kanäle

**Entsorgung:**
- Öffentlich: Normale Entsorgung
- Intern: Papierkorb/Löschen
- Vertraulich: Schreddern/Sichere Löschung
- Streng Vertraulich: Zertifizierte Vernichtung

## Deklassifizierung und Reklassifizierung

### Deklassifizierung

Informationen können deklassifiziert werden, wenn:
- Schutzbedarf entfällt
- Information wird öffentlich
- Aufbewahrungsfrist abgelaufen
- Geschäftswert gesunken

**Prozess:**
1. Antrag durch Information Owner
2. Prüfung durch Informationssicherheit
3. Genehmigung durch Management
4. Aktualisierung der Klassifizierung
5. Anpassung der Schutzmaßnahmen

### Reklassifizierung

Informationen müssen reklassifiziert werden, wenn:
- Schutzbedarf steigt
- Neue regulatorische Anforderungen
- Änderung des Geschäftswerts
- Sicherheitsvorfälle

**Prozess:**
1. Identifikation des Änderungsbedarfs
2. Neubewertung durch Information Owner
3. Dokumentation der Änderung
4. Implementierung erhöhter Schutzmaßnahmen
5. Information der Betroffenen

## Überprüfung und Wartung

### Regelmäßige Überprüfung

Klassifizierungen werden überprüft:
- **Jährlich**: Alle klassifizierten Informationen
- **Bei Änderungen**: Betroffene Informationen
- **Bei Incidents**: Involvierte Informationen
- **Auf Anfrage**: Ad-hoc Überprüfung

### Qualitätssicherung

[TODO] stellt sicher:
- Konsistente Anwendung des Schemas
- Angemessene Schutzmaßnahmen
- Aktualität der Klassifizierungen
- Compliance mit Anforderungen

## TISAX-spezifische Anforderungen

### VDA ISA Kontrollen

Dieses Dokument adressiert:

- **2.3.1**: Klassifizierung von Informationen
- **2.3.2**: Kennzeichnung von Informationen
- **2.3.3**: Handhabung von Assets

### Assessment-Nachweise

Für TISAX-Assessments:

- Klassifizierungsrichtlinie
- Klassifizierungsschema-Dokumentation
- Beispiele klassifizierter Informationen
- Schulungsnachweise
- Prozessbeschreibungen

## Schulung und Awareness

### Schulungsinhalte

Alle Mitarbeiter werden geschult zu:
- Klassifizierungsschema
- Kennzeichnungspflichten
- Handhabungsrichtlinien
- Verantwortlichkeiten
- Konsequenzen bei Verstößen

### Zielgruppen

- **Alle Mitarbeiter**: Basis-Schulung
- **Information Owner**: Erweiterte Schulung
- **IT-Personal**: Technische Schulung
- **Management**: Strategische Schulung

## Kennzahlen

[TODO] misst:

- Anteil klassifizierter Informationen (Ziel: 100%)
- Korrektheit der Klassifizierung (Stichproben)
- Einhaltung der Kennzeichnungspflicht (Ziel: >95%)
- Anzahl Reklassifizierungen
- Schulungsteilnahme (Ziel: 100%)



