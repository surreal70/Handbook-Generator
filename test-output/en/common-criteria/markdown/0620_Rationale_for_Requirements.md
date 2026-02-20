# Rationale for Security Requirements

**Document-ID:** 0620
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

> **Note:** This document is a template. Replace all `[TODO]` placeholders and HTML comments with project-specific information.



## Overview

This chapter provides the rationale demonstrating that the defined security requirements (Security Functional Requirements - SFRs and Security Assurance Requirements - SARs) completely and adequately fulfill the security objectives.



## Rationale Methodology



### Approach

[TODO: Describe the systematic approach to creating the rationale]

**Steps:**
1. Mapping of SFRs to TOE security objectives
2. Justification of completeness and adequacy
3. Justification of all SFR operations
4. Verification of SFR dependencies
5. Justification of SAR selection

### Completeness Criteria



[TODO: Define when the security requirements are considered complete]

**Criteria:**
- Each TOE security objective is fulfilled by at least one SFR
- All SFR dependencies are satisfied
- All SFR operations are justified
- SARs correspond to the chosen EAL

## Rationale for Security Functional Requirements (SFRs)



### Mapping: Security Objectives to SFRs



#### Security Objective O.1: [TODO: Objective Name]

**Objective Description:**
[TODO: Brief summary of the security objective from section 0300]

**Fulfilling SFRs:**

##### SFR 1: [TODO: SFR-Identifier] - [TODO: SFR-Name]

**SFR Description:**
[TODO: Brief description of the SFR from section 0400]

**Justification:**
[TODO: Explain in detail how this SFR fulfills the security objective]

**Adequacy:**
[TODO: Justify why this SFR is sufficient to achieve the objective]

**Operations:**


- **Selection:** [TODO: Describe selected options and justification]
- **Assignment:** [TODO: Describe assigned values and justification]
- **Refinement:** [TODO: Describe refinements and justification]
- **Iteration:** [TODO: Describe iterations and justification]

##### SFR 2: [TODO: SFR-Identifier] - [TODO: SFR-Name] (if applicable)

**SFR Description:**
[TODO: Brief description]

**Justification:**
[TODO: Detailed explanation]

**Adequacy:**
[TODO: Justification of adequacy]

**Operations:**
[TODO: Document all operations]

**Summary for O.1:**
[TODO: Summarize how the combination of SFRs completely fulfills the security objective]

#### Security Objective O.2: [TODO: Objective Name]

**Objective Description:**
[TODO: Brief summary]

**Fulfilling SFRs:**

##### SFR X: [TODO: SFR-Identifier] - [TODO: SFR-Name]

**SFR Description:**
[TODO: Brief description]

**Justification:**
[TODO: Detailed explanation]

**Adequacy:**
[TODO: Justification of adequacy]

**Operations:**
[TODO: Document all operations]

**Summary for O.2:**
[TODO: Summary of fulfillment]

### Additional Security Objectives



[TODO: Document the rationale for all additional security objectives]

## SFR Operations Rationale



### Selection



| SFR | Selection Options | Chosen Option | Justification |
|-----|-------------------|---------------|---------------|
| [TODO: SFR-ID] | [TODO: Option A, B, C] | [TODO: Option B] | [TODO: Why was this option chosen?] |
| [TODO] | [TODO] | [TODO] | [TODO] |

### Assignment



| SFR | Parameter | Assigned Value | Justification |
|-----|-----------|----------------|---------------|
| [TODO: SFR-ID] | [TODO: Parameter] | [TODO: Value] | [TODO: Why was this value assigned?] |
| [TODO] | [TODO] | [TODO] | [TODO] |

### Refinement



| SFR | Original Text | Refined Text | Justification |
|-----|---------------|--------------|---------------|
| [TODO: SFR-ID] | [TODO: Original] | [TODO: Refined] | [TODO: Why was it refined?] |
| [TODO] | [TODO] | [TODO] | [TODO] |

### Iteration



| SFR | Iteration | Purpose | Justification |
|-----|-----------|---------|---------------|
| [TODO: SFR-ID] | [TODO: Iteration 1] | [TODO: Purpose] | [TODO: Why was it iterated?] |
| [TODO] | [TODO] | [TODO] | [TODO] |

## SFR Dependencies Rationale



### Dependency Analysis



| SFR | Dependent SFR | Status | Justification |
|-----|---------------|--------|---------------|
| [TODO: SFR-ID] | [TODO: Dependent SFR] | Satisfied / Not Satisfied | [TODO: Explanation] |
| [TODO] | [TODO] | [TODO] | [TODO] |

**Legend:**
- **Satisfied:** The dependent SFR is included in the ST
- **Not Satisfied:** The dependent SFR is missing (justification required)

### Unsatisfied Dependencies



#### Dependency 1: [TODO: SFR-ID] → [TODO: Dependent SFR]

**Description:**
[TODO: Describe the dependency]

**Reason for Non-Satisfaction:**
[TODO: Explain why the dependency is not satisfied]

**Compensating Measures:**
[TODO: Describe alternative measures or justify why no compensation is required]

**Security Impact:**
[TODO: Assess the impact on security]

## Rationale for Security Assurance Requirements (SARs)



### EAL Selection Rationale

