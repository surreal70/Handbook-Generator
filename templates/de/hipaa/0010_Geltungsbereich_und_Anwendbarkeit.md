# Geltungsbereich und Anwendbarkeit

**Dokument-ID:** HIPAA-0010  
**Organisation:** {{ meta.organization.name }}  
**Verantwortlich:** {{ meta.document.owner }}  
**Genehmigt durch:** {{ meta.document.approver }}  
**Version:** {{ meta.document.version }}  
**Status:** Entwurf / In Prüfung / Genehmigt  
**Klassifizierung:** {{ meta.document.classification }}  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  

---

<!-- 
HINWEIS FÜR TEMPLATE-AUTOREN:
Diese Vorlage definiert den Geltungsbereich der HIPAA-Compliance für die Organisation.
Sie entspricht der HIPAA Security Rule §164.306 und Privacy Rule §164.500.

Erforderliche Anpassungen:
- Definieren, ob die Organisation eine Covered Entity oder ein Business Associate ist
- Alle Systeme identifizieren, die PHI speichern, verarbeiten oder übertragen
- Organisationsstruktur und Healthcare-Komponenten dokumentieren
- Alle Standorte auflisten, an denen PHI vorhanden ist
-->

## 1. Zweck

Dieses Dokument definiert den Geltungsbereich der HIPAA-Compliance für {{ meta.organization.name }} und legt die Anwendbarkeit der Anforderungen der HIPAA Security Rule, Privacy Rule und Breach Notification Rule fest.

### 1.1 Zielsetzungen

- **Geltungsbereichsdefinition:** Klare Identifizierung HIPAA-regulierter Aktivitäten und Systeme
- **Compliance-Rahmen:** Grundlage für das HIPAA-Compliance-Programm schaffen
- **Rollenklärung:** Rolle der Organisation als Covered Entity oder Business Associate definieren
- **PHI-Identifizierung:** Alle geschützten Gesundheitsinformationen im Geltungsbereich dokumentieren

### 1.2 Referenzen

- **HIPAA Security Rule**: 45 CFR §§ 164.302-164.318
- **HIPAA Privacy Rule**: 45 CFR §§ 164.500-164.534
- **Breach Notification Rule**: 45 CFR §§ 164.400-164.414
- **HITECH Act**: Health Information Technology for Economic and Clinical Health Act
- **Omnibus Rule**: Abschließende Änderungen zu HIPAA (2013)

## 2. Organisationsinformationen

### 2.1 Organisationsdetails

**Organisationsname:** {{ meta.organization.name }}  
**Adresse:** {{ meta.organization.address }}, {{ meta.organization.postal_code }} {{ meta.organization.city }}  
**Bundesstaat:** {{ meta.organization.state }}  
**Land:** {{ meta.organization.country }}  
**Website:** {{ meta.organization.website }}  
**Steuer-ID (EIN):** {{ meta.organization.tax_id }}  

### 2.2 Organisationstyp

**Primäre Klassifizierung:** [TODO: Eine auswählen]
- [ ] Covered Entity - Healthcare Provider (Gesundheitsdienstleister)
- [ ] Covered Entity - Health Plan (Krankenversicherung)
- [ ] Covered Entity - Healthcare Clearinghouse (Abrechnungsstelle)
- [ ] Business Associate (Geschäftspartner)
- [ ] Hybrid Entity (sowohl abgedeckte als auch nicht abgedeckte Funktionen)

**Falls Healthcare Provider:**
- **Provider-Typ:** [TODO: Krankenhaus, Klinik, Arztpraxis, etc.]
- **NPI (National Provider Identifier):** [TODO: 10-stellige NPI]
- **Fachgebiete:** [TODO: Medizinische Fachgebiete auflisten]
- **Elektronische Transaktionen:** [TODO: Ja/Nein - Übertragen Sie Gesundheitsinformationen elektronisch?]

