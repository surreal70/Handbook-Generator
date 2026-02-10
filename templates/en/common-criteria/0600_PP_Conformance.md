# Protection Profile Conformance

**Document-ID:** 0600  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Update:** {{ meta.date }}  

---

> **Note:** This document is a template. Replace all `[TODO]` placeholders and HTML comments with project-specific information.

<!-- 
GUIDANCE FOR TEMPLATE AUTHORS:
This template documents the Security Target (ST) conformance with one or more Protection Profiles (PP).
If no PP conformance is claimed, document this explicitly.

Important aspects:
- Identify all relevant Protection Profiles
- Document the conformance claim (strict, demonstrable, or no conformance)
- List all deviations from the PP
- Justify each deviation
- Reference corresponding ST sections
-->

## Overview

This chapter documents the conformance of the Security Target (ST) with relevant Protection Profiles (PP) according to ISO/IEC 15408.

<!-- Briefly describe whether and with which PPs conformance is claimed -->

**PP Conformance Claim:** [TODO: Strict / Demonstrable / No Conformance]

## Protection Profile Identification

<!-- List all relevant Protection Profiles -->

### PP 1: [TODO: PP Name]

- **PP Title:** [TODO: Full title of the Protection Profile]
- **PP Version:** [TODO: Version]
- **PP Date:** [TODO: Publication date]
- **PP Registration:** [TODO: Registration number if available]
- **PP Publisher:** [TODO: Organization]
- **Conformance Type:** [TODO: Strict / Demonstrable]

**Description:**
<!-- Brief description of the PP and its relevance to the TOE -->
[TODO: Describe the Protection Profile and why it is relevant for this TOE]

### PP 2: [TODO: PP Name] (if applicable)

- **PP Title:** [TODO: Full title]
- **PP Version:** [TODO: Version]
- **PP Date:** [TODO: Date]
- **PP Registration:** [TODO: Number]
- **PP Publisher:** [TODO: Organization]
- **Conformance Type:** [TODO: Strict / Demonstrable]

**Description:**
[TODO: Description]

## Conformance Claim

<!-- Document the specific conformance claim -->

### Strict Conformance

<!-- If strict conformance is claimed -->

[TODO: Document that the ST adopts all PP requirements without modifications]

**Conformance Statement:**
- All Security Functional Requirements (SFRs) from the PP are included in the ST
- All Security Assurance Requirements (SARs) from the PP are included in the ST
- All security objectives from the PP are included in the ST
- No deviations from the PP

### Demonstrable Conformance

<!-- If demonstrable conformance is claimed -->

[TODO: Document how the ST meets the PP requirements, even if adaptations were made]

**Conformance Statement:**
- The ST meets the security objectives of the PP
- The ST may contain additional requirements
- The ST may refine or extend PP requirements
- All deviations are documented and justified

### No PP Conformance

<!-- If no PP conformance is claimed -->

[TODO: Justify why no PP conformance is claimed]

**Justification:**
[TODO: Explain the reasons for the decision not to claim PP conformance]

## Conformance Analysis

<!-- Detailed analysis of conformance with each PP -->

### Conformance with [TODO: PP Name]

#### Security Functional Requirements (SFR)

<!-- Compare the SFRs of the PP with those of the ST -->

| PP SFR | ST SFR | Status | Comment |
|--------|--------|--------|---------|
| [TODO: PP-SFR-ID] | [TODO: ST-SFR-ID] | Identical / Extended / Refined | [TODO: Explanation] |
| [TODO] | [TODO] | [TODO] | [TODO] |

**Summary:**
[TODO: Summarize the SFR conformance]

#### Security Assurance Requirements (SAR)

<!-- Compare the SARs of the PP with those of the ST -->

| PP SAR | ST SAR | Status | Comment |
|--------|--------|--------|---------|
| [TODO: PP-SAR-ID] | [TODO: ST-SAR-ID] | Identical / Extended | [TODO: Explanation] |
| [TODO] | [TODO] | [TODO] | [TODO] |

**Summary:**
[TODO: Summarize the SAR conformance]

#### Security Objectives

<!-- Compare the security objectives of the PP with those of the ST -->

| PP Security Objective | ST Security Objective | Status | Comment |
|-----------------------|----------------------|--------|---------|
| [TODO: PP-Objective-ID] | [TODO: ST-Objective-ID] | Identical / Extended | [TODO: Explanation] |
| [TODO] | [TODO] | [TODO] | [TODO] |

**Summary:**
[TODO: Summarize the security objectives conformance]

## Deviations from Protection Profile

<!-- Document all deviations from the PP -->

### Deviation 1: [TODO: Title]

- **Affected PP Section:** [TODO: Section/Requirement]
- **Type of Deviation:** [TODO: Addition / Refinement / Omission / Modification]
- **Description:** [TODO: Describe the deviation in detail]
- **Justification:** [TODO: Explain why this deviation is necessary]
- **Security Impact:** [TODO: Assess the security implications]
- **Reference to ST Section:** [TODO: Section number in ST]

### Deviation 2: [TODO: Title] (if applicable)

- **Affected PP Section:** [TODO]
- **Type of Deviation:** [TODO]
- **Description:** [TODO]
- **Justification:** [TODO]
- **Security Impact:** [TODO]
- **Reference to ST Section:** [TODO]

## Additional Requirements

<!-- Document all requirements in the ST that are not in the PP -->

### Additional SFRs

| ST SFR | Description | Justification |
|--------|-------------|---------------|
| [TODO: SFR-ID] | [TODO: Brief description] | [TODO: Why was this SFR added?] |
| [TODO] | [TODO] | [TODO] |

### Additional SARs

| ST SAR | Description | Justification |
|--------|-------------|---------------|
| [TODO: SAR-ID] | [TODO: Brief description] | [TODO: Why was this SAR added?] |
| [TODO] | [TODO] | [TODO] |

### Additional Security Objectives

| ST Objective | Description | Justification |
|--------------|-------------|---------------|
| [TODO: Objective-ID] | [TODO: Brief description] | [TODO: Why was this objective added?] |
| [TODO] | [TODO] | [TODO] |

## Conformance Assessment

<!-- Summary assessment of PP conformance -->

### Conformance Status

**Overall Assessment:** [TODO: Conformant / Conformant with Deviations / Non-conformant]

**Summary:**
[TODO: Summarize the conformance status and assess whether the ST meets the PP requirements]

### Conformance Evidence

<!-- Document how conformance is demonstrated -->

[TODO: Describe the methodology and evidence for PP conformance]

**Evidence Documentation:**
- [TODO: Reference to relevant ST sections]
- [TODO: Reference to mapping tables]
- [TODO: Reference to rationale documents]

## References

<!-- List all referenced Protection Profiles and related documents -->

1. [TODO: PP Reference 1]
2. [TODO: PP Reference 2]
3. [TODO: Other relevant documents]

---

**Next Steps:**
1. Identify all relevant Protection Profiles
2. Document the conformance claim
3. Conduct detailed conformance analysis
4. Document all deviations and additional requirements
5. Create mapping tables between PP and ST
6. Have PP conformance reviewed by evaluators
