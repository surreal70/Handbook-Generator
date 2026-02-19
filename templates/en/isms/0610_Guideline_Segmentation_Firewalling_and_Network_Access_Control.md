# Guideline: Segmentation, Firewalling and Network Access Control

**Document-ID:** [FRAMEWORK]-0610
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Approved by:** {{ meta-handbook.approver }}
**Revision:** [TODO]
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Classification:** {{ meta-handbook.classification }}
**Last Update:** {{ meta-handbook.modifydate }}
**Template Version:** [TODO]

---

---

## 1. Purpose and Scope

This guideline specifies the `0600_Policy_Network_Security.md` and defines:
- Network segmentation and zone model
- Firewall rules and management
- Network Access Control (NAC)

**Scope:** All networks at **{{ meta-organisation.name }}**

## 2. Network Segmentation

### 2.1 Zone Model

**Zone 1: Internet (Untrusted)**
- Public internet
- No trust relationship

**Zone 2: DMZ (Demilitarized Zone)**
- Internet-facing services (web servers, email gateway)
- Restricted access to internal resources

**Zone 3: Corporate Network**
- Internal office networks
- Workstations, printers
- Standard security controls

**Zone 4: Server Network**
- Internal servers (file servers, application servers)
- Enhanced security controls

**Zone 5: Management Network**
- Management interfaces (IPMI, iLO, iDRAC)
- Out-of-band management
- Highest security controls

**Zone 6: Production Network**
- Critical production systems
- Databases, ERP
- Highest security controls

### 2.2 VLAN Segmentation

**VLAN Schema:**
- VLAN 10: Management
- VLAN 20: Servers
- VLAN 30: Workstations
- VLAN 40: Guest/BYOD
- VLAN 50: IoT/OT
- VLAN 60: DMZ

**Inter-VLAN Routing:**
- Via firewall (not Layer 3 switch)
- Explicit firewall rules required

### 2.3 Micro-Segmentation

**For Critical Systems:**
- Segmentation at workload level
- Software-Defined Networking (SDN)
- Zero Trust Network Access (ZTNA)

## 3. Firewall Management

### 3.1 Firewall Architecture

**Perimeter Firewall:**
- Internet ↔ DMZ
- Internet ↔ Corporate Network
- High availability (Active/Active or Active/Passive)

**Internal Firewalls:**
- Between zones
- Micro-segmentation

**Firewall Platform:** {{ meta-handbook.network_firewall }}

### 3.2 Firewall Rules

**Default Deny:**
- All connections blocked by default
- Only explicitly allowed connections

**Rule Structure:**
- Source (IP/network)
- Destination (IP/network)
- Service (port/protocol)
- Action (Allow/Deny)
- Logging (Enabled)
- Justification (business justification)

**Rule Order:**
1. Deny rules (specific)
2. Allow rules (specific to general)
3. Default deny (implicit)

### 3.3 Firewall Change Process

**Request:**
- Change request via ticket system
- Justification (business justification)
- Source and destination IP/port
- Time limitation (where possible)

**Approval:**
- IT Security: Mandatory
- Network team: Technical feasibility
- Application owner: Business justification

**Implementation:**
- Testing in dev/test (where possible)
- Implementation in maintenance window
- Verification
- Documentation

**Details:** See `0370_Guideline_Change_Management_with_Security_Approvals`

### 3.4 Firewall Review

**Regular Reviews:**
- Quarterly: Review all firewall rules
- Identify unused rules
- Extend or delete temporary rules
- Update documentation

## 4. Network Access Control (NAC)

### 4.1 NAC System

**Platform:** {{ meta-handbook.network_nac_solution }} (e.g., Cisco ISE, Aruba ClearPass)

**Functions:**
- 802.1X authentication
- MAC address authentication (MAB)
- Guest access
- Posture assessment

### 4.2 802.1X Authentication

**For Workstations:**
- Computer authentication (machine auth)
- User authentication (user auth)
- Certificate-based or EAP-TLS

