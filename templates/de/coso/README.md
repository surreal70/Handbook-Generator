# COSO Internal Control Framework Handbuch

## Überblick

Dieses Handbuch bietet eine umfassende Dokumentation des internen Kontrollsystems basierend auf dem COSO Internal Control - Integrated Framework (2013). Das COSO Framework ist weltweit als führendes Framework für das Design, die Implementierung und die Bewertung interner Kontrollen anerkannt.

## Framework-Struktur

Das COSO Framework besteht aus:

- **5 Komponenten** der internen Kontrolle
- **17 Prinzipien** die die Komponenten unterstützen
- **Punkte der Fokussierung** (Points of Focus) für jedes Prinzip

### Die fünf Komponenten

1. **Kontrollumgebung** (Control Environment) - Die Grundlage für alle anderen Komponenten
2. **Risikobewertung** (Risk Assessment) - Identifikation und Analyse von Risiken
3. **Kontrollaktivitäten** (Control Activities) - Maßnahmen zur Risikominderung
4. **Information und Kommunikation** (Information and Communication) - Informationsfluss
5. **Überwachungsaktivitäten** (Monitoring Activities) - Laufende Bewertung der Wirksamkeit

## Template-Organisation

Die Templates sind nach Komponenten organisiert und verwenden ein numerisches Präfix-System:

### 0010-0099: Framework-Übersicht und Kontrollumgebung
- 0010: COSO Framework Übersicht
- 0020: Interne Kontrollziele
- 0030: Kontrollumgebung
- 0040: Integrität und ethische Werte (Prinzip 1)
- 0050: Board-Aufsicht und Unabhängigkeit (Prinzip 2)
- 0060: Organisationsstruktur und Verantwortlichkeiten (Prinzip 3)
- 0070: Kompetenz (Prinzip 4)
- 0080: Rechenschaftspflicht (Prinzip 5)

### 0100-0199: Risikobewertung
- 0100: Risikobewertung Übersicht
- 0110: Spezifikation der Ziele (Prinzip 6)
- 0120: Risikoidentifikation (Prinzip 7)
- 0130: Betrugsbewertung (Prinzip 8)
- 0140: Änderungsidentifikation (Prinzip 9)

### 0200-0299: Kontrollaktivitäten
- 0200: Kontrollaktivitäten Übersicht
- 0210: Auswahl und Entwicklung von Kontrollaktivitäten (Prinzip 10)
- 0220: Technologiekontrollen (Prinzip 11)
- 0230: Richtlinien und Verfahren (Prinzip 12)
- 0240: Funktionstrennung

### 0300-0399: Information und Kommunikation
- 0300: Information und Kommunikation Übersicht
- 0310: Informationsqualität (Prinzip 13)
- 0320: Interne Kommunikation (Prinzip 14)
- 0330: Externe Kommunikation (Prinzip 15)

### 0400-0499: Überwachungsaktivitäten
- 0400: Überwachungsaktivitäten Übersicht
- 0410: Laufende Bewertungen (Prinzip 16)
- 0420: Separate Bewertungen (Prinzip 16)
- 0430: Bewertung und Kommunikation von Mängeln (Prinzip 17)
- 0440: Kontinuierliche Verbesserung

### 0500-0599: Integration und Implementierung
- 0500: Integration über Komponenten hinweg
- 0510: Unternehmensweite Kontrollen (Entity-Level Controls)
- 0520: Prozessebene-Kontrollen (Process-Level Controls)
- 0530: Dokumentationsanforderungen
- 0540: Tests und Validierung

## Verwendung der Templates

### Anpassung

1. **Platzhalter ersetzen**: Ersetzen Sie alle `[TODO]` Platzhalter mit organisationsspezifischen Informationen
2. **Inhalte erweitern**: Fügen Sie zusätzliche Details hinzu, die für Ihre Organisation relevant sind
3. **Abschnitte anpassen**: Passen Sie Abschnitte an Ihre spezifischen Anforderungen an
4. **Diagramme hinzufügen**: Fügen Sie Diagramme im `diagrams/` Verzeichnis hinzu

### Platzhalter-Syntax

Templates verwenden die Syntax `[TODO]` für Platzhalter:

- `[TODO]` - Name der Organisation
- `[TODO]` - Autor des Dokuments
- `{{ meta-handbook.revision }}` - Versionsnummer
- `{{ meta-handbook.modifydate }}` - Datum
- Weitere organisationsspezifische Felder nach Bedarf

### Dokumenten-Header

Jedes Template enthält einen YAML-Header mit Metadaten:

```yaml
---
Document-ID: coso-NNNN
Owner: {{ meta-handbook.author }}
Version: {{ meta-handbook.revision }}
Status: Draft
Classification: Internal
Last Update: {{ meta-handbook.modifydate }}
---
```

## Wirksamkeitskriterien

Eine interne Kontrolle gilt als wirksam, wenn:

1. **Alle fünf Komponenten vorhanden und funktionsfähig sind**
2. **Alle 17 Prinzipien vorhanden und funktionsfähig sind**
3. **Die Komponenten zusammen integriert funktionieren**

## Integration mit anderen Frameworks

Das COSO Framework integriert sich mit:

- **COSO ERM** - Enterprise Risk Management
- **SOC 1 / SOC 2** - Service Organization Controls
- **Sarbanes-Oxley Act (SOX)** - Section 404 Compliance
- **ISO 31000** - Risikomanagement

## Referenzen

- COSO Internal Control - Integrated Framework (2013)
- COSO Enterprise Risk Management Framework
- Committee of Sponsoring Organizations of the Treadway Commission (www.coso.org)

## Unterstützung

Für Fragen zur Verwendung dieser Templates oder zum COSO Framework:

- Interne Revision
- Compliance-Abteilung
- Risikomanagement

## Versionierung

- **Version 1.0** - Initiale Template-Sammlung
- Aktualisierungen werden im Dokument-Header jedes Templates vermerkt
||-----|
| 0.1 | {{meta.document.last_updated}} | Initiale Erstellung |
