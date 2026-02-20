# Geltungsbereich und CDE-Definition

**Dokument-ID:** PCI-0010
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

Dieses Dokument definiert den Geltungsbereich der PCI-DSS-Compliance für AdminSend GmbH und beschreibt das Cardholder Data Environment (CDE).

### 1.1 Ziele

- **Scope-Definition:** Klare Abgrenzung des CDE vom restlichen Netzwerk
- **Compliance-Fokus:** Identifikation aller PCI-DSS-relevanten Systeme und Prozesse
- **Risikominimierung:** Reduktion des Compliance-Scope durch Segmentierung
- **Audit-Vorbereitung:** Dokumentation für QSA-Assessments

### 1.2 Referenzen

- **PCI-DSS v4.0:** Requirements 1, 2, 11, 12
- **PCI-DSS Information Supplement:** Guidance for PCI DSS Scoping and Network Segmentation
- **PA-DSS:** Payment Application Data Security Standard (falls zutreffend)

## 2. Merchant/Service Provider Information

### 2.1 Organisationsinformationen

**Organisation:** AdminSend GmbH  
**Adresse:** Musterstraße 123, [TODO] [TODO]  
**Land:** [TODO]  
**Website:** [TODO]  

### 2.2 PCI-DSS-Klassifizierung

**Merchant Level:** [TODO: Level 1/2/3/4]  
**Service Provider Level:** [TODO: Level 1/2 oder N/A]  
**Merchant ID:** {{ meta-handbook.merchant_id }}  
**Service Provider ID:** {{ meta-handbook.service_provider_id }}  

**Transaktionsvolumen (jährlich):**
- Visa: [TODO: Anzahl Transaktionen]
- Mastercard: [TODO: Anzahl Transaktionen]
- American Express: [TODO: Anzahl Transaktionen]
- Discover: [TODO: Anzahl Transaktionen]
- Gesamt: [TODO: Anzahl Transaktionen]

### 2.3 Acquiring Banks

| Bank Name | Kontakt | Merchant ID | Kartenmarken |
|-----------|---------|-------------|--------------|
| [TODO: Bank 1] | [TODO: Kontakt] | [TODO: ID] | Visa, Mastercard |
| [TODO: Bank 2] | [TODO: Kontakt] | [TODO: ID] | American Express |

## 3. Cardholder Data Environment (CDE)

### 3.1 CDE-Definition

Das Cardholder Data Environment (CDE) umfasst:

1. **Systeme:** Alle Systeme, die Karteninhaberdaten (CHD) speichern, verarbeiten oder übertragen
2. **Netzwerke:** Alle Netzwerksegmente, die mit CDE-Systemen verbunden sind
3. **Personen:** Alle Mitarbeiter und Dienstleister mit Zugriff auf CHD
4. **Prozesse:** Alle Geschäftsprozesse, die CHD involvieren

### 3.2 Karteninhaberdaten (CHD)

**Primäre Kontonummer (PAN):**
- 13-19-stellige Kartennummer
- **Speicherung:** [TODO: Ja/Nein, wo?]
- **Verschlüsselung:** [TODO: Algorithmus, z.B. AES-256]

**Karteninhabername:**
- Name des Karteninhabers
- **Speicherung:** [TODO: Ja/Nein, wo?]

**Service Code:**
- 3-stelliger Code auf Magnetstreifen
- **Speicherung:** [TODO: Ja/Nein, wo?]

**Ablaufdatum:**
- Gültigkeitsdatum der Karte
- **Speicherung:** [TODO: Ja/Nein, wo?]

### 3.3 Sensitive Authentication Data (SAD)

**DARF NICHT nach Autorisierung gespeichert werden:**

- **Full Track Data:** Magnetstreifendaten (Track 1, Track 2)
- **CAV2/CVC2/CVV2/CID:** Kartenprüfnummer (3-4 Stellen)
- **PIN/PIN Block:** PIN-Daten

**Bestätigung:** AdminSend GmbH speichert KEINE Sensitive Authentication Data nach Autorisierung. [TODO: Bestätigen]

## 4. CDE-Systeme und -Komponenten

### 4.1 Systeme im CDE

| System-ID | Systemname | Typ | Funktion | CHD-Typ | Standort |
|-----------|------------|-----|----------|---------|----------|
| [TODO: SYS-001] | [TODO: Payment Gateway] | Server | Zahlungsabwicklung | PAN, Name | [TODO: RZ1] |
| [TODO: SYS-002] | [TODO: POS-Terminal] | Endpoint | Karteneingabe | PAN | [TODO: Filiale 1] |
| [TODO: SYS-003] | [TODO: Datenbank] | Database | CHD-Speicherung | PAN (verschlüsselt) | [TODO: RZ1] |
| [TODO: SYS-004] | [TODO: Webserver] | Server | E-Commerce | PAN (Transit) | [TODO: RZ1] |

### 4.2 Netzwerkkomponenten im CDE

| Komponente | Typ | Funktion | Standort |
|------------|-----|----------|----------|
| [TODO: FW-CDE-01] | Firewall | CDE-Segmentierung | [TODO: RZ1] |
| [TODO: SW-CDE-01] | Switch | CDE-Netzwerk | [TODO: RZ1] |
| [TODO: RTR-CDE-01] | Router | CDE-Routing | [TODO: RZ1] |
| [TODO: IDS-CDE-01] | IDS/IPS | Intrusion Detection | [TODO: RZ1] |

### 4.3 Anwendungen im CDE

| Anwendung | Version | Hersteller | PA-DSS-zertifiziert | Funktion |
|-----------|---------|------------|---------------------|----------|
| [TODO: Payment App] | [TODO: v2.1] | [TODO: Vendor] | [TODO: Ja/Nein] | Zahlungsabwicklung |
| [TODO: POS-Software] | [TODO: v3.0] | [TODO: Vendor] | [TODO: Ja/Nein] | Point of Sale |
| [TODO: E-Commerce] | [TODO: v1.5] | [TODO: Vendor] | [TODO: Ja/Nein] | Online-Shop |

## 5. Standorte und Lokationen

### 5.1 Physische Standorte mit CDE

| Standort-ID | Standortname | Adresse | CDE-Systeme | Mitarbeiter mit CHD-Zugriff |
|-------------|--------------|---------|-------------|----------------------------|
| [TODO: LOC-01] | Hauptsitz | [TODO: Adresse] | [TODO: Liste] | [TODO: Anzahl] |
| [TODO: LOC-02] | Rechenzentrum | [TODO: Adresse] | [TODO: Liste] | [TODO: Anzahl] |
| [TODO: LOC-03] | Filiale 1 | [TODO: Adresse] | [TODO: POS] | [TODO: Anzahl] |

### 5.2 Remote-Zugriff auf CDE

**Remote-Zugriff erlaubt:** [TODO: Ja/Nein]

Falls ja:
- **Zugriffsmethode:** [TODO: VPN, Jump Server, etc.]
- **Multi-Faktor-Authentifizierung:** [TODO: Ja/Nein, Methode]
- **Berechtigte Benutzer:** [TODO: Rollen/Personen]

## 6. Datenflüsse

### 6.1 Karteninhaberdaten-Flüsse

[TODO: Fügen Sie Datenflussdiagramm ein - siehe PCI-0040]

**Hauptdatenflüsse:**

1. **Karteneingabe → Autorisierung:**
   - Quelle: [TODO: POS-Terminal/Webformular]
   - Ziel: [TODO: Payment Gateway]
   - Protokoll: [TODO: TLS 1.2+]
   - Verschlüsselung: [TODO: Ja/Nein]

2. **Autorisierung → Speicherung:**
   - Quelle: [TODO: Payment Gateway]
   - Ziel: [TODO: Datenbank]
   - Verschlüsselung: [TODO: AES-256]
   - Tokenisierung: [TODO: Ja/Nein]

3. **Reporting/Abfrage:**
   - Quelle: [TODO: Datenbank]
   - Ziel: [TODO: Reporting-System]
   - Maskierung: [TODO: Ja, nur letzte 4 Ziffern]

### 6.2 Externe Verbindungen

| Verbindung | Quelle | Ziel | Zweck | Verschlüsselung |
|------------|--------|------|-------|-----------------|
| [TODO: Acquiring Bank] | CDE | Bank | Autorisierung | TLS 1.2+ |
| [TODO: Payment Processor] | CDE | Processor | Abwicklung | TLS 1.2+ |
| [TODO: ASV Scans] | Internet | CDE | Vulnerability Scans | N/A |

## 7. Scope-Ausschlüsse

### 7.1 Systeme außerhalb des CDE

Folgende Systeme sind NICHT Teil des CDE:

| System | Begründung | Segmentierung |
|--------|------------|---------------|
| [TODO: Intranet] | Keine CHD-Verarbeitung | Firewall-Trennung |
| [TODO: E-Mail-Server] | Keine CHD-Speicherung | Separate VLAN |
| [TODO: Entwicklungsumgebung] | Keine Produktionsdaten | Physisch getrennt |

### 7.2 Ausgeschlossene Standorte

[TODO: Listen Sie Standorte auf, die keine CHD verarbeiten]

## 8. Netzwerksegmentierung

### 8.1 Segmentierungsstrategie

**Segmentierungsmethode:** [TODO: VLAN, Firewall, physische Trennung]

**CDE-Segmente:**
- **CDE-Core:** Systeme mit CHD-Speicherung
- **CDE-DMZ:** Systeme mit CHD-Transit (keine Speicherung)
- **Management:** Administrative Systeme für CDE

**Nicht-CDE-Segmente:**
- **Corporate:** Büronetzwerk
- **Guest:** Gast-WLAN
- **Development:** Entwicklungsumgebung

### 8.2 Segmentierungsvalidierung

**Letzte Validierung:** [TODO: Datum]  
**Durchgeführt von:** [TODO: Name/Firma]  
**Methode:** [TODO: Penetrationstest, Netzwerk-Scan]  
**Ergebnis:** [TODO: Erfolgreich/Fehlgeschlagen]  
**Nächste Validierung:** [TODO: Datum]

## 9. Personal mit CDE-Zugriff

### 9.1 Rollen mit CHD-Zugriff

| Rolle | Anzahl Personen | Zugriffslevel | Begründung |
|-------|-----------------|---------------|------------|
| [TODO: Payment Admin] | [TODO: 2] | Voll | Administration |
| [TODO: Kassierer] | [TODO: 10] | Eingeschränkt | POS-Bedienung |
| [TODO: Support] | [TODO: 3] | Nur Abfrage | Kundenservice |

### 9.2 Dienstleister mit CDE-Zugriff

| Dienstleister | Zweck | Zugriffsmethode | PCI-DSS-Status |
|---------------|-------|-----------------|----------------|
| [TODO: Payment Processor] | Zahlungsabwicklung | API | AOC vorhanden |
| [TODO: Hosting Provider] | Server-Hosting | Remote-Admin | AOC vorhanden |
| [TODO: QSA] | Audit | Vor-Ort | N/A |

## 10. Scope-Änderungen

### 10.1 Änderungsmanagement

**Prozess für Scope-Änderungen:**

1. **Identifikation:** Neue Systeme/Prozesse mit CHD
2. **Bewertung:** PCI-DSS-Relevanz prüfen
3. **Dokumentation:** Scope-Dokument aktualisieren
4. **Genehmigung:** CISO-Freigabe erforderlich
5. **Implementation:** PCI-DSS-Kontrollen anwenden

### 10.2 Änderungshistorie

| Datum | Änderung | Begründung | Genehmigt durch |
|-------|----------|------------|-----------------|
| [TODO: 2026-01-15] | Neues POS-System | Filialerweiterung | [TODO: CISO] |
| [TODO: 2026-02-01] | Tokenisierung | Scope-Reduktion | [TODO: CISO] |

## 11. Compliance-Verantwortlichkeiten

### 11.1 Verantwortliche Personen

**PCI-DSS Program Manager:** [TODO: Name] ([TODO: E-Mail])  
**CISO:** [TODO] ([TODO])  
**IT-Leiter:** [TODO: Name] ([TODO: E-Mail])  
**QSA (Qualified Security Assessor):** [TODO: Firma/Name]  
**ASV (Approved Scanning Vendor):** [TODO: Firma]  

### 11.2 RACI-Matrix

| Aktivität | PCI Manager | CISO | IT-Leiter | QSA |
|-----------|-------------|------|-----------|-----|
| Scope-Definition | A | C | R | I |
| Netzwerksegmentierung | C | A | R | I |
| Compliance-Monitoring | R | A | C | I |
| Jährliches Assessment | C | A | I | R |

**Legende:** R = Responsible, A = Accountable, C = Consulted, I = Informed


