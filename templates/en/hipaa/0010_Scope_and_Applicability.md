# Scope and Applicability

**Document-ID:** [FRAMEWORK]-0010
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
This template defines the scope of HIPAA compliance for the organization.
It aligns with HIPAA Security Rule §164.306 and Privacy Rule §164.500.

Customization required:
- Define whether organization is a Covered Entity or Business Associate
- Identify all systems that store, process, or transmit PHI
- Document organizational structure and healthcare components
- List all locations where PHI is present
-->

## 1. Purpose

This document defines the scope of HIPAA compliance for {{ meta-organisation.name }} and establishes the applicability of HIPAA Security Rule, Privacy Rule, and Breach Notification Rule requirements.

### 1.1 Objectives

- **Scope Definition:** Clear identification of HIPAA-regulated activities and systems
- **Compliance Framework:** Establish foundation for HIPAA compliance program
- **Role Clarification:** Define organization's role as Covered Entity or Business Associate
- **PHI Identification:** Document all Protected Health Information within scope

### 1.2 References

- **HIPAA Security Rule**: 45 CFR §§ 164.302-164.318
- **HIPAA Privacy Rule**: 45 CFR §§ 164.500-164.534
- **Breach Notification Rule**: 45 CFR §§ 164.400-164.414
- **HITECH Act**: Health Information Technology for Economic and Clinical Health Act
- **Omnibus Rule**: Final modifications to HIPAA (2013)

## 2. Organization Information

### 2.1 Organization Details

**Organization Name:** {{ meta-organisation.name }}  
**Address:** {{ meta-organisation.address }}, [TODO] [TODO]  
**State:** [TODO]  
**Country:** [TODO]  
**Website:** [TODO]  
**Tax ID (EIN):** [TODO]  

### 2.2 Organization Type

**Primary Classification:** [TODO: Select one]
- [ ] Covered Entity - Healthcare Provider
- [ ] Covered Entity - Health Plan
- [ ] Covered Entity - Healthcare Clearinghouse
- [ ] Business Associate
- [ ] Hybrid Entity (both covered and non-covered functions)

**If Healthcare Provider:**
- **Provider Type:** [TODO: Hospital, Clinic, Physician Practice, etc.]
- **NPI (National Provider Identifier):** [TODO: 10-digit NPI]
- **Specialties:** [TODO: List medical specialties]
- **Electronic Transactions:** [TODO: Yes/No - Do you transmit health information electronically?]

**If Health Plan:**
- **Plan Type:** [TODO: Group health plan, Health insurance issuer, HMO, Medicare, Medicaid, etc.]
- **Number of Participants:** [TODO: Number]
- **Small Health Plan:** [TODO: Yes/No - Fewer than 50 participants]

**If Healthcare Clearinghouse:**
- **Services Provided:** [TODO: Claims processing, billing services, etc.]
- **Covered Entities Served:** [TODO: Number and types]

**If Business Associate:**
- **Services Provided:** [TODO: IT services, billing, legal, consulting, etc.]
- **Covered Entity Clients:** [TODO: Number]
- **Subcontractors:** [TODO: Yes/No]

### 2.3 Hybrid Entity Designation

**Is this a Hybrid Entity?** [TODO: Yes/No]

If yes, complete the following:

**Healthcare Components (Covered Functions):**
| Component | Function | Location | PHI Access |
|-----------|----------|----------|------------|
| [TODO: Department] | [TODO: Function] | [TODO: Location] | [TODO: Yes/No] |

**Non-Healthcare Components (Non-Covered Functions):**
| Component | Function | Location | PHI Access |
|-----------|----------|----------|------------|
| [TODO: Department] | [TODO: Function] | [TODO: Location] | [TODO: No] |

**Designation Documentation:** [TODO: Reference to formal hybrid entity designation]

## 3. Protected Health Information (PHI)

### 3.1 PHI Definition

Protected Health Information (PHI) includes individually identifiable health information that is:
1. Created or received by a healthcare provider, health plan, employer, or healthcare clearinghouse
2. Relates to past, present, or future physical or mental health, provision of healthcare, or payment for healthcare
3. Identifies the individual or could be used to identify the individual

### 3.2 PHI Elements

**Demographic Identifiers (18 HIPAA Identifiers):**
1. Names
2. Geographic subdivisions smaller than state (street address, city, county, ZIP code)
3. Dates (birth, admission, discharge, death) - except year
4. Telephone numbers
5. Fax numbers
6. Email addresses
7. Social Security numbers
8. Medical record numbers
9. Health plan beneficiary numbers
10. Account numbers
11. Certificate/license numbers
12. Vehicle identifiers and serial numbers
13. Device identifiers and serial numbers
14. Web URLs
15. IP addresses
16. Biometric identifiers (fingerprints, voiceprints)
17. Full-face photographs
18. Any other unique identifying number, characteristic, or code