**Falls Health Plan:**
- **Plan-Typ:** [TODO: Gruppenkrankenversicherung, Krankenversicherer, HMO, Medicare, Medicaid, etc.]
- **Anzahl der Teilnehmer:** [TODO: Anzahl]
- **Small Health Plan:** [TODO: Ja/Nein - Weniger als 50 Teilnehmer]

**Falls Healthcare Clearinghouse:**
- **Bereitgestellte Dienstleistungen:** [TODO: Anspruchsbearbeitung, Abrechnungsdienste, etc.]
- **Betreute Covered Entities:** [TODO: Anzahl und Typen]

**Falls Business Associate:**
- **Bereitgestellte Dienstleistungen:** [TODO: IT-Dienste, Abrechnung, Recht, Beratung, etc.]
- **Covered Entity-Kunden:** [TODO: Anzahl]
- **Subunternehmer:** [TODO: Ja/Nein]

### 2.3 Hybrid Entity-Bezeichnung

**Ist dies eine Hybrid Entity?** [TODO: Ja/Nein]

Falls ja, Folgendes ausfüllen:

**Healthcare-Komponenten (Abgedeckte Funktionen):**
| Komponente | Funktion | Standort | PHI-Zugriff |
|-----------|----------|----------|-------------|
| [TODO: Abteilung] | [TODO: Funktion] | [TODO: Standort] | [TODO: Ja/Nein] |

**Nicht-Healthcare-Komponenten (Nicht abgedeckte Funktionen):**
| Komponente | Funktion | Standort | PHI-Zugriff |
|-----------|----------|----------|-------------|
| [TODO: Abteilung] | [TODO: Funktion] | [TODO: Standort] | [TODO: Nein] |

**Bezeichnungsdokumentation:** [TODO: Verweis auf formale Hybrid Entity-Bezeichnung]

## 3. Protected Health Information (PHI)

### 3.1 PHI-Definition

Protected Health Information (PHI) umfasst individuell identifizierbare Gesundheitsinformationen, die:
1. Von einem Gesundheitsdienstleister, einer Krankenversicherung, einem Arbeitgeber oder einer Abrechnungsstelle erstellt oder empfangen wurden
2. Sich auf vergangene, gegenwärtige oder zukünftige körperliche oder geistige Gesundheit, Gesundheitsversorgung oder Zahlung für Gesundheitsversorgung beziehen
3. Die Person identifizieren oder zur Identifizierung der Person verwendet werden könnten

### 3.2 PHI-Elemente

**Demografische Identifikatoren (18 HIPAA-Identifikatoren):**
1. Namen
2. Geografische Unterteilungen kleiner als Bundesstaat (Straßenadresse, Stadt, Landkreis, Postleitzahl)
3. Daten (Geburt, Aufnahme, Entlassung, Tod) - außer Jahr
4. Telefonnummern
5. Faxnummern
6. E-Mail-Adressen
7. Sozialversicherungsnummern
8. Krankenakten-Nummern
9. Krankenversicherungs-Begünstigten-Nummern
10. Kontonummern
11. Zertifikats-/Lizenznummern
12. Fahrzeugkennzeichen und Seriennummern
13. Gerätekennzeichen und Seriennummern
14. Web-URLs
15. IP-Adressen
16. Biometrische Identifikatoren (Fingerabdrücke, Stimmabdrücke)
17. Ganzkörper-Fotografien
18. Jede andere eindeutige Identifikationsnummer, Merkmal oder Code

**Gesundheitsinformationen:**
- Krankengeschichte und Diagnosen
- Behandlungs- und Verfahrensinformationen
- Medikamentenaufzeichnungen
- Labor- und Testergebnisse
- Versicherungs- und Abrechnungsinformationen
- Klinische Notizen und Beurteilungen

### 3.3 PHI in der Organisation