**Chosen EAL:** [TODO: EAL1 / EAL2 / EAL3 / EAL4 / EAL5 / EAL6 / EAL7]

**Justification:**
[TODO: Explain why this EAL was chosen]

**Factors:**
- **Threat Environment:** [TODO: Describe the threat environment]
- **Protection Needs:** [TODO: Describe the protection needs]
- **Cost-Benefit Ratio:** [TODO: Assess the ratio]
- **Market Requirements:** [TODO: Describe market requirements]

### SAR Components Rationale



#### SAR Family: [TODO: Family Name]

| SAR Component | EAL Standard | Augmented | Justification |
|---------------|--------------|-----------|---------------|
| [TODO: SAR-ID] | Yes / No | Yes / No | [TODO: Explanation] |
| [TODO] | [TODO] | [TODO] | [TODO] |

**Summary:**
[TODO: Summarize the SAR selection for this family]

### Augmented SARs



| SAR | Standard EAL | Chosen Level | Justification |
|-----|--------------|--------------|---------------|
| [TODO: SAR-ID] | [TODO: EAL] | [TODO: Higher Level] | [TODO: Why was it augmented?] |
| [TODO] | [TODO] | [TODO] | [TODO] |

### Reduced SARs



| SAR | Standard EAL | Chosen Level | Justification |
|-----|--------------|--------------|---------------|
| [TODO: SAR-ID] | [TODO: EAL] | [TODO: Lower Level] | [TODO: Why was it reduced?] |
| [TODO] | [TODO] | [TODO] | [TODO] |

## Completeness Analysis



### Coverage Matrix: Security Objectives to SFRs



| Security Objective | Fulfilling SFRs | Status |
|--------------------|-----------------|--------|
| O.1: [TODO] | [TODO: SFR-IDs] | Complete |
| O.2: [TODO] | [TODO: SFR-IDs] | Complete |
| O.3: [TODO] | [TODO: SFR-IDs] | Complete |

**Legend:**
- **Complete:** All aspects of the objective are fulfilled by SFRs
- **Partial:** Some aspects are fulfilled, additional SFRs required
- **Incomplete:** Objective is not sufficiently fulfilled by SFRs

### Identified Gaps



[TODO: List all security objectives that are not completely fulfilled by SFRs]

**Gap 1:** [TODO: Description]
- **Affected Security Objective:** [TODO]
- **Missing Coverage:** [TODO]
- **Planned Action:** [TODO: Additional SFR or justification why no action is required]

### Redundancy Analysis



[TODO: Analyze whether SFRs are redundant or overlap]

**Redundancy 1:** [TODO: Description]
- **Affected SFRs:** [TODO: SFR-IDs]
- **Overlap:** [TODO: Describe the overlap]
- **Justification:** [TODO: Explain why both SFRs are necessary, or suggest consolidation]

## Adequacy Analysis



### Assessment Criteria

[TODO: Define the criteria for adequacy of security requirements]

**Criteria:**
- SFRs are technically implementable
- SFRs are measurable and testable
- SFRs are proportional to the risk
- SARs are appropriate for the assurance level

### Adequacy Assessment



| SFR | Fulfilled Objectives | Adequacy | Justification |
|-----|---------------------|----------|---------------|
| [TODO: SFR-ID] | [TODO: Objectives] | Adequate | [TODO: Justification] |
| [TODO] | [TODO] | [TODO] | [TODO] |

**Legend:**
- **Adequate:** SFR is sufficient to fulfill the objectives
- **To Review:** Further analysis required
- **Insufficient:** SFR must be strengthened or supplemented

## Consistency Analysis



### Internal Consistency

[TODO: Verify that the SFRs are internally consistent]

**Identified Inconsistencies:**
[TODO: List all inconsistencies]

**Inconsistency 1:** [TODO: Description]
- **Affected SFRs:** [TODO: SFR-IDs]
- **Conflict:** [TODO: Describe the conflict]
- **Resolution:** [TODO: Describe the resolution]

### Consistency with Security Objectives

[TODO: Verify that the SFRs are consistent with the security objectives]

**Identified Inconsistencies:**
[TODO: List all inconsistencies]

## Rationale Summary



### Completeness

[TODO: Confirm that all security objectives are fulfilled by SFRs]

**Status:** [TODO: Complete / Incomplete]

**Justification:**
[TODO: Explain the completeness status]

### Adequacy

[TODO: Confirm that the security requirements are adequate]

**Status:** [TODO: Adequate / Needs Improvement]

**Justification:**
[TODO: Explain the adequacy status]

### Consistency

[TODO: Confirm that the security requirements are consistent]

**Status:** [TODO: Consistent / Inconsistencies Present]

**Justification:**
[TODO: Explain the consistency status]

## References



- **Section 0300:** Security Objectives
- **Section 0400:** Security Requirements
- **Section 0410:** Evaluation Assurance Level
- **Section 0430:** SFR Dependencies
- **Section 0440:** Coverage Matrix

**Next Steps:**
1. Document the rationale for each security objective
2. Justify all SFR operations
3. Verify all SFR dependencies
4. Justify the SAR selection
5. Create the coverage matrix
6. Conduct completeness, adequacy, and consistency analyses
7. Identify and address gaps and inconsistencies
8. Have the rationale reviewed by evaluators

