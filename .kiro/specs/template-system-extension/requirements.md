# Anforderungsdokument

## Einführung

Dieses Dokument beschreibt die Anforderungen für die Erweiterung des bestehenden Handbuch-Generator-Systems um zusätzliche Template-Typen (BCM, ISMS, BSI Grundschutz) und HTML-Kommentar-Unterstützung. Das System soll professionelle, standardkonforme Handbücher für Business Continuity Management (ISO 22301), Information Security Management (ISO 27001:2022), und BSI IT-Grundschutz erstellen können. Zusätzlich wird die Möglichkeit geschaffen, nicht-gerenderte Dokumentation in Templates mittels HTML-Kommentaren einzufügen.

## Glossar

- **Handbuch-Generator**: Das bestehende System, das aus Markdown-Vorlagen angereicherte Handbücher erstellt
- **Template-Typ**: Eine Kategorie von Templates (it-operation, bcm, isms, bsi-grundschutz)
- **BCM**: Business Continuity Management nach ISO 22301 und BSI BCM-Standards
- **ISMS**: Information Security Management System nach ISO/IEC 27001:2022
- **BSI Grundschutz**: IT-Sicherheitsstandard des Bundesamts für Sicherheit in der Informationstechnik
- **HTML-Kommentar**: Nicht-gerenderte Dokumentation im Format `<!-- kommentar -->`
- **Meta-Platzhalter**: Platzhalter für organisationsweite Metadaten im Format `{{ meta.feld }}`
- **NetBox-Platzhalter**: Platzhalter für Infrastrukturdaten im Format `{{ netbox.feld }}`
- **RACI-Matrix**: Verantwortlichkeitsmatrix (Responsible, Accountable, Consulted, Informed)
- **Annex A**: Anhang A der ISO 27001 mit Sicherheitskontrollen
- **BSI Baustein**: Modulare Sicherheitsbausteine des BSI IT-Grundschutz-Kompendiums
- **CIS Controls**: Center for Internet Security Controls v8
- **Implementation Group (IG)**: CIS Controls Implementierungsgruppen (IG1, IG2, IG3)

## Anforderungen

### Anforderung 1: BCM Template-Struktur

**User Story:** Als BCM-Verantwortlicher möchte ich vollständige BCM-Handbuch-Templates nach ISO 22301 und BSI BCM-Standards, damit ich standardkonforme Business Continuity Dokumentation erstellen kann.

#### Akzeptanzkriterien

1. WHEN BCM-Templates erstellt werden THEN das System SHALL alle 30 Template-Dateien aus input/BCM-Handbuch-Templates/ berücksichtigen
2. WHEN BCM-Templates nummeriert werden THEN das System SHALL die Nummerierung 0010-0290 verwenden
3. WHEN BCM-Templates strukturiert werden THEN das System SHALL Meta-Platzhalter für Organisationsdaten integrieren
4. WHEN BCM-Templates strukturiert werden THEN das System SHALL NetBox-Platzhalter für Infrastrukturdaten integrieren
5. WHEN BCM-Templates erstellt werden THEN das System SHALL [TODO] Markierungen für anpassbare Abschnitte einfügen

### Anforderung 2: BCM Framework-Compliance

**User Story:** Als BCM-Verantwortlicher möchte ich, dass BCM-Templates ISO 22301 und BSI BCM-Standards referenzieren, damit die Compliance-Anforderungen klar dokumentiert sind.

#### Akzeptanzkriterien

1. WHEN BCM-Templates Framework-Referenzen enthalten THEN das System SHALL ISO 22301 Klauseln referenzieren
2. WHEN BCM-Templates Framework-Referenzen enthalten THEN das System SHALL BSI BCM-Standards referenzieren
3. WHEN BCM-Templates RACI-Matrizen enthalten THEN das System SHALL vollständige Verantwortlichkeitszuordnungen definieren
4. WHEN BCM-Templates erstellt werden THEN das System SHALL BIA-Methodik (Business Impact Analysis) Templates bereitstellen
5. WHEN BCM-Templates erstellt werden THEN das System SHALL RTO/RPO (Recovery Time/Point Objectives) Definitionen enthalten

### Anforderung 3: BCM Mehrsprachigkeit

**User Story:** Als internationaler BCM-Verantwortlicher möchte ich BCM-Templates in Deutsch und Englisch, damit ich Handbücher in beiden Sprachen erstellen kann.

