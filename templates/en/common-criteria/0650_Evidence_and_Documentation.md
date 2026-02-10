# Evidence and Documentation

**Document-ID:** 0650  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Update:** {{ meta.date }}  

---

> **Note:** This document is a template. Replace all `[TODO]` placeholders and HTML comments with project-specific information.

<!-- 
GUIDANCE FOR TEMPLATE AUTHORS:
This template documents all evidence and documentation required for the Common Criteria evaluation.

Important aspects:
- List all required evaluation evidence
- Document the status of each evidence item
- Reference the corresponding SARs
- Organize evidence by SAR families
- Ensure completeness and availability
- Document access restrictions
-->

## Overview

This chapter documents all evidence and documentation required for the Common Criteria evaluation of the TOE. The evidence is organized by SAR families and corresponds to the chosen Evaluation Assurance Level (EAL).

<!-- Describe the purpose and structure of the evidence documentation -->

**Chosen EAL:** [TODO: EAL1 / EAL2 / EAL3 / EAL4 / EAL5 / EAL6 / EAL7]

## Evidence Overview

<!-- Create an overview of all required evidence -->

### Evidence Matrix

| SAR Family | SAR Component | Required Evidence | Status | Availability |
|------------|---------------|-------------------|--------|--------------|
| ADV | ADV_ARC.1 | Security Architecture Description | [TODO: Status] | [TODO: Available/In Progress] |
| ADV | ADV_FSP.1 | Functional Specification | [TODO: Status] | [TODO] |
| AGD | AGD_OPE.1 | Operational User Guidance | [TODO: Status] | [TODO] |
| AGD | AGD_PRE.1 | Preparative Procedures | [TODO: Status] | [TODO] |
| ALC | ALC_CMC.1 | CM Capabilities | [TODO: Status] | [TODO] |
| ALC | ALC_CMS.1 | CM Scope | [TODO: Status] | [TODO] |
| ATE | ATE_IND.1 | Independent Testing | [TODO: Status] | [TODO] |
| AVA | AVA_VAN.1 | Vulnerability Analysis | [TODO: Status] | [TODO] |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

**Status Legend:**
- **Complete:** Evidence is complete and ready for evaluation
- **In Progress:** Evidence is being created
- **Planned:** Creation is planned
- **Not Required:** Not required for chosen EAL

## ADV: Development

<!-- Document all development evidence -->

### ADV_ARC: Security Architecture

#### ADV_ARC.1: Security Architecture Description

**Required Evidence:**
[TODO: Describe the required evidence according to ISO/IEC 15408-3]

**Documentation:**
- **Document Title:** [TODO: Title of architecture document]
- **Document Number:** [TODO: Number]
- **Version:** [TODO: Version]
- **Date:** [TODO: Date]
- **Location:** [TODO: Path or reference]
- **Classification:** [TODO: Classification]

**Content:**
- Description of TOE security architecture
- Identification of TSF subsystems
- Description of security domains
- Evidence of non-bypassability
- Evidence of domain separation

**Status:** [TODO: Complete / In Progress / Planned]

**Evaluation Notes:**
[TODO: Special notes for evaluators]

### ADV_FSP: Functional Specification

#### ADV_FSP.1: Basic Functional Specification

**Required Evidence:**
[TODO: Describe the required evidence]

**Documentation:**
- **Document Title:** [TODO: Title of functional specification]
- **Document Number:** [TODO: Number]
- **Version:** [TODO: Version]
- **Date:** [TODO: Date]
- **Location:** [TODO: Path]
- **Classification:** [TODO: Classification]

**Content:**
- Description of all external TSF interfaces
- Description of purposes and use of each interface
- Description of parameters for each interface
- Description of actions for each interface
- Mapping of SFRs to TSF interfaces

**Status:** [TODO: Complete / In Progress / Planned]

**Evaluation Notes:**
[TODO: Special notes]

### Additional ADV Components

<!-- Document additional ADV components based on chosen EAL -->

[TODO: Add additional ADV components if required (e.g., ADV_FSP.2, ADV_IMP.1, ADV_TDS.1)]

## AGD: Guidance Documents

<!-- Document all guidance documents -->

### AGD_OPE: Operational User Guidance

#### AGD_OPE.1: Operational User Guidance

**Required Evidence:**
[TODO: Describe the required evidence]

