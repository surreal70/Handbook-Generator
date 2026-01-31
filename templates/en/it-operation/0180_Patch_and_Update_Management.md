# Patch and Update Management

## Purpose and Scope

This document describes the patch and update management processes for {{ meta.organization.name }}. It defines patch categories, schedules, test and rollout processes, as well as vulnerability scanning and prioritization to ensure system security and stability.

**Scope:** All IT systems, operating systems, applications, and firmware of {{ meta.organization.name }}

**Responsible:** {{ meta.it_operations_manager.name }} ({{ meta.it_operations_manager.email }})

## Patch Management Fundamentals

### Objectives

**Primary Objectives:**
- **Security:** Closing security vulnerabilities
- **Stability:** Fixing bugs and errors
- **Compliance:** Meeting regulatory requirements
- **Performance:** Optimization and new features
- **Compatibility:** Supporting new technologies

### Patch Categories

#### Security Patches

**Description:** Patches that close security vulnerabilities

**Priority:** Critical to High

**Examples:**
- CVE-affected vulnerabilities
- Zero-day exploits
- Critical security vulnerabilities

**SLA:**
- **Critical (CVSS 9.0-10.0):** 7 days
- **High (CVSS 7.0-8.9):** 30 days
- **Medium (CVSS 4.0-6.9):** 90 days
- **Low (CVSS 0.1-3.9):** 180 days

#### Feature Updates

**Description:** Updates with new features and improvements

**Priority:** Medium

**Examples:**
- New features
- Performance improvements
- UI/UX enhancements

**SLA:** As needed, scheduled in maintenance windows

#### Bugfix Patches

**Description:** Patches to fix bugs without security relevance

**Priority:** Low to Medium

**Examples:**
- Functional errors
- Performance issues
- Compatibility problems

**SLA:** 90 days or as needed

#### Firmware Updates

**Description:** Updates for hardware firmware

**Priority:** Medium to High

**Examples:**
- BIOS/UEFI updates
- Storage controller firmware
- Network equipment firmware

**SLA:** According to vendor recommendation, scheduled

### Patch Sources

| System Type | Patch Source | Update Mechanism |
|---|---|---|
| **Windows** | Windows Update, WSUS | Automatic/Manual |
| **Linux (RHEL/CentOS)** | Red Hat Network, YUM | yum update |
| **Linux (Ubuntu/Debian)** | Ubuntu Repositories, APT | apt update && apt upgrade |
| **VMware** | VMware Update Manager | VUM |
| **Applications** | Vendor websites, Package Manager | Manual/Automatic |
| **Firmware** | Vendor support sites | Manual |
| **Cloud Services** | Provider-managed | Automatic |

## Patch Management Process

### Process Overview

```
┌─────────────────┐
│ Vulnerability   │
│ Identification  │
└────────┬────────┘
         │
┌────────▼────────┐
│ Patch           │
│ Assessment      │
└────────┬────────┘
         │
┌────────▼────────┐
│ Patch           │
│ Acquisition     │
└────────┬────────┘
         │
┌────────▼────────┐
│ Patch           │
│ Testing         │
└────────┬────────┘
         │
┌────────▼────────┐
│ Patch           │
│ Deployment      │
└────────┬────────┘
         │
┌────────▼────────┐
│ Verification    │
│ & Reporting     │
└─────────────────┘
```

### 1. Vulnerability Identification

**Identification Sources:**
- **Vulnerability Scanner:** {{ meta.vulnerability_scanner }}
- **Vendor Advisories:** Microsoft, Red Hat, VMware, etc.
- **Security Mailing Lists:** CERT, US-CERT, vendor-specific
- **Threat Intelligence:** {{ meta.threat_intelligence_source }}
- **SIEM Alerts:** {{ meta.siem_system }}

**Activities:**
- Conduct vulnerability scans (weekly)
- Monitor vendor advisories (daily)
- Check CVE database
- Identify affected systems
- Check patch availability

**Responsible:** Security Operations Team

