# Log Management and Audit

**Document-ID:** [FRAMEWORK]-0190
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

## Purpose and Scope

This document describes the log management and audit processes for {{ meta-organisation.name }}. It defines log collection, aggregation, retention, audit trail requirements, and SIEM integration to ensure traceability, compliance, and security monitoring.

**Scope:** All IT systems, networks, applications, and security components of {{ meta-organisation.name }}

**Responsible:** {{ meta-organisation-roles.role_ciso.name }} ({{ meta-organisation-roles.role_ciso.email }})

## Log Management Fundamentals

### Objectives

**Primary Objectives:**
- **Security Monitoring:** Detection of security incidents
- **Compliance:** Meeting regulatory requirements
- **Troubleshooting:** Error analysis and problem resolution
- **Forensics:** Traceability of events
- **Audit:** Evidence of controls and processes
- **Performance Analysis:** System and application performance

### Log Types

#### System Logs

**Description:** Operating system events

**Examples:**
- Windows Event Logs (Security, System, Application)
- Linux Syslog (/var/log/messages, /var/log/auth.log)
- Boot logs, Kernel logs

**Important Events:**
- System start/stop
- Service start/stop
- Errors and warnings
- Hardware events

#### Security Logs

**Description:** Security-relevant events

**Examples:**
- Authentication events (Login, Logout, Failed Login)
- Authorization events (Access denial)
- Privilege changes
- Security policy changes
- Firewall logs
- IDS/IPS alerts

**Important Events:**
- Failed login attempts
- Privilege escalation
- Account changes
- Security policy changes

#### Application Logs

**Description:** Application-specific events

**Examples:**
- Web server logs (Apache, Nginx, IIS)
- Database logs (MySQL, PostgreSQL, SQL Server)
- Application logs (Custom apps)
- Middleware logs (Tomcat, JBoss)

**Important Events:**
- Application errors
- Transaction logs
- Performance metrics
- User activities

#### Network Logs

**Description:** Network events

**Examples:**
- Firewall logs
- Router/Switch logs
- VPN logs
- DNS logs
- DHCP logs
- Proxy logs

**Important Events:**
- Connection attempts (allowed/blocked)
- Network changes
- Bandwidth usage
- Anomalies

#### Audit Logs

**Description:** Compliance and audit-relevant events

**Examples:**
- Data access
- Configuration changes
- Administrative activities
- Privileged access

**Important Events:**
- Who did what when?
- Changes to critical systems
- Access to sensitive data

### Log Levels

| Level | Description | Usage | Example |
|---|---|---|---|
| **EMERGENCY** | System unusable | Critical system errors | Kernel Panic |
| **ALERT** | Immediate action required | Critical errors | Database unreachable |
| **CRITICAL** | Critical conditions | Severe errors | Disk full |
| **ERROR** | Error conditions | Errors | Application error |
| **WARNING** | Warning conditions | Warnings | Disk 80% full |
| **NOTICE** | Normal but significant condition | Important events | Service started |
| **INFO** | Informational messages | Normal events | User login |
| **DEBUG** | Debug messages | Development | Function calls |

## Log Collection and Aggregation

### Log Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    Log Sources                          │
│  Servers, Network, Applications, Security Devices       │
└────────────────────┬────────────────────────────────────┘
                     │
                     │ Syslog, Agents, APIs
                     │
┌────────────────────▼────────────────────────────────────┐
│              Log Collectors/Forwarders                   │
│  Rsyslog, Fluentd, Logstash, Splunk Forwarders         │
└────────────────────┬────────────────────────────────────┘
                     │
                     │ Parsing, Filtering, Enrichment
                     │
┌────────────────────▼────────────────────────────────────┐
│              Log Aggregation Platform                    │
│  SIEM, ELK Stack, Splunk, Graylog                       │
└────────────────────┬────────────────────────────────────┘
                     │
         ┌───────────┴───────────┐
         │                       │
