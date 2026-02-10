# Einrichtungszugangskontrollen

**Dokument-ID:** HIPAA-0300  
**Organisation:** AdminSend GmbH  
**Verantwortlich:** IT Operations Manager  
**Genehmigt durch:** CIO  
**Version:** 1.0.0  
**Status:** Entwurf / In Prüfung / Genehmigt  
**Klassifizierung:** internal  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  

---



## 1. Zweck

Dieses Dokument beschreibt die Einrichtungszugangskontrollen für AdminSend GmbH, um den physischen Zugang zu elektronischen Informationssystemen und den Einrichtungen, in denen sie untergebracht sind, zu begrenzen und gleichzeitig ordnungsgemäß autorisierten Zugang zu ermöglichen.

### 1.1 HIPAA-Anforderung

**Standard:** §164.310(a)(1) - Facility Access Controls (Erforderlich)

**Implementierungsspezifikationen:**
- §164.310(a)(2)(i) - Notfallbetrieb (Adressierbar)
- §164.310(a)(2)(ii) - Einrichtungssicherheitsplan (Adressierbar)
- §164.310(a)(2)(iii) - Zugriffskontroll- und Validierungsverfahren (Adressierbar)
- §164.310(a)(2)(iv) - Wartungsaufzeichnungen (Adressierbar)

## 2. Einrichtungsinventar

### 2.1 Einrichtungen mit ePHI

| Einrichtungs-ID | Einrichtungsname | Adresse | Typ | ePHI-Systeme | Zugriffsstufe |
|-----------------|------------------|---------|-----|--------------|---------------|
| [TODO: FAC-001] | Hauptrechenzentrum | [TODO: Adresse] | Rechenzentrum | Alle Produktionssysteme | Eingeschränkt |
| [TODO: FAC-002] | Hauptklinik | [TODO: Adresse] | Klinisch | EHR-Workstations | Kontrolliert |
| [TODO: FAC-003] | Verwaltungsbüro | [TODO: Adresse] | Büro | Abrechnungssysteme | Kontrolliert |
| [TODO: FAC-004] | Backup-Standort | [TODO: Adresse] | DR-Standort | Backup-Systeme | Eingeschränkt |

### 2.2 Einrichtungsklassifizierung

**Eingeschränkter Zugang:**
- Rechenzentren
- Serverräume
- Netzwerkgeräteräume
- Backup-Speicherbereiche

**Kontrollierter Zugang:**
- Klinische Bereiche
- Verwaltungsbüros
- Patientenaktenräume

**Öffentlicher Zugang:**
- Wartezimmer
- Öffentliche Korridore
- Cafeteria

## 3. Notfallbetrieb

### 3.1 Notfallzugangsverfahren

**Zweck:** Verfahren festlegen, um Einrichtungszugang zur Unterstützung der Wiederherstellung verlorener Daten im Rahmen des Disaster-Recovery- und Notfallbetriebsplans zu ermöglichen.

**Notfallszenarien:**
- Feuer oder Naturkatastrophe
- Stromausfall
- Systemausfall, der sofortigen Zugang erfordert
- Sicherheitsvorfall, der Untersuchung erfordert

**Notfallzugangsprozess:**
1. **Autorisierung:** Security Officer oder Beauftragter autorisiert Notfallzugang
2. **Begleitung:** Notfallpersonal wird von autorisiertem Personal begleitet
3. **Dokumentation:** Aller Notfallzugang wird protokolliert
4. **Wiederherstellung:** Normale Zugangskontrollen nach Notfall wiederhergestellt
5. **Überprüfung:** Nachträgliche Überprüfung des Notfallzugangs

**Notfallkontakte:**
| Rolle | Name | Telefon (24/7) | Backup |
|-------|------|----------------|--------|
| Security Officer | {{ meta.roles.security_officer.name }} | [TODO: Telefon] | [TODO: Backup-Name/Telefon] |
| Facility Manager | [TODO: Name] | [TODO: Telefon] | [TODO: Backup] |
| IT Manager | [TODO: Name] | [TODO: Telefon] | [TODO: Backup] |

