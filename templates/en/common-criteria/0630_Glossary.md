# Glossary and Term Definitions

**Document-ID:** 0630  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** Draft / In Review / Approved  
**Classification:** Internal / Confidential / Strictly Confidential  
**Last Update:** {{ meta.date }}  

---

> **Note:** This document is a template. Replace all `[TODO]` placeholders and HTML comments with project-specific information.

<!-- 
GUIDANCE FOR TEMPLATE AUTHORS:
This template contains a glossary of all important terms used in the Security Target.

Important aspects:
- Define all technical terms
- Define all Common Criteria-specific terms
- Define all TOE-specific terms
- Use consistent terminology throughout the ST
- Reference ISO/IEC 15408 for standard CC terms
- Sort terms alphabetically
-->

## Overview

This glossary defines all important terms, abbreviations, and acronyms used in the Security Target. It serves as a central reference for terminology and ensures that all terms are used consistently.

<!-- Describe the purpose and structure of the glossary -->

## Common Criteria Standard Terms

<!-- Define standard CC terms according to ISO/IEC 15408 -->

### A

**Asset**
[TODO: Definition or reference to ISO/IEC 15408-1]
An asset is an entity that has value to the owner or user and therefore must be protected.

**Assumption**
[TODO: Definition or reference to ISO/IEC 15408-1]
An assumption is a statement about the security aspects of the TOE environment that is assumed to be true.

**Attack Potential**
[TODO: Definition or reference to ISO/IEC 18045]
Attack potential is a measure of an attacker's ability to conduct a successful attack.

**Augmentation**
[TODO: Definition or reference to ISO/IEC 15408-1]
Augmentation is the addition of requirements to an EAL that exceed the standard requirements.

### C

**Common Criteria (CC)**
[TODO: Definition]
ISO/IEC 15408 - International standard for evaluating the security of IT products and systems.

### E

**Evaluation Assurance Level (EAL)**
[TODO: Definition or reference to ISO/IEC 15408-3]
An EAL is a package of security assurance requirements (SARs) that represents a specific level of confidence in the security of the TOE.

**Evaluation Authority**
[TODO: Definition]
An organization responsible for overseeing and certifying Common Criteria evaluations.

### O

**Organizational Security Policy (OSP)**
[TODO: Definition or reference to ISO/IEC 15408-1]
An OSP is a security policy imposed by an organization that must be enforced by the TOE.

### P

**Protection Profile (PP)**
[TODO: Definition or reference to ISO/IEC 15408-1]
A PP is an implementation-independent set of security requirements for a category of TOEs.

### S

**Security Assurance Requirement (SAR)**
[TODO: Definition or reference to ISO/IEC 15408-3]
A SAR is a requirement that ensures confidence in the correct implementation of security functions.

**Security Functional Requirement (SFR)**
[TODO: Definition or reference to ISO/IEC 15408-2]
An SFR is a requirement that describes a security function that the TOE must provide.

**Security Objective**
[TODO: Definition or reference to ISO/IEC 15408-1]
A security objective is a statement of the intended response to identified threats and/or OSPs.

**Security Target (ST)**
[TODO: Definition or reference to ISO/IEC 15408-1]
An ST is an implementation-specific set of security requirements and specifications for a concrete TOE.

**Strength of Function (SOF)**
[TODO: Definition or reference to ISO/IEC 15408-1]
SOF is a measure of the effectiveness of a security function against direct attacks.

### T

**Target of Evaluation (TOE)**
[TODO: Definition or reference to ISO/IEC 15408-1]
The TOE is the IT product or system being evaluated.

**Threat**
[TODO: Definition or reference to ISO/IEC 15408-1]
A threat is a potential violation of security by an attacker.

**Threat Agent**
[TODO: Definition or reference to ISO/IEC 15408-1]
A threat agent is an entity that can execute a threat.

**TSF (TOE Security Functionality)**
[TODO: Definition or reference to ISO/IEC 15408-1]
The TSF is the totality of all hardware, software, and firmware components of the TOE responsible for enforcing the security policy.

**TSP (TOE Security Policy)**
[TODO: Definition or reference to ISO/IEC 15408-1]
The TSP is the set of rules that govern the security of the TOE.

## TOE-Specific Terms

<!-- Define all TOE-specific terms -->

### [TODO: Term 1]

**Definition:**
[TODO: Define the term in the context of the TOE]

**Usage in ST:**
[TODO: Describe how the term is used in the ST]

**Related Terms:**
[TODO: List related terms]

### [TODO: Term 2]

**Definition:**
[TODO: Definition]

**Usage in ST:**
[TODO: Usage]

**Related Terms:**
[TODO: Related terms]

## Technical Terms

<!-- Define all technical terms required for understanding the TOE -->

### [TODO: Technical Term 1]

**Definition:**
[TODO: Define the technical term]

**Context:**
[TODO: Explain the context in which the term is used]

**Example:**
[TODO: Provide an example of usage]

### [TODO: Technical Term 2]

**Definition:**
[TODO: Definition]

**Context:**
[TODO: Context]

**Example:**
[TODO: Example]

## Abbreviations and Acronyms

