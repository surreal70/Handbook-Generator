# Datenmanagement und Datenschutz

## Übersicht

Dieses Dokument beschreibt die Prozesse und Richtlinien für das Datenmanagement und den Datenschutz im IT-Service. Es definiert Datenklassifizierung, Datenschutzanforderungen gemäß DSGVO, Datenaufbewahrung und -löschung sowie Data-Governance-Strukturen.

**Dokumentverantwortlicher:** {{ meta.document.owner }}  
**Genehmigt durch:** {{ meta.document.approver }}  
**Version:** {{ meta.document.version }}  
**Organisation:** {{ meta.organization.name }}

---

## Datenklassifizierung

### Klassifizierungsstufen

| Stufe | Beschreibung | Beispiele | Schutzmaßnahmen |
|---|---|---|---|
| **Öffentlich** | Für die Öffentlichkeit bestimmt | Marketing-Material, Pressemitteilungen | Keine besonderen Maßnahmen |
| **Intern** | Nur für interne Nutzung | Interne Richtlinien, Organigramme | Zugriffskontrolle |
| **Vertraulich** | Sensible Geschäftsinformationen | Verträge, Finanzberichte, Strategien | Verschlüsselung, strenge Zugriffskontrolle |
| **Streng vertraulich** | Höchst sensible Daten | Personaldaten, Gesundheitsdaten, Gehälter | Verschlüsselung, MFA, Audit-Logging |

### Klassifizierungskriterien

#### Geschäftswert
- **Hoch:** Kritisch für Geschäftsbetrieb
- **Mittel:** Wichtig für Geschäftsprozesse
- **Niedrig:** Unterstützende Informationen

#### Vertraulichkeit
- **Hoch:** Schwerwiegende Schäden bei Offenlegung
- **Mittel:** Moderate Schäden bei Offenlegung
- **Niedrig:** Geringe oder keine Schäden

#### Integrität
- **Hoch:** Kritisch für Entscheidungen
- **Mittel:** Wichtig für Prozesse
- **Niedrig:** Informativ

#### Verfügbarkeit
- **Hoch:** Sofortige Verfügbarkeit erforderlich
- **Mittel:** Verfügbarkeit innerhalb von Stunden
- **Niedrig:** Verfügbarkeit innerhalb von Tagen

### Klassifizierungsprozess

1. **Datenidentifikation:** Erfassung aller Datenbestände
2. **Bewertung:** Anwendung der Klassifizierungskriterien
3. **Kennzeichnung:** Markierung der Daten mit Klassifizierungsstufe
4. **Dokumentation:** Erfassung in Data-Inventory
5. **Review:** Jährliche Überprüfung der Klassifizierung

### Daten-Inventory

| Datenbestand | Klassifizierung | Speicherort | Verantwortlich | Aufbewahrung |
|---|---|---|---|---|
| [TODO] | [TODO] | {{ netbox.storage.location }} | [TODO] | [TODO] |
| [TODO] | [TODO] | {{ netbox.storage.location }} | [TODO] | [TODO] |
| [TODO] | [TODO] | {{ netbox.storage.location }} | [TODO] | [TODO] |

---

## Datenschutz-Anforderungen (DSGVO)

### Rechtliche Grundlagen

#### EU-Datenschutz-Grundverordnung (DSGVO)
- **Gültig seit:** 25. Mai 2018
- **Anwendungsbereich:** Verarbeitung personenbezogener Daten in der EU
- **Bußgelder:** Bis zu 20 Mio. EUR oder 4% des weltweiten Jahresumsatzes

#### Bundesdatenschutzgesetz (BDSG)
- **Gültig seit:** 25. Mai 2018
- **Ergänzung:** Nationale Regelungen zur DSGVO
- **Anwendung:** Deutschland-spezifische Anforderungen

### Personenbezogene Daten

#### Definition
Alle Informationen, die sich auf eine identifizierte oder identifizierbare natürliche Person beziehen.

#### Kategorien