**Arten von gepflegten PHI:** [TODO: Alle zutreffenden markieren]
- [ ] Electronic PHI (ePHI) - elektronisch gespeichert
- [ ] Paper PHI - physische Aufzeichnungen
- [ ] Oral PHI - mündliche Kommunikation

**Erfasste PHI-Datenelemente:**
| Datenelement | Format | Speicherort | Aufbewahrungsfrist |
|--------------|--------|-------------|-------------------|
| [TODO: Patientendemografie] | Elektronisch | [TODO: EHR-System] | [TODO: Jahre] |
| [TODO: Krankenakten] | Elektronisch/Papier | [TODO: Standort] | [TODO: Jahre] |
| [TODO: Abrechnungsinformationen] | Elektronisch | [TODO: System] | [TODO: Jahre] |
| [TODO: Laborergebnisse] | Elektronisch | [TODO: System] | [TODO: Jahre] |

## 4. Systeme und Anwendungen

### 4.1 Systeme mit PHI

| System-ID | Systemname | Typ | PHI-Elemente | Standort | Anbieter |
|-----------|------------|-----|--------------|----------|----------|
| [TODO: SYS-001] | [TODO: EHR-System] | Anwendung | Alle PHI | [TODO: On-Premise/Cloud] | [TODO: Anbieter] |
| [TODO: SYS-002] | [TODO: Praxisverwaltung] | Anwendung | Demografie, Abrechnung | [TODO: Standort] | [TODO: Anbieter] |
| [TODO: SYS-003] | [TODO: Laborsystem] | Anwendung | Laborergebnisse | [TODO: Standort] | [TODO: Anbieter] |
| [TODO: SYS-004] | [TODO: Bildgebungssystem] | Anwendung | Radiologiebilder | [TODO: Standort] | [TODO: Anbieter] |
| [TODO: SYS-005] | [TODO: E-Mail-System] | Infrastruktur | PHI in Übertragung | [TODO: Standort] | [TODO: Anbieter] |

### 4.2 Infrastrukturkomponenten

| Komponente | Typ | Funktion | PHI-Zugriff | Standort |
|-----------|------|----------|-------------|----------|
| [TODO: DB-001] | Datenbankserver | PHI-Speicherung | Ja | [TODO: Rechenzentrum] |
| [TODO: APP-001] | Anwendungsserver | PHI-Verarbeitung | Ja | [TODO: Rechenzentrum] |
| [TODO: WEB-001] | Webserver | Patientenportal | Ja | [TODO: Cloud] |
| [TODO: FILE-001] | Dateiserver | Dokumentenspeicherung | Ja | [TODO: On-Premise] |
| [TODO: BACKUP-001] | Backup-System | PHI-Backup | Ja | [TODO: Standort] |

### 4.3 Netzwerkarchitektur

**Netzwerksegmente mit PHI:**
- **Klinisches Netzwerk:** [TODO: Beschreibung]
- **Administratives Netzwerk:** [TODO: Beschreibung]
- **DMZ:** [TODO: Beschreibung]
- **Drahtlose Netzwerke:** [TODO: Beschreibung]

**Netzwerkdiagramm:** [TODO: Verweis auf Netzwerkdiagramm im diagrams/-Ordner]

## 5. Physische Standorte

### 5.1 Einrichtungen mit PHI

| Standort-ID | Einrichtungsname | Adresse | Typ | PHI vorhanden | Mitarbeiteranzahl |
|-------------|------------------|---------|-----|---------------|-------------------|
| [TODO: LOC-001] | Hauptklinik | [TODO: Adresse] | Klinisch | Ja | [TODO: Anzahl] |
| [TODO: LOC-002] | Verwaltungsbüro | [TODO: Adresse] | Administrativ | Ja | [TODO: Anzahl] |
| [TODO: LOC-003] | Rechenzentrum | [TODO: Adresse] | IT-Infrastruktur | Ja | [TODO: Anzahl] |
| [TODO: LOC-004] | Satellitenklinik | [TODO: Adresse] | Klinisch | Ja | [TODO: Anzahl] |

