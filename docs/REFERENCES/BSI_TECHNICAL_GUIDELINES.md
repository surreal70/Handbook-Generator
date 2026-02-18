# BSI Technical Guidelines Reference

**Document Version:** 1.0  
**Last Updated:** 2026-02-18  
**Purpose:** Comprehensive reference for BSI (Bundesamt für Sicherheit in der Informationstechnik) technical guidelines covering cryptography, IT security, telecommunications, and German-specific IT standards

---

## Overview

This document provides a comprehensive reference to technical guidelines and publications from the BSI (Federal Office for Information Security, Germany). These publications provide detailed technical guidance for implementing IT security in accordance with German and European requirements.

**BSI (Bundesamt für Sicherheit in der Informationstechnik):**
- German Federal Office for Information Security
- National cyber security authority
- Part of the Federal Ministry of the Interior
- Responsible for IT security standards in Germany

**Coverage Areas:**
- Cryptography and Key Management
- IT Security Standards and Methodologies
- Telecommunications Security
- Cloud Computing Security
- Electronic Identity and Signatures
- Smart Cards and Chip Cards
- Network Security
- Web Application Security
- Email Security
- Mobile Device Security
- Industrial Control Systems
- Secure Software Development
- Quantum-Safe Cryptography
- eGovernment Security

---

## 1. BSI Technical Guidelines (Technische Richtlinien - TR)

### Overview of TR Series

BSI Technical Guidelines (TR) provide binding technical specifications and recommendations for IT security implementations in Germany. They are particularly important for:
- Federal agencies and authorities
- Critical infrastructure operators
- Qualified trust service providers
- Organizations seeking BSI certification

---

## 2. Cryptography Standards

### BSI TR-02102 - Cryptographic Mechanisms

**Full Title:** Kryptographische Verfahren: Empfehlungen und Schlüssellängen (Cryptographic Mechanisms: Recommendations and Key Lengths)  
**Current Version:** Part 1-4  
**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr02102/tr02102_node.html

**Description:**
Comprehensive guideline for cryptographic mechanisms approved for use in German federal IT systems. Provides recommendations for algorithms, key lengths, and protocols.

**Parts:**

#### TR-02102-1: Cryptographic Mechanisms - Recommendations and Key Lengths

**Content:**
- Approved cryptographic algorithms
- Minimum key lengths for different security levels
- Algorithm lifecycle and deprecation timelines
- Quantum computer resistance considerations

**Security Levels:**
- **Legacy:** < 100 bits (deprecated)
- **Near-term (2023+):** ≥ 100 bits
- **Long-term (2024+):** ≥ 120 bits
- **Future (post-quantum):** Quantum-resistant algorithms

**Symmetric Encryption:**
- AES-128, AES-192, AES-256
- Minimum: AES-128 for near-term, AES-256 recommended for long-term

**Asymmetric Encryption:**
- RSA: Minimum 3000 bits (near-term), 4000 bits (long-term)
- ECC: Minimum 250 bits (near-term), 500 bits (long-term)
- Curves: Brainpool curves preferred

**Hash Functions:**
- SHA-2 family (SHA-256, SHA-384, SHA-512)
- SHA-3 family
- Minimum: SHA-256

**Digital Signatures:**
- RSA-PSS, ECDSA, EdDSA
- Key lengths as per asymmetric encryption


**Framework Support:**
- 🔗 **Related:** ISO 27001 (A.8.24), NIST SP 800-57, NIST SP 800-131A
- 📝 **Guidance:** Cryptographic algorithm selection for German federal systems
- ✅ **Templates:** [templates/de/isms/](../templates/de/isms/), [templates/de/bsi-grundschutz/](../templates/de/bsi-grundschutz/)

---

#### TR-02102-2: Use of Transport Layer Security (TLS)

**Content:**
- TLS protocol versions and configuration
- Cipher suite recommendations
- Certificate requirements
- Implementation guidance

**TLS Versions:**
- **Mandatory:** TLS 1.2 minimum
- **Recommended:** TLS 1.3
- **Prohibited:** SSL 2.0, SSL 3.0, TLS 1.0, TLS 1.1

**Cipher Suites (TLS 1.2):**
- ECDHE with AES-GCM
- DHE with AES-GCM
- Forward Secrecy required

**Cipher Suites (TLS 1.3):**
- TLS_AES_128_GCM_SHA256
- TLS_AES_256_GCM_SHA384
- TLS_CHACHA20_POLY1305_SHA256

**Certificate Requirements:**
- RSA ≥ 3000 bits or ECC ≥ 250 bits
- SHA-256 or stronger for signatures
- Valid certificate chain
- Proper hostname verification

**Framework Support:**
- 🔗 **Related:** NIST SP 800-52, ISO 27001 (A.8.24)
- 📝 **Guidance:** TLS configuration for web services and APIs
- ✅ **Templates:** Network security, communications protection templates

---

#### TR-02102-3: Use of Internet Protocol Security (IPsec) and Internet Key Exchange (IKEv2)

**Content:**
- IPsec configuration recommendations
- IKEv2 protocol settings
- Cryptographic algorithm selection for VPNs
- Authentication methods

**IPsec Modes:**
- Transport mode
- Tunnel mode

**IKEv2 Configuration:**
- Diffie-Hellman groups (≥ Group 15 for near-term)
- Encryption algorithms (AES-128-GCM minimum)
- Integrity algorithms (SHA-256 minimum)
- PRF algorithms

**Authentication:**
- Certificate-based (preferred)
- Pre-shared keys (with strong keys)

**Framework Support:**
- 🔗 **Related:** NIST SP 800-77, BSI TR-02102-1
- 📝 **Guidance:** VPN security configuration
- ✅ **Templates:** Network security, remote access templates

---

#### TR-02102-4: Use of Secure Shell (SSH)

**Content:**
- SSH protocol configuration
- Key exchange algorithms
- Encryption and MAC algorithms
- Authentication methods

**SSH Version:**
- SSH-2 only (SSH-1 prohibited)

**Key Exchange:**
- curve25519-sha256
- ecdh-sha2-nistp256/384/521
- diffie-hellman-group-exchange-sha256

**Encryption:**
- chacha20-poly1305@openssh.com
- aes128-gcm@openssh.com
- aes256-gcm@openssh.com
- aes128-ctr, aes192-ctr, aes256-ctr

**MAC Algorithms:**
- hmac-sha2-256
- hmac-sha2-512

**Authentication:**
- Public key authentication (preferred)
- Password authentication (with strong passwords)
- Certificate-based authentication

**Framework Support:**
- 🔗 **Related:** CIS Controls, NIST 800-53 (AC, IA families)
- 📝 **Guidance:** Secure remote administration
- ✅ **Templates:** Access control, remote access templates

---

### BSI TR-03116 - eCard-API-Framework

**Full Title:** eCard-API-Framework  
**Current Version:** Multiple parts  
**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr03116/TR-03116_node.html

**Description:**
Specifies interfaces and protocols for electronic identity cards (eID) and electronic signature cards in Germany. Foundation for the German eID infrastructure.

**Parts:**
- TR-03116-1: Architecture
- TR-03116-2: Protocols
- TR-03116-3: Data structures
- TR-03116-4: Transport protocols
- TR-03116-5: Test specifications

**Use Cases:**
- German eID card (Personalausweis)
- Electronic residence permit (eAT)
- Qualified electronic signatures
- eGovernment services
- Online authentication

**Framework Support:**
- 🔗 **Related:** eIDAS regulation, NIST SP 800-63
- 📝 **Guidance:** Electronic identity implementation
- ✅ **Templates:** Identity management, authentication templates

---

### BSI TR-03107 - Electronic Signatures and Infrastructure

**Full Title:** Elektronische Signaturen und Infrastrukturen (Electronic Signatures and Infrastructures)  
**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr03107/tr03107_node.html

**Description:**
Technical requirements for electronic signatures and public key infrastructure (PKI) in accordance with German and European law.

**Parts:**
- TR-03107-1: Algorithms and parameters for electronic signatures
- TR-03107-2: Signature creation devices
- TR-03107-3: Signature verification

**Signature Types:**
- Simple electronic signature
- Advanced electronic signature (AdES)
- Qualified electronic signature (QES)

**Standards:**
- CAdES (CMS Advanced Electronic Signatures)
- XAdES (XML Advanced Electronic Signatures)
- PAdES (PDF Advanced Electronic Signatures)

**Framework Support:**
- 🔗 **Related:** eIDAS regulation, ETSI standards
- 📝 **Guidance:** Digital signature implementation
- ✅ **Templates:** Cryptography, document management templates

---

### BSI TR-03110 - Advanced Security Mechanisms for Machine Readable Travel Documents

**Full Title:** Advanced Security Mechanisms for Machine Readable Travel Documents and eIDAS Token  
**Current Version:** Multiple parts  
**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr03110/tr03110_node.html

**Description:**
Specifies cryptographic protocols for secure communication with electronic passports and identity documents.

**Parts:**
- TR-03110-1: Protocols (PACE, TA, CA, RI)
- TR-03110-2: Protocols for eIDAS tokens
- TR-03110-3: Common specifications
- TR-03110-4: Test specifications

**Protocols:**
- **PACE:** Password Authenticated Connection Establishment
- **TA:** Terminal Authentication
- **CA:** Chip Authentication
- **RI:** Restricted Identification
- **EAC:** Extended Access Control

**Applications:**
- Electronic passports (ePass)
- Electronic ID cards
- Electronic residence permits
- Border control systems
- eGovernment authentication

