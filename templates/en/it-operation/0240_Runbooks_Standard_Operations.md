# Runbooks and Standard Operations

**Document-ID:** [FRAMEWORK]-0240
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

## Overview

This document contains standard runbooks, step-by-step guides, and troubleshooting guides for common operational tasks. The goal is to ensure consistent and efficient execution of standard operations.

**Document Owner:** {{ meta-handbook.owner }}  
**Approved by:** {{ meta-handbook.approver }}  
**Version:** {{ meta-handbook.revision }}  
**Organization:** {{ meta-organisation.name }}

## Runbook Structure

### Runbook Template

Each runbook follows this standardized structure:

```markdown
# [RUNBOOK TITLE]

**Runbook ID:** RB-[NUMBER]
**Version:** [VERSION]
**Last Update:** [DATE]
**Responsible:** [NAME]

## Purpose
[Description of purpose and use case]

## Prerequisites
- [Required permissions]
- [Required tools]
- [Required knowledge]

## Estimated Duration
[TIME] minutes/hours

## Risk Assessment
- **Risk:** Low / Medium / High
- **Impact:** Low / Medium / High
- **Rollback possible:** Yes / No

## Steps
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Validation
- [Validation step 1]
- [Validation step 2]

## Rollback
[Rollback procedure if required]

## Troubleshooting
[Common problems and solutions]

## References
- [Documentation]
- [Tickets]
```

## System Management Runbooks

### RB-001: Server Restart

**Runbook ID:** RB-001  
**Version:** 1.0  
**Responsible:** {{ meta-organisation-roles.role_IT_Operations_Manager }}

#### Purpose
Controlled restart of a server to fix problems or after updates.

#### Prerequisites
- Root/Administrator access to server
- Approval for restart (for production systems)
- Maintenance window (if required)

#### Estimated Duration
15-30 minutes

#### Risk Assessment
- **Risk:** Medium
- **Impact:** High (for production systems)
- **Rollback possible:** No

#### Steps

1. **Preparation**
   ```bash
   # Check current system load
   uptime
   top
   
   # Check running processes
   ps aux | grep [critical_processes]
   
   # Inform users (if required)
   wall "System will restart in 5 minutes"
   ```

2. **Stop Services**
   ```bash
   # Stop application services
   systemctl stop [service_name]
   
   # Check status
   systemctl status [service_name]
   ```

3. **Perform Restart**
   ```bash
   # Initiate restart
   shutdown -r now
   # or
   reboot
   ```

4. **After Restart: Validation**
   ```bash
   # Check system uptime
   uptime
   
   # Check services
   systemctl status [service_name]
   
   # Check logs
   journalctl -xe
   tail -f /var/log/syslog
   ```

#### Validation
- [ ] Server is reachable (ping, SSH)
- [ ] All critical services running
- [ ] No errors in system logs
- [ ] Monitoring shows green status
- [ ] Application is functional

#### Troubleshooting
- **Problem:** Server won't start
  - **Solution:** Use console access, check boot logs
- **Problem:** Services won't start
  - **Solution:** Start manually, check logs, check dependencies

### RB-002: Service Restart

**Runbook ID:** RB-002  
**Version:** 1.0  
**Responsible:** {{ meta-organisation-roles.role_IT_Operations_Manager }}

#### Purpose
Restart a single service without system restart.

#### Prerequisites
- Sudo/Administrator rights
- Service name known

#### Estimated Duration
5-10 minutes

#### Steps

1. **Check Service Status**
   ```bash
   # Linux
   systemctl status [service_name]
   
   # Windows
   Get-Service [service_name]
   ```

2. **Stop Service**
   ```bash
   # Linux
   systemctl stop [service_name]
   
   # Windows
   Stop-Service [service_name]
   ```

3. **Wait and Validate**
   ```bash
   # Confirm process end
   ps aux | grep [service_name]
   
   # Check ports released
   netstat -tulpn | grep [port]
   ```

4. **Start Service**
   ```bash
   # Linux
   systemctl start [service_name]
   
   # Windows
   Start-Service [service_name]
   ```

5. **Validation**
   ```bash
   # Check status
   systemctl status [service_name]
   
   # Check logs
   journalctl -u [service_name] -f
   ```

#### Validation
- [ ] Service running (Status: active/running)
- [ ] No errors in logs
- [ ] Port is bound
- [ ] Application responds

### RB-003: Disk Space Cleanup

**Runbook ID:** RB-003  
**Version:** 1.0  
**Responsible:** {{ meta-organisation-roles.role_IT_Operations_Manager }}

#### Purpose
Free up disk space during critical disk utilization.

#### Prerequisites
- Root/Administrator access
- Backup before major deletions

#### Estimated Duration
30-60 minutes

#### Steps

