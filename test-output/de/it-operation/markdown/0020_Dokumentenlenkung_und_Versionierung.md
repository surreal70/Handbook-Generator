# Dokumentenlenkung und Versionierung

## Dokumentmetadaten

| Feld | Wert |
|---|---|
| Dokumenttitel | IT-Betriebshandbuch – AdminSend GmbH |
| Dokument-ID | [TODO: Eindeutige Dokument-ID] |
| System/Service | [TODO: System-/Service-Name] |
| Eigentümer (Owner) | IT Operations Manager |
| Verantwortlicher Redakteur | Andreas Huemmer [andreas.huemmer@adminsend.de] |
| Freigabeinstanz | CIO |
| Klassifizierung | internal |
| Ablageort | [TODO: Zentrales Repository/Ablageort] |
| Organisation | AdminSend GmbH |
| Standort | München, Deutschland |

## Versionshistorie

| Version | Datum | Autor | Änderungen | Genehmigung |
|---|---|---|---|---|
| 1.0.0 | [TODO: Datum] | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initiale Version | CIO |
| | | | | |
| | | | | |

> **Hinweis:** Nutzen Sie Semantic Versioning (SemVer) für die Versionierung:
> - **Major.Minor.Patch** (z.B. 1.0.0)
> - **Major:** Grundlegende Änderungen, Breaking Changes
> - **Minor:** Neue Features, abwärtskompatibel
> - **Patch:** Bugfixes, kleine Korrekturen

## Versionierungsrichtlinien

### Semantic Versioning (SemVer)

**Format:** MAJOR.MINOR.PATCH

- **MAJOR:** Inkompatible Änderungen, grundlegende Überarbeitungen
  - Beispiel: Wechsel der Systemarchitektur, neue Betriebsmodelle
- **MINOR:** Neue Funktionalität, abwärtskompatibel
  - Beispiel: Neue Prozesse, zusätzliche Abschnitte
- **PATCH:** Bugfixes, Korrekturen, Klarstellungen
  - Beispiel: Tippfehler, Formatierungen, kleine Ergänzungen

### Versionierungsregeln

1. **Initiale Version:** 1.0.0 nach Erstfreigabe
2. **Entwürfe:** 0.x.x vor Erstfreigabe
3. **Änderungen dokumentieren:** Jede Änderung in Versionshistorie eintragen
4. **Datum:** ISO 8601 Format (YYYY-MM-DD)
5. **Autor:** Vollständiger Name und E-Mail

## Review- und Freigabeprozess

### 1. Änderungsantrag (Change Request)

**Verantwortlich:** Dokumentverantwortlicher oder Fachbereich

**Inhalt:**
- Beschreibung der Änderung
- Begründung und Geschäftswert
- Auswirkungsanalyse
- Betroffene Abschnitte

**Genehmigung:** IT Operations Manager

### 2. Fachreview

**Reviewer:**
- **Operations:** Andreas Huemmer (andreas.huemmer@adminsend.de)
- **Architektur:** [TODO: Architektur-Verantwortlicher]
- **Security:** Thomas Weber (thomas.weber@adminsend.de)
- **Compliance:** [TODO: Compliance-Verantwortlicher]

**Prüfkriterien:**
- Fachliche Korrektheit
- Vollständigkeit
- Konsistenz mit anderen Dokumenten
- Einhaltung von Standards und Best Practices

### 3. Freigabe

**Freigabeinstanz:** CIO

**Freigabekriterien:**
- Alle Reviews abgeschlossen
- Keine offenen Kommentare
- Qualitätskriterien erfüllt
- Dokumentationsstandards eingehalten

**Freigabeprozess:**
1. Review-Kommentare einarbeiten
2. Finale Version erstellen
3. Freigabe durch CIO
4. Version inkrementieren
5. Publikation im Repository

### 4. Publikation

**Verantwortlich:** IT Operations Manager

**Schritte:**
1. Dokument im zentralen Repository ablegen
2. Stakeholder informieren
3. Alte Version archivieren
4. Änderungsnotiz veröffentlichen

## Genehmigungsprozesse

### Standard-Änderungen (Patch)

- **Genehmigung:** Dokumentverantwortlicher
- **Review:** Optional
- **Beispiele:** Tippfehler, Formatierung, kleine Ergänzungen

### Normale Änderungen (Minor)

- **Genehmigung:** CIO
- **Review:** Fachbereich (Operations/Security)
- **Beispiele:** Neue Abschnitte, Prozessänderungen

