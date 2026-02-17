# Richtlinie: Segmentierung, Firewalling und Network Access Control

**Dokument-ID:** 0610
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

## 1. Zweck und Geltungsbereich

Diese Richtlinie konkretisiert die `0600_Policy_Netzwerksicherheit.md` und definiert:
- Netzwerk-Segmentierung und Zonen-Modell
- Firewall-Regeln und -Management
- Network Access Control (NAC)

**Geltungsbereich:** Alle Netzwerke bei **{{ meta-organisation.name }}**

## 2. Netzwerk-Segmentierung

### 2.1 Zonen-Modell

**Zone 1: Internet (Untrusted)**
- Öffentliches Internet
- Keine Vertrauensstellung

**Zone 2: DMZ (Demilitarized Zone)**
- Internet-facing Services (Web-Server, E-Mail-Gateway)
- Eingeschränkter Zugriff auf interne Ressourcen

**Zone 3: Corporate Network**
- Interne Büro-Netzwerke
- Workstations, Drucker
- Standard-Sicherheitskontrollen

**Zone 4: Server Network**
- Interne Server (File-Server, Application-Server)
- Erhöhte Sicherheitskontrollen

**Zone 5: Management Network**
- Management-Interfaces (IPMI, iLO, iDRAC)
- Out-of-Band-Management
- Höchste Sicherheitskontrollen

**Zone 6: Production Network**
- Kritische Produktionssysteme
- Datenbanken, ERP
- Höchste Sicherheitskontrollen

### 2.2 VLAN-Segmentierung

**VLAN-Schema:**
- VLAN 10: Management
- VLAN 20: Server
- VLAN 30: Workstations
- VLAN 40: Guest/BYOD
- VLAN 50: IoT/OT
- VLAN 60: DMZ

**Inter-VLAN-Routing:**
- Über Firewall (nicht Layer-3-Switch)
- Explizite Firewall-Regeln erforderlich

### 2.3 Micro-Segmentation

**Für kritische Systeme:**
- Segmentierung auf Workload-Ebene
- Software-Defined Networking (SDN)
- Zero Trust Network Access (ZTNA)

## 3. Firewall-Management

### 3.1 Firewall-Architektur

**Perimeter-Firewall:**
- Internet ↔ DMZ
- Internet ↔ Corporate Network
- Hochverfügbarkeit (Active/Active oder Active/Passive)

**Internal Firewalls:**
- Zwischen Zonen
- Micro-Segmentation

**Firewall-Plattform:** {{ meta.network.firewall }}

### 3.2 Firewall-Regeln

**Default Deny:**
- Alle Verbindungen standardmäßig blockiert
- Nur explizit erlaubte Verbindungen

**Regel-Struktur:**
- Quelle (IP/Netzwerk)
- Ziel (IP/Netzwerk)
- Service (Port/Protokoll)
- Aktion (Allow/Deny)
- Logging (Enabled)
- Begründung (Business Justification)

**Regel-Reihenfolge:**
1. Deny-Regeln (spezifisch)
2. Allow-Regeln (spezifisch zu allgemein)
3. Default Deny (implizit)

### 3.3 Firewall-Change-Prozess

**Antrag:**
- Change Request über Ticketsystem
- Begründung (Business Justification)
- Quell- und Ziel-IP/Port
- Zeitliche Befristung (wo möglich)

**Genehmigung:**
- IT-Security: Verpflichtend
- Network-Team: Technische Umsetzbarkeit
- Application-Owner: Business Justification

**Implementation:**
- Testing in Dev/Test (wo möglich)
- Implementation in Wartungsfenster
- Verification
- Dokumentation

**Details:** Siehe `0370_Richtlinie_Change_Management`

### 3.4 Firewall-Review

**Regelmäßige Reviews:**
- Quartalsweise: Alle Firewall-Regeln reviewen
- Ungenutzte Regeln identifizieren
- Temporäre Regeln verlängern oder löschen
- Dokumentation aktualisieren

## 4. Network Access Control (NAC)

### 4.1 NAC-System

**Plattform:** {{ meta.network.nac_solution }} (z.B. Cisco ISE, Aruba ClearPass)

**Funktionen:**
- 802.1X Authentifizierung
- MAC-Address-Authentication (MAB)
- Guest-Access
- Posture-Assessment

### 4.2 802.1X Authentifizierung

**Für Workstations:**
- Computer-Authentifizierung (Machine Auth)
- Benutzer-Authentifizierung (User Auth)
- Zertifikat-basiert oder EAP-TLS

**Für Server:**
- Zertifikat-basierte Authentifizierung
- Dedizierte VLANs

### 4.3 Posture-Assessment