### 3.2 Notfallzugangsausrüstung

**Notfallzugangswerkzeuge:**
- Hauptschlüssel (gesichert in Notfallbox)
- Zugangskarten (Notfall-Override)
- Schlossumgehungswerkzeuge (nur autorisiertes Personal)
- Notbeleuchtung
- Kommunikationsgeräte

**Speicherort:** [TODO: Sicherer Ort mit dokumentiertem Zugang]

## 4. Einrichtungssicherheitsplan

### 4.1 Physische Sicherheitsmaßnahmen

**Perimetersicherheit:**
- Zaun: [TODO: Ja/Nein, Beschreibung]
- Tore: [TODO: Ja/Nein, Beschreibung]
- Beleuchtung: [TODO: Beschreibung]
- Beschilderung: [TODO: "Nur autorisiertes Personal"-Schilder]
- Landschaftsgestaltung: [TODO: Klare Sichtlinien]

**Gebäudesicherheit:**
- Außentüren: [TODO: Anzahl, Schließmechanismen]
- Fenster: [TODO: Sicherheitsmaßnahmen]
- Ladedocks: [TODO: Sicherheitsmaßnahmen]
- Dachzugang: [TODO: Sicherheitsmaßnahmen]

**Innensicherheit:**
- Empfang/Sicherheitsschalter: [TODO: Ja/Nein, Öffnungszeiten]
- Sicherheitspersonal: [TODO: Ja/Nein, Zeitplan]
- Besucherverwaltung: [TODO: System/Prozess]
- Begleitanforderungen: [TODO: Bereiche, die Begleitung erfordern]

**Rechenzentrum/Serverraum-Sicherheit:**
- Dedizierter Raum: [TODO: Ja/Nein]
- Verstärkte Wände: [TODO: Ja/Nein]
- Doppelboden: [TODO: Ja/Nein]
- Brandbekämpfung: [TODO: Typ]
- Umgebungsüberwachung: [TODO: Temperatur, Luftfeuchtigkeit]
- Wassererkennung: [TODO: Ja/Nein]
- Notstromversorgung: [TODO: USV, Generator]

### 4.2 Zugriffskontrollsysteme

**Physisches Zugriffskontrollsystem:**
- **Systemtyp:** [TODO: Kartenleser, biometrisch, Tastenfeld]
- **Anbieter:** [TODO: Anbietername]
- **Abdeckung:** [TODO: Abgedeckte Türen/Bereiche]
- **Überwachung:** [TODO: 24/7-Überwachung, Alarme]

**Zugriffskontrollfunktionen:**
- Individuelle Identifikation
- Zeitbasierte Zugriffsbeschränkungen
- Bereichsbasierte Zugriffsbeschränkungen
- Anti-Passback
- Audit-Protokollierung
- Echtzeitalarme

**Zugangskartenverwaltung:**
- Kartenausgabeprozess
- Kartendeaktivierungsprozess
- Verfahren bei verlorenen/gestohlenen Karten
- Kartenrückgabe bei Kündigung

### 4.3 Überwachungssysteme

**Videoüberwachung:**
- **Abdeckung:** [TODO: Eingänge, Ausgänge, Serverräume usw.]
- **Kameratyp:** [TODO: Fest, PTZ, Auflösung]
- **Aufzeichnung:** [TODO: Kontinuierlich, bewegungsaktiviert]
- **Aufbewahrung:** [TODO: Tage/Monate]
- **Überwachung:** [TODO: Live-Überwachung, Überprüfungszeitplan]

**Überwachungsstandorte:**
| Standort | Kameraanzahl | Aufzeichnung | Aufbewahrung | Zweck |
|----------|--------------|--------------|--------------|-------|
| [TODO: Haupteingang] | [TODO: 2] | Kontinuierlich | [TODO: 90 Tage] | Zugangsüberwachung |
| [TODO: Serverraum] | [TODO: 1] | Kontinuierlich | [TODO: 90 Tage] | Sicherheitsüberwachung |
| [TODO: Parkplatz] | [TODO: 4] | Bewegung | [TODO: 30 Tage] | Perimetersicherheit |


