# Policy: Mobile Device and Remote Work

**Document-ID:** [FRAMEWORK]-0500
**Organisation:** AdminSend GmbH
**Owner:** [TODO]
**Approved by:** [TODO]
**Revision:** [TODO]
**Author:** Handbook-Generator
**Status:** Draft
**Classification:** Internal
**Last Update:** [TODO]
**Template Version:** [TODO]

---

---



**Document ID:** 0500  
**Document Type:** Policy (abstract)  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.6.7, A.6.8, A.8.9 (incl. Amendment 1:2024)  
**Owner:** [TODO]  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** [TODO]  
**Next Review:** [TODO]

## 1. Purpose

This policy defines the principles for Mobile Device Management and Remote Work at **AdminSend GmbH**. It ensures that mobile devices and remote access are securely managed and comply with the organization's security requirements.

## 2. Scope

This policy applies to:

- **Organizational Units:** All departments and locations of AdminSend GmbH
- **Devices:** Laptops, smartphones, tablets, wearables (corporate-owned and BYOD)
- **Access Methods:** VPN, Remote Desktop, cloud services, mobile apps
- **Persons:** All employees, contractors with remote access
- **Locations:** [[ netbox.site.name ]], home office, public places, travel

**Exceptions:** Exceptions are only permitted through the defined exception process (`0640_Policy_Exceptions_and_Risk_Waivers.md`).

## 3. Principles (Policy Statements)

### 3.1 Mobile Device Management (MDM)
All mobile devices with access to corporate resources are managed through an MDM system. MDM enables configuration, monitoring, and remote wipe.

### 3.2 BYOD (Bring Your Own Device)
Personal devices may only be used for business purposes after approval and enrollment in MDM. BYOD devices are subject to the same security requirements as corporate devices.

### 3.3 Device Encryption
All mobile devices must be fully encrypted (Full Disk Encryption). Encryption is enforced and monitored through MDM.

### 3.4 Secure Remote Access
Remote access to corporate resources is exclusively through secure channels:
- VPN with multi-factor authentication
- Zero Trust Network Access (ZTNA)
- Secure remote desktop solutions

### 3.5 Device Compliance
Mobile devices must meet compliance requirements:
- Current operating system version
- Installed security updates
- Enabled screen lock
- No jailbreak/root
- Installed endpoint security software

### 3.6 Lost/Stolen Device Response
In case of loss or theft of mobile devices, an incident is immediately reported. Remote wipe is performed to prevent data loss.

### 3.7 Public Wi-Fi and Network Security
Use of public Wi-Fi networks is only permitted via VPN. Unencrypted connections to corporate resources are prohibited.

### 3.8 Remote Work Security
Remote workspaces must meet security requirements:
- Secure network connection
- Physical security (screen lock, clear desk)
- No sharing of credentials
- Compliance with Acceptable Use Policy

## 4. Roles and Responsibilities

### RACI Matrix: Mobile Device and Remote Work

| Activity | CISO | IT Operations | MDM Administrator | Employee | HR |
|----------|------|---------------|-------------------|----------|-----|
| Policy Creation | R/A | C | C | I | C |
| MDM Operations | A | R | R | I | I |
| Device Enrollment | I | C | R | R/A | I |
| Compliance Monitoring | A | C | R | I | I |
| Lost Device Response | A | R | R | R | C |
| Remote Access Provisioning | C | R/A | C | I | I |
| Security Training | A | I | I | R | R |

**Legend:** R = Responsible (Execution), A = Accountable (Ownership), C = Consulted, I = Informed

### Key Roles

- **Policy Owner:** [TODO] (CISO)
- **MDM Administrator:** {{ meta-handbook.it_mdm_admin }}
- **Remote Access Manager:** {{ meta-handbook.it_remote_access_manager }}
- **Implementation Responsible:** IT Operations, Employees
- **Control/Audit Function:** ISMS, Internal Audit

## 5. Derivatives (Guidelines/Standards/Processes)

Implementation details are defined in subordinate documents:

### Associated Guidelines
- **0510_Guideline_MDM_BringYourOwnDevice_and_Remote_Access.md** - Detailed implementation guideline
- `0200_Policy_Acceptable_Use_of_IT.md` - Acceptable Use Policy
- `0240_Policy_Authentication_and_Passwords.md` - Authentication Policy
- `0620_Policy_Endpoint_Security.md` - Endpoint Security Policy

### Associated Standards/Baselines
- MDM configuration standards
- Device compliance requirements
- BYOD guideline
- Remote access standards

### Associated Processes
- Device enrollment process
- Lost/stolen device response process
- Remote access provisioning process
- BYOD approval process

## 6. Compliance, Monitoring and Enforcement

### Metrics and KPIs
- MDM enrollment rate (Target: 100% of mobile devices)
- Device compliance rate (Target: 95%)
- Number of non-compliant devices
- Average time to remote wipe for lost devices
- VPN usage rate for remote work
- Number of lost/stolen device incidents

### Evidence and Proof
- MDM enrollment status
- Device compliance reports
- Remote access logs
- Lost device incident reports
- BYOD approval documentation
- Security training evidence

### Consequences of Violations
Violations of this policy are handled according to applicable HR and compliance processes:
- **Non-enrolled Devices:** Access block, enrollment requirement
- **Non-Compliance:** Access restriction until remediation
- **Unreported Device Loss:** Investigation, disciplinary action
- **Repeated Violations:** Employment consequences

## 7. Exceptions

Exceptions to this policy are only permitted in justified exceptional cases:

- **Exception Process:** See `0640_Policy_Exceptions_and_Risk_Waivers.md`
- **Approval:** Exceptions must be approved by CISO
- **Documentation:** All exceptions are documented in the risk register
- **Time Limitation:** Exceptions are generally time-limited
- **Compensating Controls:** Exceptions require alternative security measures

## 8. References

### Internal Documents
- `0010_ISMS_Information_Security_Policy.md` - ISMS Policy
- `0510_Guideline_MDM_BringYourOwnDevice_and_Remote_Access.md` - Detailed Guideline
- `0620_Policy_Endpoint_Security.md` - Endpoint Security Policy
- `0080_ISMS_Risk_Register_Template.md` - Risk Register

### External Standards and Requirements
- **ISO/IEC 27001:2022 Annex A.6.7** - Remote working
- **ISO/IEC 27001:2022 Annex A.6.8** - Information security event reporting
- **ISO/IEC 27001:2022 Annex A.8.9** - Configuration management
- **NIST SP 800-46** - Guide to Enterprise Telework, Remote Access, and BYOD Security
- **GDPR (EU 2016/679)** - Data protection for BYOD and remote work

**Approved by:**  
{{ meta-handbook.management_ceo }}, Management  
Date: [TODO]

**Next Review:** [TODO] (annually or as needed)

