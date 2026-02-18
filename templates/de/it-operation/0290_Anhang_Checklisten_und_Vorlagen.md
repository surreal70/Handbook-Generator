# Anhang: Checklisten und Vorlagen

**Dokument-ID:** [FRAMEWORK]-0290
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

## Übersicht

Dieses Dokument enthält eine Sammlung von Checklisten, Vorlagen für Standarddokumente und Formularen für den IT-Betrieb. Ziel ist es, konsistente und effiziente Durchführung von Standardprozessen zu gewährleisten.

**Dokumentverantwortlicher:** {{ meta-handbook.owner }}  
**Genehmigt durch:** {{ meta-handbook.approver }}  
**Version:** {{ meta-handbook.revision }}  
**Organisation:** {{ meta-organisation.name }}

## Checklisten

### Incident-Management-Checklisten

#### Incident-Response-Checkliste

```markdown
# Incident-Response-Checkliste

**Incident-ID:** [INC-XXXXX]
**Datum/Zeit:** [YYYY-MM-DD HH:MM]
**Melder:** [Name]
**Priorität:** P1 / P2 / P3 / P4

## Phase 1: Erkennung und Erfassung
- [ ] Incident erkannt und dokumentiert
- [ ] Priorität bewertet (P1-P4)
- [ ] Ticket erstellt
- [ ] Betroffene Systeme identifiziert
- [ ] Betroffene Benutzer identifiziert
- [ ] Erste Symptome dokumentiert

## Phase 2: Klassifizierung und Priorisierung
- [ ] Incident-Kategorie zugewiesen
- [ ] Business-Impact bewertet
- [ ] Dringlichkeit bewertet
- [ ] Priorität bestätigt
- [ ] Verantwortlichen zugewiesen

## Phase 3: Diagnose und Untersuchung
- [ ] Logs analysiert
- [ ] Monitoring-Daten geprüft
- [ ] Ähnliche Incidents gesucht
- [ ] Known Issues geprüft
- [ ] Root-Cause identifiziert (falls möglich)

## Phase 4: Lösung und Wiederherstellung
- [ ] Lösungsansatz definiert
- [ ] Genehmigung eingeholt (falls erforderlich)
- [ ] Lösung implementiert
- [ ] Funktionalität validiert
- [ ] Benutzer informiert

## Phase 5: Abschluss
- [ ] Incident gelöst
- [ ] Dokumentation vervollständigt
- [ ] Benutzer-Bestätigung eingeholt
- [ ] Ticket geschlossen
- [ ] Lessons Learned dokumentiert (bei P1/P2)

## Kommunikation
- [ ] Stakeholder informiert
- [ ] Status-Updates kommuniziert
- [ ] Lösung kommuniziert

**Bearbeitet von:** [Name]
**Abgeschlossen am:** [YYYY-MM-DD HH:MM]
**Dauer:** [HH:MM]
```

#### Major-Incident-Checkliste

```markdown
# Major-Incident-Checkliste (P1)

**Incident-ID:** [INC-XXXXX]
**Datum/Zeit:** [YYYY-MM-DD HH:MM]
**Incident-Manager:** [Name]

## Sofortmaßnahmen (0-15 Minuten)
- [ ] Major-Incident erklärt
- [ ] Incident-Manager benannt
- [ ] War-Room eingerichtet (physisch/virtuell)
- [ ] Kommunikations-Kanal etabliert
- [ ] Management informiert (CIO)
- [ ] Erste Status-Meldung versendet

## Incident-Management (15-60 Minuten)
- [ ] Technisches Team zusammengestellt
- [ ] Rollen und Verantwortlichkeiten geklärt
- [ ] Diagnose gestartet
- [ ] Workaround gesucht
- [ ] Status-Updates alle 30 Minuten
- [ ] Eskalation vorbereitet (falls erforderlich)

## Lösungsfindung (1-4 Stunden)
- [ ] Root-Cause identifiziert
- [ ] Lösungsansatz definiert
- [ ] Risikobewertung durchgeführt
- [ ] Genehmigung eingeholt
- [ ] Implementierung gestartet
- [ ] Rollback-Plan bereit

## Wiederherstellung
- [ ] Lösung implementiert
- [ ] Funktionalität validiert
- [ ] Monitoring intensiviert
- [ ] Benutzer informiert
- [ ] Services wiederhergestellt

## Nachbereitung
- [ ] Incident geschlossen
- [ ] Postmortem geplant (innerhalb 48h)
- [ ] Dokumentation vervollständigt
- [ ] Management-Report erstellt
- [ ] Verbesserungsmaßnahmen definiert

## Kommunikation
- [ ] Initiale Benachrichtigung (< 15 Min)
- [ ] Status-Updates (alle 30 Min)
- [ ] Lösungs-Benachrichtigung
- [ ] Abschluss-Benachrichtigung
- [ ] Postmortem-Einladung

**Incident-Manager:** [Name]
**Technischer Lead:** [Name]
**Kommunikations-Lead:** [Name]
```

### Change-Management-Checklisten

#### Standard-Change-Checkliste

```markdown
# Standard-Change-Checkliste

**Change-ID:** [CHG-XXXXX]
**Datum:** [YYYY-MM-DD]
**Change-Manager:** [Name]

## Planung
- [ ] Change-Request erstellt
- [ ] Beschreibung vollständig
- [ ] Begründung dokumentiert
- [ ] Risikobewertung durchgeführt
- [ ] Betroffene Systeme identifiziert
- [ ] Abhängigkeiten identifiziert
- [ ] Zeitfenster definiert
- [ ] Ressourcen allokiert

## Genehmigung
- [ ] Change-Kategorie bestimmt (Standard/Normal/Emergency)
- [ ] Genehmiger identifiziert
- [ ] Genehmigung eingeholt
- [ ] CAB-Review (falls erforderlich)

## Vorbereitung
- [ ] Implementierungsplan erstellt
- [ ] Rollback-Plan erstellt
- [ ] Test-Plan erstellt
- [ ] Kommunikationsplan erstellt
- [ ] Backup durchgeführt
- [ ] Test-Umgebung validiert

## Implementierung
- [ ] Wartungsfenster gestartet
- [ ] Benutzer informiert
- [ ] Change implementiert
- [ ] Schritt-für-Schritt dokumentiert
- [ ] Probleme dokumentiert

## Validierung
- [ ] Funktionalität getestet
- [ ] Performance validiert
- [ ] Monitoring geprüft
- [ ] Keine Fehler in Logs
- [ ] Benutzer-Akzeptanz-Test (falls erforderlich)

## Abschluss
- [ ] Change erfolgreich
- [ ] Dokumentation aktualisiert
- [ ] CMDB aktualisiert
- [ ] Benutzer informiert
- [ ] Change geschlossen
- [ ] Lessons Learned (bei Problemen)

## Rollback (falls erforderlich)
- [ ] Rollback-Entscheidung getroffen
- [ ] Rollback-Plan ausgeführt
- [ ] System wiederhergestellt
- [ ] Validierung durchgeführt
- [ ] Incident erstellt für Analyse

**Change-Manager:** [Name]
**Implementiert von:** [Name]
**Status:** Erfolgreich / Rollback / Abgebrochen
```

### Backup und Recovery Checklisten

#### Backup-Verifikations-Checkliste

```markdown
# Backup-Verifikations-Checkliste

**Datum:** [YYYY-MM-DD]
**Durchgeführt von:** [Name]

## Backup-Status
- [ ] Alle geplanten Backups durchgeführt
- [ ] Backup-Logs geprüft
- [ ] Keine Fehler in Logs
- [ ] Backup-Größen plausibel
- [ ] Backup-Zeiten akzeptabel

## Backup-Integrität
- [ ] Checksummen validiert
- [ ] Backup-Dateien lesbar
- [ ] Keine Korruption festgestellt
- [ ] Verschlüsselung funktioniert

## Restore-Test
- [ ] Zufälliges Backup ausgewählt
- [ ] Test-Umgebung vorbereitet
- [ ] Restore durchgeführt
- [ ] Daten validiert
- [ ] Funktionalität getestet
- [ ] Restore-Zeit gemessen

## Dokumentation
- [ ] Test-Ergebnis dokumentiert
- [ ] Probleme dokumentiert
- [ ] Verbesserungen identifiziert
- [ ] Report erstellt

## Systeme geprüft
- [ ] Datenbanken
- [ ] File-Server
- [ ] Anwendungs-Server
- [ ] Konfigurationen
- [ ] Virtualisierungs-Hosts

**Ergebnis:** Erfolgreich / Mit Problemen / Fehlgeschlagen
**Nächster Test:** [YYYY-MM-DD]
```

