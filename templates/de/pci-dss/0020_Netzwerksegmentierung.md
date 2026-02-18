# Netzwerksegmentierung

**Dokument-ID:** PCI-0020
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Genehmigt durch:** {{ meta-handbook.approver }}
**Revision:** [TODO]
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Klassifizierung:** {{ meta-handbook.classification }}
**Letzte Aktualisierung:** {{ meta-handbook.modifydate }}
**Template Version:** [TODO]

---

---

<!-- 
TEMPLATE AUTHOR NOTE:
This template documents network segmentation to isolate the CDE from other networks.
It aligns with PCI-DSS v4.0 Requirement 1 (Install and Maintain Network Security Controls).

Customization required:
- Document network architecture and segmentation
- Define firewall rules and access controls
- Include network diagrams
- Document segmentation validation procedures
-->

## 1. Zweck

Dieses Dokument beschreibt die Netzwerksegmentierung zur Isolation des Cardholder Data Environment (CDE) vom restlichen Unternehmensnetzwerk.

### 1.1 Ziele

- **Scope-Reduktion:** Minimierung der PCI-DSS-relevanten Systeme
- **Risikominimierung:** Begrenzung potenzieller Angriffsflächen
- **Compliance:** Erfüllung von PCI-DSS Requirement 1
- **Sicherheit:** Schutz von Karteninhaberdaten durch Netzwerkisolation

## 2. Netzwerkarchitektur

### 2.1 Netzwerksegmente

**CDE-Segmente:**

| Segment-ID | Segmentname | VLAN-ID | IP-Bereich | Zweck |
|------------|-------------|---------|------------|-------|
| [TODO: CDE-CORE] | CDE Core | [TODO: 100] | [TODO: 10.1.100.0/24] | CHD-Speicherung |
| [TODO: CDE-DMZ] | CDE DMZ | [TODO: 101] | [TODO: 10.1.101.0/24] | CHD-Transit |
| [TODO: CDE-MGMT] | CDE Management | [TODO: 102] | [TODO: 10.1.102.0/24] | CDE-Administration |

**Nicht-CDE-Segmente:**

| Segment-ID | Segmentname | VLAN-ID | IP-Bereich | Zweck |
|------------|-------------|---------|------------|-------|
| [TODO: CORP] | Corporate | [TODO: 10] | [TODO: 10.1.10.0/24] | Büronetzwerk |
| [TODO: GUEST] | Guest | [TODO: 20] | [TODO: 10.1.20.0/24] | Gast-WLAN |
| [TODO: DEV] | Development | [TODO: 30] | [TODO: 10.1.30.0/24] | Entwicklung |

### 2.2 Netzwerkdiagramm

[TODO: Fügen Sie Netzwerkdiagramm ein - siehe diagrams/network_segmentation.png]

```
Internet
    |
[Perimeter Firewall]
    |
    +--- [CDE-DMZ] --- [CDE Firewall] --- [CDE-CORE]
    |                                          |
    |                                     [CDE-MGMT]
    |
    +--- [Corporate Network]
    |
    +--- [Guest Network]
    |
    +--- [Development Network]
```

## 3. Firewall-Konfiguration

### 3.1 Firewall-Übersicht

| Firewall-ID | Typ | Standort | Funktion | Hersteller/Modell |
|-------------|-----|----------|----------|-------------------|
| [TODO: FW-PERIMETER] | Perimeter | [TODO: RZ1] | Internet-Grenze | [TODO: Vendor/Model] |
| [TODO: FW-CDE] | Internal | [TODO: RZ1] | CDE-Segmentierung | [TODO: Vendor/Model] |
| [TODO: FW-MGMT] | Internal | [TODO: RZ1] | Management-Zugriff | [TODO: Vendor/Model] |

### 3.2 Firewall-Regeln (CDE-Segmentierung)

**Grundprinzip:** Default Deny (alle Verbindungen standardmäßig blockiert)

#### 3.2.1 Eingehende Verbindungen zum CDE