**Documentation:**
- **Document Title:** [TODO: User Manual]
- **Document Number:** [TODO: Number]
- **Version:** [TODO: Version]
- **Date:** [TODO: Date]
- **Location:** [TODO: Path]
- **Classification:** [TODO: Public / Confidential]

**Content:**
- Description of security functions
- Guidance for secure use
- Warnings about insecure states
- Description of user roles
- Guidance for managing security attributes

**Status:** [TODO: Complete / In Progress / Planned]

**Target Audience:** [TODO: End users / Administrators / Both]

### AGD_PRE: Preparative Procedures

#### AGD_PRE.1: Preparative Procedures

**Required Evidence:**
[TODO: Describe the required evidence]

**Documentation:**
- **Document Title:** [TODO: Installation and Configuration Manual]
- **Document Number:** [TODO: Number]
- **Version:** [TODO: Version]
- **Date:** [TODO: Date]
- **Location:** [TODO: Path]
- **Classification:** [TODO: Classification]

**Content:**
- Description of secure installation
- Description of secure configuration
- Description of security parameters
- Guidance for verifying secure configuration

**Status:** [TODO: Complete / In Progress / Planned]

**Target Audience:** [TODO: Administrators / Installers]

## ALC: Life-cycle Support

<!-- Document all life-cycle evidence -->

### ALC_CMC: CM Capabilities

#### ALC_CMC.1: Labelling of the TOE

**Required Evidence:**
[TODO: Describe the required evidence]

**Documentation:**
- **Document Title:** [TODO: Configuration Management Plan]
- **Document Number:** [TODO: Number]
- **Version:** [TODO: Version]
- **Date:** [TODO: Date]
- **Location:** [TODO: Path]
- **Classification:** [TODO: Classification]

**Content:**
- Description of CM system
- Unique identification of TOE
- Description of version control
- Description of change control

**Status:** [TODO: Complete / In Progress / Planned]

**TOE Identification:**
- **TOE Name:** [TODO: Name]
- **TOE Version:** [TODO: Version]
- **TOE Build:** [TODO: Build number]

### ALC_CMS: CM Scope

#### ALC_CMS.1: TOE CM Coverage

**Required Evidence:**
[TODO: Describe the required evidence]

**Documentation:**
- **Document Title:** [TODO: CM Scope Document]
- **Document Number:** [TODO: Number]
- **Version:** [TODO: Version]
- **Date:** [TODO: Date]
- **Location:** [TODO: Path]
- **Classification:** [TODO: Classification]

**Content:**
- List of all TOE components under CM control
- List of all evaluation evidence under CM control
- Description of CM procedures

**Status:** [TODO: Complete / In Progress / Planned]

**CM Items:**
[TODO: List all CM items]

### Additional ALC Components

<!-- Document additional ALC components -->

[TODO: Add additional ALC components if required (e.g., ALC_DEL.1, ALC_DVS.1, ALC_LCD.1)]

## ATE: Tests

<!-- Document all test evidence -->

### ATE_IND: Independent Testing

#### ATE_IND.1: Independent Testing - Conformance

**Required Evidence:**
[TODO: Describe the required evidence]

**Documentation:**
- **Document Title:** [TODO: Test Documentation]
- **Document Number:** [TODO: Number]
- **Version:** [TODO: Version]
- **Date:** [TODO: Date]
- **Location:** [TODO: Path]
- **Classification:** [TODO: Classification]

**Content:**
- TOE for independent testing
- Test environment
- Test documentation
- Test resources

**Status:** [TODO: Complete / In Progress / Planned]

**Test Environment:**
[TODO: Describe the test environment]

### Additional ATE Components

<!-- Document additional ATE components -->

[TODO: Add additional ATE components if required (e.g., ATE_COV.1, ATE_FUN.1)]

## AVA: Vulnerability Assessment

<!-- Document all vulnerability assessment evidence -->

### AVA_VAN: Vulnerability Analysis

#### AVA_VAN.1: Vulnerability Survey

**Required Evidence:**
[TODO: Describe the required evidence]

**Documentation:**
- **Document Title:** [TODO: Vulnerability Analysis Report]
- **Document Number:** [TODO: Number]
- **Version:** [TODO: Version]
- **Date:** [TODO: Date]
- **Location:** [TODO: Path]
- **Classification:** [TODO: Strictly Confidential]