**Framework Support:**
- 🔗 **Related:** ICAO standards, ISO/IEC 7816
- 📝 **Guidance:** Secure document authentication
- ✅ **Templates:** Identity management, physical security templates

---

### BSI TR-03109 - Smart Metering PKI

**Full Title:** Smart Metering PKI  
**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr03109/tr03109_node.html

**Description:**
Technical requirements for the public key infrastructure used in German smart metering systems (Smart Meter Gateway).

**Content:**
- PKI architecture for smart metering
- Certificate profiles
- Certificate lifecycle management
- Cryptographic requirements
- Security requirements for CAs

**Framework Support:**
- 🔗 **Related:** BSI TR-03116, critical infrastructure security
- 📝 **Guidance:** Smart grid security, IoT PKI
- ✅ **Templates:** ICS/OT security, PKI templates

---

### BSI TR-03148 - Secure Broadband Router

**Full Title:** Sichere Breitband-Router (Secure Broadband Router)  
**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr03148/TR-03148_node.html

**Description:**
Security requirements for broadband routers used in home and small office environments.

**Requirements:**
- Secure boot and firmware updates
- Strong default passwords (no universal defaults)
- Automatic security updates
- Secure remote administration
- Firewall functionality
- VPN support
- Logging capabilities
- User authentication

**Testing:**
- Vulnerability assessment
- Penetration testing
- Compliance verification

**Framework Support:**
- 🔗 **Related:** CIS Controls, IoT security
- 📝 **Guidance:** Network device security
- ✅ **Templates:** Network security, device hardening templates

---

### BSI TR-03161 - Security Requirements for eHealth Applications

**Full Title:** Sicherheitsanforderungen an eHealth-Anwendungen (Security Requirements for eHealth Applications)  
**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr03161/tr03161_node.html

**Description:**
Security requirements for electronic health applications in Germany, including electronic health records and telemedicine.

**Requirements:**
- Patient data confidentiality
- Data integrity
- Authentication and authorization
- Audit logging
- Secure communication
- Data backup and recovery
- Incident response

**Framework Support:**
- 🔗 **Related:** HIPAA, GDPR, ISO 27799
- 📝 **Guidance:** Healthcare IT security
- ✅ **Templates:** GDPR, data protection, ISMS templates

---

### BSI TR-03145 - Secure Signature Creation Devices

**Full Title:** Sichere Signaturerstellungseinheiten (Secure Signature Creation Devices)  
**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Technische-Richtlinien/TR-nach-Thema-sortiert/tr03145/tr03145_node.html

**Description:**
Technical requirements for devices used to create qualified electronic signatures.

**Requirements:**
- Tamper-resistant hardware
- Secure key generation and storage
- User authentication
- Signature creation process security
- Audit logging
- Compliance with eIDAS regulation

**Framework Support:**
- 🔗 **Related:** eIDAS, Common Criteria, FIPS 140-2
- 📝 **Guidance:** Qualified signature devices
- ✅ **Templates:** Cryptography, PKI templates

---

## 3. Cloud Computing Security

### BSI C5 - Cloud Computing Compliance Controls Catalogue

**Full Title:** Cloud Computing Compliance Criteria Catalogue (C5:2020)  
**Version:** 2020  
**URL:** https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Cloud-Computing/Kriterienkatalog-C5/kriterienkatalog-c5_node.html

**Description:**
Attestation scheme for cloud service providers operating in Germany. Defines minimum security requirements for cloud computing services.

**Control Areas (17 domains):**
1. Organization of Information Security (OIS)
2. Compliance (COM)
3. Human Resources Security (HRS)
4. Asset Management (AST)
5. Access Control (ACC)
6. Cryptography (CRY)
7. Physical and Environmental Security (PHS)
8. Operations Security (OPS)
9. Communications Security (CSS)
10. System Acquisition, Development and Maintenance (SAD)
11. Supplier Relationships (SUR)
12. Information Security Incident Management (ISM)
13. Business Continuity Management (BCM)
14. Identity and Access Management (IAM)
15. Data Protection (DPR)
16. Cloud-specific Controls (CLC)
17. Threat Defense (THD)

**Audit Types:**
- Type 1: Point-in-time assessment
- Type 2: Period assessment (minimum 6 months)

**Additional Requirements:**
- Compliance with GDPR
- Data location transparency
- Subcontractor management
- Incident notification
- Right to audit

**Framework Support:**
- 🔗 **Related:** CSA CCM, ISO 27001, SOC 2, TISAX
- 📝 **Guidance:** Cloud provider assessment
- ✅ **Templates:** [templates/de/csa-ccm/](../templates/de/csa-ccm/), cloud security templates

---

### BSI Cloud Security Recommendations

**URL:** https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Cloud-Computing/cloud-computing_node.html

**Description:**
General recommendations for secure cloud adoption and usage.

**Topics:**
- Cloud service model selection (IaaS, PaaS, SaaS)
- Cloud deployment model selection
- Data classification and protection
- Encryption requirements
- Access control
- Vendor lock-in mitigation
- Exit strategies
- Multi-cloud considerations

**Framework Support:**
- 🔗 **Related:** NIST SP 800-144, ISO 27017, ISO 27018
- 📝 **Guidance:** Cloud adoption strategy
- ✅ **Templates:** Cloud security policies

---

## 4. IT-Grundschutz Methodology and Compendium

### BSI IT-Grundschutz Compendium (Edition 2024)

**Full Title:** IT-Grundschutz-Kompendium  
**Version:** Edition 2024  
**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Compendium/it-grundschutz-compendium_node.html

**Description:**
Comprehensive collection of IT security modules (formerly catalogues) containing security requirements for typical IT systems, components, and processes. Foundation of the IT-Grundschutz methodology.

**Module Categories:**

#### ISMS Modules (ISMS.*)
- ISMS.1: Security Management

#### Organization and Personnel (ORP.*)
- ORP.1: Organization
- ORP.2: Personnel
- ORP.3: Awareness and Training
- ORP.4: Identity and Access Management
- ORP.5: Compliance Management

#### Concepts and Procedures (CON.*)
- CON.1: Crypto Concept
- CON.2: Data Protection
- CON.3: Data Backup
- CON.4: Deletion and Destruction
- CON.5: Development and Testing
- CON.6: Deletion and Destruction of Data Media
- CON.7: Information Security in Projects
- CON.8: Software Development
- CON.9: Cyber Security Incident Response
- CON.10: Development and Testing of Software
- CON.11: Outsourcing

#### Operations (OPS.*)
- OPS.1.1.2: Proper IT Administration
- OPS.1.1.3: Patch and Change Management
- OPS.1.1.4: Protection against Malware
- OPS.1.1.5: Logging
- OPS.1.1.6: Software Tests and Approvals
- OPS.1.2.2: Archiving
- OPS.1.2.3: Information and Data Medium Exchange
- OPS.1.2.4: Telecommuting
- OPS.1.2.5: Remote Maintenance
- OPS.2.1: Outsourcing for Customers
- OPS.2.2: Cloud Usage
- OPS.2.3: Outsourcing for Service Providers
- OPS.3.1: Outsourcing for Service Providers

#### Detection and Reaction (DER.*)
- DER.1: Detection of Security-Relevant Events
- DER.2.1: Incident Management
- DER.2.2: Precautions for IT Forensics
- DER.2.3: Cleanup of Security Incidents
- DER.3.1: Audits and Revisions
- DER.3.2: Revision of Outsourcing
- DER.4: Emergency Management

#### Applications (APP.*)
- APP.1.1: Office Products
- APP.1.2: Web Browsers
- APP.1.4: Mobile Applications
- APP.2.1: General Directory Service
- APP.2.2: Active Directory
- APP.2.3: OpenLDAP
- APP.3.1: Web Applications
- APP.3.2: Web Server
- APP.3.3: File Server
- APP.3.4: Samba
- APP.3.6: DNS Server
- APP.4.1: Groupware
- APP.4.2: SAP ERP System
- APP.4.3: Relational Database Systems
- APP.4.4: Kubernetes
- APP.5.1: E-Mail/Groupware
- APP.5.2: Microsoft Exchange and Outlook
- APP.5.3: General Groupware
- APP.6: General Software

#### IT Systems (SYS.*)
- SYS.1.1: General Server
- SYS.1.2.2: Windows Server
- SYS.1.2.3: Windows Server 2012
- SYS.1.3: Unix Server
- SYS.1.5: Virtualization
- SYS.1.6: Containerization
- SYS.1.7: IBM Z System
- SYS.1.8: Storage Systems
- SYS.2.1: General Client
- SYS.2.2.2: Windows Clients
- SYS.2.2.3: Windows Client
- SYS.2.3: Linux and Unix Clients
- SYS.2.4: macOS Clients
- SYS.3.1: Laptops
- SYS.3.2.1: General Smartphones and Tablets
- SYS.3.2.2: Mobile Device Management (MDM)
- SYS.3.2.3: iOS (for Enterprise)
- SYS.3.2.4: Android
- SYS.3.3: Multifunctional Devices
- SYS.3.4: Mobile Data Media
- SYS.4.1: Printers, Copiers and Multifunctional Devices
- SYS.4.3: Embedded Systems
- SYS.4.4: General IoT Devices
- SYS.4.5: Wearables

