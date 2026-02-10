# Runbooks and Standard Operations

## Overview

This document contains standard runbooks, step-by-step guides, and troubleshooting guides for common operational tasks. The goal is to ensure consistent and efficient execution of standard operations.

**Document Owner:** {{ meta.document.owner }}  
**Approved by:** {{ meta.document.approver }}  
**Version:** {{ meta.document.version }}  
**Organization:** {{ meta.organization.name }}

---

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

---

## System Management Runbooks

### RB-001: Server Restart

**Runbook ID:** RB-001  
**Version:** 1.0  
**Responsible:** {{ meta.it_operations_manager.name }}

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

---

### RB-002: Service Restart

**Runbook ID:** RB-002  
**Version:** 1.0  
**Responsible:** {{ meta.it_operations_manager.name }}

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

---

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

#### Validation
- [ ] Backup file created
- [ ] Backup size plausible
- [ ] Backup integrity checked
- [ ] Backup location documented

---

## Network Management Runbooks

### RB-020: Add Firewall Rule

**Runbook ID:** RB-020  
**Version:** 1.0  
**Responsible:** {{ meta.ciso.name }}

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

---

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

---

## Processes and Responsibilities

### RACI Matrix

| Activity | CIO | Ops Manager | Ops Team | On-Call |
|---|---|---|---|---|
| Runbook Creation | C | A | R | C |
| Runbook Execution | I | C | R | R |
| Runbook Update | I | A | R | C |
| Troubleshooting | I | C | R | R |

> **Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

---

**Last Update:** {{ meta.date }}  
**Next Review:** [TODO: Date]  
**Contact:** {{ meta.it_operations_manager.email }}

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial Creation |