#### Disaster-Recovery-Test-Checkliste

```markdown
# Disaster-Recovery-Test-Checkliste

**Test-Datum:** [YYYY-MM-DD]
**Test-Leiter:** [Name]
**Szenario:** [Beschreibung]

## Vorbereitung
- [ ] Test-Szenario definiert
- [ ] Test-Plan erstellt
- [ ] Teilnehmer informiert
- [ ] Test-Umgebung vorbereitet
- [ ] Backup-Daten bereitgestellt
- [ ] Kommunikationskanäle getestet

## Disaster-Simulation
- [ ] Disaster-Szenario ausgelöst
- [ ] Incident-Response aktiviert
- [ ] Kommunikation gestartet
- [ ] DR-Team mobilisiert
- [ ] DR-Standort aktiviert (falls zutreffend)

## Recovery-Durchführung
- [ ] DR-Plan befolgt
- [ ] Systeme wiederhergestellt
- [ ] Daten wiederhergestellt
- [ ] Netzwerk wiederhergestellt
- [ ] Anwendungen wiederhergestellt
- [ ] Zeiten gemessen (RTO/RPO)

## Validierung
- [ ] Alle kritischen Systeme online
- [ ] Datenintegrität geprüft
- [ ] Funktionalität getestet
- [ ] Performance akzeptabel
- [ ] Benutzer-Zugriff funktioniert

## Rückkehr zum Normalbetrieb
- [ ] Failback-Plan ausgeführt
- [ ] Primäre Systeme wiederhergestellt
- [ ] Daten synchronisiert
- [ ] Normalbetrieb wiederhergestellt
- [ ] DR-Standort deaktiviert

## Nachbereitung
- [ ] Test-Ergebnisse dokumentiert
- [ ] RTO/RPO-Zeiten dokumentiert
- [ ] Probleme identifiziert
- [ ] Verbesserungen definiert
- [ ] DR-Plan aktualisiert
- [ ] Lessons-Learned-Session durchgeführt

## Metriken
- **RTO-Ziel:** [Zeit]
- **RTO-Erreicht:** [Zeit]
- **RPO-Ziel:** [Zeit]
- **RPO-Erreicht:** [Zeit]
- **Erfolgsrate:** [%]

**Test-Ergebnis:** Erfolgreich / Teilweise erfolgreich / Fehlgeschlagen
**Nächster Test:** [YYYY-MM-DD]
```

### Security-Checklisten

#### Security-Incident-Response-Checkliste

