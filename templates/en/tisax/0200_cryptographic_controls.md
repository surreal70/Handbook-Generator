
Document-ID: tisax-0200

Status: Draft
Classification: Internal

# Cryptographic Controls

**Document-ID:** [FRAMEWORK]-0200
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

This document defines requirements for the use of cryptographic controls according to TISAX requirements.

## Scope

This document applies to all cryptographic measures at [TODO].

## Cryptography Policy

### Objectives
- Protection of confidentiality of sensitive information
- Ensuring data integrity
- Authentication of communication partners
- Non-repudiation of transactions

### Application Areas
Encryption required for:
- Confidential and strictly confidential data
- Personal data
- Trade secrets
- Authentication information
- Data transmission over insecure networks

## Encryption Standards

### Symmetric Encryption
**Approved Algorithms:**
- AES-256 (preferred)
- AES-128 (acceptable)
- ChaCha20 (acceptable)

**Not Approved:**
- DES, 3DES
- RC4
- Blowfish

### Asymmetric Encryption
**Approved Algorithms:**
- RSA (minimum 2048 bit, preferred 4096 bit)
- ECC (minimum 256 bit)
- Ed25519

**Not Approved:**
- RSA < 2048 bit
- DSA < 2048 bit

### Hash Functions
**Approved Algorithms:**
- SHA-256 (preferred)
- SHA-384
- SHA-512
- SHA-3

**Not Approved:**
- MD5
- SHA-1

## Encryption of Data at Rest

### Data Storage
- Encryption of confidential data at rest
- Full disk encryption for mobile devices
- Database encryption for sensitive data
- Encrypted backups

### Cloud Storage
- Encryption before upload (client-side)
- Encryption by cloud provider
- Key management by organization
- Regular review

## Encryption of Data in Transit

### Network Encryption
- TLS 1.2 or higher for all connections
- Strong cipher suites
- Certificate validation
- Perfect forward secrecy

### Email Encryption
- Encryption of confidential emails
- S/MIME or PGP
- Digital signatures
- Secure key distribution

## Digital Signatures

### Application
- Contracts and agreements
- Software distribution
- Email communication
- Document authentication

## Certificate Management

### Public Key Infrastructure (PKI)
- Certificate Authority (CA)
- Registration Authority (RA)
- Certificate Revocation List (CRL)
- Online Certificate Status Protocol (OCSP)

## Key Management

### Key Generation
- Cryptographically secure random number generators
- Sufficient key length
- Secure generation environment
- Documentation

### Key Storage
- Hardware Security Modules (HSM) for critical keys
- Encrypted storage
- Access control
- Physical security

### Key Distribution
- Secure transmission channels
- Authentication of recipients
- Logging
- Confirmation of receipt

### Key Rotation
- Regular rotation (at least annually)
- Automated processes where possible
- No interruption of operations
- Documentation

### Key Revocation
**Reasons:**
- Compromise
- Employee departure
- Expiration
- Change of requirements

**Process:**
- Immediate revocation
- Notification of stakeholders
- Reissuance if needed
- Documentation

### Key Archiving
- Long-term retention for encrypted data
- Secure storage
- Access control
- Recovery process

### Key Destruction
- Secure deletion
- Multiple overwriting
- Documentation
- Verification of completeness
- No recoverability

## Cryptographic Devices

### Hardware Security Modules (HSM)
- FIPS 140-2 Level 2 or higher
- Physical security
- Access control
- Regular maintenance

## Compliance and Standards

### Relevant Standards
- ISO/IEC 27001:2013 (Annex A.10)
- NIST SP 800-57 (Key Management)
- NIST SP 800-52 (TLS)
- BSI TR-02102 (Cryptographic Procedures)

## TISAX-Specific Requirements

### VDA ISA Controls
- **4.1**: Cryptographic controls
- **4.2**: Key management

### Assessment Evidence
- Cryptography policy
- Key management processes
- Encryption evidence
- Audit reports

## Metrics

[TODO] measures:
- Percentage of encrypted data (Target: 100% for confidential data)
- Number of active keys
- Number of key rotations
- Number of security incidents related to cryptography

<!-- End of template -->