| Kategorie | Beispiele | Besondere Schutzmaßnahmen |
|---|---|---|
| **Basisdaten** | Name, Adresse, E-Mail, Telefon | Zugriffskontrolle, Verschlüsselung |
| **Identifikationsdaten** | Personalausweisnummer, Sozialversicherungsnummer | Strenge Zugriffskontrolle, Verschlüsselung |
| **Besondere Kategorien** | Gesundheit, Religion, politische Meinung | Höchste Schutzmaßnahmen, explizite Einwilligung |
| **Finanzdaten** | Bankverbindung, Kreditkartennummer | PCI-DSS-Compliance, Tokenisierung |
| **Standortdaten** | GPS-Koordinaten, IP-Adressen | Anonymisierung, Pseudonymisierung |

### DSGVO-Grundsätze

#### Rechtmäßigkeit, Verarbeitung nach Treu und Glauben, Transparenz
- Rechtsgrundlage für jede Verarbeitung
- Transparente Information der Betroffenen
- Dokumentation der Verarbeitungszwecke

#### Zweckbindung
- Daten nur für festgelegte Zwecke erheben
- Keine Weiterverarbeitung für andere Zwecke
- Dokumentation der Verarbeitungszwecke

#### Datenminimierung
- Nur notwendige Daten erheben
- Keine übermäßige Datensammlung
- Regelmäßige Überprüfung der Notwendigkeit

#### Richtigkeit
- Sicherstellung der Datenaktualität
- Korrektur unrichtiger Daten
- Löschung veralteter Daten

#### Speicherbegrenzung
- Daten nur so lange speichern wie nötig
- Definierte Aufbewahrungsfristen
- Automatische Löschung nach Fristablauf

#### Integrität und Vertraulichkeit
- Schutz vor unbefugtem Zugriff
- Verschlüsselung sensibler Daten
- Zugriffskontrolle und Audit-Logging

#### Rechenschaftspflicht
- Nachweis der DSGVO-Compliance
- Dokumentation aller Verarbeitungstätigkeiten
- Regelmäßige Audits

### Betroffenenrechte

| Recht | Beschreibung | Reaktionszeit | Verantwortlich |
|---|---|---|---|
| **Auskunftsrecht** | Information über gespeicherte Daten | 1 Monat | {{ meta.ciso.name }} |
| **Berichtigungsrecht** | Korrektur unrichtiger Daten | Unverzüglich | {{ meta.ciso.name }} |
| **Löschungsrecht** | Löschung personenbezogener Daten | Unverzüglich | {{ meta.ciso.name }} |
| **Einschränkung** | Einschränkung der Verarbeitung | Unverzüglich | {{ meta.ciso.name }} |
| **Datenübertragbarkeit** | Übertragung an anderen Verantwortlichen | 1 Monat | {{ meta.ciso.name }} |
| **Widerspruchsrecht** | Widerspruch gegen Verarbeitung | Unverzüglich | {{ meta.ciso.name }} |

### Datenschutz-Folgenabschätzung (DSFA)

#### Durchführungspflicht
- Hohes Risiko für Rechte und Freiheiten
- Neue Technologien
- Umfangreiche Verarbeitung besonderer Kategorien
- Systematische Überwachung

#### DSFA-Prozess
1. **Beschreibung:** Verarbeitungsvorgänge und Zwecke
2. **Notwendigkeit:** Bewertung der Erforderlichkeit
3. **Risikobewertung:** Identifikation und Bewertung von Risiken
4. **Schutzmaßnahmen:** Definition von Maßnahmen zur Risikominimierung
5. **Dokumentation:** Erstellung des DSFA-Berichts
6. **Konsultation:** Ggf. Konsultation der Aufsichtsbehörde

### Datenschutzbeauftragter (DSB)

- **Name:** [TODO: Name des DSB]
- **Kontakt:** [TODO: E-Mail und Telefon]
- **Aufgaben:**
  - Überwachung der DSGVO-Compliance
  - Beratung bei Datenschutzfragen
  - Schulung der Mitarbeiter
  - Zusammenarbeit mit Aufsichtsbehörden
  - Anlaufstelle für Betroffene

---

## Datenaufbewahrung und -löschung

### Aufbewahrungsfristen

#### Gesetzliche Aufbewahrungsfristen

