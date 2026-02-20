# Appendix: Glossary and Abbreviations

**Document-ID:** PCI-DSS-0710
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



## 1. Purpose

This document defines all terms and abbreviations used in the PCI-DSS documentation of AdminSend GmbH.

## 2. PCI-DSS Terms

### A

**Acquiring Bank (Acquirer)**
- Bank that processes payment card transactions for merchants
- Responsible for merchant's PCI-DSS compliance

**AOC (Attestation of Compliance)**
- Confirmation of PCI-DSS compliance
- Issued by QSA or through self-assessment

**ASV (Approved Scanning Vendor)**
- Vendor approved by PCI SSC for vulnerability scans
- Performs quarterly external scans

**Authentication**
- Process of identity verification
- Typically through password, token, or biometrics

**Authorization**
- Process of permission verification
- Determines which actions a user may perform

### C

**Cardholder Data (CHD)**
- Cardholder data
- Includes PAN, cardholder name, expiration date, service code

**Cardholder Data Environment (CDE)**
- Environment that stores, processes, or transmits cardholder data
- Includes systems, networks, people, and processes

**CDE Segmentation**
- Network segmentation to isolate CDE
- Reduces compliance scope

**CVV/CVC/CVV2/CVC2**
- Card Verification Value/Code
- 3-4 digit security code
- Must NOT be stored after authorization

### D

**Data Retention**
- Data retention policy
- Defines how long data may be stored

**Default Account**
- Vendor pre-configured account
- Must be disabled or password changed

**DMZ (Demilitarized Zone)**
- Network segment between internet and internal network
- For publicly accessible services

### E

**Encryption**
- Encryption of data
- Required for stored and transmitted CHD

**Encryption Key**
- Key for encryption and decryption
- Must be securely stored and managed

### F

**FIM (File Integrity Monitoring)**
- File integrity monitoring
- Detects unauthorized changes to critical files

**Firewall**
- Network security device
- Controls traffic between network segments

### H

**Hashing**
- One-way encryption
- For password storage

**Hardening**
- System hardening
- Removal of unnecessary services and functions

### I

**IDS/IPS (Intrusion Detection/Prevention System)**
- System for detecting and preventing attacks
- Required at all CDE boundaries

**Incident Response**
- Response to security incidents
- Structured process for handling incidents

### K

**Key Management**
- Management of cryptographic keys
- Includes generation, storage, rotation, destruction

### L

**Least Privilege**
- Principle of minimum permissions
- Users receive only required access rights

**Logging**
- Recording of events
- Required for all access to CDE and CHD

### M

**Malware**
- Malicious software
- Viruses, trojans, ransomware, etc.

**Merchant**
- Merchant that accepts payment cards
- Subject to PCI-DSS compliance

**MFA (Multi-Factor Authentication)**
- Multi-factor authentication
- Required for CDE access

### N

**Need-to-Know**
- Principle of authorized knowledge
- Access only with business necessity

**Network Segmentation**
- Network segmentation
- Separation of CDE and corporate network

**NTP (Network Time Protocol)**
- Protocol for time synchronization
- Required for correct timestamps in logs

### P

**PA-DSS (Payment Application Data Security Standard)**
- Security standard for payment applications
- Complements PCI-DSS

**PAN (Primary Account Number)**
- Primary account number
- 13-19 digit card number
- Core of cardholder data

**Penetration Test**
- Security test through simulated attacks
- Required annually

**PCI DSS (Payment Card Industry Data Security Standard)**
- Security standard for payment card industry
- Defines requirements for protecting cardholder data

**PCI SSC (Payment Card Industry Security Standards Council)**
- Organization that develops and manages PCI-DSS

**POS (Point of Sale)**
- Point of sale
- Terminal for card input

### Q

**QSA (Qualified Security Assessor)**
- Qualified security assessor
- Performs PCI-DSS assessments

### R

**RBAC (Role-Based Access Control)**
- Role-based access control
- Permissions based on roles

**Risk Assessment**
- Risk analysis
- Required annually

**ROC (Report on Compliance)**
- Compliance report
- Created by QSA after assessment

### S

**SAD (Sensitive Authentication Data)**
- Sensitive authentication data
- Full track data, CVV, PIN
- Must NOT be stored after authorization

**SAQ (Self-Assessment Questionnaire)**
- Self-assessment questionnaire
- For smaller merchants without QSA assessment

**Scope**
- Scope of PCI-DSS compliance
- All systems that store, process, or transmit CHD

