# Appendix: Data Flows and Interfaces (Template)

**Document-ID:** [FRAMEWORK]-0720
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
This template documents data flows and interfaces for risk analysis and protection needs assessment.
Reference: BSI Standard 200-2 (Structure Analysis), BSI IT-Grundschutz-Kompendium: CON.1 Crypto Concept
-->

## 1. Purpose and Objectives

The documentation of data flows and interfaces of **{{ meta-organisation.name }}** supports:
- Protection Needs Assessment (Document 0060)
- Risk Analysis (Document 0090)
- Crypto Concept (Document 0340/0350)
- Data Protection Compliance (Document 0420/0430)

**Responsible:** {{ meta.ciso.name }} (CISO), {{ meta.cio.name }} (IT Management)

## 2. Data Flow Register

| Data Flow ID | Source | Destination | Data Types | Protection Need (C/I/A) | Transport Path | Encryption | Storage | Provider/Third Country | Owner | Legal Basis | Note |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DF-001 | Web Server ({{ netbox.device.name }}) | Database Server | Customer Data (personal) | Very High/High/High | {{ netbox.vlan.name }} (internal) | TLS 1.3 | Encrypted (AES-256) | Internal | {{ meta.cio.name }} | GDPR Art. 6(1)(b) | [TODO] |
| DF-002 | Backup Server | Cloud Storage (AWS S3) | Backup Data | High/High/High | Internet (VPN) | TLS 1.3 + AES-256 | Encrypted (AES-256) | AWS (EU-West-1) | {{ meta.cio.name }} | GDPR Art. 28 | [TODO] |
| DF-003 | Employee (Remote) | VPN Gateway | Business Data | High/High/Normal | Internet | IPsec/IKEv2 | N/A | Internal | {{ meta.cio.name }} | - | [TODO] |
| DF-004 | ERP System | Payment Gateway | Payment Data | Very High/Very High/High | Internet (HTTPS) | TLS 1.3 | Not Stored | Payment Provider (EU) | {{ meta.cio.name }} | PCI-DSS | [TODO] |
| DF-005 | SIEM | Log Archive | Log Data | Normal/High/Normal | {{ netbox.vlan.name }} (Management) | TLS 1.2 | Encrypted | Internal | {{ meta.ciso.name }} | - | [TODO] |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## 3. Interface Register

| Interface ID | System A | System B | Protocol | Port | Authentication | Encryption | Data Direction | Frequency | Owner | Note |
|---|---|---|---|---|---|---|---|---|---|---|
| IF-001 | Web Server | Database | PostgreSQL | 5432 | Certificate | TLS 1.3 | Bidirectional | Permanent | {{ meta.cio.name }} | [TODO] |
| IF-002 | ERP | CRM | REST API | 443 | OAuth 2.0 | TLS 1.3 | Bidirectional | Real-time | {{ meta.cio.name }} | [TODO] |
| IF-003 | Monitoring | SIEM | Syslog | 514 | Certificate | TLS 1.2 | Unidirectional | Permanent | {{ meta.ciso.name }} | [TODO] |
| IF-004 | AD | LDAP Clients | LDAPS | 636 | Kerberos | TLS 1.2 | Bidirectional | On-Demand | {{ meta.cio.name }} | [TODO] |
| IF-005 | Backup Server | Cloud Storage | S3 API | 443 | API Key | TLS 1.3 | Unidirectional | Daily | {{ meta.cio.name }} | [TODO] |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## 4. External Interfaces and Third Parties

| Third Party | Service | Data Types | Protection Need | Location/Third Country | Contract | Data Protection Agreement | Owner | Note |
|---|---|---|---|---|---|---|---|---|
| AWS | Cloud Hosting (EC2, S3) | Business Data, Backup | High/High/High | EU-West-1 | [TODO: Contract Number] | Yes (Art. 28 GDPR) | {{ meta.cio.name }} | [TODO] |
| Microsoft | Office 365 | Email, Documents | High/High/Normal | EU | [TODO] | Yes | {{ meta.cio.name }} | [TODO] |
| Payment Provider | Payment Processing | Payment Data | Very High/Very High/High | EU | [TODO] | Yes | {{ meta.cio.name }} | PCI-DSS certified |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

