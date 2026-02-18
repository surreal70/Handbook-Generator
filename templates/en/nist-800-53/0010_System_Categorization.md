# System Categorization

**Document-ID:** NIST-0010
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

## 1. Purpose

This document describes the categorization of the information system {{ meta.nist.system_name }} according to FIPS 199 and NIST SP 800-60.

### 1.1 Objectives

- **FIPS 199 Compliance:** Categorization by security objectives (confidentiality, integrity, availability)
- **Risk Assessment:** Determination of potential impacts from security breaches
- **Baseline Selection:** Foundation for security control selection
- **Compliance:** Meeting federal requirements

### 1.2 References

- **FIPS 199:** Standards for Security Categorization of Federal Information and Information Systems
- **NIST SP 800-60 Vol. 1 Rev. 1:** Guide for Mapping Types of Information and Information Systems to Security Categories
- **NIST SP 800-60 Vol. 2 Rev. 1:** Appendices to Guide for Mapping Types of Information and Information Systems to Security Categories
- **NIST SP 800-53 Rev. 5:** Security and Privacy Controls for Information Systems and Organizations

## 2. System Information

### 2.1 System Identification

**System Name:** {{ meta.nist.system_name }}  
**System ID:** {{ meta.nist.system_id }}  
**System Owner:** [TODO: Name] ([TODO: Email])  
**Authorizing Official (AO):** [TODO] ([TODO])  
**Information System Security Officer (ISSO):** [TODO] ([TODO])  

### 2.2 System Description

**Purpose:** [TODO: Description of system purpose]

**Functions:**
- [TODO: Main function 1]
- [TODO: Main function 2]
- [TODO: Main function 3]

**Users:**
- **Internal Users:** [TODO: Number and roles]
- **External Users:** [TODO: Number and roles]
- **Privileged Users:** [TODO: Number and roles]

### 2.3 Information Types

| Information Type | Description | Source (NIST 800-60) |
|------------------|-------------|----------------------|
| [TODO: Type 1] | [TODO: Description] | [TODO: C.2.x.x] |
| [TODO: Type 2] | [TODO: Description] | [TODO: C.3.x.x] |
| [TODO: Type 3] | [TODO: Description] | [TODO: C.4.x.x] |

## 3. FIPS 199 Categorization

### 3.1 Security Objectives and Impact Levels

Categorization is performed according to three security objectives:

#### 3.1.1 Confidentiality

**Definition:** Protection from unauthorized disclosure of information.

**Impact Level:** [TODO: Low / Moderate / High]

**Rationale:**
[TODO: Describe potential impacts of unauthorized disclosure]

**Impact Examples:**
- **Low:** Limited adverse effects on organizational operations, assets, or individuals
- **Moderate:** Serious adverse effects
- **High:** Severe or catastrophic adverse effects

**Specific Impacts for This System:**
- [TODO: Impact 1]
- [TODO: Impact 2]
- [TODO: Impact 3]

#### 3.1.2 Integrity

**Definition:** Protection from unauthorized modification or destruction of information.

**Impact Level:** [TODO: Low / Moderate / High]

**Rationale:**
[TODO: Describe potential impacts of unauthorized modification]

**Specific Impacts for This System:**
- [TODO: Impact 1]
- [TODO: Impact 2]
- [TODO: Impact 3]

#### 3.1.3 Availability

**Definition:** Ensuring timely and reliable access to information.

**Impact Level:** [TODO: Low / Moderate / High]

**Rationale:**
[TODO: Describe potential impacts of availability loss]

**Specific Impacts for This System:**
- [TODO: Impact 1]
- [TODO: Impact 2]
- [TODO: Impact 3]

### 3.2 Overall Categorization

**FIPS 199 Security Category:**

```
SC {{ meta.nist.system_name }} = {(confidentiality, [TODO: impact]), (integrity, [TODO: impact]), (availability, [TODO: impact])}
```

**Example:**
```
SC Information System = {(confidentiality, MODERATE), (integrity, MODERATE), (availability, LOW)}
```

**Overall System Categorization:** [TODO: Low / Moderate / High]

> **Note:** Overall categorization corresponds to the highest impact level of the three security objectives (High-Water Mark).

## 4. Categorization by Information Types

### 4.1 Information Type Analysis

For each information type, categorization is performed according to NIST SP 800-60:

#### Information Type 1: [TODO: Name]

**Description:** [TODO: Description of information type]

**NIST 800-60 Reference:** [TODO: C.x.x.x]

| Security Objective | Provisional Impact | Adjusted Impact | Rationale |
|-------------------|-------------------|-----------------|-----------|
| Confidentiality | [TODO: L/M/H] | [TODO: L/M/H] | [TODO: Rationale] |
| Integrity | [TODO: L/M/H] | [TODO: L/M/H] | [TODO: Rationale] |
| Availability | [TODO: L/M/H] | [TODO: L/M/H] | [TODO: Rationale] |

#### Information Type 2: [TODO: Name]

**Description:** [TODO: Description of information type]

**NIST 800-60 Reference:** [TODO: C.x.x.x]

| Security Objective | Provisional Impact | Adjusted Impact | Rationale |
|-------------------|-------------------|-----------------|-----------|
| Confidentiality | [TODO: L/M/H] | [TODO: L/M/H] | [TODO: Rationale] |
| Integrity | [TODO: L/M/H] | [TODO: L/M/H] | [TODO: Rationale] |
| Availability | [TODO: L/M/H] | [TODO: L/M/H] | [TODO: Rationale] |