**Segmentation**
- See Network Segmentation

**Service Provider**
- Service provider that processes CHD on behalf
- Subject to PCI-DSS compliance

**SIEM (Security Information and Event Management)**
- System for central log management and analysis

**Strong Cryptography**
- Strong encryption
- At least AES-128, RSA-2048

### T

**Tokenization**
- Replacement of PAN with token
- Reduces compliance scope

**TLS (Transport Layer Security)**
- Encryption protocol for data transmission
- At least TLS 1.2 required

**Track Data**
- Magnetic stripe data
- Track 1 and Track 2
- Must NOT be stored after authorization

### V

**Vulnerability**
- Vulnerability in system or application
- Must be identified and remediated

**Vulnerability Scan**
- Vulnerability scan
- Required quarterly (external and internal)

### W

**WAF (Web Application Firewall)**
- Firewall for web applications
- Protection against OWASP Top 10

**WORM (Write Once Read Many)**
- Storage that can only be written once
- For log storage to ensure integrity

## 3. Abbreviations

| Abbreviation | Meaning |
|--------------|---------|
| ACL | Access Control List |
| AES | Advanced Encryption Standard |
| AOC | Attestation of Compliance |
| API | Application Programming Interface |
| ASV | Approved Scanning Vendor |
| AV | Antivirus |
| BAA | Business Associate Agreement |
| CA | Certificate Authority |
| CDE | Cardholder Data Environment |
| CHD | Cardholder Data |
| CISO | Chief Information Security Officer |
| CRL | Certificate Revocation List |
| CVV | Card Verification Value |
| CVSS | Common Vulnerability Scoring System |
| DAST | Dynamic Application Security Testing |
| DBA | Database Administrator |
| DMZ | Demilitarized Zone |
| DPA | Data Processing Agreement |
| EAL | Evaluation Assurance Level |
| EDR | Endpoint Detection and Response |
| FIM | File Integrity Monitoring |
| GDPR | General Data Protection Regulation |
| HIDS | Host-based Intrusion Detection System |
| HTTPS | Hypertext Transfer Protocol Secure |
| IAM | Identity and Access Management |
| IDS | Intrusion Detection System |
| IPS | Intrusion Prevention System |
| ISO | International Organization for Standardization |
| JIT | Just-in-Time |
| KPI | Key Performance Indicator |
| LDAP | Lightweight Directory Access Protocol |
| MAC | Media Access Control |
| MDM | Mobile Device Management |
| MFA | Multi-Factor Authentication |
| NIDS | Network-based Intrusion Detection System |
| NIST | National Institute of Standards and Technology |
| NTP | Network Time Protocol |
| OCSP | Online Certificate Status Protocol |
| OS | Operating System |
| OWASP | Open Web Application Security Project |
| PA-DSS | Payment Application Data Security Standard |
| PAM | Privileged Access Management |
| PAN | Primary Account Number |
| PCI DSS | Payment Card Industry Data Security Standard |
| PCI SSC | Payment Card Industry Security Standards Council |
| PIN | Personal Identification Number |
| PKI | Public Key Infrastructure |
| POA&M | Plan of Action and Milestones |
| POS | Point of Sale |
| QSA | Qualified Security Assessor |
| RACI | Responsible, Accountable, Consulted, Informed |
| RBAC | Role-Based Access Control |
| RFC | Request for Comments |
| ROC | Report on Compliance |
| RPO | Recovery Point Objective |
| RSA | Rivest-Shamir-Adleman (encryption algorithm) |
| RTO | Recovery Time Objective |
| SAD | Sensitive Authentication Data |
| SAQ | Self-Assessment Questionnaire |
| SAST | Static Application Security Testing |
| SDLC | Software Development Lifecycle |
| SIEM | Security Information and Event Management |
| SOC | Security Operations Center |
| SQL | Structured Query Language |
| SSH | Secure Shell |
| SSL | Secure Sockets Layer (deprecated, replaced by TLS) |
| SSO | Single Sign-On |
| TLS | Transport Layer Security |
| TOE | Target of Evaluation |
| UTC | Coordinated Universal Time |
| VLAN | Virtual Local Area Network |
| VPN | Virtual Private Network |
| WAF | Web Application Firewall |
| WORM | Write Once Read Many |

## 4. Organization-Specific Terms

[TODO: Add organization-specific terms and abbreviations here]

| Term/Abbreviation | Meaning |
|-------------------|---------|
| [TODO] | [TODO] |