#### Akzeptanzkriterien

1. WHEN BCM-Templates erstellt werden THEN das System SHALL deutsche Templates in templates/de/bcm/ speichern
2. WHEN BCM-Templates erstellt werden THEN das System SHALL englische Templates in templates/en/bcm/ speichern
3. WHEN bilinguale BCM-Templates erstellt werden THEN das System SHALL identische Nummerierung verwenden
4. WHEN bilinguale BCM-Templates erstellt werden THEN das System SHALL identische Platzhalter verwenden
5. WHEN bilinguale BCM-Templates erstellt werden THEN das System SHALL identische Struktur verwenden

### Anforderung 4: BCM README-Dokumentation

**User Story:** Als BCM-Verantwortlicher möchte ich eine umfassende README.md für BCM-Templates, damit ich die Verwendung und Best Practices verstehe.

#### Akzeptanzkriterien

1. WHEN BCM README erstellt wird THEN das System SHALL Template-Struktur und Nummerierung erklären
2. WHEN BCM README erstellt wird THEN das System SHALL Platzhalter-Verwendung mit Beispielen dokumentieren
3. WHEN BCM README erstellt wird THEN das System SHALL ISO 22301 Compliance-Mapping bereitstellen
4. WHEN BCM README erstellt wird THEN das System SHALL BSI BCM-Standards-Mapping bereitstellen
5. WHEN BCM README erstellt wird THEN das System SHALL Best Practices für Template-Anpassungen dokumentieren

### Anforderung 5: ISMS Template-Struktur

**User Story:** Als ISMS-Verantwortlicher möchte ich vollständige ISMS-Handbuch-Templates nach ISO 27001:2022, damit ich standardkonforme Informationssicherheits-Dokumentation erstellen kann.

#### Akzeptanzkriterien

1. WHEN ISMS-Templates erstellt werden THEN das System SHALL alle Template-Dateien aus input/ISMS-Templates-ISO27001/ berücksichtigen
2. WHEN ISMS-Templates nummeriert werden THEN das System SHALL die Nummerierung 0010-0740 verwenden
3. WHEN ISMS-Templates strukturiert werden THEN das System SHALL drei Ebenen unterscheiden (Basis-ISMS, Abstract Policies, Detailed Guidelines)
4. WHEN ISMS-Templates strukturiert werden THEN das System SHALL Meta-Platzhalter für Organisationsdaten integrieren
5. WHEN ISMS-Templates erstellt werden THEN das System SHALL [TODO] Markierungen für anpassbare Abschnitte einfügen

### Anforderung 6: ISMS Framework-Compliance

**User Story:** Als ISMS-Verantwortlicher möchte ich, dass ISMS-Templates ISO 27001:2022 (inkl. Amendment 1:2024) referenzieren, damit die Compliance-Anforderungen klar dokumentiert sind.

#### Akzeptanzkriterien

1. WHEN ISMS-Templates Framework-Referenzen enthalten THEN das System SHALL ISO 27001:2022 Klauseln referenzieren
2. WHEN ISMS-Templates Framework-Referenzen enthalten THEN das System SHALL Amendment 1:2024 Änderungen berücksichtigen
3. WHEN ISMS-Templates Annex A Mappings enthalten THEN das System SHALL alle relevanten Annex A Kontrollen referenzieren
4. WHEN ISMS-Templates RACI-Matrizen enthalten THEN das System SHALL vollständige Verantwortlichkeitszuordnungen definieren
5. WHEN ISMS-Templates erstellt werden THEN das System SHALL Statement of Applicability (SoA) Templates bereitstellen

### Anforderung 7: ISMS Drei-Ebenen-Struktur

**User Story:** Als ISMS-Verantwortlicher möchte ich eine klare Trennung zwischen Basis-ISMS-Dokumenten, abstrakten Policies und detaillierten Richtlinien, damit die Dokumentationshierarchie klar strukturiert ist.

#### Akzeptanzkriterien

1. WHEN ISMS Basis-Dokumente erstellt werden THEN das System SHALL Templates 0010-0160 für Context, Scope, Risk Management, Governance bereitstellen
2. WHEN ISMS Abstract Policies erstellt werden THEN das System SHALL Templates 0200-0680 für High-Level-Sicherheitsrichtlinien bereitstellen
3. WHEN ISMS Detailed Guidelines erstellt werden THEN das System SHALL Templates 0210-0690 für konkrete Implementierungsrichtlinien bereitstellen
4. WHEN ISMS-Templates strukturiert werden THEN das System SHALL Policy-Richtlinien-Paare konsistent nummerieren (z.B. 0200 Policy, 0210 Richtlinie)
5. WHEN ISMS-Templates erstellt werden THEN das System SHALL klare Abgrenzung zwischen strategischer und operativer Ebene dokumentieren