<!-- List all abbreviations and acronyms alphabetically -->

| Abbreviation | Meaning | Explanation |
|--------------|---------|-------------|
| CC | Common Criteria | ISO/IEC 15408 |
| EAL | Evaluation Assurance Level | Evaluation assurance level |
| IT | Information Technology | Information technology |
| OSP | Organizational Security Policy | Organizational security policy |
| PP | Protection Profile | Protection profile |
| SAR | Security Assurance Requirement | Security assurance requirement |
| SFR | Security Functional Requirement | Security functional requirement |
| SOF | Strength of Function | Strength of function |
| ST | Security Target | Security target |
| TOE | Target of Evaluation | Target of evaluation |
| TSF | TOE Security Functionality | TOE security functionality |
| TSP | TOE Security Policy | TOE security policy |
| [TODO] | [TODO] | [TODO] |

## Domain-Specific Terms

<!-- Define terms specific to the TOE's domain -->

### [TODO: Domain Term 1]

**Definition:**
[TODO: Define the domain-specific term]

**Relevance to TOE:**
[TODO: Explain the relevance to the TOE]

**Standards Reference:**
[TODO: Reference relevant standards or specifications]

### [TODO: Domain Term 2]

**Definition:**
[TODO: Definition]

**Relevance to TOE:**
[TODO: Relevance]

**Standards Reference:**
[TODO: Reference]

## Security Terms

<!-- Define security-related terms -->

### [TODO: Security Term 1]

**Definition:**
[TODO: Define the security term]

**Threat Context:**
[TODO: Explain the context in relation to threats]

**Protection Measures:**
[TODO: Describe relevant protection measures]

### [TODO: Security Term 2]

**Definition:**
[TODO: Definition]

**Threat Context:**
[TODO: Context]

**Protection Measures:**
[TODO: Measures]

## Operations on SFRs

<!-- Define the four operations that can be applied to SFRs -->

### Assignment

**Definition:**
Assigning a specific value to a parameter in an SFR.

**Notation:**
[assignment: value]

**Example:**
[assignment: 8 characters] for minimum password length

### Iteration

**Definition:**
Using an SFR multiple times with different operations or for different purposes.

**Notation:**
SFR-ID/Iteration (e.g., FDP_ACC.1/User, FDP_ACC.1/Admin)

**Example:**
Separate access control policies for users and administrators

### Refinement

**Definition:**
Adding details to an SFR to make it more precise or restrictive.

**Notation:**
Italic text or [refinement: text]

**Example:**
Refinement of "user" to "authenticated user with role X"

### Selection

**Definition:**
Selecting one or more options from a predefined list in an SFR.

**Notation:**
[selection: Option A, Option B, Option C]

**Example:**
[selection: symmetric encryption, asymmetric encryption]

## Evaluation Terms

<!-- Define terms related to evaluation -->

### [TODO: Evaluation Term 1]

**Definition:**
[TODO: Define the evaluation term]

**Evaluation Context:**
[TODO: Explain the context in evaluation]

**Reference:**
[TODO: Reference ISO/IEC 18045 or other relevant documents]

### [TODO: Evaluation Term 2]

**Definition:**
[TODO: Definition]

**Evaluation Context:**
[TODO: Context]

**Reference:**
[TODO: Reference]

## References and Standards

<!-- List all referenced standards and documents -->

### ISO/IEC Standards

- **ISO/IEC 15408-1:** Information technology — Security techniques — Evaluation criteria for IT security — Part 1: Introduction and general model
- **ISO/IEC 15408-2:** Information technology — Security techniques — Evaluation criteria for IT security — Part 2: Security functional components
- **ISO/IEC 15408-3:** Information technology — Security techniques — Evaluation criteria for IT security — Part 3: Security assurance components
- **ISO/IEC 18045:** Information technology — Security techniques — Methodology for IT security evaluation

### Additional Standards

[TODO: List additional relevant standards]

- [TODO: Standard 1]
- [TODO: Standard 2]

## Terminology Consistency

<!-- Document rules for consistent terminology -->

### Preferred Terms

<!-- List preferred terms when multiple variants exist -->

| Preferred Term | Avoid | Justification |
|----------------|-------|---------------|
| TOE | Product, System | Official CC terminology |
| User | End-user, Operator | Consistency with English ST version |
| [TODO] | [TODO] | [TODO] |

### Capitalization

<!-- Define rules for capitalization -->

[TODO: Document conventions for capitalization of terms]

**Examples:**
- TOE (always uppercase)
- Security Target (capitalized as proper noun)
- [TODO: Additional examples]

## Change History

<!-- Document changes to the glossary -->

| Version | Date | Change | Author |
|---------|------|--------|--------|
| [TODO: 1.0] | [TODO: Date] | Initial version | [TODO: Name] |
| [TODO] | [TODO] | [TODO] | [TODO] |

---

**Next Steps:**
1. Identify all terms used in the ST
2. Define all TOE-specific terms
3. Define all technical and domain-specific terms
4. Create the abbreviations list
5. Verify terminology consistency throughout the ST
6. Update the glossary when changes are made to the ST
7. Have the glossary reviewed by subject matter experts
