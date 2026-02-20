# Mitarbeitersicherheit

**Dokument-ID:** HIPAA-0110
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



## 1. Zweck

Dieses Dokument beschreibt die Verfahren zur Mitarbeitersicherheit für AdminSend GmbH, um sicherzustellen, dass alle Mitarbeiter angemessenen Zugang zu ePHI haben und unbefugter Zugriff verhindert wird.

### 1.1 HIPAA-Anforderung

**Standard:** §164.308(a)(3) - Workforce Security (Erforderlich)

**Implementierungsspezifikationen:**
- §164.308(a)(3)(ii)(A) - Autorisierung und/oder Überwachung (Adressierbar)
- §164.308(a)(3)(ii)(B) - Verfahren zur Mitarbeiterfreigabe (Adressierbar)
- §164.308(a)(3)(ii)(C) - Kündigungsverfahren (Adressierbar)

## 2. Autorisierung und Überwachung

### 2.1 Zugriffsautorisierung

**Prinzip:** Der Zugriff auf ePHI wird basierend auf Rolle, Jobfunktion und dem Prinzip der minimalen Notwendigkeit gewährt.

**Autorisierungsprozess:**
1. **Jobanalyse:** Ermittlung der ePHI-Zugriffsanforderungen für die Rolle
2. **Zugriffsanfrage:** Manager reicht Zugriffsanfrage ein
3. **Begründung:** Dokumentation des geschäftlichen Bedarfs
4. **Genehmigung:** Privacy Officer und/oder Security Officer genehmigen
5. **Bereitstellung:** IT stellt Zugriff bereit
6. **Dokumentation:** Zugriff wird protokolliert
7. **Bestätigung:** Mitarbeiter bestätigt Verantwortlichkeiten

**Autorisierungskriterien:**
- Jobrolle erfordert ePHI-Zugriff
- Nur minimal notwendiger Zugriff
- Angemessene Schulung abgeschlossen
- Hintergrundprüfung abgeschlossen (falls erforderlich)
- Vertraulichkeitsvereinbarung unterzeichnet

### 2.2 Überwachungsanforderungen

**Überwachter Zugriff:**
Mitarbeiter mit begrenzter Schulung oder temporärem Status benötigen möglicherweise Überwachung beim Zugriff auf ePHI.

**Überwachungsstufen:**
| Mitarbeitertyp | Überwachung erforderlich | Vorgesetzter | Dauer |
|----------------|-------------------------|--------------|-------|
| Neue Mitarbeiter (< 90 Tage) | Ja | Direkter Vorgesetzter | Bis Schulung abgeschlossen |
| Zeitarbeitskräfte | Ja | Zugewiesener Vorgesetzter | Dauer der Beauftragung |
| Praktikanten/Studenten | Ja | Betreuer/Ausbilder | Dauer des Programms |
| Auftragnehmer (kurzfristig) | Ja | Projektmanager | Dauer des Vertrags |

**Verantwortlichkeiten des Vorgesetzten:**
- Überwachung des ePHI-Zugriffs des Mitarbeiters
- Sicherstellung der Einhaltung von Richtlinien
- Bereitstellung von Anleitung und Schulung
- Meldung von Verstößen
- Dokumentation der Überwachungsaktivitäten

## 3. Verfahren zur Mitarbeiterfreigabe

### 3.1 Voreinstellungsüberprüfung

**Anforderungen an Hintergrundprüfungen:**

**Alle Mitarbeiter mit ePHI-Zugriff:**
- Identitätsüberprüfung
- Überprüfung der Beschäftigungshistorie (7 Jahre)
- Überprüfung der Ausbildung
- Überprüfung der beruflichen Lizenz (falls zutreffend)

**Mitarbeiter mit erhöhtem Zugriff:**
- Kriminelle Hintergrundprüfung
- Bonitätsprüfung (für Finanzrollen)
- Referenzprüfungen (mindestens 3)

**Hintergrundprüfungsprozess:**
1. **Bedingtes Angebot:** Angebot abhängig von Hintergrundprüfung
2. **Autorisierung:** Kandidat autorisiert Hintergrundprüfung
3. **Überprüfung:** Drittanbieter führt Prüfung durch
4. **Prüfung:** HR prüft Ergebnisse
5. **Entscheidung:** Einstellungs-/Nicht-Einstellungsentscheidung
6. **Dokumentation:** Ergebnisse dokumentiert und gesichert
7. **Nachteilige Maßnahme:** FCRA-Anforderungen befolgen, falls nachteilige Maßnahme ergriffen wird