**Content:**
- Analysis of publicly known vulnerabilities
- Assessment of applicability to TOE
- Evidence of resistance to vulnerabilities

**Status:** [TODO: Complete / In Progress / Planned]

**Vulnerability Sources:**
[TODO: List vulnerability databases used (e.g., CVE, NVD)]

### Additional AVA Components

<!-- Document additional AVA components -->

[TODO: Add additional AVA components if required (e.g., AVA_VAN.2, AVA_VAN.3)]

## Additional Evidence

<!-- Document additional evidence not directly mapped to SARs -->

### Security Target (ST)

**Documentation:**
- **Document Title:** Security Target for [TODO: TOE Name]
- **Document Number:** [TODO: Number]
- **Version:** [TODO: Version]
- **Date:** [TODO: Date]
- **Location:** [TODO: Path]
- **Classification:** [TODO: Classification]

**Status:** [TODO: Complete / In Progress]

### Evaluation Plan

**Documentation:**
- **Document Title:** [TODO: Evaluation Plan]
- **Document Number:** [TODO: Number]
- **Version:** [TODO: Version]
- **Date:** [TODO: Date]
- **Location:** [TODO: Path]
- **Classification:** [TODO: Classification]

**Status:** [TODO: Complete / In Progress / Planned]

### Additional Documents

[TODO: List additional relevant documents]

## Evidence Delivery

<!-- Document how evidence will be delivered -->

### Delivery Plan

| Evidence | Delivery Date | Recipient | Transmission Method |
|----------|---------------|-----------|---------------------|
| [TODO: Evidence 1] | [TODO: Date] | [TODO: Evaluation laboratory] | [TODO: Secure upload / Physical] |
| [TODO: Evidence 2] | [TODO: Date] | [TODO: Recipient] | [TODO: Method] |

### Access Control

<!-- Document access restrictions for evidence -->

| Evidence | Classification | Authorized Personnel | Access Method |
|----------|----------------|---------------------|---------------|
| [TODO: Evidence 1] | [TODO: Classification] | [TODO: Roles] | [TODO: Method] |
| [TODO: Evidence 2] | [TODO] | [TODO] | [TODO] |

## Evidence Validation

<!-- Document validation of evidence -->

### Completeness Check

**Check Date:** [TODO: Date]  
**Checked By:** [TODO: Name/Role]

**Result:**
- [ ] All required evidence is present
- [ ] All evidence is current
- [ ] All evidence is complete
- [ ] All evidence meets SAR requirements

**Identified Gaps:**
[TODO: List missing or incomplete evidence]

### Quality Check

**Check Date:** [TODO: Date]  
**Checked By:** [TODO: Name/Role]

**Criteria:**
- [ ] Evidence is clear and understandable
- [ ] Evidence is consistent with ST
- [ ] Evidence contains all required information
- [ ] Evidence is technically correct

**Identified Issues:**
[TODO: List quality issues]

## Evidence Archiving

<!-- Document archiving of evidence -->

### Archiving Plan

**Archive Location:** [TODO: Storage location]  
**Archive Duration:** [TODO: Duration]  
**Responsible:** [TODO: Role/Person]

**Archived Versions:**
| Evidence | Version | Archive Date | Location |
|----------|---------|--------------|----------|
| [TODO] | [TODO] | [TODO] | [TODO] |

### Recovery Procedures

[TODO: Describe the procedure for recovering archived evidence]

## Contact Information

<!-- Provide contact information for evidence questions -->

### Evidence Coordinator

**Name:** [TODO: Name]  
**Role:** [TODO: Role]  
**Email:** [TODO: Email]  
**Phone:** [TODO: Phone]

### Evaluation Laboratory Contact

**Name:** [TODO: Name]  
**Organization:** [TODO: Evaluation laboratory]  
**Email:** [TODO: Email]  
**Phone:** [TODO: Phone]

---

**Next Steps:**
1. Identify all required evidence based on chosen EAL
2. Create a timeline for evidence creation
3. Assign responsibilities for each evidence item
4. Create or collect all required evidence
5. Conduct completeness and quality checks
6. Deliver evidence to evaluation laboratory
7. Archive all evidence according to requirements
8. Update evidence documentation when changes occur
