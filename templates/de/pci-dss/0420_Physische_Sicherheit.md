# Physische Sicherheit

**Dokument-ID:** PCI-0420
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Genehmigt durch:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Klassifizierung:** {{ meta-handbook.classification }}
**Letzte Aktualisierung:** {{ meta-handbook.modifydate }}

---

---

<!-- 
TEMPLATE AUTHOR NOTE:
This template documents physical security controls.
It aligns with PCI-DSS v4.0 Requirement 9 (Restrict Physical Access to Cardholder Data).

Customization required:
- Define physical access controls
- Document facility security
- Include visitor management
- Define media handling procedures
-->

## 1. Zweck

Dieses Dokument definiert die physischen Sicherheitskontrollen für {{ meta-organisation.name }} gemäß PCI-DSS Requirement 9.

### 1.1 Ziele

- **Physischer Schutz:** Schutz von CDE-Systemen vor unbefugtem Zugriff
- **Zutrittskontrolle:** Restriktion des physischen Zugangs
- **Medien-Sicherheit:** Sichere Handhabung von Datenträgern
- **Compliance:** Erfüllung von PCI-DSS Requirement 9

### 1.2 Geltungsbereich

**Betroffene Standorte:**
- Rechenzentren mit CDE-Systemen
- Serverräume
- Büros mit POS-Terminals
- Lagerräume für Medien

## 2. Physische Zutrittskontrolle

### 2.1 Zutrittskontrollsysteme

**Implementierte Systeme:**
- Badge-System: [TODO: Name des Systems]
- Biometrische Authentifizierung: [TODO: Typ]
- Videoüberwachung: [TODO: Anzahl Kameras]
- Alarmsystem: [TODO: Name des Systems]

**Anforderungen:**
- Eindeutige Identifikation jeder Person
- Logging aller Zutritte
- Automatische Sperrung nach Geschäftszeiten
- Alarmierung bei unbefugtem Zutritt

### 2.2 Zutrittsberechtigung

**Berechtigungsstufen:**

| Stufe | Berechtigung | Bereiche | Personen |
|-------|--------------|----------|----------|
| Stufe 1 | Vollzugriff | Alle Bereiche | Facility Manager, CISO |
| Stufe 2 | CDE-Zugriff | Rechenzentrum, Serverräume | IT-Administratoren |
| Stufe 3 | Eingeschränkt | Büros mit POS | Kassierer, Support |
| Stufe 4 | Begleitet | Alle Bereiche | Besucher, Dienstleister |

**Genehmigungsprozess:**
1. Antrag durch Manager
2. Security-Prüfung
3. CISO-Genehmigung (für CDE-Bereiche)
4. Badge-Ausgabe
5. Dokumentation

### 2.3 Zutrittskontrolle Rechenzentrum

**Anforderungen:**
- Zwei-Faktor-Authentifizierung (Badge + Biometrie)
- Mantrap/Schleuse
- Videoüberwachung (24/7)
- Alarmierung bei unbefugtem Zutritt
- Logging aller Zutritte

**Autorisierte Personen:**
- Datacenter-Personal
- Autorisierte IT-Administratoren
- Wartungspersonal (nur mit Begleitung)

**Besucherregelung:**
- Voranmeldung erforderlich
- Begleitpflicht
- Besucherausweis
- Logging

## 3. Besuchermanagement

### 3.1 Besucheranmeldung

**Prozess:**
1. Voranmeldung durch Gastgeber
2. Identitätsprüfung bei Ankunft
3. Besucherausweis ausgeben
4. Sicherheitsbelehrung
5. Begleitung durch autorisierten Mitarbeiter
6. Rückgabe des Ausweises bei Verlassen

**Besucherausweis:**
- Deutlich sichtbar
- Zeitlich begrenzt
- Eindeutige Nummer
- Foto (optional)

### 3.2 Besucherbegleitung

**Anforderungen:**
- Ständige Begleitung in CDE-Bereichen
- Begleiter muss autorisiert sein
- Keine unbeaufsichtigten Besucher
- Dokumentation der Begleitung

**Ausnahmen:**
- Öffentliche Bereiche (Empfang, Cafeteria)
- Nur nach Sicherheitsbelehrung

### 3.3 Besucherprotokoll

**Geloggte Informationen:**
- Name des Besuchers
- Firma
- Zweck des Besuchs
- Gastgeber
- Ankunftszeit
- Abfahrtszeit
- Besuchte Bereiche
- Begleiter

**Aufbewahrung:** 90 Tage

## 4. Mitarbeiter-Identifikation