**Hintergrundprüfungsanbieter:** [TODO: Anbietername]

### 3.2 Freigabestufen

| Freigabestufe | Anforderungen | Rollen | ePHI-Zugriff |
|---------------|---------------|--------|--------------|
| Stufe 1 - Basis | Identitätsüberprüfung, Beschäftigungshistorie | Verwaltungspersonal | Begrenzter ePHI |
| Stufe 2 - Standard | Stufe 1 + Ausbildungsüberprüfung | Klinisches Personal | Vollständiger ePHI für Patientenversorgung |
| Stufe 3 - Erhöht | Stufe 2 + kriminelle Hintergrundprüfung | IT-Personal, Abrechnung | Systemebenen-ePHI-Zugriff |
| Stufe 4 - Führungsebene | Stufe 3 + Bonitätsprüfung, Referenzen | Führungskräfte, Compliance | Alle ePHI |

### 3.3 Laufende Freigabe

**Periodische Nachprüfung:**
- **Häufigkeit:** [TODO: Alle 3-5 Jahre oder wie für Rolle erforderlich]
- **Umfang:** Kriminelle Hintergrundprüfung, Lizenzüberprüfung
- **Auslösende Ereignisse:** Beförderung, Rollenwechsel, Sicherheitsvorfall

**Kontinuierliche Überwachung:**
- Status der beruflichen Lizenz
- Sanktionen oder Disziplinarmaßnahmen
- Strafrechtliche Verurteilungen (falls gesetzlich zulässig)

## 4. Kündigungsverfahren

### 4.1 Kündigungsprozess

**Kündigungsarten:**
- Freiwillige Kündigung
- Unfreiwillige Kündigung
- Ruhestand
- Ende des Vertrags/temporäre Beauftragung
- Tod

**Kündigungs-Checkliste:**

**Sofortige Maßnahmen (Tag der Kündigung):**
- [ ] Deaktivierung aller Systemzugriffe (innerhalb 1 Stunde nach Benachrichtigung)
- [ ] Deaktivierung des E-Mail-Kontos
- [ ] Deaktivierung des VPN-Zugriffs
- [ ] Deaktivierung des physischen Zugriffs (Ausweis, Schlüssel)
- [ ] Einsammeln von Firmengeräten (Laptop, Telefon, Tablet)
- [ ] Einsammeln von Zugangsausweisen und Schlüsseln
- [ ] Änderung gemeinsam genutzter Passwörter/Codes, die dem Mitarbeiter bekannt sind
- [ ] Benachrichtigung von IT, Security und Facilities

**Innerhalb von 24 Stunden:**
- [ ] Überprüfung und Archivierung der Dateien des Mitarbeiters
- [ ] Weiterleitung von E-Mails an Manager (falls angemessen)
- [ ] Entfernung aus Verteilerlisten
- [ ] Aktualisierung von Organigrammen
- [ ] Benachrichtigung relevanter Abteilungen
- [ ] Dokumentation der Kündigung im HR-System

**Innerhalb von 1 Woche:**
- [ ] Durchführung eines Austrittsgespräches
- [ ] Erinnerung an Vertraulichkeitsverpflichtungen
- [ ] Einsammeln der unterzeichneten Bestätigung der Verpflichtungen
- [ ] Abschlusszahlung
- [ ] COBRA-Benachrichtigung (falls zutreffend)
- [ ] Überprüfung der Rückgabe von Eigentum

### 4.2 Zugriffskündigung

**Systemzugriffskündigung:**
| System | Kündigungsmethode | Verantwortlich | Überprüfung |
|--------|-------------------|----------------|-------------|
| Active Directory | Konto deaktiviert | IT | Automatisierter Bericht |
| EHR-System | Benutzer deaktiviert | IT | Manuelle Überprüfung |
| E-Mail | Postfach deaktiviert | IT | Automatisierter Bericht |
| VPN | Zertifikat widerrufen | IT | Manuelle Überprüfung |
| Physischer Zugang | Ausweis deaktiviert | Facilities | Zugriffsprotokollprüfung |

