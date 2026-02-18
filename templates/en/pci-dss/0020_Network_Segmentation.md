# Network Segmentation

**Document-ID:** [FRAMEWORK]-0020
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

## 1. Purpose

This document describes the network segmentation used to isolate the Cardholder Data Environment (CDE) from the rest of the corporate network.

### 1.1 Objectives

- **Scope Reduction:** Minimize PCI-DSS-relevant systems
- **Risk Minimization:** Limit potential attack surfaces
- **Compliance:** Meet PCI-DSS Requirement 1
- **Security:** Protect cardholder data through network isolation

## 2. Network Architecture

### 2.1 Network Segments

**CDE Segments:**

| Segment ID | Segment Name | VLAN ID | IP Range | Purpose |
|------------|--------------|---------|----------|---------|
| [TODO: CDE-CORE] | CDE Core | [TODO: 100] | [TODO: 10.1.100.0/24] | CHD Storage |
| [TODO: CDE-DMZ] | CDE DMZ | [TODO: 101] | [TODO: 10.1.101.0/24] | CHD Transit |
| [TODO: CDE-MGMT] | CDE Management | [TODO: 102] | [TODO: 10.1.102.0/24] | CDE Administration |

**Non-CDE Segments:**

| Segment ID | Segment Name | VLAN ID | IP Range | Purpose |
|------------|--------------|---------|----------|---------|
| [TODO: CORP] | Corporate | [TODO: 10] | [TODO: 10.1.10.0/24] | Office Network |
| [TODO: GUEST] | Guest | [TODO: 20] | [TODO: 10.1.20.0/24] | Guest WiFi |
| [TODO: DEV] | Development | [TODO: 30] | [TODO: 10.1.30.0/24] | Development |

### 2.2 Network Diagram

[TODO: Insert network diagram - see diagrams/network_segmentation.png]

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

## 3. Firewall Configuration

### 3.1 Firewall Overview

| Firewall ID | Type | Location | Function | Vendor/Model |
|-------------|------|----------|----------|--------------|
| [TODO: FW-PERIMETER] | Perimeter | [TODO: DC1] | Internet Border | [TODO: Vendor/Model] |
| [TODO: FW-CDE] | Internal | [TODO: DC1] | CDE Segmentation | [TODO: Vendor/Model] |
| [TODO: FW-MGMT] | Internal | [TODO: DC1] | Management Access | [TODO: Vendor/Model] |

### 3.2 Firewall Rules (CDE Segmentation)

**Basic Principle:** Default Deny (all connections blocked by default)

#### 3.2.1 Inbound Connections to CDE

| Rule ID | Source | Destination | Port/Protocol | Purpose | Approved By |
|---------|--------|-------------|---------------|---------|-------------|
| [TODO: FW-001] | Internet | CDE-DMZ | 443/TCP | HTTPS E-Commerce | [TODO: CISO] |
| [TODO: FW-002] | Corporate | CDE-MGMT | 22/TCP | SSH Admin | [TODO: CISO] |
| [TODO: FW-003] | Acquiring Bank | CDE-CORE | 443/TCP | Payment API | [TODO: CISO] |

#### 3.2.2 Outbound Connections from CDE

| Rule ID | Source | Destination | Port/Protocol | Purpose | Approved By |
|---------|--------|-------------|---------------|---------|-------------|
| [TODO: FW-101] | CDE-CORE | Acquiring Bank | 443/TCP | Authorization | [TODO: CISO] |
| [TODO: FW-102] | CDE-CORE | Update Server | 443/TCP | Security Updates | [TODO: CISO] |
| [TODO: FW-103] | CDE-MGMT | SIEM | 514/TCP | Log Forwarding | [TODO: CISO] |

#### 3.2.3 Blocked Connections

**Explicitly blocked:**
- CDE → Corporate Network (except Management)
- Corporate → CDE (except authorized admin access)
- CDE → Internet (except explicitly allowed services)
- Guest → CDE (all connections)

### 3.3 Firewall Rule Review

**Review Interval:** Quarterly  
**Responsible:** [TODO: Network Security Team]  
**Last Review:** [TODO: Date]  
**Next Review:** [TODO: Date]  

**Review Process:**
1. Review all firewall rules
2. Identify unused rules
3. Validate business justification
4. Document changes
5. CISO approval

## 4. Router Configuration

### 4.1 Router Overview

| Router ID | Location | Function | Vendor/Model |
|-----------|----------|----------|--------------|
| [TODO: RTR-CORE] | [TODO: DC1] | Core Routing | [TODO: Vendor/Model] |
| [TODO: RTR-CDE] | [TODO: DC1] | CDE Routing | [TODO: Vendor/Model] |

