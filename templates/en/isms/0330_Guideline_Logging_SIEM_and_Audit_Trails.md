# Guideline: Logging, SIEM and Audit Trails

**Document ID:** 0330  
**Document Type:** Guideline (detailed)  
**Related Policy:** 0320_Policy_Logging_and_Monitoring.md  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.8.15, A.8.16  
**Owner:** {{ meta.it_operations.manager }}  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Confidential  
**Last Updated:** {{ meta.document.date }}

---

## 1. Purpose and Scope

This guideline implements the `0320_Policy_Logging_and_Monitoring.md` and defines:
- Logging requirements per system type
- SIEM integration and use cases
- Audit trail requirements and retention

**Scope:** All IT systems at **{{ meta.organization.name }}**

## 2. Logging Requirements

### 2.1 Events to be Logged

**Authentication:**
- Successful and failed logins
- Logout events
- MFA challenges and results
- Password changes and resets
- Account lockouts and unlocks

**Authorization:**
- Access to confidential data
- Privileged operations (sudo, admin rights)
- Access denials
- Permission changes

**System Events:**
- System start and shutdown
- Service starts and stops
- Configuration changes
- Software installations and updates
- Errors and exceptions

**Data Events:**
- File access (read, write, delete)
- Database queries (for sensitive data)
- Data exports and downloads
- Backup operations

**Network Events:**
- Firewall blocks and allows
- VPN connections
- Network scans
- Traffic anomalies

### 2.2 Log Format and Content

**Mandatory Fields:**
- Timestamp (UTC, ISO 8601)
- Event type and severity
- Source (system, application, IP)
- User/account
- Action/operation
- Result (success/failure)
- Additional context information

**Example (JSON):**
```json
{
  "timestamp": "2024-02-02T10:15:30Z",
  "event_type": "authentication",
  "severity": "info",
  "source_ip": "192.168.1.100",
  "user": "jdoe",
  "action": "login",
  "result": "success",
  "mfa_method": "authenticator_app"
}
```

### 2.3 Logging Levels

| System Type | Logging Level | Rationale |
|-------------|---------------|-----------|
| Production systems | INFO | Balance between detail and performance |
| Development systems | DEBUG | Troubleshooting |
| Security systems (firewall, IDS) | VERBOSE | Maximum visibility |
| Privileged systems | VERBOSE | Compliance and forensics |

## 3. SIEM Integration

### 3.1 SIEM System

**Platform:** {{ meta.security.siem_solution }} (e.g., Splunk, Microsoft Sentinel, Elastic SIEM)

**Architecture:**
- Log collection via agents or syslog
- Central log aggregation
- Normalization and enrichment
- Correlation and alerting
- Long-term archiving

### 3.2 Log Sources

**Priority 1 (Critical):**
- Active Directory / Azure AD
- Firewalls and IDS/IPS
- VPN gateways
- Privileged Access Management (PAM)
- Databases with confidential data

**Priority 2 (High):**
- Web servers and application servers
- Email gateways
- Cloud services (Azure, AWS, Google Cloud)
- Endpoint Detection and Response (EDR)

**Priority 3 (Medium):**
- Workstations and laptops
- Network switches
- Printers and IoT devices

### 3.3 SIEM Use Cases

**Authentication:**
- Brute-force attacks (> 10 failed logins in 5 minutes)
- Impossible travel (logins from geographically impossible locations)
- Privileged account usage outside business hours

**Malware and Intrusion:**
- Malware detections by EDR
- IDS/IPS alerts
- Command & Control (C2) communication
- Lateral movement (unusual internal connections)

**Data Exfiltration:**
- Large data volume uploads to external destinations
- Access to many confidential files in short time
- Unusual database queries

**Compliance:**
- Access to PII (Personally Identifiable Information)
- Changes to security configurations
- Privileged operations without approval

### 3.4 Alerting and Response

**Severity Levels:**
- **Critical:** Immediate escalation to on-call security (24/7)
- **High:** Escalation within 1 hour
- **Medium:** Processing within 4 hours
- **Low:** Processing within 1 business day

**Automated Response:**
- Account lockout on brute-force
- IP blocking on malware C2
- Endpoint quarantine on malware detection

## 4. Audit Trails

### 4.1 Requirements

**Immutability:**
- Logs must not be modified retroactively
- Cryptographic signatures or write-once storage
- Access to logs only for authorized personnel