### 4.2 Aggregated Categorization

**Method:** High-Water Mark (highest impact level across all information types)

| Security Objective | Aggregated Impact |
|-------------------|-------------------|
| Confidentiality | [TODO: Low / Moderate / High] |
| Integrity | [TODO: Low / Moderate / High] |
| Availability | [TODO: Low / Moderate / High] |

## 5. Baseline Selection

### 5.1 NIST 800-53 Baseline

Based on overall categorization, the following baseline is selected:

**Selected Baseline:** [TODO: Low / Moderate / High Baseline]

**Baseline Controls:**
- **Low Baseline:** NIST SP 800-53B, Appendix A
- **Moderate Baseline:** NIST SP 800-53B, Appendix B
- **High Baseline:** NIST SP 800-53B, Appendix C

### 5.2 Tailoring

**Tailoring Activities:**
- **Added Controls:** [TODO: List of additional controls]
- **Removed Controls:** [TODO: List of removed controls with rationale]
- **Modified Controls:** [TODO: List of modified controls]

## 6. Categorization Process

### 6.1 Process Steps

1. **System Identification:** Identify system to be categorized
2. **Information Type Identification:** Identify all processed information types
3. **Provisional Impact:** Determine provisional impact levels per NIST 800-60
4. **Impact Adjustment:** Adjust based on organization-specific factors
5. **Aggregation:** Aggregate to overall categorization
6. **Documentation:** Document categorization
7. **Approval:** Approval by Authorizing Official

### 6.2 Involved Roles

| Role | Name | Responsibility |
|------|------|----------------|
| System Owner | [TODO: Name] | System responsibility |
| Information Owner | [TODO: Name] | Information responsibility |
| ISSO | [TODO] | Security assessment |
| ISSM | [TODO] | Security management |
| Authorizing Official (AO) | [TODO] | Approval |

### 6.3 Categorization Date

**Initial Categorization:** [TODO: Date]  
**Last Review:** [TODO: Date]  
**Next Review:** [TODO: Date]  

## 7. Impact Analysis

### 7.1 Confidentiality Loss

**Potential impacts from unauthorized disclosure:**

| Area | Impact | Severity |
|------|--------|----------|
| Organizational Operations | [TODO: Description] | [TODO: L/M/H] |
| Organizational Assets | [TODO: Description] | [TODO: L/M/H] |
| Individuals | [TODO: Description] | [TODO: L/M/H] |
| National Security | [TODO: Description] | [TODO: L/M/H] |

### 7.2 Integrity Loss

**Potential impacts from unauthorized modification:**

| Area | Impact | Severity |
|------|--------|----------|
| Organizational Operations | [TODO: Description] | [TODO: L/M/H] |
| Organizational Assets | [TODO: Description] | [TODO: L/M/H] |
| Individuals | [TODO: Description] | [TODO: L/M/H] |
| National Security | [TODO: Description] | [TODO: L/M/H] |

### 7.3 Availability Loss

**Potential impacts from system failure:**

| Area | Impact | Severity |
|------|--------|----------|
| Organizational Operations | [TODO: Description] | [TODO: L/M/H] |
| Organizational Assets | [TODO: Description] | [TODO: L/M/H] |
| Individuals | [TODO: Description] | [TODO: L/M/H] |
| National Security | [TODO: Description] | [TODO: L/M/H] |

## 8. Approval

### 8.1 Categorization Approval

**Categorization approved by:**

**Name:** [TODO]  
**Title:** Authorizing Official (AO)  
**Date:** [TODO: Date]  
**Signature:** [TODO: Signature or electronic approval]  

### 8.2 Review Interval

**Review Frequency:** [TODO: Annually / Upon significant changes]

**Triggers for Recategorization:**
- Significant system changes
- New information types
- Changes in threat landscape
- Organizational changes
- Legal or regulatory changes

## 9. Appendix

### 9.1 FIPS 199 Impact Level Definitions

**Low Impact:**
> The potential impact is LOW if the loss of confidentiality, integrity, or availability could be expected to have a limited adverse effect on organizational operations, organizational assets, or individuals.

**Moderate Impact:**
> The potential impact is MODERATE if the loss of confidentiality, integrity, or availability could be expected to have a serious adverse effect on organizational operations, organizational assets, or individuals.

**High Impact:**
> The potential impact is HIGH if the loss of confidentiality, integrity, or availability could be expected to have a severe or catastrophic adverse effect on organizational operations, organizational assets, or individuals.

### 9.2 Categorization Matrix

| Information Type | Confidentiality | Integrity | Availability | Overall |
|------------------|-----------------|-----------|--------------|---------|
| [TODO: Type 1] | [TODO: L/M/H] | [TODO: L/M/H] | [TODO: L/M/H] | [TODO: L/M/H] |
| [TODO: Type 2] | [TODO: L/M/H] | [TODO: L/M/H] | [TODO: L/M/H] | [TODO: L/M/H] |
| [TODO: Type 3] | [TODO: L/M/H] | [TODO: L/M/H] | [TODO: L/M/H] | [TODO: L/M/H] |
| **System Overall** | **[TODO: L/M/H]** | **[TODO: L/M/H]** | **[TODO: L/M/H]** | **[TODO: L/M/H]** |

<!-- End of template -->