**Compliance-Checks:**
- Antivirus aktiv und aktuell?
- Firewall aktiviert?
- OS-Patches aktuell?
- Disk-Verschlüsselung aktiviert?

**Bei Non-Compliance:**
- Quarantäne-VLAN
- Eingeschränkter Zugriff (nur Patch-Server)
- Benachrichtigung an Nutzer

### 4.4 Guest-Access

**Guest-VLAN:**
- Isoliert von Corporate Network
- Nur Internet-Zugriff
- Captive Portal für Registrierung

**Prozess:**
1. Gast registriert sich (Self-Service oder Sponsor)
2. Credentials per SMS/E-Mail
3. Zeitlich befristeter Zugang (max. 24 Stunden)
4. Automatische Deaktivierung

## 5. Intrusion Detection/Prevention (IDS/IPS)

### 5.1 IDS/IPS-Platzierung

**Perimeter:**
- Vor Firewall (IDS)
- Hinter Firewall (IPS)

**Intern:**
- Zwischen kritischen Zonen
- IPS-Modus

**IDS/IPS-System:** {{ meta.security.ids_ips }}

### 5.2 Signaturen und Policies

**Signature-Updates:**
- Automatisch, täglich
- Kritische Signaturen: Sofort

**IPS-Policies:**
- Balanced (Standard)
- Connectivity (weniger aggressiv)
- Security (aggressiver)

### 5.3 Alerting

**SIEM-Integration:**
- Alle IDS/IPS-Alerts zu SIEM
- Korrelation mit anderen Events
- Automatische Response (bei kritischen Alerts)

## 6. VPN und Remote Access

### 6.1 VPN-Typen

**Site-to-Site VPN:**
- Zwischen Standorten
- IPsec
- Always-On

**Remote Access VPN:**
- Für Remote-Mitarbeiter
- SSL-VPN oder IPsec
- MFA verpflichtend

**Details:** Siehe `0510_Richtlinie_MDM_BringYourOwnDevice_und_Remote_Access.md`

### 6.2 VPN-Segmentierung

**VPN-Nutzer in separatem VLAN:**
- Nicht direkt im Corporate Network
- Firewall-Regeln für Zugriff
- Posture-Assessment vor Zugriff

## 7. Wireless Security

### 7.1 WLAN-Segmentierung

**Corporate WLAN:**
- 802.1X Authentifizierung
- WPA3-Enterprise
- Zugriff auf Corporate Resources

**Guest WLAN:**
- Captive Portal
- WPA2/WPA3-Personal
- Nur Internet-Zugriff

**IoT WLAN:**
- Separates VLAN
- MAC-Address-Whitelist
- Eingeschränkter Zugriff

### 7.2 WLAN-Security

**Verschlüsselung:**
- WPA3-Enterprise (Corporate)
- WPA2/WPA3-Personal (Guest)
- Kein WEP, WPA

**Rogue AP Detection:**
- Automatische Scans
- Alerts bei unautorisierten APs

## 8. Network Monitoring

### 8.1 Flow-Monitoring

**NetFlow/sFlow:**
- Sammlung von Flow-Daten
- Analyse von Traffic-Mustern
- Anomalie-Erkennung

**Tools:** {{ meta.network.flow_tool }}

### 8.2 Packet Capture

**Für Forensik:**
- Packet-Capture an kritischen Punkten
- Retention: 7 Tage
- Zugriff nur für Security-Team

## 9. Compliance und Audit

### 9.1 Messgrößen (KPIs)

| Metrik | Zielwert |
|--------|----------|
| Firewall-Regel-Review-Completion | 100% quartalsweise |
| Ungenutzte Firewall-Regeln | < 10% |
| NAC-Compliance-Rate | > 95% |
| IPS-False-Positive-Rate | < 5% |

### 9.2 Audit-Nachweise

- Firewall-Konfigurationen
- Firewall-Change-Logs
- NAC-Compliance-Reports
- IDS/IPS-Alerts und -Responses

## 10. Referenzen

### Interne Dokumente
- `0600_Policy_Netzwerksicherheit.md`
- `0370_Richtlinie_Change_Management_mit_Sicherheitsfreigaben.md`

### Externe Standards
- **ISO/IEC 27001:2022 Annex A.8.20** - Networks security
- **ISO/IEC 27001:2022 Annex A.8.21** - Security of network services
- **ISO/IEC 27001:2022 Annex A.8.22** - Segregation of networks
- **NIST SP 800-41** - Guidelines on Firewalls and Firewall Policy

**Genehmigt durch:** {{ meta.ciso.name }}, CISO  
**Nächster Review:** {{ meta-handbook.next_review }}

