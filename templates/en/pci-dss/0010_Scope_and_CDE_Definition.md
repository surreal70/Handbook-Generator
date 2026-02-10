# Scope and CDE Definition

**Document ID:** PCI-0010  
**Organization:** {{ meta.organization.name }}  
**Owner:** {{ meta.document.owner }}  
**Approved by:** {{ meta.document.approver }}  
**Version:** {{ meta.document.version }}  
**Status:** Draft / In Review / Approved  
**Classification:** {{ meta.document.classification }}  
**Last Updated:** {{ meta.document.last_updated }}  

---

<!-- 
TEMPLATE AUTHOR NOTE:
This template defines the scope of PCI-DSS compliance and the Cardholder Data Environment (CDE).
It aligns with PCI-DSS v4.0 Requirement 12.5.2 (Scope of PCI-DSS Assessment).

Customization required:
- Define all systems that store, process, or transmit cardholder data
- Document network segmentation boundaries
- List all locations where cardholder data is present
- Identify all personnel with access to cardholder data
-->

## 1. Purpose

This document defines the scope of PCI-DSS compliance for {{ meta.organization.name }} and describes the Cardholder Data Environment (CDE).

### 1.1 Objectives

- **Scope Definition:** Clear delineation of the CDE from the rest of the network
- **Compliance Focus:** Identification of all PCI-DSS-relevant systems and processes
- **Risk Minimization:** Reduction of compliance scope through segmentation
- **Audit Preparation:** Documentation for QSA assessments

### 1.2 References

- **PCI-DSS v4.0:** Requirements 1, 2, 11, 12
- **PCI-DSS Information Supplement:** Guidance for PCI DSS Scoping and Network Segmentation
- **PA-DSS:** Payment Application Data Security Standard (if applicable)

## 2. Merchant/Service Provider Information

### 2.1 Organization Information

**Organization:** {{ meta.organization.name }}  
**Address:** {{ meta.organization.address }}, {{ meta.organization.postal_code }} {{ meta.organization.city }}  
**Country:** {{ meta.organization.country }}  
**Website:** {{ meta.organization.website }}  

### 2.2 PCI-DSS Classification

**Merchant Level:** [TODO: Level 1/2/3/4]  
**Service Provider Level:** [TODO: Level 1/2 or N/A]  
**Merchant ID:** {{ meta.pci.merchant_id }}  
**Service Provider ID:** {{ meta.pci.service_provider_id }}  

**Transaction Volume (annual):**
- Visa: [TODO: Number of transactions]
- Mastercard: [TODO: Number of transactions]
- American Express: [TODO: Number of transactions]
- Discover: [TODO: Number of transactions]
- Total: [TODO: Number of transactions]

### 2.3 Acquiring Banks

| Bank Name | Contact | Merchant ID | Card Brands |
|-----------|---------|-------------|-------------|
| [TODO: Bank 1] | [TODO: Contact] | [TODO: ID] | Visa, Mastercard |
| [TODO: Bank 2] | [TODO: Contact] | [TODO: ID] | American Express |

## 3. Cardholder Data Environment (CDE)

### 3.1 CDE Definition

The Cardholder Data Environment (CDE) includes:

1. **Systems:** All systems that store, process, or transmit cardholder data (CHD)
2. **Networks:** All network segments connected to CDE systems
3. **People:** All employees and service providers with access to CHD
4. **Processes:** All business processes involving CHD

### 3.2 Cardholder Data (CHD)

**Primary Account Number (PAN):**
- 13-19 digit card number
- **Storage:** [TODO: Yes/No, where?]
- **Encryption:** [TODO: Algorithm, e.g., AES-256]

**Cardholder Name:**
- Name of cardholder
- **Storage:** [TODO: Yes/No, where?]

**Service Code:**
- 3-digit code on magnetic stripe
- **Storage:** [TODO: Yes/No, where?]

