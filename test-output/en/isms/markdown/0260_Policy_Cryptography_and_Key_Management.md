# Policy: Cryptography and Key Management

**Document-ID:** ISMS-0260
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



**Document ID:** 0260  
**Document Type:** Policy (abstract)  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.8.24 (incl. Amendment 1:2024)  
**Owner:** [TODO]  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** [TODO]  
**Next Review:** [TODO]

## 1. Purpose

This policy defines the principles for the use of cryptographic procedures and the management of cryptographic keys at **AdminSend GmbH**. It ensures that information is protected by appropriate cryptographic controls and keys are managed securely.

## 2. Scope

This policy applies to:

- **Organizational Units:** All departments and locations of AdminSend GmbH
- **Systems:** All IT systems, applications, databases, networks, cloud services
- **Data:** All data at rest, in transit, and in use
- **Cryptographic Procedures:** Encryption, hashing, digital signatures, certificates
- **Locations:** [[ netbox.site.name ]] and all other operational sites

**Exceptions:** Exceptions are only permitted through the defined exception process (`0640_Policy_Ausnahmen_und_Risk_Waivers.md`).

## 3. Principles (Policy Statements)

### 3.1 Risk-Based Use of Cryptography
Cryptographic procedures are deployed based on risk analysis. The protection requirements of information determine the strength and type of cryptographic controls.

### 3.2 Encryption of Sensitive Data
Sensitive and confidential data is encrypted both at rest and in transit:
- **Data at Rest:** Encryption of databases, file systems, backups, mobile devices
- **Data in Transit:** TLS/SSL for network communication, VPN for remote access
- **Data in Use:** Encryption in memory where technically feasible (e.g., confidential computing)

### 3.3 Use of Recognized Algorithms
Only recognized and standardized cryptographic algorithms are used:
- Symmetric encryption: AES-256 or higher
- Asymmetric encryption: RSA-2048 or higher, ECC with at least 256 bits
- Hashing: SHA-256 or higher
- Deprecated algorithms (MD5, SHA-1, DES, 3DES) are prohibited

### 3.4 Key Management Lifecycle
Cryptographic keys are managed securely throughout their entire lifecycle:
- **Generation:** Secure random number generators, sufficient key length
- **Storage:** Hardware Security Modules (HSM), Key Management Systems (KMS)
- **Distribution:** Secure transmission channels, authentication of recipients
- **Rotation:** Regular key rotation based on risk and compliance requirements
- **Archiving:** Secure retention for decryption of historical data
- **Destruction:** Secure deletion of keys no longer needed

### 3.5 Separation of Keys and Data
Cryptographic keys are stored separately from encrypted data. Keys must not be stored in plaintext in configuration files or source code.

### 3.6 Certificate Management
Digital certificates are managed centrally:
- Use of trusted Certificate Authorities (CA)
- Regular review and renewal of certificates
- Monitoring of expiring certificates
- Secure storage of private keys

### 3.7 Cryptographic Protocols
Secure cryptographic protocols are used for communication:
- TLS 1.2 or higher (TLS 1.3 preferred)
- SSH-2 for secure remote access
- IPsec for VPN connections
- Deprecated protocols (SSL, TLS 1.0/1.1) are prohibited

### 3.8 Compliance with Export Controls
The use of cryptography complies with national and international export control regulations.

## 4. Roles and Responsibilities

### RACI Matrix: Cryptography and Key Management

| Activity | CISO | IT Operations | Crypto Officer | Development | Compliance |
|----------|------|---------------|----------------|-------------|------------|
| Policy Creation | R/A | C | C | C | C |
| Crypto Architecture | A | C | R | C | I |
| Key Generation | C | R | R/A | I | I |
| Key Rotation | C | R | R/A | I | I |
| Certificate Management | C | R | R/A | I | I |
| Crypto Monitoring | A | C | R | I | C |
| Compliance Review | C | I | C | I | R/A |

**Legend:** R = Responsible (Execution), A = Accountable (Accountable), C = Consulted (Consulted), I = Informed (Informed)

### Key Roles

- **Policy Owner:** [TODO] (CISO)
- **Crypto Officer:** {{ meta-handbook.it_crypto_officer }}
- **Key Management Responsible:** {{ meta-handbook.it_key_manager }}
- **Implementation Responsible:** IT operations, development
- **Control/Audit Function:** ISMS, internal audit, compliance

## 5. Derivations (Guidelines/Standards/Processes)

Implementation details are defined in subordinate documents:

### Related Guidelines
- **0270_Richtlinie_Key_Management_und_Verschluesselung.md** - Detailed implementation guideline
- `0280_Policy_Datenklassifizierung_und_Informationshandling.md` - Data classification policy
- `0460_Policy_Lieferanten_und_Cloud_Sicherheit.md` - Cloud security policy
- `0600_Policy_Netzwerksicherheit.md` - Network security policy

### Related Standards/Baselines
- Cryptographic algorithms standard
- Key length requirements
- TLS/SSL configuration standard
- Certificate lifecycle standard

### Related Processes
- Key generation and rotation process
- Certificate renewal process
- Incident response for key compromise
- Crypto agility process (migration to new algorithms)

## 6. Compliance, Monitoring, and Enforcement

### Metrics and KPIs
- Number of encrypted systems and databases
- Encryption rate of sensitive data (target: 100%)
- Number of expiring certificates (target: 0 expired certificates)
- Average key rotation time
- Number of violations of crypto standards
- Number of compromised keys

### Evidence and Proof
- Encryption inventory
- Key management logs
- Certificate register
- Crypto compliance reports
- Penetration test results
- Audit reports on cryptographic controls

### Consequences for Violations
Violations of this policy are handled according to applicable HR and compliance processes:
- **Use of weak algorithms:** Immediate remediation, retraining
- **Insecure key storage:** Immediate key rotation, investigation
- **Key compromise:** Incident response, revocation, forensic analysis
- **Repeated violations:** Employment law consequences

## 7. Exceptions

Exceptions to this policy are only permitted in justified exceptional cases:

- **Exception Process:** See `0640_Policy_Ausnahmen_und_Risk_Waivers.md`
- **Approval:** Exceptions must be approved by CISO and crypto officer
- **Documentation:** All exceptions are documented in the risk register
- **Time Limit:** Exceptions are generally time-limited and regularly reviewed
- **Compensating Controls:** Exceptions require alternative security measures

## 8. References

### Internal Documents
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS policy
- `0270_Richtlinie_Key_Management_und_Verschluesselung.md` - Detailed guideline
- `0280_Policy_Datenklassifizierung_und_Informationshandling.md` - Data classification policy
- `0080_ISMS_Risikoregister_Template.md` - Risk register

### External Standards and Requirements
- **ISO/IEC 27001:2022 Annex A.8.24** - Use of cryptography
- **ISO/IEC 27002:2022** - Information security controls
- **NIST SP 800-57** - Recommendation for Key Management
- **NIST SP 800-175B** - Guideline for Using Cryptographic Standards
- **BSI TR-02102** - Cryptographic Procedures: Recommendations and Key Lengths
- **FIPS 140-2/140-3** - Security Requirements for Cryptographic Modules
- **eIDAS Regulation (EU 910/2014)** - Electronic Identification and Trust Services

**Approved by:**  
{{ meta-handbook.management_ceo }}, Management  
Date: [TODO]

**Next Review:** [TODO] (annually or as needed)

