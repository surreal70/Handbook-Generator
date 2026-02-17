# Physical Security

**Document-ID:** [FRAMEWORK]-0420
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
This template documents physical security controls.
It aligns with PCI-DSS v4.0 Requirement 9 (Restrict Physical Access to Cardholder Data).

Customization required:
- Define physical access controls
- Document facility security
- Include visitor management
- Define media handling procedures
-->

## 1. Purpose

This document defines the physical security controls for {{ meta-organisation.name }} in accordance with PCI-DSS Requirement 9.

### 1.1 Objectives

- **Physical Protection:** Protect CDE systems from unauthorized access
- **Access Control:** Restrict physical access
- **Media Security:** Secure handling of media
- **Compliance:** Fulfillment of PCI-DSS Requirement 9

### 1.2 Scope

**Affected Locations:**
- Data centers with CDE systems
- Server rooms
- Offices with POS terminals
- Media storage rooms

## 2. Physical Access Control

### 2.1 Access Control Systems

**Implemented Systems:**
- Badge system: [TODO: Name of system]
- Biometric authentication: [TODO: Type]
- Video surveillance: [TODO: Number of cameras]
- Alarm system: [TODO: Name of system]

**Requirements:**
- Unique identification of each person
- Logging of all access
- Automatic lockout after business hours
- Alerting on unauthorized access

### 2.2 Access Authorization

**Authorization Levels:**

| Level | Authorization | Areas | Personnel |
|-------|---------------|-------|-----------|
| Level 1 | Full access | All areas | Facility Manager, CISO |
| Level 2 | CDE access | Data center, server rooms | IT Administrators |
| Level 3 | Limited | Offices with POS | Cashiers, Support |
| Level 4 | Escorted | All areas | Visitors, Service providers |

**Approval Process:**
1. Request by manager
2. Security review
3. CISO approval (for CDE areas)
4. Badge issuance
5. Documentation

### 2.3 Data Center Access Control

**Requirements:**
- Two-factor authentication (Badge + Biometrics)
- Mantrap/Airlock
- Video surveillance (24/7)
- Alerting on unauthorized access
- Logging of all access

**Authorized Personnel:**
- Data center personnel
- Authorized IT administrators
- Maintenance personnel (with escort only)

**Visitor Policy:**
- Pre-registration required
- Escort requirement
- Visitor badge
- Logging

## 3. Visitor Management

### 3.1 Visitor Registration

**Process:**
1. Pre-registration by host
2. Identity verification upon arrival
3. Issue visitor badge
4. Security briefing
5. Escort by authorized employee
6. Return badge upon departure

**Visitor Badge:**
- Clearly visible
- Time-limited
- Unique number
- Photo (optional)

### 3.2 Visitor Escort

**Requirements:**
- Constant escort in CDE areas
- Escort must be authorized
- No unattended visitors
- Document escort

**Exceptions:**
- Public areas (reception, cafeteria)
- Only after security briefing

### 3.3 Visitor Log

**Logged Information:**
- Visitor name
- Company
- Purpose of visit
- Host
- Arrival time
- Departure time
- Areas visited
- Escort

**Retention:** 90 days

## 4. Employee Identification

### 4.1 Employee Badges

**Requirements:**
- Photo ID
- Name
- Employee number
- Department
- Expiration date
- Visibly worn

**Issuance:**
- Upon hiring
- After identity verification
- Documentation

**Return:**
- Upon termination
- Upon loss (deactivation + reissuance)

### 4.2 Employee/Visitor Distinction

**Measures:**
- Different badge colors
- Clear "VISITOR" marking
- Time-limited visitor badges

## 5. Video Surveillance

### 5.1 Camera Locations

**Monitored Areas:**
- All data center entrances
- Server rooms
- Areas with POS terminals
- Media storage rooms
- Parking lots (optional)

**Camera Specifications:**
- Minimum resolution: 1080p
- Night vision capable
- Motion detection
- Tamper protection

### 5.2 Recording and Storage

**Requirements:**
- Continuous recording (24/7)
- Retention: 90 days
- Secure storage (encrypted)
- Access control to recordings
- Backup of recordings

**Access to Recordings:**
- Only authorized personnel
- Logging of all access
- Approval by Security Manager

### 5.3 Privacy

**Measures:**
- Signs indicating video surveillance
- Privacy policy
- No surveillance of private areas (restrooms, changing rooms)
- GDPR compliance

## 6. Media Handling

### 6.1 Media Classification

**Classification Levels:**

| Level | Description | Examples | Handling |
|-------|-------------|----------|----------|
| Critical | CHD in cleartext | Backup tapes with unencrypted CHD | Encrypted, secured |
| Confidential | CHD encrypted | Encrypted backups | Secured |
| Internal | No CHD | System logs | Standard |
| Public | No sensitive data | Marketing material | No restriction |