**Expiration Date:**
- Card validity date
- **Storage:** [TODO: Yes/No, where?]

### 3.3 Sensitive Authentication Data (SAD)

**MUST NOT be stored after authorization:**

- **Full Track Data:** Magnetic stripe data (Track 1, Track 2)
- **CAV2/CVC2/CVV2/CID:** Card verification value (3-4 digits)
- **PIN/PIN Block:** PIN data

**Confirmation:** {{ meta.organization.name }} does NOT store Sensitive Authentication Data after authorization. [TODO: Confirm]

## 4. CDE Systems and Components

### 4.1 Systems in CDE

| System ID | System Name | Type | Function | CHD Type | Location |
|-----------|-------------|------|----------|----------|----------|
| [TODO: SYS-001] | [TODO: Payment Gateway] | Server | Payment processing | PAN, Name | [TODO: DC1] |
| [TODO: SYS-002] | [TODO: POS Terminal] | Endpoint | Card input | PAN | [TODO: Branch 1] |
| [TODO: SYS-003] | [TODO: Database] | Database | CHD storage | PAN (encrypted) | [TODO: DC1] |
| [TODO: SYS-004] | [TODO: Web Server] | Server | E-Commerce | PAN (transit) | [TODO: DC1] |

### 4.2 Network Components in CDE

| Component | Type | Function | Location |
|-----------|------|----------|----------|
| [TODO: FW-CDE-01] | Firewall | CDE segmentation | [TODO: DC1] |
| [TODO: SW-CDE-01] | Switch | CDE network | [TODO: DC1] |
| [TODO: RTR-CDE-01] | Router | CDE routing | [TODO: DC1] |
| [TODO: IDS-CDE-01] | IDS/IPS | Intrusion detection | [TODO: DC1] |

### 4.3 Applications in CDE

| Application | Version | Vendor | PA-DSS Certified | Function |
|-------------|---------|--------|------------------|----------|
| [TODO: Payment App] | [TODO: v2.1] | [TODO: Vendor] | [TODO: Yes/No] | Payment processing |
| [TODO: POS Software] | [TODO: v3.0] | [TODO: Vendor] | [TODO: Yes/No] | Point of sale |
| [TODO: E-Commerce] | [TODO: v1.5] | [TODO: Vendor] | [TODO: Yes/No] | Online shop |

## 5. Locations

### 5.1 Physical Locations with CDE

| Location ID | Location Name | Address | CDE Systems | Staff with CHD Access |
|-------------|---------------|---------|-------------|----------------------|
| [TODO: LOC-01] | Headquarters | [TODO: Address] | [TODO: List] | [TODO: Number] |
| [TODO: LOC-02] | Data Center | [TODO: Address] | [TODO: List] | [TODO: Number] |
| [TODO: LOC-03] | Branch 1 | [TODO: Address] | [TODO: POS] | [TODO: Number] |

### 5.2 Remote Access to CDE

**Remote Access Allowed:** [TODO: Yes/No]

If yes:
- **Access Method:** [TODO: VPN, Jump Server, etc.]
- **Multi-Factor Authentication:** [TODO: Yes/No, Method]
- **Authorized Users:** [TODO: Roles/Persons]

## 6. Data Flows

### 6.1 Cardholder Data Flows

[TODO: Insert data flow diagram - see PCI-0040]

**Main Data Flows:**

1. **Card Input → Authorization:**
   - Source: [TODO: POS Terminal/Web Form]
   - Destination: [TODO: Payment Gateway]
   - Protocol: [TODO: TLS 1.2+]
   - Encryption: [TODO: Yes/No]

2. **Authorization → Storage:**
   - Source: [TODO: Payment Gateway]
   - Destination: [TODO: Database]
   - Encryption: [TODO: AES-256]
   - Tokenization: [TODO: Yes/No]

3. **Reporting/Query:**
   - Source: [TODO: Database]
   - Destination: [TODO: Reporting System]
   - Masking: [TODO: Yes, last 4 digits only]

