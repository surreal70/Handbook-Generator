# Guideline: Key Management and Encryption

**Document-ID:** [FRAMEWORK]-0270
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

<!-- 
TEMPLATE AUTHOR NOTE:
This guideline provides detailed implementation guidance for cryptographic key management
and encryption controls. Customize based on your organization's cryptographic requirements.
-->

**Document ID:** 0270  
**Document Type:** Guideline (detailed)  
**Related Policy:** 0260_Policy_Cryptography_and_Key_Management.md  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.8.24  
**Owner:** {{ meta.it_operations.manager }}  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Confidential  
**Last Updated:** {{ meta-handbook.modifydate }}  
**Next Review:** {{ meta-handbook.next_review }}

## 1. Purpose and Scope

This guideline implements the `0260_Policy_Cryptography_and_Key_Management.md` and defines detailed procedures for:
- Cryptographic algorithms and standards
- Key generation, storage, and rotation
- Certificate management
- Encryption of data at rest and in transit

**Scope:** All cryptographic systems at **{{ meta-organisation.name }}**

## 2. Cryptographic Standards

### 2.1 Approved Algorithms

**Symmetric Encryption:**
- **AES-256** (Advanced Encryption Standard, 256-bit) - Recommended
- **AES-128** - Acceptable for non-critical data
- **ChaCha20** - Acceptable for mobile devices

**Asymmetric Encryption:**
- **RSA-4096** - Recommended for long-term security
- **RSA-2048** - Acceptable, minimum requirement
- **ECDSA P-384** - Recommended for performance
- **Ed25519** - Acceptable for SSH keys

**Hash Functions:**
- **SHA-256** - Minimum requirement
- **SHA-384, SHA-512** - Recommended for critical applications
- **BLAKE2** - Acceptable

**Prohibited Algorithms:**
- MD5, SHA-1 (cryptographically broken)
- DES, 3DES (deprecated)
- RSA < 2048 bit (too weak)
- RC4 (insecure)

### 2.2 TLS/SSL Configuration

**TLS Versions:**
- **TLS 1.3** - Recommended
- **TLS 1.2** - Minimum requirement
- **TLS 1.1, 1.0, SSL** - Prohibited

**Cipher Suites (Recommended):**
```
TLS_AES_256_GCM_SHA384
TLS_CHACHA20_POLY1305_SHA256
TLS_AES_128_GCM_SHA256
ECDHE-RSA-AES256-GCM-SHA384
ECDHE-RSA-AES128-GCM-SHA256
```

**Certificates:**
- Minimum RSA-2048 or ECDSA P-256
- Validity period: Max. 13 months (398 days)
- Trusted Certificate Authorities (CAs)

## 3. Key Management

### 3.1 Key Generation

**Requirements:**
- Cryptographically secure random number generators (CSPRNG)
- Key lengths per section 2.1
- Generation in secure environment (HSM, Key Vault)

**Process:**
1. Key request via ticket system
2. Approval by CISO or IT security
3. Generation by Key Management System
4. Secure handover to requester
5. Documentation in key register

### 3.2 Key Storage

**Hardware Security Modules (HSM):**
- Critical keys (Root CA, master keys) in HSM: {{ meta.security.hsm }}
- FIPS 140-2 Level 2 or higher
- Physical security and access control

**Key Management Systems:**
- **Cloud:** {{ meta.cloud.key_vault }} (e.g., Azure Key Vault, AWS KMS)
- **On-Premises:** {{ meta.security.kms }} (e.g., HashiCorp Vault)
- Encrypted storage
- Audit logging of all access

**Prohibited:**
- Storage in plaintext
- Hardcoding in source code
- Storage in configuration files
- Transmission via email or chat

### 3.3 Key Rotation

**Rotation Intervals:**

| Key Type | Rotation | Justification |
|----------|----------|---------------|
| Data Encryption Keys (DEK) | Annually | Balance between security and effort |
| Key Encryption Keys (KEK) | Every 2 years | Rarely used, higher security |
| TLS Certificates | Every 12 months | CA requirements |
| API Keys | Every 90 days | Frequent use, higher risk |
| SSH Keys | Every 180 days | Administrative access |

**Automation:**
- Automatic rotation where possible (cloud services)
- Notifications 30 days before expiration
- Documentation of all rotations

**Emergency Rotation:**
- On suspected compromise: Immediate rotation
- On personnel change: Rotation of all affected keys
- On security incidents: Rotation per incident response

### 3.4 Key Destruction

**Process:**
1. Mark key as "deprecated"
2. Grace period (30 days) for data decryption
3. Secure deletion from all systems
4. Documentation of destruction

**Methods:**
- Cryptographic overwriting (multiple passes)
- HSM: Secure erase function
- Physical media: Destruction per DIN 66399

## 4. Certificate Management

### 4.1 Public Key Infrastructure (PKI)

**Components:**
- **Root CA:** {{ meta.pki.root_ca }} (Offline, HSM-protected)
- **Issuing CA:** {{ meta.pki.issuing_ca }} (Online, for certificate issuance)
- **Certificate Management System:** {{ meta.pki.cms }}

**Certificate Types:**
- **Server Certificates:** Web servers, API endpoints
- **Client Certificates:** User authentication, VPN
- **Code Signing:** Software signing
- **Email Certificates:** S/MIME encryption

### 4.2 Certificate Lifecycle

**Issuance:**
1. Create Certificate Signing Request (CSR)
2. Submit request via PKI portal
3. Validation by Certificate Authority
4. Issue and provide certificate
5. Installation and configuration

