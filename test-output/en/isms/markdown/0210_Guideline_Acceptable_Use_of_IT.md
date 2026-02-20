# Guideline: Acceptable Use of IT

**Document-ID:** ISMS-0210
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



**Document ID:** 0210  
**Document Type:** Guideline (detailed)  
**Related Policy:** 0200_Policy_Acceptable_Use_of_IT.md  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.5.10  
**Owner:** {{ meta-handbook.it_operations_manager }}  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** [TODO]  
**Next Review:** [TODO]

## 1. Purpose and Scope

This guideline implements the `0200_Policy_Acceptable_Use_of_IT.md` and defines detailed rules, procedures, and technical controls for the acceptable use of IT resources at **AdminSend GmbH**.

**Scope:**
- All employees, contractors, and third parties with access to IT resources
- All IT systems, networks, applications, and devices
- Locations: [[ netbox.site.name ]] and all operational sites

## 2. Detailed Usage Rules

### 2.1 Email Usage

**Permitted Use:**
- Business communication with customers, partners, and colleagues
- Limited personal use (max. 10 emails per day, no large attachments)
- Registration for business online services

**Prohibited Activities:**
- Sending spam, chain letters, or unsolicited mass emails
- Sending confidential information without encryption
- Using personal email accounts for business communication
- Opening suspicious attachments or links (see phishing awareness)
- Automatic forwarding of business emails to external addresses

**Technical Controls:**
- Email filtering and anti-spam systems
- DLP (Data Loss Prevention) for outgoing emails
- Email archiving for compliance (retention: {{ meta-handbook.retention_email_years }} years)
- Encryption for confidential emails (S/MIME or PGP)

### 2.2 Internet Usage

**Permitted Use:**
- Research for business purposes
- Access to approved cloud services and SaaS applications
- Limited personal use during breaks (max. 30 minutes per day)
- Access to professional portals, documentation, and training resources

**Prohibited Activities:**
- Access to illegal, pornographic, or violence-glorifying content
- Downloading unapproved software or files
- Streaming videos/music during work hours (except for business purposes)
- Using anonymization services (VPN, proxy) without approval
- Online shopping, gambling, or private business activities

**Technical Controls:**
- Web filtering and URL categorization
- Blocking known malware and phishing sites
- Bandwidth management for streaming services
- Logging and monitoring of internet usage
- SSL inspection for encrypted traffic (with data protection compliance)

### 2.3 Software Installation and Usage

**Permitted Activities:**
- Using approved software from the software catalog
- Software installation by IT operations or via self-service portal
- Using browser extensions from approved whitelist

**Prohibited Activities:**
- Installing unapproved software (shadow IT)
- Using pirated or unlicensed software
- Installing peer-to-peer software (torrents, file sharing)
- Disabling or bypassing security software (antivirus, EDR)
- Changing system configurations without approval

**Technical Controls:**
- Application whitelisting (only approved software can execute)
- Software Asset Management (SAM) for license compliance
- Endpoint protection (antivirus, EDR) with tamper protection
- Regular software inventory
- Patch management for approved software

### 2.4 Data Handling and Storage

**Permitted Activities:**
- Storing business data on approved network drives and cloud storage
- Using {{ meta-handbook.cloud_storage_service }} for file storage
- Encrypting confidential data according to classification

**Prohibited Activities:**
- Storing business data on personal cloud services (Dropbox, personal Google Drive)
- Storing confidential data on local hard drives without encryption
- Sharing access credentials or passwords
- Exfiltrating large amounts of data without approval

**Technical Controls:**
- DLP (Data Loss Prevention) for data transfer monitoring
- Hard drive encryption (BitLocker, FileVault)
- Cloud Access Security Broker (CASB) for cloud service monitoring
- Network segmentation for sensitive data
- Backup and retention per `0420_Policy_Backup_und_Wiederherstellung.md`

### 2.5 Mobile Devices and BYOD

**Permitted Activities:**
- Using company-owned mobile devices for business purposes
- BYOD (Bring Your Own Device) after registration and MDM enrollment
- Accessing approved enterprise applications via mobile apps