#### Industrial IT (IND.*)
- IND.1: Process Control Systems
- IND.2.1: General ICS Components
- IND.2.2: Speicherprogrammierbare Steuerung (SPS)
- IND.2.3: Sensors and Actuators
- IND.2.4: Machine-to-Machine Communication for Industry 4.0
- IND.2.7: Safety Instrumented Systems
- IND.3.1: Safety-Related Control Systems
- IND.3.2: Distributed Control Systems (DCS)

#### Networks and Communication (NET.*)
- NET.1.1: Network Architecture and Design
- NET.1.2: Network Management
- NET.2.1: WLAN Operation
- NET.2.2: WLAN Usage
- NET.3.1: Routers and Switches
- NET.3.2: Firewall
- NET.3.3: VPN
- NET.4.1: TK Systems
- NET.4.2: VoIP
- NET.4.3: Fax

#### Infrastructure (INF.*)
- INF.1: General Building
- INF.2: Data Center
- INF.3: Electrotechnical Cabling
- INF.4: IT Cabling
- INF.5: Technical Room
- INF.6: Protective Cabinet
- INF.7: Office Workplace
- INF.8: Home Workplace
- INF.9: Mobile Workplace
- INF.10: Meeting, Event and Training Rooms
- INF.11: Courier, Cleaning and Support Personnel
- INF.12: Telecommuting Workplace

**Framework Support:**
- ✅ **Implemented:** [templates/de/bsi-grundschutz/](../templates/de/bsi-grundschutz/)
- 📄 **Mapping:** [templates/de/bsi-grundschutz/9999_Framework_Mapping.md](../templates/de/bsi-grundschutz/9999_Framework_Mapping.md)
- 🔗 **Related:** ISO 27001, NIST 800-53

---

### IT-Grundschutz Methodology (BSI Standard 200-2)

**Methodology Steps:**

1. **Initiation of the Security Process**
   - Management commitment
   - Security organization
   - Resource allocation

2. **Creation of a Security Concept**
   - Scope definition
   - Asset identification
   - Protection requirements assessment
   - Modeling (mapping to IT-Grundschutz modules)
   - Base security check
   - Risk analysis (for high protection requirements)

3. **Implementation of the Security Concept**
   - Implementation planning
   - Consolidation of measures
   - Cost-benefit analysis
   - Implementation execution

4. **Maintenance and Continuous Improvement**
   - Monitoring and measurement
   - Audits and reviews
   - Management review
   - Continuous improvement

**Framework Support:**
- ✅ **Documented:** BSI Grundschutz templates
- 📝 **Guidance:** Structured security implementation
- 🔗 **Related:** ISO 27001, PDCA cycle

---

## 5. Minimum Standards (Mindeststandards)

### Overview

BSI Minimum Standards define mandatory security requirements for federal agencies and provide best practice recommendations for other organizations.

---

### Minimum Standard for Web Browsers

**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Mindeststandards/Web-Browser/web-browser_node.html

**Requirements:**
- Use of current browser versions
- Automatic updates enabled
- Secure configuration (disable unnecessary features)
- Plugin management
- Certificate validation
- Private browsing mode availability
- Content Security Policy (CSP) support

**Recommended Browsers:**
- Mozilla Firefox (current ESR or latest)
- Google Chrome (current version)
- Microsoft Edge (Chromium-based)

**Configuration:**
- Disable Flash, Java applets
- Enable Do Not Track
- Restrict third-party cookies
- Enable HTTPS-only mode where possible

**Framework Support:**
- 🔗 **Related:** CIS Controls, endpoint security
- 📝 **Guidance:** Browser security policies
- ✅ **Templates:** Endpoint security, user awareness templates

---

### Minimum Standard for Email Security

**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Mindeststandards/E-Mail-Sicherheit/e-mail-sicherheit_node.html

**Requirements:**

**Transport Security:**
- TLS encryption for email transport (SMTP, IMAP, POP3)
- TLS 1.2 minimum (TLS 1.3 recommended)
- Valid certificates

**Authentication:**
- SPF (Sender Policy Framework)
- DKIM (DomainKeys Identified Mail)
- DMARC (Domain-based Message Authentication, Reporting, and Conformance)

**Content Security:**
- Spam filtering
- Malware scanning
- Phishing protection
- Attachment filtering

**End-to-End Encryption:**
- S/MIME or PGP/GPG for sensitive communications
- Key management procedures

**Framework Support:**
- 🔗 **Related:** NIST SP 800-177, BSI TR-02102-2
- 📝 **Guidance:** Email security policies
- ✅ **Templates:** Communications security, ISMS templates

---

### Minimum Standard for Logging

**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Mindeststandards/Protokollierung/protokollierung_node.html

**Requirements:**

**Log Sources:**
- Authentication events
- Authorization changes
- System changes
- Security events
- Application events
- Network events

**Log Content:**
- Timestamp (synchronized)
- Event type
- User/system identifier
- Source and destination
- Success/failure indication
- Relevant details

**Log Management:**
- Centralized log collection
- Secure log storage
- Log retention (minimum periods defined)
- Log analysis and monitoring
- Integrity protection
- Access control

**Retention Periods:**
- Security events: Minimum 7 days online, 6 months archive
- Authentication events: Minimum 90 days
- System changes: Minimum 1 year

**Framework Support:**
- 🔗 **Related:** NIST SP 800-92, ISO 27001 (A.8.15-A.8.16)
- 📝 **Guidance:** Logging and monitoring policies
- ✅ **Templates:** Audit logging, SIEM templates

---

### Minimum Standard for Mobile Device Management

**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Mindeststandards/Mobile-Device-Management/mobile-device-management_node.html

**Requirements:**

**MDM Solution:**
- Centralized device management
- Policy enforcement
- Remote wipe capability
- Device inventory
- Compliance monitoring

**Device Security:**
- Device encryption
- Strong authentication (PIN/password/biometric)
- Automatic lock
- Current OS version
- Security updates

**Application Management:**
- App whitelisting/blacklisting
- App distribution control
- App data protection
- Separation of business and private data (containerization)

**Network Security:**
- VPN for corporate access
- Certificate-based authentication
- Secure Wi-Fi configuration

**Framework Support:**
- 🔗 **Related:** NIST SP 800-124, ISO 27001 (A.6.2.1, A.8.1.3)
- 📝 **Guidance:** Mobile device policies
- ✅ **Templates:** Mobile device management, BYOD templates

---

### Minimum Standard for Secure Web Offering

**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Mindeststandards/Sichere-Web-Angebote/sichere-web-angebote_node.html

**Requirements:**

**Transport Security:**
- HTTPS mandatory (HTTP redirects to HTTPS)
- TLS 1.2 minimum (TLS 1.3 recommended)
- HSTS (HTTP Strict Transport Security)
- Valid certificates from trusted CAs

**Web Application Security:**
- Input validation
- Output encoding
- CSRF protection
- XSS prevention
- SQL injection prevention
- Secure session management
- Security headers (CSP, X-Frame-Options, etc.)

**Authentication:**
- Strong password requirements
- Multi-factor authentication for sensitive functions
- Account lockout mechanisms
- Secure password reset

**Monitoring:**
- Access logging
- Error logging
- Security event monitoring
- Intrusion detection

**Framework Support:**
- 🔗 **Related:** OWASP Top 10, NIST SP 800-95
- 📝 **Guidance:** Web application security
- ✅ **Templates:** Application security, secure SDLC templates

---

## 6. Sector-Specific Guidelines

### KRITIS (Critical Infrastructure) Security

**URL:** https://www.bsi.bund.de/DE/Themen/KRITIS-und-regulierte-Unternehmen/kritis-und-regulierte-unternehmen_node.html

**Description:**
Security requirements for operators of critical infrastructure in Germany under the IT Security Act (IT-Sicherheitsgesetz).

**Sectors:**
- Energy
- Water
- Food
- Information Technology and Telecommunications
- Health
- Finance and Insurance
- Transport and Traffic

**Requirements:**
- Implementation of state-of-the-art security measures
- Use of security systems for attack detection
- Reporting of significant IT security incidents to BSI
- Proof of compliance (audit every 2 years)
- Appointment of contact person for BSI

**Security Standards:**
- Sector-specific security standards (B3S)
- IT-Grundschutz
- ISO 27001 certification
- Alternative standards with equivalent security level

**Framework Support:**
- ✅ **Templates:** BSI Grundschutz, ISMS templates
- 🔗 **Related:** NIS Directive, DORA
- 📝 **Guidance:** Critical infrastructure protection

---

### Telecommunications Security (TK-Sicherheit)

**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Telekommunikation/telekommunikation_node.html

**Description:**
Security requirements for telecommunications providers under the Telecommunications Act (TKG).

**Requirements:**
- Protection of telecommunications systems
- Secure network architecture
- Incident detection and response
- Customer data protection
- Availability assurance
- Security concept documentation

**Framework Support:**
- 🔗 **Related:** ETSI standards, 3GPP security
- 📝 **Guidance:** Telecommunications security
- ✅ **Templates:** Network security, service provider templates

---

## 7. Industrial Control Systems and OT Security

### ICS Security Compendium

**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Industrielle-Steuerungs-und-Automatisierungssysteme/industrielle-steuerungs-und-automatisierungssysteme_node.html

**Description:**
Comprehensive guidance for securing industrial control systems (ICS) and operational technology (OT) environments.

**Topics:**
- ICS architecture and components
- Network segmentation (Purdue Model)
- Access control for ICS
- Patch management for ICS
- Incident response for ICS
- Remote access security
- Vendor management
- Safety vs. security considerations

**ICS Components:**
- SCADA systems
- DCS (Distributed Control Systems)
- PLC (Programmable Logic Controllers)
- HMI (Human-Machine Interfaces)
- Field devices and sensors
- Safety systems (SIS)

