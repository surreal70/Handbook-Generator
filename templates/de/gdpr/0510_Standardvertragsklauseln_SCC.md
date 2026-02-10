# Standardvertragsklauseln (SCC)

**Dokument-ID:** 0510  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** Entwurf  
**Klassifizierung:** Intern  
**Letzte Aktualisierung:** {{ meta.date }}  

---

<!-- 
Dieses Template dokumentiert die Verwendung von Standardvertragsklauseln für Drittlandübermittlungen.
Es beschreibt die verschiedenen Module und deren Anwendung.

Anpassung erforderlich:
- Wähle das passende SCC-Modul
- Fülle die Anhänge aus (Datenübermittlung, TOM, Sub-Prozessoren)
- Führe Transfer Impact Assessment durch
- Implementiere zusätzliche Maßnahmen
- Dokumentiere Vertragsabschlüsse

Referenz: DSGVO Art. 46 Abs. 2 lit. c, Durchführungsbeschluss (EU) 2021/914
-->

## Zweck

Dieses Dokument beschreibt die Verwendung von Standardvertragsklauseln (Standard Contractual Clauses, SCC) bei {{ meta.organization }} für die Übermittlung personenbezogener Daten in Drittländer gemäß Art. 46 Abs. 2 lit. c DSGVO.

## Neue Standardvertragsklauseln (2021)

### Durchführungsbeschluss (EU) 2021/914

**Verabschiedung:** 4. Juni 2021  
**Anwendbar ab:** 27. Juni 2021  
**Übergangszeit für alte SCCs:** Bis 27. Dezember 2022

**Vorteile der neuen SCCs:**
- Modularer Aufbau für verschiedene Übermittlungsszenarien
- Berücksichtigung des Schrems-II-Urteils
- Flexibilität bei komplexen Verarbeitungsketten
- Docking-Klausel für weitere Parteien

## SCC-Module

### Modul 1: Controller zu Controller

**Anwendungsfall:** Verantwortlicher in der EU übermittelt Daten an Verantwortlichen im Drittland

**Beispiele:**
- Übermittlung von Kundendaten an ausländischen Geschäftspartner
- Datenaustausch zwischen Konzerngesellschaften (beide als Verantwortliche)
- Übermittlung an ausländische Behörden (soweit zulässig)

**Verwendung bei {{ meta.organization }}:**

| Übermittlung | Empfänger | Land | Datum Abschluss | Dokumentation |
|--------------|-----------|------|-----------------|---------------|
| [TODO: Beschreibung] | [TODO: Name] | [TODO: Land] | [TODO: Datum] | [TODO: Link] |

### Modul 2: Controller zu Processor

**Anwendungsfall:** Verantwortlicher in der EU beauftragt Auftragsverarbeiter im Drittland

**Beispiele:**
- Cloud-Hosting außerhalb EU/EWR
- Outsourcing von IT-Services
- Call-Center in Drittländern
- Lohnabrechnung durch ausländischen Dienstleister

**Verwendung bei {{ meta.organization }}:**

| Auftragsverarbeiter | Dienstleistung | Land | Datum Abschluss | Dokumentation |
|---------------------|----------------|------|-----------------|---------------|
| [TODO: Name] | [TODO: Service] | [TODO: Land] | [TODO: Datum] | [TODO: Link] |

### Modul 3: Processor zu Processor

**Anwendungsfall:** Auftragsverarbeiter beauftragt Sub-Auftragsverarbeiter im Drittland

**Beispiele:**
- Cloud-Provider nutzt Sub-Hosting-Provider
- IT-Dienstleister lagert Teile an Sub-Dienstleister aus

**Verwendung bei {{ meta.organization }}:**

| Hauptauftragsverarbeiter | Sub-Auftragsverarbeiter | Land | Datum Abschluss | Dokumentation |
|-------------------------|------------------------|------|-----------------|---------------|
| [TODO: Name] | [TODO: Name] | [TODO: Land] | [TODO: Datum] | [TODO: Link] |

### Modul 4: Processor zu Controller

**Anwendungsfall:** Auftragsverarbeiter übermittelt Daten an Verantwortlichen im Drittland

**Beispiele:**
- Auftragsverarbeiter übermittelt Daten an Konzernmutter im Drittland
- Rückübermittlung von Daten nach Vertragsende

**Verwendung bei {{ meta.organization }}:**

| Auftragsverarbeiter | Empfänger | Land | Datum Abschluss | Dokumentation |
|---------------------|-----------|------|-----------------|---------------|
| [TODO: Name] | [TODO: Name] | [TODO: Land] | [TODO: Datum] | [TODO: Link] |

## Pflichtanhänge der SCCs

### Anhang I: Parteien und Datenübermittlung

#### Teil A: Liste der Parteien

**Datenexporteur (EU):**
- Name: [TODO: {{ meta.organization }}]
- Adresse: [TODO: Adresse]
- Kontakt: [TODO: Name, E-Mail, Telefon]
- Rolle: Verantwortlicher / Auftragsverarbeiter
- Unterschrift: ___________________

**Datenimporteur (Drittland):**
- Name: [TODO: Name des Empfängers]
- Adresse: [TODO: Adresse]
- Kontakt: [TODO: Name, E-Mail, Telefon]
- Rolle: Verantwortlicher / Auftragsverarbeiter
- Unterschrift: ___________________

#### Teil B: Beschreibung der Übermittlung

**Kategorien betroffener Personen:**
- [TODO: z.B. Kunden, Mitarbeiter, Lieferanten]

**Kategorien personenbezogener Daten:**
- [TODO: z.B. Stammdaten, Kontaktdaten, Vertragsdaten]
- **Besondere Kategorien (Art. 9):** [TODO: falls zutreffend]

**Sensible Daten (falls zutreffend):**
- [TODO: Beschreibung]

**Häufigkeit der Übermittlung:**
- [TODO: z.B. kontinuierlich, monatlich, bei Bedarf]

**Art der Übermittlung:**
- [TODO: z.B. E-Mail, API, Cloud-Speicher]

**Zweck(e) der Datenübermittlung:**
- [TODO: z.B. Vertragserfüllung, IT-Services]

**Speicherdauer beim Importeur:**
- [TODO: z.B. Vertragslaufzeit + 3 Jahre]

**Für Übermittlungen an Sub-Prozessoren:**
- [TODO: Beschreibung der Verarbeitung durch Sub-Prozessoren]

#### Teil C: Zuständige Aufsichtsbehörde

**Aufsichtsbehörde des Exporteurs:**
- Name: [TODO: z.B. Landesbeauftragter für Datenschutz]
- Adresse: [TODO: Adresse]
- E-Mail: [TODO: E-Mail]
- Website: [TODO: URL]

### Anhang II: Technische und organisatorische Maßnahmen (TOM)

**Beschreibung der technischen und organisatorischen Maßnahmen des Datenimporteurs:**

#### 1. Zugangskontrollen

**Physische Zugangskontrollen:**
- [TODO: z.B. Zutrittskontrollsystem, Besuchermanagement]

**Logische Zugangskontrollen:**
- [TODO: z.B. Benutzerauthentifizierung, Multi-Faktor-Authentifizierung]

#### 2. Zugriffskontrollen

**Berechtigungskonzept:**
- [TODO: z.B. Rollenbasierte Zugriffskontrolle (RBAC)]

**Least Privilege Prinzip:**
- [TODO: Beschreibung]

#### 3. Verschlüsselung

**Verschlüsselung im Transit:**
- [TODO: z.B. TLS 1.3]

**Verschlüsselung at Rest:**
- [TODO: z.B. AES-256]

**Schlüsselverwaltung:**
- [TODO: Beschreibung]

#### 4. Pseudonymisierung

**Verfahren:**
- [TODO: Beschreibung, falls anwendbar]

#### 5. Logging und Monitoring

**Protokollierung:**
- [TODO: z.B. Zugriffsprotokolle, Änderungsprotokolle]

**Aufbewahrungsdauer Logs:**
- [TODO: z.B. 90 Tage]

**Monitoring:**
- [TODO: z.B. SIEM, Intrusion Detection]

#### 6. Incident Response

**Incident-Response-Plan:**
- [TODO: Verweis auf Dokument]

**Meldepflicht:**
- [TODO: Unverzügliche Meldung an Exporteur]

#### 7. Backup und Recovery

**Backup-Strategie:**
- [TODO: z.B. tägliche Backups, 30 Tage Aufbewahrung]

**Recovery Time Objective (RTO):**
- [TODO: z.B. 24 Stunden]

**Recovery Point Objective (RPO):**
- [TODO: z.B. 1 Stunde]

#### 8. Datenlöschung

**Löschverfahren:**
- [TODO: z.B. sichere Löschung nach NIST 800-88]

**Löschnachweis:**
- [TODO: Beschreibung]

#### 9. Schulung und Sensibilisierung

**Schulungsprogramm:**
- [TODO: z.B. jährliche Datenschutzschulungen]

**Vertraulichkeitsverpflichtung:**
- [TODO: Alle Mitarbeiter verpflichtet]

#### 10. Audits und Zertifizierungen

**Interne Audits:**
- [TODO: z.B. jährlich]

**Externe Audits:**
- [TODO: z.B. ISO 27001, SOC 2]

**Zertifizierungen:**
- [TODO: Liste der Zertifizierungen]

### Anhang III: Liste der Sub-Prozessoren (nur Modul 2 und 3)

**Genehmigungsverfahren:** [ ] Allgemeine Genehmigung [ ] Spezifische Genehmigung

**Liste der genehmigten Sub-Prozessoren:**

