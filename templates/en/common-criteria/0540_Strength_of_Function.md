# Strength of Function

**Document-ID:** 0540
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

> **Note:** This document is a template. Replace all `[TODO]` placeholders and adapt the content to your specific TOE (Target of Evaluation).

<!-- 
GUIDANCE FOR TEMPLATE AUTHORS:
The Strength of Function (SOF) analysis evaluates the strength of probabilistic or
permutation-based security mechanisms against attacks.

IMPORTANT NOTES:
- SOF applies only to probabilistic/permutation-based mechanisms (e.g., passwords, keys)
- SOF does NOT apply to deterministic mechanisms (e.g., access control lists)
- The analysis must be mathematically sound
- Consider realistic attack scenarios
- Document all assumptions
-->

## 1. Introduction

### 1.1 Purpose

This document analyzes the Strength of Function (SOF) for **[TODO: TOE Name]**. The SOF analysis evaluates the strength of probabilistic or permutation-based security mechanisms against various types of attacks.

### 1.2 SOF Concept

**Definition:**
The Strength of Function is a measure of the minimum strength that a TOE security mechanism provides against direct attacks. It is expressed as the probability that an attacker can overcome the mechanism in a given time with given resources.

**SOF Levels:**
- **SOF-basic**: Protection against attackers with limited resources and capabilities
- **SOF-medium**: Protection against attackers with moderate resources and capabilities
- **SOF-high**: Protection against attackers with high resources and capabilities

### 1.3 Applicability

SOF applies to the following types of mechanisms:
- Password-based authentication
- Biometric authentication
- Random number generators
- Cryptographic key generation (for probabilistic methods)
- Challenge-response mechanisms

SOF does NOT apply to:
- Deterministic access control mechanisms
- Cryptographic algorithms themselves (these are evaluated separately)
- Audit mechanisms
- Timestamp mechanisms

## 2. SOF-Claim

### 2.1 Claimed SOF Level

The TOE claims the following SOF level:

**SOF-Claim:** [TODO: SOF-basic / SOF-medium / SOF-high]

<!-- 
GUIDANCE:
Choose the SOF level based on:
- The threat analysis (Chapter 2 of the Security Target)
- Expected attacker capabilities
- Security objectives
- Stakeholder requirements

SOF-basic: Attackers with limited resources (e.g., individual, simple tools)
SOF-medium: Attackers with moderate resources (e.g., small group, specialized tools)
SOF-high: Attackers with high resources (e.g., organized group, significant resources)
-->

**Rationale for SOF-Claim:**

[TODO: Justify the choice of SOF level. Example:]

The TOE is deployed in an environment where the following threats exist:
- [TODO: Describe relevant Threats from Chapter 2]
- [TODO: Describe expected attacker capabilities]
- [TODO: Describe security objectives]

Based on this analysis, SOF-[TODO] is appropriate because:
- [TODO: Rationale 1]
- [TODO: Rationale 2]
- [TODO: Rationale 3]

## 3. Identification of Probabilistic Mechanisms

### 3.1 Overview

The following probabilistic or permutation-based mechanisms have been identified in the TOE:

| Mechanism-ID | Mechanism-Name | TSF-ID | Type | SOF-relevant |
|--------------|----------------|--------|------|--------------|
| M-1 | [TODO] | TSF-[TODO] | [TODO: Password/Biometric/RNG/etc.] | Yes/No |
| M-2 | [TODO] | TSF-[TODO] | [TODO] | Yes/No |
| M-3 | [TODO] | TSF-[TODO] | [TODO] | Yes/No |

<!-- 
GUIDANCE:
- Identify all probabilistic/permutation-based mechanisms
- Map them to the corresponding TSFs
- Classify the type of mechanism
- Mark whether the mechanism is SOF-relevant
-->

### 3.2 Non-SOF-relevant Mechanisms

The following mechanisms are NOT SOF-relevant because they are deterministic:

| Mechanism-ID | Mechanism-Name | TSF-ID | Rationale |
|--------------|----------------|--------|-----------|
| [TODO] | [TODO] | TSF-[TODO] | [TODO: Why not SOF-relevant?] |

