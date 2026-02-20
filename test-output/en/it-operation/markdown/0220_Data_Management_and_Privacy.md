# Data Management and Privacy

**Document-ID:** [FRAMEWORK]-0220
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

## Overview

This document describes the processes and policies for data management and data protection in the IT service. It defines data classification, data protection requirements according to GDPR, data retention and deletion, as well as data governance structures.

**Document Owner:** [TODO]  
**Approved by:** [TODO]  
**Version:** 0  
**Organization:** AdminSend GmbH

## Data Classification

### Classification Levels

| Level | Description | Examples | Protection Measures |
|---|---|---|---|
| **Public** | Intended for public | Marketing material, Press releases | No special measures |
| **Internal** | For internal use only | Internal policies, Org charts | Access control |
| **Confidential** | Sensitive business information | Contracts, Financial reports, Strategies | Encryption, strict access control |
| **Highly Confidential** | Highly sensitive data | Personnel data, Health data, Salaries | Encryption, MFA, Audit logging |

### Classification Criteria

#### Business Value
- **High:** Critical for business operations
- **Medium:** Important for business processes
- **Low:** Supporting information

#### Confidentiality
- **High:** Severe damage if disclosed
- **Medium:** Moderate damage if disclosed
- **Low:** Little or no damage

#### Integrity
- **High:** Critical for decisions
- **Medium:** Important for processes
- **Low:** Informational

#### Availability
- **High:** Immediate availability required
- **Medium:** Availability within hours
- **Low:** Availability within days

### Classification Process

1. **Data Identification:** Capture all data assets
2. **Assessment:** Apply classification criteria
3. **Labeling:** Mark data with classification level
4. **Documentation:** Record in Data Inventory
5. **Review:** Annual review of classification

### Data Inventory

| Data Asset | Classification | Storage Location | Responsible | Retention |
|---|---|---|---|---|
| [TODO] | [TODO] | [[ netbox.storage.location ]] | [TODO] | [TODO] |
| [TODO] | [TODO] | [[ netbox.storage.location ]] | [TODO] | [TODO] |
| [TODO] | [TODO] | [[ netbox.storage.location ]] | [TODO] | [TODO] |

## Data Protection Requirements (GDPR)

### Legal Basis

#### EU General Data Protection Regulation (GDPR)
- **Effective since:** May 25, 2018
- **Scope:** Processing of personal data in the EU
- **Fines:** Up to 20 million EUR or 4% of worldwide annual revenue

#### Federal Data Protection Act (BDSG)
- **Effective since:** May 25, 2018
- **Supplement:** National regulations to GDPR
- **Application:** Germany-specific requirements

### Personal Data

#### Definition
All information relating to an identified or identifiable natural person.

#### Categories

| Category | Examples | Special Protection Measures |
|---|---|---|
| **Basic Data** | Name, Address, Email, Phone | Access control, Encryption |
| **Identification Data** | ID number, Social security number | Strict access control, Encryption |
| **Special Categories** | Health, Religion, Political opinion | Highest protection measures, explicit consent |
| **Financial Data** | Bank details, Credit card number | PCI-DSS compliance, Tokenization |
| **Location Data** | GPS coordinates, IP addresses | Anonymization, Pseudonymization |

### GDPR Principles

#### Lawfulness, Fairness, and Transparency
- Legal basis for each processing
- Transparent information to data subjects
- Documentation of processing purposes

#### Purpose Limitation
- Collect data only for specified purposes
- No further processing for other purposes
- Documentation of processing purposes

#### Data Minimization
- Collect only necessary data
- No excessive data collection
- Regular review of necessity

#### Accuracy
- Ensure data currency
- Correct inaccurate data
- Delete outdated data

#### Storage Limitation
- Store data only as long as necessary
- Defined retention periods
- Automatic deletion after expiry

#### Integrity and Confidentiality
- Protection against unauthorized access
- Encryption of sensitive data
- Access control and audit logging

#### Accountability
- Demonstrate GDPR compliance
- Documentation of all processing activities
- Regular audits

### Data Subject Rights

| Right | Description | Response Time | Responsible |
|---|---|---|---|
| **Right of Access** | Information about stored data | 1 month | [TODO] |
| **Right to Rectification** | Correction of inaccurate data | Without delay | [TODO] |
| **Right to Erasure** | Deletion of personal data | Without delay | [TODO] |
| **Right to Restriction** | Restriction of processing | Without delay | [TODO] |
| **Right to Data Portability** | Transfer to another controller | 1 month | [TODO] |
| **Right to Object** | Object to processing | Without delay | [TODO] |

### Data Protection Impact Assessment (DPIA)

#### Obligation to Conduct
- High risk to rights and freedoms
- New technologies
- Large-scale processing of special categories
- Systematic monitoring

#### DPIA Process
1. **Description:** Processing operations and purposes
2. **Necessity:** Assessment of necessity
3. **Risk Assessment:** Identification and assessment of risks
4. **Protective Measures:** Definition of measures to minimize risks
5. **Documentation:** Creation of DPIA report
6. **Consultation:** If necessary, consultation with supervisory authority

### Data Protection Officer (DPO)

