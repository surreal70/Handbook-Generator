# Policy: Physical Security

**Document-ID:** [FRAMEWORK]-0480
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
This policy establishes the principles for physical security of facilities,
equipment, and information. It ensures that physical access to sensitive areas
and assets is controlled and monitored. Customize based on your organization's
facility types and security requirements.

ISO 27001:2022 Annex A Reference: A.7.1, A.7.2, A.7.3, A.7.4
-->

**Document ID:** 0480  
**Document Type:** Policy (abstract)  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.7.1-A.7.4 (incl. Amendment 1:2024)  
**Owner:** {{ meta.ciso.name }}  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** {{ meta-handbook.modifydate }}  
**Next Review:** {{ meta-handbook.next_review }}

## 1. Purpose

This policy defines the principles for physical security at **{{ meta-organisation.name }}**. It ensures that physical access to facilities, equipment, and information is controlled and monitored to prevent unauthorized access, theft, and damage.

## 2. Scope

This policy applies to:

- **Organizational Units:** All departments and locations of {{ meta-organisation.name }}
- **Facilities:** Offices, data centers, server rooms, warehouses, production facilities
- **Assets:** IT equipment, servers, network components, mobile devices, documents
- **Persons:** Employees, visitors, contractors, suppliers
- **Locations:** {{ netbox.site.name }} and all other operational sites

**Exceptions:** Exceptions are only permitted through the defined exception process (`0640_Policy_Exceptions_and_Risk_Waivers.md`).

## 3. Principles (Policy Statements)

### 3.1 Perimeter Security
Physical security areas are protected by perimeter security (fences, walls, security doors). Entry points are controlled and monitored.

### 3.2 Access Control
Access to sensitive areas is controlled:
- Electronic access control systems (badge, biometrics)
- Visitor management and escort requirements
- Logging of all access
- Regular review of access rights

### 3.3 Security Zones
Facilities are divided into security zones:
- **Public:** Reception, meeting rooms
- **Internal:** Offices, workspaces
- **Restricted:** Server rooms, data centers
- **High Security:** Critical infrastructure, vault rooms

### 3.4 Video Surveillance
Critical areas are video monitored. Recordings are stored and protected according to data protection requirements.

### 3.5 Protection Against Environmental Hazards
IT equipment is protected against environmental hazards:
- Fire protection (smoke detectors, extinguishing systems)
- Air conditioning and temperature monitoring
- Water protection (leak detection)
- Power supply (UPS, emergency generators)

### 3.6 Secure Disposal
Physical media and documents are securely disposed of (shredding, incineration, certified disposal).

### 3.7 Clear Desk and Clear Screen
Workspaces are cleared when absent (Clear Desk). Screens are locked (Clear Screen).

### 3.8 Equipment Security
IT equipment is protected against theft (Kensington locks, alarm systems, inventory management).

## 4. Roles and Responsibilities

### RACI Matrix: Physical Security

| Activity | CISO | Facility Management | Security | IT Operations | HR |
|----------|------|---------------------|----------|---------------|-----|
| Policy Creation | R/A | C | C | C | I |
| Access Control | C | R/A | R | I | C |
| Visitor Management | I | R/A | R | I | C |
| Video Surveillance | C | R/A | R | I | C |
| Environmental Protection | C | R/A | I | C | I |
| Equipment Security | C | C | I | R/A | I |
| Compliance Review | R/A | C | C | I | I |

**Legend:** R = Responsible (Execution), A = Accountable (Ownership), C = Consulted, I = Informed

### Key Roles

- **Policy Owner:** {{ meta.ciso.name }} (CISO)
- **Facility Manager:** {{ meta.facility.manager }}
- **Security Manager:** {{ meta.security.physical_security_manager }}
- **Implementation Responsible:** Facility Management, Security, IT Operations
- **Control/Audit Function:** ISMS, Internal Audit

## 5. Derivatives (Guidelines/Standards/Processes)

Implementation details are defined in subordinate documents:

### Associated Guidelines
- **0490_Guideline_Access_Visitors_and_Equipment_Protection.md** - Detailed implementation guideline
- `0300_Policy_Asset_Management.md` - Asset Management Policy
- `0560_Policy_Data_Protection_Interfaces.md` - Data Protection Policy (video surveillance)

### Associated Standards/Baselines
- Security zones concept
- Access control matrix
- Visitor management process
- Video surveillance guideline

### Associated Processes
- Access control process
- Visitor management process
- Incident response for physical security incidents
- Equipment disposal process

## 6. Compliance, Monitoring and Enforcement

### Metrics and KPIs
- Number of unauthorized access attempts
- Number of visitors and compliance with escort requirements
- Number of physical security incidents (theft, break-in)
- Access control system availability (Target: 99.9%)
- Clear Desk/Clear Screen compliance rate
- Number of lost or stolen assets

### Evidence and Proof
- Access control logs
- Visitor logs
- Video surveillance recordings
- Security incident reports
- Facility audit reports
- Equipment inventory

### Consequences of Violations
Violations of this policy are handled according to applicable HR and compliance processes:
- **Unauthorized Access:** Immediate escalation, investigation
- **Tailgating:** Warning, retraining
- **Clear Desk/Screen Violations:** Warning, retraining
- **Repeated Violations:** Employment consequences

## 7. Exceptions

Exceptions to this policy are only permitted in justified exceptional cases:

- **Exception Process:** See `0640_Policy_Exceptions_and_Risk_Waivers.md`
- **Approval:** Exceptions must be approved by CISO and Facility Manager
- **Documentation:** All exceptions are documented in the risk register
- **Time Limitation:** Exceptions are generally time-limited

## 8. References

### Internal Documents
- `0010_ISMS_Information_Security_Policy.md` - ISMS Policy
- `0490_Guideline_Access_Visitors_and_Equipment_Protection.md` - Detailed Guideline
- `0300_Policy_Asset_Management.md` - Asset Management Policy
- `0080_ISMS_Risk_Register_Template.md` - Risk Register

### External Standards and Requirements
- **ISO/IEC 27001:2022 Annex A.7.1** - Physical security perimeters
- **ISO/IEC 27001:2022 Annex A.7.2** - Physical entry
- **ISO/IEC 27001:2022 Annex A.7.3** - Securing offices, rooms and facilities
- **ISO/IEC 27001:2022 Annex A.7.4** - Physical security monitoring
- **GDPR (EU 2016/679)** - Data protection for video surveillance
- **BSI IT-Grundschutz** - Module INF.1 General Building

**Approved by:**  
{{ meta.management.ceo }}, Management  
Date: {{ meta-handbook.modifydate }}

**Next Review:** {{ meta-handbook.next_review }} (annually or as needed)

