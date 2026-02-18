# Guideline: Data Classification, Labeling and Handling

**Document-ID:** [FRAMEWORK]-0290
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Approved by:** {{ meta-handbook.approver }}
**Revision:** [TODO]
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Classification:** {{ meta-handbook.classification }}
**Last Update:** {{ meta-handbook.modifydate }}
**Template Version:** [TODO]

---

---

## 1. Purpose and Scope

This guideline implements the `0280_Policy_Data_Classification_and_Information_Handling.md` and defines:
- Classification levels and criteria
- Labeling procedures for documents and emails
- Handling requirements per classification level

**Scope:** All information at **{{ meta-organisation.name }}**

## 2. Classification Levels

### 2.1 Public

**Definition:** Information intended for public distribution

**Examples:**
- Marketing materials, press releases
- Public website content
- Product documentation

**Handling:**
- No access restrictions
- No encryption required
- Free distribution permitted

### 2.2 Internal

**Definition:** Information for internal use, not for the public

**Examples:**
- Internal process documentation
- Organizational structures
- General business communication

**Handling:**
- Access only for employees and authorized third parties
- No encryption required (except for external transmission)
- Sharing with third parties only with NDA

### 2.3 Confidential

**Definition:** Sensitive business information, damage upon disclosure

**Examples:**
- Contracts, proposals
- Personnel data
- Financial reports (internal)
- Customer data

**Handling:**
- Access only on need-to-know basis
- Encryption for transmission and storage
- Sharing only with approval
- Secure destruction required

### 2.4 Highly Confidential

**Definition:** Highly sensitive information, significant damage upon disclosure

**Examples:**
- Trade secrets, M&A plans
- Strategic plans
- Security concepts
- Critical infrastructure data

**Handling:**
- Access only for authorized persons (explicit approval)
- Encryption mandatory (at rest and in transit)
- No email transmission without encryption
- Physical documents in safe
- Secure destruction per DIN 66399 P-5

## 3. Classification Process

### 3.1 Responsibilities

**Data Owner:**
- Classification of new information
- Review and adjustment upon changes
- Approval of access

**Creator:**
- Application of classification during document creation
- Labeling per guidelines
- Compliance with handling requirements

**IT Operations:**
- Technical implementation (DLP, encryption)
- Monitoring and compliance checks

### 3.2 Classification Criteria

**Questions for Determination:**
1. What damage occurs upon disclosure?
2. Are there legal/regulatory requirements?
3. Who needs access (public, employees, specific persons)?
4. How long must data be retained?

**Decision Tree:**
- Intended for public? → Public
- Only internally relevant? → Internal
- Business damage upon disclosure? → Confidential
- Significant damage or legal obligation? → Highly Confidential

## 4. Labeling Procedures

### 4.1 Documents

**Microsoft Office:**
- Sensitivity labels in Office 365
- Automatic application via DLP rules
- Header/footer with classification

**PDF:**
- Watermark with classification
- Metadata tags

**Physical Documents:**
- Stamp or print on each page
- Color coding (e.g., red for Highly Confidential)

### 4.2 Emails

**Subject Line:**
- Prefix: [CONFIDENTIAL], [HIGHLY CONFIDENTIAL]
- Automatic via email client

**Email Body:**
- Disclaimer in footer
- Encryption for Confidential/Highly Confidential

**Outlook Integration:**
- Sensitivity labels
- Automatic encryption upon classification

### 4.3 Digital Assets

**File Systems:**
- Metadata tags
- Separate folder structures per classification
- Access control via ACLs

**Databases:**
- Column-level classification
- Row-level security
- Audit logging for access

## 5. Handling Requirements

### 5.1 Storage

| Classification | Storage Location | Encryption | Access Control |
|----------------|------------------|------------|----------------|
| Public | Any | Optional | None |
| Internal | Approved systems | For external storage | Employees |
| Confidential | Approved systems | Mandatory | Need-to-know |
| Highly Confidential | Dedicated systems | Mandatory (AES-256) | Explicit approval |

### 5.2 Transmission

| Classification | Email | File Transfer | Physical |
|----------------|-------|---------------|----------|
| Public | Unencrypted OK | Any | No requirements |
| Internal | TLS recommended | SFTP/HTTPS | Sealed envelopes |
| Confidential | S/MIME mandatory | SFTP/HTTPS encrypted | Registered mail, sealed |
| Highly Confidential | S/MIME + approval | Dedicated channels | Courier, personal handover |

### 5.3 Destruction

| Classification | Digital | Paper | Storage Media |
|----------------|---------|-------|---------------|
| Public | Normal deletion | Trash | Normal deletion |
| Internal | Secure deletion | Shredder P-3 | Secure deletion |
| Confidential | Cryptographic deletion | Shredder P-4 | Degaussing + destruction |
| Highly Confidential | Cryptographic deletion | Shredder P-5 | Physical destruction |

## 6. Data Loss Prevention (DLP)

### 6.1 DLP Rules

**Automatic Detection:**
- Credit card numbers, social security numbers
- Documents with "Confidential" label
- Personal data (GDPR)

**Actions:**
- **Warning:** When sending Internal-classified data externally
- **Blocking:** When sending Confidential/Highly Confidential without encryption
- **Quarantine:** On suspected data leak

### 6.2 Monitoring

**Monitored Channels:**
- Email (outgoing)
- Cloud uploads (OneDrive, SharePoint)
- USB devices
- Printers

**Alerts:**
- Automatic notification to security team
- Incident creation for critical violations

## 7. Training and Awareness

**Mandatory Training:**
- Onboarding: Data classification basics
- Annually: Refresher and updates

**Awareness Materials:**
- Posters with classification levels
- Quick reference cards
- Intranet articles

## 8. Compliance and Audit

### 8.1 Key Performance Indicators (KPIs)

| Metric | Target Value |
|--------|--------------|
| Classified Documents | > 80% |
| DLP Incidents | < 10 per month |
| Training Participation | 100% |

### 8.2 Audit Evidence

- Classification register
- DLP logs and incidents
- Training records
- Access logs

## 9. References

### Internal Documents
- `0280_Policy_Data_Classification_and_Information_Handling.md`
- `0320_Policy_Logging_und_Monitoring.md`

### External Standards
- **ISO/IEC 27001:2022 Annex A.5.12** - Classification of information
- **ISO/IEC 27001:2022 Annex A.5.13** - Labelling of information
- **DIN 66399** - Destruction of data carriers

**Approved by:** {{ meta.ciso.name }}, CISO  
**Next Review:** {{ meta-handbook.next_review }}