**Prohibited Activities:**
- Jailbreaking or rooting devices
- Installing unapproved apps on BYOD devices with enterprise access
- Storing confidential data on personal devices without container
- Using insecure WiFi networks without VPN

**Technical Controls:**
- Mobile Device Management (MDM) for all devices with enterprise access
- Containerization for business data on BYOD devices
- Remote wipe in case of loss or theft
- Enforced encryption and PIN/biometrics
- Compliance checks (OS version, jailbreak detection)

**Details:** See `0500_Policy_Mobile_Device_und_Remote_Work.md`

### 2.6 Social Media and External Communication

**Permitted Activities:**
- Using social media for marketing and corporate communication (authorized accounts)
- Professional use of LinkedIn, Xing for networking
- Participation in professional forums and communities (with disclaimer)

**Prohibited Activities:**
- Publishing confidential company information
- Negative statements about company, customers, or colleagues
- Pretending to represent official company opinion without authorization
- Using company logos without approval

**Guidelines:**
- Social media guidelines for employees
- Approval process for official company accounts
- Training on social engineering and phishing via social media

### 2.7 Remote Work and VPN Usage

**Permitted Activities:**
- Remote access via approved VPN connections
- Using remote desktop (RDP, Citrix) for system access
- Working from home office after approval

**Prohibited Activities:**
- Using insecure networks without VPN
- Sharing VPN credentials
- Working in public areas with screen visibility (shoulder surfing)
- Using personal devices without MDM enrollment

**Technical Controls:**
- VPN with multi-factor authentication (MFA)
- Zero Trust Network Access (ZTNA) for granular access control
- Endpoint compliance checks before VPN access
- Session timeouts and idle disconnects

**Details:** See `0500_Policy_Mobile_Device_und_Remote_Work.md`

## 3. Monitoring and Surveillance

### 3.1 Monitoring Scope

The organization monitors the following activities to ensure security and compliance:

- **Email Traffic:** Metadata (sender, recipient, subject), DLP scans
- **Internet Usage:** Visited URLs, categories, bandwidth usage
- **File Transfers:** Uploads/downloads, cloud service usage
- **System Access:** Login activities, privileged access
- **Application Usage:** Used applications, usage duration

### 3.2 Data Protection and Privacy

**Principles:**
- Monitoring is purpose-bound for security and compliance
- No indiscriminate monitoring of individual employees
- Monitoring data is only analyzed with justified suspicion
- Compliance with GDPR and works council agreements

**Transparency:**
- Employees are informed about monitoring measures (onboarding, training)
- Works council is involved in monitoring measures
- Data protection officer reviews monitoring concepts

### 3.3 Incident Response for Violations

**Process:**
1. **Detection:** Automatic alerts for policy violations (DLP, web filter, SIEM)
2. **Triage:** IT security reviews alert and assesses severity
3. **Investigation:** With justified suspicion: detailed analysis, HR involvement
4. **Measures:** Depending on severity: warning, training, disciplinary action
5. **Documentation:** Incident report, lessons learned

**Escalation:**
- Minor violations: IT operations informs supervisor
- Medium violations: CISO and HR are involved
- Severe violations: Management, legal, possibly law enforcement

## 4. Training and Awareness

### 4.1 Mandatory Training

**Onboarding:**
- Acceptable Use Policy training (1 hour)
- Phishing awareness training
- Data protection basics

**Annual Refresher:**
- Acceptable Use Policy refresher (30 minutes)
- Current threats and best practices
- Quiz for knowledge verification (passing threshold: 80%)

### 4.2 Awareness Campaigns

**Regular Measures:**
- Monthly security newsletters
- Phishing simulations (quarterly)
- Posters and infographics on security topics
- Lunch & Learn sessions on current topics

### 4.3 Documentation

**Evidence:**
- Training participation tracking in LMS (Learning Management System)
- Policy acknowledgment confirmations (annual)
- Quiz results and certificates
- Phishing simulation results

## 5. Exceptions and Special Cases

### 5.1 Exception Process

**Request:**
- Form: Exception request with justification and risk assessment
- Approval: CISO (for technical exceptions), HR (for usage exceptions)
- Time limit: Max. 12 months, then re-evaluation