**Completeness:**
- Continuous recording of all relevant events
- Monitoring of log integrity
- Alerts on log failures

**Traceability:**
- Who did what when?
- Reconstruction of event chains
- Forensic analysis possible

### 4.2 Privileged Access

**Additional Requirements:**
- Session recording for privileged access
- Four-eyes principle for critical operations
- Approval workflow before access
- Detailed logging of all actions

**PAM Integration:**
- Privileged Access Management System: {{ meta.security.pam_solution }}
- Just-in-Time (JIT) access
- Automatic password rotation
- Session monitoring and recording

### 4.3 Compliance Audit Trails

**Regulatory Requirements:**
- GDPR: Access to personal data
- SOX: Financially relevant transactions
- HIPAA: Access to health data (if applicable)

**Documentation:**
- Who accessed which data?
- Purpose of access
- Approval (if required)
- Time period

## 5. Log Retention

### 5.1 Retention Periods

| Log Type | Retention (Online) | Retention (Archive) | Rationale |
|----------|--------------------|--------------------|-----------|
| Security logs | 90 days | {{ meta.retention.log_years }} years | Forensics, compliance |
| Authentication logs | 90 days | {{ meta.retention.log_years }} years | Audit, compliance |
| System logs | 30 days | 1 year | Troubleshooting |
| Application logs | 30 days | 1 year | Debugging |
| Audit trails (compliance) | 180 days | {{ meta.retention.audit_years }} years | Regulatory |

### 5.2 Archiving

**Process:**
1. Logs older than retention period (online) are archived
2. Compression and encryption
3. Transfer to archive storage (e.g., Azure Blob Archive, AWS Glacier)
4. Verification of archiving
5. Deletion from online SIEM

**Archive Access:**
- Only with justified need (forensics, audit)
- Approval by CISO
- Restoration to SIEM for analysis

### 5.3 Secure Deletion

**After Retention Expiry:**
- Automatic deletion from archive
- Cryptographic deletion (destroy keys)
- Documentation of deletion

## 6. Log Security

### 6.1 Access Control

**Permissions:**
- **Security Team:** Full access to all logs
- **IT Operations:** Access to system and application logs
- **Auditors:** Read-only access to audit trails
- **Developers:** Access only to dev logs

**Authentication:**
- MFA for SIEM access
- Privileged accounts for admin operations
- Audit logging for SIEM access

### 6.2 Encryption

**In Transit:**
- TLS 1.2+ for log transmission
- Mutual TLS for critical systems

**At Rest:**
- Encryption of SIEM storage (AES-256)
- Encryption of archive logs

### 6.3 Integrity Protection

**Methods:**
- Cryptographic signatures (HMAC)
- Write-Once-Read-Many (WORM) storage
- Blockchain-based log integrity (optional)

**Monitoring:**
- Regular integrity checks
- Alerts on tampering attempts

## 7. Monitoring and Alerting

### 7.1 Log Health Monitoring

**Monitored Metrics:**
- Log ingestion rate (logs per second)
- Log latency (time until log in SIEM)
- Missing log sources
- SIEM storage capacity

**Alerts:**
- Log source not sending logs (> 15 minutes)
- Unusually high log rate (possible attack or error)
- SIEM storage > 80% full

### 7.2 Security Monitoring

**24/7 Security Operations Center (SOC):**
- Monitoring of all SIEM alerts
- Triage and incident response
- Escalation for critical incidents

**Automation:**
- SOAR (Security Orchestration, Automation and Response)
- Automated playbooks for common incidents
- Integration with ticketing system

## 8. Compliance and Audit

### 8.1 Key Performance Indicators (KPIs)

| Metric | Target Value |
|--------|--------------|
| Log source availability | > 99% |
| SIEM alert response time (critical) | < 15 minutes |
| False positive rate | < 10% |
| Log retention compliance | 100% |

### 8.2 Audit Evidence

- SIEM configuration and use cases
- Log retention reports
- Incident response documentation
- SIEM access logs

## 9. References

### Internal Documents
- `0320_Policy_Logging_and_Monitoring.md`
- `0400_Policy_Incident_Management.md`

### External Standards
- **ISO/IEC 27001:2022 Annex A.8.15** - Logging
- **ISO/IEC 27001:2022 Annex A.8.16** - Monitoring activities
- **NIST SP 800-92** - Guide to Computer Security Log Management

---

**Approved by:** {{ meta.ciso.name }}, CISO  
**Next Review:** {{ meta.document.next_review }}