1. **Analyze Disk Usage**
   ```bash
   # Overall view
   df -h
   
   # Find largest directories
   du -h / | sort -rh | head -20
   
   # Find largest files
   find / -type f -size +100M -exec ls -lh {} \; 2>/dev/null
   ```

2. **Clean Log Files**
   ```bash
   # Delete old logs
   find /var/log -type f -name "*.log" -mtime +30 -delete
   
   # Delete compressed logs
   find /var/log -type f -name "*.gz" -mtime +90 -delete
   
   # Clean journal logs
   journalctl --vacuum-time=30d
   ```

3. **Delete Temporary Files**
   ```bash
   # Clean /tmp
   find /tmp -type f -atime +7 -delete
   
   # Clean /var/tmp
   find /var/tmp -type f -atime +30 -delete
   ```

4. **Clean Package Cache**
   ```bash
   # Debian/Ubuntu
   apt-get clean
   apt-get autoclean
   apt-get autoremove
   
   # RedHat/CentOS
   yum clean all
   
   # Docker
   docker system prune -a
   ```

5. **Archive/Delete Old Backups**
   ```bash
   # Identify old backups
   find /backup -type f -mtime +90
   
   # Delete after approval
   find /backup -type f -mtime +90 -delete
   ```

#### Validation
- [ ] Disk utilization below 80%
- [ ] Critical services still running
- [ ] No important data deleted
- [ ] Monitoring alerts resolved

## Database Management Runbooks

### RB-010: Database Backup

**Runbook ID:** RB-010  
**Version:** 1.0  
**Responsible:** Database Administrator

#### Purpose
Manual database backup before critical changes.

#### Prerequisites
- Database admin rights
- Sufficient storage space
- Backup directory exists

#### Estimated Duration
15-60 minutes (depending on DB size)

#### Steps

**PostgreSQL:**
```bash
# Full Backup
pg_dump -U postgres -F c -b -v -f /backup/db_$(date +%Y%m%d_%H%M%S).backup [database_name]

# Schema-only Backup
pg_dump -U postgres -s -f /backup/schema_$(date +%Y%m%d_%H%M%S).sql [database_name]
```

**MySQL/MariaDB:**
```bash
# Full Backup
mysqldump -u root -p --single-transaction --routines --triggers [database_name] > /backup/db_$(date +%Y%m%d_%H%M%S).sql

# All Databases
mysqldump -u root -p --all-databases > /backup/all_dbs_$(date +%Y%m%d_%H%M%S).sql
```

**MongoDB:**
```bash
# Full Backup
mongodump --out /backup/mongodb_$(date +%Y%m%d_%H%M%S)

# Specific Database
mongodump --db [database_name] --out /backup/mongodb_$(date +%Y%m%d_%H%M%S)
```

#### Validation
- [ ] Backup file created
- [ ] Backup size plausible
- [ ] Backup integrity checked
- [ ] Backup location documented

### RB-011: Database Restore

**Runbook ID:** RB-011  
**Version:** 1.0  
**Responsible:** Database Administrator

#### Purpose
Restore a database from backup.

#### Prerequisites
- Database admin rights
- Valid backup available
- Maintenance window (for production systems)

#### Estimated Duration
30-120 minutes (depending on DB size)

#### Risk Assessment
- **Risk:** High
- **Impact:** High
- **Rollback possible:** Yes (with current backup)

#### Steps

1. **Preparation**
   ```bash
   # Create current backup (safety!)
   [see RB-010]
   
   # Inform users
   # Stop services
   ```

2. **Perform Restore**

   **PostgreSQL:**
   ```bash
   # Drop and recreate database
   dropdb [database_name]
   createdb [database_name]
   
   # Restore
   pg_restore -U postgres -d [database_name] -v /backup/db_backup.backup
   ```

   **MySQL/MariaDB:**
   ```bash
   # Restore
   mysql -u root -p [database_name] < /backup/db_backup.sql
   ```

   **MongoDB:**
   ```bash
   # Restore
   mongorestore --db [database_name] /backup/mongodb_backup/[database_name]
   ```

3. **Validation**
   ```bash
   # Check tables/collections
   # Count records
   # Check integrity
   ```

#### Validation
- [ ] Database is reachable
- [ ] All tables/collections present
- [ ] Record count plausible
- [ ] Application functional
- [ ] No errors in logs

## Network Management Runbooks

### RB-020: Add Firewall Rule

**Runbook ID:** RB-020  
**Version:** 1.0  
**Responsible:** {{ meta-organisation-roles.role_CISO }}

#### Purpose
Adding a new firewall rule.

#### Prerequisites
- Firewall admin rights
- Change ticket approved
- Rule details documented

#### Estimated Duration
15-30 minutes

#### Steps

1. **Document Rule Details**
   - Source IP/Network
   - Destination IP/Network
   - Port/Protocol
   - Action (Allow/Deny)
   - Justification