### 2. Patch Assessment

**Assessment Criteria:**

| Criterion | Assessment |
|---|---|
| **CVSS Score** | 0.0 - 10.0 |
| **Exploit Availability** | Yes/No |
| **Asset Criticality** | Critical/Important/Standard |
| **Exposure** | Internet-facing/Internal |
| **Vendor Recommendation** | Immediate/Planned/Optional |

**Risk Matrix:**

|  | **Internet-facing** | **Internal** |
|---|---|---|
| **Critical (CVSS 9-10)** | Immediate (7 days) | High (14 days) |
| **High (CVSS 7-8.9)** | High (14 days) | Medium (30 days) |
| **Medium (CVSS 4-6.9)** | Medium (30 days) | Low (90 days) |
| **Low (CVSS 0-3.9)** | Low (90 days) | Very low (180 days) |

**Impact Assessment:**
- Which systems are affected?
- Which business processes are dependent?
- Is a reboot required?
- Are there known compatibility issues?
- Which maintenance window is available?

**Decision:**
- **Patch:** Install patch
- **Defer:** Postpone patch (with justification)
- **Reject:** Do not install patch (with justification)
- **Workaround:** Alternative mitigation

**Responsible:** Patch Management Team

### 3. Patch Acquisition

**Acquisition Activities:**
- Download patch from vendor source
- Verify patch integrity (checksums, signatures)
- Store patch in patch repository
- Document patch metadata

**Patch Repository:** {{ meta.patch_repository }}

**Documentation:**
- Patch ID
- Vendor
- Release date
- CVE IDs
- Affected systems
- Installation instructions

**Responsible:** Patch Management Team

### 4. Patch Testing

**Test Environments:**

| Environment | Purpose | Systems |
|---|---|---|
| **Dev** | Developer tests | {{ netbox.environment.dev }} |
| **Test** | Functional tests | {{ netbox.environment.test }} |
| **Staging** | Pre-production tests | {{ netbox.environment.staging }} |
| **Production** | Production systems | {{ netbox.environment.production }} |

**Test Process:**

#### Phase 1: Dev Testing (Optional)

**Duration:** 1-2 days

**Activities:**
- Install patch in dev environment
- Test basic functionality
- Identify obvious problems

#### Phase 2: Test Testing

**Duration:** 3-5 days

**Activities:**
- Install patch in test environment
- Conduct functional tests
- Conduct performance tests
- Conduct compatibility tests
- Test rollback procedure

**Test Checklist:**
- [ ] Patch successfully installed
- [ ] System boots after reboot
- [ ] Applications start
- [ ] Basic functionality works
- [ ] Performance acceptable
- [ ] No error logs
- [ ] Rollback successfully tested

#### Phase 3: Staging Testing

**Duration:** 2-3 days

**Activities:**
- Install patch in staging environment
- Conduct business process tests
- User acceptance tests (UAT)
- Load tests (if critical)

**Go/No-Go Decision:**
- All tests passed → Go
- Critical problems → No-Go, defer patch
- Non-critical problems → Go with workaround

**Responsible:** QA Team, Application Owners

**Exceptions (Emergency Patches):**
- Critical security patches can shorten test phase
- Minimum basic tests in test environment
- Increased risk accepted and documented

### 5. Patch Deployment

**Deployment Strategies:**

#### Phased Rollout (Standard)

**Description:** Gradual rollout in phases

**Phases:**
1. **Pilot Group:** 5-10% of systems (1-2 days)
2. **Phase 1:** 25% of systems (2-3 days)
3. **Phase 2:** 50% of systems (2-3 days)
4. **Phase 3:** All remaining systems

**Advantages:**
- Risk minimization
- Early problem detection
- Controlled rollout

**Application:** Standard patches, feature updates

#### Big Bang (All at once)

**Description:** Patch all systems simultaneously

**Advantages:**
- Fast rollout
- Simple coordination

**Disadvantages:**
- High risk
- Large impact if problems occur