| Regel-ID | Quelle | Ziel | Port/Protokoll | Zweck | Genehmigt durch |
|----------|--------|------|----------------|-------|-----------------|
| [TODO: FW-001] | Internet | CDE-DMZ | 443/TCP | HTTPS E-Commerce | [TODO: CISO] |
| [TODO: FW-002] | Corporate | CDE-MGMT | 22/TCP | SSH Admin | [TODO: CISO] |
| [TODO: FW-003] | Acquiring Bank | CDE-CORE | 443/TCP | Payment API | [TODO: CISO] |

#### 3.2.2 Ausgehende Verbindungen vom CDE

| Regel-ID | Quelle | Ziel | Port/Protokoll | Zweck | Genehmigt durch |
|----------|--------|------|----------------|-------|-----------------|
| [TODO: FW-101] | CDE-CORE | Acquiring Bank | 443/TCP | Autorisierung | [TODO: CISO] |
| [TODO: FW-102] | CDE-CORE | Update Server | 443/TCP | Security Updates | [TODO: CISO] |
| [TODO: FW-103] | CDE-MGMT | SIEM | 514/TCP | Log-Forwarding | [TODO: CISO] |

#### 3.2.3 Blockierte Verbindungen

**Explizit blockiert:**
- CDE → Corporate Network (außer Management)
- Corporate → CDE (außer autorisierte Admin-Zugriffe)
- CDE → Internet (außer explizit erlaubte Dienste)
- Guest → CDE (alle Verbindungen)

### 3.3 Firewall-Regelüberprüfung

**Überprüfungsintervall:** Quartalsweise  
**Verantwortlich:** [TODO: Network Security Team]  
**Letzte Überprüfung:** [TODO: Datum]  
**Nächste Überprüfung:** [TODO: Datum]  

**Überprüfungsprozess:**
1. Review aller Firewall-Regeln
2. Identifikation ungenutzter Regeln
3. Validierung der Business-Begründung
4. Dokumentation von Änderungen
5. Genehmigung durch CISO

## 4. Router-Konfiguration

### 4.1 Router-Übersicht

| Router-ID | Standort | Funktion | Hersteller/Modell |
|-----------|----------|----------|-------------------|
| [TODO: RTR-CORE] | [TODO: RZ1] | Core Routing | [TODO: Vendor/Model] |
| [TODO: RTR-CDE] | [TODO: RZ1] | CDE Routing | [TODO: Vendor/Model] |

### 4.2 Access Control Lists (ACLs)

[TODO: Dokumentieren Sie Router-ACLs analog zu Firewall-Regeln]

## 5. Segmentierungsvalidierung

### 5.1 Validierungsmethoden

**Jährliche Validierung erforderlich (PCI-DSS Req 11.4.6):**

1. **Penetrationstests:**
   - Versuch, CDE-Segmentierung zu umgehen
   - Test von Firewall-Regeln
   - Validierung der Netzwerkisolation

2. **Netzwerk-Scans:**
   - Port-Scans von verschiedenen Segmenten
   - Erreichbarkeitstests
   - Routing-Validierung

3. **Konfigurationsüberprüfung:**
   - Review von Firewall-Konfigurationen
   - Überprüfung von Router-ACLs
   - VLAN-Konfigurationsvalidierung

### 5.2 Validierungshistorie

| Datum | Methode | Durchgeführt von | Ergebnis | Maßnahmen |
|-------|---------|------------------|----------|-----------|
| [TODO: 2025-12-01] | Penetrationstest | [TODO: Firma] | Erfolgreich | Keine |
| [TODO: 2025-06-15] | Netzwerk-Scan | [TODO: Team] | 1 Schwachstelle | Regel FW-042 entfernt |

### 5.3 Nächste Validierung

**Geplantes Datum:** [TODO: Datum]  
**Methode:** [TODO: Penetrationstest/Scan]  
**Durchführende Firma:** [TODO: Name]  

## 6. Wireless Networks

### 6.1 Wireless-Segmentierung

**Wireless-Netzwerke:**

| SSID | Segment | Verschlüsselung | CDE-Zugriff | Zweck |
|------|---------|-----------------|-------------|-------|
| [TODO: Corp-WiFi] | Corporate | WPA3-Enterprise | Nein | Mitarbeiter |
| [TODO: Guest-WiFi] | Guest | WPA3-Personal | Nein | Gäste |
| [TODO: CDE-WiFi] | CDE-MGMT | WPA3-Enterprise + MFA | Ja | CDE-Admin |

