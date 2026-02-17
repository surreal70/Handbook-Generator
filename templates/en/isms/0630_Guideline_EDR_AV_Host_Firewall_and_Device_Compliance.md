# Guideline: EDR, Antivirus, Host Firewall and Device Compliance

**Document-ID:** [FRAMEWORK]-0630
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Approved by:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Classification:** {{ meta-handbook.classification }}
**Last Update:** {{ meta-handbook.modifydate }}

---

---

## 1. Purpose and Scope

This guideline implements `0620_Policy_Endpoint_Security.md` and defines:
- Endpoint Detection and Response (EDR) requirements
- Antivirus configuration and management
- Host firewall policies
- Device compliance requirements

**Scope:** All endpoints at **{{ meta-organisation.name }}**

## 2. Endpoint Detection and Response (EDR)

### 2.1 EDR System

**Platform:** {{ meta.security.edr_solution }} (e.g., CrowdStrike, SentinelOne, Microsoft Defender for Endpoint)

**Functions:**
- Real-time Threat Detection
- Behavioral Analysis
- Automated Response
- Forensic Capabilities
- Threat Hunting

### 2.2 EDR Deployment

**Mandatory Installation:**
- All workstations (Windows, macOS, Linux)
- All servers
- No exceptions (except via exception process)

**Deployment Methods:**
- Group Policy (Windows)
- MDM (macOS, Mobile)
- Configuration Management (Linux)

### 2.3 EDR Policies

**Detection Modes:**
- **Prevent:** Automatic blocking (default)
- **Detect:** Alerting only (for legacy systems)

**Behavioral Policies:**
- Ransomware Protection
- Credential Theft Protection
- Exploit Protection
- Script Control (PowerShell, CMD)

### 2.4 EDR Response

**Automated Actions:**
- Malware Quarantine
- Process Termination
- Network Isolation (for critical threats)

**Manual Actions:**
- Remote Shell for forensics
- File Retrieval
- Memory Dump

### 2.5 Tamper Protection

**Protection Against Deactivation:**
- EDR agent cannot be disabled (without admin password)
- Uninstall password required
- Alerts on tamper attempts

## 3. Antivirus (AV)

### 3.1 AV System

**Platform:** {{ meta.security.av_solution }} (often integrated in EDR)

**Scan Types:**
- Real-time Scanning (On-Access)
- Scheduled Full Scans (weekly)
- Quick Scans (daily)

### 3.2 AV Configuration

**Scan Settings:**
- Scan all file types
- Scan archives
- Scan email attachments
- Scan removable media

**Exclusions:**
- Only after approval by IT Security
- Documentation required
- Regular review (quarterly)

### 3.3 Signature Updates

**Automatic Updates:**
- Multiple times daily
- Via internal update servers (WSUS, etc.)
- Fallback to cloud updates

**Monitoring:**
- Alerts for outdated signatures (> 7 days)

### 3.4 Malware Handling

**Upon Malware Detection:**
1. Automatic quarantine
2. Alert to security team
3. Create incident ticket
4. Forensic analysis (if needed)
5. Remediation
6. Lessons learned

## 4. Host Firewall

### 4.1 Windows Firewall

**Configuration via GPO:**
- Firewall enabled (all profiles: Domain, Private, Public)
- Inbound: Default Deny
- Outbound: Default Allow (with exceptions)

**Allowed Inbound Connections:**
- Remote Desktop (only from management VLAN)
- File Sharing (only in corporate network)
- Monitoring Agents

### 4.2 macOS Firewall

**Configuration via MDM:**
- Application Firewall enabled
- Stealth Mode enabled
- Only signed apps allowed

### 4.3 Linux Firewall

**iptables/firewalld:**
- Default Deny for inbound
- Only required services allowed
- Logging enabled

## 5. Device Compliance

### 5.1 Compliance Requirements

**Mandatory Requirements:**
- EDR/AV installed and active
- OS patches current (< 30 days old)
- Disk encryption enabled
- Host firewall enabled
- Screen lock configured (max. 15 minutes)
- No jailbreak/root (mobile)

### 5.2 Compliance Checks

**Automatic Verification:**
- At every network access (NAC)
- At VPN connection
- Daily (endpoint management)

**Upon Non-Compliance:**
- Warning to user (24-hour grace period)
- Restricted network access
- Complete blocking after 7 days

### 5.3 Compliance Reporting

**Weekly Report:**
- Compliance rate per department
- Top non-compliance items
- Trend analysis

**Target:** > 95% compliance

## 6. Patch Management

### 6.1 OS Patches

**Windows:**
- WSUS for patch distribution
- Automatic installation (outside business hours)
- Reboot window: Weekend

**macOS:**
- Automatic updates via MDM
- Deferred updates (7-day test period)

**Linux:**
- Automatic security updates (unattended-upgrades)
- Manual updates for kernel

### 6.2 Application Patches

**Third-Party Applications:**
- Ninite, Chocolatey for automatic updates
- Manual updates for critical apps

**Patch SLA:**
- Critical: 7 days
- High: 30 days
- Medium: 90 days

**Details:** See `0350_Guideline_Vulnerability_Scans_Patching`

## 7. Application Control

### 7.1 Application Whitelisting

**For Critical Systems:**
- Only signed, approved applications
- Blocking of unapproved software
- Exceptions via ticketing system

**Tools:**
- Windows Defender Application Control (WDAC)
- AppLocker

### 7.2 Script Control

**PowerShell:**
- Constrained Language Mode
- Script signing required
- Logging enabled

**CMD/Batch:**
- Blocked for standard users
- Only for admins

## 8. USB and Removable Media

### 8.1 USB Control

**Policies:**
- USB storage blocked (standard users)
- Only approved USB devices (whitelist)
- Automatic scanning upon connection

**Exceptions:**
- Request via ticketing system
- Time-limited
- Encrypted USB drives

### 8.2 DLP for Removable Media

**Data Loss Prevention:**
- Blocking of confidential data on USB
- Alerts on copy attempts
- Logging of all USB activities

## 9. Monitoring and Alerting

### 9.1 Endpoint Monitoring

**Monitored Metrics:**
- EDR/AV status
- Patch level
- Compliance status
- Malware detections
- Anomalies (CPU, network)

### 9.2 SIEM Integration

**Events to SIEM:**
- Malware detections
- EDR alerts
- Compliance violations
- Tamper attempts

### 9.3 Automated Response

**SOAR Integration:**
- Automatic isolation upon malware
- Automatic ticket creation
- Automatic notifications

## 10. Compliance and Audit

### 10.1 Metrics (KPIs)

| Metric | Target Value |
|--------|--------------|
| EDR Deployment Rate | 100% |
| AV Signature Currency | 100% |
| Device Compliance Rate | > 95% |
| Malware Detection Rate | Baseline |
| Patch Compliance (30 days) | > 90% |

### 10.2 Audit Evidence

- EDR Deployment Status
- Compliance Reports
- Malware Incident Reports
- Patch Compliance Reports

## 11. References

### Internal Documents
- `0620_Policy_Endpoint_Security.md`
- `0350_Guideline_Vulnerability_Scans_Patching_and_Exploitation_Response.md`

### External Standards
- **ISO/IEC 27001:2022 Annex A.8.7** - Protection against malware
- **NIST SP 800-83** - Guide to Malware Incident Prevention and Handling
- **CIS Controls** - Malware Defenses

**Approved by:** {{ meta.ciso.name }}, CISO  
**Next Review:** {{ meta-handbook.next_review }}

