
Document-ID: tisax-0370

Status: Draft
Classification: Internal

# Information Transfer

**Document-ID:** [FRAMEWORK]-0370
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Approved by:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Classification:** {{ meta-handbook.classification }}
**Last Update:** {{ meta-handbook.modifydate }}

---

---

## Purpose

This document defines requirements for secure transfer of information according to TISAX requirements.

## Scope

This document applies to all information transfers of [TODO].

## Transfer Channels

### Email
- Encryption of confidential emails (S/MIME or PGP)
- SPF, DKIM, DMARC
- Spam and malware filter
- DLP (Data Loss Prevention)

### File Transfer
**Secure Methods:**
- SFTP/SCP
- HTTPS
- Encrypted cloud services
- Managed File Transfer (MFT)

**Not Approved:**
- FTP (unencrypted)
- HTTP (unencrypted)
- Unencrypted email attachments (confidential data)

### Physical Media
- Encryption
- Secure packaging
- Tracking
- Receipt confirmation

## Encryption

### Transmission Encryption
- TLS 1.2 or higher
- Strong cipher suites
- Certificate validation
- Perfect forward secrecy

### End-to-End Encryption
**Use for:**
- Strictly confidential information
- Personal data
- Trade secrets

## Data Classification

### Transfer Policies
**Public:** No special requirements
**Internal:** Encrypted channels preferred
**Confidential:** Encryption mandatory, approval required
**Strictly Confidential:** End-to-end encryption, approval and documentation required

## External Communication

### Partners and Suppliers
- Confidentiality agreements
- Secure transfer channels
- Documentation
- Regular review

### Cloud Services
- Encrypted transmission
- Encrypted storage
- Access control
- Compliance review

## Monitoring

### Monitoring
**Monitored Activities:**
- Transfer of confidential data
- Large data volumes
- Unusual transfer patterns
- External transfers

### DLP (Data Loss Prevention)
- Detection of sensitive data
- Blocking unauthorized transfers
- Alerting
- Reporting

## TISAX-Specific Requirements

### VDA ISA Controls
- **7.2**: Information transfer

### Assessment Evidence
- Transfer policies
- Encryption configuration
- DLP reports

## Metrics

[TODO] measures:
- Number of encrypted transfers
- Number of DLP incidents
- Compliance rate

<!-- End of template -->
