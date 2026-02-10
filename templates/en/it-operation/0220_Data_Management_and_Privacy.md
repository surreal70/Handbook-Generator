# Data Management and Privacy

## Overview

This document describes the processes and policies for data management and data protection in the IT service. It defines data classification, data protection requirements according to GDPR, data retention and deletion, as well as data governance structures.

**Document Owner:** {{ meta.document.owner }}  
**Approved by:** {{ meta.document.approver }}  
**Version:** {{ meta.document.version }}  
**Organization:** {{ meta.organization.name }}

---

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

---

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
| **Right of Access** | Information about stored data | 1 month | {{ meta.ciso.name }} |
| **Right to Rectification** | Correction of inaccurate data | Without delay | {{ meta.ciso.name }} |
| **Right to Erasure** | Deletion of personal data | Without delay | {{ meta.ciso.name }} |
| **Right to Restriction** | Restriction of processing | Without delay | {{ meta.ciso.name }} |
| **Right to Data Portability** | Transfer to another controller | 1 month | {{ meta.ciso.name }} |
| **Right to Object** | Object to processing | Without delay | {{ meta.ciso.name }} |

---

## Data Retention and Deletion

### Retention Periods

#### Legal Retention Periods

| Data Type | Retention Period | Legal Basis | Responsible |
|---|---|---|---|
| Business Letters | 6 years | HGB § 257 | {{ meta.cfo.name }} |
| Accounting Documents | 10 years | HGB § 257, AO § 147 | {{ meta.cfo.name }} |
| Annual Financial Statements | 10 years | HGB § 257 | {{ meta.cfo.name }} |
| Payroll Documents | 6 years | AO § 147 | {{ meta.cfo.name }} |
| Tax Documents | 10 years | AO § 147 | {{ meta.cfo.name }} |
| Personnel Files | 3-10 years | Various | {{ meta.coo.name }} |

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
| Hard Drives | Secure Erase / Degaussing | NIST SP 800-88 | {{ meta.it_operations_manager.name }} |
| SSDs | Crypto Erase / Destruction | NIST SP 800-88 | {{ meta.it_operations_manager.name }} |
| Backup Media | Overwrite / Destruction | NIST SP 800-88 | {{ meta.it_operations_manager.name }} |
| Cloud Data | API-based Deletion | Provider Standard | {{ meta.it_operations_manager.name }} |
| Databases | SQL DELETE / TRUNCATE | Database Standard | {{ meta.it_operations_manager.name }} |
| Paper | Shredding (P-4) | DIN 66399 | {{ meta.coo.name }} |

---

## Data Governance

### Governance Structure

#### Data Governance Board
- **Chair:** {{ meta.cio.name }}
- **Members:** {{ meta.ciso.name }}, {{ meta.cfo.name }}, Department Heads
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

---

## Data Security

### Encryption

#### Encryption at Rest (Data at Rest)

| Data Type | Encryption | Algorithm | Key Length | Responsible |
|---|---|---|---|---|
| Highly Confidential | Mandatory | AES | 256 Bit | {{ meta.ciso.name }} |
| Confidential | Mandatory | AES | 256 Bit | {{ meta.ciso.name }} |
| Internal | Recommended | AES | 128/256 Bit | {{ meta.it_operations_manager.name }} |
| Public | Not required | - | - | - |

#### Encryption in Transit (Data in Transit)

| Connection Type | Protocol | Minimum Version | Responsible |
|---|---|---|---|
| Web Traffic | HTTPS/TLS | TLS 1.2 | {{ meta.it_operations_manager.name }} |
| Email | TLS/S/MIME | TLS 1.2 | {{ meta.it_operations_manager.name }} |
| File Transfer | SFTP/FTPS | TLS 1.2 | {{ meta.it_operations_manager.name }} |
| VPN | IPsec/OpenVPN | - | {{ meta.it_operations_manager.name }} |
| Database | TLS | TLS 1.2 | {{ meta.it_operations_manager.name }} |

---

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

---

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

---

## Compliance and Standards

### Relevant Standards
- **GDPR:** EU General Data Protection Regulation
- **BDSG:** Federal Data Protection Act
- **ISO 27001:** Information Security Management
- **ISO 27701:** Privacy Information Management
- **NIST SP 800-88:** Guidelines for Media Sanitization

---

**Last Update:** {{ meta.date }}  
**Next Review:** [TODO: Date]  
**Contact:** {{ meta.ciso.email }}

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial Creation |