**Kündigungsüberprüfung:**
- IT erstellt Kündigungsbericht
- Security Officer prüft Bericht
- Ausnahmen werden untersucht und behoben
- Dokumentation wird aufbewahrt

### 4.3 Wissenstransfer

**Wissenstransferprozess:**
1. **Identifikation:** Identifikation kritischen Wissens und Verantwortlichkeiten
2. **Dokumentation:** Dokumentation von Prozessen und Verfahren
3. **Schulung:** Schulung von Ersatz oder Teammitgliedern
4. **Übergang:** Schrittweiser Übergang von Verantwortlichkeiten (falls möglich)
5. **Überprüfung:** Überprüfung, dass Wissenstransfer abgeschlossen ist

**Kritische Wissensbereiche:**
- Systemzugriff und Passwörter
- Laufende Projekte
- Wichtige Kontakte
- Ausstehende Probleme
- Dokumentationsspeicherorte

### 4.4 Überwachung nach Kündigung

**Überwachungsaktivitäten:**
- Überprüfung von Audit-Protokollen für gekündigte Mitarbeiterkonten
- Überwachung auf unbefugte Zugriffsversuche
- Überprüfung auf Datenexfiltration
- Überwachung auf Richtlinienverstöße vor Kündigung

**Überwachungszeitraum:** [TODO: 90 Tage nach Kündigung]

## 5. Rollenbasierte Zugriffskontrolle (RBAC)

### 5.1 Rollendefinitionen

| Rollen-ID | Rollenname | Abteilung | ePHI-Zugriffsstufe | Systeme | Genehmigung erforderlich |
|-----------|------------|-----------|-------------------|---------|--------------------------|
| [TODO: ROLE-001] | Arzt | Klinisch | Vollständige Patientenversorgung | EHR, Labor, Bildgebung | Ärztlicher Direktor |
| [TODO: ROLE-002] | Krankenschwester | Klinisch | Vollständige Patientenversorgung | EHR, Medikation | Pflegedienstleitung |
| [TODO: ROLE-003] | Medizinischer Assistent | Klinisch | Begrenzt | EHR (Vitalwerte, Terminplanung) | Klinischer Manager |
| [TODO: ROLE-004] | Abrechnungsspezialist | Abrechnung | Nur Abrechnungsdaten | Abrechnungssystem | Abrechnungsmanager |
| [TODO: ROLE-005] | IT-Administrator | IT | Systemadministrator | Alle Systeme | IT-Manager + Security Officer |
| [TODO: ROLE-006] | Rezeptionist | Empfang | Nur demografische Daten | EHR (Terminplanung) | Büroleiter |

### 5.2 Zugriffsmatrix

| Rolle | Patientendemografie | Klinische Notizen | Laborergebnisse | Medikamente | Abrechnung | Systemadministrator |
|-------|---------------------|-------------------|-----------------|-------------|------------|---------------------|
| Arzt | Lesen/Schreiben | Lesen/Schreiben | Lesen/Schreiben | Lesen/Schreiben | Lesen | Nein |
| Krankenschwester | Lesen/Schreiben | Lesen/Schreiben | Lesen | Lesen/Schreiben | Nein | Nein |
| Medizinischer Assistent | Lesen/Schreiben | Lesen | Lesen | Nein | Nein | Nein |
| Abrechnungsspezialist | Lesen | Nein | Nein | Nein | Lesen/Schreiben | Nein |
| IT-Administrator | Nein* | Nein* | Nein* | Nein* | Nein* | Ja |
| Rezeptionist | Lesen/Schreiben | Nein | Nein | Nein | Nein | Nein |

*IT-Administratoren haben technischen Zugriff, sollten aber nicht auf ePHI zugreifen, es sei denn, dies ist für die Fehlerbehebung erforderlich

## 6. Schulungsanforderungen

### 6.1 Schulung zur Mitarbeitersicherheit

**Erstschulung (Innerhalb von 30 Tagen nach Einstellung):**
- HIPAA-Überblick
- Richtlinien zur Mitarbeitersicherheit
- Zugriffskontrollverfahren
- Passwortanforderungen
- Vertraulichkeitsverpflichtungen
- Sanktionen bei Verstößen