### Anforderung 8: ISMS Mehrsprachigkeit

**User Story:** Als internationaler ISMS-Verantwortlicher möchte ich ISMS-Templates in Deutsch und Englisch, damit ich Handbücher in beiden Sprachen erstellen kann.

#### Akzeptanzkriterien

1. WHEN ISMS-Templates erstellt werden THEN das System SHALL deutsche Templates in templates/de/isms/ speichern
2. WHEN ISMS-Templates erstellt werden THEN das System SHALL englische Templates in templates/en/isms/ speichern
3. WHEN bilinguale ISMS-Templates erstellt werden THEN das System SHALL identische Nummerierung verwenden
4. WHEN bilinguale ISMS-Templates erstellt werden THEN das System SHALL identische Platzhalter verwenden
5. WHEN bilinguale ISMS-Templates erstellt werden THEN das System SHALL identische Drei-Ebenen-Struktur verwenden

### Anforderung 9: ISMS README-Dokumentation

**User Story:** Als ISMS-Verantwortlicher möchte ich eine umfassende README.md für ISMS-Templates, damit ich die Verwendung und ISO 27001 Compliance verstehe.

#### Akzeptanzkriterien

1. WHEN ISMS README erstellt wird THEN das System SHALL Template-Struktur und Drei-Ebenen-Hierarchie erklären
2. WHEN ISMS README erstellt wird THEN das System SHALL Platzhalter-Verwendung mit Beispielen dokumentieren
3. WHEN ISMS README erstellt wird THEN das System SHALL ISO 27001:2022 Compliance-Mapping bereitstellen
4. WHEN ISMS README erstellt wird THEN das System SHALL Annex A Kontroll-Mapping bereitstellen
5. WHEN ISMS README erstellt wird THEN das System SHALL Best Practices für Template-Anpassungen dokumentieren

### Anforderung 10: BSI Grundschutz Template-Struktur

**User Story:** Als IT-Sicherheitsbeauftragter möchte ich vollständige BSI Grundschutz-Templates nach BSI Standards 200-1, 200-2, 200-3, damit ich BSI-konforme IT-Sicherheitsdokumentation erstellen kann.

#### Akzeptanzkriterien

1. WHEN BSI Grundschutz-Templates erstellt werden THEN das System SHALL alle Template-Dateien aus input/BSI-Grundschutz-Templates/ berücksichtigen
2. WHEN BSI Grundschutz-Templates nummeriert werden THEN das System SHALL die Nummerierung 0010-0740 verwenden
3. WHEN BSI Grundschutz-Templates strukturiert werden THEN das System SHALL Meta-Platzhalter für Organisationsdaten integrieren
4. WHEN BSI Grundschutz-Templates strukturiert werden THEN das System SHALL BSI Baustein-Referenzen integrieren
5. WHEN BSI Grundschutz-Templates erstellt werden THEN das System SHALL [TODO] Markierungen für anpassbare Abschnitte einfügen

### Anforderung 11: BSI Grundschutz Framework-Compliance

**User Story:** Als IT-Sicherheitsbeauftragter möchte ich, dass BSI Grundschutz-Templates BSI Standards 200-1, 200-2, 200-3 referenzieren, damit die Compliance-Anforderungen klar dokumentiert sind.

#### Akzeptanzkriterien

1. WHEN BSI Grundschutz-Templates Framework-Referenzen enthalten THEN das System SHALL BSI Standard 200-1 (Management System) referenzieren
2. WHEN BSI Grundschutz-Templates Framework-Referenzen enthalten THEN das System SHALL BSI Standard 200-2 (Methodology) referenzieren
3. WHEN BSI Grundschutz-Templates Framework-Referenzen enthalten THEN das System SHALL BSI Standard 200-3 (Risk Analysis) referenzieren
4. WHEN BSI Grundschutz-Templates Baustein-Referenzen enthalten THEN das System SHALL relevante BSI Grundschutz Bausteine referenzieren
5. WHEN BSI Grundschutz-Templates RACI-Matrizen enthalten THEN das System SHALL vollständige Verantwortlichkeitszuordnungen definieren

