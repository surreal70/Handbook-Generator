# Covered Entities und Healthcare-Komponenten

**Dokument-ID:** HIPAA-0020
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
Diese Vorlage dokumentiert den Status der Organisation als Covered Entity und definiert Healthcare-Komponenten.
Sie entspricht den HIPAA-Definitionen in 45 CFR §160.103.

Erforderliche Anpassungen:
- Covered Entity-Typ und -Funktionen definieren
- Healthcare-Komponenten für Hybrid Entities dokumentieren
- Alle abgedeckten Funktionen und Aktivitäten auflisten
- Belegschaftsmitglieder in abgedeckten Funktionen identifizieren
-->

## 1. Zweck

Dieses Dokument definiert den Status von {{ meta-organisation.name }} als HIPAA Covered Entity und dokumentiert alle Healthcare-Komponenten und abgedeckten Funktionen.

### 1.1 Zielsetzungen

- **Entity-Klassifizierung:** Organisationsstatus unter HIPAA klar definieren
- **Komponentenidentifizierung:** Alle Healthcare-Komponenten dokumentieren (falls Hybrid Entity)
- **Funktionsdokumentation:** Alle abgedeckten Funktionen und Aktivitäten auflisten
- **Compliance-Grenzen:** Klare Grenzen für HIPAA-Compliance festlegen

## 2. Covered Entity-Bestimmung

### 2.1 Covered Entity-Definition

Unter HIPAA ist eine Covered Entity:
1. **Healthcare Provider** (Gesundheitsdienstleister), der bestimmte Transaktionen elektronisch durchführt
2. **Health Plan** (Krankenversicherung), der medizinische Versorgung bereitstellt oder bezahlt
3. **Healthcare Clearinghouse** (Abrechnungsstelle), das Gesundheitsinformationen verarbeitet

### 2.2 Organisationsklassifizierung

**{{ meta-organisation.name }} ist ein:** [TODO: Eine auswählen]

- [ ] **Healthcare Provider** (45 CFR §160.103)
- [ ] **Health Plan** (45 CFR §160.103)
- [ ] **Healthcare Clearinghouse** (45 CFR §160.103)
- [ ] **Hybrid Entity** (45 CFR §164.105(a))

**Klassifizierungsbegründung:** [TODO: Erklären, warum die Organisation die Covered Entity-Definition erfüllt]

## 3. Healthcare Provider-Details

**Diesen Abschnitt ausfüllen, falls die Organisation ein Healthcare Provider ist**

### 3.1 Provider-Informationen

**Provider-Typ:** [TODO: Zutreffendes auswählen]
- [ ] Krankenhaus
- [ ] Arztpraxis
- [ ] Klinik
- [ ] Pflegeheim
- [ ] Apotheke
- [ ] Labor
- [ ] Rettungsdienst
- [ ] Sonstiges: [TODO: Angeben]

**National Provider Identifier (NPI):**
- **NPI-Nummer:** [TODO: 10-stellige NPI]
- **NPI-Typ:** [TODO: Typ 1 (Individuell) oder Typ 2 (Organisation)]
- **Registrierungsdatum:** [TODO: Datum]

**Medizinische Fachgebiete:**
| Fachgebiet | Taxonomie-Code | Anbieter |
|-----------|----------------|----------|
| [TODO: Allgemeinmedizin] | [TODO: Code] | [TODO: Anzahl] |
| [TODO: Fachgebiet 1] | [TODO: Code] | [TODO: Anzahl] |
| [TODO: Fachgebiet 2] | [TODO: Code] | [TODO: Anzahl] |

### 3.2 Elektronische Transaktionen

**Überträgt die Organisation Gesundheitsinformationen elektronisch im Zusammenhang mit einer HIPAA-Standardtransaktion?** [TODO: Ja/Nein]

**Durchgeführte HIPAA-Standardtransaktionen:**
- [ ] Gesundheitsansprüche oder gleichwertige Begegnungsinformationen (837)
- [ ] Berechtigung für einen Gesundheitsplan (270/271)
- [ ] Überweisungszertifizierung und -autorisierung (278)
- [ ] Gesundheitsanspruchsstatus (276/277)
- [ ] Anmeldung und Abmeldung bei einem Gesundheitsplan (834)
- [ ] Gesundheitszahlung und Überweisungsberatung (835)
- [ ] Gesundheitsplan-Prämienzahlungen (820)
- [ ] Koordination der Leistungen (837)