### 6.2 Media Storage

**Requirements:**
- Secured storage room
- Access control
- Climate control
- Fire protection
- Inventory management

**Storage Room Specifications:**
- Fire-resistant cabinets for critical media
- Locked cabinets
- Access control (badge system)
- Video surveillance
- Logging of all access

### 6.3 Media Transport

**Internal Transport:**
- Sealed containers
- Escort person
- Documentation (handover protocol)

**External Transport:**
- Encrypted media
- Sealed containers
- Trusted courier
- Tracking
- Insurance
- Documentation

**Courier Requirements:**
- Background check
- Confidentiality agreement
- Insurance
- Tracking system

## 7. Media Destruction

### 7.1 Destruction Methods

**Paper:**
- Cross-cut shredder (DIN 66399 P-4 or higher)
- For CHD: P-5 or higher
- Secure disposal of shreds

**Electronic Media:**

| Media Type | Method | Standard |
|------------|--------|----------|
| Hard drives | Degaussing + physical destruction | NIST 800-88 |
| SSDs | Cryptographic erasure + destruction | NIST 800-88 |
| USB drives | Physical destruction | NIST 800-88 |
| CDs/DVDs | Shredding | DIN 66399 O-4 |
| Backup tapes | Degaussing + shredding | NIST 800-88 |

**Certification:**
- Destruction certificate required
- Document all destroyed media
- Record serial numbers

### 7.2 Destruction Service Provider

**Requirements:**
- Certified service provider (e.g., DIN 66399)
- Confidentiality agreement
- On-site destruction or secure pickup
- Destruction certificate
- Insurance

**Service Provider:** [TODO: Name of service provider]

### 7.3 Destruction Log

**Logged Information:**
- Date of destruction
- Media type
- Serial number (if available)
- Destruction method
- Performed by
- Certificate number

**Retention:** 3 years

## 8. Point-of-Sale (POS) Security

### 8.1 POS Terminal Protection

**Physical Security:**
- Tamper protection (Tamper-evident Seals)
- Regular inspection
- Secure mounting
- Video surveillance of area

**Inspection:**
- Daily before business opening
- After maintenance
- Upon suspicion of tampering

**Checklist:**
- [ ] Tamper seal intact
- [ ] No unusual devices connected
- [ ] No damage
- [ ] Firmware version correct

### 8.2 POS Terminal Inventory

**Inventory Management:**
- List of all POS terminals
- Serial numbers
- Locations
- Responsible persons
- Maintenance history

**Quarterly Review:**
- Validate inventory
- Check locations
- Verify tamper seals
- Documentation

### 8.3 POS Terminal Maintenance

**Maintenance Process:**
1. Announce maintenance
2. Escort by authorized employee
3. Document all activities
4. Apply new tamper seals
5. Functional test
6. Documentation

## 9. Backup Media

### 9.1 Backup Media Security

**Requirements:**
- Encrypted backups
- Secure storage
- Offsite storage
- Access control
- Inventory management

**Storage:**
- Onsite: Fire-resistant safe
- Offsite: Secure data center or vault

### 9.2 Backup Media Transport

**Process:**
- Encrypted media
- Sealed containers
- Trusted courier
- Handover protocol
- Documentation

## 10. Workplace Security

### 10.1 Clean Desk Policy

**Requirements:**
- No sensitive documents on desks
- Lock screens when absent
- Documents in locked cabinets
- No passwords on sticky notes

**Controls:**
- Regular inspections
- Employee awareness

### 10.2 Screen Privacy

**Requirements:**
- Privacy filters for screens with CHD
- Screens not visible from outside
- Automatic screen lock (15 minutes)

## 11. Emergency Access

### 11.1 Break-Glass Procedure

**Process:**
- Sealed envelope with emergency access credentials
- Storage in safe
- Access only with witness
- Document each use
- Immediate password change after use

**Documentation:**
- Date and time
- Reason for emergency access
- Performed by
- Witness
- Actions performed

### 11.2 Emergency Evacuation

**Process:**
- Evacuation plan
- Assembly points
- Responsible persons
- Regular drills

**Security Measures:**
- Automatic lockdown of all systems
- Activate alarm system
- Notify security

## 12. Compliance Validation

### 12.1 Validation Activities

**Quarterly:**
- POS terminal inspection
- Media inventory
- Visitor log review
- Video surveillance test

**Annually:**
- Physical security audit
- Penetration test (physical)
- Employee awareness

### 12.2 Validation Documentation

**Required Evidence:**
- Access control logs
- Visitor logs
- POS inspection logs
- Media destruction certificates
- Video recordings (90 days)

<!-- End of template -->