### Wesentliche Änderungen (Major)

- **Genehmigung:** Anna Schmidt (anna.schmidt@adminsend.de)
- **Review:** Alle Fachbereiche + Management
- **CAB-Sitzung:** Erforderlich
- **Beispiele:** Grundlegende Überarbeitungen, Architekturänderungen

## Dokumentationsstandards

### Sprache und Format

- **Sprache:** de
- **Format:** Markdown (.md)
- **Zeichensatz:** UTF-8
- **Zeilenumbruch:** Unix (LF)

### Pflichtfelder

Jedes Dokument MUSS folgende Informationen enthalten:

- **Titel:** Eindeutiger Dokumenttitel
- **Version:** Nach SemVer
- **Datum:** Letzte Änderung (ISO 8601)
- **Autor:** Verantwortlicher Redakteur
- **Owner:** Dokumentverantwortlicher
- **Freigabe:** Freigabeinstanz
- **Klassifizierung:** Vertraulichkeitsstufe

### Strukturvorgaben

1. **Überschriften:** Hierarchisch (# H1, ## H2, ### H3)
2. **Tabellen:** Markdown-Syntax mit Ausrichtung
3. **Listen:** Nummeriert oder Aufzählungszeichen
4. **Code:** Fenced Code Blocks mit Syntax-Highlighting
5. **Links:** Relative Links bevorzugt

### Verlinkungen

- **Interne Links:** Relative Pfade innerhalb des Repositories
- **Externe Links:** Absolute URLs mit Beschreibung
- **Referenzen:** Eindeutige Bezeichner für Querverweise

### Metadaten-Platzhalter

Verwenden Sie folgende Platzhalter für organisationsweite Informationen:

- **Organisation:** `AdminSend GmbH`
- **Rollen:** `Max Mustermann`, `Anna Schmidt`, `Thomas Weber`
- **Dokument:** `IT Operations Manager`, `CIO`
- **Autor:** `Andreas Huemmer [andreas.huemmer@adminsend.de]`

## Dokumentenklassifizierung

| Klassifizierung | Beschreibung | Zugriff | Beispiele |
|---|---|---|---|
| **Öffentlich** | Keine Einschränkungen | Alle | Allgemeine Informationen |
| **Intern** | Nur für Mitarbeiter | Mitarbeiter | Betriebshandbücher, Prozesse |
| **Vertraulich** | Eingeschränkter Zugriff | Autorisierte Personen | Sicherheitskonzepte, Passwörter |
| **Streng vertraulich** | Höchste Vertraulichkeit | Management + Autorisierte | Geschäftsgeheimnisse, Compliance |

**Aktuelle Klassifizierung:** internal

## Archivierung und Aufbewahrung

### Aufbewahrungsfristen

- **Aktuelle Version:** Unbegrenzt im Repository
- **Vorversionen:** Mindestens 3 Jahre
- **Entwürfe:** 1 Jahr nach Freigabe
- **Archivierte Dokumente:** Nach Aufbewahrungsrichtlinie

### Archivierungsprozess

1. **Versionswechsel:** Alte Version in Archiv verschieben
2. **Metadaten:** Archivierungsdatum und Grund dokumentieren
3. **Zugriff:** Lesezugriff für autorisierte Personen
4. **Löschung:** Nach Ablauf der Aufbewahrungsfrist

## Verantwortlichkeiten

| Rolle | Verantwortung | Person |
|---|---|---|
| **Dokumentverantwortlicher** | Gesamtverantwortung, Aktualität | IT Operations Manager |
| **Redakteur** | Inhaltliche Pflege, Änderungen | Andreas Huemmer [andreas.huemmer@adminsend.de] |
| **Freigabeinstanz** | Genehmigung von Änderungen | CIO |
| **CIO** | Strategische Ausrichtung | Anna Schmidt |
| **CISO** | Security-Review | Thomas Weber |

## Kontakte

**Bei Fragen zur Dokumentenlenkung:**
- **Dokumentverantwortlicher:** IT Operations Manager
- **IT Operations Manager:** Andreas Huemmer (andreas.huemmer@adminsend.de)
- **CIO:** Anna Schmidt (anna.schmidt@adminsend.de)

---

**Dokumentverantwortlicher:** IT Operations Manager  
**Genehmigt durch:** CIO  
**Version:** 1.0.0  
**Organisation:** AdminSend GmbH
