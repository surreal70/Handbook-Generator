# Appendix: Network Plan and Zone Model (Template)

**Document-ID:** BSI-GRUNDSCHUTZ-0730
**Organisation:** AdminSend GmbH
**Owner:** [TODO]
**Approved by:** [TODO]
**Revision:** [TODO]
**Author:** Handbook-Generator
**Status:** Draft
**Classification:** Internal
**Last Update:** [TODO]
**Template Version:** [TODO]

---

---



## 1. Purpose and Objectives

The documentation of network architecture and zone model of **AdminSend GmbH** serves:
- Structure Analysis (Document 0050)
- Risk Analysis (Document 0090)
- Network Security (Document 0460/0470)
- Incident Response (Document 0320/0330)

**Responsible:** [TODO] (IT Management)

## 2. High-Level Network Plan

**Storage Location:** `diagrams/network-highlevel.png` or [TODO: Confluence/SharePoint]

**Representation:**
- All network zones
- Firewalls and trust boundaries
- Main connections (Internet, WAN, VPN)
- Critical systems

**Tools:** [TODO: e.g., Lucidchart, Draw.io, Visio]

## 3. Network Zones and Segmentation

| Zone ID | Zone Name | Description | Trust Level | Access Control | Responsible | Note |
|---|---|---|---|---|---|---|
| Z-001 | Internet | Public Internet | Untrusted | Firewall (Deny All) | [TODO] | [TODO] |
| Z-002 | DMZ | Demilitarized Zone (Web Server, Mail Gateway) | Low Trust | Firewall (Whitelist) | [TODO] | [TODO] |
| Z-003 | Internal LAN | Internal Corporate Network | Trusted | Firewall (Default Allow) | [TODO] | [[ netbox.vlan.name ]] |
| Z-004 | Server VLAN | Production Servers | High Trust | Firewall (Whitelist) | [TODO] | [[ netbox.vlan.name ]] |
| Z-005 | Database VLAN | Database Servers | High Trust | Firewall (Strict Whitelist) | [TODO] | [[ netbox.vlan.name ]] |
| Z-006 | Management VLAN | Management Network (Monitoring, Backup, Admin) | High Trust | Firewall (Strict Whitelist) | [TODO] | [[ netbox.vlan.name ]] |
| Z-007 | Guest WiFi | Guest WLAN | Untrusted | Captive Portal, Firewall | [TODO] | [TODO] |
| Z-008 | VPN | Remote Access (VPN) | Trusted (after authentication) | VPN Gateway, MFA | [TODO] | [TODO] |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## 4. Trust Boundaries and Firewall Rules

### 4.1 Trust Boundaries

**Definition:** Trust boundaries are borders between network zones with different trust levels.

**Main Boundaries:**
1. **Internet ↔ DMZ:** Firewall with strict rules (only HTTP/HTTPS inbound)
2. **DMZ ↔ Internal LAN:** Firewall with whitelist (only defined connections)
3. **Internal LAN ↔ Server VLAN:** Firewall with whitelist
4. **Server VLAN ↔ Database VLAN:** Firewall with strict whitelist (only DB ports)
5. **Management VLAN ↔ All Zones:** Firewall with strict whitelist (only admin access)

### 4.2 Firewall Rules (Example)

| Rule ID | Source | Destination | Service/Port | Action | Justification | Owner |
|---|---|---|---|---|---|---|
| FW-001 | Internet | DMZ (Web Server) | HTTPS (443) | Allow | Public web access | [TODO] |
| FW-002 | DMZ (Web Server) | Server VLAN (App Server) | HTTPS (8443) | Allow | Backend communication | [TODO] |
| FW-003 | Server VLAN (App Server) | Database VLAN (DB Server) | PostgreSQL (5432) | Allow | Database access | [TODO] |
| FW-004 | Management VLAN | All Zones | SSH (22), RDP (3389) | Allow | Admin access | [TODO] |
| FW-005 | Guest WiFi | Internet | HTTP/HTTPS (80/443) | Allow | Internet access for guests | [TODO] |
| FW-006 | Guest WiFi | Internal LAN | All | Deny | Isolation from internal network | [TODO] |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

**Reference:** Document 0460/0470 (Network Security)

## 5. Network Devices

| Device ID | Type | Model | Location | IP Address | Management IP | Role | Owner | Note |
|---|---|---|---|---|---|---|---|---|
| [[ netbox.device.id ]] | [[ netbox.device.type ]] | [[ netbox.device.model ]] | [[ netbox.site.name ]] | [[ netbox.ipaddress.address ]] | [TODO] | [[ netbox.device.role ]] | [TODO] | [TODO] |
| [TODO] | Firewall | [TODO] | [TODO] | [TODO] | [TODO] | Perimeter Firewall | [TODO] | [TODO] |
| [TODO] | Switch | [TODO] | [TODO] | [TODO] | [TODO] | Core Switch | [TODO] | [TODO] |
| [TODO] | Router | [TODO] | [TODO] | [TODO] | [TODO] | Internet Router | [TODO] | [TODO] |