**Security Measures:**
- Network segmentation (IT/OT separation)
- Firewall and DMZ architecture
- Whitelisting
- Anomaly detection
- Physical security
- Backup and recovery
- Security monitoring

**Framework Support:**
- ✅ **Templates:** IT-Grundschutz IND modules
- 🔗 **Related:** IEC 62443, NIST SP 800-82, VDI/VDE 2182
- 📝 **Guidance:** OT security implementation
- ✅ **Templates:** ICS security, network segmentation templates

---

### ICS Security Recommendations

**Key Recommendations:**

1. **Network Segmentation:**
   - Separate IT and OT networks
   - Implement defense-in-depth
   - Use industrial firewalls
   - DMZ for data exchange

2. **Access Control:**
   - Principle of least privilege
   - Role-based access control
   - Multi-factor authentication
   - Secure remote access (VPN)

3. **Asset Management:**
   - Complete inventory of ICS components
   - Software and firmware versions
   - Network topology documentation
   - Dependency mapping

4. **Patch Management:**
   - Risk-based patching strategy
   - Testing in non-production environment
   - Compensating controls for unpatchable systems
   - Vendor coordination

5. **Monitoring and Detection:**
   - Network traffic monitoring
   - Anomaly detection
   - Security event logging
   - Intrusion detection systems (IDS)

6. **Incident Response:**
   - ICS-specific incident response plan
   - Coordination with safety systems
   - Communication procedures
   - Recovery procedures

**Framework Support:**
- 🔗 **Related:** IEC 62443 series, ISA/IEC 62443
- 📝 **Guidance:** ICS security program development

---

## 8. Artificial Intelligence and Machine Learning

### AI Security Recommendations

**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Kuenstliche-Intelligenz/kuenstliche-intelligenz_node.html

**Description:**
BSI guidance on security considerations for artificial intelligence and machine learning systems.

**Topics:**

**AI System Security:**
- Data poisoning attacks
- Model inversion attacks
- Adversarial examples
- Model extraction
- Backdoor attacks

**Secure AI Development:**
- Secure data collection and preparation
- Model training security
- Model validation and testing
- Secure deployment
- Monitoring and maintenance

**AI Governance:**
- Risk assessment for AI systems
- Transparency and explainability
- Bias detection and mitigation
- Privacy considerations
- Ethical guidelines

**Data Protection:**
- GDPR compliance for AI
- Data minimization
- Purpose limitation
- Anonymization and pseudonymization
- Right to explanation

**Framework Support:**
- 🔗 **Related:** NIST AI RMF, EU AI Act, ISO/IEC 23894
- 📝 **Guidance:** AI security and governance
- ✅ **Templates:** Risk management, data protection templates

---

## 9. Quantum-Safe Cryptography

### Post-Quantum Cryptography Recommendations

**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Quantentechnologien-und-Post-Quanten-Kryptografie/quantentechnologien-und-post-quanten-kryptografie_node.html

**Description:**
BSI guidance on preparing for quantum computing threats and transitioning to quantum-safe cryptography.

**Quantum Threat:**
- Shor's algorithm: Breaks RSA, DH, ECC
- Grover's algorithm: Weakens symmetric encryption
- Timeline: Cryptographically relevant quantum computer (CRQC) expected 2030-2040

**Migration Strategy:**

1. **Inventory Phase:**
   - Identify all cryptographic systems
   - Document algorithms and key lengths
   - Assess quantum vulnerability
   - Prioritize critical systems

2. **Preparation Phase:**
   - Increase symmetric key lengths (AES-256)
   - Plan for crypto-agility
   - Monitor PQC standardization
   - Pilot testing of PQC algorithms

3. **Migration Phase:**
   - Implement hybrid approaches (classical + PQC)
   - Deploy PQC algorithms
   - Update protocols and systems
   - Maintain backward compatibility

4. **Post-Migration Phase:**
   - Phase out classical algorithms
   - Monitor for vulnerabilities
   - Continuous improvement

**PQC Algorithm Families:**
- Lattice-based cryptography
- Hash-based signatures
- Code-based cryptography
- Multivariate cryptography
- Isogeny-based cryptography

**BSI Recommendations:**
- Follow NIST PQC standardization
- Implement crypto-agility now
- Use AES-256 for symmetric encryption
- Plan long-term data protection
- Consider "harvest now, decrypt later" attacks

**Framework Support:**
- 🔗 **Related:** NIST PQC project, BSI TR-02102-1
- 📝 **Guidance:** Cryptographic transition planning
- ✅ **Templates:** Cryptography policy, technology roadmap templates

---

## 10. Mobile and IoT Security

### Mobile Security Recommendations

**URL:** https://www.bsi.bund.de/DE/Themen/Verbraucherinnen-und-Verbraucher/Informationen-und-Empfehlungen/Mobiltelefone-und-Tablets/mobiltelefone-und-tablets_node.html

**Topics:**
- Mobile device selection criteria
- Secure configuration
- App security
- Mobile malware protection
- Data protection on mobile devices
- Lost/stolen device procedures
- BYOD policies

**Framework Support:**
- 🔗 **Related:** NIST SP 800-124, IT-Grundschutz SYS.3.2.x modules
- 📝 **Guidance:** Mobile device policies
- ✅ **Templates:** Mobile device management templates

---

### IoT Security Recommendations

**URL:** https://www.bsi.bund.de/DE/Themen/Verbraucherinnen-und-Verbraucher/Informationen-und-Empfehlungen/Internet-der-Dinge/internet-der-dinge_node.html

**Topics:**
- IoT device security requirements
- Secure IoT deployment
- IoT network security
- IoT data protection
- IoT lifecycle management
- Consumer IoT security

**IT-Grundschutz IoT Modules:**
- SYS.4.4: General IoT Devices
- IND.2.4: Machine-to-Machine Communication for Industry 4.0

**Framework Support:**
- 🔗 **Related:** NIST IR 8259, ETSI EN 303 645
- 📝 **Guidance:** IoT security policies
- ✅ **Templates:** IoT security, device management templates

---

## 11. Secure Software Development

### Secure Software Development Lifecycle

**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Software-Entwicklung/software-entwicklung_node.html

**Description:**
BSI recommendations for integrating security into the software development lifecycle.

**SDLC Phases:**

1. **Requirements Phase:**
   - Security requirements definition
   - Threat modeling
   - Privacy requirements
   - Compliance requirements

2. **Design Phase:**
   - Security architecture
   - Secure design patterns
   - Data flow analysis
   - Attack surface minimization

3. **Implementation Phase:**
   - Secure coding standards
   - Code review
   - Static analysis (SAST)
   - Dependency management

4. **Testing Phase:**
   - Security testing
   - Dynamic analysis (DAST)
   - Penetration testing
   - Fuzzing

5. **Deployment Phase:**
   - Secure configuration
   - Hardening
   - Security documentation
   - Deployment verification

6. **Maintenance Phase:**
   - Vulnerability management
   - Patch management
   - Security monitoring
   - Incident response

**Secure Coding Practices:**
- Input validation
- Output encoding
- Authentication and session management
- Access control
- Cryptographic practices
- Error handling and logging
- Data protection
- Communication security

**Framework Support:**
- 🔗 **Related:** NIST SP 800-218, OWASP SAMM, ISO 27034
- 📝 **Guidance:** Secure SDLC implementation
- ✅ **Templates:** IT-Grundschutz CON.8, APP modules

---

## 12. Web Application Security

### Web Application Security Recommendations

**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Webanwendungen/webanwendungen_node.html

**Description:**
Security recommendations for web applications based on OWASP and BSI best practices.

**Common Vulnerabilities (OWASP Top 10):**
1. Broken Access Control
2. Cryptographic Failures
3. Injection
4. Insecure Design
5. Security Misconfiguration
6. Vulnerable and Outdated Components
7. Identification and Authentication Failures
8. Software and Data Integrity Failures
9. Security Logging and Monitoring Failures
10. Server-Side Request Forgery (SSRF)

**Security Measures:**

**Input Validation:**
- Whitelist validation
- Type checking
- Length restrictions
- Format validation
- Encoding validation

**Output Encoding:**
- Context-aware encoding
- HTML encoding
- JavaScript encoding
- URL encoding
- SQL encoding

**Authentication:**
- Strong password policies
- Multi-factor authentication
- Secure password storage (bcrypt, Argon2)
- Session management
- Account lockout

**Authorization:**
- Principle of least privilege
- Role-based access control
- Attribute-based access control
- Vertical and horizontal access control

**Security Headers:**
- Content-Security-Policy (CSP)
- X-Frame-Options
- X-Content-Type-Options
- Strict-Transport-Security (HSTS)
- Referrer-Policy
- Permissions-Policy

**Framework Support:**
- 🔗 **Related:** OWASP ASVS, OWASP Top 10
- 📝 **Guidance:** Web application security
- ✅ **Templates:** IT-Grundschutz APP.3.1, secure SDLC templates

---

## 13. Data Protection and Privacy

### GDPR Implementation Guidance

**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Datenschutz/datenschutz_node.html

**Description:**
BSI guidance on implementing technical and organizational measures for GDPR compliance.

**Technical Measures:**

**Pseudonymization:**
- Separation of identifying data
- Use of pseudonyms
- Key management
- Re-identification controls

**Encryption:**
- Data at rest encryption
- Data in transit encryption
- End-to-end encryption
- Key management