┌────────▼────────┐    ┌────────▼────────────────────────┐
│ Hot Storage     │    │ Cold Storage / Archive          │
│ (Fast Access)   │    │ (Long-term Retention)           │
└─────────────────┘    └─────────────────────────────────┘
```

### Log Collection Methods

#### Syslog

**Protocol:** RFC 5424 (Syslog Protocol)  
**Transport:** UDP 514 (Standard), TCP 514 (Reliable), TLS 6514 (Secure)

**Advantages:**
- Standard protocol
- Widely adopted
- Simple configuration

**Disadvantages:**
- UDP not reliable
- Limited structure
- No authentication (without TLS)

**Usage:** Linux/Unix systems, Network devices

#### Agent-based

**Agents:**
- Splunk Universal Forwarder
- Elastic Beats (Filebeat, Metricbeat)
- Fluentd
- NXLog

**Advantages:**
- Reliable transmission
- Local buffering
- Parsing and filtering
- Encrypted transmission

**Disadvantages:**
- Agent installation required
- Agent management
- Resource consumption

**Usage:** Servers, Workstations

#### API-based

**Methods:**
- REST APIs
- Cloud provider APIs (AWS CloudWatch, Azure Monitor)
- Webhook integration

**Advantages:**
- Structured data
- Real-time integration
- No agent installation

**Disadvantages:**
- API limits
- Network dependency
- More complex configuration

**Usage:** Cloud services, SaaS applications

#### Windows Event Forwarding (WEF)

**Method:** Windows-native event forwarding

**Advantages:**
- No additional agents
- Central configuration via GPO
- Reliable

**Disadvantages:**
- Windows only
- Limited parsing options

**Usage:** Windows environments

### Log Aggregation Platform

**SIEM System:** {{ meta-handbook.siem_system }}  
**Version:** [TODO]  
**Management URL:** {{ meta-handbook.siem_url }}

**Components:**
- **Log Collectors:** {{ meta-handbook.log_collectors }}
- **Indexers:** {{ meta-handbook.log_indexers }}
- **Search Heads:** {{ meta-handbook.log_search_heads }}
- **Storage:** {{ meta-handbook.log_storage }}

**Capacity:**
- **Ingestion Rate:** {{ meta-handbook.log_ingestion_rate }} GB/day
- **Storage Capacity:** {{ meta-handbook.log_storage_capacity }} TB
- **Retention (Hot):** {{ meta-handbook.log_retention_hot }} days
- **Retention (Cold):** {{ meta-handbook.log_retention_cold }} days

### Log Source Configuration

#### Linux Servers

**Rsyslog Configuration:**
```bash
# /etc/rsyslog.d/50-remote.conf

# Send all logs to central syslog server
*.* @@syslog.{{ meta-organisation.domain }}:514

# Send only security logs
authpriv.* @@syslog.{{ meta-organisation.domain }}:514

# TLS encrypted
$DefaultNetstreamDriver gtls
$ActionSendStreamDriverMode 1
$ActionSendStreamDriverAuthMode x509/name
*.* @@syslog.{{ meta-organisation.domain }}:6514
```

#### Windows Servers

**Event Forwarding Configuration:**
```powershell
# Enable event forwarding
wecutil qc

# Create subscription
wecutil cs subscription.xml

# Subscription XML
<Subscription>
  <SubscriptionId>Security-Events</SubscriptionId>
  <DestinationUrl>http://wec-server.{{ meta-organisation.domain }}:5985/wsman</DestinationUrl>
  <Query>
    <QueryList>
      <Query Id="0">
        <Select Path="Security">*[System[(EventID=4624 or EventID=4625)]]</Select>
      </Query>
    </QueryList>
  </Query>
</Subscription>
```

#### Firewall

**Syslog Configuration:**
- Syslog Server: {{ netbox.syslog.server }}
- Facility: Local6
- Severity: Informational and higher
- Format: RFC 5424

**Logged Events:**
- All allowed/blocked connections
- Policy changes
- VPN connections
- Admin access

#### Web Server (Apache)

**Log Configuration:**
```apache
# /etc/apache2/sites-available/default-ssl.conf

# Access Log
CustomLog /var/log/apache2/access.log combined

# Error Log
ErrorLog /var/log/apache2/error.log
LogLevel warn

# Forwarding to Syslog
CustomLog "|/usr/bin/logger -t apache -p local6.info" combined
```

#### Database (MySQL)

**Log Configuration:**
```ini
# /etc/mysql/my.cnf