### 5.2 Fernzugriff

**Fernzugriff auf PHI erlaubt:** [TODO: Ja/Nein]

Falls ja:
- **Zugriffsmethode:** [TODO: VPN, Remote Desktop, Webportal]
- **Authentifizierung:** [TODO: Benutzername/Passwort, MFA, Smart Card]
- **Autorisierte Benutzer:** [TODO: Rollen/Anzahl]
- **Geräte:** [TODO: Firmeneigene, BYOD, Beides]
- **Mobile Device Management:** [TODO: Ja/Nein, Lösungsname]

## 6. Belegschaft

### 6.1 Belegschaft mit PHI-Zugriff

| Rolle/Abteilung | Mitarbeiteranzahl | PHI-Zugriffsebene | Zugriffsbegründung |
|-----------------|-------------------|-------------------|-------------------|
| [TODO: Ärzte] | [TODO: Anzahl] | Vollständig | Direkte Patientenversorgung |
| [TODO: Pflegekräfte] | [TODO: Anzahl] | Vollständig | Direkte Patientenversorgung |
| [TODO: Medizinische Assistenten] | [TODO: Anzahl] | Eingeschränkt | Patientenaufnahme |
| [TODO: Abrechnungspersonal] | [TODO: Anzahl] | Nur Abrechnungsdaten | Anspruchsbearbeitung |
| [TODO: IT-Personal] | [TODO: Anzahl] | Systemadministration | Systemwartung |
| [TODO: Empfang] | [TODO: Anzahl] | Nur Demografie | Terminplanung |

### 6.2 Belegschaftsschulung

**HIPAA-Schulung erforderlich:** Ja (Jährlich)  
**Schulungsthemen:**
- HIPAA Privacy Rule
- HIPAA Security Rule
- Breach Notification-Anforderungen
- Organisationsrichtlinien und -verfahren
- Sanktionen bei Verstößen

**Aufbewahrung von Schulungsunterlagen:** [TODO: Jahre]

## 7. Business Associates

### 7.1 Business Associate-Beziehungen

| Business Associate | Bereitgestellte Dienstleistung | PHI-Zugriff | BAA unterzeichnet | BAA-Datum |
|--------------------|-------------------------------|-------------|-------------------|-----------|
| [TODO: IT-Anbieter] | IT-Support | Ja | [TODO: Ja/Nein] | [TODO: Datum] |
| [TODO: Abrechnungsdienst] | Medizinische Abrechnung | Ja | [TODO: Ja/Nein] | [TODO: Datum] |
| [TODO: Cloud-Anbieter] | Daten-Hosting | Ja | [TODO: Ja/Nein] | [TODO: Datum] |
| [TODO: Aktenvernichtungsdienst] | Dokumentenvernichtung | Ja | [TODO: Ja/Nein] | [TODO: Datum] |
| [TODO: Rechtsanwalt] | Rechtsdienstleistungen | Ja | [TODO: Ja/Nein] | [TODO: Datum] |

### 7.2 Subunternehmer-Beziehungen

**Nutzen Business Associates Subunternehmer?** [TODO: Ja/Nein]

Falls ja:
| Subunternehmer | Dienstleistung | Primärer BA | BAA vorhanden |
|----------------|----------------|-------------|---------------|
| [TODO: Name] | [TODO: Dienstleistung] | [TODO: BA-Name] | [TODO: Ja/Nein] |

## 8. Compliance-Geltungsbereich

### 8.1 Anwendbare HIPAA-Regeln

**Security Rule (45 CFR Part 164, Subpart C):** [TODO: Anwendbar/Nicht anwendbar]
- Administrative Safeguards (§164.308)
- Physical Safeguards (§164.310)
- Technical Safeguards (§164.312)
- Organizational Requirements (§164.314)
- Policies and Procedures (§164.316)

**Privacy Rule (45 CFR Part 164, Subpart E):** [TODO: Anwendbar/Nicht anwendbar]
- Uses and Disclosures (§164.502-§164.514)
- Individual Rights (§164.520-§164.528)
- Administrative Requirements (§164.530-§164.534)

**Breach Notification Rule (45 CFR Part 164, Subpart D):** [TODO: Anwendbar/Nicht anwendbar]
- Breach Discovery and Notification (§164.404-§164.410)
- Notification by Business Associates (§164.410)

### 8.2 Ausschlüsse vom Geltungsbereich

**Systeme/Prozesse NICHT im Geltungsbereich:**
| System/Prozess | Grund für Ausschluss |
|----------------|----------------------|
| [TODO: HR-System] | Keine PHI - nur Mitarbeiterdaten |
| [TODO: Marketing-Datenbank] | Nur de-identifizierte Daten |
| [TODO: Öffentliche Website] | Keine PHI erfasst |

## 9. Compliance-Verantwortlichkeiten

### 9.1 Schlüsselrollen

**Privacy Officer:**
- **Name:** {{ meta.roles.privacy_officer.name }}
- **E-Mail:** {{ meta.roles.privacy_officer.email }}
- **Telefon:** {{ meta.roles.privacy_officer.phone }}

**Security Officer:**
- **Name:** {{ meta.roles.security_officer.name }}
- **E-Mail:** {{ meta.roles.security_officer.email }}
- **Telefon:** {{ meta.roles.security_officer.phone }}

**HIPAA Compliance Officer:**
- **Name:** [TODO: Name]
- **E-Mail:** [TODO: E-Mail]
- **Telefon:** [TODO: Telefon]

**Kontaktperson (für Personen, die Rechte ausüben):**
- **Name:** [TODO: Name]
- **E-Mail:** [TODO: E-Mail]
- **Telefon:** [TODO: Telefon]
- **Adresse:** [TODO: Postanschrift]

### 9.2 Governance-Struktur

**HIPAA Compliance Committee:**
- **Vorsitz:** [TODO: Name, Titel]
- **Mitglieder:** [TODO: Mitglieder und Titel auflisten]
- **Sitzungshäufigkeit:** [TODO: Monatlich/Vierteljährlich]
- **Verantwortlichkeiten:** Aufsicht über HIPAA-Compliance-Programm

## 10. Geltungsbereichsänderungen

### 10.1 Change Management-Prozess

**Auslöser für Geltungsbereichsprüfung:**
1. Neue Systeme oder Anwendungen, die PHI verarbeiten
2. Neue Business Associate-Beziehungen
3. Neue physische Standorte
4. Änderungen in bereitgestellten Dienstleistungen
5. Organisatorische Umstrukturierung
6. Regulatorische Änderungen

**Prüfungsprozess:**
1. Änderung identifizieren
2. HIPAA-Anwendbarkeit bewerten
3. Geltungsbereichsdokumentation aktualisieren
4. Erforderliche Schutzmaßnahmen implementieren
5. Richtlinien und Verfahren aktualisieren
6. Betroffene Belegschaft schulen
7. Änderungen dokumentieren

### 10.2 Geltungsbereichsprüfungsplan

**Jährliche Prüfung:** [TODO: Monat]  
**Letztes Prüfungsdatum:** [TODO: Datum]  
**Nächstes Prüfungsdatum:** [TODO: Datum]  
**Geprüft von:** [TODO: Name, Titel]

### 10.3 Änderungshistorie

| Datum | Änderungsbeschreibung | Auswirkung | Genehmigt durch |
|-------|----------------------|------------|-----------------|
| [TODO: Datum] | Initiale Geltungsbereichsdefinition | N/A | [TODO: Name] |
| [TODO: Datum] | Neues EHR-System hinzugefügt | Erweiterter ePHI-Geltungsbereich | [TODO: Name] |

---

**Dokumentenhistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Ersterstellung |

<!-- Ende der Vorlage -->
