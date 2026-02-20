# Functions Rationale

**Document-ID:** COMMON-CRITERIA-0520
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

> **Note:** This document is a template. Replace all `[TODO]` placeholders and adapt the content to your specific TOE (Target of Evaluation).



## 1. Introduction

### 1.1 Purpose

This document provides the rationale for the mapping of TOE Security Functions (TSFs) to Security Functional Requirements (SFRs) for **[TODO: TOE Name]**.

The Functions Rationale demonstrates that:
- Each SFR is fulfilled by at least one TSF
- The TSFs implement the SFRs completely and correctly
- No gaps exist in the security functionality
- The mapping between TSFs and SFRs is traceable

### 1.2 Structure

This document is structured as follows:

- **Chapter 2**: Overview of TSF ↔ SFR mapping
- **Chapter 3**: Detailed rationale for each SFR
- **Chapter 4**: Completeness analysis
- **Chapter 5**: Summary

## 2. Mapping Overview

### 2.1 Mapping Matrix

The following matrix shows the mapping between TSFs and SFRs:

| SFR-ID | SFR-Name | TSF-1 | TSF-2 | TSF-3 | TSF-4 | TSF-5 | TSF-6 |
|--------|----------|-------|-------|-------|-------|-------|-------|
| [TODO] | [TODO]   | ●     |       |       |       |       |       |
| [TODO] | [TODO]   | ●     | ●     |       |       |       |       |
| [TODO] | [TODO]   |       | ●     |       |       |       |       |
| [TODO] | [TODO]   |       |       | ●     |       |       |       |
| [TODO] | [TODO]   |       |       | ●     | ●     |       |       |

**Legend:**
- ● = TSF fulfills this SFR (completely or partially)



### 2.2 TSF Overview

| TSF-ID | TSF-Name | Number of Associated SFRs | Description |
|--------|----------|---------------------------|-------------|
| TSF-1 | [TODO] | [TODO] | [TODO: Brief description] |
| TSF-2 | [TODO] | [TODO] | [TODO: Brief description] |
| TSF-3 | [TODO] | [TODO] | [TODO: Brief description] |

## 3. Detailed Rationale



### 3.1 Security Audit (FAU)

#### 3.1.1 FAU_GEN.1: Audit Data Generation

**SFR Description:**
[TODO: Brief description of the SFR. Example:]
The TOE must be able to generate audit records for security-relevant events.

**Associated TSFs:**
- TSF-[TODO]: [TODO: TSF Name]

**Rationale:**

[TODO: Detailed rationale. Example:]

TSF-3 (Audit Function) fulfills FAU_GEN.1 through the following mechanisms:

1. **Event Detection**: The audit function monitors all security-relevant events, including:
   - Authentication attempts (successful and failed)
   - Access to protected resources
   - Changes to security parameters
   - Administrative actions

2. **Audit Records**: For each event, an audit record is generated containing:
   - Timestamp
   - Event type
   - User ID
   - Result (Success/Failure)
   - Additional event-specific information

3. **Completeness**: All events required by FAU_GEN.1 are captured.

**Fulfillment Level:** Completely fulfilled ✓

#### 3.1.2 FAU_SAR.1: Audit Review

**SFR Description:**
[TODO: Description of the SFR]

**Associated TSFs:**
- TSF-[TODO]: [TODO: TSF Name]

**Rationale:**

[TODO: Detailed rationale analogous to 3.1.1]

**Fulfillment Level:** [TODO: Completely fulfilled / Partially fulfilled / With limitations]

### 3.2 Cryptographic Support (FCS)

#### 3.2.1 FCS_CKM.1: Cryptographic Key Generation

**SFR Description:**
[TODO: Description of the SFR]

**Associated TSFs:**
- TSF-[TODO]: [TODO: TSF Name]

**Rationale:**

[TODO: Detailed rationale]

**Fulfillment Level:** [TODO]

#### 3.2.2 FCS_COP.1: Cryptographic Operation

**SFR Description:**
[TODO: Description of the SFR]

**Associated TSFs:**
- TSF-[TODO]: [TODO: TSF Name]

**Rationale:**

[TODO: Detailed rationale]

**Fulfillment Level:** [TODO]

### 3.3 User Data Protection (FDP)

#### 3.3.1 FDP_ACC.1: Subset Access Control

**SFR Description:**
[TODO: Description of the SFR]

**Associated TSFs:**
- TSF-[TODO]: [TODO: TSF Name]

**Rationale:**

[TODO: Detailed rationale]

**Fulfillment Level:** [TODO]

#### 3.3.2 FDP_ACF.1: Security Attribute Based Access Control

**SFR Description:**
[TODO: Description of the SFR]

**Associated TSFs:**
- TSF-[TODO]: [TODO: TSF Name]

**Rationale:**

[TODO: Detailed rationale]

**Fulfillment Level:** [TODO]

### 3.4 Identification and Authentication (FIA)

#### 3.4.1 FIA_UID.1: Timing of Identification

**SFR Description:**
[TODO: Description of the SFR]