**For Servers:**
- Certificate-based authentication
- Dedicated VLANs

### 4.3 Posture Assessment

**Compliance Checks:**
- Antivirus active and current?
- Firewall enabled?
- OS patches current?
- Disk encryption enabled?

**For Non-Compliance:**
- Quarantine VLAN
- Restricted access (patch servers only)
- Notification to user

### 4.4 Guest Access

**Guest VLAN:**
- Isolated from corporate network
- Internet access only
- Captive portal for registration

**Process:**
1. Guest registers (self-service or sponsor)
2. Credentials via SMS/email
3. Time-limited access (max. 24 hours)
4. Automatic deactivation

## 5. Intrusion Detection/Prevention (IDS/IPS)

### 5.1 IDS/IPS Placement

**Perimeter:**
- Before firewall (IDS)
- Behind firewall (IPS)

**Internal:**
- Between critical zones
- IPS mode

**IDS/IPS System:** {{ meta-handbook.security_ids_ips }}

### 5.2 Signatures and Policies

**Signature Updates:**
- Automatic, daily
- Critical signatures: Immediate

**IPS Policies:**
- Balanced (standard)
- Connectivity (less aggressive)
- Security (more aggressive)

### 5.3 Alerting

**SIEM Integration:**
- All IDS/IPS alerts to SIEM
- Correlation with other events
- Automatic response (for critical alerts)

## 6. VPN and Remote Access

### 6.1 VPN Types

**Site-to-Site VPN:**
- Between locations
- IPsec
- Always-on

**Remote Access VPN:**
- For remote employees
- SSL-VPN or IPsec
- MFA mandatory

**Details:** See `0510_Guideline_MDM_BringYourOwnDevice_and_Remote_Access.md`

### 6.2 VPN Segmentation

**VPN Users in Separate VLAN:**
- Not directly in corporate network
- Firewall rules for access
- Posture assessment before access

## 7. Wireless Security

### 7.1 WLAN Segmentation

**Corporate WLAN:**
- 802.1X authentication
- WPA3-Enterprise
- Access to corporate resources

**Guest WLAN:**
- Captive portal
- WPA2/WPA3-Personal
- Internet access only

**IoT WLAN:**
- Separate VLAN
- MAC address whitelist
- Restricted access

### 7.2 WLAN Security

**Encryption:**
- WPA3-Enterprise (corporate)
- WPA2/WPA3-Personal (guest)
- No WEP, WPA

**Rogue AP Detection:**
- Automatic scans
- Alerts for unauthorized APs

## 8. Network Monitoring

### 8.1 Flow Monitoring

**NetFlow/sFlow:**
- Collection of flow data
- Analysis of traffic patterns
- Anomaly detection

**Tools:** {{ meta-handbook.network_flow_tool }}

### 8.2 Packet Capture

**For Forensics:**
- Packet capture at critical points
- Retention: 7 days
- Access only for security team

## 9. Compliance and Audit

### 9.1 Metrics (KPIs)

| Metric | Target Value |
|--------|--------------|
| Firewall rule review completion | 100% quarterly |
| Unused firewall rules | < 10% |
| NAC compliance rate | > 95% |
| IPS false positive rate | < 5% |

### 9.2 Audit Evidence

- Firewall configurations
- Firewall change logs
- NAC compliance reports
- IDS/IPS alerts and responses

## 10. References

### Internal Documents
- `0600_Policy_Network_Security.md`
- `0370_Guideline_Change_Management_with_Security_Approvals.md`

### External Standards
- **ISO/IEC 27001:2022 Annex A.8.20** - Networks security
- **ISO/IEC 27001:2022 Annex A.8.21** - Security of network services
- **ISO/IEC 27001:2022 Annex A.8.22** - Segregation of networks
- **NIST SP 800-41** - Guidelines on Firewalls and Firewall Policy

**Approved by:** {{ meta-organisation-roles.role_CISO }}, CISO  
**Next Review:** {{ meta-handbook.next_review }}

