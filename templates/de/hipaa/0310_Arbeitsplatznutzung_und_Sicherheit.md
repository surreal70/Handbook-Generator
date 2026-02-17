# Arbeitsplatznutzung und -sicherheit

**Dokument-ID:** HIPAA-0310
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
HINWEIS FÜR TEMPLATE-AUTOREN:
Dieses Template dokumentiert Arbeitsplatznutzung und Arbeitsplatzsicherheit (Physical Safeguards).
Es entspricht der HIPAA Security Rule §164.310(b) und §164.310(c).

Erforderliche (R) Standards:
- Workstation Use (R)
- Workstation Security (R)
-->

## 1. Zweck

Dieses Dokument beschreibt die Richtlinien zur Arbeitsplatznutzung und Arbeitsplatzsicherheit für {{ meta-organisation.name }}, um ordnungsgemäße auszuführende Funktionen, die Art und Weise ihrer Ausführung und physische Attribute der Umgebung von Arbeitsplätzen festzulegen, die auf ePHI zugreifen.

### 1.1 HIPAA-Anforderungen

**Standard:** §164.310(b) - Workstation Use (Erforderlich)  
**Standard:** §164.310(c) - Workstation Security (Erforderlich)

## 2. Arbeitsplatznutzung

### 2.1 Arbeitsplatzdefinition

**Arbeitsplatz:** Ein elektronisches Computergerät (z.B. Laptop, Desktop-Computer, Tablet, Smartphone) und seine elektronischen Medien, die zum Zugriff auf, Erstellen, Empfangen, Verwalten oder Übertragen von ePHI verwendet werden.

**Arbeitsplatztypen:**
- Desktop-Computer
- Laptop-Computer
- Tablets
- Smartphones
- Thin Clients
- Workstations on Wheels (WOWs)
- Kioske

### 2.2 Autorisierte Nutzung

**Zulässige Verwendungen:**
- Zugriff auf ePHI für Behandlung, Zahlung oder Gesundheitsoperationen
- Erstellen und Pflegen von Patientenakten
- Kommunikation mit Patienten und Gesundheitsteam
- Abrechnungs- und Verwaltungsfunktionen
- Autorisierte Forschungsaktivitäten

**Verbotene Verwendungen:**
- Persönliche Nutzung (außer minimaler gelegentlicher Nutzung)
- Zugriff auf ePHI ohne Autorisierung
- Weitergabe von Anmeldedaten
- Installation nicht autorisierter Software
- Anschluss nicht autorisierter Geräte
- Zugriff auf unangemessene Websites
- Herunterladen nicht autorisierter Dateien

### 2.3 Benutzerverantwortlichkeiten

**Mitarbeiter müssen:**
- Arbeitsplätze nur für autorisierte Zwecke verwenden
- Anmeldedaten schützen
- Arbeitsplatz sperren beim Verlassen (auch kurz)
- Abmelden nach Beendigung
- Verlorene, gestohlene oder kompromittierte Arbeitsplätze sofort melden
- Arbeitsplatzsoftware aktuell halten
- Arbeitsplätze nicht ohne ordnungsgemäße Abmeldung/Anmeldung teilen
- Bildschirme positionieren, um unbefugte Einsicht zu verhindern
- Sichtschutzfilter in öffentlichen Bereichen verwenden

## 3. Arbeitsplatzsicherheit

### 3.1 Physische Sicherheit

**Arbeitsplatzpositionierung:**
- Positionierung zur Minimierung unbefugter Einsicht
- Vermeidung der Platzierung in der Nähe von Fenstern oder öffentlichen Bereichen
- Sicherstellung angemessener physischer Sicherheit des Standorts
- Berücksichtigung von Verkehrsmustern und Sichtbarkeit

**Physische Sicherheitskontrollen:**
- Kabelschlösser für Laptops
- Verschlossene Büros oder gesicherte Bereiche
- Sichtschutzfilter
- Automatische Bildschirmsperren
- Physische Barrieren (Wände, Trennwände)

**Mobile Arbeitsplätze:**
- Laptoptaschen, die Inhalt nicht identifizieren
- Niemals unbeaufsichtigt in Fahrzeugen lassen
- Hotelsafes bei Reisen verwenden
- Alle mobilen Geräte verschlüsseln
- Remote-Wipe-Funktion aktivieren

### 3.2 Technische Sicherheit

**Authentifizierung:**
- Eindeutige Benutzer-ID erforderlich
- Starkes Passwort oder biometrische Authentifizierung
- Multi-Faktor-Authentifizierung (für Fernzugriff)
- Keine gemeinsam genutzten Konten

