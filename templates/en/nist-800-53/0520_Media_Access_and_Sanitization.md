# Media Access and Sanitization

**Document ID:** NIST-0520  
**Control Family:** Media Protection (MP)  
**Controls:** MP-2, MP-3, MP-4, MP-5, MP-6, MP-7  
**Organization:** {{ meta.organization.name }}  
**Owner:** {{ meta.document.owner }}  
**Version:** {{ meta.document.version }}  
**Status:** Draft / In Review / Approved  
**Last Updated:** {{ meta.document.last_updated }}  

---

## 1. Control Description

This document covers multiple media protection controls:
- **MP-2:** Media Access
- **MP-3:** Media Marking
- **MP-4:** Media Storage
- **MP-5:** Media Transport
- **MP-6:** Media Sanitization
- **MP-7:** Media Use

## 2. Control Implementation

### 2.1 Media Access (MP-2)

**Access Controls:**
[TODO: Describe access control mechanisms for media]

**Authorization Process:**
[TODO: Describe authorization process]

### 2.2 Media Marking (MP-3)

**Marking Requirements:**
- Classification labels
- Handling instructions
- Distribution limitations

[TODO: Specify marking requirements]

### 2.3 Media Storage (MP-4)

**Storage Requirements:**
- Physical security controls
- Environmental controls
- Access logging

[TODO: Describe storage requirements]

### 2.4 Media Transport (MP-5)

**Transport Procedures:**
- Encryption requirements
- Chain of custody
- Approved carriers

[TODO: Detail transport procedures]

### 2.5 Media Sanitization (MP-6)

**Sanitization Methods:**
| Media Type | Method | Standard |
|------------|--------|----------|
| Hard Drives | Cryptographic Erase / Physical Destruction | NIST SP 800-88 |
| SSDs | Cryptographic Erase / Physical Destruction | NIST SP 800-88 |
| USB Drives | Overwrite / Physical Destruction | NIST SP 800-88 |
| Optical Media | Physical Destruction | NIST SP 800-88 |
| Paper | Shredding / Pulping | Cross-cut P-4 or higher |

[TODO: Specify sanitization methods]

### 2.6 Media Use (MP-7)

**Usage Restrictions:**
- Approved media types
- Prohibited uses
- Monitoring requirements

[TODO: Define usage restrictions]

## 3. Control Enhancements

- **MP-2(1):** Automated Restricted Access
- **MP-3(1):** Automated Marking
- **MP-4(1):** Cryptographic Protection
- **MP-5(4):** Cryptographic Protection
- **MP-6(1):** Review, Approve, Track, Document, and Verify
- **MP-6(2):** Equipment Testing
- **MP-6(3):** Nondestructive Techniques
- **MP-7(1):** Prohibit Use Without Owner

[TODO: Mark applicable enhancements]

## 4. Implementation Status

**Status:** [TODO: Implemented / Partially Implemented / Planned / Not Applicable]  
**Implementation Date:** [TODO: Date]  
**Responsible:** [TODO: Name/Role]  

## 5. Assessment

**Assessment Method:** Examine, Interview, Test  
**Assessment Status:** [TODO: Satisfied / Other than Satisfied / Not Applicable]  
**Findings:** [TODO: Description]  

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial creation |

<!-- End of template -->