## 4. SOF Analysis

<!-- 
GUIDANCE:
For each SOF-relevant mechanism:
1. Describe the mechanism in detail
2. Identify possible attack types
3. Calculate the attack strength (success probability)
4. Evaluate the SOF level
5. Compare with the SOF-Claim
-->

### 4.1 Mechanism M-1: [TODO: Name]

**Mechanism-ID:** M-1  
**TSF-ID:** TSF-[TODO]  
**Type:** [TODO: e.g., Password Authentication]

#### 4.1.1 Mechanism Description

[TODO: Describe the mechanism in detail. Example:]

The password authentication mechanism uses:
- Password length: Minimum [TODO] characters, Maximum [TODO] characters
- Character set: [TODO: e.g., Upper/lowercase letters, digits, special characters]
- Password complexity rules: [TODO: Describe the rules]
- Storage: [TODO: e.g., SHA-256 hash with salt]
- Failed attempt handling: [TODO: e.g., Account lockout after X attempts]

#### 4.1.2 Attack Scenarios

**Possible Attack Types:**

1. **Brute-Force Attack**
   - Description: Systematic trying of all possible passwords
   - Resources: [TODO: Describe required resources]
   - Time required: [TODO: Calculate time required]

2. **Dictionary Attack**
   - Description: Trying commonly used passwords
   - Resources: [TODO: Describe required resources]
   - Time required: [TODO: Calculate time required]

3. **Guessing Attack**
   - Description: Guessing passwords based on user information
   - Resources: [TODO: Describe required resources]
   - Success probability: [TODO: Estimate probability]

#### 4.1.3 SOF Calculation

**Assumptions:**
- [TODO: List all assumptions, e.g.:]
- Users choose passwords randomly from the allowed character set
- Attacker has no access to the password hash
- Attacker can perform maximum [TODO] attempts per time unit

**Calculation:**

[TODO: Perform the SOF calculation. Example:]

**Character Set Size:**
- Lowercase letters: 26
- Uppercase letters: 26
- Digits: 10
- Special characters: 10
- Total: 72 characters

**Password Space:**
- Minimum password length: 8 characters
- Number of possible passwords: 72^8 = 7.22 × 10^14

**Brute-Force Attack:**
- Attempts per second: [TODO: e.g., 1000]
- Time for complete enumeration: 7.22 × 10^14 / 1000 / 86400 / 365 = approx. 22.9 million years
- Success probability after 1 year: 1 / 22,900,000 ≈ 4.4 × 10^-8

**Account Lockout:**
- Maximum failed attempts: [TODO: e.g., 5]
- Success probability: 5 / 7.22 × 10^14 ≈ 6.9 × 10^-15

**Dictionary Attack:**
- Dictionary size: [TODO: e.g., 1 million common passwords]
- Success probability (without lockout): 1,000,000 / 7.22 × 10^14 ≈ 1.4 × 10^-9
- Success probability (with lockout): 5 / 1,000,000 = 5 × 10^-6

#### 4.1.4 SOF Evaluation

**Determined SOF Level:** [TODO: SOF-basic / SOF-medium / SOF-high]

**Rationale:**

[TODO: Justify the determined SOF level. Example:]

Based on the analysis:
- Brute-force attacks are practically impossible (success probability < 10^-10)
- Dictionary attacks are effectively prevented by account lockout (success probability < 10^-5)
- The mechanism provides protection against attackers with [TODO: limited/moderate/high] resources

The determined SOF level is **SOF-[TODO]**.

**Comparison with SOF-Claim:**
- SOF-Claim: SOF-[TODO]
- Determined SOF: SOF-[TODO]
- Fulfillment: ✓ Yes / ✗ No

### 4.2 Mechanism M-2: [TODO: Name]

**Mechanism-ID:** M-2  
**TSF-ID:** TSF-[TODO]  
**Type:** [TODO]

#### 4.2.1 Mechanism Description

[TODO: Description analogous to 4.1.1]