**Jährliche Schulung:**
- Auffrischung zur Mitarbeitersicherheit
- Richtlinienaktualisierungen
- Fallstudien
- Neue Bedrohungen

**Rollenspezifische Schulung:**
- Vorgesetzte: Überwachungsverantwortlichkeiten
- IT-Personal: Technische Schutzmaßnahmen
- Manager: Verfahren zur Zugriffsgenehmigung

### 6.2 Schulungsdokumentation

**Erforderliche Dokumentation:**
- Schulungsteilnahmeprotokolle
- Schulungsmaterialien
- Testergebnisse (falls zutreffend)
- Bestätigung des Verständnisses
- Schulungszertifikate

**Aufbewahrung:** [TODO: 6 Jahre]

## 7. Vertraulichkeitsvereinbarungen

### 7.1 Anforderungen an Vertraulichkeitsvereinbarungen

**Alle Mitarbeiter müssen unterzeichnen:**
- Vertraulichkeitsvereinbarung
- Richtlinie zur akzeptablen Nutzung
- HIPAA-Bestätigung
- Sicherheitsrichtlinienbestätigung

**Zeitpunkt:**
- Vor Gewährung des Zugriffs auf ePHI
- Bei Richtlinienänderungen (erneute Bestätigung)
- Jährlich (erneute Bestätigung)

### 7.2 Vereinbarungsinhalt

**Vertraulichkeitsvereinbarung muss enthalten:**
- Verpflichtung zum Schutz von PHI/ePHI
- Verbot unbefugten Zugriffs
- Verbot unbefugter Offenlegung
- Meldepflichten für Vorfälle
- Sanktionen bei Verstößen
- Verpflichtungen bestehen nach Kündigung fort
- Bestätigung des Verständnisses

**Vereinbarungsspeicherung:** [TODO: HR-Personalakten, elektronisches Repository]

## 8. Überwachung und Compliance

### 8.1 Überwachung der Mitarbeitersicherheit

**Überwachungsaktivitäten:**
- Überprüfung von Zugriffsprotokollen
- Untersuchungen unangemessenen Zugriffs
- Audits zur Richtlinieneinhaltung
- Verfolgung der Schulungsabschlüsse
- Compliance bei Hintergrundprüfungen
- Compliance bei Kündigungsverfahren

**Überwachungshäufigkeit:**
| Aktivität | Häufigkeit | Verantwortlich |
|-----------|-----------|----------------|
| Zugriffsprotokollprüfung | Monatlich | Security Officer |
| Schulungs-Compliance | Vierteljährlich | HR + Privacy Officer |
| Hintergrundprüfungs-Compliance | Jährlich | HR |
| Kündigungsverfahrensaudit | Vierteljährlich | Security Officer |

### 8.2 Compliance-Metriken

| Metrik | Ziel | Aktuell | Status |
|--------|------|---------|--------|
| Schulungsabschlussrate | 100% | [TODO: %] | [TODO: Grün/Gelb/Rot] |
| Hintergrundprüfungen abgeschlossen | 100% | [TODO: %] | [TODO: Grün/Gelb/Rot] |
| Kündigungsverfahren befolgt | 100% | [TODO: %] | [TODO: Grün/Gelb/Rot] |
| Zugriffsüberprüfungen abgeschlossen | 100% | [TODO: %] | [TODO: Grün/Gelb/Rot] |

## 9. Dokumentation und Aufzeichnungen

### 9.1 Erforderliche Dokumentation

- Zugriffsautorisierungsformulare
- Hintergrundprüfungsergebnisse
- Vertraulichkeitsvereinbarungen
- Schulungsunterlagen
- Kündigungs-Checklisten
- Überprüfung der Zugriffskündigung
- Überwachungsprotokolle
- Vorfallberichte

### 9.2 Aufbewahrung

**Aufbewahrungsfrist:** [TODO: 6 Jahre ab Beendigung des Arbeitsverhältnisses oder letztem Gültigkeitsdatum]

**Speicherort:** [TODO: HR-System, Dokumentenmanagementsystem]

**Dokumentenhistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | [TODO] | Handbook-Generator | Ersterstellung |



