# Anforderungsdokument

## Einführung

Dieses Dokument beschreibt die Anforderungen für einen Handbuch-Generator, der aus Markdown-Vorlagen professionelle Handbücher erstellt. Das System soll Platzhalter in Vorlagen durch echte Daten aus externen Systemen (wie NetBox) ersetzen und mehrsprachige Handbücher in verschiedenen Formaten (Markdown, PDF) generieren. Der Generator unterstützt verschiedene Handbuchtypen (Backup, BCM, ISMS, IT-Operation) und ermöglicht die Erstellung standardisierter, datenangereicherter Dokumentation.

## Glossar

- **Handbuch-Generator**: Das System, das aus Vorlagen angereicherte Handbücher erstellt
- **Vorlage**: Eine Markdown-Datei mit Platzhaltern, die durch echte Daten ersetzt werden
- **Platzhalter**: Markierungen im Format "{{ quelle.feld }}", die durch echte Daten ersetzt werden
- **Datenquelle**: Externes System, das Daten für Platzhalter bereitstellt (z.B. NetBox)
- **Content-Vorlage**: Vorlage mit führender 4-stelliger Nummer für Sortierung (z.B. "0100_einleitung.md")
- **Metadaten-Vorlage**: Vorlage mit Erstellungsdatum, Autoren und Versionsnummer (Format: "0000_metadata_[sprache]_[vorlagenname].md")
- **Vorlagenverzeichnis**: Strukturiertes Verzeichnis mit Vorlagen nach Sprache und Handbuchtyp organisiert
- **Ausgabeverzeichnis**: Das "Handbook"-Verzeichnis, in dem generierte Handbücher gespeichert werden
- **NetBox**: IP-Adress- und Datencenter-Infrastruktur-Management-System als primäre Datenquelle
- **API-Schlüssel**: Authentifizierungstoken für den Zugriff auf externe Datenquellen
- **Konfigurationsdatei**: Datei mit Zugangsdaten und Einstellungen, die von Git ausgeschlossen ist

## Anforderungen

### Anforderung 1

**User Story:** Als Benutzer möchte ich beim Start des Generators eine Übersicht verfügbarer Vorlagen sehen, damit ich die gewünschte Vorlage und Sprache auswählen kann.

#### Akzeptanzkriterien

1. WHEN der Handbuch-Generator gestartet wird THEN das System SHALL alle verfügbaren Vorlagenverzeichnisse scannen
2. WHEN Vorlagen gescannt werden THEN das System SHALL verfügbare Sprachen (de, en) identifizieren
3. WHEN Sprachen identifiziert sind THEN das System SHALL verfügbare Handbuchtypen pro Sprache auflisten (backup, bcm, isms, it-operation)
4. WHEN keine Vorlagen gefunden werden THEN das System SHALL eine Fehlermeldung ausgeben und die erwartete Verzeichnisstruktur beschreiben
5. WHEN Vorlagen gefunden werden THEN das System SHALL die Anzahl der Content-Vorlagen und Metadaten-Vorlagen pro Typ anzeigen

### Anforderung 2

**User Story:** Als Benutzer möchte ich über Kommandozeilenparameter Sprache und Vorlagentyp auswählen, damit ich den Generierungsprozess automatisieren kann.

#### Akzeptanzkriterien

1. WHEN der Generator mit --language Parameter aufgerufen wird THEN das System SHALL die angegebene Sprache verwenden
2. WHEN der Generator mit --template Parameter aufgerufen wird THEN das System SHALL den angegebenen Handbuchtyp verwenden
3. WHEN ungültige Parameter übergeben werden THEN das System SHALL eine Fehlermeldung mit verfügbaren Optionen ausgeben
4. WHEN keine Parameter übergeben werden THEN das System SHALL interaktiv nach Sprache und Vorlagentyp fragen
5. WHEN Parameter validiert werden THEN das System SHALL prüfen, ob die Kombination aus Sprache und Vorlagentyp existiert

### Anforderung 3

**User Story:** Als Entwickler möchte ich, dass das System Platzhalter in Vorlagen erkennt und validiert, damit fehlerhafte Vorlagen frühzeitig erkannt werden.

#### Akzeptanzkriterien

1. WHEN eine Vorlage gelesen wird THEN das System SHALL alle Platzhalter im Format "{{ quelle.feld }}" identifizieren
2. WHEN ein Platzhalter erkannt wird THEN das System SHALL prüfen, dass er die einzige Anweisung in seiner Zeile ist
3. WHEN ein Platzhalter ungültig formatiert ist THEN das System SHALL eine Warnung mit Dateiname und Zeilennummer ausgeben
4. WHEN Platzhalter geparst werden THEN das System SHALL Quelle und Feld extrahieren (z.B. "netbox.device_name" → Quelle: "netbox", Feld: "device_name")
5. WHEN eine Vorlage keine Platzhalter enthält THEN das System SHALL die Vorlage unverändert in die Ausgabe übernehmen

