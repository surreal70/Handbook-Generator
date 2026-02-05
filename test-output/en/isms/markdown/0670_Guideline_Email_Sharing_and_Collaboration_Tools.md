# Guideline: Email, Sharing and Collaboration Tools

**Document ID:** 0670  
**Document Type:** Guideline (detailed)  
**Related Policy:** 0660_Policy_Information_Transfer_and_Communication.md  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.5.14  
**Owner:** {{ meta.it_operations.manager }}  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** {{ meta.document.date }}

---

## 1. Purpose and Scope

This guideline implements `0660_Policy_Information_Transfer_and_Communication.md` and defines:
- Email security and usage
- File sharing and collaboration tools
- Secure communication channels

**Scope:** All communication tools at **AdminSend GmbH**

## 2. Email Security

### 2.1 Email System

**Platform:** {{ meta.email.system }} (e.g., Microsoft 365, Google Workspace)

**Security Features:**
- SPF, DKIM, DMARC configured
- TLS for transport encryption
- Anti-spam and anti-malware
- DLP (Data Loss Prevention)
- Email archiving

### 2.2 Email Usage

**Permitted Use:**
- Business communication
- Limited private use (max. 10 emails/day)
- Registration for business online services

**Prohibited Activities:**
- Sending confidential data without encryption
- Spam, chain emails
- Using private email for business purposes
- Automatic forwarding to external addresses

**Details:** See `0210_Guideline_Acceptable_Use_of_IT.md`

### 2.3 Email Encryption

**S/MIME:**
- Mandatory for confidential emails
- Certificates for all employees
- Automatic encryption with "Confidential" label

**Opportunistic TLS:**
- For all outgoing emails
- MTA-STS for known partners

**Details:** See `0270_Guideline_Key_Management_and_Encryption.md`

### 2.4 Phishing Protection

**Technical Controls:**
- Email gateway with anti-phishing
- Link rewriting and sandbox
- Attachment scanning
- DMARC enforcement

**User Training:**
- Phishing awareness training (annually)
- Phishing simulations (quarterly)
- Reporting button in email client

**Upon Phishing Suspicion:**
1. Do not open/click email
2. Report via reporting button
3. Delete email
4. IT Security reviews and responds

### 2.5 Email Archiving

**Automatic Archiving:**
- All business emails
- Retention: {{ meta.retention.email_years }} years
- Immutability (WORM)

**Access:**
- Users: Own emails
- Legal/Compliance: For eDiscovery
- Supervisors: With approval

**Details:** See `0590_Guideline_Records_Retention`

## 3. File Sharing

### 3.1 Approved Platforms

**Internal:**
- **File Server:** {{ netbox.device.fileserver }}
- **SharePoint/OneDrive:** {{ meta.collaboration.sharepoint }}
- **Teams/Slack:** {{ meta.collaboration.teams }}

**External (with customers/partners):**
- **Secure File Transfer:** {{ meta.filesharing.secure_platform }}
- **Only with encryption and password protection**

**Prohibited:**
- Private cloud services (private Dropbox, private Google Drive)
- WeTransfer, Filemail (without approval)
- USB drives for confidential data

### 3.2 Permissions

**Least Privilege:**
- Only required permissions
- Read-only where possible
- Time-limited shares

**External Shares:**
- Approval by data owner
- Password protection mandatory
- Set expiration date (max. 90 days)
- Logging of all access

### 3.3 DLP for File Sharing

**Automatic Controls:**
- Blocking confidential data on external shares
- Warning for large data volumes
- Alerts for unusual sharing patterns

## 4. Collaboration Tools

### 4.1 Microsoft Teams / Slack

**Approved Use:**
- Internal communication
- Project collaboration
- Video conferences

**Security Settings:**
- External guests only with approval
- DLP policies activated
- Retention policies configured
- Audit logging activated

**Prohibited Activities:**
- Sharing confidential data in public channels
- Using private accounts for business purposes
- Installing unapproved apps/bots

### 4.2 Video Conferences

**Approved Platforms:**
- **Internal:** {{ meta.collaboration.video }} (e.g., Teams, Zoom)
- **External:** Only approved platforms

**Security Settings:**
- Waiting room activated
- Password protection for meetings
- No recording without consent
- Screen sharing only for moderator

**Best Practices:**
- Use background blur
- Mute microphone when not speaking
- No confidential information in public meetings

### 4.3 Instant Messaging

**Approved Tools:**
- Microsoft Teams Chat
- Slack (Enterprise)

**Prohibited:**
- WhatsApp, Telegram for business communication
- Private messaging apps

**Retention:**
- Chat history: {{ meta.retention.chat_years }} years
- Compliance archiving

## 5. External Communication

### 5.1 Communication with Customers

**Channels:**
- Email (preferred)
- Phone
- Video conference
- Customer portal (if available)

**Confidential Information:**
- Encryption mandatory
- Use secure file transfer
- No confidential data via SMS/WhatsApp

### 5.2 Communication with Suppliers

**Requirements:**
- NDA before exchanging confidential information
- Approved communication channels
- Documentation of important communication

### 5.3 Social Media

**Business Use:**
- Only authorized accounts
- Follow social media guidelines
- No confidential information

**Private Use:**
- No impersonation of official company opinion
- Disclaimer for opinions
- No negative statements about company

**Details:** See `0210_Guideline_Acceptable_Use_of_IT.md`

## 6. Mobile Communication

### 6.1 Business Smartphones

**Configuration:**
- MDM enrollment mandatory
- Encryption enabled
- Remote wipe capability
- Approved apps only

**Usage:**
- Business emails and calendar
- Teams/Slack
- Business calls

### 6.2 BYOD

**Requirements:**
- Containerization (work profile)
- Separate apps for business/private
- MDM enrollment

**Details:** See `0510_Guideline_MDM_BringYourOwnDevice`

## 7. Data Loss Prevention (DLP)

### 7.1 DLP Policies

**For Email:**
- Blocking credit card numbers
- Warning for "Confidential" label external
- Blocking large attachments (> 25 MB)

**For File Sharing:**
- Blocking confidential data on external shares
- Warning for sharing with many people

**For Collaboration Tools:**
- Warning for posting confidential data in public channels

### 7.2 DLP Incidents

**Upon DLP Blocking:**
1. User receives warning
2. Incident ticket created
3. Security team reviews
4. If needed: Training or disciplinary measures

## 8. Compliance and Audit

### 8.1 Metrics (KPIs)

| Metric | Target Value |
|--------|--------------|
| Email Encryption (confidential) | 100% |
| Phishing Click Rate (simulation) | < 5% |
| DLP Incidents | < 10 per month |
| External Shares with Password | 100% |

### 8.2 Audit Evidence

- Email Archive
- File Sharing Logs
- DLP Incident Reports
- Phishing Simulation Results

## 9. References

### Internal Documents
- `0660_Policy_Information_Transfer_and_Communication.md`
- `0210_Guideline_Acceptable_Use_of_IT.md`
- `0270_Guideline_Key_Management_and_Encryption.md`

### External Standards
- **ISO/IEC 27001:2022 Annex A.5.14** - Information transfer
- **NIST SP 800-177** - Trustworthy Email

---

**Approved by:** Thomas Weber, CISO  
**Next Review:** {{ meta.document.next_review }}