**Examples of Exceptions:**
- Installing special software for projects
- Extended internet access for research
- Using personal devices without MDM (temporary)

**Documentation:** See `0640_Policy_Ausnahmen_und_Risk_Waivers.md`

### 5.2 Privileged Users

**Administrators and IT Operations:**
- Extended rights for system administration
- Additional training and background checks
- Increased monitoring of privileged activities
- Four-eyes principle for critical changes

**Details:** See `0230_Richtlinie_IAM_Joiner_Mover_Leaver_und_Zugriffsantraege.md`

## 6. Technical Implementation

### 6.1 Technology Stack

**Security Tools:**
- **Web Filter:** {{ meta-handbook.security_web_filter }} (e.g., Cisco Umbrella, Zscaler)
- **Email Security:** {{ meta-handbook.security_email_gateway }} (e.g., Proofpoint, Mimecast)
- **DLP:** {{ meta-handbook.security_dlp_solution }} (e.g., Microsoft Purview, Symantec DLP)
- **Endpoint Protection:** {{ meta-handbook.security_edr_solution }} (e.g., CrowdStrike, SentinelOne)
- **CASB:** {{ meta-handbook.security_casb_solution }} (e.g., Microsoft Defender for Cloud Apps)

**Monitoring and Logging:**
- **SIEM:** {{ meta-handbook.security_siem_solution }} (e.g., Splunk, Microsoft Sentinel)
- **Log Retention:** {{ meta-handbook.retention_log_years }} years for security logs
- **Alerting:** Automatic alerts for critical violations

### 6.2 Configuration Examples

**Web Filter Categories (blocked):**
- Adult Content, Gambling, Illegal Drugs
- Malware, Phishing, Command & Control
- Anonymizers, Proxy Avoidance
- Peer-to-Peer, File Sharing (except approved services)

**DLP Rules:**
- Blocking credit card numbers in emails
- Warning when sending documents with "Confidential" classification
- Blocking uploads to unapproved cloud services
- Detection of PII (Personally Identifiable Information) in file transfers

**Application Whitelisting:**
- Only signed applications from approved catalog
- Blocking PowerShell/CMD for standard users
- Exceptions for developers and administrators

## 7. Compliance and Audit

### 7.1 Key Performance Indicators (KPIs)

| Metric | Target Value | Measurement |
|--------|--------------|-------------|
| Training Participation | 100% annually | LMS reports |
| Policy Violations | < 5 per month | SIEM alerts |
| Phishing Click Rate | < 5% | Simulation results |
| Unapproved Software | 0 installations | Software inventory |
| DLP Incidents | < 10 per month | DLP reports |

### 7.2 Audit Evidence

**Documentation:**
- Policy documents and version history
- Training evidence and confirmations
- Monitoring logs and incident reports
- Exception register
- Audit trails for access and changes

**Audit Frequency:**
- Internal audits: Annually
- External audits: For ISO 27001 certification
- Ad-hoc audits: In case of suspected violations

## 8. Review and Updates

**Review Cycle:**
- Annual review by CISO and IT operations
- Ad-hoc updates for new threats or technologies
- Involvement of HR and legal for changes

**Change Management:**
- Changes are managed through change process
- Communication to all employees for significant changes
- Update of training materials

## 9. References

### Internal Documents
- `0200_Policy_Acceptable_Use_of_IT.md` - Parent policy
- `0220_Policy_Zugriffssteuerung_und_Identitaetsmanagement.md` - Access control
- `0320_Policy_Logging_und_Monitoring.md` - Logging policy
- `0400_Policy_Incident_Management.md` - Incident management
- `0500_Policy_Mobile_Device_und_Remote_Work.md` - Mobile device policy
- `0640_Policy_Ausnahmen_und_Risk_Waivers.md` - Exception process

### External Standards
- **ISO/IEC 27001:2022 Annex A.5.10** - Acceptable use of information
- **ISO/IEC 27002:2022** - Information security controls
- **GDPR (EU 2016/679)** - General Data Protection Regulation
- **Works Constitution Act (BetrVG)** - Co-determination in monitoring

**Approved by:**  
[TODO], CISO  
Date: [TODO]

**Next Review:** [TODO]

