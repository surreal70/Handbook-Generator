# Richtlinie: Zutritt, Besucher und Schutz von Equipment

**Dokument-ID:** 0490  
**Dokumenttyp:** Richtlinie (detailliert)  
**Zugehörige Policy:** 0480_Policy_Physische_Sicherheit.md  
**Standard-Referenz:** ISO/IEC 27001:2022 Annex A.7.1, A.7.2, A.7.3, A.7.4  
**Owner:** {{ meta.facilities.manager }}  
**Version:** 1.0  
**Status:** Freigegeben  
**Klassifizierung:** Intern  
**Letzte Aktualisierung:** {{ meta.document.date }}

---

## 1. Zweck und Geltungsbereich

Diese Richtlinie konkretisiert die `0480_Policy_Physische_Sicherheit.md` und definiert:
- Zutrittskontrollsysteme und -prozesse
- Besuchermanagement
- Physischer Schutz von IT-Equipment

**Geltungsbereich:** Alle Standorte von **{{ meta.organization.name }}**

## 2. Sicherheitszonen

### 2.1 Zonen-Klassifizierung

**Zone 1 (Öffentlich):**
- Empfangsbereich, Lobby
- Keine Zutrittskontrolle
- Videoüberwachung

**Zone 2 (Intern):**
- Bürobereiche, Besprechungsräume
- Zutrittskarte erforderlich
- Mitarbeiter und registrierte Besucher

**Zone 3 (Eingeschränkt):**
- Serverräume, Rechenzentren
- Zusätzliche Authentifizierung (PIN, Biometrie)
- Nur autorisiertes Personal

**Zone 4 (Hochsicherheit):**
- Kritische Infrastruktur
- Vier-Augen-Prinzip
- Videoüberwachung und Logging

## 3. Zutrittskontrollsystem

### 3.1 Zutrittskarten

**Kartentyp:** RFID-Karten mit Foto  
**Ausgabe:** Bei Onboarding durch HR  
**Gültigkeit:** Bis Vertragsende

**Kartenverlust:**
1. Sofortige Meldung an Security
2. Karte sperren (innerhalb 15 Minuten)
3. Neue Karte ausstellen
4. Dokumentation

### 3.2 Biometrische Authentifizierung

**Für Zone 3/4:**
- Fingerabdruck-Scanner
- Iris-Scanner (optional)
- Datenschutz-konform (DSGVO)

### 3.3 Zugriffsprotokolle

**Logging:**
- Alle Zutrittsversuche (Erfolg und Fehler)
- Timestamp, Person, Tür/Zone
- Retention: {{ meta.retention.access_years }} Jahre

**Monitoring:**
- Alerts bei unautorisierten Zugriffsversuchen
- Alerts bei Zugriff außerhalb Geschäftszeiten (Zone 3/4)

## 4. Besuchermanagement

### 4.1 Besucheranmeldung

**Prozess:**
1. Gastgeber meldet Besucher vorab an (E-Mail, Portal)
2. Besucher meldet sich am Empfang
3. Ausweis-Kontrolle (Personalausweis, Führerschein)
4. Besucherausweis ausgeben
5. Gastgeber abholen

**Besucherausweis:**
- Temporäre RFID-Karte
- Gültigkeit: 1 Tag
- Automatische Deaktivierung nach Ablauf

### 4.2 Begleitung

**Pflicht:**
- Besucher müssen jederzeit begleitet werden
- Keine unbeaufsichtigten Besucher in Zone 2/3/4
- Gastgeber verantwortlich

**Ausnahmen:**
- Langzeit-Auftragnehmer mit eigenem Badge
- Nach Background-Check und NDA

### 4.3 Besucherprotokoll

**Dokumentation:**
- Name, Firma, Ausweisnummer
- Gastgeber, Zweck des Besuchs
- Ein- und Austrittszeit
- Retention: {{ meta.retention.visitor_years }} Jahre

## 5. Physischer Schutz von Equipment

### 5.1 Serverräume und Rechenzentren

**Anforderungen:**
- Klimatisierung (18-27°C, 40-60% Luftfeuchtigkeit)
- Brandmeldeanlage und Löschsystem
- Unterbrechungsfreie Stromversorgung (USV)
- Notstromgenerator
- Wassersensoren (Leckage-Erkennung)

**Zutrittskontrolle:**
- Zone 3 oder 4
- Logging aller Zutritte
- Videoüberwachung

### 5.2 Arbeitsplätze

**Clean Desk Policy:**
- Keine vertraulichen Dokumente auf Schreibtisch (Feierabend)
- Bildschirmsperre bei Abwesenheit
- Abschließbare Schränke für vertrauliche Unterlagen

**Kensington-Locks:**
- Pflicht für Laptops in Büros
- Diebstahlschutz

### 5.3 Mobile Geräte

**Sicherheitsanforderungen:**
- Verschlüsselung (BitLocker, FileVault)
- Remote Wipe-Fähigkeit (MDM)
- Keine vertraulichen Daten lokal (Cloud-Storage bevorzugen)

**Bei Verlust:**
1. Sofortige Meldung an IT-Support
2. Remote Wipe auslösen
3. Incident-Ticket erstellen
4. Polizeimeldung (bei Diebstahl)

## 6. Videoüberwachung

### 6.1 Überwachte Bereiche

**Kameras:**
- Eingänge und Ausgänge
- Serverräume (Zone 3/4)
- Parkplätze
- Keine Überwachung in Büros, Toiletten, Umkleiden

### 6.2 Datenschutz

**DSGVO-Compliance:**
- Hinweisschilder auf Videoüberwachung
- Zweckbindung (Sicherheit, Zutrittskontrolle)
- Zugriff nur für autorisiertes Personal
- Retention: 30 Tage (dann automatische Löschung)

## 7. Notfallzugang

### 7.1 Break-Glass-Verfahren

**Für Notfälle:**
- Physischer Schlüssel in versiegeltem Umschlag
- Aufbewahrung in Safe
- Nutzung nur bei Notfällen (Feuer, medizinischer Notfall)
- Dokumentation jeder Nutzung

### 7.2 Evakuierung

**Evakuierungsplan:**
- Fluchtwege ausgeschildert
- Sammelplätze definiert
- Regelmäßige Evakuierungsübungen (jährlich)

## 8. Compliance und Audit

### 8.1 Messgrößen (KPIs)

| Metrik | Zielwert |
|--------|----------|
| Unbegleitete Besucher | 0 |
| Zutrittskarten-Verluste | < 5 pro Jahr |
| Clean-Desk-Compliance | > 90% |
| Evakuierungsübungen | 1 pro Jahr |

### 8.2 Audit-Nachweise

- Zutrittsprotokolle
- Besucherprotokolle
- Videoaufzeichnungen (30 Tage)
- Evakuierungsübungs-Protokolle

## 9. Referenzen

### Interne Dokumente
- `0480_Policy_Physische_Sicherheit.md`
- `0300_Policy_Asset_Management.md`

### Externe Standards
- **ISO/IEC 27001:2022 Annex A.7.1** - Physical security perimeters
- **ISO/IEC 27001:2022 Annex A.7.2** - Physical entry
- **ISO/IEC 27001:2022 Annex A.7.3** - Securing offices, rooms and facilities
- **ISO/IEC 27001:2022 Annex A.7.4** - Physical security monitoring

---

**Genehmigt durch:** {{ meta.ciso.name }}, CISO  
**Nächster Review:** {{ meta.document.next_review }}
