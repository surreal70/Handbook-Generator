# Guideline: Access, Visitors and Equipment Protection

**Document-ID:** [FRAMEWORK]-0490
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

This guideline specifies the `0480_Policy_Physical_Security.md` and defines:
- Access control systems and processes
- Visitor management
- Physical protection of IT equipment

**Scope:** All locations of **{{ meta-organisation.name }}**

## 2. Security Zones

### 2.1 Zone Classification

**Zone 1 (Public):**
- Reception area, lobby
- No access control
- Video surveillance

**Zone 2 (Internal):**
- Office areas, meeting rooms
- Access card required
- Employees and registered visitors

**Zone 3 (Restricted):**
- Server rooms, data centers
- Additional authentication (PIN, biometrics)
- Authorized personnel only

**Zone 4 (High Security):**
- Critical infrastructure
- Four-eyes principle
- Video surveillance and logging

## 3. Access Control System

### 3.1 Access Cards

**Card Type:** RFID cards with photo  
**Issuance:** During onboarding by HR  
**Validity:** Until contract end

**Card Loss:**
1. Immediate report to Security
2. Disable card (within 15 minutes)
3. Issue new card
4. Documentation

### 3.2 Biometric Authentication

**For Zone 3/4:**
- Fingerprint scanner
- Iris scanner (optional)
- Data protection compliant (GDPR)

### 3.3 Access Logs

**Logging:**
- All access attempts (success and failure)
- Timestamp, person, door/zone
- Retention: {{ meta-handbook.retention_access_years }} years

**Monitoring:**
- Alerts for unauthorized access attempts
- Alerts for access outside business hours (Zone 3/4)

## 4. Visitor Management

### 4.1 Visitor Registration

**Process:**
1. Host pre-registers visitor (email, portal)
2. Visitor reports to reception
3. ID check (ID card, driver's license)
4. Issue visitor badge
5. Host picks up visitor

**Visitor Badge:**
- Temporary RFID card
- Validity: 1 day
- Automatic deactivation after expiration

### 4.2 Escort

**Requirement:**
- Visitors must be escorted at all times
- No unaccompanied visitors in Zone 2/3/4
- Host responsible

**Exceptions:**
- Long-term contractors with own badge
- After background check and NDA

### 4.3 Visitor Log

**Documentation:**
- Name, company, ID number
- Host, purpose of visit
- Entry and exit time
- Retention: {{ meta-handbook.retention_visitor_years }} years

## 5. Physical Protection of Equipment

### 5.1 Server Rooms and Data Centers

**Requirements:**
- Air conditioning (18-27°C, 40-60% humidity)
- Fire detection and suppression system
- Uninterruptible power supply (UPS)
- Emergency generator
- Water sensors (leak detection)

**Access Control:**
- Zone 3 or 4
- Logging of all access
- Video surveillance

### 5.2 Workspaces

**Clean Desk Policy:**
- No confidential documents on desk (end of day)
- Screen lock when absent
- Lockable cabinets for confidential materials

**Kensington Locks:**
- Mandatory for laptops in offices
- Theft protection

### 5.3 Mobile Devices

**Security Requirements:**
- Encryption (BitLocker, FileVault)
- Remote wipe capability (MDM)
- No confidential data locally (prefer cloud storage)

**In Case of Loss:**
1. Immediate report to IT support
2. Trigger remote wipe
3. Create incident ticket
4. Police report (in case of theft)

## 6. Video Surveillance

### 6.1 Monitored Areas

**Cameras:**
- Entrances and exits
- Server rooms (Zone 3/4)
- Parking lots
- No surveillance in offices, restrooms, changing rooms

### 6.2 Data Protection

**GDPR Compliance:**
- Signs indicating video surveillance
- Purpose limitation (security, access control)
- Access only for authorized personnel
- Retention: 30 days (then automatic deletion)

## 7. Emergency Access

### 7.1 Break-Glass Procedure

**For Emergencies:**
- Physical key in sealed envelope
- Storage in safe
- Use only in emergencies (fire, medical emergency)
- Documentation of each use

### 7.2 Evacuation

**Evacuation Plan:**
- Escape routes marked
- Assembly points defined
- Regular evacuation drills (annually)

## 8. Compliance and Audit

### 8.1 Metrics (KPIs)

| Metric | Target Value |
|--------|--------------|
| Unescorted visitors | 0 |
| Access card losses | < 5 per year |
| Clean-desk compliance | > 90% |
| Evacuation drills | 1 per year |

### 8.2 Audit Evidence

- Access logs
- Visitor logs
- Video recordings (30 days)
- Evacuation drill protocols

## 9. References

### Internal Documents
- `0480_Policy_Physical_Security.md`
- `0300_Policy_Asset_Management.md`

### External Standards
- **ISO/IEC 27001:2022 Annex A.7.1** - Physical security perimeters
- **ISO/IEC 27001:2022 Annex A.7.2** - Physical entry
- **ISO/IEC 27001:2022 Annex A.7.3** - Securing offices, rooms and facilities
- **ISO/IEC 27001:2022 Annex A.7.4** - Physical security monitoring

**Approved by:** {{ meta-organisation-roles.role_CISO }}, CISO  
**Next Review:** {{ meta-handbook.next_review }}

