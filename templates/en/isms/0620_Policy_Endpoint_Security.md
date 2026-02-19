# Policy: Endpoint Security

**Document-ID:** [FRAMEWORK]-0620
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

<!-- 
TEMPLATE AUTHOR NOTE:
This policy establishes requirements for endpoint security and device protection.
It ensures that all endpoints (workstations, laptops, mobile devices) are properly secured.
Customize based on your organization's endpoint landscape and security requirements.

ISO 27001:2022 Annex A Reference: A.8.1, A.8.2, A.8.3, A.6.7
-->

**Document ID:** 0620  
**Document Type:** Policy (abstract)  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.8.1-A.8.3, A.6.7 (incl. Amendment 1:2024)  
**Owner:** {{ meta-organisation-roles.role_CISO }}  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** {{ meta-handbook.modifydate }}  
**Next Review:** {{ meta-handbook.next_review }}

## 1. Purpose

This policy defines the endpoint security requirements of **{{ meta-organisation.name }}**. It ensures that all endpoint devices (workstations, laptops, mobile devices) are appropriately secured and protected against threats.

## 2. Scope

This policy applies to:

- **Organizational Units:** All departments and locations of {{ meta-organisation.name }}
- **Devices:** All endpoint devices (workstations, laptops, tablets, smartphones)
- **Operating Systems:** Windows, macOS, Linux, iOS, Android
- **Ownership:** Company-owned and BYOD devices (with corporate access)
- **Locations:** [[ netbox.site.name ]] and all other operational sites, remote work

**Exceptions:** Exceptions are only permitted through the defined exception process (`0640_Policy_Exceptions_and_Risk_Waivers.md`).

## 3. Policy Statements

### 3.1 Endpoint Protection Platform (EPP)
All endpoint devices are equipped with endpoint protection. EPP includes antivirus, anti-malware, host firewall, and application control.

### 3.2 Endpoint Detection and Response (EDR)
Critical endpoint devices are equipped with EDR solution. EDR enables advanced threat detection, incident response, and forensics.

### 3.3 Device Compliance
Endpoint devices must meet compliance requirements:
- Current operating system version
- Current security patches
- EPP/EDR installed and active
- Disk encryption enabled
- Screen lock configured

### 3.4 Disk Encryption
All endpoint devices with corporate data are encrypted (full disk encryption). Encryption protects against data loss in case of theft or loss.

### 3.5 Host-based Firewall
All endpoint devices have an enabled host firewall. Firewall rules follow the least privilege principle.

### 3.6 Application Control
Unauthorized applications are blocked (application whitelisting or blacklisting). Application control reduces malware risk.

### 3.7 Patch Management
Endpoint devices are patched regularly. Security patches are installed promptly (see `0340_Policy_Vulnerability_and_Patch_Management.md`).

### 3.8 Remote Wipe
Lost or stolen devices can be remotely wiped. Remote wipe protects against data loss.

### 3.9 BYOD (Bring Your Own Device)
BYOD devices with corporate access must meet minimum security requirements. BYOD is managed via MDM/MAM (see `0500_Policy_Mobile_Device_and_Remote_Work.md`).

## 4. Roles and Responsibilities

### RACI Matrix: Endpoint Security

| Activity | CISO | Endpoint Security | IT Operations | SOC | End User |
|----------|------|-------------------|---------------|-----|----------|
| Policy Creation | R/A | R | C | C | I |
| EPP/EDR Deployment | C | R/A | R | C | I |
| Device Compliance | C | R/A | R | C | R |
| Disk Encryption | C | R/A | R | I | C |
| Patch Management | C | R | R/A | I | C |
| Remote Wipe | C | R/A | C | C | I |
| BYOD Management | C | R/A | R | I | R |
| Incident Response | C | R | C | R/A | I |

**Legend:** R = Responsible (Execution), A = Accountable (Ownership), C = Consulted, I = Informed

### Key Roles