**Access Control:**
- Authentication mechanisms
- Authorization controls
- Audit logging
- Segregation of duties

**Data Minimization:**
- Purpose limitation
- Storage limitation
- Data retention policies
- Automated deletion

**Organizational Measures:**
- Data protection policies
- Privacy by design
- Privacy by default
- Data protection impact assessment (DPIA)
- Data breach procedures
- Data processing agreements

**Framework Support:**
- ✅ **Templates:** [templates/de/gdpr/](../templates/de/gdpr/)
- 🔗 **Related:** GDPR, IT-Grundschutz CON.2
- 📝 **Guidance:** GDPR compliance implementation

---

## 14. Incident Response and Forensics

### IT Security Incident Response

**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Cyber-Sicherheitslage/Reaktion/reaktion_node.html

**Description:**
BSI guidance on establishing and operating an incident response capability.

**Incident Response Process:**

1. **Preparation:**
   - Incident response plan
   - Team formation and training
   - Tools and resources
   - Communication procedures
   - Escalation paths

2. **Detection and Analysis:**
   - Event monitoring
   - Alert triage
   - Incident classification
   - Impact assessment
   - Evidence collection

3. **Containment:**
   - Short-term containment
   - Long-term containment
   - System isolation
   - Evidence preservation

4. **Eradication:**
   - Root cause analysis
   - Malware removal
   - Vulnerability remediation
   - System hardening

5. **Recovery:**
   - System restoration
   - Validation testing
   - Monitoring
   - Return to normal operations

6. **Post-Incident Activity:**
   - Lessons learned
   - Documentation
   - Process improvement
   - Reporting (if required)

**Incident Categories:**
- Malware infections
- Unauthorized access
- Data breaches
- Denial of service
- Social engineering
- Insider threats
- Supply chain incidents

**Reporting Requirements:**
- KRITIS operators: Report to BSI
- GDPR: Report to data protection authority (72 hours)
- NIS Directive: Report significant incidents

**Framework Support:**
- 🔗 **Related:** NIST SP 800-61, ISO 27035
- 📝 **Guidance:** Incident response procedures
- ✅ **Templates:** IT-Grundschutz DER.2.1, incident management templates

---

### IT Forensics

**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/IT-Forensik/it-forensik_node.html

**Description:**
Guidance on IT forensics for incident investigation and evidence collection.

**Forensic Process:**
1. Identification
2. Preservation
3. Collection
4. Examination
5. Analysis
6. Presentation

**Evidence Handling:**
- Chain of custody
- Evidence integrity
- Documentation
- Legal admissibility
- Secure storage

**Framework Support:**
- 🔗 **Related:** ISO/IEC 27037, IT-Grundschutz DER.2.2
- 📝 **Guidance:** Forensic readiness
- ✅ **Templates:** Incident response, forensics templates

---

## 15. Business Continuity and Disaster Recovery

### Business Continuity Management

**Standard:** BSI Standard 200-4  
**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/BSI-Standards/bsi-standards_node.html

**Description:**
Requirements and recommendations for establishing a Business Continuity Management (BCM) system.

**BCM Process:**

1. **BCM Organization:**
   - Management commitment
   - BCM policy
   - Roles and responsibilities
   - Resource allocation

2. **Business Impact Analysis (BIA):**
   - Critical business processes
   - Dependencies
   - Recovery time objectives (RTO)
   - Recovery point objectives (RPO)
   - Impact assessment

3. **BCM Strategy:**
   - Recovery strategies
   - Preventive measures
   - Alternative locations
   - Resource requirements

4. **Emergency Management:**
   - Emergency response procedures
   - Crisis management team
   - Communication plans
   - Decision-making processes

5. **Tests and Exercises:**
   - Test planning
   - Test execution
   - Evaluation
   - Improvement

6. **Awareness and Training:**
   - BCM awareness
   - Role-specific training
   - Exercise participation

**Framework Support:**
- ✅ **Templates:** [templates/de/bcm/](../templates/de/bcm/)
- 🔗 **Related:** ISO 22301, NIST SP 800-34
- 📝 **Guidance:** BCM implementation

---

## 16. Certification and Evaluation

### Common Criteria Certification

**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Zertifizierung-und-Anerkennung/Produktzertifizierung/Common-Criteria/common-criteria_node.html

**Description:**
BSI operates as a Common Criteria certification body for IT security evaluations.

**Evaluation Assurance Levels (EAL):**
- EAL1: Functionally tested
- EAL2: Structurally tested
- EAL3: Methodically tested and checked
- EAL4: Methodically designed, tested, and reviewed
- EAL5: Semi-formally designed and tested
- EAL6: Semi-formally verified design and tested
- EAL7: Formally verified design and tested

**Product Categories:**
- Operating systems
- Databases
- Firewalls
- Smart cards
- Biometric systems
- Cryptographic modules
- Network devices

**Framework Support:**
- ✅ **Templates:** [templates/de/common-criteria/](../templates/de/common-criteria/)
- 🔗 **Related:** ISO/IEC 15408, Protection Profiles
- 📝 **Guidance:** Security Target development

---

### ISO 27001 Certification (based on IT-Grundschutz)

**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Zertifizierung-und-Anerkennung/ISO27001-Zertifizierung/ISO-27001-Zertifizierung-auf-der-Basis-von-IT-Grundschutz/iso-27001-zertifizierung-auf-der-basis-von-it-grundschutz_node.html

**Description:**
BSI certification scheme for ISO 27001 based on IT-Grundschutz methodology.

**Certification Levels:**
- **Basic Certificate:** Core security requirements
- **Standard Certificate:** Comprehensive IT-Grundschutz implementation
- **Advanced Certificate:** Additional risk analysis for high protection requirements

**Certification Process:**
1. Application
2. Documentation review
3. On-site audit
4. Certification decision
5. Certificate issuance
6. Surveillance audits (annual)
7. Re-certification (every 3 years)

**Framework Support:**
- ✅ **Templates:** BSI Grundschutz, ISMS templates
- 🔗 **Related:** ISO 27001, IT-Grundschutz Compendium
- 📝 **Guidance:** Certification preparation

---

## 17. Awareness and Training

### Security Awareness Recommendations

**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Awareness/awareness_node.html

**Description:**
Guidance on establishing and maintaining security awareness programs.

**Awareness Topics:**
- Password security
- Phishing recognition
- Social engineering
- Malware threats
- Data protection
- Physical security
- Mobile device security
- Clean desk policy
- Incident reporting

**Training Methods:**
- E-learning modules
- Classroom training
- Simulated phishing exercises
- Security newsletters
- Posters and reminders
- Security champions program
- Gamification

**Measurement:**
- Training completion rates
- Phishing simulation results
- Security incident metrics
- Knowledge assessments
- Behavioral observations

**Framework Support:**
- 🔗 **Related:** IT-Grundschutz ORP.3, ISO 27001 (A.6.3)
- 📝 **Guidance:** Awareness program development
- ✅ **Templates:** Awareness and training templates

---

## 18. Supply Chain Security

### Supply Chain Security Recommendations

**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Lieferkettensicherheit/lieferkettensicherheit_node.html

**Description:**
Guidance on managing cybersecurity risks in the supply chain.

**Risk Areas:**
- Hardware supply chain
- Software supply chain
- Service providers
- Cloud services
- Outsourcing
- Third-party components

**Security Measures:**

**Supplier Assessment:**
- Security questionnaires
- On-site audits
- Certifications review
- Reference checks
- Financial stability

**Contractual Requirements:**
- Security requirements
- Audit rights
- Incident notification
- Data protection
- Subcontractor management
- Exit clauses

**Ongoing Monitoring:**
- Performance monitoring
- Security incident tracking
- Compliance verification
- Regular reassessment

**Software Supply Chain:**
- Software Bill of Materials (SBOM)
- Dependency analysis
- Vulnerability scanning
- Code signing
- Secure distribution

**Framework Support:**
- 🔗 **Related:** NIST SP 800-161, ISO 27036, IT-Grundschutz CON.11
- 📝 **Guidance:** Supply chain risk management
- ✅ **Templates:** Supplier management, third-party risk templates

---

## 19. Penetration Testing

### Penetration Testing Recommendations

**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Penetrationstests/penetrationstests_node.html

**Description:**
Guidance on planning, conducting, and evaluating penetration tests.

**Penetration Test Types:**
- **Black Box:** No prior knowledge
- **Grey Box:** Limited knowledge
- **White Box:** Full knowledge

**Test Scope:**
- External network
- Internal network
- Web applications
- Mobile applications
- Wireless networks
- Social engineering
- Physical security

**Testing Methodology:**
1. Planning and preparation
2. Information gathering
3. Vulnerability analysis
4. Exploitation
5. Post-exploitation
6. Reporting
7. Remediation verification

**Legal Considerations:**
- Written authorization required
- Scope definition
- Rules of engagement
- Data handling
- Liability

**Reporting:**
- Executive summary
- Technical findings
- Risk assessment
- Remediation recommendations
- Evidence documentation

**Framework Support:**
- 🔗 **Related:** NIST SP 800-115, OWASP Testing Guide, PTES
- 📝 **Guidance:** Penetration testing program
- ✅ **Templates:** Security testing, vulnerability management templates

---

## 20. Ransomware Protection

### Ransomware Protection Recommendations

**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Ransomware/ransomware_node.html

**Description:**
Comprehensive guidance on preventing, detecting, and responding to ransomware attacks.

**Prevention Measures:**