### 4.1 Mitarbeiterausweise

**Anforderungen:**
- Foto-ID
- Name
- Mitarbeiternummer
- Abteilung
- Gültigkeitsdatum
- Sichtbar zu tragen

**Ausgabe:**
- Bei Einstellung
- Nach Identitätsprüfung
- Dokumentation

**Rückgabe:**
- Bei Ausscheiden
- Bei Verlust (Sperrung + Neuausgabe)

### 4.2 Unterscheidung Mitarbeiter/Besucher

**Maßnahmen:**
- Unterschiedliche Ausweisfarben
- Deutliche Kennzeichnung "BESUCHER"
- Zeitlich begrenzte Besucherausweise

## 5. Videoüberwachung

### 5.1 Kamerastandorte

**Überwachte Bereiche:**
- Alle Eingänge zum Rechenzentrum
- Serverräume
- Bereiche mit POS-Terminals
- Lagerräume für Medien
- Parkplätze (optional)

**Kamera-Spezifikationen:**
- Mindestauflösung: 1080p
- Nachtsicht-fähig
- Bewegungserkennung
- Manipulationsschutz

### 5.2 Aufzeichnung und Speicherung

**Anforderungen:**
- Kontinuierliche Aufzeichnung (24/7)
- Aufbewahrung: 90 Tage
- Sichere Speicherung (verschlüsselt)
- Zugriffskontrolle auf Aufzeichnungen
- Backup der Aufzeichnungen

**Zugriff auf Aufzeichnungen:**
- Nur autorisiertes Personal
- Logging aller Zugriffe
- Genehmigung durch Security Manager

### 5.3 Datenschutz

**Maßnahmen:**
- Hinweisschilder auf Videoüberwachung
- Datenschutzerklärung
- Keine Überwachung von Privatbereichen (Toiletten, Umkleiden)
- Einhaltung DSGVO

## 6. Medien-Handling

### 6.1 Medien-Klassifizierung

**Klassifizierungsstufen:**

| Stufe | Beschreibung | Beispiele | Handhabung |
|-------|--------------|-----------|------------|
| Kritisch | CHD im Klartext | Backup-Tapes mit unverschlüsselten CHD | Verschlüsselt, gesichert |
| Vertraulich | CHD verschlüsselt | Verschlüsselte Backups | Gesichert |
| Intern | Keine CHD | Systemlogs | Standard |
| Öffentlich | Keine sensiblen Daten | Marketing-Material | Keine Einschränkung |

### 6.2 Medien-Lagerung

**Anforderungen:**
- Gesicherter Lagerraum
- Zutrittskontrolle
- Klimatisierung
- Brandschutz
- Inventarverwaltung

**Lagerraum-Spezifikationen:**
- Feuerfeste Schränke für kritische Medien
- Verschlossene Schränke
- Zutrittskontrolle (Badge-System)
- Videoüberwachung
- Logging aller Zugriffe

### 6.3 Medien-Transport

**Interner Transport:**
- Versiegelte Container
- Begleitperson
- Dokumentation (Übergabeprotokoll)

**Externer Transport:**
- Verschlüsselte Medien
- Versiegelte Container
- Vertrauenswürdiger Kurier
- Tracking
- Versicherung
- Dokumentation

**Kurier-Anforderungen:**
- Hintergrundprüfung
- Vertraulichkeitsvereinbarung
- Versicherung
- Tracking-System

## 7. Medien-Vernichtung

### 7.1 Vernichtungsmethoden

**Papier:**
- Kreuzschnitt-Schredder (DIN 66399 P-4 oder höher)
- Für CHD: P-5 oder höher
- Sichere Entsorgung der Schnipsel

**Elektronische Medien:**

| Medientyp | Methode | Standard |
|-----------|---------|----------|
| Festplatten | Degaussing + physische Zerstörung | NIST 800-88 |
| SSDs | Kryptografisches Löschen + Zerstörung | NIST 800-88 |
| USB-Sticks | Physische Zerstörung | NIST 800-88 |
| CDs/DVDs | Schreddern | DIN 66399 O-4 |
| Backup-Tapes | Degaussing + Schreddern | NIST 800-88 |

**Zertifizierung:**
- Vernichtungszertifikat erforderlich
- Dokumentation aller vernichteten Medien
- Seriennummern erfassen

### 7.2 Vernichtungsdienstleister

**Anforderungen:**
- Zertifizierter Dienstleister (z.B., DIN 66399)
- Vertraulichkeitsvereinbarung
- Vor-Ort-Vernichtung oder sichere Abholung
- Vernichtungszertifikat
- Versicherung