**Renewal:**
- Automatic notification 60 days before expiration
- Renewal 30 days before expiration
- Automation via ACME protocol (Let's Encrypt)

**Revocation:**
- On compromise: Immediate revocation
- On personnel change: Revocation of all personal certificates
- Publication in Certificate Revocation List (CRL)
- OCSP (Online Certificate Status Protocol) for real-time checks

### 4.3 Certificate Inventory

**Documentation:**
- All issued certificates in CMDB
- Expiration dates, purpose, owner
- Automatic scans for unknown certificates

**Monitoring:**
- Daily check for expiring certificates
- Alerts for certificates < 30 days validity
- Automatic renewal where possible

## 5. Data Encryption

### 5.1 Data at Rest

**Encryption Requirement:**
- All confidential and highly confidential data
- Personal data (GDPR requirement)
- Financial data and trade secrets
- Backups and archived data

**Methods:**

| Storage Location | Method | Key Management |
|------------------|--------|----------------|
| Laptops/Desktops | BitLocker (Windows), FileVault (macOS) | TPM + Recovery Key in Key Vault |
| Server Disks | LUKS (Linux), BitLocker (Windows) | Key Vault |
| Databases | Transparent Data Encryption (TDE) | Database Key Management |
| Cloud Storage | Server-Side Encryption (SSE) | Cloud Key Management Service |
| File Servers | Encrypted File System (EFS) | Active Directory + Key Vault |

**Configuration:**
- AES-256 for all encryption
- Automatic encryption on storage
- No user interaction required

### 5.2 Data in Transit

**Encryption Requirement:**
- All data transmission over public networks
- Internal transmission of confidential data
- API communication
- Email with confidential content

**Methods:**

| Transmission Type | Protocol | Configuration |
|-------------------|----------|---------------|
| Web Traffic | HTTPS (TLS 1.2+) | See section 2.2 |
| Email | TLS (SMTP), S/MIME | Opportunistic TLS + encryption for confidential |
| File Transfer | SFTP, FTPS, HTTPS | No unencrypted protocols |
| VPN | IPsec, WireGuard | AES-256, Perfect Forward Secrecy |
| Database | TLS for connections | Enforced encryption |

**Prohibited Protocols:**
- FTP (unencrypted)
- Telnet (unencrypted)
- HTTP for confidential data
- SMTP without TLS for confidential emails

### 5.3 Data in Use

**Technologies:**
- **Confidential Computing:** Encryption during processing (Intel SGX, AMD SEV)
- **Homomorphic Encryption:** Computations on encrypted data (experimental)
- **Secure Enclaves:** Isolated processing environments

**Use Cases:**
- Processing highly sensitive data in cloud
- Multi-party computation
- Privacy-preserving analytics

## 6. Email Encryption

### 6.1 S/MIME

**Implementation:**
- S/MIME certificates for all employees
- Automatic encryption for emails with "Confidential" classification
- Signing of all outgoing emails

**Configuration:**
- Outlook, Thunderbird: S/MIME plugin
- Mobile devices: Native S/MIME support
- Certificate distribution via Active Directory

### 6.2 Opportunistic TLS

**SMTP TLS:**
- All email servers support STARTTLS
- Enforced encryption for known partners
- Fallback to unencrypted only for non-confidential emails

**MTA-STS (Mail Transfer Agent Strict Transport Security):**
- Policy publication via DNS
- Enforcement of TLS for incoming emails

## 7. Backup Encryption

**Requirements:**
- All backups encrypted (AES-256)
- Separate keys for backups (not production keys)
- Offline copy of backup keys (safe)

**Process:**
1. Backup creation with encryption
2. Store key in Key Vault
3. Offline copy of key in safe
4. Regular restore tests (quarterly)

**Disaster Recovery:**
- Backup keys in emergency documentation
- Access only by authorized persons
- Four-eyes principle for key access

## 8. Cloud Encryption

### 8.1 Cloud Storage

**Configuration:**
- **Azure:** Customer-Managed Keys (CMK) in Azure Key Vault
- **AWS:** Customer Master Keys (CMK) in AWS KMS
- **Google Cloud:** Customer-Managed Encryption Keys (CMEK)

**Benefits:**
- Control over keys
- Ability to rotate keys
- Compliance requirements met

### 8.2 Cloud Databases

**Encryption:**
- Transparent Data Encryption (TDE) enabled
- Encrypted connections (TLS)
- Customer-managed keys for critical databases

## 9. Compliance and Audit

### 9.1 Key Performance Indicators (KPIs)

| Metric | Target Value | Measurement |
|--------|--------------|-------------|
| Encrypted Laptops | 100% | Endpoint Management |
| TLS 1.2+ Usage | 100% | Web Server Logs |
| Certificate Expiration Incidents | 0 per year | PKI Monitoring |
| Key Rotation Compliance | > 95% | Key Management System |

### 9.2 Audit Evidence

**Documentation:**
- Cryptography policy and guidelines
- Key register and inventory
- Certificate inventory
- Encryption configurations
- Audit logs for key access

## 10. References

### Internal Documents
- `0260_Policy_Cryptography_and_Key_Management.md` - Parent policy
- `0420_Policy_Backup_und_Wiederherstellung.md` - Backup policy

### External Standards
- **ISO/IEC 27001:2022 Annex A.8.24** - Use of cryptography
- **NIST SP 800-57** - Key Management Recommendations
- **NIST SP 800-52** - TLS Guidelines
- **BSI TR-02102** - Cryptographic Procedures

**Approved by:**  
{{ meta.ciso.name }}, CISO  
Date: {{ meta-handbook.modifydate }}

**Next Review:** {{ meta-handbook.next_review }}

