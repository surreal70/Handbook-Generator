# Guideline: MDM, Bring Your Own Device and Remote Access

**Document-ID:** [FRAMEWORK]-0510
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

This guideline specifies the `0500_Policy_Mobile_Device_and_Remote_Work.md` and defines:
- Mobile Device Management (MDM) requirements
- BYOD guidelines and processes
- Remote access controls

**Scope:** All mobile devices and remote access at **{{ meta-organisation.name }}**

## 2. Mobile Device Management (MDM)

### 2.1 MDM System

**Platform:** {{ meta.mdm.system }} (e.g., Microsoft Intune, Jamf, MobileIron)

**Managed Devices:**
- Corporate-owned smartphones and tablets
- BYOD devices with corporate access
- Laptops (optional, depending on MDM capability)

### 2.2 MDM Enrollment

**Process:**
1. Receive device or BYOD request approved
2. Install MDM app
3. Perform enrollment
4. Pass compliance checks
5. Corporate access activated

**Mandatory Enrollment:**
- All corporate-owned devices
- All BYOD devices with email access or corporate apps

### 2.3 MDM Policies

**Enforced Settings:**
- Device encryption enabled
- PIN/passcode (min. 6 characters) or biometrics
- Automatic screen lock (5 minutes)
- OS updates within 30 days
- Jailbreak/root detection

**Prohibited Activities:**
- Jailbreak or rooting
- Installation from unknown sources
- Disabling security features

### 2.4 Compliance Checks

**Automatic Checks:**
- OS version current?
- Encryption active?
- Jailbreak/root detected?
- Malware detected?

**For Non-Compliance:**
- Warning to user (24-hour deadline)
- Restricted access
- Complete block after 7 days

## 3. BYOD (Bring Your Own Device)

### 3.1 BYOD Authorization

**Prerequisites:**
- Request via self-service portal
- Approval by supervisor
- Sign BYOD agreement
- MDM enrollment

**Eligible Devices:**
- Smartphones (iOS, Android)
- Tablets (iOS, Android)
- Laptops (case-by-case review)

### 3.2 BYOD Agreement

**Contents:**
- Terms of use
- Security requirements
- MDM enrollment requirement
- Remote wipe consent
- Data protection (separation private/business)
- Liability for loss

### 3.3 Containerization

**Technology:**
- Separate containers for business data
- Encrypted containers
- No mixing private/business

**Examples:**
- iOS: Managed Apps
- Android: Work Profile
- Windows: Windows Information Protection (WIP)

### 3.4 BYOD Offboarding

**At Contract End or BYOD Termination:**
1. Remote wipe of business container
2. Removal of corporate apps
3. Revocation of certificates
4. MDM unenrollment
5. Private data remains intact

## 4. Remote Access

### 4.1 VPN Access

**VPN System:** {{ meta.network.vpn_solution }}

**Requirements:**
- Multi-factor authentication (MFA)
- Endpoint compliance check before connection
- Split tunneling prohibited (full tunnel)
- Session timeout: 8 hours

**VPN Clients:**
- Corporate-approved clients
- Automatic updates
- Kill switch enabled

### 4.2 Zero Trust Network Access (ZTNA)

**Principles:**
- Never Trust, Always Verify
- Least Privilege Access
- Micro-segmentation

**Implementation:**
- Identity-based access control
- Device posture checks
- Continuous authentication

### 4.3 Remote Desktop

**Technologies:**
- RDP over VPN (Windows)
- SSH over VPN (Linux)
- Citrix/VMware Horizon (Virtual Desktops)

**Security Controls:**
- MFA for remote desktop
- Session recording (privileged access)
- Idle timeout: 30 minutes

## 5. Remote Work Security

### 5.1 Home Office Requirements

**Network:**
- Secure Wi-Fi (WPA3 or WPA2)
- No public Wi-Fi without VPN
- Router firmware current

**Workspace:**
- Private workspace (no third-party visibility)
- Screen lock when absent
- No use by family members

### 5.2 Public Places

**Allowed with Restrictions:**
- Work in cafes, airports, hotels
- VPN mandatory
- Privacy screen for laptop
- No confidential conversations

**Prohibited:**
- Public computers (internet cafes)
- Unsecured Wi-Fi without VPN
- Unattended device

### 5.3 Travel

**International Travel:**
- Report to IT Security (high-risk countries)
- Travel laptop without confidential data
- Encryption mandatory
- No use of local USB drives

## 6. Mobile Application Management (MAM)

### 6.1 Approved Apps

**Corporate Apps:**
- Email ({{ meta.email.mobile_app }})
- Collaboration ({{ meta.collaboration.mobile_app }})
- VPN client
- Authenticator app

**Approval Process:**
- Request via IT portal
- Security review
- Approval by IT Security

### 6.2 App Wrapping

**For Corporate-Owned Apps:**
- MDM policies integrated into app
- Enforce encryption
- Copy/paste control

## 7. Incident Response

### 7.1 Device Loss

**Immediate Actions:**
1. Report to IT Support ({{ meta.support.phone }})
2. Trigger remote wipe (within 1 hour)
3. Change passwords
4. Create incident ticket
5. Police report (in case of theft)

### 7.2 Compromise

**For Suspected Malware:**
1. Disconnect device from network
2. Inform IT Security
3. Forensic analysis (if required)
4. Rebuild device
5. Lessons learned

## 8. Compliance and Audit

### 8.1 Metrics (KPIs)

| Metric | Target Value |
|--------|--------------|
| MDM enrollment rate | 100% |
| Compliance rate | > 95% |
| OS update rate (30 days) | > 90% |
| Remote wipe success rate | 100% |

### 8.2 Audit Evidence

- MDM enrollment logs
- Compliance reports
- BYOD agreements
- Remote access logs

## 9. References

### Internal Documents
- `0500_Policy_Mobile_Device_and_Remote_Work.md`
- `0250_Guideline_MFA_Password_Rules_and_Session_Management.md`

### External Standards
- **ISO/IEC 27001:2022 Annex A.6.7** - Remote working
- **ISO/IEC 27001:2022 Annex A.8.9** - Configuration management
- **NIST SP 800-124** - Guidelines for Managing the Security of Mobile Devices

**Approved by:** {{ meta.ciso.name }}, CISO  
**Next Review:** {{ meta-handbook.next_review }}

