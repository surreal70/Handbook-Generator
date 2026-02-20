
Document-ID: csa-ccm-0210

Status: Draft
Classification: Internal

# DSP-05: Data Encryption at Rest

**Document-ID:** CSA-CCM-0210
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

## CCM Control

**Control Domain**: Data Security & Privacy (DSP)  
**Control ID**: DSP-05  
**Control Name**: Data Encryption at Rest

## Control Objective

Protect sensitive data at rest through encryption to prevent unauthorized access and ensure confidentiality.

## Control Description

The organization must:
- Encrypt all sensitive data at rest
- Use strong encryption algorithms (minimum AES-256)
- Securely manage encryption keys
- Implement encryption for all storage locations (databases, file storage, backups)
- Regularly review encryption implementation

## Implementation at [TODO]

### Encryption Standards

**Algorithms**:
- **Symmetric**: AES-256-GCM
- **Asymmetric**: RSA-4096, ECC P-384
- **Hashing**: SHA-256, SHA-384

**Protocols**:
- TLS 1.3 (for data in transit)
- IPSec (for VPN connections)

### Encryption Implementation

**Databases**:

| Database | Type | Encryption Method | Status |
|----------|------|-------------------|--------|
| [DB 1] | PostgreSQL | Transparent Data Encryption (TDE) | Active |
| [DB 2] | MySQL | InnoDB Encryption | Active |
| [DB 3] | MongoDB | Encryption at Rest | Active |

**File Storage**:

| Storage | Type | Encryption Method | Status |
|---------|------|-------------------|--------|
| [Storage 1] | Object Storage | Server-Side Encryption (SSE) | Active |
| [Storage 2] | Block Storage | LUKS Full Disk Encryption | Active |
| [Storage 3] | NAS | AES-256 Encryption | Active |

**Backups**:

| Backup System | Encryption Method | Key Management | Status |
|---------------|-------------------|----------------|--------|
| [Backup 1] | AES-256 | KMS | Active |
| [Backup 2] | AES-256 | HSM | Active |

### Key Management

**Key Management System (KMS)**:
- **Provider**: [KMS Provider]
- **Type**: Cloud-based / On-Premises / Hybrid
- **FIPS 140-2 Level**: Level 2/3

**Key Hierarchy**:
```
Master Key (Root Key)
    ├── Key Encryption Keys (KEK)
    │   ├── Data Encryption Key 1 (DEK)
    │   ├── Data Encryption Key 2 (DEK)
    │   └── Data Encryption Key 3 (DEK)
    └── Backup Encryption Keys
```

**Key Rotation**:
- **Master Keys**: Annually
- **Data Encryption Keys**: Quarterly
- **Backup Keys**: Semi-annually

### Access Control for Encryption Keys

**Permission Model**:

| Role | Permission | Approval Required |
|------|------------|-------------------|
| Security Admin | Full KMS access | CISO |
| Database Admin | Access to DB keys | Security Admin |
| Backup Admin | Access to backup keys | Security Admin |
| Developer | No direct access | N/A |

**Multi-Person Control**:
- Key generation: 2 persons required
- Key deletion: 3 persons required
- Master Key rotation: CISO + 2 Security Admins

## Control Activities

### 1. Encryption Implementation

**Process**:
1. Perform data classification
2. Define encryption requirements
3. Select encryption solution
4. Implementation and configuration
5. Testing and validation
6. Documentation

**Responsible**: Security Team, Infrastructure Team

### 2. Key Management

**Process**:
1. Key generation
2. Key storage in KMS/HSM
3. Key distribution (automated)
4. Key rotation (scheduled)
5. Key archival
6. Key destruction

**Automation**: 95% of key operations automated

### 3. Encryption Monitoring

**Monitoring**:
- Encryption status of all systems
- Key access and usage
- Failed encryption operations
- Compliance deviations

**Tools**:
- SIEM Integration
- KMS Audit Logs
- Cloud Security Posture Management (CSPM)

**Alerting**:
- Unencrypted sensitive data detected
- Unauthorized key access
- Encryption failures
- Key rotation overdue

### 4. Compliance Validation

**Validation Methods**:
- Automated compliance scans
- Manual sampling
- Penetration tests
- External audits

**Frequency**:
- Automated: Daily
- Manual: Monthly
- Penetration Test: Annually
- Audit: Annually

## Evidence and Documentation

### Required Evidence

1. **Encryption Configuration**:
   - Encryption policies
   - Configuration documentation
   - Encryption inventory

2. **Key Management**:
   - KMS configuration
   - Key rotation logs
   - Access logs

3. **Monitoring and Alerting**:
   - SIEM logs
   - Compliance scan reports
   - Alert history

4. **Testing and Validation**:
   - Encryption tests
   - Penetration test reports
   - Audit reports

## Metrics and KPIs

| Metric | Target Value | Measurement Frequency |
|--------|--------------|----------------------|
| Encryption rate (sensitive data) | 100% | Daily |
| Unencrypted sensitive data | 0 | Daily |
| Key rotation on time | 100% | Monthly |
| Encryption failures | < 0.1% | Weekly |
| KMS availability | ≥ 99.9% | Monthly |
| Time to encrypt new data | ≤ 24 hours | Per system |

## Risks and Control Gaps

### Identified Risks

| Risk | Likelihood | Impact | Risk Score | Mitigation |
|------|-----------|--------|------------|------------|
| Key loss | Low | Critical | 15 | Backup, Escrow |
| Unauthorized key access | Low | High | 10 | MFA, Monitoring |
| Weak encryption | Very low | High | 5 | Standards, Reviews |
| Performance issues | Medium | Medium | 9 | Hardware acceleration |

### Control Gaps

**Legacy Systems**:
- **Description**: Some legacy systems do not support modern encryption
- **Risk**: Medium
- **Remediation**: Migration to new systems planned
- **Due Date**: [Date]

## Audit Notes

### Audit Questions

1. Is all sensitive data at rest encrypted?
2. Are strong encryption algorithms used (AES-256)?
3. Is a Key Management System implemented?
4. Are encryption keys rotated regularly?
5. Is encryption status monitored?
6. Are backups encrypted?

### Audit Evidence

- Encryption policies
- Encryption inventory
- KMS configuration
- Key rotation logs
- Compliance scan reports
- Audit logs
- Penetration test reports

## References

### Internal Documents

- Data Encryption Policy
- Key Management Procedures
- Data Classification Policy

### External Standards

- CSA CCM v4.0 - DSP-05
- NIST SP 800-57 (Key Management)
- NIST SP 800-111 (Storage Encryption)
- ISO/IEC 27018:2019 (Cloud Privacy)
- FIPS 140-2 (Cryptographic Module Validation)
- GDPR Article 32 (Security of Processing)

## Change History

| Version | Date | Author | Change |
|---------|------|--------|--------|
| 1.0 | [Date] | [Author] | Initial version |