**Dienstleister:** [TODO: Name des Dienstleisters]

### 7.3 Vernichtungsprotokoll

**Geloggte Informationen:**
- Datum der Vernichtung
- Medientyp
- Seriennummer (falls vorhanden)
- Vernichtungsmethode
- Durchgeführt von
- Zertifikatsnummer

**Aufbewahrung:** 3 Jahre

## 8. Point-of-Sale (POS) Sicherheit

### 8.1 POS-Terminal-Schutz

**Physische Sicherheit:**
- Manipulationsschutz (Tamper-evident Seals)
- Regelmäßige Inspektion
- Sichere Befestigung
- Videoüberwachung des Bereichs

**Inspektion:**
- Täglich vor Geschäftsbeginn
- Nach Wartung
- Bei Verdacht auf Manipulation

**Checkliste:**
- [ ] Tamper-Seal intakt
- [ ] Keine ungewöhnlichen Geräte angeschlossen
- [ ] Keine Beschädigungen
- [ ] Firmware-Version korrekt

### 8.2 POS-Terminal-Inventar

**Inventarverwaltung:**
- Liste aller POS-Terminals
- Seriennummern
- Standorte
- Verantwortliche Personen
- Wartungshistorie

**Quartalsweise Überprüfung:**
- Inventar validieren
- Standorte überprüfen
- Tamper-Seals prüfen
- Dokumentation

### 8.3 POS-Terminal-Wartung

**Wartungsprozess:**
1. Wartung ankündigen
2. Begleitung durch autorisierten Mitarbeiter
3. Dokumentation aller Aktivitäten
4. Neue Tamper-Seals anbringen
5. Funktionstest
6. Dokumentation

## 9. Medien-Backup

### 9.1 Backup-Medien-Sicherheit

**Anforderungen:**
- Verschlüsselte Backups
- Sichere Lagerung
- Offsite-Lagerung
- Zutrittskontrolle
- Inventarverwaltung

**Lagerung:**
- Onsite: Feuerfester Tresor
- Offsite: Sicheres Rechenzentrum oder Tresorraum

### 9.2 Backup-Medien-Transport

**Prozess:**
- Verschlüsselte Medien
- Versiegelte Container
- Vertrauenswürdiger Kurier
- Übergabeprotokoll
- Dokumentation

## 10. Arbeitsplatz-Sicherheit

### 10.1 Clean Desk Policy

**Anforderungen:**
- Keine sensiblen Dokumente auf Schreibtischen
- Bildschirme sperren bei Abwesenheit
- Dokumente in verschlossenen Schränken
- Keine Passwörter auf Notizzetteln

**Kontrollen:**
- Regelmäßige Inspektionen
- Sensibilisierung der Mitarbeiter

### 10.2 Bildschirm-Sichtschutz

**Anforderungen:**
- Privacy-Filter für Bildschirme mit CHD
- Bildschirme nicht von außen einsehbar
- Automatische Bildschirmsperre (15 Minuten)

## 11. Notfallzugang

### 11.1 Break-Glass-Verfahren

**Prozess:**
- Versiegelter Umschlag mit Notfall-Zugangsdaten
- Lagerung in Tresor
- Zugriff nur mit Zeugen
- Dokumentation jeder Verwendung
- Sofortige Passwortänderung nach Verwendung

**Dokumentation:**
- Datum und Uhrzeit
- Grund für Notfallzugang
- Durchgeführt von
- Zeuge
- Durchgeführte Aktionen

### 11.2 Notfall-Evakuierung

**Prozess:**
- Evakuierungsplan
- Sammelplätze
- Verantwortliche Personen
- Regelmäßige Übungen

**Sicherheitsmaßnahmen:**
- Automatische Sperrung aller Systeme
- Aktivierung Alarmsystem
- Benachrichtigung Security

## 12. Compliance-Validierung

### 12.1 Validierungsaktivitäten

**Quartalsweise:**
- POS-Terminal-Inspektion
- Medien-Inventar
- Besucherprotokoll-Review
- Videoüberwachungs-Test

**Jährlich:**
- Physische Sicherheits-Audit
- Penetrationstest (physisch)
- Mitarbeiter-Sensibilisierung

### 12.2 Validierungsdokumentation

**Erforderliche Nachweise:**
- Zutrittskontroll-Protokolle
- Besucherprotokolle
- POS-Inspektionsprotokolle
- Medien-Vernichtungszertifikate
- Videoaufzeichnungen (90 Tage)

<!-- End of template -->