## 5. Zugriffskontroll- und Validierungsverfahren

### 5.1 Zugriffsautorisierung

**Autorisierungsprozess:**
1. **Anfrage:** Manager reicht Zugriffsanfrage ein
2. **Begründung:** Geschäftlicher Bedarf dokumentiert
3. **Genehmigung:** Security Officer genehmigt
4. **Bereitstellung:** Facility Manager stellt Zugriff bereit
5. **Dokumentation:** Zugriff im System protokolliert
6. **Benachrichtigung:** Mitarbeiter über gewährten Zugriff benachrichtigt

**Zugriffsstufen:**
| Stufe | Beschreibung | Erforderliche Autorisierung | Zugängliche Bereiche |
|-------|--------------|----------------------------|----------------------|
| Stufe 1 - Öffentlich | Allgemeine Öffentlichkeit | Keine | Wartebereiche, öffentliche Korridore |
| Stufe 2 - Mitarbeiter | Reguläre Mitarbeiter | Manager-Genehmigung | Bürobereiche, Pausenräume |
| Stufe 3 - Klinisch | Klinisches Personal | Manager + Privacy Officer | Klinische Bereiche, Patientenakten |
| Stufe 4 - IT | IT-Personal | IT-Manager + Security Officer | Serverräume, Netzwerkschränke |
| Stufe 5 - Führungsebene | Führungszugang | CEO-Genehmigung | Alle Bereiche |

### 5.2 Besucherverwaltung

**Besucherverfahren:**
1. **Check-in:** Besucher meldet sich am Empfang an
2. **Identifikation:** Lichtbildausweis erforderlich und aufgezeichnet
3. **Ausweis:** Besucherausweis ausgestellt
4. **Begleitung:** Besucher wird in eingeschränkten Bereichen jederzeit begleitet
5. **Protokoll:** Besuch protokolliert (Name, Firma, Zweck, Zeit ein/aus, Gastgeber)
6. **Check-out:** Besucher gibt Ausweis zurück und meldet sich ab

**Besuchertypen:**
- Lieferanten/Auftragnehmer
- Business Associates
- Auditoren
- Gäste
- Lieferpersonal

**Besucherausweis:** Deutlich mit "BESUCHER" gekennzeichneter Ausweis, andere Farbe als Mitarbeiterausweise

### 5.3 Zugriffvalidierung

**Zugriffsüberprüfungsprozess:**
- **Häufigkeit:** Vierteljährlich
- **Prüfer:** Facility Manager + Security Officer
- **Umfang:** Alle aktiven Zugriffsberechtigungen
- **Maßnahmen:** Unnötigen Zugriff widerrufen, Aufzeichnungen aktualisieren

**Zugriffvalidierungs-Checkliste:**
- [ ] Überprüfen, ob Mitarbeiter noch Zugriff benötigt
- [ ] Überprüfen, ob Zugriffsstufe für Rolle angemessen ist
- [ ] Überprüfen, dass keine gekündigten Mitarbeiter aktiven Zugriff haben
- [ ] Überprüfen, dass kein abgelaufener temporärer Zugriff besteht
- [ ] Zugriffsdokumentation aktualisieren

### 5.4 Zugriffskündigung

**Kündigungsprozess:**
1. **Benachrichtigung:** HR benachrichtigt Facility Manager und Security Officer
2. **Sofortiger Widerruf:** Zugriff wird sofort bei Kündigung widerrufen
3. **Ausweiseinsammlung:** Mitarbeiterausweis eingesammelt
4. **Schlüsseleinsammlung:** Alle Schlüssel eingesammelt
5. **Überprüfung:** Zugriffskündigung im System überprüft
6. **Dokumentation:** Kündigung protokolliert

**Kündigungs-Checkliste:**
- [ ] Zugangskarte deaktiviert
- [ ] Schlüssel zurückgegeben
- [ ] Alarmcodes geändert (falls zutreffend)
- [ ] Besucherbegleitrechte widerrufen
- [ ] Dokumentation aktualisiert

