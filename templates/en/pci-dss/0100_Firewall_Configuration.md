# Firewall Configuration

**Document ID:** PCI-0100  
**Organization:** {{ meta.organization.name }}  
**Owner:** {{ meta.document.owner }}  
**Approved by:** {{ meta.document.approver }}  
**Version:** {{ meta.document.version }}  
**Status:** Draft / In Review / Approved  
**Classification:** {{ meta.document.classification }}  
**Last Updated:** {{ meta.document.last_updated }}  

---

<!-- 
TEMPLATE AUTHOR NOTE:
This template documents firewall configuration standards.
It aligns with PCI-DSS v4.0 Requirement 1 (Install and Maintain Network Security Controls).

Customization required:
- Document firewall standards and configurations
- Define rule management procedures
- Include change management process
- Document review procedures
-->

## 1. Purpose

This document defines firewall configuration standards for {{ meta.organization.name }} per PCI-DSS Requirement 1.

### 1.1 Objectives

- **Network Security:** Protect CDE through firewall controls
- **Access Control:** Restrict unauthorized network access
- **Compliance:** Meet PCI-DSS Requirement 1
- **Documentation:** Traceable firewall configuration

### 1.2 Scope

**Affected Systems:**
- Perimeter firewalls (Internet border)
- Internal firewalls (CDE segmentation)
- Host-based firewalls (servers, workstations)
- Cloud firewalls (if applicable)

## 2. Firewall Standards

### 2.1 Basic Principles

**Default Deny:**
- All connections blocked by default
- Only explicitly approved connections allowed
- Documentation of all exceptions required

**Least Privilege:**
- Minimum required access rights
- Specific source and destination IP addresses
- Specific ports and protocols

**Defense in Depth:**
- Multiple firewall layers
- Perimeter + internal segmentation
- Host-based firewalls as additional layer

### 2.2 Firewall Architecture

**Firewall Layers:**

1. **Perimeter Firewall:**
   - Protection from Internet threats
   - Inbound and outbound traffic
   - DMZ for public services

2. **Internal Firewall:**
   - CDE segmentation
   - Separation of corporate and CDE
   - Access control between segments

3. **Host-based Firewall:**
   - Protection of individual systems
   - Additional defense layer
   - Protection during network compromise

## 3. Firewall Rule Management

### 3.1 Rule Requirements

**Each firewall rule must contain:**
- Unique rule ID
- Source (IP address/network)
- Destination (IP address/network)
- Port/protocol
- Action (Allow/Deny)
- Business justification
- Approver
- Creation date
- Review date

### 3.2 Rule Approval Process

**Process for new rules:**

1. **Request:** Change request with justification
2. **Security Review:** Assessment by IT Security
3. **Approval:** CISO approval for CDE rules
4. **Implementation:** Configuration by network team
5. **Documentation:** Update of ruleset
6. **Validation:** Test of rule

**Approval Matrix:**

| Rule Type | Approver | Documentation |
|-----------|----------|---------------|
| CDE-related | CISO | Complete |
| Corporate | IT Manager | Standard |
| Temporary | IT Security | With expiration date |

### 3.3 Quarterly Rule Review

**Review Process:**

1. **Review all rules:** Complete review
2. **Validation:** Business justification still valid?
3. **Cleanup:** Removal of unused rules
4. **Documentation:** Update documentation
5. **Approval:** CISO confirmation

**Last Review:** [TODO: Date]  
**Next Review:** [TODO: Date]  
**Responsible:** [TODO: Network Security Team]  

## 4. Firewall Configuration Standards

### 4.1 Perimeter Firewall

**Inbound Traffic:**

| Service | Port | Protocol | Source | Destination | Allowed |
|---------|------|----------|--------|-------------|---------|
| HTTPS | 443 | TCP | Any | Web Server (DMZ) | Yes |
| SSH | 22 | TCP | Admin IPs | Jump Server | Yes (with MFA) |
| All others | * | * | Any | CDE | No |

**Outbound Traffic:**

| Service | Port | Protocol | Source | Destination | Allowed |
|---------|------|----------|--------|-------------|---------|
| HTTPS | 443 | TCP | CDE | Acquiring Bank | Yes |
| DNS | 53 | UDP | CDE | DNS Server | Yes |
| NTP | 123 | UDP | CDE | NTP Server | Yes |
| All others | * | * | CDE | Internet | No (Default Deny) |

### 4.2 Internal Firewall (CDE Segmentation)

**CDE → Corporate:**
- Blocked by default
- Exceptions only with CISO approval
- Logging of all connection attempts

**Corporate → CDE:**
- Only authorized admin access
- MFA required
- Via jump server/VPN
- Complete logging

### 4.3 Host-based Firewalls

**Requirements:**
- Enabled on all CDE systems
- Configuration per hardening standards
- Central management (if possible)
- Logging enabled

**Example Configuration (Linux iptables):**
```bash
# Default Deny
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT DROP

# Allow established connections
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Allow specific services
iptables -A INPUT -p tcp --dport 443 -j ACCEPT  # HTTPS
iptables -A INPUT -p tcp --dport 22 -s 10.1.102.0/24 -j ACCEPT  # SSH from Management

# Log dropped packets
iptables -A INPUT -j LOG --log-prefix "FW-DROP: "
```

## 5. Prohibited Configurations

**The following configurations are NOT allowed:**

- **Any-Any Rules:** No rules with Source=Any and Destination=Any
- **Direct Internet Connections:** CDE systems must not communicate directly with Internet
- **Unencrypted Protocols:** Telnet, FTP, HTTP (except redirect to HTTPS)
- **Deprecated Protocols:** SSLv2, SSLv3, TLS 1.0, TLS 1.1
- **Undocumented Rules:** All rules must be documented

## 6. Change Management

### 6.1 Emergency Changes

**Emergency changes allowed for:**
- Active security incidents
- Critical system failures
- Immediate threats

**Process:**
1. Verbal approval by CISO
2. Immediate implementation
3. Retrospective documentation (within 24h)
4. Formal approval (within 48h)

### 6.2 Change History

| Date | Rule ID | Change | Justification | Approved By |
|------|---------|--------|---------------|-------------|
| [TODO: 2026-01-15] | FW-105 | New rule | Payment API | [TODO: CISO] |
| [TODO: 2026-02-01] | FW-042 | Removed | No longer needed | [TODO: CISO] |

## 7. Monitoring and Alerting

### 7.1 Firewall Logging

**Logging Requirements:**
- All blocked connections
- All allowed connections to/from CDE
- Firewall configuration changes
- Firewall system events (start, stop, errors)

**Log Retention:** [TODO: 90 days online, 1 year archive]  
**Log Forwarding:** [TODO: SIEM system]  

### 7.2 Alerting Rules

| Alert | Condition | Severity | Notification |
|-------|-----------|----------|--------------|
| Unauthorized CDE access | Blocked connection to CDE | High | SOC + IT Security |
| Firewall rule change | Configuration change | Medium | Network Team |
| Firewall failure | Firewall unreachable | Critical | SOC + CISO |

## 8. Compliance Validation

### 8.1 Validation Activities

**Quarterly:**
- Firewall rule review
- Documentation validation
- Unused rule cleanup

**Annual:**
- Penetration test of firewall configuration
- Segmentation validation
- Compliance audit

### 8.2 Validation Documentation

**Required Evidence:**
- Firewall configuration files
- Rule review logs
- Change logs
- Approval records

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial creation |

<!-- End of template -->