- **Name:** [TODO: Name of DPO]
- **Contact:** [TODO: Email and phone]
- **Tasks:**
  - Monitoring GDPR compliance
  - Advice on data protection issues
  - Employee training
  - Cooperation with supervisory authorities
  - Contact point for data subjects

## Data Retention and Deletion

### Retention Periods

#### Legal Retention Periods

| Data Type | Retention Period | Legal Basis | Responsible |
|---|---|---|---|
| Business Letters | 6 years | HGB § 257 | [TODO] |
| Accounting Documents | 10 years | HGB § 257, AO § 147 | [TODO] |
| Annual Financial Statements | 10 years | HGB § 257 | [TODO] |
| Payroll Documents | 6 years | AO § 147 | [TODO] |
| Tax Documents | 10 years | AO § 147 | [TODO] |
| Personnel Files | 3-10 years | Various | {{ meta-organisation-roles.role_COO }} |

#### Operational Retention Periods

| Data Type | Retention Period | Reason | Responsible |
|---|---|---|---|
| Contracts | Contract term + 3 years | Warranty | [TODO] |
| Project Documentation | 5 years | Traceability | [TODO] |
| Audit Logs | 1 year | Security | [TODO] |
| Backup Data | 30-90 days | Recovery | {{ meta-organisation-roles.role_IT_Operations_Manager }} |
| Emails | 1-3 years | Business Communication | [TODO] |

### Deletion Concept

#### Deletion Process

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│  1. Expiry  →  2. Review  →  3. Approval               │
│       ↓                                    ↓            │
│       │                                    │            │
│  6. Documentation  ←  5. Verification  ←  4. Deletion  │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

#### Deletion Methods

| Media | Method | Standard | Responsible |
|---|---|---|---|
| Hard Drives | Secure Erase / Degaussing | NIST SP 800-88 | {{ meta-organisation-roles.role_IT_Operations_Manager }} |
| SSDs | Crypto Erase / Destruction | NIST SP 800-88 | {{ meta-organisation-roles.role_IT_Operations_Manager }} |
| Backup Media | Overwrite / Destruction | NIST SP 800-88 | {{ meta-organisation-roles.role_IT_Operations_Manager }} |
| Cloud Data | API-based Deletion | Provider Standard | {{ meta-organisation-roles.role_IT_Operations_Manager }} |
| Databases | SQL DELETE / TRUNCATE | Database Standard | {{ meta-organisation-roles.role_IT_Operations_Manager }} |
| Paper | Shredding (P-4) | DIN 66399 | {{ meta-organisation-roles.role_COO }} |

#### Deletion Proof
- Documentation of all deletion processes
- Logging of date, data type, method
- Retention of deletion proofs for 3 years
- Responsible: [TODO]

### Archiving

#### Archiving Process
1. **Identification:** Data that must be archived
2. **Preparation:** Data cleansing and validation
3. **Archiving:** Transfer to archive system
4. **Indexing:** Metadata for retrievability
5. **Verification:** Check archive integrity
6. **Documentation:** Recording in archive register

#### Archiving Systems

| System | Data Type | Retention | Access | Responsible |
|---|---|---|---|---|
| [TODO: Archive System] | [TODO] | [TODO] years | [TODO] | [TODO] |

## Data Governance

### Governance Structure

#### Data Governance Board
- **Chair:** [TODO]
- **Members:** [TODO], [TODO], Department Heads
- **Frequency:** Quarterly
- **Tasks:**
  - Strategic data governance
  - Approval of data policies
  - Compliance monitoring
  - Escalation of data protection incidents

#### Data Stewards
- **Role:** Functional data owners
- **Tasks:**
  - Ensure data quality
  - Perform data classification
  - Grant access permissions
  - Monitor data protection compliance

#### Data Custodians
- **Role:** Technical data owners
- **Tasks:**
  - Technical implementation of data policies
  - Ensure data security
  - Backup and recovery
  - Implement access control

### Data Policies

#### Data Usage Policy
- Permitted and prohibited data uses
- Approval processes for data usage
- Sanctions for violations

#### Data Access Policy
- Access control model (RBAC, ABAC)
- Approval processes for access
- Regular access reviews

#### Data Security Policy
- Encryption requirements
- Security measures by classification
- Incident response processes

#### Data Quality Policy
- Data quality criteria
- Data validation and cleansing
- Data quality metrics

### Data Quality Management

#### Data Quality Dimensions

| Dimension | Description | Target Value | Measurement Method |
|---|---|---:|---|
| **Completeness** | All required data present | > 95% | Automated check |
| **Accuracy** | Data correct and error-free | > 98% | Sampling |
| **Consistency** | Data without contradictions | > 99% | Automated check |
| **Timeliness** | Data up to date | > 95% | Timestamp check |
| **Uniqueness** | No duplicates | > 99% | Duplicate check |

#### Data Quality Process
1. **Measurement:** Capture data quality metrics
2. **Analysis:** Identify quality issues
3. **Cleansing:** Correct erroneous data
4. **Prevention:** Measures to avoid future problems
5. **Monitoring:** Continuous monitoring

## Data Security