**Application:** Only for non-critical systems or emergencies

#### Rolling Update

**Description:** Patch systems one after another (e.g., in clusters)

**Advantages:**
- No downtime
- Continuous availability

**Application:** High-availability systems, load-balanced clusters

**Deployment Methods:**

| Method | Tool | Application |
|---|---|---|
| **Automatic** | WSUS, SCCM, Ansible | Standard patches |
| **Semi-Automatic** | Patch management tool | Scheduled patches |
| **Manual** | Remote session | Critical systems, firmware |

**Deployment Time Windows:**

| System Tier | Maintenance Window | Frequency |
|---|---|---|
| **Tier 0 (Critical)** | Sunday 02:00-06:00 | Monthly |
| **Tier 1 (Important)** | Saturday 22:00-02:00 | Monthly |
| **Tier 2 (Standard)** | Wednesday 20:00-22:00 | Monthly |
| **Tier 3 (Non-critical)** | Anytime | As needed |

**Deployment Checklist:**
- [ ] Change ticket created and approved
- [ ] Stakeholders informed
- [ ] Backup created
- [ ] Rollback plan ready
- [ ] Monitoring activated
- [ ] On-call team available

**Responsible:** IT Operations Team

### 6. Verification & Reporting

**Verification Activities:**
- Confirm patch installation
- Check system functionality
- Monitor performance metrics
- Check error logs
- Repeat vulnerability scan

**Verification Checklist:**
- [ ] Patch installed on all target systems
- [ ] Systems running stable
- [ ] No critical errors
- [ ] Performance normal
- [ ] Vulnerability closed (scan)

**Reporting:**
- Patch status report
- Success/failure rate
- Open patches
- Compliance status

**Responsible:** Patch Management Team

## Patch Schedules

### Monthly Patch Cycle

**Microsoft Patch Tuesday:**
- **Patch Release:** 2nd Tuesday of month
- **Assessment:** Tuesday-Wednesday
- **Testing:** Wednesday-Friday (Week 1)
- **Staging:** Monday-Wednesday (Week 2)
- **Production Deployment:** Saturday/Sunday (Week 2-3)

**Linux Patches:**
- **Assessment:** Weekly (Monday)
- **Testing:** Tuesday-Thursday
- **Deployment:** Saturday (monthly)

**Application Patches:**
- **Assessment:** Upon vendor release
- **Testing:** 1 week
- **Deployment:** Next maintenance window

### Emergency Patches

**Trigger:**
- Critical vulnerability (CVSS > 9.0)
- Active exploits in the wild
- Zero-day vulnerabilities
- Vendor recommendation "Immediate"

**Process:**
- **Assessment:** Immediate (< 4 hours)
- **Testing:** Minimal (< 8 hours)
- **Deployment:** Immediate (< 24 hours)

**Approval:** CIO or CISO

**Communication:** Inform all stakeholders immediately

### Patch Calendar

| Week | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday |
|---|---|---|---|---|---|---|---|
| **Week 1** | Assessment | Testing | Testing | Testing | Testing | - | - |
| **Week 2** | Staging | Staging | Staging | Go/No-Go | - | Tier 1 Deploy | Tier 0 Deploy |
| **Week 3** | Verification | Reporting | Tier 2 Deploy | - | - | - | - |
| **Week 4** | - | - | - | - | - | - | - |

## Patch Management Tools

### Windows Patch Management

**Tool:** Windows Server Update Services (WSUS)  
**Server:** {{ netbox.wsus.server }}  
**Management:** {{ netbox.wsus.management_url }}

**Configuration:**
- Automatic synchronization with Microsoft Update
- Patch approval workflow
- Computer groups by tier
- Reporting and compliance dashboard

**Patch Groups:**
- **Pilot:** Test systems
- **Tier-0:** Critical production systems
- **Tier-1:** Important production systems
- **Tier-2:** Standard systems
- **Tier-3:** Non-critical systems

### Linux Patch Management