**Automatische Abmeldung/Sperre:**
- Bildschirmsperre nach [TODO: 5-15] Minuten Inaktivität
- Automatische Abmeldung nach [TODO: 30] Minuten Inaktivität
- Erneute Authentifizierung zum Fortsetzen erforderlich

**Verschlüsselung:**
- Vollständige Festplattenverschlüsselung für alle Arbeitsplätze erforderlich
- Verschlüsselungsstandard: [TODO: AES-256 oder gleichwertig]
- Verfahren zur Verschlüsselungsschlüsselverwaltung

**Antivirus/Anti-Malware:**
- Endpoint-Protection-Software erforderlich
- Echtzeit-Scanning aktiviert
- Automatische Updates aktiviert
- Regelmäßige Scans geplant

**Firewall:**
- Host-basierte Firewall aktiviert
- Standard-Ablehnung eingehender Verbindungen
- Nur autorisierte Anwendungen erlaubt

**Software-Updates:**
- Betriebssystem-Patches innerhalb von [TODO: 30] Tagen angewendet
- Kritische Sicherheitspatches innerhalb von [TODO: 7] Tagen angewendet
- Anwendungsupdates gemäß Herstellerempfehlungen angewendet

### 3.3 Konfigurationsstandards

**Basiskonfiguration:**
- Genehmigte Betriebssystemversion
- Nur genehmigte Anwendungen
- Unnötige Dienste deaktiviert
- Standardpasswörter geändert
- Administratorrechte eingeschränkt
- Audit-Protokollierung aktiviert

**Konfigurationsverwaltung:**
- Standard-Images für Arbeitsplatzbereitstellung
- Konfigurationsänderungen dokumentiert und genehmigt
- Regelmäßige Konfigurationsaudits
- Nicht konforme Arbeitsplätze behoben

## 4. Arbeitsplatzinventar

### 4.1 Asset-Inventar

| Asset-ID | Typ | Standort | Benutzer | ePHI-Zugriff | Verschlüsselung | Letztes Update |
|----------|-----|----------|----------|--------------|-----------------|----------------|
| [TODO: WS-001] | Desktop | [TODO: Büro 101] | [TODO: Benutzername] | Ja | Ja | [TODO: Datum] |
| [TODO: WS-002] | Laptop | [TODO: Mobil] | [TODO: Benutzername] | Ja | Ja | [TODO: Datum] |
| [TODO: WS-003] | Tablet | [TODO: Klinik A] | [TODO: Geteilt] | Ja | Ja | [TODO: Datum] |

### 4.2 Asset-Tracking

**Tracking-Anforderungen:**
- Asset-Tag/ID
- Seriennummer
- Hersteller und Modell
- Zugewiesener Benutzer
- Standort
- ePHI-Zugriff (Ja/Nein)
- Verschlüsselungsstatus
- Letztes Sicherheitsupdate
- Garantie-/Support-Ablauf

**Inventaraktualisierungen:**
- Neue Arbeitsplatzbereitstellung
- Arbeitsplatzneuzuweisung
- Arbeitsplatzstilllegung
- Standortänderungen
- Vierteljährliche Inventarüberprüfung

## 5. Arbeitsplatz-Lebenszyklus

### 5.1 Beschaffung

**Beschaffungsanforderungen:**
- Erfüllung minimaler Sicherheitsstandards
- Kompatibilität mit Sicherheitssoftware
- Unterstützung vollständiger Festplattenverschlüsselung
- Von IT-Abteilung genehmigt
- Angemessene Garantie/Support enthalten

**Genehmigungsprozess:**
1. Abteilung reicht Anfrage ein
2. IT prüft technische Anforderungen
3. Security Officer genehmigt Sicherheitsfunktionen
4. Beschaffung bearbeitet Bestellung

### 5.2 Bereitstellung

**Bereitstellungsprozess:**
1. **Imaging:** Standard-Image installieren
2. **Konfiguration:** Sicherheitskonfiguration anwenden
3. **Verschlüsselung:** Vollständige Festplattenverschlüsselung aktivieren
4. **Software:** Erforderliche Anwendungen installieren
5. **Testen:** Funktionalität und Sicherheit überprüfen
6. **Dokumentation:** Zum Asset-Inventar hinzufügen
7. **Zuweisung:** Benutzer zuweisen
8. **Schulung:** Benutzerschulung bereitstellen
9. **Bestätigung:** Benutzer unterzeichnet Nutzungsvereinbarung

### 5.3 Wartung

**Wartungsaktivitäten:**
- Software-Updates und Patches
- Antivirus-Updates
- Hardware-Reparaturen
- Leistungsoptimierung
- Sicherheitsscans

