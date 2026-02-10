# Facility Access Controls

**Document ID:** HIPAA-0300  
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
This template documents Facility Access Controls (Physical Safeguard).
It aligns with HIPAA Security Rule §164.310(a)(1) - Facility Access Controls.

Required (R) Standard with Addressable (A) Implementation Specifications:
- Contingency Operations (A)
- Facility Security Plan (A)
- Access Control and Validation Procedures (A)
- Maintenance Records (A)
-->

## 1. Purpose

This document describes the Facility Access Controls for {{ meta.organization.name }} to limit physical access to electronic information systems and the facilities in which they are housed, while ensuring properly authorized access is allowed.

### 1.1 HIPAA Requirement

**Standard:** §164.310(a)(1) - Facility Access Controls (Required)

**Implementation Specifications:**
- §164.310(a)(2)(i) - Contingency Operations (Addressable)
- §164.310(a)(2)(ii) - Facility Security Plan (Addressable)
- §164.310(a)(2)(iii) - Access Control and Validation Procedures (Addressable)
- §164.310(a)(2)(iv) - Maintenance Records (Addressable)

## 2. Facility Inventory

### 2.1 Facilities with ePHI

| Facility ID | Facility Name | Address | Type | ePHI Systems | Access Level |
|-------------|---------------|---------|------|--------------|--------------|
| [TODO: FAC-001] | Main Data Center | [TODO: Address] | Data Center | All production systems | Restricted |
| [TODO: FAC-002] | Main Clinic | [TODO: Address] | Clinical | EHR workstations | Controlled |
| [TODO: FAC-003] | Administrative Office | [TODO: Address] | Office | Billing systems | Controlled |
| [TODO: FAC-004] | Backup Site | [TODO: Address] | DR Site | Backup systems | Restricted |

### 2.2 Facility Classification

**Restricted Access:**
- Data centers
- Server rooms
- Network equipment rooms
- Backup storage areas

**Controlled Access:**
- Clinical areas
- Administrative offices
- Medical records rooms

**Public Access:**
- Waiting rooms
- Public corridors
- Cafeteria

## 3. Contingency Operations

### 3.1 Emergency Access Procedures

**Purpose:** Establish procedures to allow facility access in support of restoration of lost data under the disaster recovery and emergency mode operations plan.

**Emergency Scenarios:**
- Fire or natural disaster
- Power failure
- System failure requiring immediate access
- Security incident requiring investigation

**Emergency Access Process:**
1. **Authorization:** Security Officer or designee authorizes emergency access
2. **Escort:** Emergency personnel escorted by authorized staff
3. **Documentation:** All emergency access logged
4. **Restoration:** Normal access controls restored after emergency
5. **Review:** Post-incident review of emergency access

**Emergency Contacts:**
| Role | Name | Phone (24/7) | Backup |
|------|------|--------------|--------|
| Security Officer | {{ meta.roles.security_officer.name }} | [TODO: Phone] | [TODO: Backup name/phone] |
| Facility Manager | [TODO: Name] | [TODO: Phone] | [TODO: Backup] |
| IT Manager | [TODO: Name] | [TODO: Phone] | [TODO: Backup] |

### 3.2 Emergency Access Equipment

**Emergency Access Tools:**
- Master keys (secured in break-glass box)
- Access cards (emergency override)
- Lock bypass tools (authorized personnel only)
- Emergency lighting
- Communication devices

**Storage Location:** [TODO: Secure location with documented access]

## 4. Facility Security Plan

### 4.1 Physical Security Measures

**Perimeter Security:**
- Fencing: [TODO: Yes/No, Description]
- Gates: [TODO: Yes/No, Description]
- Lighting: [TODO: Description]
- Signage: [TODO: "Authorized Personnel Only" signs]
- Landscaping: [TODO: Clear sight lines]

**Building Security:**
- Exterior doors: [TODO: Number, locking mechanisms]
- Windows: [TODO: Security measures]
- Loading docks: [TODO: Security measures]
- Roof access: [TODO: Security measures]

**Interior Security:**
- Reception/Security desk: [TODO: Yes/No, Hours]
- Security guards: [TODO: Yes/No, Schedule]
- Visitor management: [TODO: System/Process]
- Escort requirements: [TODO: Areas requiring escort]

**Data Center/Server Room Security:**
- Dedicated room: [TODO: Yes/No]
- Reinforced walls: [TODO: Yes/No]
- Raised floor: [TODO: Yes/No]
- Fire suppression: [TODO: Type]
- Environmental monitoring: [TODO: Temperature, humidity]
- Water detection: [TODO: Yes/No]
- Backup power: [TODO: UPS, generator]

### 4.2 Access Control Systems

**Physical Access Control System:**
- **System Type:** [TODO: Card reader, biometric, keypad]
- **Vendor:** [TODO: Vendor name]
- **Coverage:** [TODO: Doors/areas covered]
- **Monitoring:** [TODO: 24/7 monitoring, alerts]

**Access Control Features:**
- Individual identification
- Time-based access restrictions
- Area-based access restrictions
- Anti-passback
- Audit logging
- Real-time alerts

**Access Card Management:**
- Card issuance process
- Card deactivation process
- Lost/stolen card procedures
- Card return upon termination

### 4.3 Surveillance Systems

**Video Surveillance:**
- **Coverage:** [TODO: Entrances, exits, server rooms, etc.]
- **Camera Type:** [TODO: Fixed, PTZ, resolution]
- **Recording:** [TODO: Continuous, motion-activated]
- **Retention:** [TODO: Days/months]
- **Monitoring:** [TODO: Live monitoring, review schedule]

