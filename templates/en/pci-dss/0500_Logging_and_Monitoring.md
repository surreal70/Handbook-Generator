# Logging and Monitoring

**Document-ID:** [FRAMEWORK]-0500
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

<!-- 
TEMPLATE AUTHOR NOTE:
This template documents logging and monitoring requirements.
It aligns with PCI-DSS v4.0 Requirement 10 (Log and Monitor All Access to System Components and Cardholder Data).

Customization required:
- Define logging requirements
- Document SIEM configuration
- Include log retention policies
- Define monitoring and alerting rules
-->

## 1. Purpose

This document defines the logging and monitoring requirements for {{ meta-organisation.name }} in accordance with PCI-DSS Requirement 10.

### 1.1 Objectives

- **Traceability:** Log all access to CDE and CHD
- **Anomaly Detection:** Identify suspicious activities
- **Incident Response:** Enable forensic investigations
- **Compliance:** Fulfillment of PCI-DSS Requirement 10

### 1.2 Scope

**Affected Systems:**
- All CDE systems
- Systems with CHD access
- Network components
- Security systems

## 2. Logging Requirements

### 2.1 Events to Log

**User Access:**
- All logins (successful and failed)
- All logouts
- Privileged actions
- Access to CHD
- Permission changes

**System Events:**
- System starts and stops
- Configuration changes
- Software installations
- Patch installations
- Service starts and stops

**Network Events:**
- Firewall rule changes
- Blocked connections
- VPN connections
- IDS/IPS alerts

**Security Events:**
- Antivirus detections
- Security policy violations
- Account lockouts
- Password changes

**Database Events:**
- All access to CHD tables
- Schema changes
- Privileged database operations
- Failed access attempts

### 2.2 Log Entry Format

**Required Fields:**
- **User ID:** Who performed the action?
- **Event Type:** What happened?
- **Timestamp:** When did it happen? (synchronized time)
- **Success/Failure:** Was the action successful?
- **Source:** Where did the action come from? (IP address, hostname)
- **Target:** Which system/resource was affected?
- **Additional Details:** Relevant context information

**Example:**
```
2026-02-06 14:32:15 UTC | USER=john.doe | EVENT=LOGIN_SUCCESS | SOURCE=10.1.100.50 | TARGET=payment-gateway-01 | DETAILS=MFA_VERIFIED
```

## 3. SIEM System

### 3.1 SIEM Implementation

**SIEM System:** [TODO: Name of SIEM system]

**Functions:**
- Central log collection
- Real-time analysis
- Event correlation
- Alerting
- Reporting
- Forensic search

**Architecture:**
- Log sources → Log forwarder → SIEM
- Encrypted transmission (TLS 1.2+)
- Redundant SIEM servers
- Secure log storage

### 3.2 Log Forwarding

**Configuration:**
- All CDE systems send logs to SIEM
- Real-time transmission (< 5 minutes delay)
- Encrypted transmission
- Authentication of log sources

**Log Forwarders:**
- Syslog (RFC 5424)
- Windows Event Forwarding
- Agent-based (e.g., Splunk Forwarder, Elastic Beats)

### 3.3 Log Parsing and Normalization

**Requirements:**
- Uniform log format
- Parsing of all relevant fields
- Normalization of timestamps
- Enrichment with context (e.g., Geo-IP)

## 4. Log Retention

### 4.1 Retention Periods

**Online Storage:**
- 90 days in SIEM (fast access)
- Full-text search possible
- Real-time analysis

**Archive Storage:**
- 1 year in archive
- Compressed
- Encrypted
- WORM storage (Write Once Read Many)

**Long-term Archiving:**
- According to legal requirements
- Secure storage
- Documentation

### 4.2 Log Backup

**Requirements:**
- Daily log backups
- Offsite storage
- Encrypted backups
- Regular restore tests

## 5. Log Integrity

### 5.1 Protection Against Tampering

**Measures:**
- WORM storage for logs
- Digital signatures
- Hash values for log files
- Access control to logs
- Logging of log access

**Validation:**
- Regular integrity checks
- Automatic alerts on tampering
- Forensic investigation on suspicion

### 5.2 Log Access Control

**Permissions:**
- Only authorized personnel
- Read-only access for most users
- Full access only for log administrators
- Logging of all log access

**Roles:**
- Log Administrator: Full access
- Security Analyst: Read access, search, alerting
- Auditor: Read access
- Standard User: No access

## 6. Time Synchronization

### 6.1 NTP Configuration

**Requirements:**
- All systems synchronized with NTP
- Internal NTP servers
- External NTP sources (Stratum 1 or 2)
- Redundant NTP servers

**NTP Servers:**
- Primary: [TODO: IP address]
- Secondary: [TODO: IP address]
- External source: [TODO: e.g., time.nist.gov]

**Time Zone:**
- UTC for all logs
- Local time zone for display (with UTC offset)

### 6.2 Time Drift Monitoring