**Transaktionsvolumen (Jährlich):**
| Transaktionstyp | Volumen | Primärer Handelspartner |
|-----------------|---------|-------------------------|
| [TODO: Ansprüche] | [TODO: Anzahl] | [TODO: Zahler-Name] |
| [TODO: Berechtigung] | [TODO: Anzahl] | [TODO: Zahler-Name] |

### 3.3 Bereitgestellte Gesundheitsdienstleistungen

**Angebotene Dienstleistungen:**
| Dienstleistung | Beschreibung | Standort | PHI generiert |
|----------------|--------------|----------|---------------|
| [TODO: Allgemeinmedizin] | [TODO: Beschreibung] | [TODO: Standort] | Ja |
| [TODO: Diagnostische Dienste] | [TODO: Beschreibung] | [TODO: Standort] | Ja |
| [TODO: Behandlungsdienste] | [TODO: Beschreibung] | [TODO: Standort] | Ja |

## 4. Health Plan-Details

**Diesen Abschnitt ausfüllen, falls die Organisation ein Health Plan ist**

### 4.1 Health Plan-Informationen

**Plan-Typ:** [TODO: Zutreffendes auswählen]
- [ ] Gruppenkrankenversicherung
- [ ] Krankenversicherer
- [ ] HMO (Health Maintenance Organization)
- [ ] Medicare
- [ ] Medicaid
- [ ] Medicare Advantage
- [ ] Medicare Part D
- [ ] TRICARE
- [ ] Sonstiges: [TODO: Angeben]

**Plan-Merkmale:**
- **Anzahl der Teilnehmer:** [TODO: Anzahl]
- **Small Health Plan:** [TODO: Ja/Nein - Weniger als 50 Teilnehmer]
- **Selbstversichert:** [TODO: Ja/Nein]
- **Vollversichert:** [TODO: Ja/Nein]

**Plan-Sponsor-Informationen:**
- **Sponsor-Name:** [TODO: Name]
- **Sponsor-Typ:** [TODO: Arbeitgeber, Gewerkschaft, etc.]
- **Beziehung zum Plan:** [TODO: Beschreibung]

### 4.2 Health Plan-Funktionen

**Durchgeführte Funktionen:**
- [ ] Anspruchsbearbeitung
- [ ] Berechtigungsbestimmung
- [ ] Anmeldung und Abmeldung
- [ ] Prämieneinzug
- [ ] Anbieternetzwerkverwaltung
- [ ] Nutzungsüberprüfung
- [ ] Fallmanagement
- [ ] Krankheitsmanagement

**PHI verwendet für:**
- [ ] Zahlung
- [ ] Gesundheitsbetrieb
- [ ] Behandlungskoordination
- [ ] Qualitätsverbesserung
- [ ] Betrugserkennung

## 5. Healthcare Clearinghouse-Details

**Diesen Abschnitt ausfüllen, falls die Organisation ein Healthcare Clearinghouse ist**

### 5.1 Clearinghouse-Informationen

**Bereitgestellte Dienstleistungen:**
- [ ] Anspruchsbearbeitung
- [ ] Anspruchsbereinigung
- [ ] Formatkonvertierung
- [ ] Transaktionsweiterleitung
- [ ] Berechtigungsüberprüfung
- [ ] Sonstiges: [TODO: Angeben]

**Betreute Covered Entities:**
- **Anzahl der Anbieter:** [TODO: Anzahl]
- **Anzahl der Zahler:** [TODO: Anzahl]
- **Transaktionsvolumen (Monatlich):** [TODO: Anzahl]

**Unterstützte Standardformate:**
| Transaktion | Format | Version |
|-------------|--------|---------|
| [TODO: Ansprüche] | X12 837 | [TODO: 5010] |
| [TODO: Berechtigung] | X12 270/271 | [TODO: 5010] |

## 6. Hybrid Entity-Bezeichnung

**Diesen Abschnitt ausfüllen, falls die Organisation eine Hybrid Entity ist**

### 6.1 Hybrid Entity-Definition