**Technical Controls:**
- Regular backups (3-2-1 rule)
- Offline/immutable backups
- Patch management
- Endpoint protection
- Email filtering
- Web filtering
- Network segmentation
- Application whitelisting
- Privilege management

**Organizational Controls:**
- Security awareness training
- Phishing simulations
- Incident response plan
- Business continuity plan
- Backup testing
- Access control policies

**Detection:**
- Behavioral analysis
- Anomaly detection
- File integrity monitoring
- Network traffic analysis
- Endpoint detection and response (EDR)

**Response:**
1. Isolate affected systems
2. Identify ransomware variant
3. Assess impact
4. Notify stakeholders
5. Preserve evidence
6. Restore from backups (if available)
7. Do not pay ransom (BSI recommendation)
8. Report to authorities

**Recovery:**
- System restoration
- Validation testing
- Root cause analysis
- Security improvements
- Lessons learned

**Framework Support:**
- 🔗 **Related:** IT-Grundschutz DER modules, incident response
- 📝 **Guidance:** Ransomware resilience
- ✅ **Templates:** Incident response, backup, BCM templates

---

## 21. Home Office and Remote Work Security

### Home Office Security Recommendations

**URL:** https://www.bsi.bund.de/DE/Themen/Verbraucherinnen-und-Verbraucher/Informationen-und-Empfehlungen/Arbeiten-im-Homeoffice/arbeiten-im-homeoffice_node.html

**Description:**
Security guidance for home office and remote work environments.

**Technical Security:**

**Device Security:**
- Company-managed devices preferred
- Full disk encryption
- Endpoint protection
- Automatic updates
- Screen lock
- Physical security

**Network Security:**
- VPN for corporate access
- Secure Wi-Fi configuration (WPA3)
- Separate network for IoT devices
- Router security (firmware updates, strong passwords)

**Access Control:**
- Multi-factor authentication
- Strong passwords
- Privileged access management
- Session timeouts

**Data Protection:**
- Data classification
- Encryption for sensitive data
- Secure file sharing
- Data backup
- Secure disposal

**Organizational Security:**

**Policies:**
- Home office policy
- Acceptable use policy
- BYOD policy (if applicable)
- Data handling guidelines
- Incident reporting procedures

**Physical Security:**
- Secure workspace
- Visitor restrictions
- Clean desk policy
- Secure storage for documents
- Privacy screens

**Awareness:**
- Home office security training
- Phishing awareness
- Social engineering awareness
- Family member awareness

**Framework Support:**
- 🔗 **Related:** IT-Grundschutz INF.8, OPS.1.2.4
- 📝 **Guidance:** Remote work policies
- ✅ **Templates:** Remote access, telecommuting templates

---

## 22. 5G Security

### 5G Network Security

**URL:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/5G/5g_node.html

**Description:**
Security considerations for 5G network deployment and usage.

**5G Security Features:**
- Enhanced encryption
- Network slicing security
- Improved authentication
- Integrity protection
- Privacy enhancements

**Security Challenges:**
- Increased attack surface
- Software-defined networking risks
- Supply chain security
- Edge computing security
- IoT device proliferation

**Recommendations:**

**For Network Operators:**
- Security by design
- Vendor diversity
- Security testing and certification
- Continuous monitoring
- Incident response capability

**For Organizations:**
- Risk assessment for 5G adoption
- Network slicing security requirements
- Edge computing security
- IoT device management
- Data protection measures

**Framework Support:**
- 🔗 **Related:** 3GPP security standards, ETSI NFV security
- 📝 **Guidance:** 5G security architecture
- ✅ **Templates:** Network security, telecommunications templates

---

## 23. Secure Email Communication

### S/MIME and PGP/GPG

**URL:** https://www.bsi.bund.de/DE/Themen/Verbraucherinnen-und-Verbraucher/Informationen-und-Empfehlungen/E-Mail-Verschluesselung/e-mail-verschluesselung_node.html

**Description:**
Guidance on implementing end-to-end email encryption.

**S/MIME (Secure/Multipurpose Internet Mail Extensions):**
- Certificate-based encryption
- Digital signatures
- PKI infrastructure required
- Native support in email clients
- Suitable for enterprise environments

**PGP/GPG (Pretty Good Privacy/GNU Privacy Guard):**
- Public key cryptography
- Web of trust or PKI
- Plugin required for most email clients
- Suitable for individual users and organizations

**Implementation:**
- Key generation and management
- Certificate/key distribution
- Email client configuration
- User training
- Key backup and recovery

**Framework Support:**
- 🔗 **Related:** BSI TR-02102-1, email security minimum standard
- 📝 **Guidance:** Email encryption policies
- ✅ **Templates:** Communications security, cryptography templates

---

## Cross-Reference Tables

### BSI TR Quick Reference

| TR Number | Title | Topic | Status |
|-----------|-------|-------|--------|
| TR-02102-1 | Cryptographic Mechanisms | Algorithms, key lengths | Active |
| TR-02102-2 | TLS | Transport security | Active |
| TR-02102-3 | IPsec/IKEv2 | VPN security | Active |
| TR-02102-4 | SSH | Secure shell | Active |
| TR-03107 | Electronic Signatures | Digital signatures, PKI | Active |
| TR-03109 | Smart Metering PKI | Smart grid security | Active |
| TR-03110 | ePassport Security | Travel documents | Active |
| TR-03116 | eCard-API | eID infrastructure | Active |
| TR-03145 | Signature Creation Devices | Qualified signatures | Active |
| TR-03148 | Secure Broadband Router | Router security | Active |
| TR-03161 | eHealth Security | Healthcare IT | Active |

---

### BSI Standards Quick Reference

| Standard | Title | Topic | Status |
|----------|-------|-------|--------|
| 200-1 | ISMS | Management system | Active |
| 200-2 | IT-Grundschutz Methodology | Implementation approach | Active |
| 200-3 | Risk Analysis | Risk assessment | Active |
| 200-4 | BCM | Business continuity | Active |

---

### IT-Grundschutz Module Categories

| Category | Prefix | Example Modules | Count |
|----------|--------|-----------------|-------|
| ISMS | ISMS.* | ISMS.1 | 1 |
| Organization & Personnel | ORP.* | ORP.1-5 | 5 |
| Concepts & Procedures | CON.* | CON.1-11 | 11 |
| Operations | OPS.* | OPS.1.x, OPS.2.x, OPS.3.x | 15+ |
| Detection & Reaction | DER.* | DER.1-4 | 7 |
| Applications | APP.* | APP.1.x-6.x | 25+ |
| IT Systems | SYS.* | SYS.1.x-4.x | 30+ |
| Industrial IT | IND.* | IND.1-3 | 8 |
| Networks | NET.* | NET.1.x-4.x | 10+ |
| Infrastructure | INF.* | INF.1-12 | 12 |

---

### BSI vs. NIST Comparison

| Topic | BSI | NIST | Notes |
|-------|-----|------|-------|
| Cryptography | TR-02102 series | SP 800-57, 800-131A, FIPS | Similar recommendations |
| TLS | TR-02102-2 | SP 800-52 | Aligned requirements |
| Risk Management | Standard 200-3 | SP 800-30, 800-37 | Different approaches |
| Security Controls | IT-Grundschutz | SP 800-53 | Complementary |
| Cloud Security | C5 | FedRAMP, SP 800-144 | Different focus |
| IoT Security | IT-Grundschutz SYS.4.4 | IR 8259 | Similar concerns |
| Zero Trust | Recommendations | SP 800-207 | NIST more detailed |
| Incident Response | DER modules | SP 800-61 | Similar processes |

---

## Implementation Roadmap

### Phase 1: Foundation (Months 1-3)

**Cryptography:**
- Implement TR-02102-1 compliant algorithms
- Deploy TLS 1.2/1.3 per TR-02102-2
- Establish key management procedures

**IT-Grundschutz:**
- Define ISMS scope
- Conduct asset inventory
- Perform protection requirements assessment
- Begin IT-Grundschutz modeling

**Minimum Standards:**
- Implement web browser security
- Deploy email security (SPF, DKIM, DMARC)
- Establish logging infrastructure

---

### Phase 2: Enhancement (Months 4-6)

**Security Controls:**
- Implement IT-Grundschutz modules
- Deploy security monitoring
- Establish patch management
- Implement access control

**Compliance:**
- GDPR technical measures
- KRITIS requirements (if applicable)
- Sector-specific requirements

---

### Phase 3: Advanced (Months 7-12)

**Advanced Security:**
- ICS/OT security (if applicable)
- Cloud security (C5 requirements)
- Mobile device management
- Advanced threat detection

**Certification:**
- Prepare for ISO 27001 (IT-Grundschutz)
- Common Criteria evaluation (if applicable)
- C5 attestation (cloud providers)

---

### Phase 4: Optimization (Ongoing)

**Continuous Improvement:**
- Regular IT-Grundschutz updates
- Monitoring new BSI publications
- Adapting to threat landscape
- Maintaining certifications
- Post-quantum cryptography preparation

---

## Framework Template Integration

### How BSI Technical Guidelines Map to Handbook Templates

This section shows how BSI technical guidelines integrate with existing framework templates in the Handbook Generator.

---

### Cryptography → ISMS and BSI Grundschutz Templates

**BSI Guidelines:**
- TR-02102-1 (Algorithms and key lengths)
- TR-02102-2 (TLS)
- TR-02102-3 (IPsec)
- TR-02102-4 (SSH)