| Datenart | Aufbewahrungsfrist | Rechtsgrundlage | Verantwortlich |
|---|---|---|---|
| Geschäftsbriefe | 6 Jahre | HGB § 257 | {{ meta.cfo.name }} |
| Buchungsbelege | 10 Jahre | HGB § 257, AO § 147 | {{ meta.cfo.name }} |
| Jahresabschlüsse | 10 Jahre | HGB § 257 | {{ meta.cfo.name }} |
| Lohnunterlagen | 6 Jahre | AO § 147 | {{ meta.cfo.name }} |
| Steuerunterlagen | 10 Jahre | AO § 147 | {{ meta.cfo.name }} |
| Personalakten | 3-10 Jahre | Verschiedene | {{ meta.coo.name }} |

#### Betriebliche Aufbewahrungsfristen

| Datenart | Aufbewahrungsfrist | Grund | Verantwortlich |
|---|---|---|---|
| Verträge | Vertragslaufzeit + 3 Jahre | Gewährleistung | [TODO] |
| Projektdokumentation | 5 Jahre | Nachvollziehbarkeit | [TODO] |
| Audit-Logs | 1 Jahr | Sicherheit | {{ meta.ciso.name }} |
| Backup-Daten | 30-90 Tage | Wiederherstellung | {{ meta.it_operations_manager.name }} |
| E-Mails | 1-3 Jahre | Geschäftskommunikation | [TODO] |

### Löschkonzept

#### Löschprozess

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  1. Fristablauf  →  2. Prüfung  →  3. Genehmigung      │
│       ↓                                    ↓            │
│       │                                    │            │
│  6. Dokumentation  ←  5. Verifikation  ←  4. Löschung  │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

#### Löschmethoden

| Datenträger | Methode | Standard | Verantwortlich |
|---|---|---|---|
| Festplatten | Secure Erase / Degaussing | NIST SP 800-88 | {{ meta.it_operations_manager.name }} |
| SSDs | Crypto Erase / Zerstörung | NIST SP 800-88 | {{ meta.it_operations_manager.name }} |
| Backup-Medien | Überschreiben / Zerstörung | NIST SP 800-88 | {{ meta.it_operations_manager.name }} |
| Cloud-Daten | API-basierte Löschung | Provider-Standard | {{ meta.it_operations_manager.name }} |
| Datenbanken | SQL DELETE / TRUNCATE | Datenbankstandard | {{ meta.it_operations_manager.name }} |
| Papier | Aktenvernichtung (P-4) | DIN 66399 | {{ meta.coo.name }} |

#### Löschnachweis
- Dokumentation aller Löschvorgänge
- Protokollierung von Datum, Datenart, Methode
- Aufbewahrung der Löschnachweise für 3 Jahre
- Verantwortlich: {{ meta.ciso.name }}

### Archivierung

#### Archivierungsprozess
1. **Identifikation:** Daten, die archiviert werden müssen
2. **Vorbereitung:** Datenbereinigung und -validierung
3. **Archivierung:** Transfer in Archivsystem
4. **Indexierung:** Metadaten für Wiederauffindbarkeit
5. **Verifikation:** Prüfung der Archivintegrität
6. **Dokumentation:** Erfassung im Archivregister

#### Archivierungssysteme

| System | Datenart | Aufbewahrung | Zugriff | Verantwortlich |
|---|---|---|---|---|
| [TODO: Archivsystem] | [TODO] | [TODO] Jahre | [TODO] | [TODO] |

---

## Data-Governance

### Governance-Struktur

#### Data Governance Board
- **Vorsitz:** {{ meta.cio.name }}
- **Mitglieder:** {{ meta.ciso.name }}, {{ meta.cfo.name }}, Fachbereichsleiter
- **Frequenz:** Quartalsweise
- **Aufgaben:**
  - Strategische Daten-Governance
  - Genehmigung von Data Policies
  - Überwachung der Compliance
  - Eskalation von Datenschutzvorfällen

#### Data Stewards
- **Rolle:** Fachliche Datenverantwortliche
- **Aufgaben:**
  - Datenqualität sicherstellen
  - Datenklassifizierung durchführen
  - Zugriffsgenehmigungen erteilen
  - Datenschutz-Compliance überwachen

#### Data Custodians
- **Rolle:** Technische Datenverantwortliche
- **Aufgaben:**
  - Technische Umsetzung der Data Policies
  - Datensicherheit gewährleisten
  - Backup und Recovery
  - Zugriffskontrolle implementieren

### Data Policies