**Health Information:**
- Medical history and diagnoses
- Treatment and procedure information
- Medication records
- Laboratory and test results
- Insurance and billing information
- Clinical notes and assessments

### 3.3 PHI in Organization

**Types of PHI Maintained:** [TODO: Check all that apply]
- [ ] Electronic PHI (ePHI) - stored electronically
- [ ] Paper PHI - physical records
- [ ] Oral PHI - verbal communications

**PHI Data Elements Collected:**
| Data Element | Format | Storage Location | Retention Period |
|--------------|--------|------------------|------------------|
| [TODO: Patient demographics] | Electronic | [TODO: EHR system] | [TODO: Years] |
| [TODO: Medical records] | Electronic/Paper | [TODO: Location] | [TODO: Years] |
| [TODO: Billing information] | Electronic | [TODO: System] | [TODO: Years] |
| [TODO: Lab results] | Electronic | [TODO: System] | [TODO: Years] |

## 4. Systems and Applications

### 4.1 Systems Containing PHI

| System ID | System Name | Type | PHI Elements | Location | Vendor |
|-----------|-------------|------|--------------|----------|--------|
| [TODO: SYS-001] | [TODO: EHR System] | Application | All PHI | [TODO: On-premise/Cloud] | [TODO: Vendor] |
| [TODO: SYS-002] | [TODO: Practice Management] | Application | Demographics, Billing | [TODO: Location] | [TODO: Vendor] |
| [TODO: SYS-003] | [TODO: Lab System] | Application | Lab results | [TODO: Location] | [TODO: Vendor] |
| [TODO: SYS-004] | [TODO: Imaging System] | Application | Radiology images | [TODO: Location] | [TODO: Vendor] |
| [TODO: SYS-005] | [TODO: Email System] | Infrastructure | PHI in transit | [TODO: Location] | [TODO: Vendor] |

### 4.2 Infrastructure Components

| Component | Type | Function | PHI Access | Location |
|-----------|------|----------|------------|----------|
| [TODO: DB-001] | Database Server | PHI storage | Yes | [TODO: Data center] |
| [TODO: APP-001] | Application Server | PHI processing | Yes | [TODO: Data center] |
| [TODO: WEB-001] | Web Server | Patient portal | Yes | [TODO: Cloud] |
| [TODO: FILE-001] | File Server | Document storage | Yes | [TODO: On-premise] |
| [TODO: BACKUP-001] | Backup System | PHI backup | Yes | [TODO: Location] |

### 4.3 Network Architecture

**Network Segments with PHI:**
- **Clinical Network:** [TODO: Description]
- **Administrative Network:** [TODO: Description]
- **DMZ:** [TODO: Description]
- **Wireless Networks:** [TODO: Description]

**Network Diagram:** [TODO: Reference to network diagram in diagrams/ folder]

## 5. Physical Locations

### 5.1 Facilities with PHI

| Location ID | Facility Name | Address | Type | PHI Present | Staff Count |
|-------------|---------------|---------|------|-------------|-------------|
| [TODO: LOC-001] | Main Clinic | [TODO: Address] | Clinical | Yes | [TODO: Number] |
| [TODO: LOC-002] | Administrative Office | [TODO: Address] | Administrative | Yes | [TODO: Number] |
| [TODO: LOC-003] | Data Center | [TODO: Address] | IT Infrastructure | Yes | [TODO: Number] |
| [TODO: LOC-004] | Satellite Clinic | [TODO: Address] | Clinical | Yes | [TODO: Number] |

### 5.2 Remote Access

**Remote Access to PHI Allowed:** [TODO: Yes/No]

If yes:
- **Access Method:** [TODO: VPN, Remote Desktop, Web Portal]
- **Authentication:** [TODO: Username/Password, MFA, Smart Card]
- **Authorized Users:** [TODO: Roles/Number]
- **Devices:** [TODO: Company-owned, BYOD, Both]
- **Mobile Device Management:** [TODO: Yes/No, Solution name]

## 6. Workforce

### 6.1 Workforce with PHI Access

| Role/Department | Number of Staff | PHI Access Level | Access Justification |
|-----------------|-----------------|------------------|----------------------|
| [TODO: Physicians] | [TODO: Number] | Full | Direct patient care |
| [TODO: Nurses] | [TODO: Number] | Full | Direct patient care |
| [TODO: Medical Assistants] | [TODO: Number] | Limited | Patient intake |
| [TODO: Billing Staff] | [TODO: Number] | Billing data only | Claims processing |
| [TODO: IT Staff] | [TODO: Number] | System admin | System maintenance |
| [TODO: Reception] | [TODO: Number] | Demographics only | Scheduling |