Eine Hybrid Entity ist eine Organisation, die:
1. Sowohl abgedeckte als auch nicht abgedeckte Funktionen ausführt
2. Ihre Healthcare-Komponenten formal bezeichnet hat
3. HIPAA nur auf bezeichnete Healthcare-Komponenten anwendet

**Ist {{ meta-organisation.name }} eine Hybrid Entity?** [TODO: Ja/Nein]

### 6.2 Healthcare-Komponenten

**Bezeichnete Healthcare-Komponenten:**

| Komponenten-ID | Komponentenname | Funktion | Standort | Mitarbeiteranzahl |
|----------------|-----------------|----------|----------|-------------------|
| [TODO: HC-001] | [TODO: Medizinische Klinik] | Healthcare Provider | [TODO: Gebäude A] | [TODO: 25] |
| [TODO: HC-002] | [TODO: Mitarbeiter-Gesundheitsplan] | Health Plan | [TODO: HR-Abteilung] | [TODO: 5] |
| [TODO: HC-003] | [TODO: Arbeitsmedizin] | Healthcare Provider | [TODO: Gebäude B] | [TODO: 10] |

**Healthcare-Komponentenfunktionen:**
| Komponente | Abgedeckte Funktionen | Erstellte/Gepflegte PHI |
|-----------|----------------------|-------------------------|
| [TODO: Medizinische Klinik] | Patientenversorgung, Abrechnung | Patientenakten, Abrechnungsdaten |
| [TODO: Mitarbeiter-Gesundheitsplan] | Anspruchsbearbeitung | Ansprüche, Anmeldedaten |

### 6.3 Nicht-Healthcare-Komponenten

**Nicht abgedeckte Komponenten:**

| Komponenten-ID | Komponentenname | Funktion | PHI-Zugriff |
|----------------|-----------------|----------|-------------|
| [TODO: NC-001] | [TODO: Fertigung] | Produktherstellung | Nein |
| [TODO: NC-002] | [TODO: Vertrieb] | Produktverkauf | Nein |
| [TODO: NC-003] | [TODO: Unternehmens-IT] | IT-Support (nicht Healthcare) | Nein |

**Begründung für nicht abgedeckten Status:** [TODO: Erklären, warum diese Komponenten keine abgedeckten Funktionen sind]

### 6.4 Hybrid Entity-Dokumentation

**Formales Bezeichnungsdokument:**
- **Dokumenttitel:** [TODO: "Hybrid Entity-Bezeichnung"]
- **Bezeichnungsdatum:** [TODO: Datum]
- **Genehmigt durch:** [TODO: Vorstand, CEO, etc.]
- **Dokumentstandort:** [TODO: Dateipfad oder Verweis]

**Bezeichnungskriterien:**
- Klare Trennung abgedeckter und nicht abgedeckter Funktionen
- Separate Verwaltung und Betrieb
- Unterschiedliche Belegschaftszuweisungen
- Separate physische Standorte (falls zutreffend)

### 6.5 Belegschaftszuweisung

**Healthcare-Komponenten-Belegschaft:**
| Mitarbeiter-ID | Name | Rolle | Komponente | PHI-Zugriff |
|----------------|------|------|-----------|-------------|
| [TODO: EMP-001] | [TODO: Name] | [TODO: Arzt] | HC-001 | Vollständig |
| [TODO: EMP-002] | [TODO: Name] | [TODO: Pflegekraft] | HC-001 | Vollständig |
| [TODO: EMP-003] | [TODO: Name] | [TODO: Anspruchsbearbeiter] | HC-002 | Eingeschränkt |

**Gemeinsame Belegschaft:**
| Mitarbeiter-ID | Name | Rolle | Zugriff auf Healthcare-Komponenten |
|----------------|------|------|------------------------------------|
| [TODO: EMP-100] | [TODO: Name] | [TODO: IT-Support] | HC-001, HC-002 (nur Systemadministration) |
| [TODO: EMP-101] | [TODO: Name] | [TODO: Recht] | Alle Komponenten (nach Bedarf) |

**Belegschaftsschulung:**
- Healthcare-Komponenten-Belegschaft: Vollständige HIPAA-Schulung
- Gemeinsame Belegschaft: HIPAA-Schulung für Healthcare-Komponentenzugriff
- Nicht-Healthcare-Belegschaft: Keine HIPAA-Schulung erforderlich (außer bei PHI-Zugriff)