### Encryption

#### Encryption at Rest (Data at Rest)

| Data Type | Encryption | Algorithm | Key Length | Responsible |
|---|---|---|---|---|
| Highly Confidential | Mandatory | AES | 256 Bit | [TODO] |
| Confidential | Mandatory | AES | 256 Bit | [TODO] |
| Internal | Recommended | AES | 128/256 Bit | {{ meta-organisation-roles.role_IT_Operations_Manager }} |
| Public | Not required | - | - | - |

#### Encryption in Transit (Data in Transit)

| Connection Type | Protocol | Minimum Version | Responsible |
|---|---|---|---|
| Web Traffic | HTTPS/TLS | TLS 1.2 | {{ meta-organisation-roles.role_IT_Operations_Manager }} |
| Email | TLS/S/MIME | TLS 1.2 | {{ meta-organisation-roles.role_IT_Operations_Manager }} |
| File Transfer | SFTP/FTPS | TLS 1.2 | {{ meta-organisation-roles.role_IT_Operations_Manager }} |
| VPN | IPsec/OpenVPN | - | {{ meta-organisation-roles.role_IT_Operations_Manager }} |
| Database | TLS | TLS 1.2 | {{ meta-organisation-roles.role_IT_Operations_Manager }} |

### Access Control

#### Access Control Model
- **Model:** Role-Based Access Control (RBAC)
- **Principle:** Least Privilege, Need-to-Know
- **Authentication:** Multi-Factor Authentication (MFA) for sensitive data
- **Authorization:** Role-based permissions

#### Access Rights Review
- **Frequency:** Quarterly
- **Responsible:** Data Stewards
- **Process:**
  1. Export all access rights
  2. Review by department
  3. Remove no longer needed rights
  4. Document changes

### Audit Logging

#### Logging Requirements

| Event Type | Logging | Retention | Responsible |
|---|---|---|---|
| Data Access (confidential) | Mandatory | 1 year | [TODO] |
| Data Modification | Mandatory | 1 year | [TODO] |
| Data Deletion | Mandatory | 3 years | [TODO] |
| Access Denial | Mandatory | 1 year | [TODO] |
| Admin Activities | Mandatory | 1 year | [TODO] |

#### Log Contents
- Timestamp
- User ID
- Action (Read, Write, Delete)
- Affected data/objects
- Source IP address
- Result (Success/Error)

## Data Protection Incidents

### Notification Obligation

#### GDPR Notification Obligation
- **Deadline:** 72 hours after becoming aware
- **Recipient:** Competent supervisory authority
- **Content:**
  - Nature of the breach
  - Affected data categories and persons
  - Likely consequences
  - Measures taken

#### Notification of Data Subjects
- **Requirement:** High risk to rights and freedoms
- **Deadline:** Without delay
- **Content:**
  - Nature of the breach
  - Contact point
  - Likely consequences
  - Measures taken

### Incident Response Process

1. **Detection:** Identification of data protection incident
2. **Assessment:** Risk evaluation
3. **Containment:** Immediate measures to limit damage
4. **Notification:** Report to supervisory authority (if required)
5. **Communication:** Inform data subjects (if required)
6. **Investigation:** Root cause analysis
7. **Remediation:** Corrective measures
8. **Documentation:** Record in incident register
9. **Lessons Learned:** Process improvements

## Processes and Responsibilities

### RACI Matrix

| Activity | CIO | CISO | Ops Manager | DPO | Data Stewards |
|---|---|---|---|---|---|
| Data Classification | I | C | I | C | R/A |
| GDPR Compliance | A | R | C | C | I |
| Data Protection Impact Assessment | C | R | C | A | C |
| Data Retention | C | C | R | C | A |
| Data Deletion | I | C | R | C | A |
| Data Governance | A | C | C | C | R |
| Data Security | C | A | R | C | I |
| Data Protection Incidents | A | R | C | C | I |

> **Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

## Compliance and Standards

### Relevant Standards
- **GDPR:** EU General Data Protection Regulation
- **BDSG:** Federal Data Protection Act
- **ISO 27001:** Information Security Management
- **ISO 27701:** Privacy Information Management
- **NIST SP 800-88:** Guidelines for Media Sanitization

### Audit Requirements
- Record of processing activities
- Data protection impact assessments
- Data processing agreements
- Deletion proofs
- Audit logs

## Appendix

### Glossary

| Term | Definition |
|---|---|
| GDPR | General Data Protection Regulation of the EU |
| Personal Data | Data relating to an identifiable person |
| Data Steward | Functional data owner |
| Data Custodian | Technical data owner |
| DPIA | Data Protection Impact Assessment |
| Pseudonymization | Processing without attribution to a person without additional information |
| Anonymization | Irreversible removal of personal reference |

### References
- EU General Data Protection Regulation (GDPR)
- Federal Data Protection Act (BDSG)
- ISO/IEC 27001:2013
- ISO/IEC 27701:2019
- NIST SP 800-88 Rev. 1

**Last Update:** {{ meta-handbook.date }}  
**Next Review:** [TODO: Date]  
**Contact:** {{ meta-organisation-roles.role_CISO_email }}