### Anforderung 4

**User Story:** Als Benutzer möchte ich, dass Platzhalter durch echte Daten aus NetBox ersetzt werden, damit die Handbücher aktuelle Infrastrukturdaten enthalten.

#### Akzeptanzkriterien

1. WHEN ein Platzhalter mit Quelle "netbox" erkannt wird THEN das System SHALL eine Verbindung zur NetBox-API herstellen
2. WHEN die NetBox-Verbindung hergestellt wird THEN das System SHALL den API-Schlüssel aus der Konfigurationsdatei verwenden
3. WHEN Daten von NetBox abgerufen werden THEN das System SHALL das angeforderte Feld aus der API-Antwort extrahieren
4. WHEN ein Feld nicht gefunden wird THEN das System SHALL eine Warnung ausgeben und den Platzhalter unverändert lassen
5. WHEN Daten erfolgreich abgerufen werden THEN das System SHALL den Platzhalter durch den echten Wert ersetzen

### Anforderung 5

**User Story:** Als Administrator möchte ich Zugangsdaten sicher in einer Konfigurationsdatei speichern, damit sensible Informationen nicht im Code oder Repository landen.

#### Akzeptanzkriterien

1. WHEN der Generator startet THEN das System SHALL nach einer Konfigurationsdatei im Projektverzeichnis suchen
2. WHEN keine Konfigurationsdatei existiert THEN das System SHALL eine Beispiel-Konfigurationsdatei erstellen und den Benutzer informieren
3. WHEN die Konfigurationsdatei gelesen wird THEN das System SHALL NetBox-URL und API-Schlüssel extrahieren
4. WHEN die Konfigurationsdatei erstellt wird THEN das System SHALL sicherstellen, dass sie in .gitignore eingetragen ist
5. WHEN Zugangsdaten fehlen oder ungültig sind THEN das System SHALL eine aussagekräftige Fehlermeldung ausgeben

### Anforderung 6

**User Story:** Als Benutzer möchte ich Content-Vorlagen in der richtigen Reihenfolge verarbeitet haben, damit das generierte Handbuch logisch strukturiert ist.

#### Akzeptanzkriterien

1. WHEN Content-Vorlagen verarbeitet werden THEN das System SHALL diese nach der führenden 4-stelligen Nummer sortieren
2. WHEN Vorlagen sortiert sind THEN das System SHALL sie in aufsteigender Reihenfolge verarbeiten (0100, 0200, 0300, etc.)
3. WHEN eine Vorlage keine führende Nummer hat THEN das System SHALL eine Warnung ausgeben und die Vorlage ans Ende setzen
4. WHEN Metadaten-Vorlagen erkannt werden THEN das System SHALL diese als erste Seite des Handbuchs verarbeiten
5. WHEN die Verarbeitung abgeschlossen ist THEN das System SHALL die Dokumente in der sortierten Reihenfolge zusammenfügen

### Anforderung 7

**User Story:** Als Benutzer möchte ich Metadaten-Vorlagen mit Erstellungsdatum, Autoren und Versionsnummer verarbeiten, damit jedes Handbuch korrekt identifiziert werden kann.

#### Akzeptanzkriterien

1. WHEN eine Metadaten-Vorlage erkannt wird THEN das System SHALL das Format "0000_metadata_[sprache]_[vorlagenname].md" validieren
2. WHEN Metadaten verarbeitet werden THEN das System SHALL das aktuelle Datum im ISO-Format (YYYY-MM-DD) einfügen
3. WHEN Autoreninformationen hinzugefügt werden THEN das System SHALL "Andreas Huemmer [andreas.huemmer@adminsend.de]" als Standard verwenden
4. WHEN Versionsnummern verarbeitet werden THEN das System SHALL die Version aus der Konfiguration oder "1.0.0" als Standard verwenden
5. WHEN die Metadaten-Vorlage verarbeitet ist THEN das System SHALL sie als erste Seite der Ausgabe platzieren

### Anforderung 8

**User Story:** Als Benutzer möchte ich Handbücher im Markdown-Format ausgeben, damit ich die Dateien weiter bearbeiten oder versionieren kann.

#### Akzeptanzkriterien

1. WHEN die Markdown-Ausgabe gewählt wird THEN das System SHALL alle verarbeiteten Vorlagen in einer einzigen .md-Datei zusammenfügen
2. WHEN Markdown generiert wird THEN das System SHALL die Ausgabedatei im "Handbook"-Verzeichnis speichern
3. WHEN die Ausgabestruktur erstellt wird THEN das System SHALL die Vorlagenstruktur spiegeln (Sprache/Handbuchtyp)
4. WHEN eine Ausgabedatei bereits existiert THEN das System SHALL den Benutzer warnen und Überschreiben bestätigen lassen
5. WHEN die Markdown-Datei erstellt wird THEN das System SHALL gültige Markdown-Syntax und Formatierung sicherstellen