**Wartungsplan:**
| Aktivität | Häufigkeit | Verantwortlich |
|-----------|-----------|----------------|
| OS-Patches | Monatlich | IT |
| Antivirus-Updates | Täglich (automatisch) | Endpoint Protection |
| Sicherheitsscans | Wöchentlich | IT Security |
| Hardware-Inspektion | Jährlich | IT |

### 5.4 Stilllegung/Entsorgung

**Stilllegungsprozess:**
1. **Außerbetriebnahme:** Aus Produktion entfernen
2. **Datenlöschung:** Alle Daten sicher löschen
3. **Überprüfung:** Datenvernichtung überprüfen
4. **Dokumentation:** Entsorgung dokumentieren
5. **Physische Vernichtung:** Speichermedien vernichten (falls erforderlich)
6. **Zertifikat:** Vernichtungszertifikat einholen
7. **Inventaraktualisierung:** Aus Asset-Inventar entfernen

**Datenlöschungsmethoden:**
- Softwarebasiertes Löschen (NIST 800-88-konform)
- Entmagnetisierung (für magnetische Medien)
- Physische Vernichtung (Schreddern, Zerkleinern)

**Löschungsstandards:**
- Mindestens 3-faches Überschreiben
- Überprüfung der Löschung
- Dokumentation der verwendeten Methode
- Vernichtungszertifikat aufbewahrt

## 6. Fernzugriffs-Arbeitsplätze

### 6.1 Fernzugriffsanforderungen

**Fernzugriffsszenarien:**
- Arbeit von zu Hause
- Telemedizin
- Mobile Kliniker
- Geschäftsreisen
- Notfallzugriff

**Sicherheitsanforderungen:**
- VPN für allen Fernzugriff erforderlich
- Multi-Faktor-Authentifizierung erforderlich
- Nur verschlüsselte Verbindungen
- Nur firmeneigene oder genehmigte Geräte
- Einhaltung aller Arbeitsplatzsicherheitsrichtlinien

### 6.2 Heimbüro-Sicherheit

**Heimbüro-Anforderungen:**
- Dedizierter Arbeitsbereich (falls möglich)
- Physische Sicherheit (verschlossener Raum/Bereich)
- Sicheres WLAN (WPA3 oder WPA2)
- Keine gemeinsame Computernutzung
- Privatsphäre vor Familienmitgliedern
- Sichere Dokumentenaufbewahrung

**Heimnetzwerksicherheit:**
- Standard-Router-Passwort ändern
- Router-Firewall aktivieren
- WPS deaktivieren
- Starkes WLAN-Passwort verwenden
- Router-Firmware aktuell halten
- Separates Gästenetzwerk

## 7. Gemeinsam genutzte Arbeitsplätze

### 7.1 Richtlinie für gemeinsam genutzte Arbeitsplätze

**Szenarien für gemeinsam genutzte Arbeitsplätze:**
- Klinische Workstations on Wheels (WOWs)
- Pflegestationscomputer
- Kioske
- Konferenzraumcomputer

**Sicherheitsanforderungen:**
- Individuelle Anmeldung erforderlich (keine gemeinsamen Konten)
- Automatische Abmeldung nach Inaktivität
- Clear-Screen-Richtlinie (Abmeldung zwischen Benutzern)
- Physische Sicherheit des Standorts
- Regelmäßige Reinigung und Wartung

### 7.2 Kiosk-Modus

**Kiosk-Konfiguration:**
- Begrenzte Funktionalität
- Eingeschränkter Anwendungszugriff
- Keine lokale Datenspeicherung
- Automatisches Sitzungs-Timeout
- Automatische Rückkehr zum Anmeldebildschirm
- Manipulationssichere Hardware

## 8. Mobile Device Management (MDM)

### 8.1 MDM-Anforderungen

**MDM-Funktionen:**
- Remote-Wipe
- Verschlüsselungsdurchsetzung
- Passwortrichtliniendurchsetzung
- Anwendungsverwaltung
- Geräte-Compliance-Überwachung
- Standortverfolgung (falls zulässig)

**MDM-Registrierung:**
- Alle mobilen Geräte mit ePHI-Zugriff müssen registriert werden
- Registrierung vor Gewährung des ePHI-Zugriffs
- Benutzerbestätigung der MDM-Funktionen

### 8.2 BYOD (Bring Your Own Device)

**BYOD-Richtlinie:** [TODO: Erlaubt/Nicht erlaubt]