## 6. Wartungsaufzeichnungen

### 6.1 Einrichtungswartung

**Wartungsaktivitäten:**
- Wartung des Zugriffskontrollsystems
- Wartung des Überwachungssystems
- Schloss- und Schlüsselwartung
- Alarmsystemwartung
- Brandbekämpfungssystemwartung
- Wartung der Umgebungskontrollen
- Notbeleuchtungswartung

**Wartungsplan:**
| System | Wartungstyp | Häufigkeit | Anbieter | Letzter Service | Nächster Service |
|--------|-------------|-----------|----------|-----------------|------------------|
| [TODO: Zugriffskontrolle] | Präventiv | Vierteljährlich | [TODO: Anbieter] | [TODO: Datum] | [TODO: Datum] |
| [TODO: Überwachung] | Präventiv | Halbjährlich | [TODO: Anbieter] | [TODO: Datum] | [TODO: Datum] |
| [TODO: Brandbekämpfung] | Inspektion | Jährlich | [TODO: Anbieter] | [TODO: Datum] | [TODO: Datum] |

### 6.2 Wartungsdokumentation

**Erforderliche Dokumentation:**
- Wartungsarbeitsaufträge
- Serviceberichte
- Ersetzte Teile
- Durchgeführte Systemtests
- Technikerqualifikationen
- Zugriffsprotokolle für Wartungspersonal

**Aufbewahrung:** [TODO: 6 Jahre]

### 6.3 Wartungszugriffskontrolle

**Anbieterzugang:**
- Anbieter wird während Wartung begleitet
- Anbieterzugang wird protokolliert
- Anbieterqualifikationen werden überprüft
- Hintergrundprüfungen für reguläre Anbieter
- Business Associate Agreement (falls PHI-Zugriff möglich)

## 7. Physische Sicherheitsvorfälle

### 7.1 Vorfalltypen

- Unbefugter Einrichtungszugang
- Tailgating
- Verlorene/gestohlene Zugangskarten oder Schlüssel
- Gewaltsamer Zutritt
- Manipulation des Überwachungssystems
- Alarmsystemausfälle

### 7.2 Vorfallreaktion

**Reaktionsprozess:**
1. **Erkennung:** Vorfall erkannt (Alarm, Beobachtung, Meldung)
2. **Benachrichtigung:** Security Officer sofort benachrichtigt
3. **Bewertung:** Schweregrad und Auswirkung bewerten
4. **Eindämmung:** Bereich sichern, Zugriffscodes bei Bedarf ändern
5. **Untersuchung:** Protokolle, Überwachungsaufnahmen überprüfen
6. **Behebung:** Korrekturmaßnahmen umsetzen
7. **Dokumentation:** Vorfall und Reaktion dokumentieren
8. **Überprüfung:** Nachträgliche Überprüfung und Lessons Learned

### 7.3 Vorfallprotokoll

| Vorfall-ID | Datum | Typ | Standort | Beschreibung | Reaktion | Status |
|------------|-------|-----|----------|--------------|----------|--------|
| [TODO: INC-001] | [TODO: Datum] | [TODO: Typ] | [TODO: Standort] | [TODO: Beschreibung] | [TODO: Ergriffene Maßnahmen] | [TODO: Geschlossen] |

## 8. Dokumentation und Aufzeichnungen

### 8.1 Erforderliche Dokumentation

- Einrichtungssicherheitsplan
- Zugriffsautorisierungsaufzeichnungen
- Besucherprotokolle
- Zugriffsüberprüfungsaufzeichnungen
- Wartungsaufzeichnungen
- Vorfallberichte
- Überwachungsaufnahmen (gemäß Aufbewahrungsrichtlinie)

### 8.2 Aufbewahrung

**Aufbewahrungsfrist:** [TODO: 6 Jahre ab Erstellung oder letztem Gültigkeitsdatum]

**Speicherort:** [TODO: Dokumentenmanagementsystem-Standort]

---

**Dokumentenhistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Ersterstellung |