2. **Add Rule**

   **iptables (Linux):**
   ```bash
   # Add rule
   iptables -A INPUT -s [source_ip] -p tcp --dport [port] -j ACCEPT
   
   # Save rule
   iptables-save > /etc/iptables/rules.v4
   ```

   **firewalld (Linux):**
   ```bash
   # Open port
   firewall-cmd --permanent --add-port=[port]/tcp
   
   # Reload
   firewall-cmd --reload
   ```

   **Windows Firewall:**
   ```powershell
   # Add rule
   New-NetFirewallRule -DisplayName "[Rule Name]" -Direction Inbound -Protocol TCP -LocalPort [port] -Action Allow
   ```

3. **Validation**
   ```bash
   # Check rule
   iptables -L -n -v
   
   # Test connectivity
   telnet [target_ip] [port]
   nc -zv [target_ip] [port]
   ```

#### Validation
- [ ] Rule is active
- [ ] Connectivity works
- [ ] No unwanted side effects
- [ ] Rule documented

## User Management Runbooks

### RB-030: Create User Account

**Runbook ID:** RB-030  
**Version:** 1.0  
**Responsible:** {{ meta-organisation-roles.role_IT_Operations_Manager }}

#### Purpose
Create a new user account.

#### Prerequisites
- Admin rights
- Approved ticket
- User details available

#### Estimated Duration
10-15 minutes

#### Steps

1. **Collect User Details**
   - Full name
   - Email address
   - Department
   - Required groups/roles
   - Manager/Approver

2. **Create Account**

   **Linux:**
   ```bash
   # Create user
   useradd -m -s /bin/bash -c "[Full Name]" [username]
   
   # Set password
   passwd [username]
   
   # Add to groups
   usermod -aG [group1],[group2] [username]
   ```

   **Active Directory:**
   ```powershell
   # Create user
   New-ADUser -Name "[Full Name]" -GivenName "[First]" -Surname "[Last]" `
     -SamAccountName [username] -UserPrincipalName [username]@domain.com `
     -Path "OU=Users,DC=domain,DC=com" -AccountPassword (ConvertTo-SecureString "[password]" -AsPlainText -Force) `
     -Enabled $true
   
   # Add to groups
   Add-ADGroupMember -Identity "[Group Name]" -Members [username]
   ```

3. **Assign Permissions**
   - Filesystem permissions
   - Application access
   - Email account
   - VPN access

4. **Inform User**
   - Send welcome email
   - Transmit credentials (securely!)
   - Provide documentation

#### Validation
- [ ] Account is active
- [ ] Login works
- [ ] Permissions correct
- [ ] User informed
- [ ] Documented in CMDB

### RB-031: Deactivate User Account

**Runbook ID:** RB-031  
**Version:** 1.0  
**Responsible:** {{ meta-organisation-roles.role_IT_Operations_Manager }}

#### Purpose
Deactivate a user account (e.g., upon departure).

#### Prerequisites
- Admin rights
- Approved ticket
- Offboarding checklist

#### Estimated Duration
20-30 minutes

#### Steps

1. **Deactivate Account**

   **Linux:**
   ```bash
   # Lock account
   usermod -L [username]
   passwd -l [username]
   
   # Disable shell
   usermod -s /sbin/nologin [username]
   ```

   **Active Directory:**
   ```powershell
   # Deactivate account
   Disable-ADAccount -Identity [username]
   
   # Update description
   Set-ADUser -Identity [username] -Description "Deactivated on $(Get-Date -Format 'yyyy-MM-dd')"
   ```

2. **Remove Access**
   - Deactivate VPN access
   - Set up email forwarding
   - Remove group memberships
   - Revoke application access
   - Reclaim hardware

3. **Backup Data**
   - Archive home directory
   - Archive emails
   - Backup important files

4. **Documentation**
   - Complete offboarding checklist
   - Update CMDB
   - Inform manager

#### Validation
- [ ] Account is deactivated
- [ ] Login no longer possible
- [ ] All access removed
- [ ] Data backed up
- [ ] Documented

## Monitoring and Alerting Runbooks

### RB-040: Alert Investigation

**Runbook ID:** RB-040  
**Version:** 1.0  
**Responsible:** {{ meta-organisation-roles.role_IT_Operations_Manager }}

#### Purpose
Systematic investigation of a monitoring alert.

#### Prerequisites
- Access to monitoring system
- Access to affected systems

#### Estimated Duration
15-60 minutes

#### Steps

1. **Capture Alert Details**
   - Alert name and severity
   - Affected system/service
   - Time of occurrence
   - Alert description

2. **Initial Analysis**
   ```bash
   # Check system status
   uptime
   top
   df -h
   free -m
   
   # Check service status
   systemctl status [service]
   
   # Check logs
   journalctl -xe
   tail -f /var/log/[relevant_log]
   ```

3. **Identify Cause**
   - Correlation with other events
   - Recent changes
   - Check known issues
   - Analyze metrics

4. **Take Action**
   - Immediate measures (if required)
   - Create incident ticket
   - Escalation (if required)
   - Documentation

5. **Validation**
   - Alert is resolved
   - System functioning normally
   - No further alerts

#### Troubleshooting Matrix

| Alert Type | First Check | Common Causes | Immediate Action |
|---|---|---|---|
| High CPU | top, ps aux | Runaway process | Kill process |
| High Memory | free -m, ps aux | Memory leak | Service restart |
| Disk Full | df -h, du -h | Log files, backups | Perform cleanup |
| Service Down | systemctl status | Crash, config error | Service restart |
| High Latency | ping, traceroute | Network, load | Check load balancing |

## Backup and Recovery Runbooks

### RB-050: Backup Verification

**Runbook ID:** RB-050  
**Version:** 1.0  
**Responsible:** {{ meta-organisation-roles.role_IT_Operations_Manager }}

#### Purpose
Regular verification of backup integrity.

#### Prerequisites
- Access to backup system
- Test environment available

#### Estimated Duration
30-60 minutes

#### Steps

1. **Check Backup Status**
   ```bash
   # Show recent backups
   [backup_tool] list --last 7
   
   # Check backup logs
   tail -100 /var/log/backup.log
   ```

2. **Check Backup Integrity**
   ```bash
   # Validate checksums
   [backup_tool] verify [backup_id]
   
   # Check backup size
   ls -lh /backup/
   ```

3. **Perform Restore Test**
   - Select random backup
   - Restore to test environment
   - Validate functionality
   - Document result

4. **Documentation**
   - Record test result
   - Document issues
   - Identify improvements

#### Validation
- [ ] All backups successful
- [ ] Integrity confirmed
- [ ] Restore test successful
- [ ] Documented

## Troubleshooting Guides

### General Troubleshooting Methodology

1. **Identify Problem**
   - Collect symptoms
   - Note error messages
   - Time of occurrence

2. **Gather Information**
   - Analyze logs
   - Check monitoring data
   - Identify changes

3. **Form Hypothesis**
   - List possible causes
   - Assess probability
   - Prioritize

4. **Test**
   - Test hypothesis
   - Document results
   - Next hypothesis

5. **Implement Solution**
   - Perform corrective action
   - Validate
   - Document

6. **Prevention**
   - Root cause analysis
   - Identify improvements
   - Implement

### Common Problems and Solutions

#### Problem: Service Won't Start

**Symptoms:**
- Service status: failed
- Error message in logs

**Diagnosis:**
```bash
# Check status
systemctl status [service]

