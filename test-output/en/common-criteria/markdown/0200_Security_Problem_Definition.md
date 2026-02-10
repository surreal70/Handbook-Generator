# Security Problem Definition

**Document-ID:** 0200  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** Draft  
**Classification:** Confidential  
**Last Update:** {{ meta.date }}  

---



## 1. Security Problem Overview

### 1.1 Purpose
This document defines the security problem that the TOE shall solve. It describes:
- **Threats**: Potential attacks and security violations
- **Organizational Security Policies (OSPs)**: Security policies that must be enforced
- **Assumptions**: Expectations about the operational environment

### 1.2 Security Problem Context
**Application Context:**
[TODO: Describe the context in which the TOE is deployed]

**Security-Relevant Factors:**
- [TODO: Factor 1]
- [TODO: Factor 2]
- [TODO: Factor 3]

### 1.3 Security Problem Scope
**In Scope:**
- [TODO: What is covered by the security problem definition]

**Out of Scope:**
- [TODO: What is not covered]

## 2. Assets

### 2.1 Asset Identification
**Assets to be Protected:**

| Asset ID | Asset Name | Type | Value | Description |
|----------|------------|------|-------|-------------|
| [TODO: A.001] | [TODO: Asset Name] | Data/Service/Function | High/Medium/Low | [TODO: Description] |
| [TODO: A.002] | [TODO: Asset Name] | Data/Service/Function | High/Medium/Low | [TODO: Description] |
| [TODO: A.003] | [TODO: Asset Name] | Data/Service/Function | High/Medium/Low | [TODO: Description] |

### 2.2 Asset Classification
**Data Assets:**
- [TODO: Data Asset 1]: [TODO: Classification and protection needs]
- [TODO: Data Asset 2]: [TODO: Classification and protection needs]

**Service Assets:**
- [TODO: Service Asset 1]: [TODO: Availability requirements]
- [TODO: Service Asset 2]: [TODO: Availability requirements]

**Function Assets:**
- [TODO: Function Asset 1]: [TODO: Integrity requirements]
- [TODO: Function Asset 2]: [TODO: Integrity requirements]

### 2.3 Asset Dependencies
[TODO: Describe dependencies between assets]

```
[TODO: Insert asset dependency diagram]
```

## 3. Threat Agents

### 3.1 Threat Agent Profiles
**Identified Threat Agents:**

| Agent ID | Agent Type | Motivation | Capability | Resources | Description |
|----------|------------|------------|------------|-----------|-------------|
| [TODO: TA.001] | [TODO: e.g., Insider, External Attacker] | [TODO: Motivation] | High/Medium/Low | High/Medium/Low | [TODO: Description] |
| [TODO: TA.002] | [TODO: Type] | [TODO: Motivation] | High/Medium/Low | High/Medium/Low | [TODO: Description] |

### 3.2 Threat Agent Capabilities
**[TODO: Threat Agent 1]**
- **Capabilities**: [TODO: e.g., Network access, physical access, insider knowledge]
- **Resources**: [TODO: e.g., Time, budget, tools]
- **Motivation**: [TODO: e.g., Financial gain, sabotage, espionage]
- **Attack Vectors**: [TODO: Possible attack paths]

**[TODO: Threat Agent 2]**
- [TODO: Details]

### 3.3 Attack Potential
**Attack Potential Assessment:**

| Agent | Elapsed Time | Expertise | Knowledge | Window of Opportunity | Equipment | Attack Potential |
|-------|--------------|-----------|-----------|----------------------|-----------|------------------|
| [TODO: TA.001] | [TODO: < 1 day / < 1 month / > 1 month] | [TODO: Layman / Proficient / Expert] | [TODO: Public / Restricted / Sensitive] | [TODO: Unnecessary / Easy / Moderate / Difficult] | [TODO: Standard / Specialized / Bespoke] | [TODO: Basic / Enhanced-Basic / Moderate / High] |

## 4. Threats

### 4.1 Threat Catalog
**Identified Threats:**

| Threat ID | Threat Name | Asset | Agent | Likelihood | Impact | Risk | Description |
|-----------|-------------|-------|-------|------------|--------|------|-------------|
| [TODO: T.001] | [TODO: Threat Name] | [TODO: A.001] | [TODO: TA.001] | High/Medium/Low | High/Medium/Low | High/Medium/Low | [TODO: Description] |
| [TODO: T.002] | [TODO: Threat Name] | [TODO: A.002] | [TODO: TA.002] | High/Medium/Low | High/Medium/Low | High/Medium/Low | [TODO: Description] |

### 4.2 Threat Details

#### T.001: [TODO: Threat Name]
**Description:**
[TODO: Detailed description of the threat]

**Affected Assets:**
- [TODO: Asset 1]
- [TODO: Asset 2]

**Threat Agent:**
- [TODO: TA.001]

**Attack Scenario:**
1. [TODO: Step 1]
2. [TODO: Step 2]
3. [TODO: Step 3]

**Impact:**
- Confidentiality: [TODO: High/Medium/Low/None]
- Integrity: [TODO: High/Medium/Low/None]
- Availability: [TODO: High/Medium/Low/None]

**Likelihood:** [TODO: High/Medium/Low]

**Risk Assessment:** [TODO: High/Medium/Low]

---

#### T.002: [TODO: Threat Name]
[TODO: Repeat structure for each threat]