**Template Integration:**
- ✅ [templates/de/isms/0500_Kryptografische_Kontrollen.md](../templates/de/isms/)
- ✅ [templates/de/bsi-grundschutz/0200_CON_1_Kryptokonzept.md](../templates/de/bsi-grundschutz/)
- ✅ ISO 27001 Control A.8.24 (Kryptografie)

**Implementation:**
- Reference TR-02102-1 for algorithm selection
- Use TR-02102-2 for TLS configuration
- Apply TR-02102-3 for VPN security
- Follow TR-02102-4 for SSH hardening
- Document cryptographic standards in policy templates

---

### IT-Grundschutz → BSI Grundschutz Templates

**BSI Guidelines:**
- IT-Grundschutz Compendium (Edition 2024)
- BSI Standard 200-2 (Methodology)

**Template Integration:**
- ✅ [templates/de/bsi-grundschutz/](../templates/de/bsi-grundschutz/)
- 📄 **Mapping:** [templates/de/bsi-grundschutz/9999_Framework_Mapping.md](../templates/de/bsi-grundschutz/9999_Framework_Mapping.md)

**Implementation:**
- Follow IT-Grundschutz methodology
- Map assets to IT-Grundschutz modules
- Implement module requirements
- Document in BSI Grundschutz templates

---

### Cloud Security (C5) → CSA CCM Templates

**BSI Guidelines:**
- C5:2020 Catalogue

**Template Integration:**
- ✅ [templates/de/csa-ccm/](../templates/de/csa-ccm/)
- 🔗 **Related:** ISO 27001, SOC 2

**Implementation:**
- Map C5 requirements to CSA CCM controls
- Document German-specific requirements
- Address data location requirements
- Implement GDPR compliance measures

---

### GDPR → Data Protection Templates

**BSI Guidelines:**
- GDPR implementation guidance
- Technical and organizational measures

**Template Integration:**
- ✅ [templates/de/gdpr/](../templates/de/gdpr/)
- ✅ [templates/de/bsi-grundschutz/0200_CON_2_Datenschutz.md](../templates/de/bsi-grundschutz/)

**Implementation:**
- Apply BSI recommendations for technical measures
- Implement pseudonymization and encryption
- Document data protection impact assessments
- Establish data breach procedures

---

### ICS Security → Industrial Control Templates

**BSI Guidelines:**
- ICS Security Compendium
- IT-Grundschutz IND modules

**Template Integration:**
- ✅ [templates/de/bsi-grundschutz/IND_modules/](../templates/de/bsi-grundschutz/)
- 🔗 **Related:** IEC 62443, NIST SP 800-82

**Implementation:**
- Apply ICS-specific security measures
- Implement network segmentation
- Document OT security architecture
- Establish ICS incident response

---

### Business Continuity → BCM Templates

**BSI Guidelines:**
- BSI Standard 200-4

**Template Integration:**
- ✅ [templates/de/bcm/](../templates/de/bcm/)
- 🔗 **Related:** ISO 22301

**Implementation:**
- Follow BSI Standard 200-4 methodology
- Conduct business impact analysis
- Develop BCM strategy
- Document emergency management procedures

---

### Incident Response → Incident Management Templates

**BSI Guidelines:**
- Incident response guidance
- IT-Grundschutz DER modules

**Template Integration:**
- ✅ [templates/de/isms/0500_Incident_Management.md](../templates/de/isms/)
- ✅ [templates/de/bsi-grundschutz/DER_modules/](../templates/de/bsi-grundschutz/)

**Implementation:**
- Establish incident response process
- Define reporting requirements (KRITIS, GDPR)
- Document forensics procedures
- Implement continuous improvement

---

## Compliance Mapping

### German Federal Compliance

**Required BSI Standards:**
- Federal agencies: IT-Grundschutz mandatory
- KRITIS operators: State-of-the-art security, BSI reporting
- Telecommunications providers: TKG requirements

**Template Support:**
- ✅ BSI Grundschutz templates cover federal requirements
- ✅ KRITIS-specific guidance in templates
- ✅ Telecommunications security templates

---

### EU Compliance

**NIS Directive / NIS2:**
- Security measures for essential services
- Incident reporting
- Risk management

**Template Support:**
- ✅ BSI Grundschutz aligns with NIS requirements
- ✅ Incident reporting procedures in templates
- 🔗 **Related:** DORA (financial sector)

**GDPR:**
- Technical and organizational measures
- Data protection by design and default
- Data breach notification

**Template Support:**
- ✅ [templates/de/gdpr/](../templates/de/gdpr/)
- ✅ BSI GDPR implementation guidance integrated

---

### Industry Compliance

**Automotive (TISAX):**
- Based on ISO 27001 + VDA ISA
- BSI Grundschutz can support TISAX

**Template Support:**
- ✅ [templates/de/tisax/](../templates/de/tisax/)
- 🔗 **Related:** BSI Grundschutz, ISO 27001

**Healthcare:**
- Patient data protection
- eHealth security requirements

**Template Support:**
- ✅ BSI TR-03161 guidance
- ✅ GDPR templates for healthcare data

---

## Practical Implementation Examples

### Example 1: Implementing BSI-Compliant Cryptography

**Scenario:** Organization needs to implement cryptography compliant with BSI requirements

**BSI Guidelines to Apply:**
1. TR-02102-1 - Select approved algorithms and key lengths
2. TR-02102-2 - Configure TLS for web services
3. TR-02102-3 - Implement IPsec VPN
4. TR-02102-4 - Harden SSH access

**Template Workflow:**
1. Review [templates/de/bsi-grundschutz/0200_CON_1_Kryptokonzept.md](../templates/de/bsi-grundschutz/)
2. Document algorithm selection per TR-02102-1
3. Define key management procedures
4. Configure TLS per TR-02102-2 requirements
5. Implement VPN per TR-02102-3
6. Harden SSH per TR-02102-4

**Deliverables:**
- Crypto concept document (Kryptokonzept)
- Algorithm selection matrix
- TLS configuration standards
- VPN security policy
- SSH hardening guide

---

### Example 2: IT-Grundschutz Implementation

**Scenario:** Organization implementing IT-Grundschutz for ISO 27001 certification

**BSI Guidelines to Apply:**
1. BSI Standard 200-1 - ISMS requirements
2. BSI Standard 200-2 - IT-Grundschutz methodology
3. BSI Standard 200-3 - Risk analysis (if needed)
4. IT-Grundschutz Compendium - Security modules

**Template Workflow:**
1. Define ISMS scope and boundaries
2. Conduct asset inventory
3. Assess protection requirements (normal, high, very high)
4. Model IT environment using IT-Grundschutz modules
5. Perform base security check
6. Conduct risk analysis for high protection requirements
7. Create implementation plan
8. Document in [templates/de/bsi-grundschutz/](../templates/de/bsi-grundschutz/)

**Deliverables:**
- ISMS documentation
- IT-Grundschutz modeling
- Base security check results
- Risk analysis (if applicable)
- Implementation plan
- Security concept

---

### Example 3: KRITIS Compliance

**Scenario:** Critical infrastructure operator needs to comply with IT Security Act

**BSI Guidelines to Apply:**
1. IT-Grundschutz or equivalent standard
2. Sector-specific security standard (B3S)
3. Attack detection systems
4. Incident reporting procedures

**Template Workflow:**
1. Determine KRITIS applicability
2. Select appropriate security standard
3. Implement IT-Grundschutz or B3S requirements
4. Deploy attack detection systems
5. Establish BSI reporting procedures
6. Prepare for mandatory audit
7. Document in BSI Grundschutz templates

**Deliverables:**
- KRITIS compliance documentation
- Security concept
- Attack detection system documentation
- Incident reporting procedures
- Audit preparation materials

---

### Example 4: Cloud Provider C5 Attestation

**Scenario:** Cloud service provider seeking C5 attestation

**BSI Guidelines to Apply:**
1. C5:2020 Catalogue
2. GDPR requirements
3. ISO 27001 (foundation)

**Template Workflow:**
1. Review C5:2020 requirements (17 domains)
2. Map existing controls to C5 requirements
3. Implement missing controls
4. Document in [templates/de/csa-ccm/](../templates/de/csa-ccm/)
5. Engage C5 auditor
6. Undergo Type 1 or Type 2 audit
7. Obtain C5 attestation report

**Deliverables:**
- C5 control documentation
- System description
- Control implementation evidence
- C5 attestation report (Type 1 or Type 2)

---

## Staying Current with BSI Publications

### Official Resources

**BSI Website:**
- Main site: https://www.bsi.bund.de/
- English version: https://www.bsi.bund.de/EN/
- Publications: https://www.bsi.bund.de/EN/Service-Navi/Publikationen/publikationen_node.html

**IT-Grundschutz Portal:**
- URL: https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/it-grundschutz_node.html
- IT-Grundschutz Compendium downloads
- Module updates
- Implementation guidance

**BSI Newsletter:**
- Subscribe for updates on new publications
- Security advisories
- Threat intelligence

**CERT-Bund:**
- URL: https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Cyber-Sicherheitslage/Reaktion/CERT-Bund/cert-bund_node.html
- Security advisories
- Vulnerability information
- Incident warnings

---

### Publication Types

**Technical Guidelines (TR):**
- Binding technical specifications
- Numbered: TR-02102, TR-03107, etc.
- Regular updates

**BSI Standards:**
- Management and methodology standards
- Numbered: 200-1, 200-2, 200-3, 200-4
- Periodic revisions

**IT-Grundschutz Compendium:**
- Annual edition (e.g., Edition 2024)
- Module updates throughout the year
- Available in German and English