```markdown
# Security-Incident-Response-Checkliste

**Incident-ID:** [SEC-XXXXX]
**Datum/Zeit:** [YYYY-MM-DD HH:MM]
**Incident-Commander:** [Name]

## Phase 1: Identifikation (0-30 Minuten)
- [ ] Security-Event erkannt
- [ ] Incident bestätigt
- [ ] Severity bewertet
- [ ] CISO informiert
- [ ] Security-Team mobilisiert
- [ ] Incident-Ticket erstellt

## Phase 2: Eindämmung (30 Min - 2 Stunden)
- [ ] Betroffene Systeme identifiziert
- [ ] Systeme isoliert (falls erforderlich)
- [ ] Accounts gesperrt (falls erforderlich)
- [ ] Netzwerk-Segmentierung aktiviert
- [ ] Forensik-Daten gesichert
- [ ] Weitere Ausbreitung verhindert

## Phase 3: Eradikation (2-8 Stunden)
- [ ] Malware entfernt
- [ ] Backdoors geschlossen
- [ ] Schwachstellen gepatcht
- [ ] Kompromittierte Accounts zurückgesetzt
- [ ] Systeme gehärtet

## Phase 4: Wiederherstellung (8-24 Stunden)
- [ ] Systeme aus sauberem Backup wiederhergestellt
- [ ] Passwörter zurückgesetzt
- [ ] Monitoring intensiviert
- [ ] Systeme schrittweise online gebracht
- [ ] Funktionalität validiert

## Phase 5: Lessons Learned (24-48 Stunden)
- [ ] Postmortem durchgeführt
- [ ] Timeline erstellt
- [ ] Root-Cause identifiziert
- [ ] Verbesserungen definiert
- [ ] Incident-Report erstellt

## Kommunikation
- [ ] Management informiert
- [ ] Betroffene Benutzer informiert
- [ ] Behörden informiert (falls erforderlich)
- [ ] Kunden informiert (falls erforderlich)
- [ ] Medien-Statement (falls erforderlich)

## Compliance
- [ ] DSGVO-Meldepflicht geprüft (72h)
- [ ] Aufsichtsbehörde informiert (falls erforderlich)
- [ ] Betroffene benachrichtigt (falls erforderlich)
- [ ] Dokumentation für Audit

**Incident-Commander:** [Name]
**Forensik-Lead:** [Name]
**Kommunikations-Lead:** [Name]
**Status:** Offen / Eingedämmt / Gelöst
```

## Vorlagen

### Incident-Report-Vorlage

```markdown
# Incident-Report

**Incident-ID:** [INC-XXXXX]
**Datum:** [YYYY-MM-DD]
**Erstellt von:** [Name]

## Executive Summary
[Kurze Zusammenfassung des Incidents für Management]

## Incident-Details
- **Priorität:** P1 / P2 / P3 / P4
- **Kategorie:** [Kategorie]
- **Betroffene Systeme:** [Liste]
- **Betroffene Benutzer:** [Anzahl/Beschreibung]
- **Beginn:** [YYYY-MM-DD HH:MM]
- **Ende:** [YYYY-MM-DD HH:MM]
- **Dauer:** [HH:MM]

## Timeline
| Zeit | Ereignis | Aktion |
|---|---|---|
| HH:MM | [Ereignis] | [Aktion] |
| HH:MM | [Ereignis] | [Aktion] |

## Root Cause
[Detaillierte Beschreibung der Ursache]

## Impact
- **Business-Impact:** [Beschreibung]
- **Finanzielle Auswirkungen:** [Schätzung]
- **Reputations-Schaden:** [Bewertung]
- **Betroffene Services:** [Liste]

## Lösung
[Beschreibung der implementierten Lösung]

## Verbesserungsmaßnahmen
1. [Maßnahme 1] - Verantwortlich: [Name] - Frist: [Datum]
2. [Maßnahme 2] - Verantwortlich: [Name] - Frist: [Datum]
3. [Maßnahme 3] - Verantwortlich: [Name] - Frist: [Datum]

## Lessons Learned
- [Lesson 1]
- [Lesson 2]
- [Lesson 3]

## Anhänge
- [Logs]
- [Screenshots]
- [Monitoring-Daten]

**Erstellt von:** [Name]
**Genehmigt von:** {{ meta-organisation-roles.role_it_operations_manager.name }}
**Datum:** [YYYY-MM-DD]
```

### Change-Request-Vorlage