**Wichtig:** Wireless-Netzwerke mit CDE-Zugriff erfordern:
- WPA3 oder höher
- Multi-Faktor-Authentifizierung
- Separate VLAN-Segmentierung
- Verschlüsselte Übertragung

### 6.2 Wireless Access Points

| AP-ID | Standort | SSID | Segment | Firmware-Version |
|-------|----------|------|---------|------------------|
| [TODO: AP-001] | [TODO: Büro] | Corp-WiFi | Corporate | [TODO: v2.1] |
| [TODO: AP-002] | [TODO: RZ] | CDE-WiFi | CDE-MGMT | [TODO: v2.1] |

## 7. Remote Access

### 7.1 VPN-Konfiguration

**VPN-Zugriff zum CDE:**

| VPN-Typ | Zielgruppe | Authentifizierung | Ziel-Segment | Verschlüsselung |
|---------|------------|-------------------|--------------|-----------------|
| [TODO: SSL-VPN] | Administratoren | MFA (Token) | CDE-MGMT | TLS 1.3 |
| [TODO: IPSec-VPN] | Dienstleister | MFA (Zertifikat) | CDE-MGMT | AES-256 |

**VPN-Anforderungen:**
- Multi-Faktor-Authentifizierung (MFA) erforderlich
- Verschlüsselung: TLS 1.2+ oder IPSec mit AES-256
- Session-Timeout: [TODO: 15 Minuten Inaktivität]
- Logging aller VPN-Verbindungen

### 7.2 Jump Server / Bastion Hosts

**Jump Server für CDE-Zugriff:**

| Server-ID | Standort | Funktion | Zugriffsmethode |
|-----------|----------|----------|-----------------|
| [TODO: JUMP-01] | CDE-MGMT | Admin-Zugriff | SSH/RDP über VPN |

**Jump Server-Anforderungen:**
- Keine direkte Internet-Verbindung
- Zugriff nur über VPN mit MFA
- Vollständiges Logging aller Sessions
- Keine lokale Datenspeicherung

## 8. Monitoring und Alerting

### 8.1 Netzwerk-Monitoring

**Überwachte Metriken:**
- Firewall-Regel-Verletzungen
- Unerwartete Verbindungsversuche zum CDE
- Änderungen an Firewall-Konfigurationen
- Anomalien im Netzwerkverkehr

**Monitoring-Tools:**
- [TODO: SIEM-System]
- [TODO: Network Monitoring Tool]
- [TODO: IDS/IPS]

### 8.2 Alerting-Regeln

| Alert-ID | Bedingung | Schweregrad | Benachrichtigung |
|----------|-----------|-------------|------------------|
| [TODO: ALT-001] | Verbindung von Corporate zu CDE-CORE | Kritisch | SOC + CISO |
| [TODO: ALT-002] | Firewall-Regel-Änderung | Hoch | Network Team |
| [TODO: ALT-003] | Fehlgeschlagene VPN-Anmeldung (3x) | Mittel | Security Team |

## 9. Änderungsmanagement

### 9.1 Änderungsprozess

**Prozess für Netzwerkänderungen:**

1. **Change Request:** Formale Anfrage mit Begründung
2. **Security Review:** Bewertung der PCI-DSS-Auswirkungen
3. **Testing:** Test in Nicht-Produktionsumgebung
4. **Genehmigung:** CISO-Freigabe für CDE-Änderungen
5. **Implementation:** Durchführung mit Rollback-Plan
6. **Dokumentation:** Aktualisierung dieses Dokuments
7. **Validation:** Überprüfung der Segmentierung

### 9.2 Änderungshistorie

| Datum | Änderung | Begründung | Genehmigt durch | Validiert |
|-------|----------|------------|-----------------|-----------|
| [TODO: 2026-01-15] | Neue Firewall-Regel FW-105 | Payment API | [TODO: CISO] | Ja |

<!-- End of template -->
