# Cryptographic Protection

**Document ID:** NIST-0720  
**Control Family:** System and Communications Protection (SC)  
**Controls:** SC-8, SC-12, SC-13, SC-17, SC-28  
**Organization:** {{ meta.organization.name }}  
**Owner:** {{ meta.document.owner }}  
**Version:** {{ meta.document.version }}  
**Status:** Draft / In Review / Approved  
**Last Updated:** {{ meta.document.last_updated }}  

---

## 1. Control Description

This document covers cryptographic protection controls:
- **SC-8:** Transmission Confidentiality and Integrity
- **SC-12:** Cryptographic Key Establishment and Management
- **SC-13:** Cryptographic Protection
- **SC-17:** Public Key Infrastructure Certificates
- **SC-28:** Protection of Information at Rest

## 2. Control Implementation

### 2.1 Transmission Confidentiality and Integrity (SC-8)

**Encryption Requirements:**
| Data Type | Encryption Method | Key Length | Protocol |
|-----------|------------------|------------|----------|
| Web traffic | TLS 1.2/1.3 | 256-bit | HTTPS |
| Email | TLS, S/MIME | 256-bit | SMTP/TLS |
| File transfer | SFTP, FTPS | 256-bit | SSH, TLS |
| Database | TLS | 256-bit | DB-specific |
| VPN | IPsec, SSL/TLS | 256-bit | Various |

**Approved Algorithms:**
- Symmetric: AES-256, ChaCha20
- Asymmetric: RSA-2048+, ECDSA P-256+
- Hash: SHA-256, SHA-384, SHA-512
- Key exchange: ECDHE, DHE

[TODO: Specify approved algorithms]

### 2.2 Cryptographic Key Management (SC-12)

**Key Lifecycle:**
1. **Generation**
   - Secure random number generation
   - Approved algorithms
   - Appropriate key lengths

2. **Distribution**
   - Secure key exchange protocols
   - Out-of-band verification
   - Access controls

3. **Storage**
   - Hardware security modules (HSMs)
   - Key encryption keys (KEKs)
   - Access controls

4. **Usage**
   - Purpose-specific keys
   - Usage logging
   - Access controls

5. **Rotation**
   - Rotation schedule
   - Automated rotation
   - Key history

6. **Destruction**
   - Secure deletion
   - Verification
   - Documentation

[TODO: Define key management procedures]

**Key Management System:**
- Centralized key management
- HSM integration
- Automated key rotation
- Audit logging

[TODO: Describe key management system]

### 2.3 Cryptographic Protection (SC-13)

**Cryptographic Modules:**
- FIPS 140-2/140-3 validated modules
- Approved algorithms
- Proper implementation
- Regular updates

[TODO: List cryptographic modules in use]

**Implementation Requirements:**
- No custom cryptography
- Use of established libraries
- Proper initialization
- Secure defaults

[TODO: Define implementation requirements]

### 2.4 PKI Certificates (SC-17)

**Certificate Management:**
- Certificate issuance
- Certificate renewal
- Certificate revocation
- Certificate validation

[TODO: Define certificate management procedures]

**Certificate Authorities:**
| CA Type | Purpose | Validation Level |
|---------|---------|------------------|
| Internal CA | Internal systems | Domain validation |
| Public CA | External services | Extended validation |
| [TODO] | [TODO] | [TODO] |

**Certificate Policies:**
- Certificate lifetimes
- Key lengths
- Allowed uses
- Revocation procedures

[TODO: Define certificate policies]

### 2.5 Protection of Information at Rest (SC-28)

**Encryption at Rest:**
| Data Type | Encryption Method | Key Management |
|-----------|------------------|----------------|
| Database | Transparent Data Encryption (TDE) | HSM |
| File systems | Full disk encryption | TPM/HSM |
| Backups | AES-256 | HSM |
| Archives | AES-256 | HSM |
| Mobile devices | Device encryption | Device-based |

**Encryption Scope:**
- All sensitive data
- All regulated data
- All backup media
- All portable media

[TODO: Define encryption scope]

**Key Management:**
- Separate encryption keys per system
- Regular key rotation
- Secure key storage
- Key backup and recovery

[TODO: Define key management for data at rest]

## 3. Control Enhancements

- **SC-8(1):** Cryptographic Protection
- **SC-8(2):** Pre- and Post-Transmission Handling
- **SC-8(3):** Cryptographic Protection for Message Externals
- **SC-8(4):** Conceal or Randomize Communications
- **SC-12(1):** Availability
- **SC-12(2):** Symmetric Keys
- **SC-12(3):** Asymmetric Keys
- **SC-12(6):** Physical Control of Keys
- **SC-13(1):** FIPS-Validated Cryptography
- **SC-17(1):** Receiver Checks
- **SC-17(2):** Validation of Binding
- **SC-28(1):** Cryptographic Protection
- **SC-28(2):** Offline Storage
- **SC-28(3):** Cryptographic Keys

[TODO: Mark applicable enhancements]

## 4. Implementation Status

**Status:** [TODO: Implemented / Partially Implemented / Planned / Not Applicable]  
**Implementation Date:** [TODO: Date]  
**Responsible:** [TODO: Name/Role]  

## 5. Assessment

**Assessment Method:** Examine, Interview, Test  
**Assessment Status:** [TODO: Satisfied / Other than Satisfied / Not Applicable]  
**Findings:** [TODO: Description]  

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial creation |

<!-- End of template -->
