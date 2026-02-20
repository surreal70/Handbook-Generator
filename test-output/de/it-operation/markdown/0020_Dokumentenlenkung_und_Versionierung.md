# Dokumentenlenkung und Versionierung

**Dokument-ID:** IT-OPERATION-0020
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

## Dokumentmetadaten

| Feld | Wert |
|---|---|
| Dokumenttitel | IT-Betriebshandbuch – AdminSend GmbH |
| Dokument-ID | [TODO: Eindeutige Dokument-ID] |
| System/Service | [TODO: System-/Service-Name] |
| Eigentümer (Owner) | [TODO] |
| Verantwortlicher Redakteur | [Author] |
| Freigabeinstanz | [TODO] |
| Klassifizierung | Internal |
| Ablageort | [TODO: Zentrales Repository/Ablageort] |
| Organisation | AdminSend GmbH |
| Standort | {{ meta-organisation.city }}, {{ meta-organisation.country }} |

## Versionshistorie

| Version | Datum | Autor | Änderungen | Genehmigung |
|---|---|---|---|---|
| 0 | [TODO: Datum] | [Author] | Initiale Version | [TODO] |
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

**Genehmigung:** [TODO]

### 2. Fachreview

**Reviewer:**
- **Operations:** {{ meta-organisation-roles.role_IT_Operations_Manager }} ({{ meta-organisation-roles.role_IT_Operations_Manager_email }})
- **Architektur:** [TODO: Architektur-Verantwortlicher]
- **Security:** [TODO] ({{ meta-organisation-roles.role_CISO_email }})
- **Compliance:** [TODO: Compliance-Verantwortlicher]

**Prüfkriterien:**
- Fachliche Korrektheit
- Vollständigkeit
- Konsistenz mit anderen Dokumenten
- Einhaltung von Standards und Best Practices

### 3. Freigabe

**Freigabeinstanz:** [TODO]

**Freigabekriterien:**
- Alle Reviews abgeschlossen
- Keine offenen Kommentare
- Qualitätskriterien erfüllt
- Dokumentationsstandards eingehalten

**Freigabeprozess:**
1. Review-Kommentare einarbeiten
2. Finale Version erstellen
3. Freigabe durch [TODO]
4. Version inkrementieren
5. Publikation im Repository

### 4. Publikation

**Verantwortlich:** [TODO]

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

- **Genehmigung:** [TODO]
- **Review:** Fachbereich (Operations/Security)
- **Beispiele:** Neue Abschnitte, Prozessänderungen

### Wesentliche Änderungen (Major)

- **Genehmigung:** [TODO] ({{ meta-organisation-roles.role_CIO_email }})
- **Review:** Alle Fachbereiche + Management
- **CAB-Sitzung:** Erforderlich
- **Beispiele:** Grundlegende Überarbeitungen, Architekturänderungen

## Dokumentationsstandards

### Sprache und Format

- **Sprache:** {{ meta-handbook.language }}
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
- **Rollen:** `[TODO]`, `[TODO]`, `[TODO]`
- **Dokument:** `[TODO]`, `[TODO]`
- **Autor:** `Handbook-Generator`

## Dokumentenklassifizierung

| Klassifizierung | Beschreibung | Zugriff | Beispiele |
|---|---|---|---|
| **Öffentlich** | Keine Einschränkungen | Alle | Allgemeine Informationen |
| **Intern** | Nur für Mitarbeiter | Mitarbeiter | Betriebshandbücher, Prozesse |
| **Vertraulich** | Eingeschränkter Zugriff | Autorisierte Personen | Sicherheitskonzepte, Passwörter |
| **Streng vertraulich** | Höchste Vertraulichkeit | Management + Autorisierte | Geschäftsgeheimnisse, Compliance |

**Aktuelle Klassifizierung:** Internal

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
| **Dokumentverantwortlicher** | Gesamtverantwortung, Aktualität | [TODO] |
| **Redakteur** | Inhaltliche Pflege, Änderungen | [Author] |
| **Freigabeinstanz** | Genehmigung von Änderungen | [TODO] |
| **CIO** | Strategische Ausrichtung | [TODO] |
| **CISO** | Security-Review | [TODO] |

## Kontakte

**Bei Fragen zur Dokumentenlenkung:**
- **Dokumentverantwortlicher:** [TODO]
- **IT Operations Manager:** {{ meta-organisation-roles.role_IT_Operations_Manager }} ({{ meta-organisation-roles.role_IT_Operations_Manager_email }})
- **CIO:** [TODO] ({{ meta-organisation-roles.role_CIO_email }})

**Dokumentverantwortlicher:** [TODO]  
**Genehmigt durch:** [TODO]  
**Version:** 0  
**Organisation:** AdminSend GmbH