# Check logs
journalctl -u [service] -n 50

# Config test
[service] -t  # (e.g., nginx -t, apache2ctl configtest)
```

**Solutions:**
1. Correct config errors
2. Check dependencies
3. Check permissions
4. Check ports (already in use?)

#### Problem: High CPU Load

**Symptoms:**
- CPU utilization > 80%
- System slow

**Diagnosis:**
```bash
# Identify top processes
top
htop

# Process details
ps aux | sort -nrk 3,3 | head -n 5
```

**Solutions:**
1. Kill runaway process
2. Set resource limits
3. Check scaling
4. Code optimization

#### Problem: Disk Full

**Symptoms:**
- Disk utilization > 90%
- "No space left on device" error

**Diagnosis:**
```bash
# Check utilization
df -h

# Find large files
du -h / | sort -rh | head -20
find / -type f -size +100M
```

**Solutions:**
1. Clean logs
2. Delete temporary files
3. Archive old backups
4. Expand storage

## Processes and Responsibilities

### RACI Matrix

| Activity | CIO | Ops Manager | Ops Team | On-Call |
|---|---|---|---|---|
| Runbook Creation | C | A | R | C |
| Runbook Execution | I | C | R | R |
| Runbook Update | I | A | R | C |
| Troubleshooting | I | C | R | R |

> **Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

## Compliance and Standards

### Relevant Standards
- **ITIL v4:** Service Operation Practice
- **ISO 20000:** Clause 8.1 - Operational Planning and Control
- **COBIT 2019:** DSS01 - Managed Operations

## Appendix

### Glossary

| Term | Definition |
|---|---|
| Runbook | Documented step-by-step guide for standard operations |
| Troubleshooting | Systematic error detection and resolution |
| Standard Operating Procedure (SOP) | Standardized operational instruction |

### References
- ITIL v4 Foundation Handbook
- ISO/IEC 20000-1:2018
- COBIT 2019 Framework

**Last Update:** {{ meta-handbook.date }}  
**Next Review:** [TODO: Date]  
**Contact:** {{ meta-organisation-roles.role_IT_Operations_Manager_email }}