```markdown
# Change-Request

**Change-ID:** [CHG-XXXXX]
**Datum:** [YYYY-MM-DD]
**Antragsteller:** [Name]

## Change-Details
- **Titel:** [Kurzer Titel]
- **Kategorie:** Standard / Normal / Emergency
- **Priorität:** Niedrig / Mittel / Hoch / Kritisch
- **Geplantes Datum:** [YYYY-MM-DD]
- **Geplante Zeit:** [HH:MM - HH:MM]
- **Dauer:** [Geschätzte Dauer]

## Beschreibung
[Detaillierte Beschreibung des Changes]

## Begründung
[Warum ist dieser Change notwendig?]

## Betroffene Systeme
- [System 1]
- [System 2]
- [System 3]

## Betroffene Benutzer
[Anzahl und Beschreibung der betroffenen Benutzer]

## Risikobewertung
- **Risiko:** Niedrig / Mittel / Hoch
- **Impact:** Niedrig / Mittel / Hoch
- **Wahrscheinlichkeit:** Niedrig / Mittel / Hoch

## Risiken und Mitigationen
| Risiko | Wahrscheinlichkeit | Impact | Mitigation |
|---|---|---|---|
| [Risiko 1] | [L/M/H] | [L/M/H] | [Maßnahme] |
| [Risiko 2] | [L/M/H] | [L/M/H] | [Maßnahme] |

## Implementierungsplan
1. [Schritt 1]
2. [Schritt 2]
3. [Schritt 3]

## Rollback-Plan
1. [Schritt 1]
2. [Schritt 2]
3. [Schritt 3]

## Test-Plan
1. [Test 1]
2. [Test 2]
3. [Test 3]

## Kommunikationsplan
- **Vor Change:** [Wer, Wann, Wie]
- **Während Change:** [Wer, Wann, Wie]
- **Nach Change:** [Wer, Wann, Wie]

## Genehmigungen
- [ ] Technische Genehmigung: [Name] - [Datum]
- [ ] Business-Genehmigung: [Name] - [Datum]
- [ ] CAB-Genehmigung: [Name] - [Datum]

**Antragsteller:** [Name]
**Change-Manager:** {{ meta-organisation-roles.role_it_operations_manager.name }}
**Status:** Beantragt / Genehmigt / Abgelehnt / Implementiert
```

### Postmortem-Vorlage

```markdown
# Postmortem

**Incident-ID:** [INC-XXXXX]
**Datum:** [YYYY-MM-DD]
**Facilitator:** [Name]
**Teilnehmer:** [Namen]

## Incident-Zusammenfassung
[Kurze Zusammenfassung des Incidents]

## Timeline
| Zeit | Ereignis | Wer | Aktion |
|---|---|---|---|
| HH:MM | [Ereignis] | [Name] | [Aktion] |
| HH:MM | [Ereignis] | [Name] | [Aktion] |

## Was lief gut?
- [Punkt 1]
- [Punkt 2]
- [Punkt 3]

## Was lief nicht gut?
- [Punkt 1]
- [Punkt 2]
- [Punkt 3]

## Root Cause
[5-Why-Analyse oder andere Root-Cause-Methode]

1. **Warum trat das Problem auf?** [Antwort]
2. **Warum?** [Antwort]
3. **Warum?** [Antwort]
4. **Warum?** [Antwort]
5. **Warum?** [Antwort]

**Root Cause:** [Finale Ursache]

## Action Items
| # | Aktion | Verantwortlich | Frist | Status |
|---|---|---|---|---|
| 1 | [Aktion] | [Name] | [Datum] | Offen |
| 2 | [Aktion] | [Name] | [Datum] | Offen |
| 3 | [Aktion] | [Name] | [Datum] | Offen |

## Lessons Learned
- [Lesson 1]
- [Lesson 2]
- [Lesson 3]

## Verbesserungen
### Kurzfristig (< 1 Monat)
- [Verbesserung 1]
- [Verbesserung 2]

### Mittelfristig (1-3 Monate)
- [Verbesserung 1]
- [Verbesserung 2]

### Langfristig (> 3 Monate)
- [Verbesserung 1]
- [Verbesserung 2]

**Facilitator:** [Name]
**Datum:** [YYYY-MM-DD]
**Follow-Up:** [Datum für Review der Action Items]
```

## Formulare

### Zugriffs-Anforderungs-Formular