## 7. Abgedeckte Funktionen

### 7.1 Healthcare Operations

**Durchgeführte Healthcare Operations:**
- [ ] Qualitätsbewertung und -verbesserung
- [ ] Fallmanagement und Versorgungskoordination
- [ ] Überprüfung der Kompetenz von Gesundheitsfachkräften
- [ ] Underwriting und Prämienbewertung (Gesundheitspläne)
- [ ] Medizinische Überprüfung und Nutzungsüberprüfung
- [ ] Betrugs- und Missbrauchserkennung
- [ ] Geschäftsplanung und -entwicklung
- [ ] Geschäftsführung und allgemeine Verwaltungsaktivitäten

**Für Healthcare Operations verwendete PHI:**
| Operation | Verwendete PHI-Elemente | Häufigkeit | Verantwortliche Abteilung |
|-----------|------------------------|-----------|---------------------------|
| [TODO: Qualitätsverbesserung] | [TODO: Klinische Daten] | [TODO: Vierteljährlich] | [TODO: Qualitätsabteilung] |
| [TODO: Nutzungsüberprüfung] | [TODO: Anspruchsdaten] | [TODO: Laufend] | [TODO: UM-Abteilung] |

### 7.2 Behandlungsaktivitäten

**Behandlungsfunktionen:**
- [ ] Bereitstellung von Gesundheitsdienstleistungen
- [ ] Versorgungskoordination
- [ ] Patientenüberweisung
- [ ] Konsultation zwischen Anbietern
- [ ] Fallmanagement

**Behandlungsstandorte:**
| Standort | Dienstleistungen | Anbieter | Patientenvolumen |
|----------|------------------|----------|------------------|
| [TODO: Hauptklinik] | [TODO: Allgemeinmedizin] | [TODO: 5 Ärzte] | [TODO: 100/Tag] |
| [TODO: Satellitenbüro] | [TODO: Fachversorgung] | [TODO: 2 Spezialisten] | [TODO: 30/Tag] |

### 7.3 Zahlungsaktivitäten

**Zahlungsfunktionen:**
- [ ] Abrechnung und Anspruchsverwaltung
- [ ] Anspruchsbearbeitung
- [ ] Zahlungseinzug
- [ ] Erstattung
- [ ] Nutzungsüberprüfung für Zahlung
- [ ] Vorautorisierung

**Zahlungssysteme:**
| System | Funktion | Verarbeitete PHI | Volumen |
|--------|----------|------------------|---------|
| [TODO: Abrechnungssystem] | Anspruchserstellung | Abrechnungsdaten | [TODO: 500/Tag] |
| [TODO: Zahlungsportal] | Patientenzahlungen | Demografie, Konto | [TODO: 100/Tag] |

## 8. Compliance-Auswirkungen

### 8.1 Anwendbarkeit der HIPAA-Regeln

**Für Covered Entity:**
- **Privacy Rule:** Gilt für alle PHI
- **Security Rule:** Gilt für alle ePHI
- **Breach Notification Rule:** Gilt für alle ungesicherten PHI

**Für Hybrid Entity:**
- **Privacy Rule:** Gilt nur für Healthcare-Komponenten
- **Security Rule:** Gilt nur für Healthcare-Komponenten
- **Breach Notification Rule:** Gilt nur für Healthcare-Komponenten
- **Hinweis:** Gemeinsame Belegschaft und Infrastruktur müssen beim Zugriff auf Healthcare-Komponenten-PHI konform sein

### 8.2 Dokumentationsanforderungen

**Erforderliche Dokumentation:**
- [ ] Covered Entity-Bestimmung
- [ ] Hybrid Entity-Bezeichnung (falls zutreffend)
- [ ] Healthcare-Komponentendefinitionen
- [ ] Belegschaftszuweisungen
- [ ] Business Associate Agreements
- [ ] Richtlinien und Verfahren
- [ ] Schulungsunterlagen

**Dokumentationsaufbewahrung:** [TODO: 6 Jahre ab Erstellung oder letztem Gültigkeitsdatum]

**Dokumentenhistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta-handbook.modifydate }} | {{ meta-handbook.author }} | Ersterstellung |

<!-- Ende der Vorlage -->