#### 4.2.2 Attack Scenarios

[TODO: Analysis analogous to 4.1.2]

#### 4.2.3 SOF Calculation

[TODO: Calculation analogous to 4.1.3]

#### 4.2.4 SOF Evaluation

[TODO: Evaluation analogous to 4.1.4]

### 4.3 Mechanism M-3: [TODO: Name]

[TODO: Analyze additional mechanisms following the same schema]

## 5. Summary of SOF Analysis

### 5.1 Overview of All Mechanisms

| Mechanism-ID | Mechanism-Name | Determined SOF | SOF-Claim | Fulfillment |
|--------------|----------------|----------------|-----------|-------------|
| M-1 | [TODO] | SOF-[TODO] | SOF-[TODO] | ✓/✗ |
| M-2 | [TODO] | SOF-[TODO] | SOF-[TODO] | ✓/✗ |
| M-3 | [TODO] | SOF-[TODO] | SOF-[TODO] | ✓/✗ |

### 5.2 Fulfillment of SOF-Claim

**SOF-Claim:** SOF-[TODO]

**Analysis:**

[TODO: Analyze whether all mechanisms fulfill the SOF-Claim. Example:]

- Number of analyzed mechanisms: [TODO]
- Number of mechanisms fulfilling SOF-Claim: [TODO]
- Number of mechanisms not fulfilling SOF-Claim: [TODO]

**Result:**

[TODO: Choose one of the following options:]

✓ **All mechanisms fulfill the SOF-Claim**
- The SOF-Claim of SOF-[TODO] is met or exceeded by all analyzed mechanisms.

✗ **Not all mechanisms fulfill the SOF-Claim**
- The following mechanisms do not fulfill the SOF-Claim: [TODO: List]
- Actions: [TODO: Describe planned actions]

### 5.3 Weakest Mechanism

**Weakest Mechanism:** [TODO: Mechanism-ID and Name]  
**SOF Level:** SOF-[TODO]

**Rationale:**
[TODO: Explain why this mechanism is the weakest and whether this is acceptable.]

### 5.4 Assumptions and Limitations

**Assumptions:**
[TODO: List all assumptions made for the SOF analysis. Example:]
- Users choose passwords randomly
- Attacker has no physical access to the system
- Attacker has no insider information
- [TODO: Additional assumptions]

**Limitations:**
[TODO: List all limitations of the analysis. Example:]
- The analysis does not consider side-channel attacks
- The analysis does not consider social engineering attacks
- [TODO: Additional limitations]

## 6. Recommendations

### 6.1 Improvement Opportunities

[TODO: Provide recommendations for improving SOF. Example:]

1. **Increase Password Complexity**
   - Current minimum length: [TODO]
   - Recommended minimum length: [TODO]
   - Expected SOF improvement: [TODO]

2. **Multi-Factor Authentication**
   - Implementation of a second factor (e.g., OTP, hardware token)
   - Expected SOF improvement: [TODO]

3. **Adaptive Authentication**
   - Adjustment of security requirements based on risk assessment
   - Expected SOF improvement: [TODO]

### 6.2 Maintenance and Monitoring

[TODO: Describe measures to maintain SOF. Example:]

- Regular review of password policies
- Monitoring of authentication attempts
- Update of SOF analysis when TOE changes
- Consideration of new attack techniques

## 7. Summary

### 7.1 Result of SOF Analysis

The SOF analysis for **[TODO: TOE Name]** shows:

- ✓ All probabilistic mechanisms have been identified
- ✓ All mechanisms have been analyzed
- ✓ SOF calculations are documented
- ✓ SOF-Claim is fulfilled / ✗ SOF-Claim is not fulfilled

**Overall Assessment:** [TODO: Summary assessment]

### 7.2 Reference to Additional Documents

For further information see:

- **0500_TOE_Summary_Specification.md**: Detailed description of TSFs
- **0510_Assurance_Measures.md**: AVA_SOF.1 Assurance Measure
- **Chapter 4 of the Security Target**: Definition of SFRs

