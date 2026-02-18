# Guideline: Backup, Restore and Regular Tests

**Document-ID:** [FRAMEWORK]-0430
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

This guideline implements the `0420_Policy_Backup_and_Recovery.md` and defines:
- Backup strategies and frequencies
- Restore processes and tests
- Backup monitoring and verification

**Scope:** All data and systems at **{{ meta-organisation.name }}**

## 2. Backup Strategy

### 2.1 3-2-1 Rule

**Principle:**
- **3** copies of data (1 production + 2 backups)
- **2** different media types (e.g., disk + tape/cloud)
- **1** copy off-site (geographically separated)

### 2.2 Backup Types

**Full Backup:**
- Complete backup of all data
- Frequency: Weekly (Sunday)
- Longest restore time, but simplest recovery

**Incremental Backup:**
- Only changes since last backup
- Frequency: Daily
- Fastest backup, longer restore time

**Differential Backup:**
- Changes since last full backup
- Frequency: Optional, as needed
- Balance between full and incremental

### 2.3 Backup Frequencies

| System Type | Full | Incremental | RPO | RTO |
|-------------|------|-------------|-----|-----|
| Critical databases | Daily | Hourly | 1h | 4h |
| Production servers | Weekly | Daily | 24h | 8h |
| File servers | Weekly | Daily | 24h | 8h |
| Workstations | Monthly | Weekly | 7d | 24h |
| Email | Daily | Hourly | 1h | 4h |

**RPO (Recovery Point Objective):** Maximum data loss  
**RTO (Recovery Time Objective):** Maximum recovery time

## 3. Backup Implementation

### 3.1 Backup Systems

**On-Premises:**
- **Backup Server:** {{ meta.backup.server }}
- **Backup Software:** {{ meta.backup.software }} (e.g., Veeam, Commvault)
- **Storage:** {{ meta.backup.storage }} (disk, tape)

**Cloud Backup:**
- **Cloud Provider:** {{ meta.cloud.backup_provider }} (e.g., Azure Backup, AWS Backup)
- **Encryption:** AES-256
- **Geo-Redundancy:** Enabled

### 3.2 Backup Windows

**Production Systems:**
- Backup window: 22:00 - 06:00
- Minimal performance impact
- Monitoring during backup

**Development Systems:**
- Backup window: Anytime
- No performance requirements

### 3.3 Encryption

**In Transit:**
- TLS 1.2+ for backup transmission
- VPN for off-site backups

**At Rest:**
- AES-256 encryption of all backups
- Key management via Key Vault
- Separate keys for backups

### 3.4 Retention

**Retention Scheme (GFS - Grandfather-Father-Son):**
- **Daily:** 7 days
- **Weekly:** 4 weeks
- **Monthly:** 12 months
- **Yearly:** {{ meta.retention.backup_years }} years

**Compliance Backups:**
- Financial data: 10 years
- Personnel data: Per GDPR
- Emails: {{ meta.retention.email_years }} years

## 4. Restore Processes

### 4.1 Restore Types

**File-Level Restore:**
- Individual files or folders
- Self-service for users (limited)
- IT support for extensive restores

**System-Level Restore:**
- Complete server recovery
- Bare-metal recovery
- Only by IT operations

**Database Restore:**
- Point-in-time recovery
- Transaction logs
- Only by database admins

### 4.2 Restore Process

**Step 1: Request**
- Create ticket with details (what, when, why)
- Approval by supervisor (for extensive restores)

**Step 2: Preparation**
- Check backup catalog
- Prepare restore target
- Plan downtime (if required)

**Step 3: Restore**
- Perform restore
- Monitor progress
- Error handling

**Step 4: Verification**
- Check data integrity
- Functional test
- User confirmation

**Step 5: Documentation**
- Restore log
- Lessons learned
- Close ticket

### 4.3 Disaster Recovery

