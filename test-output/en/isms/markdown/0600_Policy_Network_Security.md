# Policy: Network Security

**Document-ID:** ISMS-0600
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



**Document ID:** 0600  
**Document Type:** Policy (abstract)  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.8.20-A.8.23 (incl. Amendment 1:2024)  
**Owner:** [TODO]  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** [TODO]  
**Next Review:** [TODO]

## 1. Purpose

This policy defines the requirements for network security at **AdminSend GmbH**. It ensures that networks are properly secured, segmented, and monitored to protect the confidentiality, integrity, and availability of information.

## 2. Scope

This policy applies to:

- **Organizational Units:** All departments and locations of AdminSend GmbH
- **Networks:** All internal and external networks, LAN, WLAN, WAN, VPN
- **Systems:** Firewalls, routers, switches, load balancers, IDS/IPS
- **Connections:** All network connections (internal, external, partner, cloud)
- **Locations:** [[ netbox.site.name ]] and all other operational sites

**Exceptions:** Exceptions are only permitted through the defined exception process (`0640_Policy_Exceptions_and_Risk_Waivers.md`).

## 3. Principles (Policy Statements)

### 3.1 Network Segmentation
Networks are segmented by protection requirements and function. Segmentation is achieved through firewalls, VLANs, and zones (e.g., DMZ, production network, management network).

### 3.2 Defense in Depth
Network security follows the defense-in-depth principle. Multiple security layers protect against attacks (perimeter, segmentation, host-based).

### 3.3 Least Privilege Network Access
Network access follows the least privilege principle. Only required connections are permitted (default deny, whitelist approach).

### 3.4 Firewall Management
Firewalls protect network boundaries. Firewall rules are documented, regularly reviewed, and changed according to change management process.

### 3.5 Network Access Control (NAC)
Access to networks is controlled. NAC ensures that only authorized and compliant devices gain access.

### 3.6 Intrusion Detection/Prevention (IDS/IPS)
Networks are monitored for attacks. IDS/IPS systems detect and block suspicious activities.

### 3.7 VPN and Remote Access
Remote access occurs via secure VPN connections. VPN connections are encrypted and authenticated (MFA).

### 3.8 Wireless Security
WLAN networks are secured (WPA3, 802.1X). Guest WLANs are separated from production network.

### 3.9 Network Monitoring and Logging
Network activities are monitored and logged. Logs are centrally collected and analyzed (SIEM).

## 4. Roles and Responsibilities

### RACI Matrix: Network Security

| Activity | CISO | Network Security | IT Operations | SOC | Network Admin |
|----------|------|------------------|---------------|-----|---------------|
| Policy Creation | R/A | R | C | C | C |
| Network Segmentation | R | R/A | R | C | R |
| Firewall Management | C | R/A | R | C | R |
| NAC Implementation | C | R/A | R | C | R |
| IDS/IPS Operations | C | R | C | R/A | C |
| VPN Management | C | R/A | R | C | R |
| WLAN Security | C | R/A | R | C | R |
| Network Monitoring | C | R | C | R/A | C |

**Legend:** R = Responsible (Execution), A = Accountable (Ownership), C = Consulted, I = Informed

### Key Roles

- **Policy Owner:** [TODO] (CISO)
- **Network Security Manager:** {{ meta-handbook.network_security_manager }}
- **Network Administrator:** {{ meta-handbook.network_admin }}
- **SOC Manager:** {{ meta-handbook.soc_manager }}
- **Implementation Responsible:** IT Operations, Network Team
- **Control/Audit Function:** ISMS, Internal Audit, SOC

## 5. Derivatives (Guidelines/Standards/Processes)

Implementation details are defined in subordinate documents:

### Associated Guidelines
- **0610_Guideline_Segmentation_Firewalling_and_Network_Access_Control.md** - Detailed implementation guideline
- `0220_Policy_Access_Control_and_Identity_Management.md` - Access Control Policy
- `0320_Policy_Logging_and_Monitoring.md` - Logging and Monitoring Policy
- `0500_Policy_Mobile_Device_and_Remote_Work.md` - Remote Work Policy

### Associated Standards/Baselines
- Network segmentation concept
- Firewall ruleset
- NAC configuration
- IDS/IPS signatures and rules
- VPN configuration
- WLAN security baseline

### Associated Processes
- Firewall change management
- NAC onboarding/offboarding
- IDS/IPS alert response
- VPN access request
- Network security monitoring

## 6. Compliance, Monitoring and Enforcement

### Metrics and KPIs
- Network segmentation coverage (Target: 100% of critical systems)
- Firewall rule review frequency (Target: quarterly)
- NAC coverage (Target: 100% production network)
- IDS/IPS alert response time (Target: < 15 minutes for critical alerts)
- VPN availability (Target: 99.5%)
- WLAN security compliance (Target: 100% WPA3)
- Number of blocked attacks (IDS/IPS)

### Evidence and Proof
- Network diagrams and segmentation concept
- Firewall ruleset and change logs
- NAC configuration and device inventory
- IDS/IPS logs and alert reports
- VPN logs and access logs
- WLAN configuration and security scans
- Network monitoring dashboards

### Consequences of Violations
Violations of this policy are handled according to applicable HR and compliance processes:
- **Unauthorized Firewall Changes:** Incident response, rollback, disciplinary action
- **Missing Segmentation:** Completion, risk assessment
- **Insecure WLAN Configuration:** Immediate correction, incident response
- **Repeated Violations:** Employment consequences, access revocation

## 7. Exceptions

Exceptions to this policy are only permitted in justified exceptional cases:

- **Exception Process:** See `0640_Policy_Exceptions_and_Risk_Waivers.md`
- **Approval:** Exceptions must be approved by CISO and Network Security Manager
- **Documentation:** All exceptions are documented in the risk register
- **Time Limitation:** Exceptions are generally time-limited

## 8. References

### Internal Documents
- `0010_ISMS_Information_Security_Policy.md` - ISMS Policy
- `0610_Guideline_Segmentation_Firewalling_and_Network_Access_Control.md` - Detailed Guideline
- `0220_Policy_Access_Control_and_Identity_Management.md` - Access Control Policy
- `0080_ISMS_Risk_Register_Template.md` - Risk Register

### External Standards and Requirements
- **ISO/IEC 27001:2022 Annex A.8.20** - Networks security
- **ISO/IEC 27001:2022 Annex A.8.21** - Security of network services
- **ISO/IEC 27001:2022 Annex A.8.22** - Segregation of networks
- **ISO/IEC 27001:2022 Annex A.8.23** - Web filtering
- **NIST SP 800-41** - Guidelines on Firewalls and Firewall Policy
- **NIST SP 800-97** - Establishing Wireless Robust Security Networks
- **BSI IT-Grundschutz** - NET.1.1, NET.1.2, NET.3.2

**Approved by:**  
{{ meta-handbook.management_ceo }}, Management  
Date: [TODO]

**Next Review:** [TODO] (annually or as needed)