### Anforderung 9

**User Story:** Als Benutzer möchte ich Handbücher im PDF-Format ausgeben, damit ich druckfertige Dokumente erhalte.

#### Akzeptanzkriterien

1. WHEN die PDF-Ausgabe gewählt wird THEN das System SHALL die verarbeiteten Vorlagen in eine PDF-Datei konvertieren
2. WHEN PDF generiert wird THEN das System SHALL die Ausgabedatei im "Handbook"-Verzeichnis speichern
3. WHEN die PDF erstellt wird THEN das System SHALL die Metadaten-Vorlage als erste Seite rendern
4. WHEN Content-Vorlagen in PDF konvertiert werden THEN das System SHALL Markdown-Formatierung korrekt in PDF-Layout übertragen
5. WHEN die PDF-Generierung fehlschlägt THEN das System SHALL eine aussagekräftige Fehlermeldung mit Details ausgeben

### Anforderung 10

**User Story:** Als Benutzer möchte ich verschiedene Logging-Level verwenden, damit ich die Ausgabe an meine Bedürfnisse anpassen kann.

#### Akzeptanzkriterien

1. WHEN der Generator im normalen Modus läuft THEN das System SHALL verarbeitete Dokumente und Statistiken ausgeben
2. WHEN Statistiken ausgegeben werden THEN das System SHALL Anzahl der Dokumente, Handbuchgröße und Wortanzahl anzeigen
3. WHEN der Generator im verbose Modus läuft THEN das System SHALL zusätzlich Details zu Platzhalter-Ersetzungen ausgeben
4. WHEN Platzhalter ersetzt werden THEN das System SHALL im verbose Modus anzeigen, welcher Platzhalter durch welchen Inhalt ersetzt wurde
5. WHEN Fehler oder Warnungen auftreten THEN das System SHALL im verbose Modus erweiterte Fehlerinformationen ausgeben

### Anforderung 11

**User Story:** Als Entwickler möchte ich das System erweiterbar gestalten, damit zukünftig weitere Datenquellen neben NetBox integriert werden können.

#### Akzeptanzkriterien

1. WHEN eine neue Datenquelle hinzugefügt wird THEN das System SHALL eine einheitliche Schnittstelle für Datenquellen verwenden
2. WHEN Platzhalter verarbeitet werden THEN das System SHALL die Quelle dynamisch identifizieren und den entsprechenden Adapter verwenden
3. WHEN eine unbekannte Quelle erkannt wird THEN das System SHALL eine Warnung ausgeben und verfügbare Quellen auflisten
4. WHEN Datenquellen-Adapter implementiert werden THEN das System SHALL Fehlerbehandlung und Retry-Logik einheitlich handhaben
5. WHEN die Konfigurationsdatei gelesen wird THEN das System SHALL Zugangsdaten für mehrere Datenquellen unterstützen

### Anforderung 12

**User Story:** Als Benutzer möchte ich aussagekräftige Fehlermeldungen erhalten, damit ich Probleme schnell identifizieren und beheben kann.

#### Akzeptanzkriterien

1. WHEN ein Fehler auftritt THEN das System SHALL eine klare Fehlermeldung mit Kontext ausgeben
2. WHEN Vorlagen nicht gefunden werden THEN das System SHALL den erwarteten Pfad und verfügbare Alternativen anzeigen
3. WHEN API-Verbindungen fehlschlagen THEN das System SHALL URL, Statuscode und Fehlermeldung ausgeben
4. WHEN Platzhalter nicht ersetzt werden können THEN das System SHALL Dateiname, Zeilennummer und Platzhalter anzeigen
5. WHEN die Verarbeitung abgeschlossen ist THEN das System SHALL eine Zusammenfassung aller Fehler und Warnungen ausgeben

### Anforderung 13

**User Story:** Als Benutzer möchte ich, dass das System die Vorlagenstruktur mit Beispielen unterstützt, damit ich Referenzvorlagen für neue Handbücher habe.

#### Akzeptanzkriterien

1. WHEN das Vorlagenverzeichnis gescannt wird THEN das System SHALL das "examples"-Unterverzeichnis erkennen
2. WHEN Beispielvorlagen vorhanden sind THEN das System SHALL diese separat von regulären Vorlagen behandeln
3. WHEN Beispiele aufgelistet werden THEN das System SHALL verfügbare Beispieltypen anzeigen (ISO 27001, ISO 9001, BSI Grundschutz)
4. WHEN ein Benutzer Beispiele verwenden möchte THEN das System SHALL die Möglichkeit bieten, Beispiele als Basis für neue Vorlagen zu kopieren
5. WHEN Beispiele verarbeitet werden THEN das System SHALL dieselben Regeln wie für reguläre Vorlagen anwenden
