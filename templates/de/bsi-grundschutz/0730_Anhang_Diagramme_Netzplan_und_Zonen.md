# Anhang: Netzplan und Zonenmodell (Template)

**Dokument-ID:** 0730  
**Dokumenttyp:** Anhang  
**Referenzrahmen:** BSI IT-Grundschutz (BSI Standards 200-1/200-2)  
**Owner:** {{ meta.document.owner }}  
**Version:** {{ meta.document.version }}  
**Status:** {{ meta.document.status }}  
**Klassifizierung:** {{ meta.document.classification }}  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  
**Nächster Review:** {{ meta.document.next_review }}

---

<!-- 
TEMPLATE AUTHOR NOTE:
This template documents network architecture, zones, and trust boundaries.
Reference: BSI IT-Grundschutz-Kompendium: NET.1.1 Netzarchitektur und -design
-->

## 1. Zweck und Zielsetzung

Die Dokumentation der Netzarchitektur und des Zonenmodells von **{{ meta.organization.name }}** dient:
- Strukturanalyse (Dokument 0050)
- Risikoanalyse (Dokument 0090)
- Netzwerksicherheit (Dokument 0460/0470)
- Incident Response (Dokument 0320/0330)

**Verantwortlich:** {{ meta.cio.name }} (IT-Leitung)

## 2. High-Level Netzplan

**Ablageort:** `diagrams/network-highlevel.png` oder [TODO: Confluence/SharePoint]

**Darstellung:**
- Alle Netzwerkzonen
- Firewalls und Trust Boundaries
- Hauptverbindungen (Internet, WAN, VPN)
- Kritische Systeme

**Tools:** [TODO: z.B. Lucidchart, Draw.io, Visio]

## 3. Netzwerkzonen und Segmentierung

| Zone-ID | Zonenname | Beschreibung | Trust Level | Zugriffskontrolle | Verantwortlich | Notiz |
|---|---|---|---|---|---|---|
| Z-001 | Internet | Öffentliches Internet | Untrusted | Firewall (Deny All) | {{ meta.cio.name }} | [TODO] |
| Z-002 | DMZ | Demilitarisierte Zone (Webserver, Mail-Gateway) | Low Trust | Firewall (Whitelist) | {{ meta.cio.name }} | [TODO] |
| Z-003 | Internal LAN | Internes Unternehmensnetzwerk | Trusted | Firewall (Default Allow) | {{ meta.cio.name }} | {{ netbox.vlan.name }} |
| Z-004 | Server VLAN | Produktionsserver | High Trust | Firewall (Whitelist) | {{ meta.cio.name }} | {{ netbox.vlan.name }} |
| Z-005 | Database VLAN | Datenbank-Server | High Trust | Firewall (Strict Whitelist) | {{ meta.cio.name }} | {{ netbox.vlan.name }} |
| Z-006 | Management VLAN | Management-Netzwerk (Monitoring, Backup, Admin) | High Trust | Firewall (Strict Whitelist) | {{ meta.cio.name }} | {{ netbox.vlan.name }} |
| Z-007 | Guest WiFi | Gast-WLAN | Untrusted | Captive Portal, Firewall | {{ meta.cio.name }} | [TODO] |
| Z-008 | VPN | Remote-Zugriff (VPN) | Trusted (nach Authentisierung) | VPN-Gateway, MFA | {{ meta.cio.name }} | [TODO] |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## 4. Trust Boundaries und Firewall-Regeln

### 4.1 Trust Boundaries

**Definition:** Trust Boundaries sind Grenzen zwischen Netzwerkzonen mit unterschiedlichem Vertrauensniveau.

**Hauptgrenzen:**
1. **Internet ↔ DMZ:** Firewall mit strikten Regeln (nur HTTP/HTTPS eingehend)
2. **DMZ ↔ Internal LAN:** Firewall mit Whitelist (nur definierte Verbindungen)
3. **Internal LAN ↔ Server VLAN:** Firewall mit Whitelist
4. **Server VLAN ↔ Database VLAN:** Firewall mit strikter Whitelist (nur DB-Ports)
5. **Management VLAN ↔ Alle Zonen:** Firewall mit strikter Whitelist (nur Admin-Zugriffe)