**In Case of Total Failure:**
1. Activate disaster recovery plan
2. Provide alternative infrastructure
3. Restore critical systems first
4. Gradual restoration of additional systems
5. Verification and return to normal operations

**Details:** See `0160_Disaster_Recovery_and_Business_Continuity.md` (IT Operation Templates)

## 5. Backup Monitoring

### 5.1 Monitored Metrics

**Backup Jobs:**
- Successful/failed backups
- Backup duration
- Backup size
- Change rate

**Storage:**
- Available storage space
- Growth rate
- Deduplication rate

**Performance:**
- Backup speed
- Network utilization
- Storage performance

### 5.2 Alerting

**Critical Alerts:**
- Backup failed (2x consecutive)
- Storage > 90% full
- Backup window exceeded
- Encryption failed

**Escalation:**
- First notification: Backup admin
- After 2 hours: IT Operations Manager
- After 4 hours: CISO (for critical systems)

### 5.3 Reporting

**Daily Backup Report:**
- Status of all backup jobs
- Failed backups
- Storage utilization

**Monthly Management Report:**
- Backup success rate
- Restore statistics
- Capacity planning
- Compliance status

## 6. Backup Tests

### 6.1 Test Frequencies

| Test Type | Frequency | Execution |
|-----------|-----------|-----------|
| File-level restore | Monthly | Sample |
| System-level restore | Quarterly | Critical systems |
| Database restore | Monthly | Point-in-time recovery |
| Disaster recovery | Annually | Full DR test |

### 6.2 Test Process

**Planning:**
1. Define test scope
2. Set test time window
3. Inform stakeholders
4. Prepare test environment

**Execution:**
1. Restore to test environment
2. Check data integrity
3. Functional test
4. Performance test
5. Time measurement (RTO verification)

**Documentation:**
1. Create test protocol
2. Document success/failure
3. Problems and lessons learned
4. Define improvement measures

**Follow-up:**
1. Clean up test environment
2. Adjust backup processes (if required)
3. Management report

### 6.3 Disaster Recovery Drill

**Annual DR Test:**
- Simulation of total failure
- Activation of DR plan
- Restoration of critical systems
- Time measurement and documentation
- Management presentation

**Participants:**
- IT operations
- Application owners
- Management
- Business representatives

## 7. Backup Security

### 7.1 Access Control

**Permissions:**
- **Backup Admins:** Full access to backup system
- **System Admins:** Restore permission for own systems
- **Users:** Self-service restore (limited)

**Authentication:**
- MFA for backup system access
- Privileged accounts for backup admins

### 7.2 Immutable Backups

**Ransomware Protection:**
- Immutable backups (write-once-read-many)
- Air-gapped backups (offline)
- Separate credentials for backup storage

**Retention Lock:**
- Backups cannot be deleted prematurely
- Protection against accidental or malicious deletion

### 7.3 Audit Logging

**Logged Events:**
- Backup job starts and ends
- Restore requests and executions
- Configuration changes
- Access to backup system

**Retention:** {{ meta.retention.log_years }} years

## 8. Compliance and Audit

### 8.1 Key Performance Indicators (KPIs)

| Metric | Target Value |
|--------|--------------|
| Backup success rate | > 99% |
| Restore success rate | 100% |
| RTO compliance | 100% |
| RPO compliance | 100% |
| Test completion rate | 100% |

### 8.2 Audit Evidence

- Backup logs and reports
- Restore test protocols
- DR drill documentation
- Compliance reports

## 9. References

### Internal Documents
- `0420_Policy_Backup_and_Recovery.md`
- `0160_Disaster_Recovery_and_Business_Continuity.md` (IT Operation)

### External Standards
- **ISO/IEC 27001:2022 Annex A.8.13** - Information backup
- **NIST SP 800-34** - Contingency Planning Guide

**Approved by:** {{ meta.ciso.name }}, CISO  
**Next Review:** {{ meta-handbook.next_review }}