**Associated TSFs:**
- TSF-[TODO]: [TODO: TSF Name]

**Rationale:**

[TODO: Detailed rationale]

**Fulfillment Level:** [TODO]

#### 3.4.2 FIA_UAU.1: Timing of Authentication

**SFR Description:**
[TODO: Description of the SFR]

**Associated TSFs:**
- TSF-[TODO]: [TODO: TSF Name]

**Rationale:**

[TODO: Detailed rationale]

**Fulfillment Level:** [TODO]

#### 3.4.3 FIA_AFL.1: Authentication Failure Handling

**SFR Description:**
[TODO: Description of the SFR]

**Associated TSFs:**
- TSF-[TODO]: [TODO: TSF Name]

**Rationale:**

[TODO: Detailed rationale]

**Fulfillment Level:** [TODO]

### 3.5 Security Management (FMT)

#### 3.5.1 FMT_SMF.1: Specification of Management Functions

**SFR Description:**
[TODO: Description of the SFR]

**Associated TSFs:**
- TSF-[TODO]: [TODO: TSF Name]

**Rationale:**

[TODO: Detailed rationale]

**Fulfillment Level:** [TODO]

#### 3.5.2 FMT_SMR.1: Security Roles

**SFR Description:**
[TODO: Description of the SFR]

**Associated TSFs:**
- TSF-[TODO]: [TODO: TSF Name]

**Rationale:**

[TODO: Detailed rationale]

**Fulfillment Level:** [TODO]

### 3.6 Protection of the TSF (FPT)

#### 3.6.1 FPT_STM.1: Reliable Time Stamps

**SFR Description:**
[TODO: Description of the SFR]

**Associated TSFs:**
- TSF-[TODO]: [TODO: TSF Name]

**Rationale:**

[TODO: Detailed rationale]

**Fulfillment Level:** [TODO]

### 3.7 TOE Access (FTA)

#### 3.7.1 FTA_SSL.1: TSF-initiated Session Locking

**SFR Description:**
[TODO: Description of the SFR]

**Associated TSFs:**
- TSF-[TODO]: [TODO: TSF Name]

**Rationale:**

[TODO: Detailed rationale]

**Fulfillment Level:** [TODO]

### 3.8 Trusted Path/Channels (FTP)

#### 3.8.1 FTP_TRP.1: Trusted Path

**SFR Description:**
[TODO: Description of the SFR]

**Associated TSFs:**
- TSF-[TODO]: [TODO: TSF Name]

**Rationale:**

[TODO: Detailed rationale]

**Fulfillment Level:** [TODO]



## 4. Completeness Analysis

### 4.1 Coverage of SFRs

**Statistics:**
- Total number of SFRs: [TODO]
- Completely fulfilled SFRs: [TODO]
- Partially fulfilled SFRs: [TODO]
- Unfulfilled SFRs: [TODO]

**Coverage Rate:** [TODO]%

### 4.2 Unfulfilled or Partially Fulfilled SFRs

[TODO: If SFRs are not completely fulfilled, list them here and justify:]

| SFR-ID | Status | Rationale | Actions |
|--------|--------|-----------|---------|
| [TODO] | Partially fulfilled | [TODO: Why only partially?] | [TODO: Planned actions] |

**Note:** If all SFRs are completely fulfilled, write: "All SFRs are completely fulfilled."

### 4.3 Multiple Mappings

Some SFRs are fulfilled by multiple TSFs. This is the case in the following situations:

| SFR-ID | Associated TSFs | Rationale for Multiple Mapping |
|--------|-----------------|-------------------------------|
| [TODO] | TSF-X, TSF-Y | [TODO: Why multiple TSFs?] |



### 4.4 TSF Coverage

The following table shows which TSFs fulfill how many SFRs:

| TSF-ID | TSF-Name | Number of Fulfilled SFRs | Percentage |
|--------|----------|-------------------------|------------|
| TSF-1 | [TODO] | [TODO] | [TODO]% |
| TSF-2 | [TODO] | [TODO] | [TODO]% |
| TSF-3 | [TODO] | [TODO] | [TODO]% |

**Analysis:**
[TODO: Analyze the distribution. Are there TSFs that fulfill many SFRs? Is the distribution balanced?]

## 5. Summary

### 5.1 Completeness of Mapping

The mapping between TSFs and SFRs is complete:

- ✓ All SFRs are covered by at least one TSF
- ✓ All mappings are justified
- ✓ No gaps in security functionality
- ✓ Multiple mappings are explained

### 5.2 Correctness of Mapping

The rationales demonstrate that:

- The TSFs correctly implement the SFRs
- The TSFs provide the required functionality
- The TSFs ensure the security properties
- The mapping is traceable and convincing

### 5.3 Reference to Additional Documents

For further information see:

- **0500_TOE_Summary_Specification.md**: Detailed description of TSFs
- **0530_Coverage_Matrix.md**: Complete Coverage Matrix
- **Chapter 4 of the Security Target**: Definition of SFRs