### 4.2 Firewall-Regeln (Beispiel)

| Regel-ID | Quelle | Ziel | Service/Port | Aktion | Begründung | Owner |
|---|---|---|---|---|---|---|
| FW-001 | Internet | DMZ (Webserver) | HTTPS (443) | Allow | Öffentlicher Webzugriff | {{ meta.cio.name }} |
| FW-002 | DMZ (Webserver) | Server VLAN (App-Server) | HTTPS (8443) | Allow | Backend-Kommunikation | {{ meta.cio.name }} |
| FW-003 | Server VLAN (App-Server) | Database VLAN (DB-Server) | PostgreSQL (5432) | Allow | Datenbank-Zugriff | {{ meta.cio.name }} |
| FW-004 | Management VLAN | Alle Zonen | SSH (22), RDP (3389) | Allow | Admin-Zugriff | {{ meta.cio.name }} |
| FW-005 | Guest WiFi | Internet | HTTP/HTTPS (80/443) | Allow | Internet-Zugriff für Gäste | {{ meta.cio.name }} |
| FW-006 | Guest WiFi | Internal LAN | Alle | Deny | Isolation von internem Netzwerk | {{ meta.cio.name }} |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

**Referenz:** Dokument 0460/0470 (Netzwerksicherheit)

## 5. Netzwerkgeräte

| Gerät-ID | Typ | Modell | Standort | IP-Adresse | Management-IP | Rolle | Owner | Notiz |
|---|---|---|---|---|---|---|---|---|
| {{ netbox.device.id }} | {{ netbox.device.type }} | {{ netbox.device.model }} | {{ netbox.site.name }} | {{ netbox.ipaddress.address }} | [TODO] | {{ netbox.device.role }} | {{ meta.cio.name }} | [TODO] |
| [TODO] | Firewall | [TODO] | [TODO] | [TODO] | [TODO] | Perimeter-Firewall | {{ meta.cio.name }} | [TODO] |
| [TODO] | Switch | [TODO] | [TODO] | [TODO] | [TODO] | Core-Switch | {{ meta.cio.name }} | [TODO] |
| [TODO] | Router | [TODO] | [TODO] | [TODO] | [TODO] | Internet-Router | {{ meta.cio.name }} | [TODO] |

**NetBox-Integration:** {{ netbox.url }}

## 6. VLANs

| VLAN-ID | VLAN-Name | Netzwerk (CIDR) | Gateway | Beschreibung | Zone | Notiz |
|---|---|---|---|---|---|---|
| {{ netbox.vlan.id }} | {{ netbox.vlan.name }} | [TODO: z.B. 10.0.10.0/24] | [TODO] | [TODO] | [TODO] | [TODO] |
| [TODO] | Management | [TODO] | [TODO] | Management-Netzwerk | Z-006 | [TODO] |
| [TODO] | Servers | [TODO] | [TODO] | Produktionsserver | Z-004 | [TODO] |
| [TODO] | Database | [TODO] | [TODO] | Datenbank-Server | Z-005 | [TODO] |

## 7. Administrative Zugänge

### 7.1 Bastion/Jump Hosts

**Bastion Host:** [TODO: Hostname/IP]  
**Zweck:** Zentraler Zugangspunkt für administrative Zugriffe auf Produktionssysteme  
**Authentisierung:** MFA (Multi-Factor Authentication)  
**Protokolle:** SSH, RDP  
**Logging:** Alle Zugriffe werden geloggt (SIEM)

**Referenz:** Dokument 0200/0210 (Zugriffssteuerung)

### 7.2 Remote Admin

**VPN-Gateway:** [TODO: Hostname/IP]  
**Authentisierung:** MFA (Multi-Factor Authentication)  
**Protokoll:** IPsec/IKEv2 oder OpenVPN  
**Zugriff:** Nur für autorisierte Administratoren  
**Logging:** Alle VPN-Verbindungen werden geloggt

**Referenz:** Dokument 0470 (VPN und Admin-Zugänge)

### 7.3 Break-Glass-Zugang