**Tool:** Ansible / Satellite  
**Server:** {{ netbox.ansible.server }}

**Playbooks:**
- `patch-assessment.yml` - Check available updates
- `patch-security.yml` - Security updates only
- `patch-all.yml` - All updates
- `patch-rollback.yml` - Rollback

**Example Playbook:**
```yaml
---
- name: Patch Linux Servers
  hosts: linux_servers
  become: yes
  tasks:
    - name: Update package cache
      apt:
        update_cache: yes
      when: ansible_os_family == "Debian"
    
    - name: Install security updates
      apt:
        upgrade: safe
        autoremove: yes
      when: ansible_os_family == "Debian"
    
    - name: Check if reboot required
      stat:
        path: /var/run/reboot-required
      register: reboot_required
    
    - name: Reboot if required
      reboot:
        msg: "Reboot for security updates"
      when: reboot_required.stat.exists
```

### VMware Patch Management

**Tool:** VMware Update Manager (VUM)  
**Integration:** vCenter {{ netbox.vcenter.server }}

**Baseline Groups:**
- **Critical-Patches:** Critical security patches
- **Non-Critical-Patches:** All other patches
- **Upgrades:** ESXi upgrades

**Remediation Process:**
- Check baseline compliance
- Put hosts in maintenance mode
- Install patches
- Reboot hosts
- Verify compliance

### Vulnerability Scanner

**Tool:** {{ meta.vulnerability_scanner }}  
**Scan Frequency:** Weekly

**Scan Profiles:**
- **Full Scan:** All vulnerabilities
- **Patch Scan:** Missing patches only
- **Compliance Scan:** Compliance checks

**Integration:** SIEM, Ticketing System

## Rollback Procedures

### Rollback Triggers

**Rollback required when:**
- Critical functionality not available
- Performance degradation > 20%
- Data corruption
- Security issues caused by patch
- Business process failure

**Rollback Decision:** IT Operations Manager or higher

### Rollback Methods

#### Windows Rollback

**Method 1: Windows Uninstall**
```powershell
# Display patch list
Get-HotFix

# Uninstall patch
wusa /uninstall /kb:KBXXXXXX /quiet /norestart
```

**Method 2: System Restore**
- Restore point before patch installation
- Perform system recovery

**Method 3: Backup Restore**
- Restore VM snapshot
- Bare-metal restore

#### Linux Rollback

**Method 1: Package Downgrade**
```bash
# Ubuntu/Debian
apt-cache policy <package>
apt-get install <package>=<old-version>

# RHEL/CentOS
yum downgrade <package>
```

**Method 2: Snapshot Rollback**
- Restore LVM snapshot
- Restore VM snapshot

#### VMware Rollback

**Method:** VUM Rollback
- Undo baseline remediation
- Install previous patch version

### Rollback Process

1. **Make Rollback Decision**
   - Assess impact
   - Inform stakeholders

2. **Perform Rollback**
   - Select rollback method
   - Execute rollback
   - Restart system (if required)

3. **Verification**
   - Check functionality
   - Check performance
   - Check logs

4. **Documentation**
   - Document rollback reason
   - Lessons learned
   - Evaluate alternative solutions

## Compliance and Reporting

### Patch Compliance Metrics

| Metric | Target Value | Measurement |
|---|---|---|
| **Patch Compliance Rate** | > 95% | Patched systems / Total systems |
| **Critical Patch SLA** | > 95% | Patches in SLA / Total patches |
| **Mean Time to Patch (MTTP)** | < 30 days | Average patch duration |
| **Patch Success Rate** | > 98% | Successful patches / Total patches |
| **Rollback Rate** | < 2% | Rollbacks / Total patches |

### Patch Compliance Dashboard

**Metrics:**
- Patch status by system tier
- Open critical patches
- SLA compliance
- Patch trends (monthly)
- Top 10 vulnerabilities

**Tool:** {{ meta.patch_dashboard }}

**Access:** IT Management, Security Team

### Reporting

**Weekly Patch Status Report:**
- New patches available
- Patches in testing
- Planned deployments
- Open critical patches

**Monthly Patch Compliance Report:**
- Patch compliance rate
- SLA compliance
- Patch statistics
- Trend analysis
- Improvement measures

**Quarterly Management Report:**
- Patch management strategy review
- Risk assessment
- Compliance status
- Budget and resources

**Recipients:**
- Weekly: IT Operations Team
- Monthly: IT Management, Security Team
- Quarterly: CIO, CISO, Management

## Exceptions and Special Cases

### Patch Exceptions

**Reasons for Exceptions:**
- Vendor support ends (End-of-Life)
- Application incompatibility
- Business-critical systems (change freeze)
- Special vendor requirements

**Exception Process:**
1. Submit exception request
2. Conduct risk assessment
3. Define compensating measures
4. Obtain management approval
5. Document exception
6. Review regularly (quarterly)

**Exception Register:** {{ meta.exception_register }}

### End-of-Life Systems

**Strategy:**
- Plan migration
- Network segmentation
- Additional monitoring
- Compensating controls
- Document risk acceptance

**EOL Register:** {{ meta.eol_register }}

### Legacy Applications

**Challenges:**
- No patches available
- Incompatibility with new OS versions
- Vendor support discontinued

**Mitigations:**
- Virtualization/containerization
- Network isolation
- WAF/IPS in front of application
- Regular vulnerability scans
- Migration roadmap

## Roles and Responsibilities

### Patch Management Team

**Responsibilities:**
- Patch process ownership
- Vulnerability assessment
- Patch testing coordination
- Deployment planning
- Reporting

**Team Lead:** {{ meta.it_operations_manager.name }}

### System Administrators

**Responsibilities:**
- Perform patch deployment
- System monitoring
- Perform rollback
- Documentation

### Security Team

**Responsibilities:**
- Vulnerability scanning
- Risk assessment
- Security patch prioritization
- Compliance monitoring

**Lead:** {{ meta.ciso.name }}

### Application Owners

**Responsibilities:**
- Check application compatibility
- User acceptance tests
- Go/No-Go decision
- Business impact assessment

### Change Manager

**Responsibilities:**
- Approve change tickets
- Manage change calendar
- Stakeholder communication
- Post-implementation review

## Best Practices

### Patch Management Best Practices

1. **Regular Vulnerability Scans**
   - Weekly scans
   - Automated scans
   - Prioritization by risk

2. **Test Before Deployment**
   - Always test in test environment
   - Have rollback plan ready
   - Keep documentation current

3. **Phased Rollout**
   - Pilot group first
   - Gradual rollout
   - Monitoring during rollout

4. **Backup Before Patching**
   - Always create backup
   - Check backup integrity
   - Test restore procedure

5. **Communication**
   - Inform stakeholders early
   - Status updates during deployment
   - Post-deployment communication

6. **Documentation**
   - Document patch process
   - Record lessons learned
   - Maintain knowledge base

7. **Automation**
   - Automate patch deployment
   - Automate reporting
   - Automate compliance checks

8. **Continuous Improvement**
   - Review process regularly
   - Analyze metrics
   - Implement optimizations

## References

- NIST SP 800-40 Rev. 4 - Guide to Enterprise Patch Management Planning
- ISO/IEC 27002:2013 - Control 12.6.1 (Management of Technical Vulnerabilities)
- CIS Controls v8 - Control 7 (Continuous Vulnerability Management)
- ITIL v4 - Change Enablement Practice
- Vendor Patch Documentation (Microsoft, Red Hat, VMware)
- CVE Database: https://cve.mitre.org
- NVD Database: https://nvd.nist.gov

---

**Document Owner:** {{ meta.document.owner }}  
**Approved by:** {{ meta.document.approver }}  
**Version:** {{ meta.document.version }}  
**Classification:** {{ meta.document.classification }}  
**Last Update:** {{ meta.date }}