### Anforderung 12: BSI Grundschutz Themenbereiche

**User Story:** Als IT-Sicherheitsbeauftragter möchte ich BSI Grundschutz-Templates für alle relevanten Themenbereiche, damit ich eine vollständige IT-Sicherheitsdokumentation erstellen kann.

#### Akzeptanzkriterien

1. WHEN BSI Grundschutz ISMS-Foundation-Templates erstellt werden THEN das System SHALL Templates 0010-0100 für Policy, Organization, Scope, Structure Analysis bereitstellen
2. WHEN BSI Grundschutz Security-Concept-Templates erstellt werden THEN das System SHALL Templates 0100-0110 für Gap Analysis, Risk Analysis, Measures bereitstellen
3. WHEN BSI Grundschutz Policy-Templates erstellt werden THEN das System SHALL Templates 0200-0530 für detaillierte Sicherheitsrichtlinien bereitstellen
4. WHEN BSI Grundschutz Management-Templates erstellt werden THEN das System SHALL Templates 0600-0630 für Training, Audits, Reviews, Non-conformities bereitstellen
5. WHEN BSI Grundschutz Appendix-Templates erstellt werden THEN das System SHALL Templates 0700-0740 für Evidence Register, Asset Inventory, Data Flows, Diagrams bereitstellen

### Anforderung 13: BSI Grundschutz Mehrsprachigkeit

**User Story:** Als internationaler IT-Sicherheitsbeauftragter möchte ich BSI Grundschutz-Templates in Deutsch und Englisch, damit ich Handbücher in beiden Sprachen erstellen kann.

#### Akzeptanzkriterien

1. WHEN BSI Grundschutz-Templates erstellt werden THEN das System SHALL deutsche Templates in templates/de/bsi-grundschutz/ speichern
2. WHEN BSI Grundschutz-Templates erstellt werden THEN das System SHALL englische Templates in templates/en/bsi-grundschutz/ speichern
3. WHEN bilinguale BSI Grundschutz-Templates erstellt werden THEN das System SHALL identische Nummerierung verwenden
4. WHEN bilinguale BSI Grundschutz-Templates erstellt werden THEN das System SHALL identische Platzhalter verwenden
5. WHEN bilinguale BSI Grundschutz-Templates erstellt werden THEN das System SHALL identische Struktur verwenden

### Anforderung 14: BSI Grundschutz README-Dokumentation

**User Story:** Als IT-Sicherheitsbeauftragter möchte ich eine umfassende README.md für BSI Grundschutz-Templates, damit ich die Verwendung und BSI Compliance verstehe.

#### Akzeptanzkriterien

1. WHEN BSI Grundschutz README erstellt wird THEN das System SHALL Template-Struktur und Themenbereiche erklären
2. WHEN BSI Grundschutz README erstellt wird THEN das System SHALL Platzhalter-Verwendung mit Beispielen dokumentieren
3. WHEN BSI Grundschutz README erstellt wird THEN das System SHALL BSI Standards 200-1, 200-2, 200-3 Compliance-Mapping bereitstellen
4. WHEN BSI Grundschutz README erstellt wird THEN das System SHALL BSI Baustein-Mapping bereitstellen
5. WHEN BSI Grundschutz README erstellt wird THEN das System SHALL Best Practices für Template-Anpassungen dokumentieren

### Anforderung 15: CIS Controls Struktur-Design

**User Story:** Als Sicherheitsarchitekt möchte ich eine dokumentierte Struktur für CIS Controls v8 Templates, damit zukünftige Implementierung vorbereitet ist.

#### Akzeptanzkriterien

1. WHEN CIS Controls Struktur entworfen wird THEN das System SHALL alle 18 CIS Controls Kategorien berücksichtigen
2. WHEN CIS Controls Struktur entworfen wird THEN das System SHALL Implementation Groups (IG1, IG2, IG3) Mapping definieren
3. WHEN CIS Controls Struktur entworfen wird THEN das System SHALL Platzhalter-Strategie dokumentieren
4. WHEN CIS Controls Struktur entworfen wird THEN das System SHALL README-Struktur definieren
5. WHEN CIS Controls Struktur entworfen wird THEN das System SHALL keine Template-Dateien implementieren (nur Design)

