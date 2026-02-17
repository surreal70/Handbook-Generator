# User and Device Authentication

**Document-ID:** [FRAMEWORK]-0410
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

## 1. Control Description

This document covers user and device authentication controls:
- **IA-2:** Identification and Authentication (Organizational Users)
- **IA-3:** Device Identification and Authentication
- **IA-4:** Identifier Management
- **IA-6:** Authentication Feedback
- **IA-8:** Identification and Authentication (Non-Organizational Users)

## 2. Control Implementation

### 2.1 User Authentication (IA-2)

**Authentication Methods:**
- Username and password
- Multi-factor authentication (MFA)
- Biometric authentication
- Smart cards/tokens
- Certificate-based authentication

[TODO: Specify authentication methods by system/application]

**MFA Requirements:**
| System/Application | MFA Required | MFA Type |
|-------------------|--------------|----------|
| [TODO] | Yes/No | [TODO: SMS, App, Hardware token] |

### 2.2 Device Authentication (IA-3)

**Device Types:**
- Workstations
- Servers
- Mobile devices
- Network devices
- IoT devices

[TODO: Define device authentication requirements]

**Authentication Mechanisms:**
- Device certificates
- MAC address filtering
- Network access control (NAC)
- Device registration

[TODO: Specify mechanisms]

### 2.3 Identifier Management (IA-4)

**Identifier Assignment:**
- Unique identifiers for each user
- Naming conventions: [TODO: Define]
- Identifier reuse policy: [TODO: Define]

**Identifier Lifecycle:**
1. Creation
2. Assignment
3. Modification
4. Suspension
5. Deletion

[TODO: Define lifecycle procedures]

**Identifier Types:**
| Identifier Type | Format | Example |
|----------------|--------|---------|
| User ID | [TODO] | [TODO] |
| Service Account | [TODO] | [TODO] |
| Device ID | [TODO] | [TODO] |

### 2.4 Authentication Feedback (IA-6)

**Feedback Restrictions:**
- No password display during entry
- Generic error messages for failed authentication
- No indication of which credential failed
- Masking of authentication information

[TODO: Define feedback restrictions]

### 2.5 Non-Organizational User Authentication (IA-8)

**External User Types:**
- Contractors
- Partners
- Customers
- Vendors
- Public users

[TODO: Define external user types]

**Authentication Requirements:**
| User Type | Authentication Method | Access Level |
|-----------|----------------------|--------------|
| [TODO] | [TODO] | [TODO] |

**Federated Authentication:**
- Supported identity providers: [TODO: List]
- Federation protocols: SAML, OAuth, OpenID Connect
- Trust relationships: [TODO: Define]

## 3. Control Enhancements

- **IA-2(1):** Multi-Factor Authentication to Privileged Accounts
- **IA-2(2):** Multi-Factor Authentication to Non-Privileged Accounts
- **IA-2(5):** Individual Authentication with Group Authentication
- **IA-2(6):** Access to Accounts - Separate Device
- **IA-2(8):** Access to Accounts - Replay Resistant
- **IA-2(12):** Acceptance of PIV Credentials
- **IA-3(1):** Cryptographic Bidirectional Authentication
- **IA-3(4):** Device Attestation
- **IA-4(4):** Identify User Status
- **IA-8(1):** Acceptance of PIV Credentials from Other Agencies
- **IA-8(2):** Acceptance of External Authenticators
- **IA-8(4):** Use of Defined Profiles

[TODO: Mark applicable enhancements]

## 4. Implementation Status

**Status:** [TODO: Implemented / Partially Implemented / Planned / Not Applicable]  
**Implementation Date:** [TODO: Date]  
**Responsible:** [TODO: Name/Role]  

## 5. Assessment

**Assessment Method:** Examine, Interview, Test  
**Assessment Status:** [TODO: Satisfied / Other than Satisfied / Not Applicable]  
**Findings:** [TODO: Description]  

<!-- End of template -->