```markdown
# Zugriffs-Anforderung

**Antragsteller:** [Name]
**Datum:** [YYYY-MM-DD]
**Abteilung:** [Abteilung]

## Benutzer-Informationen
- **Name:** [Vollständiger Name]
- **E-Mail:** [E-Mail-Adresse]
- **Telefon:** [Telefonnummer]
- **Abteilung:** [Abteilung]
- **Position:** [Position]
- **Manager:** [Manager-Name]

## Zugriffs-Details
- **System/Anwendung:** [Name]
- **Zugriffs-Level:** Read / Write / Admin
- **Begründung:** [Geschäftliche Begründung]
- **Dauer:** Permanent / Temporär bis [Datum]

## Erforderliche Berechtigungen
- [ ] [Berechtigung 1]
- [ ] [Berechtigung 2]
- [ ] [Berechtigung 3]

## Genehmigungen
- [ ] Manager-Genehmigung: [Name] - [Datum]
- [ ] Data-Owner-Genehmigung: [Name] - [Datum]
- [ ] Security-Genehmigung: [Name] - [Datum]

## IT-Bearbeitung
- **Bearbeitet von:** [Name]
- **Datum:** [YYYY-MM-DD]
- **Zugriff gewährt:** Ja / Nein
- **Kommentare:** [Kommentare]

**Status:** Beantragt / Genehmigt / Abgelehnt / Implementiert
```

### Hardware-Anforderungs-Formular

```markdown
# Hardware-Anforderung

**Antragsteller:** [Name]
**Datum:** [YYYY-MM-DD]
**Abteilung:** [Abteilung]

## Benutzer-Informationen
- **Name:** [Vollständiger Name]
- **E-Mail:** [E-Mail-Adresse]
- **Abteilung:** [Abteilung]
- **Standort:** [Standort]
- **Manager:** [Manager-Name]

## Hardware-Details
- **Typ:** Laptop / Desktop / Monitor / Peripherie / Sonstiges
- **Spezifikation:** [Gewünschte Spezifikation]
- **Begründung:** [Geschäftliche Begründung]
- **Dringlichkeit:** Normal / Hoch / Kritisch

## Alte Hardware (falls Ersatz)
- **Typ:** [Typ]
- **Modell:** [Modell]
- **Seriennummer:** [Seriennummer]
- **Zustand:** [Zustand]
- **Rückgabe:** Ja / Nein

## Kosten
- **Geschätzte Kosten:** [Betrag]
- **Budget-Code:** [Budget-Code]
- **Kostenstelle:** [Kostenstelle]

## Genehmigungen
- [ ] Manager-Genehmigung: [Name] - [Datum]
- [ ] Budget-Genehmigung: [Name] - [Datum]
- [ ] IT-Genehmigung: [Name] - [Datum]

## IT-Bearbeitung
- **Bearbeitet von:** [Name]
- **Bestelldatum:** [YYYY-MM-DD]
- **Lieferdatum:** [YYYY-MM-DD]
- **Installationsdatum:** [YYYY-MM-DD]
- **Asset-Tag:** [Asset-Tag]

**Status:** Beantragt / Genehmigt / Bestellt / Geliefert / Installiert
```

## Prozesse und Verantwortlichkeiten

### RACI-Matrix

| Aktivität | Ops Manager | Ops Team | Service Desk | Benutzer |
|---|---|---|---|---|
| Checklisten-Erstellung | A | R | C | - |
| Vorlagen-Erstellung | A | R | C | - |
| Checklisten-Nutzung | C | R | R | - |
| Vorlagen-Nutzung | C | R | R | R |
| Aktualisierung | A | R | C | - |

> **Legende:** R = Responsible, A = Accountable, C = Consulted, I = Informed

## Compliance und Standards

### Relevante Standards
- **ITIL v4:** Service Operation Practice
- **ISO 20000:** Clause 8.1 - Operational Planning and Control
- **COBIT 2019:** DSS01 - Managed Operations

## Anhang

### Glossar

| Begriff | Definition |
|---|---|
| Checkliste | Strukturierte Liste von Aufgaben oder Prüfpunkten |
| Vorlage | Standardisiertes Dokument-Format |
| Formular | Strukturiertes Eingabe-Dokument |
| Postmortem | Nachträgliche Analyse eines Incidents |

### Referenzen
- ITIL v4 Foundation Handbook
- ISO/IEC 20000-1:2018
- COBIT 2019 Framework

**Letzte Aktualisierung:** {{ meta-handbook.date }}  
**Nächste Review:** [TODO: Datum]  
**Kontakt:** {{ meta-organisation-roles.role_it_operations_manager.email }}