**Surveillance Locations:**
| Location | Camera Count | Recording | Retention | Purpose |
|----------|--------------|-----------|-----------|---------|
| [TODO: Main entrance] | [TODO: 2] | Continuous | [TODO: 90 days] | Access monitoring |
| [TODO: Server room] | [TODO: 1] | Continuous | [TODO: 90 days] | Security monitoring |
| [TODO: Parking lot] | [TODO: 4] | Motion | [TODO: 30 days] | Perimeter security |

## 5. Access Control and Validation Procedures

### 5.1 Access Authorization

**Authorization Process:**
1. **Request:** Manager submits access request
2. **Justification:** Business need documented
3. **Approval:** Security Officer approves
4. **Provisioning:** Facility Manager provisions access
5. **Documentation:** Access logged in system
6. **Notification:** Employee notified of access granted

**Access Levels:**
| Level | Description | Authorization Required | Areas Accessible |
|-------|-------------|------------------------|------------------|
| Level 1 - Public | General public | None | Waiting areas, public corridors |
| Level 2 - Employee | Regular employees | Manager approval | Office areas, break rooms |
| Level 3 - Clinical | Clinical staff | Manager + Privacy Officer | Clinical areas, medical records |
| Level 4 - IT | IT staff | IT Manager + Security Officer | Server rooms, network closets |
| Level 5 - Executive | Executive access | CEO approval | All areas |

### 5.2 Visitor Management

**Visitor Procedures:**
1. **Check-in:** Visitor checks in at reception
2. **Identification:** Photo ID required and recorded
3. **Badge:** Visitor badge issued
4. **Escort:** Visitor escorted at all times in restricted areas
5. **Log:** Visit logged (name, company, purpose, time in/out, host)
6. **Check-out:** Visitor returns badge and checks out

**Visitor Types:**
- Vendors/contractors
- Business associates
- Auditors
- Guests
- Delivery personnel

**Visitor Badge:** Clearly marked "VISITOR" badge, different color from employee badges

### 5.3 Access Validation

**Access Review Process:**
- **Frequency:** Quarterly
- **Reviewer:** Facility Manager + Security Officer
- **Scope:** All active access permissions
- **Actions:** Revoke unnecessary access, update records

**Access Validation Checklist:**
- [ ] Verify employee still requires access
- [ ] Verify access level appropriate for role
- [ ] Verify no terminated employees have active access
- [ ] Verify no expired temporary access
- [ ] Update access documentation

### 5.4 Access Termination

**Termination Process:**
1. **Notification:** HR notifies Facility Manager and Security Officer
2. **Immediate Revocation:** Access revoked immediately upon termination
3. **Badge Collection:** Employee badge collected
4. **Key Collection:** All keys collected
5. **Verification:** Access termination verified in system
6. **Documentation:** Termination logged

**Termination Checklist:**
- [ ] Access card deactivated
- [ ] Keys returned
- [ ] Alarm codes changed (if applicable)
- [ ] Visitor escort privileges revoked
- [ ] Documentation updated

## 6. Maintenance Records

### 6.1 Facility Maintenance

**Maintenance Activities:**
- Access control system maintenance
- Surveillance system maintenance
- Lock and key maintenance
- Alarm system maintenance
- Fire suppression system maintenance
- Environmental controls maintenance
- Emergency lighting maintenance

**Maintenance Schedule:**
| System | Maintenance Type | Frequency | Vendor | Last Service | Next Service |
|--------|------------------|-----------|--------|--------------|--------------|
| [TODO: Access control] | Preventive | Quarterly | [TODO: Vendor] | [TODO: Date] | [TODO: Date] |
| [TODO: Surveillance] | Preventive | Semi-annual | [TODO: Vendor] | [TODO: Date] | [TODO: Date] |
| [TODO: Fire suppression] | Inspection | Annual | [TODO: Vendor] | [TODO: Date] | [TODO: Date] |

### 6.2 Maintenance Documentation

**Required Documentation:**
- Maintenance work orders
- Service reports
- Parts replaced
- System tests performed
- Technician credentials
- Access logs for maintenance personnel

**Retention:** [TODO: 6 years]

### 6.3 Maintenance Access Control

**Vendor Access:**
- Vendor escorted during maintenance
- Vendor access logged
- Vendor credentials verified
- Background checks for regular vendors
- Business Associate Agreement (if PHI access possible)

## 7. Physical Security Incidents

### 7.1 Incident Types

- Unauthorized facility access
- Tailgating
- Lost/stolen access cards or keys
- Forced entry
- Surveillance system tampering
- Alarm system failures

### 7.2 Incident Response

**Response Process:**
1. **Detection:** Incident detected (alarm, observation, report)
2. **Notification:** Security Officer notified immediately
3. **Assessment:** Assess severity and impact
4. **Containment:** Secure area, change access codes if needed
5. **Investigation:** Review logs, surveillance footage
6. **Remediation:** Implement corrective actions
7. **Documentation:** Document incident and response
8. **Review:** Post-incident review and lessons learned

### 7.3 Incident Log

| Incident ID | Date | Type | Location | Description | Response | Status |
|-------------|------|------|----------|-------------|----------|--------|
| [TODO: INC-001] | [TODO: Date] | [TODO: Type] | [TODO: Location] | [TODO: Description] | [TODO: Actions taken] | [TODO: Closed] |

## 8. Documentation and Records

### 8.1 Required Documentation

- Facility security plan
- Access authorization records
- Visitor logs
- Access review records
- Maintenance records
- Incident reports
- Surveillance footage (per retention policy)

### 8.2 Retention

**Retention Period:** [TODO: 6 years from creation or last effective date]

**Storage Location:** [TODO: Document management system location]

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial creation |

<!-- End of template -->