| Name | Adresse | Land | Verarbeitungstätigkeit | Garantien |
|------|---------|------|----------------------|-----------|
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO: z.B. SCCs] |

**Informationspflicht bei Änderungen:**
- Frist für Widerspruch: [TODO: z.B. 30 Tage]
- Benachrichtigungsmethode: [TODO: z.B. E-Mail]

## Optionale Klauseln

### Docking-Klausel (Klausel 7)

**Aktiviert:** [TODO: Ja/Nein]

**Zweck:** Ermöglicht weiteren Parteien, den SCCs beizutreten

**Beigetretene Parteien:**

| Name | Rolle | Beitrittsdatum | Dokumentation |
|------|-------|----------------|---------------|
| [TODO] | [TODO] | [TODO] | [TODO] |

### Lokale Gesetze und Praktiken (Klausel 14)

**Verpflichtung des Importeurs:**
- Benachrichtigung bei Anfragen von Behörden
- Widerspruch gegen unverhältnismäßige Anfragen
- Jährliche Überprüfung der Rechtslage

**Dokumentation von Behördenanfragen:**

| Datum | Behörde | Art der Anfrage | Maßnahmen | Benachrichtigung Exporteur |
|-------|---------|----------------|-----------|---------------------------|
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO: Datum] |

## Transfer Impact Assessment (TIA)

### Erforderlichkeit

Gemäß Schrems-II-Urteil muss zusätzlich zu den SCCs ein TIA durchgeführt werden.

**TIA durchgeführt:** [TODO: Ja/Nein]  
**Datum:** [TODO: Datum]  
**Ergebnis:** [TODO: Angemessenes Schutzniveau gewährleistet Ja/Nein]

### Zusätzliche Maßnahmen

**Technische Maßnahmen:**
- [TODO: z.B. End-to-End-Verschlüsselung]
- [TODO: z.B. Pseudonymisierung]

**Organisatorische Maßnahmen:**
- [TODO: z.B. Vertragliche Verpflichtungen]
- [TODO: z.B. Transparenzberichte]

**Rechtliche Maßnahmen:**
- [TODO: z.B. Widerspruch gegen Behördenanfragen]

**Dokumentation:** [TODO: Verweis auf TIA-Bericht]

## Vertragsmanagement

### Abschlussprozess

1. **Auswahl des Moduls:** Passende SCC-Vorlage wählen
2. **Ausfüllen der Anhänge:** Alle Pflichtanhänge vollständig ausfüllen
3. **TIA durchführen:** Transfer Impact Assessment
4. **Zusätzliche Maßnahmen:** Falls erforderlich implementieren
5. **Datenschutzbeauftragten konsultieren:** Stellungnahme einholen
6. **Vertragsunterzeichnung:** Beide Parteien unterzeichnen
7. **Dokumentation:** Vertrag ablegen und registrieren

### Überwachung

**Überprüfungsfrequenz:** [TODO: z.B. jährlich]

**Zu prüfen:**
- Einhaltung der SCCs durch Importeur
- Aktualität der TOM
- Änderungen der Rechtslage im Drittland
- Sub-Prozessoren-Liste aktuell
- Behördenanfragen dokumentiert

**Audit-Rechte:**
- Recht auf Audits vor Ort
- Recht auf Dokumentenprüfung
- Recht auf Zertifikatsprüfung

### Vertragsende

**Bei Vertragsende:**
- Rückgabe oder Löschung der Daten
- Löschnachweis einholen
- Dokumentation abschließen

## Verantwortlichkeiten

| Aufgabe | Verantwortlich | Rechenschaftspflichtig | Konsultiert | Informiert |
|---------|----------------|----------------------|-------------|------------|
| Modulauswahl | [TODO] | [TODO] | [TODO] | [TODO] |
| Anhänge ausfüllen | [TODO] | [TODO] | [TODO] | [TODO] |
| TIA durchführen | [TODO] | [TODO] | [TODO] | [TODO] |
| Vertragsabschluss | [TODO] | [TODO] | [TODO] | [TODO] |
| Überwachung | [TODO] | [TODO] | [TODO] | [TODO] |

## Verknüpfung zu anderen Dokumenten

- **Datenübermittlung Drittländer (Art. 44-50):** Übergeordnetes Dokument
- **Auftragsverarbeitung (Art. 28):** Bei Modul 2 und 3
- **TOM-Dokumentation (Art. 32):** Detaillierte Sicherheitsmaßnahmen
- **Transfer Impact Assessment:** Risikobewertung

---

**Nächste Schritte:**
1. Identifizieren Sie alle Drittlandübermittlungen, die SCCs erfordern
2. Wählen Sie das passende SCC-Modul
3. Füllen Sie alle Anhänge vollständig aus
4. Führen Sie ein Transfer Impact Assessment durch
5. Schließen Sie die SCCs mit allen Datenimporteuren ab
