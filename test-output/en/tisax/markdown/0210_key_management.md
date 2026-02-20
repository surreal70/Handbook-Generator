
Document-ID: tisax-0210

Status: Draft
Classification: Internal

# Key Management

**Document-ID:** [FRAMEWORK]-0210
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

## Purpose

This document describes the processes and procedures for managing cryptographic keys according to TISAX requirements.

## Scope

This document applies to all cryptographic keys at [TODO].

## Key Lifecycle

### 1. Key Generation
- Cryptographically secure random number generators (CSRNG)
- Sufficient key length according to standards
- Secure generation environment
- Documentation of generation

### 2. Key Storage
- Hardware Security Modules (HSM) for critical keys
- Encrypted storage
- Redundant storage
- Access control
- Physical security

### 3. Key Distribution
- Secure transmission channels
- Authentication of recipients
- Encrypted transmission
- Logging
- Confirmation of receipt

### 4. Key Usage
- Use only for intended purpose
- Logging of usage
- Monitoring for misuse
- Regular review

### 5. Key Rotation
- Regular rotation according to policy
- Automated processes where possible
- No interruption of operations
- Documentation

**Rotation Intervals:**
- Critical keys: Quarterly
- Production keys: Semi-annually
- Standard keys: Annually
- Test keys: As needed

### 6. Key Revocation
**Reasons:**
- Compromise suspected or confirmed
- Employee departure
- Expiration
- Change of requirements
- Security incident

**Process:**
1. Identification of revocation reason
2. Immediate revocation of key
3. Notification of all stakeholders
4. Reissuance if needed
5. Documentation
6. Post-incident review

### 7. Key Archiving
- Long-term retention for encrypted data
- Secure storage
- Access control
- Recovery process
- Regular integrity verification

### 8. Key Destruction
- Secure deletion
- Multiple overwriting
- Documentation
- Verification of completeness
- No recoverability

## Key Types

### Symmetric Keys
- Data encryption
- Message authentication
- Database encryption

### Asymmetric Key Pairs
- Digital signatures
- Key exchange
- Authentication
- Certificates

### Master Keys
- Encryption of other keys (Key Encryption Keys)
- Highest security level

### Session Keys
- Temporary encryption
- Communication sessions

## Key Management Systems

### Hardware Security Modules (HSM)
- Secure key generation
- Protected key storage
- Cryptographic operations
- Audit logging

**Requirements:**
- FIPS 140-2 Level 2 or higher
- Redundant configuration
- Regular maintenance
- Backup and recovery

### Key Management Service (KMS)
- Central key management
- API-based access
- Automated rotation
- Audit logging

## Key Recovery

### Backup and Recovery
- Regular backups of critical keys
- Secure storage of backups
- Tested recovery processes
- Documentation

### Escrow
- For critical business keys
- Upon employee departure
- For emergency recovery

## Access Control

### Permissions
**Roles:**
- Key Manager: Complete management
- Key User: Use of assigned keys
- Auditor: Read-only access to logs
- Emergency Access: Break-glass access

### Authentication
- Multi-factor authentication
- Strong passwords
- Regular recertification
- Logging of all access

## Monitoring and Audit

### Logging
**Events:**
- Key generation
- Key access
- Key rotation
- Key revocation
- Key destruction
- Failed access attempts

### Monitoring
- Real-time monitoring of critical operations
- Automatic alerting on anomalies
- Regular log analyses
- Compliance checks

### Audit
- Quarterly sampling
- Annual full review
- Compliance verification
- Identification of improvement potential

## Emergency Management

### Key Compromise
**Immediate Actions:**
1. Identification of compromised key
2. Immediate revocation
3. Notification of all stakeholders
4. Reissuance of keys
5. Investigation of incident
6. Documentation

### Key Loss
1. Attempt recovery from backup
2. If unsuccessful: Reissuance
3. Review of impact
4. Notification of affected parties
5. Documentation

## TISAX-Specific Requirements

### VDA ISA Controls
- **4.2.1**: Key management
- **4.2.2**: Key generation
- **4.2.3**: Key storage
- **4.2.4**: Key distribution

### Assessment Evidence
- Key management processes
- Key management database
- Audit logs
- Training evidence
- Incident response plans

## Metrics

[TODO] measures:
- Number of active keys
- Number of key rotations (Target: 100% on time)
- Number of key compromises (Target: 0)
- Average time to key provisioning
- Compliance rate (Target: 100%)