#### Datennutzungsrichtlinie
- Erlaubte und verbotene Datennutzungen
- Genehmigungsprozesse für Datennutzung
- Sanktionen bei Verstößen

#### Datenzugriffsrichtlinie
- Zugriffskontrollmodell (RBAC, ABAC)
- Genehmigungsprozesse für Zugriffe
- Regelmäßige Zugriffsprüfungen

#### Datensicherheitsrichtlinie
- Verschlüsselungsanforderungen
- Sicherheitsmaßnahmen nach Klassifizierung
- Incident-Response-Prozesse

#### Datenqualitätsrichtlinie
- Datenqualitätskriterien
- Datenvalidierung und -bereinigung
- Datenqualitäts-Metriken

### Datenqualitätsmanagement

#### Datenqualitätsdimensionen

| Dimension | Beschreibung | Zielwert | Messmethode |
|---|---|---:|---|
| **Vollständigkeit** | Alle erforderlichen Daten vorhanden | > 95% | Automatische Prüfung |
| **Richtigkeit** | Daten korrekt und fehlerfrei | > 98% | Stichproben |
| **Konsistenz** | Daten widerspruchsfrei | > 99% | Automatische Prüfung |
| **Aktualität** | Daten auf dem neuesten Stand | > 95% | Zeitstempel-Prüfung |
| **Eindeutigkeit** | Keine Duplikate | > 99% | Duplikatsprüfung |

#### Datenqualitätsprozess
1. **Messung:** Erfassung der Datenqualitäts-Metriken
2. **Analyse:** Identifikation von Qualitätsproblemen
3. **Bereinigung:** Korrektur fehlerhafter Daten
4. **Prävention:** Maßnahmen zur Vermeidung zukünftiger Probleme
5. **Monitoring:** Kontinuierliche Überwachung

---

## Datensicherheit

### Verschlüsselung

#### Verschlüsselung im Ruhezustand (Data at Rest)

| Datenart | Verschlüsselung | Algorithmus | Schlüssellänge | Verantwortlich |
|---|---|---|---|---|
| Streng vertraulich | Pflicht | AES | 256 Bit | {{ meta.ciso.name }} |
| Vertraulich | Pflicht | AES | 256 Bit | {{ meta.ciso.name }} |
| Intern | Empfohlen | AES | 128/256 Bit | {{ meta.it_operations_manager.name }} |
| Öffentlich | Nicht erforderlich | - | - | - |

#### Verschlüsselung in Übertragung (Data in Transit)

| Verbindungstyp | Protokoll | Mindestversion | Verantwortlich |
|---|---|---|---|
| Web-Traffic | HTTPS/TLS | TLS 1.2 | {{ meta.it_operations_manager.name }} |
| E-Mail | TLS/S/MIME | TLS 1.2 | {{ meta.it_operations_manager.name }} |
| Dateiübertragung | SFTP/FTPS | TLS 1.2 | {{ meta.it_operations_manager.name }} |
| VPN | IPsec/OpenVPN | - | {{ meta.it_operations_manager.name }} |
| Datenbank | TLS | TLS 1.2 | {{ meta.it_operations_manager.name }} |

### Zugriffskontrolle

#### Zugriffskontrollmodell
- **Modell:** Role-Based Access Control (RBAC)
- **Prinzip:** Least Privilege, Need-to-Know
- **Authentifizierung:** Multi-Faktor-Authentifizierung (MFA) für sensible Daten
- **Autorisierung:** Rollenbasierte Berechtigungen

#### Zugriffsrechte-Review
- **Frequenz:** Quartalsweise
- **Verantwortlich:** Data Stewards
- **Prozess:**
  1. Export aller Zugriffsrechte
  2. Review durch Fachbereich
  3. Entfernung nicht mehr benötigter Rechte
  4. Dokumentation der Änderungen

### Audit-Logging

#### Logging-Anforderungen

| Ereignistyp | Logging | Aufbewahrung | Verantwortlich |
|---|---|---|---|
| Datenzugriff (vertraulich) | Pflicht | 1 Jahr | {{ meta.ciso.name }} |
| Datenänderung | Pflicht | 1 Jahr | {{ meta.ciso.name }} |
| Datenlöschung | Pflicht | 3 Jahre | {{ meta.ciso.name }} |
| Zugriffsverweigerung | Pflicht | 1 Jahr | {{ meta.ciso.name }} |
| Admin-Aktivitäten | Pflicht | 1 Jahr | {{ meta.ciso.name }} |