Falls BYOD erlaubt:
- MDM-Registrierung erforderlich
- Containerisierung von Arbeitsdaten
- Trennung von Arbeits-/Privatdaten
- Remote-Wipe nur von Arbeitsdaten
- Benutzervereinbarung mit Bestätigung von MDM
- Einhaltung aller Sicherheitsrichtlinien

## 9. Vorfallreaktion

### 9.1 Arbeitsplatzvorfälle

**Vorfalltypen:**
- Verlorener oder gestohlener Arbeitsplatz
- Malware-Infektion
- Unbefugter Zugriff
- Physischer Schaden
- Datenschutzverletzung
- Richtlinienverstoß

### 9.2 Meldeverfahren

**Sofortige Meldung erforderlich:**
1. **Melden:** Sofort an IT-Helpdesk und Security Officer melden
2. **Deaktivieren:** IT deaktiviert Fernzugriff und Netzwerkzugriff
3. **Bewerten:** Security Officer bewertet Vorfall
4. **Eindämmen:** Vorfall eindämmen (Remote-Wipe falls erforderlich)
5. **Untersuchen:** Umfang und Auswirkung untersuchen
6. **Beheben:** Korrekturmaßnahmen umsetzen
7. **Dokumentieren:** Vorfall und Reaktion dokumentieren
8. **Nachbereitung:** Nachträgliche Überprüfung durchführen

**Kontaktinformationen:**
- IT-Helpdesk: [TODO: Telefon/E-Mail]
- Security Officer: [TODO]
- Nach Geschäftsschluss: [TODO: Notfallkontakt]

## 10. Schulung und Sensibilisierung

### 10.1 Schulungsanforderungen

**Erstschulung:**
- Arbeitsplatznutzungsrichtlinie
- Arbeitsplatzsicherheitsanforderungen
- Physische Sicherheitsmaßnahmen
- Vorfallmeldung
- Richtlinie zur akzeptablen Nutzung

**Jährliche Schulung:**
- Richtlinienauffrischung
- Neue Bedrohungen
- Best Practices
- Fallstudien

**Just-in-Time-Schulung:**
- Neue Arbeitsplatzbereitstellung
- Richtlinienänderungen
- Nach Sicherheitsvorfällen

### 10.2 Sensibilisierungsaktivitäten

- Sicherheitserinnerungen (E-Mail, Poster)
- Bildschirmsperr-Erinnerungen
- Clean-Desk-Richtlinienerinnerungen
- Phishing-Sensibilisierung
- Social-Engineering-Sensibilisierung

## 11. Überwachung und Compliance

### 11.1 Compliance-Überwachung

**Überwachungsaktivitäten:**
- Arbeitsplatzkonfigurationsaudits
- Verschlüsselungs-Compliance-Prüfungen
- Software-Update-Compliance
- Antivirus-Statusprüfungen
- Physische Sicherheitsinspektionen
- Richtlinien-Compliance-Audits

**Überwachungshäufigkeit:**
| Aktivität | Häufigkeit | Verantwortlich |
|-----------|-----------|----------------|
| Konfigurationsaudit | Vierteljährlich | IT Security |
| Verschlüsselungsprüfung | Monatlich | IT Security |
| Update-Compliance | Wöchentlich | IT |
| Physische Inspektion | Halbjährlich | Facilities + IT |

### 11.2 Nicht-Compliance

**Nicht-Compliance-Maßnahmen:**
1. **Identifikation:** Nicht-konformer Arbeitsplatz identifiziert
2. **Benachrichtigung:** Benutzer benachrichtigt
3. **Behebung:** Benutzer erhält Zeitrahmen zur Behebung
4. **Eskalation:** Eskalieren, falls nicht behoben
5. **Einschränkung:** ePHI-Zugriff bei Bedarf einschränken
6. **Sanktionen:** Sanktionen gemäß Richtlinie anwenden

## 12. Dokumentation und Aufzeichnungen

### 12.1 Erforderliche Dokumentation

- Arbeitsplatzinventar
- Konfigurationsstandards
- Bereitstellungsaufzeichnungen
- Wartungsaufzeichnungen
- Entsorgungs-/Löschungszertifikate
- Vorfallberichte
- Schulungsunterlagen
- Compliance-Audit-Ergebnisse

### 12.2 Aufbewahrung

**Aufbewahrungsfrist:** [TODO: 6 Jahre ab Stilllegung/Entsorgung]

**Speicherort:** [TODO: Asset-Management-System, Dokumenten-Repository]

**Dokumentenhistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta-handbook.modifydate }} | {{ meta-handbook.author }} | Ersterstellung |

<!-- Ende des Templates -->