### Anforderung 16: HTML-Kommentar-Erkennung

**User Story:** Als Template-Autor möchte ich HTML-Kommentare in Templates verwenden, damit ich nicht-gerenderte Dokumentation und Hinweise einfügen kann.

#### Akzeptanzkriterien

1. WHEN Templates HTML-Kommentare enthalten THEN das System SHALL Kommentare im Format `<!-- kommentar -->` erkennen
2. WHEN HTML-Kommentare erkannt werden THEN das System SHALL einzeilige Kommentare unterstützen
3. WHEN HTML-Kommentare erkannt werden THEN das System SHALL mehrzeilige Kommentare unterstützen
4. WHEN HTML-Kommentare erkannt werden THEN das System SHALL verschachtelte Kommentare korrekt behandeln
5. WHEN HTML-Kommentare erkannt werden THEN das System SHALL Kommentare von regulärem Markdown-Inhalt unterscheiden

### Anforderung 17: HTML-Kommentar-Entfernung

**User Story:** Als Handbuch-Nutzer möchte ich, dass HTML-Kommentare nicht im generierten Output erscheinen, damit die Handbücher nur relevante Inhalte enthalten.

#### Akzeptanzkriterien

1. WHEN Markdown-Output generiert wird THEN das System SHALL alle HTML-Kommentare entfernen
2. WHEN PDF-Output generiert wird THEN das System SHALL alle HTML-Kommentare entfernen
3. WHEN HTML-Kommentare entfernt werden THEN das System SHALL umgebenden Markdown-Inhalt unverändert lassen
4. WHEN HTML-Kommentare entfernt werden THEN das System SHALL Leerzeilen korrekt behandeln
5. WHEN HTML-Kommentare entfernt werden THEN das System SHALL keine Markdown-Formatierung beschädigen

### Anforderung 18: HTML-Kommentar-Verarbeitung

**User Story:** Als Entwickler möchte ich, dass HTML-Kommentare während der Template-Verarbeitung entfernt werden, damit die Verarbeitung effizient und korrekt erfolgt.

#### Akzeptanzkriterien

1. WHEN Templates verarbeitet werden THEN das System SHALL HTML-Kommentare vor Platzhalter-Ersetzung entfernen
2. WHEN Templates verarbeitet werden THEN das System SHALL HTML-Kommentare nach Template-Laden entfernen
3. WHEN HTML-Kommentare entfernt werden THEN das System SHALL Verarbeitungsstatistiken aktualisieren
4. WHEN HTML-Kommentare entfernt werden THEN das System SHALL Fehlerbehandlung für ungültige Kommentare implementieren
5. WHEN HTML-Kommentare entfernt werden THEN das System SHALL Performance nicht signifikant beeinträchtigen

### Anforderung 19: HTML-Kommentar-Dokumentation

**User Story:** Als Template-Autor möchte ich Dokumentation über HTML-Kommentar-Verwendung, damit ich diese Funktion korrekt nutzen kann.

#### Akzeptanzkriterien

1. WHEN Template-README erstellt wird THEN das System SHALL HTML-Kommentar-Syntax dokumentieren
2. WHEN Template-README erstellt wird THEN das System SHALL Verwendungsbeispiele für HTML-Kommentare bereitstellen
3. WHEN Template-README erstellt wird THEN das System SHALL Best Practices für Kommentar-Verwendung dokumentieren
4. WHEN Template-README erstellt wird THEN das System SHALL Einschränkungen von HTML-Kommentaren dokumentieren
5. WHEN Template-README erstellt wird THEN das System SHALL Unterschied zu Markdown-Kommentaren erklären

### Anforderung 20: Abwärtskompatibilität

**User Story:** Als bestehender Nutzer möchte ich, dass meine existierenden Templates weiterhin funktionieren, damit ich keine Änderungen vornehmen muss.

#### Akzeptanzkriterien

1. WHEN neue Template-Typen hinzugefügt werden THEN das System SHALL bestehende it-operation Templates unverändert verarbeiten
2. WHEN HTML-Kommentar-Unterstützung hinzugefügt wird THEN das System SHALL Templates ohne HTML-Kommentare unverändert verarbeiten
3. WHEN neue Features hinzugefügt werden THEN das System SHALL bestehende CLI-Parameter unterstützen
4. WHEN neue Features hinzugefügt werden THEN das System SHALL bestehende Konfigurationsdateien unterstützen
5. WHEN neue Features hinzugefügt werden THEN das System SHALL bestehende Platzhalter-Syntax unterstützen