### 4.3 Threat Scenarios
**Attack Scenario 1: [TODO: Scenario Name]**
[TODO: Describe a complete attack scenario]

**Attack Scenario 2: [TODO: Scenario Name]**
[TODO: Describe another attack scenario]

## 5. Organizational Security Policies

### 5.1 OSP Catalog
**Organizational Security Policies:**

| OSP ID | OSP Name | Category | Mandatory | Description |
|--------|----------|----------|-----------|-------------|
| [TODO: P.001] | [TODO: Policy Name] | [TODO: e.g., Access Control, Audit, Crypto] | Yes/No | [TODO: Description] |
| [TODO: P.002] | [TODO: Policy Name] | [TODO: Category] | Yes/No | [TODO: Description] |

### 5.2 OSP Details

#### P.001: [TODO: Policy Name]
**Description:**
[TODO: Detailed description of the policy]

**Purpose:**
[TODO: Why is this policy required?]

**Requirements:**
- [TODO: Requirement 1]
- [TODO: Requirement 2]
- [TODO: Requirement 3]

**Scope:**
[TODO: Where does this policy apply?]

**Compliance Requirements:**
[TODO: External standards or regulations this policy fulfills]

---

#### P.002: [TODO: Policy Name]
[TODO: Repeat structure for each OSP]

### 5.3 Policy Compliance Matrix
**Mapping of Policies to External Standards:**

| OSP ID | ISO 27001 | NIST 800-53 | PCI-DSS | GDPR | Other |
|--------|-----------|-------------|---------|------|-------|
| [TODO: P.001] | [TODO: Control] | [TODO: Control] | [TODO: Req] | [TODO: Article] | [TODO: Standard] |
| [TODO: P.002] | [TODO: Control] | [TODO: Control] | [TODO: Req] | [TODO: Article] | [TODO: Standard] |

## 6. Assumptions

### 6.1 Assumption Catalog
**Assumptions about the Operational Environment:**

| Assumption ID | Assumption Name | Category | Criticality | Description |
|---------------|-----------------|----------|-------------|-------------|
| [TODO: A.001] | [TODO: Assumption Name] | [TODO: e.g., Physical, Personnel, Connectivity] | High/Medium/Low | [TODO: Description] |
| [TODO: A.002] | [TODO: Assumption Name] | [TODO: Category] | High/Medium/Low | [TODO: Description] |

### 6.2 Assumption Details

#### A.001: [TODO: Assumption Name]
**Description:**
[TODO: Detailed description of the assumption]

**Rationale:**
[TODO: Why is this assumption justified?]

**Impact:**
[TODO: What happens if this assumption is not met?]

**Responsibility:**
[TODO: Who is responsible for fulfilling this assumption?]

**Verification:**
[TODO: How can it be verified that this assumption is met?]

---

#### A.002: [TODO: Assumption Name]
[TODO: Repeat structure for each assumption]

### 6.3 Environmental Assumptions
**Physical Environment:**
- [TODO: Assumption about physical security]
- [TODO: Assumption about environmental conditions]

**Personnel:**
- [TODO: Assumption about user behavior]
- [TODO: Assumption about administrator competence]

**Connectivity:**
- [TODO: Assumption about network security]
- [TODO: Assumption about communication channels]

## 7. Security Problem Summary

### 7.1 Threat Summary
**Threat Summary:**
- Number of identified threats: [TODO: Number]
- High-risk threats: [TODO: Number]
- Medium-risk threats: [TODO: Number]
- Low-risk threats: [TODO: Number]

### 7.2 OSP Summary
**Policy Summary:**
- Number of organizational security policies: [TODO: Number]
- Mandatory policies: [TODO: Number]
- Optional policies: [TODO: Number]

### 7.3 Assumption Summary
**Assumption Summary:**
- Number of assumptions: [TODO: Number]
- Critical assumptions: [TODO: Number]
- Medium criticality assumptions: [TODO: Number]
- Low criticality assumptions: [TODO: Number]

### 7.4 Coverage Analysis
**Coverage Analysis:**
[TODO: Analyze whether all assets are covered by threats, OSPs, or assumptions]

## 8. Traceability

### 8.1 Asset-to-Threat Mapping
**Mapping of Assets to Threats:**

| Asset ID | Threats |
|----------|---------|
| [TODO: A.001] | [TODO: T.001, T.003, T.005] |
| [TODO: A.002] | [TODO: T.002, T.004] |

### 8.2 Threat-to-Agent Mapping
**Mapping of Threats to Agents:**

| Threat ID | Threat Agents |
|-----------|---------------|
| [TODO: T.001] | [TODO: TA.001, TA.002] |
| [TODO: T.002] | [TODO: TA.003] |

### 8.3 Security Problem Traceability Matrix
**Complete Traceability:**

| Asset | Threat | OSP | Assumption | Agent |
|-------|--------|-----|------------|-------|
| [TODO: A.001] | [TODO: T.001] | [TODO: P.001] | [TODO: A.001] | [TODO: TA.001] |
| [TODO: A.002] | [TODO: T.002] | [TODO: P.002] | [TODO: A.002] | [TODO: TA.002] |

---

**Next Steps:**
1. Complete all [TODO] placeholders with TOE-specific information
2. Conduct complete threat analysis
3. Document all relevant OSPs
4. Identify and validate all assumptions
5. Create threat model and attack scenarios
6. Verify consistency with Security Objectives (Template 0300)

