# Policy: Information Transfer and Communication

**Document-ID:** [FRAMEWORK]-0660
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



**Document ID:** 0660  
**Document Type:** Policy (abstract)  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.5.14, A.8.24, A.8.26 (incl. Amendment 1:2024)  
**Owner:** [TODO]  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** [TODO]  
**Next Review:** [TODO]

## 1. Purpose

This policy defines the requirements for secure information transfer and communication of **AdminSend GmbH**. It ensures that information is appropriately protected during transmission and that communication channels are secure.

## 2. Scope

This policy applies to:

- **Organizational Units:** All departments and locations of AdminSend GmbH
- **Communication Channels:** Email, messaging, file sharing, collaboration tools
- **Data:** All information (especially confidential and personal data)
- **Transmission Paths:** Internal, external, cloud, partners
- **Locations:** [[ netbox.site.name ]] and all other operational sites

**Exceptions:** Exceptions are only permitted through the defined exception process (`0640_Policy_Exceptions_and_Risk_Waivers.md`).

## 3. Policy Statements

### 3.1 Encrypted Transmission
Confidential information is transmitted encrypted. Encryption occurs in transit (TLS/SSL) and at rest.

### 3.2 Email Security
Email communication is secured:
- **Inbound:** SPF, DKIM, DMARC, anti-spam, anti-malware
- **Outbound:** TLS encryption, S/MIME or PGP for confidential content
- **Phishing Protection:** User awareness, technical protection measures

### 3.3 Secure File Sharing
File sharing occurs via approved platforms. Confidential files are shared encrypted. Public file sharing (e.g., WeTransfer) is prohibited for confidential data.

### 3.4 Collaboration Tools
Collaboration tools (Teams, Slack, etc.) must meet security requirements:
- Encrypted communication
- Access control
- Data Loss Prevention (DLP)
- Audit logging

### 3.5 Messaging and Chat
Instant messaging for business communication occurs via approved tools. Private messaging apps are prohibited for confidential business information.

### 3.6 Data Loss Prevention (DLP)
DLP systems prevent unintentional or malicious data exfiltration. DLP monitors email, file sharing, and collaboration tools.

### 3.7 External Communication
Communication with external parties (customers, partners, suppliers) occurs via secure channels. Confidentiality agreements (NDAs) are concluded as needed.

### 3.8 Mobile Communication
Mobile communication (smartphones, tablets) occurs via secure channels. Mobile devices are managed with MDM/MAM (see `0500_Policy_Mobile_Device_and_Remote_Work.md`).

### 3.9 Social Media
Business social media use follows social media guidelines. Confidential information is not shared via social media.

## 4. Roles and Responsibilities

### RACI Matrix: Information Transfer and Communication

| Activity | CISO | IT Operations | Communication Security | End User | DPO |
|----------|------|---------------|------------------------|----------|-----|
| Policy Creation | R/A | C | R | I | C |
| Email Security | C | R/A | R | I | C |
| File Sharing | C | R/A | R | R | C |
| Collaboration Tools | C | R/A | R | R | C |
| DLP Implementation | R/A | R | R | I | C |
| External Communication | C | C | C | R | C |
| Mobile Communication | C | R/A | C | R | I |
| Social Media | C | I | R/A | R | I |

**Legend:** R = Responsible (Execution), A = Accountable (Ownership), C = Consulted, I = Informed

### Key Roles

- **Policy Owner:** [TODO] (CISO)
- **Communication Security Manager:** {{ meta-handbook.communication_security_manager }}
- **IT Operations Manager:** {{ meta-handbook.it_operations_manager }}
- **Data Protection Officer:** {{ meta-handbook.dpo_name }}
- **Implementation Responsible:** IT Operations, End Users
- **Control/Audit Function:** ISMS, Internal Audit, DPO

## 5. Derived Documents (Guidelines/Standards/Processes)

Implementation details are defined in subordinate documents:

### Related Guidelines
- **0670_Guideline_Email_Sharing_and_Collaboration_Tools.md** - Detailed implementation guideline
- `0280_Policy_Data_Classification_and_Information_Handling.md` - Data Classification Policy
- `0260_Policy_Cryptography_and_Key_Management.md` - Encryption Policy
- `0500_Policy_Mobile_Device_and_Remote_Work.md` - Mobile Device Policy

### Related Standards/Baselines
- Email Security Configuration (SPF, DKIM, DMARC)
- Approved File Sharing Platforms
- Approved Collaboration Tools
- DLP Rules and Policies
- Social Media Guidelines

### Related Processes
- Email Encryption Process (S/MIME, PGP)
- File Sharing Approval Process
- DLP Incident Response
- External Communication (NDA Process)

## 6. Compliance, Monitoring and Enforcement

### Metrics and KPIs
- Email Encryption Rate (Target: 100% for confidential emails)
- SPF/DKIM/DMARC Compliance (Target: 100%)
- DLP Incident Rate
- Number of blocked phishing emails
- File Sharing Compliance (Target: 100% approved platforms)
- Collaboration Tool Compliance
- Number of social media violations

### Evidence and Proof
- Email Security Configuration (SPF, DKIM, DMARC)
- Email Encryption Logs
- DLP Logs and Incident Reports
- File Sharing Logs
- Collaboration Tool Configuration
- Phishing Simulation Results
- Social Media Monitoring

### Consequences of Violations
Violations of this policy are handled according to applicable HR and compliance processes:
- **Unencrypted Confidential Emails:** Incident response, user awareness training
- **Unapproved File Sharing Tools:** Access blocked, disciplinary measures
- **DLP Violations:** Incident response, investigation, disciplinary measures if applicable
- **Repeated Violations:** Employment consequences, access revocation

## 7. Exceptions

Exceptions to this policy are only permitted in justified exceptional cases:

- **Exception Process:** See `0640_Policy_Exceptions_and_Risk_Waivers.md`
- **Approval:** Exceptions must be approved by CISO and Communication Security Manager
- **Documentation:** All exceptions are documented in the risk register
- **Time Limitation:** Exceptions are generally time-limited

## 8. References

### Internal Documents
- `0010_ISMS_Information_Security_Policy.md` - ISMS Policy
- `0670_Guideline_Email_Sharing_and_Collaboration_Tools.md` - Detailed Guideline
- `0280_Policy_Data_Classification_and_Information_Handling.md` - Data Classification Policy
- `0080_ISMS_Risk_Register_Template.md` - Risk Register

### External Standards and Regulations
- **ISO/IEC 27001:2022 Annex A.5.14** - Information transfer
- **ISO/IEC 27001:2022 Annex A.8.24** - Use of cryptography
- **ISO/IEC 27001:2022 Annex A.8.26** - Application security requirements
- **NIST SP 800-177** - Trustworthy Email
- **RFC 7208** - Sender Policy Framework (SPF)
- **RFC 6376** - DomainKeys Identified Mail (DKIM)
- **RFC 7489** - Domain-based Message Authentication, Reporting, and Conformance (DMARC)

**Approved by:**  
{{ meta-handbook.management_ceo }}, Executive Management  
Date: [TODO]

**Next Review:** [TODO] (annually or as needed)