### Anforderung 21: CLI-Integration für neue Template-Typen

**User Story:** Als Benutzer möchte ich neue Template-Typen über die CLI auswählen können, damit ich alle Handbuchtypen generieren kann.

#### Akzeptanzkriterien

1. WHEN CLI mit --template bcm aufgerufen wird THEN das System SHALL BCM-Templates verwenden
2. WHEN CLI mit --template isms aufgerufen wird THEN das System SHALL ISMS-Templates verwenden
3. WHEN CLI mit --template bsi-grundschutz aufgerufen wird THEN das System SHALL BSI Grundschutz-Templates verwenden
4. WHEN CLI ohne --template Parameter aufgerufen wird THEN das System SHALL alle verfügbaren Template-Typen auflisten
5. WHEN CLI mit ungültigem --template Parameter aufgerufen wird THEN das System SHALL Fehlermeldung mit verfügbaren Optionen ausgeben

### Anforderung 22: Template-Validierung

**User Story:** Als Entwickler möchte ich automatische Template-Validierung, damit Template-Qualität sichergestellt ist.

#### Akzeptanzkriterien

1. WHEN Templates validiert werden THEN das System SHALL Platzhalter-Syntax prüfen
2. WHEN Templates validiert werden THEN das System SHALL RACI-Matrizen auf Vollständigkeit prüfen
3. WHEN Templates validiert werden THEN das System SHALL Framework-Referenzen auf Vorhandensein prüfen
4. WHEN Templates validiert werden THEN das System SHALL [TODO] Markierungen identifizieren
5. WHEN Templates validiert werden THEN das System SHALL Nummerierungskonsistenz prüfen

### Anforderung 23: Template-Nummerierung

**User Story:** Als Template-Autor möchte ich konsistente Template-Nummerierung, damit die logische Reihenfolge klar ist.

#### Akzeptanzkriterien

1. WHEN IT-Operation-Templates umbenannt werden THEN das System SHALL 0100_einleitung.md zu 0010_Einleitung.md umbenennen
2. WHEN neue Templates erstellt werden THEN das System SHALL 4-stellige Nummerierung verwenden
3. WHEN Templates sortiert werden THEN das System SHALL aufsteigende numerische Reihenfolge verwenden
4. WHEN Templates in verschiedenen Sprachen erstellt werden THEN das System SHALL identische Nummerierung verwenden
5. WHEN Templates in verschiedenen Typen erstellt werden THEN das System SHALL konsistente Nummerierungslogik verwenden

### Anforderung 24: Platzhalter-Konsistenz

**User Story:** Als Template-Autor möchte ich konsistente Platzhalter-Verwendung über alle Template-Typen, damit die Konfiguration einheitlich ist.

#### Akzeptanzkriterien

1. WHEN Meta-Platzhalter verwendet werden THEN das System SHALL identische Syntax über alle Template-Typen verwenden
2. WHEN NetBox-Platzhalter verwendet werden THEN das System SHALL identische Syntax über alle Template-Typen verwenden
3. WHEN Platzhalter dokumentiert werden THEN das System SHALL vollständige Liste verfügbarer Platzhalter bereitstellen
4. WHEN neue Platzhalter hinzugefügt werden THEN das System SHALL Abwärtskompatibilität sicherstellen
5. WHEN Platzhalter validiert werden THEN das System SHALL undefinierte Platzhalter warnen

### Anforderung 25: Ausgabestruktur

**User Story:** Als Benutzer möchte ich konsistente Ausgabestruktur für alle Handbuchtypen, damit die Organisation einheitlich ist.

#### Akzeptanzkriterien

1. WHEN Handbücher generiert werden THEN das System SHALL Ausgabe in Handbook/{language}/{template-type}/ speichern
2. WHEN Markdown-Output generiert wird THEN das System SHALL Dateiname nach Pattern {template-type}_handbook_{language}.md erstellen
3. WHEN PDF-Output generiert wird THEN das System SHALL Dateiname nach Pattern {template-type}_handbook_{language}.pdf erstellen
4. WHEN mehrere Handbücher generiert werden THEN das System SHALL Überschreiben bestehender Dateien bestätigen lassen
5. WHEN Ausgabeverzeichnisse nicht existieren THEN das System SHALL diese automatisch erstellen
