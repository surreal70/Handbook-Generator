# Data Flow Diagrams

**Document ID:** PCI-0040  
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
This template documents cardholder data flows throughout the organization.
It aligns with PCI-DSS v4.0 Requirement 12.5.2 (Document and confirm PCI DSS scope).

Customization required:
- Create data flow diagrams showing all CHD flows
- Document all systems that handle cardholder data
- Include data flow from capture to storage/transmission/disposal
- Update diagrams when systems or processes change
-->

## 1. Purpose

This document visualizes all cardholder data (CHD) flows within {{ meta.organization.name }}.

### 1.1 Objectives

- **Transparency:** Complete visibility of all CHD flows
- **Scope Definition:** Identification of all PCI-DSS-relevant systems
- **Risk Assessment:** Detection of potential vulnerabilities
- **Compliance:** Meet PCI-DSS Requirement 12.5.2

## 2. Data Flow Overview

### 2.1 Main Data Flows

[TODO: Insert high-level data flow diagram - see diagrams/data_flow_overview.png]

**Data Flow Phases:**
1. **Capture:** Card input at POS/web form
2. **Transmission:** Transport for authorization
3. **Processing:** Authorization by acquiring bank
4. **Storage:** Persistence for reporting (if required)
5. **Deletion:** Secure disposal after retention period

### 2.2 Data Flow Categories

| Category | Description | Systems | Encryption |
|----------|-------------|---------|------------|
| Point of Sale | Card input in stores | POS Terminals | P2PE |
| E-Commerce | Online payments | Web Server, Payment Gateway | TLS 1.3 |
| Call Center | Phone orders | CRM, IVR | Tokenization |
| Recurring Billing | Recurring payments | Billing System | Tokenization |

## 3. Detailed Data Flows

### 3.1 Point-of-Sale Data Flow

[TODO: Insert POS data flow diagram]

**Steps:**
1. Customer presents card at POS terminal
2. Terminal reads card data (encrypted)
3. Encrypted data to payment gateway
4. Gateway sends to acquiring bank
5. Authorization response back to terminal
6. Receipt for customer

**Involved Systems:**
- POS Terminal: [TODO: Model/Vendor]
- Payment Gateway: [TODO: System ID]
- Acquiring Bank: [TODO: Bank Name]

**Data Protection:**
- P2PE (Point-to-Point Encryption)
- No storage of full track data
- Only last 4 digits on receipt

### 3.2 E-Commerce Data Flow

[TODO: Insert e-commerce data flow diagram]

**Steps:**
1. Customer enters card data in web form
2. HTTPS transmission to web server
3. Forward to payment gateway
4. Gateway tokenizes PAN
5. Token back to web server for storage
6. Authorization with token

**Involved Systems:**
- Web Server: [TODO: System ID]
- Payment Gateway: [TODO: System ID]
- Database: [TODO: System ID] (tokens only)

**Data Protection:**
- TLS 1.3 for transmission
- Tokenization before storage
- No storage of CVV2

### 3.3 Call Center Data Flow

[TODO: Insert call center data flow diagram]

**Steps:**
1. Customer provides card data by phone
2. Agent enters data in CRM (masked)
3. IVR system captures sensitive data
4. Direct transmission to payment gateway
5. Token back to CRM

**Involved Systems:**
- CRM System: [TODO: System ID]
- IVR System: [TODO: System ID]
- Payment Gateway: [TODO: System ID]

**Data Protection:**
- IVR for sensitive data entry
- No storage of PAN in CRM
- Only token stored

## 4. System Overview

### 4.1 Systems with CHD Access

| System ID | System Name | CHD Type | Function | Encryption |
|-----------|-------------|----------|----------|------------|
| [TODO: SYS-001] | POS Terminal | PAN (Transit) | Card Input | P2PE |
| [TODO: SYS-002] | Payment Gateway | PAN | Authorization | TLS 1.3 |
| [TODO: SYS-003] | Database | Token | Storage | AES-256 |
| [TODO: SYS-004] | Web Server | PAN (Transit) | E-Commerce | TLS 1.3 |

### 4.2 Data Transmission Protocols

| Connection | Protocol | Encryption | Port |
|------------|----------|------------|------|
| POS → Gateway | HTTPS | TLS 1.3 | 443 |
| Web → Gateway | HTTPS | TLS 1.3 | 443 |
| Gateway → Bank | HTTPS | TLS 1.3 | 443 |
| Gateway → DB | SQL/TLS | TLS 1.2+ | 3306 |

## 5. Data Storage

### 5.1 Stored Cardholder Data

| Data Type | Storage Location | Encryption | Retention Period | Justification |
|-----------|------------------|------------|------------------|---------------|
| PAN (Token) | Database | AES-256 | [TODO: 13 months] | Refunds |
| Cardholder Name | Database | AES-256 | [TODO: 13 months] | Refunds |
| Transaction Data | Database | AES-256 | [TODO: 7 years] | Accounting |

**Not Stored:**
- Full Track Data
- CVV2/CVC2/CID
- PIN/PIN Block

### 5.2 Data Deletion

**Deletion Process:**
1. Automatic identification of expired data
2. Secure deletion (overwrite/crypto-shredding)
3. Logging of deletion operations
4. Quarterly verification

**Responsible:** [TODO: Data Retention Manager]

## 6. External Data Flows

### 6.1 Acquiring Bank

**Bank:** [TODO: Bank Name]  
**Connection:** HTTPS/TLS 1.3  
**Data Type:** PAN, transaction data  
**Purpose:** Authorization and settlement  

### 6.2 Payment Processor

**Processor:** [TODO: Processor Name]  
**Connection:** HTTPS/TLS 1.3  
**Data Type:** PAN (encrypted)  
**Purpose:** Payment processing  

### 6.3 Tokenization Service

**Service:** [TODO: Service Name]  
**Connection:** HTTPS/TLS 1.3  
**Data Type:** PAN → Token  
**Purpose:** Scope reduction  

## 7. Data Flow Change Management

### 7.1 Change Process

**For changes to data flows:**
1. Update diagrams
2. PCI-DSS impact assessment
3. CISO approval
4. Document the change
5. Train affected employees

### 7.2 Change History

| Date | Change | Justification | Approved By |
|------|--------|---------------|-------------|
| [TODO: 2026-01-15] | Tokenization implemented | Scope reduction | [TODO: CISO] |

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial creation |

<!-- End of template -->