### 4.2 Access Control Lists (ACLs)

[TODO: Document router ACLs similar to firewall rules]

## 5. Segmentation Validation

### 5.1 Validation Methods

**Annual validation required (PCI-DSS Req 11.4.6):**

1. **Penetration Testing:**
   - Attempt to bypass CDE segmentation
   - Test firewall rules
   - Validate network isolation

2. **Network Scans:**
   - Port scans from different segments
   - Reachability tests
   - Routing validation

3. **Configuration Review:**
   - Review firewall configurations
   - Check router ACLs
   - VLAN configuration validation

### 5.2 Validation History

| Date | Method | Performed By | Result | Actions |
|------|--------|--------------|--------|---------|
| [TODO: 2025-12-01] | Penetration Test | [TODO: Company] | Successful | None |
| [TODO: 2025-06-15] | Network Scan | [TODO: Team] | 1 Vulnerability | Rule FW-042 removed |

### 5.3 Next Validation

**Planned Date:** [TODO: Date]  
**Method:** [TODO: Penetration Test/Scan]  
**Performing Company:** [TODO: Name]  

## 6. Wireless Networks

### 6.1 Wireless Segmentation

**Wireless Networks:**

| SSID | Segment | Encryption | CDE Access | Purpose |
|------|---------|------------|------------|---------|
| [TODO: Corp-WiFi] | Corporate | WPA3-Enterprise | No | Employees |
| [TODO: Guest-WiFi] | Guest | WPA3-Personal | No | Guests |
| [TODO: CDE-WiFi] | CDE-MGMT | WPA3-Enterprise + MFA | Yes | CDE Admin |

**Important:** Wireless networks with CDE access require:
- WPA3 or higher
- Multi-Factor Authentication
- Separate VLAN segmentation
- Encrypted transmission

### 6.2 Wireless Access Points

| AP ID | Location | SSID | Segment | Firmware Version |
|-------|----------|------|---------|------------------|
| [TODO: AP-001] | [TODO: Office] | Corp-WiFi | Corporate | [TODO: v2.1] |
| [TODO: AP-002] | [TODO: DC] | CDE-WiFi | CDE-MGMT | [TODO: v2.1] |

## 7. Remote Access

### 7.1 VPN Configuration

**VPN Access to CDE:**

| VPN Type | Target Group | Authentication | Target Segment | Encryption |
|----------|--------------|----------------|----------------|------------|
| [TODO: SSL-VPN] | Administrators | MFA (Token) | CDE-MGMT | TLS 1.3 |
| [TODO: IPSec-VPN] | Service Providers | MFA (Certificate) | CDE-MGMT | AES-256 |

**VPN Requirements:**
- Multi-Factor Authentication (MFA) required
- Encryption: TLS 1.2+ or IPSec with AES-256
- Session timeout: [TODO: 15 minutes inactivity]
- Logging of all VPN connections

### 7.2 Jump Server / Bastion Hosts

**Jump Server for CDE Access:**

| Server ID | Location | Function | Access Method |
|-----------|----------|----------|---------------|
| [TODO: JUMP-01] | CDE-MGMT | Admin Access | SSH/RDP via VPN |

**Jump Server Requirements:**
- No direct Internet connection
- Access only via VPN with MFA
- Complete logging of all sessions
- No local data storage

## 8. Monitoring and Alerting

### 8.1 Network Monitoring

**Monitored Metrics:**
- Firewall rule violations
- Unexpected connection attempts to CDE
- Changes to firewall configurations
- Network traffic anomalies

**Monitoring Tools:**
- [TODO: SIEM System]
- [TODO: Network Monitoring Tool]
- [TODO: IDS/IPS]

### 8.2 Alerting Rules

| Alert ID | Condition | Severity | Notification |
|----------|-----------|----------|--------------|
| [TODO: ALT-001] | Connection from Corporate to CDE-CORE | Critical | SOC + CISO |
| [TODO: ALT-002] | Firewall rule change | High | Network Team |
| [TODO: ALT-003] | Failed VPN login (3x) | Medium | Security Team |

## 9. Change Management

### 9.1 Change Process

**Process for Network Changes:**

1. **Change Request:** Formal request with justification
2. **Security Review:** Assessment of PCI-DSS impact
3. **Testing:** Test in non-production environment
4. **Approval:** CISO approval for CDE changes
5. **Implementation:** Execute with rollback plan
6. **Documentation:** Update this document
7. **Validation:** Verify segmentation

### 9.2 Change History

| Date | Change | Justification | Approved By | Validated |
|------|--------|---------------|-------------|-----------|
| [TODO: 2026-01-15] | New firewall rule FW-105 | Payment API | [TODO: CISO] | Yes |

<!-- End of template -->