**Notfallzugang:** [TODO: Beschreibung]  
**Aktivierung:** Nur in Notfällen (dokumentiert)  
**Überwachung:** Sofortige Benachrichtigung bei Nutzung

**Referenz:** BCM-Dokument (Notfallzugang)

## 8. Netzwerk-Monitoring

**Monitoring-Tools:**
- **SIEM:** [TODO: z.B. Splunk, ELK]
- **Network Monitoring:** [TODO: z.B. Nagios, Zabbix, PRTG]
- **Flow Analysis:** [TODO: z.B. NetFlow, sFlow]

**Überwachte Metriken:**
- Bandbreitennutzung
- Firewall-Logs
- Anomalien (z.B. Port-Scans, DDoS)
- VPN-Verbindungen

**Referenz:** Dokument 0300/0310 (Logging und Monitoring)

## 9. Netzwerk-Diagramme

**Verfügbare Diagramme:**
1. **High-Level Netzplan:** Übersicht über alle Zonen und Hauptverbindungen
2. **Detaillierter Netzplan:** Alle Geräte, VLANs, IP-Adressen
3. **Firewall-Topologie:** Alle Firewalls und Trust Boundaries
4. **WAN-Topologie:** Standortvernetzung (falls zutreffend)
5. **Cloud-Integration:** Verbindungen zu Cloud-Providern (AWS, Azure, etc.)

**Ablageort:** `diagrams/` oder [TODO: Confluence/SharePoint]

## 10. Standortvernetzung (WAN)

**Falls zutreffend:**

| Standort | Verbindungstyp | Bandbreite | Provider | Backup-Verbindung | Verschlüsselung | Notiz |
|---|---|---|---|---|---|---|
| {{ netbox.site.name }} | [TODO: z.B. MPLS, VPN] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## 11. Cloud-Integration

**Cloud-Provider:**

| Provider | Service | Verbindungstyp | Verschlüsselung | Region | Notiz |
|---|---|---|---|---|---|
| AWS | EC2, S3, RDS | VPN (Site-to-Site) | IPsec | EU-West-1 | [TODO] |
| Azure | [TODO] | ExpressRoute | [TODO] | West Europe | [TODO] |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

**Referenz:** Dokument 0400/0410 (Lieferanten und Cloud-Sicherheit)

## 12. Verantwortlichkeiten (RACI)

| Aktivität | IT-Leitung | Netzwerk-Admin | ISB | Firewall-Admin |
|---|---|---|---|---|
| Netzplan pflegen | A | R | I | C |
| Firewall-Regeln ändern | A | C | C | R |
| VLAN-Konfiguration | A | R | I | I |
| Netzwerk-Monitoring | A | R | C | I |
| Jährlicher Review | A | R | C | C |

**Legende:**
- **R** = Responsible (Durchführungsverantwortung)
- **A** = Accountable (Gesamtverantwortung)
- **C** = Consulted (Konsultiert)
- **I** = Informed (Informiert)

## 13. Änderungsmanagement

**Änderungen an Netzwerkarchitektur:**
- Alle Änderungen erfordern Change-Ticket
- Sicherheitsrelevante Änderungen erfordern ISB-Freigabe
- Netzplan muss nach Änderungen aktualisiert werden

**Referenz:** Dokument 0380/0390 (Change Management)

## 14. Freigabe

| Rolle | Name | Datum | Freigabe |
|---|---|---|---|
| IT-Leitung | {{ meta.cio.name }} | {{ meta.document.approval_date }} | {{ meta.document.approval_status }} |
| ISB | {{ meta.ciso.name }} | {{ meta.document.approval_date }} | {{ meta.document.approval_status }} |

---

**Referenzen:**
- BSI IT-Grundschutz-Kompendium: NET.1.1 Netzarchitektur und -design
- BSI IT-Grundschutz-Kompendium: NET.1.2 Netzmanagement
- BSI IT-Grundschutz-Kompendium: NET.3.2 Firewall
- Dokument 0050: Strukturanalyse
- Dokument 0090: Risikoanalyse
- Dokument 0460/0470: Netzwerksicherheit

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |

<!-- End of template -->