**Reference:** Document 0400/0410 (Supplier and Outsourcing Management)

## 5. Data Flow Diagrams

**Storage Location:** `diagrams/dataflows.png` or [TODO: Confluence/SharePoint]

**Recommended Diagrams:**
1. **High-Level Data Flow:** Overview of all main data flows
2. **Detailed Data Flows:** Per critical system/service
3. **External Data Flows:** All data flows to third parties
4. **Personal Data:** GDPR-relevant data flows

**Tools:** [TODO: e.g., Lucidchart, Draw.io, Visio]

## 6. Data Categories

### 6.1 Personal Data (GDPR)
- Customer Data (name, address, email, etc.)
- Employee Data (HR data)
- Special Categories (Art. 9 GDPR): [TODO: if applicable]

### 6.2 Business Data
- Contracts
- Financial Data
- Trade Secrets
- Strategic Documents

### 6.3 Technical Data
- Log Data
- Monitoring Data
- Configuration Data

### 6.4 Public Data
- Marketing Materials
- Public Website Content

## 7. Encryption Requirements

| Data Type | Protection Need | Transport Encryption | Storage Encryption | Key Management |
|---|---|---|---|---|
| Personal Data | Very High | TLS 1.3 (min. TLS 1.2) | AES-256 | HSM/KMS |
| Business Data | High | TLS 1.3 (min. TLS 1.2) | AES-256 | KMS |
| Log Data | Normal | TLS 1.2 | Optional | KMS |
| Public Data | Normal | TLS 1.2 | Not Required | - |

**Reference:** Document 0340/0350 (Cryptography and Key Management)

## 8. Cross-Border Data Transfer

**Data Transfer to Third Countries:**

| Destination Country | Data Types | Legal Basis | Safeguards | Approval | Note |
|---|---|---|---|---|---|
| USA | [TODO] | Standard Contractual Clauses (SCC) | [TODO] | [TODO] | [TODO] |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

**Reference:** Document 0420/0430 (Data Protection)

## 9. Responsibilities (RACI)

| Activity | IT Management | CISO | Data Protection Officer | Business Unit |
|---|---|---|---|---|
| Document Data Flows | A | C | C | R |
| Determine Protection Need | A | R | C | C |
| Implement Encryption | R | C | I | I |
| Review Third-Party Contracts | C | C | R | A |
| Annual Review | A | R | C | C |

**Legend:**
- **R** = Responsible (Execution responsibility)
- **A** = Accountable (Overall responsibility)
- **C** = Consulted
- **I** = Informed

## 10. Change Management

**Changes to Data Flows:**
- New data flows must be documented before commissioning
- Changes to existing data flows require change ticket
- Security-relevant changes require CISO approval

**Reference:** Document 0380/0390 (Change Management)

## 11. Approval

| Role | Name | Date | Approval |
|---|---|---|---|
| CISO | {{ meta.ciso.name }} | {{ meta-handbook.modifydate }} | {{ meta-handbook.status }} |
| IT Management | {{ meta.cio.name }} | {{ meta-handbook.modifydate }} | {{ meta-handbook.status }} |
| Data Protection Officer | [TODO] | {{ meta-handbook.modifydate }} | {{ meta-handbook.status }} |

**References:**
- BSI Standard 200-2: IT-Grundschutz Methodology (Structure Analysis)
- BSI IT-Grundschutz-Kompendium: CON.1 Crypto Concept
- Document 0050: Structure Analysis
- Document 0060: Protection Needs Assessment
- Document 0090: Risk Analysis
- Document 0340/0350: Cryptography and Key Management
- Document 0420/0430: Data Protection

<!-- End of template -->