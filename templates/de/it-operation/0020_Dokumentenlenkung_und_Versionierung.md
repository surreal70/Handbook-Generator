# Dokumentenlenkung und Versionierung

**Dokument-ID:** [FRAMEWORK]-0020
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Genehmigt durch:** {{ meta-handbook.approver }}
**Revision:** [TODO]
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Klassifizierung:** {{ meta-handbook.classification }}
**Letzte Aktualisierung:** {{ meta-handbook.modifydate }}
**Template Version:** [TODO]

---

---

## Dokumentmetadaten

| Feld | Wert |
|---|---|
| Dokumenttitel | IT-Betriebshandbuch – {{ meta-organisation.name }} |
| Dokument-ID | [TODO: Eindeutige Dokument-ID] |
| System/Service | [TODO: System-/Service-Name] |
| Eigentümer (Owner) | {{ meta-handbook.owner }} |
| Verantwortlicher Redakteur | [Author] |
| Freigabeinstanz | {{ meta-handbook.approver }} |
| Klassifizierung | {{ meta-handbook.classification }} |
| Ablageort | [TODO: Zentrales Repository/Ablageort] |
| Organisation | {{ meta-organisation.name }} |
| Standort | {{ meta-organisation.city }}, {{ meta-organisation.country }} |

## Versionshistorie

| Version | Datum | Autor | Änderungen | Genehmigung |
|---|---|---|---|---|
| {{ meta-handbook.revision }} | [TODO: Datum] | [Author] | Initiale Version | {{ meta-handbook.approver }} |
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

**Genehmigung:** {{ meta-handbook.owner }}

### 2. Fachreview

**Reviewer:**
- **Operations:** {{ meta-organisation-roles.role_it_operations_manager.name }} ({{ meta-organisation-roles.role_it_operations_manager.email }})
- **Architektur:** [TODO: Architektur-Verantwortlicher]
- **Security:** {{ meta-organisation-roles.role_ciso.name }} ({{ meta-organisation-roles.role_ciso.email }})
- **Compliance:** [TODO: Compliance-Verantwortlicher]

**Prüfkriterien:**
- Fachliche Korrektheit
- Vollständigkeit
- Konsistenz mit anderen Dokumenten
- Einhaltung von Standards und Best Practices

### 3. Freigabe

**Freigabeinstanz:** {{ meta-handbook.approver }}

**Freigabekriterien:**
- Alle Reviews abgeschlossen
- Keine offenen Kommentare
- Qualitätskriterien erfüllt
- Dokumentationsstandards eingehalten

**Freigabeprozess:**
1. Review-Kommentare einarbeiten
2. Finale Version erstellen
3. Freigabe durch {{ meta-handbook.approver }}
4. Version inkrementieren
5. Publikation im Repository

### 4. Publikation

**Verantwortlich:** {{ meta-handbook.owner }}

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

- **Genehmigung:** {{ meta-handbook.approver }}
- **Review:** Fachbereich (Operations/Security)
- **Beispiele:** Neue Abschnitte, Prozessänderungen

### Wesentliche Änderungen (Major)

- **Genehmigung:** {{ meta-organisation-roles.role_cio.name }} ({{ meta-organisation-roles.role_cio.email }})
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

- **Organisation:** `{{ meta-organisation.name }}`
- **Rollen:** `{{ meta-organisation-roles.role_ceo.name }}`, `{{ meta-organisation-roles.role_cio.name }}`, `{{ meta-organisation-roles.role_ciso.name }}`
- **Dokument:** `{{ meta-handbook.owner }}`, `{{ meta-handbook.approver }}`
- **Autor:** `{{ meta-handbook.author }}`

## Dokumentenklassifizierung

| Klassifizierung | Beschreibung | Zugriff | Beispiele |
|---|---|---|---|
| **Öffentlich** | Keine Einschränkungen | Alle | Allgemeine Informationen |
| **Intern** | Nur für Mitarbeiter | Mitarbeiter | Betriebshandbücher, Prozesse |
| **Vertraulich** | Eingeschränkter Zugriff | Autorisierte Personen | Sicherheitskonzepte, Passwörter |
| **Streng vertraulich** | Höchste Vertraulichkeit | Management + Autorisierte | Geschäftsgeheimnisse, Compliance |

**Aktuelle Klassifizierung:** {{ meta-handbook.classification }}

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
| **Dokumentverantwortlicher** | Gesamtverantwortung, Aktualität | {{ meta-handbook.owner }} |
| **Redakteur** | Inhaltliche Pflege, Änderungen | [Author] |
| **Freigabeinstanz** | Genehmigung von Änderungen | {{ meta-handbook.approver }} |
| **CIO** | Strategische Ausrichtung | {{ meta-organisation-roles.role_cio.name }} |
| **CISO** | Security-Review | {{ meta-organisation-roles.role_ciso.name }} |

## Kontakte

**Bei Fragen zur Dokumentenlenkung:**
- **Dokumentverantwortlicher:** {{ meta-handbook.owner }}
- **IT Operations Manager:** {{ meta-organisation-roles.role_it_operations_manager.name }} ({{ meta-organisation-roles.role_it_operations_manager.email }})
- **CIO:** {{ meta-organisation-roles.role_cio.name }} ({{ meta-organisation-roles.role_cio.email }})

**Dokumentverantwortlicher:** {{ meta-handbook.owner }}  
**Genehmigt durch:** {{ meta-handbook.approver }}  
**Version:** {{ meta-handbook.revision }}  
**Organisation:** {{ meta-organisation.name }}