[mysqld]
# General Query Log (for debugging only)
general_log = 0
general_log_file = /var/log/mysql/query.log

# Error Log
log_error = /var/log/mysql/error.log

# Slow Query Log
slow_query_log = 1
slow_query_log_file = /var/log/mysql/slow.log
long_query_time = 2

# Audit Plugin (for compliance)
plugin-load = audit_log.so
audit_log_file = /var/log/mysql/audit.log
audit_log_format = JSON
```

## Log Retention and Archiving

### Retention Policies

#### Retention by Log Type

| Log Type | Hot Storage | Cold Storage | Total | Rationale |
|---|---|---|---|---|
| **Security Logs** | 90 days | 7 years | 7 years | Compliance, Forensics |
| **Audit Logs** | 90 days | 7 years | 7 years | Compliance, Regulation |
| **System Logs** | 30 days | 1 year | 1 year | Troubleshooting |
| **Application Logs** | 30 days | 1 year | 1 year | Troubleshooting |
| **Network Logs** | 30 days | 1 year | 1 year | Security, Troubleshooting |
| **Web Access Logs** | 30 days | 6 months | 6 months | Analytics, Security |
| **Debug Logs** | 7 days | - | 7 days | Development |

#### Retention by Compliance

**GDPR:**
- Personal data: Only as long as necessary
- Access logs: 6 months (recommended)
- Security logs: 1-2 years

**ISO 27001:**
- Security logs: At least 1 year
- Audit logs: At least 1 year

**Industry-specific:**
- Financial sector: 7-10 years
- Healthcare: 10 years
- Telecommunications: 6 months (data retention)

### Storage Tiers

#### Hot Storage (Fast Access)

**Technology:** SSD, NVMe  
**Retention:** 30-90 days  
**Access:** Real-time search, Dashboards  
**Cost:** High

**Usage:**
- Active monitoring
- Security analysis
- Troubleshooting

#### Warm Storage (Medium Access)

**Technology:** HDD, Object Storage  
**Retention:** 3-12 months  
**Access:** Search (slower)  
**Cost:** Medium

**Usage:**
- Historical analysis
- Compliance audits
- Forensics

#### Cold Storage (Archive)

**Technology:** Tape, Cloud Glacier, Object Storage  
**Retention:** 1-7 years  
**Access:** Restore required (hours to days)  
**Cost:** Low

**Usage:**
- Long-term archiving
- Compliance requirements
- Legal retention

### Archiving Process

**Automatic Archiving:**
1. Logs older than hot retention are compressed
2. Compressed logs are moved to warm/cold storage
3. Metadata remains available for search
4. Originals are deleted from hot storage

**Archive Format:**
- Compression: gzip, bzip2
- Encryption: AES-256
- Integrity: SHA-256 checksums
- Metadata: JSON index

**Archive Location:** {{ meta-handbook.log_archive_location }}

### Log Deletion

**Automatic Deletion:**
- Logs older than retention policy are automatically deleted
- Deletion is logged (audit trail)
- Verify checksums before deletion

**Manual Deletion:**
- Only with management approval
- Document justification
- Create deletion protocol

**GDPR Deletion:**
- Right to be forgotten
- Delete personal data
- Document deletion

## Log Analysis and Monitoring

### SIEM Integration

**SIEM System:** {{ meta-handbook.siem_system }}

**Functions:**
- **Real-time Monitoring:** Real-time monitoring
- **Correlation:** Event correlation
- **Alerting:** Automatic alerts
- **Dashboards:** Visualization
- **Reporting:** Compliance reports
- **Threat Intelligence:** Integration of threat feeds

### Use Cases and Correlation Rules

#### Failed Login Attempts

**Use Case:** Detection of brute-force attacks

**Rule:**
```
IF failed_login_count > 5 
   AND time_window = 5 minutes
   AND same_source_ip
THEN alert "Possible Brute-Force Attack"
```

**Severity:** High  
**Response:** Temporarily lock account, block IP

#### Privilege Escalation

**Use Case:** Detection of unauthorized privilege changes

**Rule:**
```
IF event_type = "privilege_change"
   AND new_privilege = "admin"
   AND user NOT IN admin_group
