# Covered Entities and Healthcare Components

**Document-ID:** [FRAMEWORK]-0020
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

This document defines AdminSend GmbH's status as a HIPAA Covered Entity and documents all healthcare components and covered functions.

### 1.1 Objectives

- **Entity Classification:** Clearly define organization's HIPAA status
- **Component Identification:** Document all healthcare components (if hybrid entity)
- **Function Documentation:** List all covered functions and activities
- **Compliance Boundaries:** Establish clear boundaries for HIPAA compliance

## 2. Covered Entity Determination

### 2.1 Covered Entity Definition

Under HIPAA, a Covered Entity is:
1. **Healthcare Provider** that conducts certain transactions electronically
2. **Health Plan** that provides or pays for medical care
3. **Healthcare Clearinghouse** that processes health information

### 2.2 Organization Classification

**AdminSend GmbH is a:** [TODO: Select one]

- [ ] **Healthcare Provider** (45 CFR §160.103)
- [ ] **Health Plan** (45 CFR §160.103)
- [ ] **Healthcare Clearinghouse** (45 CFR §160.103)
- [ ] **Hybrid Entity** (45 CFR §164.105(a))

**Classification Justification:** [TODO: Explain why organization meets covered entity definition]

## 3. Healthcare Provider Details

**Complete this section if organization is a Healthcare Provider**

### 3.1 Provider Information

**Provider Type:** [TODO: Select applicable]
- [ ] Hospital
- [ ] Physician Practice
- [ ] Clinic
- [ ] Nursing Home
- [ ] Pharmacy
- [ ] Laboratory
- [ ] Ambulance Service
- [ ] Other: [TODO: Specify]

**National Provider Identifier (NPI):**
- **NPI Number:** [TODO: 10-digit NPI]
- **NPI Type:** [TODO: Type 1 (Individual) or Type 2 (Organization)]
- **Enumeration Date:** [TODO: Date]

**Medical Specialties:**
| Specialty | Taxonomy Code | Providers |
|-----------|---------------|-----------|
| [TODO: Primary Care] | [TODO: Code] | [TODO: Number] |
| [TODO: Specialty 1] | [TODO: Code] | [TODO: Number] |
| [TODO: Specialty 2] | [TODO: Code] | [TODO: Number] |

### 3.2 Electronic Transactions

**Does the organization transmit health information electronically in connection with a HIPAA standard transaction?** [TODO: Yes/No]

**HIPAA Standard Transactions Conducted:**
- [ ] Healthcare claims or equivalent encounter information (837)
- [ ] Eligibility for a health plan (270/271)
- [ ] Referral certification and authorization (278)
- [ ] Healthcare claim status (276/277)
- [ ] Enrollment and disenrollment in a health plan (834)
- [ ] Healthcare payment and remittance advice (835)
- [ ] Health plan premium payments (820)
- [ ] Coordination of benefits (837)

**Transaction Volume (Annual):**
| Transaction Type | Volume | Primary Trading Partner |
|------------------|--------|-------------------------|
| [TODO: Claims] | [TODO: Number] | [TODO: Payer name] |
| [TODO: Eligibility] | [TODO: Number] | [TODO: Payer name] |

### 3.3 Healthcare Services Provided

**Services Offered:**
| Service | Description | Location | PHI Generated |
|---------|-------------|----------|---------------|
| [TODO: Primary Care] | [TODO: Description] | [TODO: Location] | Yes |
| [TODO: Diagnostic Services] | [TODO: Description] | [TODO: Location] | Yes |
| [TODO: Treatment Services] | [TODO: Description] | [TODO: Location] | Yes |

## 4. Health Plan Details

**Complete this section if organization is a Health Plan**

### 4.1 Health Plan Information

**Plan Type:** [TODO: Select applicable]
- [ ] Group Health Plan
- [ ] Health Insurance Issuer
- [ ] HMO (Health Maintenance Organization)
- [ ] Medicare
- [ ] Medicaid
- [ ] Medicare Advantage
- [ ] Medicare Part D
- [ ] TRICARE
- [ ] Other: [TODO: Specify]