### 6.2 External Connections

| Connection | Source | Destination | Purpose | Encryption |
|------------|--------|-------------|---------|------------|
| [TODO: Acquiring Bank] | CDE | Bank | Authorization | TLS 1.2+ |
| [TODO: Payment Processor] | CDE | Processor | Processing | TLS 1.2+ |
| [TODO: ASV Scans] | Internet | CDE | Vulnerability scans | N/A |

## 7. Scope Exclusions

### 7.1 Systems Outside CDE

The following systems are NOT part of the CDE:

| System | Justification | Segmentation |
|--------|---------------|--------------|
| [TODO: Intranet] | No CHD processing | Firewall separation |
| [TODO: Email Server] | No CHD storage | Separate VLAN |
| [TODO: Development] | No production data | Physically separated |

### 7.2 Excluded Locations

[TODO: List locations that do not process CHD]

## 8. Network Segmentation

### 8.1 Segmentation Strategy

**Segmentation Method:** [TODO: VLAN, Firewall, physical separation]

**CDE Segments:**
- **CDE-Core:** Systems with CHD storage
- **CDE-DMZ:** Systems with CHD transit (no storage)
- **Management:** Administrative systems for CDE

**Non-CDE Segments:**
- **Corporate:** Office network
- **Guest:** Guest WiFi
- **Development:** Development environment

### 8.2 Segmentation Validation

**Last Validation:** [TODO: Date]  
**Performed by:** [TODO: Name/Company]  
**Method:** [TODO: Penetration test, Network scan]  
**Result:** [TODO: Successful/Failed]  
**Next Validation:** [TODO: Date]

## 9. Personnel with CDE Access

### 9.1 Roles with CHD Access

| Role | Number of People | Access Level | Justification |
|------|------------------|--------------|---------------|
| [TODO: Payment Admin] | [TODO: 2] | Full | Administration |
| [TODO: Cashier] | [TODO: 10] | Limited | POS operation |
| [TODO: Support] | [TODO: 3] | Query only | Customer service |

### 9.2 Service Providers with CDE Access

| Service Provider | Purpose | Access Method | PCI-DSS Status |
|------------------|---------|---------------|----------------|
| [TODO: Payment Processor] | Payment processing | API | AOC available |
| [TODO: Hosting Provider] | Server hosting | Remote admin | AOC available |
| [TODO: QSA] | Audit | On-site | N/A |

## 10. Scope Changes

### 10.1 Change Management

**Process for Scope Changes:**

1. **Identification:** New systems/processes with CHD
2. **Assessment:** Check PCI-DSS relevance
3. **Documentation:** Update scope document
4. **Approval:** CISO approval required
5. **Implementation:** Apply PCI-DSS controls

### 10.2 Change History

| Date | Change | Justification | Approved by |
|------|--------|---------------|-------------|
| [TODO: 2026-01-15] | New POS system | Branch expansion | [TODO: CISO] |
| [TODO: 2026-02-01] | Tokenization | Scope reduction | [TODO: CISO] |

## 11. Compliance Responsibilities

### 11.1 Responsible Persons

**PCI-DSS Program Manager:** [TODO: Name] ([TODO: Email])  
**CISO:** {{ meta.roles.ciso.name }} ({{ meta.roles.ciso.email }})  
**IT Manager:** [TODO: Name] ([TODO: Email])  
**QSA (Qualified Security Assessor):** [TODO: Company/Name]  
**ASV (Approved Scanning Vendor):** [TODO: Company]  

### 11.2 RACI Matrix

| Activity | PCI Manager | CISO | IT Manager | QSA |
|----------|-------------|------|------------|-----|
| Scope definition | A | C | R | I |
| Network segmentation | C | A | R | I |
| Compliance monitoring | R | A | C | I |
| Annual assessment | C | A | I | R |

**Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial creation |

<!-- End of template -->