### 6.2 Workforce Training

**HIPAA Training Required:** Yes (Annual)  
**Training Topics:**
- HIPAA Privacy Rule
- HIPAA Security Rule
- Breach Notification requirements
- Organization policies and procedures
- Sanctions for violations

**Training Records Retention:** [TODO: Years]

## 7. Business Associates

### 7.1 Business Associate Relationships

| Business Associate | Service Provided | PHI Access | BAA Signed | BAA Date |
|--------------------|------------------|------------|------------|----------|
| [TODO: IT Vendor] | IT support | Yes | [TODO: Yes/No] | [TODO: Date] |
| [TODO: Billing Service] | Medical billing | Yes | [TODO: Yes/No] | [TODO: Date] |
| [TODO: Cloud Provider] | Data hosting | Yes | [TODO: Yes/No] | [TODO: Date] |
| [TODO: Shredding Service] | Document destruction | Yes | [TODO: Yes/No] | [TODO: Date] |
| [TODO: Legal Counsel] | Legal services | Yes | [TODO: Yes/No] | [TODO: Date] |

### 7.2 Subcontractor Relationships

**Do Business Associates use Subcontractors?** [TODO: Yes/No]

If yes:
| Subcontractor | Service | Primary BA | BAA in Place |
|---------------|---------|------------|--------------|
| [TODO: Name] | [TODO: Service] | [TODO: BA Name] | [TODO: Yes/No] |

## 8. Compliance Scope

### 8.1 Applicable HIPAA Rules

**Security Rule (45 CFR Part 164, Subpart C):** [TODO: Applicable/Not Applicable]
- Administrative Safeguards (§164.308)
- Physical Safeguards (§164.310)
- Technical Safeguards (§164.312)
- Organizational Requirements (§164.314)
- Policies and Procedures (§164.316)

**Privacy Rule (45 CFR Part 164, Subpart E):** [TODO: Applicable/Not Applicable]
- Uses and Disclosures (§164.502-§164.514)
- Individual Rights (§164.520-§164.528)
- Administrative Requirements (§164.530-§164.534)

**Breach Notification Rule (45 CFR Part 164, Subpart D):** [TODO: Applicable/Not Applicable]
- Breach Discovery and Notification (§164.404-§164.410)
- Notification by Business Associates (§164.410)

### 8.2 Exclusions from Scope

**Systems/Processes NOT in Scope:**
| System/Process | Reason for Exclusion |
|----------------|----------------------|
| [TODO: HR System] | No PHI - employee data only |
| [TODO: Marketing Database] | De-identified data only |
| [TODO: Public Website] | No PHI collected |

## 9. Compliance Responsibilities

### 9.1 Key Roles

**Privacy Officer:**
- **Name:** [TODO]
- **Email:** [TODO]
- **Phone:** [TODO]

**Security Officer:**
- **Name:** [TODO]
- **Email:** [TODO]
- **Phone:** [TODO]

**HIPAA Compliance Officer:**
- **Name:** [TODO: Name]
- **Email:** [TODO: Email]
- **Phone:** [TODO: Phone]

**Contact Person (for individuals exercising rights):**
- **Name:** [TODO: Name]
- **Email:** [TODO: Email]
- **Phone:** [TODO: Phone]
- **Address:** [TODO: Mailing address]

### 9.2 Governance Structure

**HIPAA Compliance Committee:**
- **Chair:** [TODO: Name, Title]
- **Members:** [TODO: List members and titles]
- **Meeting Frequency:** [TODO: Monthly/Quarterly]
- **Responsibilities:** Oversight of HIPAA compliance program

## 10. Scope Changes

### 10.1 Change Management Process

**Triggers for Scope Review:**
1. New systems or applications that handle PHI
2. New business associate relationships
3. New physical locations
4. Changes in services provided
5. Organizational restructuring
6. Regulatory changes

**Review Process:**
1. Identify change
2. Assess HIPAA applicability
3. Update scope documentation
4. Implement required safeguards
5. Update policies and procedures
6. Train affected workforce
7. Document changes

### 10.2 Scope Review Schedule

**Annual Review:** [TODO: Month]  
**Last Review Date:** [TODO: Date]  
**Next Review Date:** [TODO: Date]  
**Reviewed by:** [TODO: Name, Title]

### 10.3 Change History

| Date | Change Description | Impact | Approved By |
|------|-------------------|--------|-------------|
| [TODO: Date] | Initial scope definition | N/A | [TODO: Name] |
| [TODO: Date] | Added new EHR system | Expanded ePHI scope | [TODO: Name] |

<!-- End of template -->
