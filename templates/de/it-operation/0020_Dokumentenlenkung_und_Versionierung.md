# Dokumentenlenkung und Versionierung

## Dokumentmetadaten

| Feld | Wert |
|---|---|
| Dokumenttitel | IT-Betriebshandbuch – {{ meta.organization.name }} |
| Dokument-ID | [TODO: Eindeutige Dokument-ID] |
| System/Service | [TODO: System-/Service-Name] |
| Eigentümer (Owner) | {{ meta.document.owner }} |
| Verantwortlicher Redakteur | {{ meta.author }} |
| Freigabeinstanz | {{ meta.document.approver }} |
| Klassifizierung | {{ meta.document.classification }} |
| Ablageort | [TODO: Zentrales Repository/Ablageort] |
| Organisation | {{ meta.organization.name }} |
| Standort | {{ meta.organization.city }}, {{ meta.organization.country }} |

## Versionshistorie

| Version | Datum | Autor | Änderungen | Genehmigung |
|---|---|---|---|---|
| {{ meta.document.version }} | [TODO: Datum] | {{ meta.author }} | Initiale Version | {{ meta.document.approver }} |
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

**Genehmigung:** {{ meta.document.owner }}

### 2. Fachreview

**Reviewer:**
- **Operations:** {{ meta.it_operations_manager.name }} ({{ meta.it_operations_manager.email }})
- **Architektur:** [TODO: Architektur-Verantwortlicher]
- **Security:** {{ meta.ciso.name }} ({{ meta.ciso.email }})
- **Compliance:** [TODO: Compliance-Verantwortlicher]

**Prüfkriterien:**
- Fachliche Korrektheit
- Vollständigkeit
- Konsistenz mit anderen Dokumenten
- Einhaltung von Standards und Best Practices

### 3. Freigabe

**Freigabeinstanz:** {{ meta.document.approver }}

**Freigabekriterien:**
- Alle Reviews abgeschlossen
- Keine offenen Kommentare
- Qualitätskriterien erfüllt
- Dokumentationsstandards eingehalten

**Freigabeprozess:**
1. Review-Kommentare einarbeiten
2. Finale Version erstellen
3. Freigabe durch {{ meta.document.approver }}
4. Version inkrementieren
5. Publikation im Repository

### 4. Publikation

**Verantwortlich:** {{ meta.document.owner }}

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

- **Genehmigung:** {{ meta.document.approver }}
- **Review:** Fachbereich (Operations/Security)
- **Beispiele:** Neue Abschnitte, Prozessänderungen

### Wesentliche Änderungen (Major)

- **Genehmigung:** {{ meta.cio.name }} ({{ meta.cio.email }})
- **Review:** Alle Fachbereiche + Management
- **CAB-Sitzung:** Erforderlich
- **Beispiele:** Grundlegende Überarbeitungen, Architekturänderungen

## Dokumentationsstandards

### Sprache und Format

- **Sprache:** {{ meta.language }}
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

- **Organisation:** `{{ meta.organization.name }}`
- **Rollen:** `{{ meta.ceo.name }}`, `{{ meta.cio.name }}`, `{{ meta.ciso.name }}`
- **Dokument:** `{{ meta.document.owner }}`, `{{ meta.document.approver }}`
- **Autor:** `{{ meta.author }}`

## Dokumentenklassifizierung

| Klassifizierung | Beschreibung | Zugriff | Beispiele |
|---|---|---|---|
| **Öffentlich** | Keine Einschränkungen | Alle | Allgemeine Informationen |
| **Intern** | Nur für Mitarbeiter | Mitarbeiter | Betriebshandbücher, Prozesse |
| **Vertraulich** | Eingeschränkter Zugriff | Autorisierte Personen | Sicherheitskonzepte, Passwörter |
| **Streng vertraulich** | Höchste Vertraulichkeit | Management + Autorisierte | Geschäftsgeheimnisse, Compliance |

**Aktuelle Klassifizierung:** {{ meta.document.classification }}

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
| **Dokumentverantwortlicher** | Gesamtverantwortung, Aktualität | {{ meta.document.owner }} |
| **Redakteur** | Inhaltliche Pflege, Änderungen | {{ meta.author }} |
| **Freigabeinstanz** | Genehmigung von Änderungen | {{ meta.document.approver }} |
| **CIO** | Strategische Ausrichtung | {{ meta.cio.name }} |
| **CISO** | Security-Review | {{ meta.ciso.name }} |

## Kontakte

**Bei Fragen zur Dokumentenlenkung:**
- **Dokumentverantwortlicher:** {{ meta.document.owner }}
- **IT Operations Manager:** {{ meta.it_operations_manager.name }} ({{ meta.it_operations_manager.email }})
- **CIO:** {{ meta.cio.name }} ({{ meta.cio.email }})

---

**Dokumentverantwortlicher:** {{ meta.document.owner }}  
**Genehmigt durch:** {{ meta.document.approver }}  
**Version:** {{ meta.document.version }}  
**Organisation:** {{ meta.organization.name }}

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |
