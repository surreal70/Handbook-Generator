# Datenfluss-Diagramme

**Dokument-ID:** PCI-0040  
**Organisation:** AdminSend GmbH  
**Owner:** IT Operations Manager  
**Genehmigt durch:** CIO  
**Version:** 1.0.0  
**Status:** Entwurf / In Review / Freigegeben  
**Klassifizierung:** internal  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  

---



## 1. Zweck

Dieses Dokument visualisiert alle Datenflüsse von Karteninhaberdaten (CHD) innerhalb der AdminSend GmbH.

### 1.1 Ziele

- **Transparenz:** Vollständige Sichtbarkeit aller CHD-Flüsse
- **Scope-Definition:** Identifikation aller PCI-DSS-relevanten Systeme
- **Risikobewertung:** Erkennung potenzieller Schwachstellen
- **Compliance:** Erfüllung von PCI-DSS Requirement 12.5.2

## 2. Datenfluss-Übersicht

### 2.1 Hauptdatenflüsse

[TODO: Fügen Sie High-Level-Datenflussdiagramm ein - siehe diagrams/data_flow_overview.png]

**Datenfluss-Phasen:**
1. **Erfassung:** Karteneingabe am POS/Webformular
2. **Übertragung:** Transport zur Autorisierung
3. **Verarbeitung:** Autorisierung durch Acquiring Bank
4. **Speicherung:** Persistierung für Reporting (falls erforderlich)
5. **Löschung:** Sichere Entsorgung nach Aufbewahrungsfrist

### 2.2 Datenfluss-Kategorien

| Kategorie | Beschreibung | Systeme | Verschlüsselung |
|-----------|--------------|---------|-----------------|
| Point of Sale | Karteneingabe in Filialen | POS-Terminals | P2PE |
| E-Commerce | Online-Zahlungen | Webserver, Payment Gateway | TLS 1.3 |
| Call Center | Telefonische Bestellungen | CRM, IVR | Tokenisierung |
| Recurring Billing | Wiederkehrende Zahlungen | Billing System | Tokenisierung |

## 3. Detaillierte Datenflüsse

### 3.1 Point-of-Sale-Datenfluss

[TODO: Fügen Sie POS-Datenflussdiagramm ein]

**Schritte:**
1. Kunde präsentiert Karte am POS-Terminal
2. Terminal liest Kartendaten (verschlüsselt)
3. Verschlüsselte Daten an Payment Gateway
4. Gateway sendet an Acquiring Bank
5. Autorisierungsantwort zurück an Terminal
6. Quittung für Kunde

**Beteiligte Systeme:**
- POS-Terminal: [TODO: Modell/Hersteller]
- Payment Gateway: [TODO: System-ID]
- Acquiring Bank: [TODO: Bank-Name]

**Datenschutz:**
- P2PE (Point-to-Point Encryption)
- Keine Speicherung von Full Track Data
- Nur letzte 4 Ziffern auf Quittung


### 3.2 E-Commerce-Datenfluss

[TODO: Fügen Sie E-Commerce-Datenflussdiagramm ein]

**Schritte:**
1. Kunde gibt Kartendaten im Webformular ein
2. HTTPS-Übertragung an Webserver
3. Weiterleitung an Payment Gateway
4. Gateway tokenisiert PAN
5. Token zurück an Webserver für Speicherung
6. Autorisierung mit Token

**Beteiligte Systeme:**
- Webserver: [TODO: System-ID]
- Payment Gateway: [TODO: System-ID]
- Datenbank: [TODO: System-ID] (nur Token)

**Datenschutz:**
- TLS 1.3 für Übertragung
- Tokenisierung vor Speicherung
- Keine Speicherung von CVV2

### 3.3 Call-Center-Datenfluss

[TODO: Fügen Sie Call-Center-Datenflussdiagramm ein]

**Schritte:**
1. Kunde nennt Kartendaten am Telefon
2. Agent gibt Daten in CRM ein (maskiert)
3. IVR-System erfasst sensible Daten
4. Direkte Übertragung an Payment Gateway
5. Token zurück an CRM