#### Log-Inhalte
- Zeitstempel
- Benutzer-ID
- Aktion (Lesen, Schreiben, Löschen)
- Betroffene Daten/Objekte
- Quell-IP-Adresse
- Ergebnis (Erfolg/Fehler)

---

## Datenschutzvorfälle

### Meldepflicht

#### DSGVO-Meldepflicht
- **Frist:** 72 Stunden nach Bekanntwerden
- **Empfänger:** Zuständige Aufsichtsbehörde
- **Inhalt:**
  - Art der Verletzung
  - Betroffene Datenkategorien und Personen
  - Wahrscheinliche Folgen
  - Ergriffene Maßnahmen

#### Benachrichtigung Betroffener
- **Voraussetzung:** Hohes Risiko für Rechte und Freiheiten
- **Frist:** Unverzüglich
- **Inhalt:**
  - Art der Verletzung
  - Kontaktstelle
  - Wahrscheinliche Folgen
  - Ergriffene Maßnahmen

### Incident-Response-Prozess

1. **Erkennung:** Identifikation des Datenschutzvorfalls
2. **Bewertung:** Einschätzung des Risikos
3. **Eindämmung:** Sofortmaßnahmen zur Schadensbegrenzung
4. **Meldung:** Meldung an Aufsichtsbehörde (falls erforderlich)
5. **Benachrichtigung:** Information der Betroffenen (falls erforderlich)
6. **Untersuchung:** Root-Cause-Analyse
7. **Behebung:** Korrekturmaßnahmen
8. **Dokumentation:** Erfassung im Incident-Register
9. **Lessons Learned:** Prozessverbesserungen

---

## Prozesse und Verantwortlichkeiten

### RACI-Matrix

| Aktivität | CIO | CISO | Ops Manager | DSB | Data Stewards |
|---|---|---|---|---|---|
| Datenklassifizierung | I | C | I | C | R/A |
| DSGVO-Compliance | A | R | C | C | I |
| Datenschutz-Folgenabschätzung | C | R | C | A | C |
| Datenaufbewahrung | C | C | R | C | A |
| Datenlöschung | I | C | R | C | A |
| Data-Governance | A | C | C | C | R |
| Datensicherheit | C | A | R | C | I |
| Datenschutzvorfälle | A | R | C | C | I |

> **Legende:** R = Responsible, A = Accountable, C = Consulted, I = Informed

---

## Compliance und Standards

### Relevante Standards
- **DSGVO:** EU-Datenschutz-Grundverordnung
- **BDSG:** Bundesdatenschutzgesetz
- **ISO 27001:** Informationssicherheitsmanagement
- **ISO 27701:** Privacy Information Management
- **NIST SP 800-88:** Guidelines for Media Sanitization

### Audit-Anforderungen
- Verzeichnis von Verarbeitungstätigkeiten
- Datenschutz-Folgenabschätzungen
- Auftragsverarbeitungsverträge
- Löschnachweise
- Audit-Logs

---

## Anhang

### Glossar

| Begriff | Definition |
|---|---|
| DSGVO | Datenschutz-Grundverordnung der EU |
| Personenbezogene Daten | Daten, die sich auf eine identifizierbare Person beziehen |
| Data Steward | Fachlicher Datenverantwortlicher |
| Data Custodian | Technischer Datenverantwortlicher |
| DSFA | Datenschutz-Folgenabschätzung |
| Pseudonymisierung | Verarbeitung ohne Zuordnung zu einer Person ohne Zusatzinformationen |
| Anonymisierung | Irreversible Entfernung des Personenbezugs |

### Referenzen
- EU-Datenschutz-Grundverordnung (DSGVO)
- Bundesdatenschutzgesetz (BDSG)
- ISO/IEC 27001:2013
- ISO/IEC 27701:2019
- NIST SP 800-88 Rev. 1

---

**Letzte Aktualisierung:** {{ meta.date }}  
**Nächste Review:** [TODO: Datum]  
**Kontakt:** {{ meta.ciso.email }}

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |
