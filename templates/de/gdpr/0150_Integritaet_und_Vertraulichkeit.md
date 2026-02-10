# Integrität und Vertraulichkeit

**Dokument-ID:** 0150  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** Entwurf  
**Klassifizierung:** Intern  
**Letzte Aktualisierung:** {{ meta.date }}  

---

<!-- 
Dieses Template dokumentiert den Grundsatz der Integrität und Vertraulichkeit gemäß Art. 5 Abs. 1 lit. f DSGVO.

Anpassung erforderlich:
- Definiere technische und organisatorische Maßnahmen (TOM)
- Dokumentiere Sicherheitsmaßnahmen für Datenverarbeitung
- Beschreibe Zugriffskontroll- und Verschlüsselungskonzepte
- Implementiere Incident Response Prozesse

Referenz: DSGVO Art. 5 Abs. 1 lit. f (Integrität und Vertraulichkeit), Art. 32 (Sicherheit der Verarbeitung)
-->

## Zweck

Dieses Dokument beschreibt die Umsetzung des Grundsatzes der Integrität und Vertraulichkeit in der {{ meta.organization }}. Personenbezogene Daten müssen sicher verarbeitet und vor unbefugtem Zugriff geschützt werden.

## Grundsatz gemäß Art. 5 Abs. 1 lit. f DSGVO

**Rechtliche Anforderung:**  
Personenbezogene Daten müssen in einer Weise verarbeitet werden, die eine angemessene Sicherheit der personenbezogenen Daten gewährleistet, einschließlich Schutz vor unbefugter oder unrechtmäßiger Verarbeitung und vor unbeabsichtigtem Verlust, unbeabsichtigter Zerstörung oder unbeabsichtigter Schädigung durch geeignete technische und organisatorische Maßnahmen.

### Schutzziele

1. **Vertraulichkeit:** Schutz vor unbefugtem Zugriff
2. **Integrität:** Schutz vor unbefugter Veränderung
3. **Verfügbarkeit:** Schutz vor Verlust oder Zerstörung
4. **Belastbarkeit:** Widerstandsfähigkeit der Systeme

## Technische und Organisatorische Maßnahmen (TOM)

### Übersicht der Maßnahmenkategorien (Art. 32 DSGVO)

| Kategorie | Beschreibung | Beispiele |
|-----------|--------------|-----------|
| Zutrittskontrolle | Schutz vor unbefugtem Zutritt | Zugangskontrollen, Alarmanlagen, Videoüberwachung |
| Zugangskontrolle | Schutz vor unbefugter Systemnutzung | Benutzerauthentifizierung, Passwortrichtlinien, MFA |
| Zugriffskontrolle | Schutz vor unbefugtem Datenzugriff | Berechtigungskonzept, Rollenmodell, Need-to-know |
| Weitergabekontrolle | Schutz bei Datenübermittlung | Verschlüsselung, VPN, sichere Protokolle |
| Eingabekontrolle | Nachvollziehbarkeit von Eingaben | Logging, Audit-Trails, Versionierung |
| Auftragskontrolle | Sicherheit bei Auftragsverarbeitung | AVV, Kontrollen, Audits |
| Verfügbarkeitskontrolle | Schutz vor Datenverlust | Backups, Redundanz, Disaster Recovery |
| Trennungskontrolle | Trennung unterschiedlicher Zwecke | Mandantenfähigkeit, Datensegmentierung |

## Zutrittskontrolle

### Physische Sicherheit

**Maßnahmen zum Schutz vor unbefugtem Zutritt:**

| Maßnahme | Beschreibung | Verantwortlich | Status |
|----------|--------------|----------------|--------|
| [TODO: Zugangskontrollen] | Chipkarten, Schlüssel, Codes | Facility Management | [TODO] |
| [TODO: Besucherregistrierung] | Anmeldung und Begleitung | Empfang | [TODO] |
| [TODO: Videoüberwachung] | Überwachung sensibler Bereiche | Security | [TODO] |
| [TODO: Alarmanlagen] | Einbruchmeldesysteme | Security | [TODO] |
| [TODO: Serverraum-Sicherung] | Besonderer Schutz für Server | IT | [TODO] |

## Zugangskontrolle

### Authentifizierung und Autorisierung

**Maßnahmen zur Systemzugangskontrolle:**

| Maßnahme | Beschreibung | Implementierung | Status |
|----------|--------------|-----------------|--------|
| [TODO: Benutzerauthentifizierung] | Eindeutige Benutzerkonten | Active Directory | [TODO] |
| [TODO: Passwortrichtlinie] | Komplexität, Länge, Ablauf | Gruppenrichtlinien | [TODO] |
| [TODO: Multi-Faktor-Authentifizierung] | Zusätzlicher Authentifizierungsfaktor | MFA-System | [TODO] |
| [TODO: Single Sign-On] | Zentrale Authentifizierung | SSO-Lösung | [TODO] |
| [TODO: Automatische Sperrung] | Nach Inaktivität | Systemeinstellung | [TODO] |

### Passwortrichtlinie

**Anforderungen:**
- Mindestlänge: [TODO: z.B. 12 Zeichen]
- Komplexität: [TODO: Groß-/Kleinbuchstaben, Zahlen, Sonderzeichen]
- Ablauf: [TODO: z.B. 90 Tage]
- Historie: [TODO: z.B. letzte 5 Passwörter nicht wiederverwendbar]
- Sperrung: [TODO: Nach 5 Fehlversuchen]

## Zugriffskontrolle

### Berechtigungskonzept

**Prinzipien:**
- Need-to-know: Nur erforderliche Zugriffe
- Least Privilege: Minimale Berechtigungen
- Rollenbased Access Control (RBAC): Rollenbasierte Zugriffe
- Regelmäßige Überprüfung: Quartalsweise Rezertifizierung

### Berechtigungsmatrix

| Rolle | System/Daten | Zugriff | Begründung |
|-------|-------------|---------|------------|
| [TODO: Administrator] | Alle Systeme | Vollzugriff | Systemverwaltung |
| [TODO: Vertrieb] | CRM | Lesen/Schreiben | Kundenbetreuung |
| [TODO: Buchhaltung] | Finanzsystem | Lesen/Schreiben | Rechnungswesen |
| [TODO: Support] | Ticketsystem | Lesen/Schreiben | Kundenservice |

### Zugriffskontrollprozesse

| Prozess | Beschreibung | Verantwortlich | Frequenz |
|---------|--------------|----------------|----------|
| Berechtigungsvergabe | Antrag und Genehmigung | IT/Vorgesetzter | Bei Bedarf |
| Rezertifizierung | Überprüfung bestehender Rechte | IT/Vorgesetzter | Quartalsweise |
| Entzug bei Austritt | Sofortige Sperrung | HR/IT | Bei Austritt |
| Privilegierte Zugriffe | Besondere Kontrolle | IT-Sicherheit | Monatlich |

## Weitergabekontrolle

### Verschlüsselung

**Verschlüsselungsmaßnahmen:**

| Bereich | Methode | Standard | Status |
|---------|---------|----------|--------|
| [TODO: Datenübertragung] | TLS/SSL | TLS 1.2+ | [TODO] |
| [TODO: E-Mail] | S/MIME oder PGP | - | [TODO] |
| [TODO: Datenträger] | Festplattenverschlüsselung | AES-256 | [TODO] |
| [TODO: Datenbanken] | Transparent Data Encryption | AES-256 | [TODO] |
| [TODO: Backups] | Verschlüsselte Backups | AES-256 | [TODO] |

### Sichere Datenübermittlung

**Maßnahmen:**
- [TODO: VPN für Remote-Zugriffe]
- [TODO: HTTPS für Webanwendungen]
- [TODO: SFTP für Dateitransfers]
- [TODO: Verschlüsselte E-Mail für sensible Daten]
- [TODO: Sichere Cloud-Verbindungen]

## Eingabekontrolle

### Logging und Audit-Trails

**Protokollierung von:**

| Ereignis | Details | Aufbewahrung | Zugriff |
|----------|---------|--------------|---------|
| [TODO: Anmeldungen] | Erfolg/Fehlschlag, Zeitpunkt | 90 Tage | IT-Sicherheit |
| [TODO: Datenänderungen] | Wer, Was, Wann | 1 Jahr | DSB |
| [TODO: Zugriffe auf sensible Daten] | Benutzer, Zeitpunkt, Daten | 1 Jahr | DSB |
| [TODO: Systemänderungen] | Administrator, Änderung | 2 Jahre | IT |
| [TODO: Sicherheitsereignisse] | Art, Zeitpunkt, Quelle | 2 Jahre | IT-Sicherheit |

### Nachvollziehbarkeit

**Maßnahmen:**
- Eindeutige Benutzeridentifikation
- Zeitstempel für alle Aktionen
- Unveränderbare Protokolle
- Regelmäßige Auswertung
- Langfristige Archivierung

## Verfügbarkeitskontrolle

### Backup und Recovery

**Backup-Strategie:**

| Backup-Typ | Frequenz | Aufbewahrung | Speicherort | Verantwortlich |
|------------|----------|--------------|-------------|----------------|
| [TODO: Vollbackup] | Wöchentlich | 4 Wochen | Offsite | IT |
| [TODO: Inkrementell] | Täglich | 7 Tage | Onsite | IT |
| [TODO: Archiv] | Monatlich | 1 Jahr | Offsite | IT |

**Recovery-Prozess:**
- Regelmäßige Restore-Tests
- Dokumentierte Recovery-Verfahren
- Recovery Time Objective (RTO): [TODO]
- Recovery Point Objective (RPO): [TODO]

### Business Continuity

**Maßnahmen:**
- [TODO: Redundante Systeme]
- [TODO: Disaster Recovery Plan]
- [TODO: Notfallhandbuch]
- [TODO: Regelmäßige Tests]

## Incident Response

### Sicherheitsvorfälle

**Prozess bei Sicherheitsvorfällen:**

1. **Erkennung und Meldung**
   - Identifikation des Vorfalls
   - Sofortige Meldung an IT-Sicherheit
   - Erste Bewertung

2. **Eindämmung**
   - Isolation betroffener Systeme
   - Schadensbegrenzung
   - Beweissicherung

3. **Analyse**
   - Ursachenanalyse
   - Umfang der Betroffenheit
   - Bewertung der Auswirkungen

4. **Behebung**
   - Beseitigung der Ursache
   - Wiederherstellung des Normalbetriebs
   - Dokumentation

5. **Nachbereitung**
   - Lessons Learned
   - Verbesserungsmaßnahmen
   - Schulungen

### Datenschutzverletzungen (Art. 33-34 DSGVO)

**Bei Datenschutzverletzungen zusätzlich:**
- Meldung an Aufsichtsbehörde (innerhalb 72 Stunden)
- Benachrichtigung betroffener Personen (bei hohem Risiko)
- Dokumentation im Verzeichnis von Datenschutzverletzungen

## Kontrollen und Überwachung

### Regelmäßige Überprüfungen

| Kontrolle | Frequenz | Verantwortlich | Dokumentation |
|-----------|----------|----------------|---------------|
| Sicherheitsaudit | Jährlich | IT-Sicherheit | Audit-Bericht |
| Penetrationstest | Jährlich | Externer Dienstleister | Testbericht |
| Berechtigungsprüfung | Quartalsweise | IT | Prüfprotokoll |
| Backup-Test | Monatlich | IT | Testprotokoll |
| Log-Auswertung | Wöchentlich | IT-Sicherheit | Analysebericht |

## Dokumentation

### Nachweispflichten

**Dokumentation der TOM:**
- Beschreibung aller technischen und organisatorischen Maßnahmen
- Begründung der Angemessenheit
- Wirksamkeitsnachweise (Tests, Audits)
- Aktualisierung bei Änderungen

### Sicherheitskonzept

**Inhalte:**
- Schutzziele und Risikobewertung
- Technische Maßnahmen
- Organisatorische Maßnahmen
- Verantwortlichkeiten
- Kontrollen und Tests
- Incident Response Plan

## Verknüpfung zu anderen Dokumenten

- **Datenschutzgrundsätze (Art. 5):** Integrität und Vertraulichkeit als Grundprinzip
- **Sicherheit der Verarbeitung (Art. 32):** Detaillierte Anforderungen an TOM
- **Datenschutzverletzungen (Art. 33-34):** Meldepflichten bei Sicherheitsvorfällen
- **Verzeichnis (Art. 30):** Dokumentation der TOM
- **DSFA (Art. 35):** Risikobewertung und Maßnahmen

## Häufige Verstöße und deren Vermeidung

| Verstoß | Beispiel | Vermeidung |
|---------|----------|------------|
| Schwache Passwörter | Einfache Passwörter | Passwortrichtlinie durchsetzen |
| Fehlende Verschlüsselung | Unverschlüsselte Übertragung | TLS/SSL implementieren |
| Übermäßige Berechtigungen | Alle haben Admin-Rechte | Berechtigungskonzept umsetzen |
| Keine Backups | Datenverlust ohne Recovery | Backup-Strategie implementieren |

---

**Nächste Schritte:**
1. Implementieren Sie umfassende TOM gemäß Art. 32
2. Etablieren Sie Zugriffskontroll- und Berechtigungskonzept
3. Implementieren Sie Verschlüsselung für Daten in Ruhe und Übertragung
4. Richten Sie Backup- und Recovery-Prozesse ein
5. Etablieren Sie Incident Response Prozess