**Plan Characteristics:**
- **Number of Participants:** [TODO: Number]
- **Small Health Plan:** [TODO: Yes/No - Fewer than 50 participants]
- **Self-Insured:** [TODO: Yes/No]
- **Fully Insured:** [TODO: Yes/No]

**Plan Sponsor Information:**
- **Sponsor Name:** [TODO: Name]
- **Sponsor Type:** [TODO: Employer, Union, etc.]
- **Relationship to Plan:** [TODO: Description]

### 4.2 Health Plan Functions

**Functions Performed:**
- [ ] Claims adjudication
- [ ] Eligibility determination
- [ ] Enrollment and disenrollment
- [ ] Premium collection
- [ ] Provider network management
- [ ] Utilization review
- [ ] Case management
- [ ] Disease management

**PHI Used for:**
- [ ] Payment
- [ ] Healthcare operations
- [ ] Treatment coordination
- [ ] Quality improvement
- [ ] Fraud detection

## 5. Healthcare Clearinghouse Details

**Complete this section if organization is a Healthcare Clearinghouse**

### 5.1 Clearinghouse Information

**Services Provided:**
- [ ] Claims processing
- [ ] Claims scrubbing
- [ ] Format conversion
- [ ] Transaction routing
- [ ] Eligibility verification
- [ ] Other: [TODO: Specify]

**Covered Entities Served:**
- **Number of Providers:** [TODO: Number]
- **Number of Payers:** [TODO: Number]
- **Transaction Volume (Monthly):** [TODO: Number]

**Standard Formats Supported:**
| Transaction | Format | Version |
|-------------|--------|---------|
| [TODO: Claims] | X12 837 | [TODO: 5010] |
| [TODO: Eligibility] | X12 270/271 | [TODO: 5010] |

## 6. Hybrid Entity Designation

**Complete this section if organization is a Hybrid Entity**

### 6.1 Hybrid Entity Definition

A Hybrid Entity is an organization that:
1. Performs both covered and non-covered functions
2. Has formally designated its healthcare components
3. Applies HIPAA only to designated healthcare components

**Is AdminSend GmbH a Hybrid Entity?** [TODO: Yes/No]

### 6.2 Healthcare Components

**Designated Healthcare Components:**

| Component ID | Component Name | Function | Location | Staff Count |
|--------------|----------------|----------|----------|-------------|
| [TODO: HC-001] | [TODO: Medical Clinic] | Healthcare Provider | [TODO: Building A] | [TODO: 25] |
| [TODO: HC-002] | [TODO: Employee Health Plan] | Health Plan | [TODO: HR Dept] | [TODO: 5] |
| [TODO: HC-003] | [TODO: Occupational Health] | Healthcare Provider | [TODO: Building B] | [TODO: 10] |

**Healthcare Component Functions:**
| Component | Covered Functions | PHI Created/Maintained |
|-----------|-------------------|------------------------|
| [TODO: Medical Clinic] | Patient care, billing | Patient records, billing data |
| [TODO: Employee Health Plan] | Claims processing | Claims, enrollment data |

### 6.3 Non-Healthcare Components

**Non-Covered Components:**

| Component ID | Component Name | Function | PHI Access |
|--------------|----------------|----------|------------|
| [TODO: NC-001] | [TODO: Manufacturing] | Product manufacturing | No |
| [TODO: NC-002] | [TODO: Sales] | Product sales | No |
| [TODO: NC-003] | [TODO: Corporate IT] | IT support (non-healthcare) | No |

**Justification for Non-Covered Status:** [TODO: Explain why these components are not covered functions]

### 6.4 Hybrid Entity Documentation

**Formal Designation Document:**
- **Document Title:** [TODO: "Hybrid Entity Designation"]
- **Date of Designation:** [TODO: Date]
- **Approved by:** [TODO: Board of Directors, CEO, etc.]
- **Document Location:** [TODO: File path or reference]

**Designation Criteria:**
- Clear separation of covered and non-covered functions
- Separate management and operations
- Distinct workforce assignments
- Separate physical locations (if applicable)