**NetBox Integration:** [[ netbox.url ]]

## 6. VLANs

| VLAN ID | VLAN Name | Network (CIDR) | Gateway | Description | Zone | Note |
|---|---|---|---|---|---|---|
| [[ netbox.vlan.id ]] | [[ netbox.vlan.name ]] | [TODO: e.g., 10.0.10.0/24] | [TODO] | [TODO] | [TODO] | [TODO] |
| [TODO] | Management | [TODO] | [TODO] | Management Network | Z-006 | [TODO] |
| [TODO] | Servers | [TODO] | [TODO] | Production Servers | Z-004 | [TODO] |
| [TODO] | Database | [TODO] | [TODO] | Database Servers | Z-005 | [TODO] |

## 7. Administrative Access

### 7.1 Bastion/Jump Hosts

**Bastion Host:** [TODO: Hostname/IP]  
**Purpose:** Central access point for administrative access to production systems  
**Authentication:** MFA (Multi-Factor Authentication)  
**Protocols:** SSH, RDP  
**Logging:** All access is logged (SIEM)

**Reference:** Document 0200/0210 (Access Control)

### 7.2 Remote Admin

**VPN Gateway:** [TODO: Hostname/IP]  
**Authentication:** MFA (Multi-Factor Authentication)  
**Protocol:** IPsec/IKEv2 or OpenVPN  
**Access:** Only for authorized administrators  
**Logging:** All VPN connections are logged

**Reference:** Document 0470 (VPN and Admin Access)

### 7.3 Break-Glass Access

**Emergency Access:** [TODO: Description]  
**Activation:** Only in emergencies (documented)  
**Monitoring:** Immediate notification upon use

**Reference:** BCM Document (Emergency Access)

## 8. Network Monitoring

**Monitoring Tools:**
- **SIEM:** [TODO: e.g., Splunk, ELK]
- **Network Monitoring:** [TODO: e.g., Nagios, Zabbix, PRTG]
- **Flow Analysis:** [TODO: e.g., NetFlow, sFlow]

**Monitored Metrics:**
- Bandwidth utilization
- Firewall logs
- Anomalies (e.g., port scans, DDoS)
- VPN connections

**Reference:** Document 0300/0310 (Logging and Monitoring)

## 9. Network Diagrams

**Available Diagrams:**
1. **High-Level Network Plan:** Overview of all zones and main connections
2. **Detailed Network Plan:** All devices, VLANs, IP addresses
3. **Firewall Topology:** All firewalls and trust boundaries
4. **WAN Topology:** Site connectivity (if applicable)
5. **Cloud Integration:** Connections to cloud providers (AWS, Azure, etc.)

**Storage Location:** `diagrams/` or [TODO: Confluence/SharePoint]

## 10. Site Connectivity (WAN)

**If applicable:**

| Site | Connection Type | Bandwidth | Provider | Backup Connection | Encryption | Note |
|---|---|---|---|---|---|---|
| [[ netbox.site.name ]] | [TODO: e.g., MPLS, VPN] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## 11. Cloud Integration

**Cloud Providers:**

| Provider | Service | Connection Type | Encryption | Region | Note |
|---|---|---|---|---|---|
| AWS | EC2, S3, RDS | VPN (Site-to-Site) | IPsec | EU-West-1 | [TODO] |
| Azure | [TODO] | ExpressRoute | [TODO] | West Europe | [TODO] |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

**Reference:** Document 0400/0410 (Suppliers and Cloud Security)

## 12. Responsibilities (RACI)

| Activity | IT Management | Network Admin | CISO | Firewall Admin |
|---|---|---|---|---|
| Maintain Network Plan | A | R | I | C |
| Change Firewall Rules | A | C | C | R |
| VLAN Configuration | A | R | I | I |
| Network Monitoring | A | R | C | I |
| Annual Review | A | R | C | C |

**Legend:**
- **R** = Responsible (Execution responsibility)
- **A** = Accountable (Overall responsibility)
- **C** = Consulted
- **I** = Informed

## 13. Change Management

**Changes to Network Architecture:**
- All changes require change ticket
- Security-relevant changes require CISO approval
- Network plan must be updated after changes

**Reference:** Document 0380/0390 (Change Management)

## 14. Approval

| Role | Name | Date | Approval |
|---|---|---|---|
| IT Management | [TODO] | [TODO] | Draft |
| CISO | [TODO] | [TODO] | Draft |

**References:**
- BSI IT-Grundschutz-Kompendium: NET.1.1 Network Architecture and Design
- BSI IT-Grundschutz-Kompendium: NET.1.2 Network Management
- BSI IT-Grundschutz-Kompendium: NET.3.2 Firewall
- Document 0050: Structure Analysis
- Document 0090: Risk Analysis
- Document 0460/0470: Network Security