- **Policy Owner:** {{ meta-organisation-roles.role_CISO }} (CISO)
- **Endpoint Security Manager:** {{ meta-handbook.endpoint_security_manager }}
- **IT Operations Manager:** {{ meta-handbook.it_operations_manager }}
- **SOC Manager:** {{ meta-handbook.soc_manager }}
- **Implementation Responsible:** IT Operations, End Users
- **Control/Audit Function:** ISMS, Internal Audit, SOC

## 5. Derived Documents (Guidelines/Standards/Processes)

Implementation details are defined in subordinate documents:

### Related Guidelines
- **0630_Guideline_EDR_AV_Host_Firewall_and_Device_Compliance.md** - Detailed implementation guideline
- `0500_Policy_Mobile_Device_and_Remote_Work.md` - Mobile Device Policy
- `0340_Policy_Vulnerability_and_Patch_Management.md` - Patch Management Policy
- `0260_Policy_Cryptography_and_Key_Management.md` - Encryption Policy

### Related Standards/Baselines
- Endpoint Security Baseline (Windows, macOS, Linux)
- EPP/EDR Configuration
- Device Compliance Requirements
- Disk Encryption Standards
- Application Whitelist/Blacklist

### Related Processes
- Endpoint Onboarding/Offboarding
- Device Compliance Monitoring
- EPP/EDR Alert Response
- Remote Wipe Process
- BYOD Enrollment

## 6. Compliance, Monitoring and Enforcement

### Metrics and KPIs
- EPP/EDR Coverage (Target: 100% of all endpoints)
- Device Compliance Rate (Target: >95%)
- Disk Encryption Coverage (Target: 100%)
- Patch Compliance (Target: >95% within SLA)
- EPP/EDR Detection Rate
- Average Incident Response Time (Target: < 30 minutes)
- Number of Remote Wipes

### Evidence and Proof
- Endpoint Inventory
- EPP/EDR Deployment Status
- Device Compliance Reports
- Disk Encryption Status
- Patch Compliance Reports
- EPP/EDR Logs and Alerts
- Remote Wipe Logs

### Consequences of Violations
Violations of this policy are handled according to applicable HR and compliance processes:
- **Non-compliant Devices:** Network access blocked until compliance is established
- **Disabled EPP/EDR:** Immediate reactivation, incident response
- **Missing Disk Encryption:** Remediation, access restriction
- **Repeated Violations:** Employment consequences, device usage prohibited

## 7. Exceptions

Exceptions to this policy are only permitted in justified exceptional cases:

- **Exception Process:** See `0640_Policy_Exceptions_and_Risk_Waivers.md`
- **Approval:** Exceptions must be approved by CISO and Endpoint Security Manager
- **Documentation:** All exceptions are documented in the risk register
- **Time Limitation:** Exceptions are generally time-limited

## 8. References

### Internal Documents
- `0010_ISMS_Information_Security_Policy.md` - ISMS Policy
- `0630_Guideline_EDR_AV_Host_Firewall_and_Device_Compliance.md` - Detailed Guideline
- `0500_Policy_Mobile_Device_and_Remote_Work.md` - Mobile Device Policy
- `0080_ISMS_Risk_Register_Template.md` - Risk Register

### External Standards and Regulations
- **ISO/IEC 27001:2022 Annex A.8.1** - User endpoint devices
- **ISO/IEC 27001:2022 Annex A.8.2** - Privileged access rights
- **ISO/IEC 27001:2022 Annex A.8.3** - Information access restriction
- **ISO/IEC 27001:2022 Annex A.6.7** - Remote working
- **NIST SP 800-124** - Guidelines for Managing the Security of Mobile Devices
- **NIST SP 800-171** - Protecting Controlled Unclassified Information
- **CIS Controls v8** - Control 4 (Secure Configuration of Enterprise Assets)

**Approved by:**  
{{ meta-handbook.management_ceo }}, Executive Management  
Date: {{ meta-handbook.modifydate }}

**Next Review:** {{ meta-handbook.next_review }} (annually or as needed)