THEN alert "Unauthorized Privilege Escalation"
```

**Severity:** Critical  
**Response:** Immediate investigation, deactivate account

#### Data Exfiltration

**Use Case:** Detection of unusual data transfers

**Rule:**
```
IF data_transfer_size > 1GB
   AND destination = external
   AND time = outside_business_hours
THEN alert "Possible Data Exfiltration"
```

**Severity:** Critical  
**Response:** Block connection, start forensics

#### Malware Detection

**Use Case:** Detection of malware activities

**Rule:**
```
IF antivirus_alert = "malware_detected"
   OR process_name IN malware_indicators
   OR network_connection TO known_c2_server
THEN alert "Malware Detected"
```

**Severity:** Critical  
**Response:** Isolate host, incident response

#### Configuration Changes

**Use Case:** Monitoring of critical configuration changes

**Rule:**
```
IF event_type = "config_change"
   AND system IN critical_systems
   AND user NOT IN authorized_admins
THEN alert "Unauthorized Configuration Change"
```

**Severity:** High  
**Response:** Verify change, rollback if necessary

### Dashboards

#### Security Dashboard

**Metrics:**
- Failed login attempts (last 24h)
- Security alerts (by severity)
- Top 10 attacker IPs
- Malware detections
- Firewall blocks

**Target Audience:** Security Operations Team

#### Operations Dashboard

**Metrics:**
- System errors (by system)
- Application errors (by app)
- Performance metrics
- Disk space warnings
- Service availability

**Target Audience:** IT Operations Team

#### Compliance Dashboard

**Metrics:**
- Audit log coverage
- Retention compliance
- Access reviews
- Policy violations
- Privileged access monitoring

**Target Audience:** Compliance Officer, Auditors

### Alerting

**Alert Channels:**
- **Email:** {{ meta-handbook.alert_email }}
- **SMS:** For critical alerts
- **Ticketing:** {{ meta-handbook.ticketing_system }}
- **SIEM Console:** Real-time alerts
- **Slack/Teams:** Team notifications

**Alert Prioritization:**

| Severity | Response Time | Escalation | Example |
|---|---|---|---|
| **Critical** | Immediate | Immediate to on-call | Malware, Data Breach |
| **High** | < 1 hour | After 1h | Failed Logins, Privilege Escalation |
| **Medium** | < 4 hours | After 4h | Config Changes, Policy Violations |
| **Low** | < 24 hours | After 24h | Informational Events |

**Alert Tuning:**
- False positive reduction
- Threshold adjustment
- Whitelist for legitimate activities
- Regular review (monthly)

## Audit Trail Requirements

### Audit Logging Principles

**What is logged:**
- **Who:** User ID, IP address, Session ID
- **What:** Action, Resource, Changes
- **When:** Timestamp (UTC)
- **Where:** System, Application, Component
- **Result:** Success/Failure, Error code

**Audit Log Format:**
```json
{
  "timestamp": "2024-01-31T10:30:45Z",
  "user": "jdoe",
  "source_ip": "192.168.1.100",
  "action": "file_access",
  "resource": "/data/sensitive/customer_data.csv",
  "result": "success",
  "system": "fileserver01",
  "session_id": "abc123xyz"
}
```

### Critical Audit Events

#### Authentication and Authorization

**Events:**
- Login (successful/failed)
- Logout
- Password change
- Account creation/deletion
- Privilege change
- Role assignment

#### Data Access

**Events:**
- Access to sensitive data
- Data export
- Data modification
- Data deletion
- Database queries (for sensitive data)

#### System Changes

**Events:**
- Configuration changes
- Software installation/uninstallation
- Service start/stop
- Firewall rule changes
- Network changes

#### Administrative Activities

**Events:**
- Privileged access
- Backup/restore operations
- Security policy changes
- Audit log access
- System maintenance

### Audit Log Integrity

**Protection Measures:**
- **Write-Once:** Logs cannot be modified
- **Digital Signatures:** Logs are signed
- **Checksums:** Integrity verification
- **Separate Storage:** Logs on separate system
- **Access Control:** Only authorized access

**Verification:**
- Regular integrity checks
- Checksum validation
- Signature verification
- Anomaly detection (missing logs)

## Roles and Responsibilities

### Log Management Team

**Responsibilities:**
- Log infrastructure management
- Log collection configuration
- Retention policy implementation
- Tool administration

**Team Lead:** {{ meta-organisation-roles.role_it_operations_manager.name }}

### Security Operations Team

**Responsibilities:**
- SIEM monitoring
- Alert response
- Use case development
- Threat hunting

**Team Lead:** {{ meta-organisation-roles.role_ciso.name }}

### Compliance Officer

**Responsibilities:**
- Define compliance requirements
- Audit support
- Retention policy review
- Regulatory monitoring

**Person:** {{ meta-organisation-roles.role_Compliance_Manager }}

## Compliance and Regulation

### GDPR

**Requirements:**
- Logging of access to personal data
- Right to information (which data was processed)
- Right to deletion (logs with personal data)
- Breach notification obligation (72h)

**Implementation:**
- Access logs for all personal data
- Pseudonymization where possible
- Observe retention policies
- Deletion processes implemented

### ISO 27001

**Requirements:**
- A.12.4.1: Event Logging
- A.12.4.2: Protection of log information
- A.12.4.3: Administrator and operator logs
- A.12.4.4: Time synchronization

**Implementation:**
- Comprehensive event logging
- Log integrity ensured
- Privileged access logged
- NTP synchronization

### PCI-DSS (if applicable)

**Requirements:**
- Requirement 10: Track and monitor all access to network resources and cardholder data
- Audit trails for all access
- Daily log reviews
- Retention: At least 1 year (3 months online)

### SOX (if applicable)

**Requirements:**
- Audit trails for financially relevant systems
- Change traceability
- Access controls logged
- Retention: 7 years

## Log Management Tools

### SIEM Platform

**System:** {{ meta-handbook.siem_system }}  
**Components:**
- Indexers
- Search Heads
- Forwarders
- Deployment Server

### Log Collectors

**Rsyslog:**
- Central syslog servers
- Filtering and parsing
- Forwarding to SIEM

**Fluentd/Fluent Bit:**
- Lightweight log collector
- Plugin-based
- Kubernetes integration

**Elastic Beats:**
- Filebeat: Log files
- Metricbeat: System metrics
- Packetbeat: Network traffic
- Auditbeat: Audit data

### Log Analysis Tools

**Kibana:**
- Visualization
- Dashboards
- Ad-hoc queries

**Grafana:**
- Metrics visualization
- Alerting
- Multi-source integration

## Metrics and Reporting

### Log Management Metrics

| Metric | Target Value | Measurement |
|---|---|---|
| **Log Collection Rate** | > 99% | Collected Logs / Expected Logs |
| **Log Ingestion Latency** | < 5 Min | Time from Event to SIEM |
| **Storage Utilization** | < 80% | Used Storage / Total Storage |
| **Alert Response Time** | < 15 Min | Time from Alert to Response |
| **False Positive Rate** | < 10% | False Positives / Total Alerts |

### Reporting

**Daily Log Status Report:**
- Log collection status
- Missing log sources
- Storage utilization
- Critical alerts

**Weekly Security Report:**
- Security events summary
- Top alerts
- Trend analysis
- Anomalies

**Monthly Compliance Report:**
- Audit log coverage
- Retention compliance
- Access reviews
- Policy violations

**Quarterly Management Report:**
- Log management strategy review
- Capacity planning
- Compliance status
- Improvement measures

## References

- ISO/IEC 27001:2013 - A.12.4 (Logging and Monitoring)
- NIST SP 800-92 - Guide to Computer Security Log Management
- PCI-DSS v4.0 - Requirement 10
- GDPR - Article 30 (Record of processing activities)
- CIS Controls v8 - Control 8 (Audit Log Management)
- ITIL v4 - Monitoring and Event Management

**Document Owner:** {{ meta-handbook.owner }}  
**Approved by:** {{ meta-handbook.approver }}  
**Version:** {{ meta-handbook.revision }}  
**Classification:** {{ meta-handbook.classification }}  
**Last Update:** {{ meta-handbook.date }}