### 6.5 Workforce Assignment

**Healthcare Component Workforce:**
| Employee ID | Name | Role | Component | PHI Access |
|-------------|------|------|-----------|------------|
| [TODO: EMP-001] | [TODO: Name] | [TODO: Physician] | HC-001 | Full |
| [TODO: EMP-002] | [TODO: Name] | [TODO: Nurse] | HC-001 | Full |
| [TODO: EMP-003] | [TODO: Name] | [TODO: Claims Processor] | HC-002 | Limited |

**Shared Workforce:**
| Employee ID | Name | Role | Access to Healthcare Components |
|-------------|------|------|--------------------------------|
| [TODO: EMP-100] | [TODO: Name] | [TODO: IT Support] | HC-001, HC-002 (system admin only) |
| [TODO: EMP-101] | [TODO: Name] | [TODO: Legal] | All components (as needed) |

**Workforce Training:**
- Healthcare component workforce: Full HIPAA training
- Shared workforce: HIPAA training for healthcare component access
- Non-healthcare workforce: No HIPAA training required (unless accessing PHI)

## 7. Covered Functions

### 7.1 Healthcare Operations

**Healthcare Operations Performed:**
- [ ] Quality assessment and improvement
- [ ] Case management and care coordination
- [ ] Reviewing competence of healthcare professionals
- [ ] Underwriting and premium rating (health plans)
- [ ] Medical review and utilization review
- [ ] Fraud and abuse detection
- [ ] Business planning and development
- [ ] Business management and general administrative activities

**PHI Used for Healthcare Operations:**
| Operation | PHI Elements Used | Frequency | Responsible Department |
|-----------|-------------------|-----------|------------------------|
| [TODO: Quality improvement] | [TODO: Clinical data] | [TODO: Quarterly] | [TODO: Quality Dept] |
| [TODO: Utilization review] | [TODO: Claims data] | [TODO: Ongoing] | [TODO: UM Dept] |

### 7.2 Treatment Activities

**Treatment Functions:**
- [ ] Provision of healthcare services
- [ ] Coordination of care
- [ ] Referral of patients
- [ ] Consultation between providers
- [ ] Case management

**Treatment Locations:**
| Location | Services | Providers | Patient Volume |
|----------|----------|-----------|----------------|
| [TODO: Main Clinic] | [TODO: Primary care] | [TODO: 5 physicians] | [TODO: 100/day] |
| [TODO: Satellite Office] | [TODO: Specialty care] | [TODO: 2 specialists] | [TODO: 30/day] |

### 7.3 Payment Activities

**Payment Functions:**
- [ ] Billing and claims management
- [ ] Claims adjudication
- [ ] Payment collection
- [ ] Reimbursement
- [ ] Utilization review for payment
- [ ] Pre-authorization

**Payment Systems:**
| System | Function | PHI Processed | Volume |
|--------|----------|---------------|--------|
| [TODO: Billing System] | Claims generation | Billing data | [TODO: 500/day] |
| [TODO: Payment Portal] | Patient payments | Demographics, account | [TODO: 100/day] |

## 8. Compliance Implications

### 8.1 HIPAA Rules Applicability

**For Covered Entity:**
- **Privacy Rule:** Applies to all PHI
- **Security Rule:** Applies to all ePHI
- **Breach Notification Rule:** Applies to all unsecured PHI

**For Hybrid Entity:**
- **Privacy Rule:** Applies only to healthcare components
- **Security Rule:** Applies only to healthcare components
- **Breach Notification Rule:** Applies only to healthcare components
- **Note:** Shared workforce and infrastructure must comply when accessing healthcare component PHI

### 8.2 Documentation Requirements

**Required Documentation:**
- [ ] Covered entity determination
- [ ] Hybrid entity designation (if applicable)
- [ ] Healthcare component definitions
- [ ] Workforce assignments
- [ ] Business associate agreements
- [ ] Policies and procedures
- [ ] Training records

**Documentation Retention:** [TODO: 6 years from creation or last effective date]