**Minimum Standards:**
- Mandatory for federal agencies
- Best practice for others
- Topic-specific (browsers, email, logging, etc.)

**Recommendations and Guidance:**
- Topic-specific guidance documents
- Implementation recommendations
- Threat-specific guidance

---

### Update Frequency

**Regular Updates:**
- IT-Grundschutz Compendium: Annual edition
- Technical Guidelines: As needed
- Minimum Standards: Periodic updates
- Security advisories: Ongoing

**Major Initiatives:**
- Post-quantum cryptography: Ongoing
- AI security: Developing guidance
- 5G security: Ongoing updates
- Cloud security: C5 updates

---

## Additional Resources

### BSI Resources

**Primary:**
- BSI Homepage: https://www.bsi.bund.de/
- BSI for Citizens: https://www.bsi-fuer-buerger.de/
- BSI for Business: https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/unternehmen-und-organisationen_node.html
- CERT-Bund: https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Cyber-Sicherheitslage/Reaktion/CERT-Bund/cert-bund_node.html

**IT-Grundschutz:**
- IT-Grundschutz Portal: https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/it-grundschutz_node.html
- IT-Grundschutz Compendium: https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/IT-Grundschutz-Compendium/it-grundschutz-compendium_node.html
- IT-Grundschutz Tools: https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Tools/tools_node.html

**Certification:**
- Certification Overview: https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Zertifizierung-und-Anerkennung/zertifizierung-und-anerkennung_node.html
- ISO 27001 on IT-Grundschutz: https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Zertifizierung-und-Anerkennung/ISO27001-Zertifizierung/iso-27001-zertifizierung_node.html
- Common Criteria: https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Zertifizierung-und-Anerkennung/Produktzertifizierung/Common-Criteria/common-criteria_node.html

**Tools:**
- GSTOOL (IT-Grundschutz Tool): Commercial tool for IT-Grundschutz implementation
- verinice: Open-source ISMS tool with IT-Grundschutz support

**Training:**
- BSI Training Courses: https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/Schulungen/schulungen_node.html
- IT-Grundschutz Practitioner
- IT-Grundschutz Auditor
- Information Security Officer

---

### Related German Standards Organizations

**DIN (Deutsches Institut für Normung):**
- URL: https://www.din.de/
- German standards organization
- National member of ISO
- DIN ISO standards (German versions of ISO standards)

**VDE (Verband der Elektrotechnik):**
- URL: https://www.vde.com/
- Electrical engineering standards
- VDI/VDE 2182 (ICS security)

**VDA (Verband der Automobilindustrie):**
- URL: https://www.vda.de/
- Automotive industry association
- VDA ISA (Information Security Assessment) - basis for TISAX

---

### European Resources

**ENISA (European Union Agency for Cybersecurity):**
- URL: https://www.enisa.europa.eu/
- EU cybersecurity agency
- Guidelines and recommendations
- Threat landscape reports

**ETSI (European Telecommunications Standards Institute):**
- URL: https://www.etsi.org/
- Telecommunications standards
- ETSI EN 303 645 (IoT security)
- ETSI TS 103 645 (Consumer IoT)

**eIDAS:**
- URL: https://digital-strategy.ec.europa.eu/en/policies/eidas-regulation
- Electronic identification and trust services
- Qualified electronic signatures
- Cross-border recognition

---

### Related Documentation

**Handbook Generator Documentation:**
- [Framework Mapping Documentation](FRAMEWORK_MAPPING.md)
- [IT Standards Reference Guide](IT_STANDARDS_REFERENCE.md)
- [NIST Technical Guidelines](NIST_TECHNICAL_GUIDELINES.md)
- [Configuration Reference](CONFIGURATION_REFERENCE.md)

**Framework Templates:**
- [BSI Grundschutz Templates](../templates/de/bsi-grundschutz/)
- [ISMS Templates (German)](../templates/de/isms/)
- [GDPR Templates (German)](../templates/de/gdpr/)
- [BCM Templates (German)](../templates/de/bcm/)
- [All Framework Templates](../templates/)

---

## Glossary (German-English)

**German Terms:**

**Bundesamt für Sicherheit in der Informationstechnik (BSI):** Federal Office for Information Security

**IT-Grundschutz:** IT Baseline Protection (BSI's security methodology)

**Kryptokonzept:** Cryptographic Concept

**Mindeststandard:** Minimum Standard

**Schutzbedarfsfeststellung:** Protection Requirements Assessment

**Sicherheitskonzept:** Security Concept

**Technische Richtlinie (TR):** Technical Guideline

**Zertifizierung:** Certification

**KRITIS:** Kritische Infrastrukturen (Critical Infrastructure)

**Datenschutz:** Data Protection

**Informationssicherheit:** Information Security

**Notfallmanagement:** Emergency Management

**Risikoanalyse:** Risk Analysis

**Sicherheitsvorfall:** Security Incident

**Telearbeit:** Telework/Remote Work

**Verschlüsselung:** Encryption

**Zwei-Faktor-Authentifizierung:** Two-Factor Authentication

---

**Technical Terms:**

**AES:** Advanced Encryption Standard

**DMARC:** Domain-based Message Authentication, Reporting, and Conformance

**DKIM:** DomainKeys Identified Mail

**EAL:** Evaluation Assurance Level

**eID:** Electronic Identity

**ICS:** Industrial Control Systems

**ISMS:** Information Security Management System

**OT:** Operational Technology

**PLC:** Programmable Logic Controller

**SCADA:** Supervisory Control and Data Acquisition

**SPF:** Sender Policy Framework

**TLS:** Transport Layer Security

**VPN:** Virtual Private Network

---

## Document Maintenance

**Version History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-02-18 | Documentation Team | Initial comprehensive BSI technical guidelines reference |

**Review Schedule:**
- Quarterly review for new BSI publications
- Annual comprehensive update for IT-Grundschutz Compendium
- Ad-hoc updates for critical standards and technical guidelines

**Change Management:**
- Monitor BSI website for new publications
- Track IT-Grundschutz Compendium updates
- Update cross-references as standards evolve
- Maintain alignment with framework templates
- Coordinate with NIST Technical Guidelines document

---

## Comparison: BSI vs. NIST Technical Guidelines

### Similarities

**Cryptography:**
- Both provide algorithm recommendations
- Similar key length requirements
- TLS/SSL guidance aligned
- Post-quantum cryptography preparation

**Risk Management:**
- Structured risk assessment approaches
- Control-based frameworks
- Continuous improvement focus

**Incident Response:**
- Similar incident response processes
- Emphasis on preparation and lessons learned
- Reporting requirements

**Cloud Security:**
- Control-based attestation (C5 vs. FedRAMP)
- Similar security domains
- Emphasis on transparency

---

### Differences

**Approach:**
- **BSI:** Prescriptive, module-based (IT-Grundschutz)
- **NIST:** Flexible, risk-based (RMF, CSF)

**Scope:**
- **BSI:** German/European focus, mandatory for German federal agencies
- **NIST:** US/International focus, mandatory for US federal agencies

**Methodology:**
- **BSI:** IT-Grundschutz modeling and base security check
- **NIST:** Risk Management Framework (RMF) with control tailoring

**Language:**
- **BSI:** Primary language German, English translations available
- **NIST:** Primary language English

**Certification:**
- **BSI:** ISO 27001 on IT-Grundschutz basis, Common Criteria, C5
- **NIST:** FedRAMP, FISMA compliance

---

### When to Use Which

**Use BSI Guidelines When:**
- Operating in Germany or German-speaking regions
- Subject to German regulations (IT Security Act, KRITIS)
- Seeking ISO 27001 certification with IT-Grundschutz
- Prefer structured, prescriptive approach
- Need German-language documentation

**Use NIST Guidelines When:**
- Operating in US or internationally
- Subject to US regulations (FISMA, FedRAMP)
- Prefer flexible, risk-based approach
- Need detailed technical specifications
- Working with US federal agencies

**Use Both When:**
- Operating internationally (Germany and US)
- Need comprehensive coverage
- Seeking multiple certifications
- Want defense-in-depth approach
- Serving diverse customer base

---

### Integration Strategy

**Complementary Use:**
1. Use BSI IT-Grundschutz for structured implementation
2. Use NIST technical guidelines for detailed specifications
3. Map controls between frameworks
4. Document compliance with both standards
5. Leverage templates for both frameworks

**Example:**
- Implement IT-Grundschutz modules for structure
- Apply NIST SP 800-52 for detailed TLS configuration
- Use BSI TR-02102-2 for German-specific requirements
- Document in both BSI Grundschutz and NIST 800-53 templates

---

## Conclusion

This BSI Technical Guidelines Reference provides comprehensive coverage of German IT security standards and best practices. Organizations operating in Germany or serving German customers should prioritize BSI guidelines, while those with international operations should consider integrating both BSI and NIST approaches.

The Handbook Generator provides templates for both BSI and NIST frameworks, enabling organizations to document compliance with either or both standards efficiently.

**Key Takeaways:**
- BSI provides authoritative guidance for German IT security
- IT-Grundschutz offers structured, comprehensive approach
- Technical Guidelines (TR) provide detailed specifications
- Integration with ISO 27001 enables international recognition
- Templates support efficient implementation and documentation

**Next Steps:**
1. Review applicable BSI standards for your organization
2. Assess current compliance status
3. Identify gaps and prioritize implementation
4. Use Handbook Generator templates for documentation
5. Engage BSI-certified auditors for certification (if desired)

---

**End of Document**