**Monitoring:**
- Maximum drift: 1 second
- Alerts on drift > 1 second
- Automatic correction
- Logging of time changes

## 7. Monitoring and Alerting

### 7.1 Security Monitoring

**24/7 Monitoring:**
- Security Operations Center (SOC)
- Real-time monitoring of all alerts
- Incident response on critical alerts
- Escalation by severity

**SOC Team:**
- SOC Analyst (Tier 1)
- Senior SOC Analyst (Tier 2)
- Security Engineer (Tier 3)
- CISO (Escalation)

### 7.2 Alerting Rules

**Critical Alerts:**

| Alert | Condition | Action | Escalation |
|-------|-----------|--------|------------|
| Multiple failed logins | >10 in 5 min | Immediate investigation | SOC → CISO |
| Unauthorized CDE access | Blocked connection to CDE | Immediate investigation | SOC → IT Security |
| Malware detection | Antivirus alert | System isolation | SOC → IT Security |
| Data exfiltration | Large data transfer | Block connection | SOC → CISO |
| Privileged action | Root/Admin action | Logging, review | SOC |
| Firewall rule change | Configuration change | Validation | SOC → Network Team |

**High Alerts:**
- Admin login outside business hours
- Access to CHD
- Configuration changes
- New software installation

**Medium Alerts:**
- Failed authentication
- Password change
- Account lockout

**Low Alerts:**
- Informational events
- Routine activities

### 7.3 Alert Response

**Process:**
1. Receive alert
2. Assess severity
3. Initial investigation
4. Escalation (if required)
5. Incident response (if required)
6. Documentation
7. Follow-up

**Response Times:**
- Critical: Immediate (< 15 minutes)
- High: < 1 hour
- Medium: < 4 hours
- Low: < 24 hours

## 8. Log Review

### 8.1 Daily Log Review

**Process:**
- Automated analysis by SIEM
- Review critical alerts
- Identify anomalies
- Document findings

**Responsible:** SOC Team

### 8.2 Weekly Log Review

**Process:**
- Review all alerts of the week
- Trend analysis
- Identify patterns
- Optimize alerting rules

**Responsible:** Senior SOC Analyst

### 8.3 Monthly Log Review

**Process:**
- Comprehensive analysis of all logs
- Compliance validation
- Reporting to management
- Identify improvements

**Responsible:** IT Security Manager

## 9. Use Cases and Correlation Rules

### 9.1 Defined Use Cases

**Authentication:**
- Brute-force attacks
- Credential stuffing
- Unusual login times
- Geographic anomalies

**Access Control:**
- Unauthorized access
- Privilege escalation
- Lateral movement

**Data Exfiltration:**
- Large data transfers
- Unusual data access
- Access to many records

**Malware:**
- Antivirus detections
- Suspicious processes
- Command & Control communication

**Insider Threats:**
- Unusual user activities
- Access outside working hours
- Mass downloads

### 9.2 Correlation Rules

**Example Rule: Brute-Force Attack**
```
IF (failed_logins > 10 IN 5 minutes)
AND (same_source_ip)
THEN
  ALERT "Brute-force attack detected"
  SEVERITY = CRITICAL
  ACTION = Block_IP
```

**Example Rule: Privilege Escalation**
```
IF (user_receives_admin_rights)
AND (user_performs_privileged_action IN 10 minutes)
THEN
  ALERT "Possible privilege escalation"
  SEVERITY = HIGH
  ACTION = Investigate
```

## 10. Audit Trails

### 10.1 Audit Trail Requirements

**For All CHD Access:**
- Complete audit trails
- Immutable
- Traceable
- Chronologically ordered

**Information:**
- Who accessed?
- When was access?
- Which data was accessed?
- Which action was performed?
- Was the action successful?

### 10.2 Audit Trail Review

**Process:**
- Regular review (daily for critical systems)
- Identify anomalies
- Document findings
- Follow-up on anomalies

## 11. Forensic Investigations

### 11.1 Log Analysis for Forensics

**Process:**
1. Incident identified
2. Collect relevant logs
3. Create timeline
4. Root cause analysis
5. Documentation
6. Lessons learned

**Tools:**
- SIEM forensic functions
- Log analysis tools
- Timeline analysis tools

### 11.2 Chain of Custody

**Requirements:**
- Document all log access
- Immutability of logs
- Traceable chain of evidence
- Legally sound documentation

## 12. Compliance Validation

### 12.1 Validation Activities

**Daily:**
- Log review
- Alert response
- Anomaly detection

**Weekly:**
- Trend analysis
- Use case validation

**Monthly:**
- Comprehensive log review
- Compliance reporting

**Quarterly:**
- Log retention validation
- SIEM configuration review

**Annually:**
- Complete logging audit
- Penetration testing
- Compliance assessment

### 12.2 Validation Documentation

**Required Evidence:**
- Logging configuration
- SIEM configuration
- Log review protocols
- Alert response protocols
- Forensic investigation reports

<!-- End of template -->