**Beteiligte Systeme:**
- CRM-System: [TODO: System-ID]
- IVR-System: [TODO: System-ID]
- Payment Gateway: [TODO: System-ID]

**Datenschutz:**
- IVR für sensible Dateneingabe
- Keine Speicherung von PAN im CRM
- Nur Token gespeichert

## 4. Systemübersicht

### 4.1 Systeme mit CHD-Zugriff

| System-ID | Systemname | CHD-Typ | Funktion | Verschlüsselung |
|-----------|------------|---------|----------|-----------------|
| [TODO: SYS-001] | POS-Terminal | PAN (Transit) | Karteneingabe | P2PE |
| [TODO: SYS-002] | Payment Gateway | PAN | Autorisierung | TLS 1.3 |
| [TODO: SYS-003] | Datenbank | Token | Speicherung | AES-256 |
| [TODO: SYS-004] | Webserver | PAN (Transit) | E-Commerce | TLS 1.3 |

### 4.2 Datenübertragungsprotokolle

| Verbindung | Protokoll | Verschlüsselung | Port |
|------------|-----------|-----------------|------|
| POS → Gateway | HTTPS | TLS 1.3 | 443 |
| Web → Gateway | HTTPS | TLS 1.3 | 443 |
| Gateway → Bank | HTTPS | TLS 1.3 | 443 |
| Gateway → DB | SQL/TLS | TLS 1.2+ | 3306 |

## 5. Datenspeicherung

### 5.1 Gespeicherte Karteninhaberdaten

| Datentyp | Speicherort | Verschlüsselung | Aufbewahrungsfrist | Begründung |
|----------|-------------|-----------------|-------------------|------------|
| PAN (Token) | Datenbank | AES-256 | [TODO: 13 Monate] | Rückerstattungen |
| Karteninhaber-Name | Datenbank | AES-256 | [TODO: 13 Monate] | Rückerstattungen |
| Transaktionsdaten | Datenbank | AES-256 | [TODO: 7 Jahre] | Buchhaltung |

**Nicht gespeichert:**
- Full Track Data
- CVV2/CVC2/CID
- PIN/PIN Block

### 5.2 Datenlöschung

**Löschprozess:**
1. Automatische Identifikation abgelaufener Daten
2. Sichere Löschung (Overwrite/Crypto-Shredding)
3. Logging der Löschvorgänge
4. Quartalsweise Überprüfung

**Verantwortlich:** [TODO: Data Retention Manager]

## 6. Externe Datenflüsse

### 6.1 Acquiring Bank

**Bank:** [TODO: Bank-Name]  
**Verbindung:** HTTPS/TLS 1.3  
**Datentyp:** PAN, Transaktionsdaten  
**Zweck:** Autorisierung und Settlement  

### 6.2 Payment Processor

**Processor:** [TODO: Processor-Name]  
**Verbindung:** HTTPS/TLS 1.3  
**Datentyp:** PAN (verschlüsselt)  
**Zweck:** Zahlungsabwicklung  

### 6.3 Tokenization Service

**Service:** [TODO: Service-Name]  
**Verbindung:** HTTPS/TLS 1.3  
**Datentyp:** PAN → Token  
**Zweck:** Scope-Reduktion  

## 7. Datenfluss-Änderungsmanagement

### 7.1 Änderungsprozess

**Bei Änderungen an Datenflüssen:**
1. Aktualisierung der Diagramme
2. PCI-DSS-Impact-Assessment
3. Genehmigung durch CISO
4. Dokumentation der Änderung
5. Schulung betroffener Mitarbeiter

### 7.2 Änderungshistorie

| Datum | Änderung | Begründung | Genehmigt durch |
|-------|----------|------------|-----------------|
| [TODO: 2026-01-15] | Tokenisierung implementiert | Scope-Reduktion | [TODO: CISO] |

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |


