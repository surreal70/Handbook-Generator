# Guideline: Security Baselines, Hardening and Configuration Changes

**Document-ID:** [FRAMEWORK]-0550
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

This guideline specifies the `0540_Policy_Configuration_and_Hardening.md` and defines:
- Security baselines for different system types
- Hardening processes and standards
- Configuration management and change control

**Scope:** All IT systems at **{{ meta-organisation.name }}**

## 2. Security Baselines

### 2.1 Windows Server

**Baseline Standard:** CIS Benchmark Level 1

**Core Requirements:**
- Disable local administrator accounts (except break-glass)
- Windows Firewall enabled
- Windows Defender enabled
- Automatic updates enabled
- SMBv1 disabled
- PowerShell logging enabled
- Audit policies configured

**Tools:**
- Group Policy Objects (GPOs)
- Microsoft Security Compliance Toolkit
- CIS-CAT Pro

### 2.2 Linux Server

**Baseline Standard:** CIS Benchmark Level 1

**Core Requirements:**
- Root login via SSH disabled
- SSH key-based authentication
- Firewall (iptables/firewalld) enabled
- SELinux/AppArmor enabled
- Automatic security updates
- Unnecessary services disabled
- Audit daemon (auditd) enabled

**Tools:**
- Ansible/Puppet for configuration management
- Lynis for security audits

### 2.3 Network Devices

**Baseline Standard:** Vendor best practices + CIS Benchmarks

**Core Requirements:**
- Default passwords changed
- SNMP v3 (or disabled)
- Unused ports disabled
- Management access only via dedicated VLAN
- Logging to SIEM
- NTP configured

### 2.4 Cloud Workloads

**Baseline Standard:** Cloud Security Posture Management (CSPM)

**Azure:**
- Azure Security Benchmark
- Microsoft Defender for Cloud recommendations

**AWS:**
- AWS Foundational Security Best Practices
- CIS AWS Foundations Benchmark

**GCP:**
- CIS Google Cloud Platform Foundation Benchmark

## 3. Hardening Process

### 3.1 Build Phase

**Golden Images:**
- Pre-configured, hardened images
- Regular updates (monthly)
- Automated builds (CI/CD)

**Process:**
1. Base image (vendor)
2. Apply hardening scripts
3. Security scan
4. Approval
5. Image repository

### 3.2 Deployment Phase

**Automation:**
- Infrastructure as Code (Terraform, ARM Templates)
- Configuration Management (Ansible, Puppet, Chef)
- Compliance checks before deployment

**Manual Steps:**
- Only for exceptions
- Documentation required
- Post-deployment verification

### 3.3 Maintenance Phase

**Regular Reviews:**
- Quarterly configuration audits
- Drift detection (deviations from baseline)
- Remediation of non-compliance

## 4. Configuration Management

### 4.1 Configuration Management Database (CMDB)

**System:** {{ meta-handbook.itsm_cmdb }}

**Documented Configurations:**
- System type and version
- Installed software
- Network configuration
- Security configuration
- Baseline version

### 4.2 Configuration Baselines

**Baseline Versions:**
- Major version: For significant changes
- Minor version: For smaller updates
- Patch version: For security fixes

**Example:** Windows-Server-Baseline v2.1.3

### 4.3 Drift Detection

**Monitoring:**
- Automatic scans (daily)
- Comparison with baseline
- Alerts for deviations

**Tools:**
- Microsoft Defender for Cloud (Azure)
- AWS Config (AWS)
- Chef InSpec, Ansible Tower

**Remediation:**
- Automatic correction (where possible)
- Manual correction with ticket
- Exception process (see Section 6)

## 5. Configuration Changes

### 5.1 Change Process

**All Configuration Changes Through Change Management:**
- Create change request (RFC)
- Security impact assessment
- Testing in dev/test
- CAB approval
- Implementation
- Verification

**Details:** See `0370_Guideline_Change_Management_with_Security_Approvals`

### 5.2 Emergency Changes

**For Critical Security Fixes:**
- Expedited process
- ECAB approval
- Retrospective documentation

### 5.3 Configuration Backup

**Before Each Change:**
- Backup of current configuration
- Versioning
- Rollback capability

**Retention:** {{ meta-handbook.retention_config_years }} years

## 6. Exceptions and Deviations

### 6.1 Exception Process

**Request:**
- Justification (business justification)
- Risk assessment
- Compensating controls
- Time limitation

**Approval:**
- CISO approval required
- Documentation in exception register
- Regular review (quarterly)

**Details:** See `0640_Policy_Exceptions_and_Risk_Waivers.md`

### 6.2 Legacy Systems

**For Systems That Cannot Meet Baseline:**
- Implement compensating controls
- Network isolation
- Enhanced monitoring
- Create migration plan

## 7. Compliance Monitoring

### 7.1 Automated Compliance Scanning

**Tools:**
- **Windows:** Microsoft Security Compliance Toolkit, CIS-CAT
- **Linux:** Lynis, OpenSCAP
- **Cloud:** Cloud Security Posture Management (CSPM)
- **Network:** Nessus, Qualys

**Frequency:**
- Critical systems: Weekly
- Standard systems: Monthly

### 7.2 Compliance Reporting

**Monthly Compliance Report:**
- Compliance rate per baseline
- Top non-compliance items
- Trend analysis
- Remediation status

**Target:** > 95% compliance

### 7.3 Audit Evidence

- Baseline documents
- Compliance scan reports
- Exception register
- Remediation tickets

## 8. Hardening Standards

### 8.1 Reference Standards

**Primary:**
- CIS Benchmarks (Center for Internet Security)
- DISA STIGs (Defense Information Systems Agency Security Technical Implementation Guides)
- Vendor best practices

**Secondary:**
- NIST Cybersecurity Framework
- BSI IT-Grundschutz

### 8.2 Baseline Documentation

**For Each Baseline:**
- Scope and applicability
- Configuration settings (detailed)
- Justification for each setting
- Test procedures
- Rollback procedures

**Location:** {{ meta-handbook.documentation_baseline_repo }}

## 9. Compliance and Audit

### 9.1 Metrics (KPIs)

| Metric | Target Value |
|--------|--------------|
| Baseline compliance rate | > 95% |
| Drift remediation time | < 7 days |
| Golden image currency | < 30 days |
| Exceptions with current review | 100% |

### 9.2 Audit Evidence

- Baseline documents
- Compliance scan reports
- Configuration backups
- Change records

## 10. References

### Internal Documents
- `0540_Policy_Configuration_and_Hardening.md`
- `0370_Guideline_Change_Management_with_Security_Approvals.md`
- `0640_Policy_Exceptions_and_Risk_Waivers.md`

### External Standards
- **ISO/IEC 27001:2022 Annex A.8.9** - Configuration management
- **CIS Benchmarks** - https://www.cisecurity.org/cis-benchmarks/
- **NIST SP 800-70** - Security Configuration Checklists

**Approved by:** {{ meta-organisation-roles.role_CISO }}, CISO  
**Next Review:** {{ meta-handbook.next_review }}

