# Threat Agents and Assets

**Document-ID:** 0240
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
This template documents threat agents and assets to be protected according to ISO/IEC 15408-1:2022.
It describes in detail who potential attackers are and which assets must be protected.

Customization required:
- Identify all relevant threat agents
- Describe capabilities, motivation, and resources of each agent
- Identify all assets to be protected
- Classify assets by value and protection needs
- Document asset dependencies
- Assess attack potential

Reference: ISO/IEC 15408-1:2022, Section 8.3 (Security Problem Definition)
-->

## 1. Overview

### 1.1 Purpose
This document defines:
- **Threat Agents**: Potential attackers with their capabilities and motivations
- **Assets**: Resources, data, and functions to be protected

### 1.2 Scope
**In Scope:**
[TODO: What is covered in this document?]

**Out of Scope:**
[TODO: What is not covered?]

## 2. Assets

### 2.1 Asset Identification

#### 2.1.1 Asset Categories
**Asset Categories:**
- **Data Assets**: Data and information
- **Service Assets**: Services and functions
- **System Assets**: System components and infrastructure
- **Credential Assets**: Authentication and authorization data
- **Configuration Assets**: Configuration data and settings

#### 2.1.2 Asset Inventory
**Asset Inventory:**

| Asset ID | Asset Name | Category | Owner | Location | Description |
|----------|------------|----------|-------|----------|-------------|
| [TODO: A.001] | [TODO: Name] | [TODO: Data/Service/System] | [TODO: Owner] | [TODO: Location] | [TODO: Description] |
| [TODO: A.002] | [TODO: Name] | [TODO: Category] | [TODO: Owner] | [TODO: Location] | [TODO: Description] |
| [TODO: A.003] | [TODO: Name] | [TODO: Category] | [TODO: Owner] | [TODO: Location] | [TODO: Description] |

### 2.2 Data Assets

#### A.USER_DATA
**Asset ID:** A.USER_DATA  
**Category:** Data  
**Type:** [TODO: Personal Data / Business Data / Technical Data]

**Description:**
[TODO: User data including personal information, preferences, and profile data]

**Properties:**
- **Confidentiality:** [TODO: High/Medium/Low]
- **Integrity:** [TODO: High/Medium/Low]
- **Availability:** [TODO: High/Medium/Low]
- **Data Volume:** [TODO: e.g., 1 TB]
- **Data Format:** [TODO: e.g., JSON, XML, Database]

**Protection Needs:**
- **Confidentiality:** [TODO: Rationale for protection need]
- **Integrity:** [TODO: Rationale for protection need]
- **Availability:** [TODO: Rationale for protection need]

**Regulatory Requirements:**
- [TODO: GDPR Article 32 - Security of processing]
- [TODO: HIPAA §164.312 - Technical safeguards]
- [TODO: Additional requirements]

**Value:**
- **Business Value:** [TODO: High/Medium/Low]
- **Monetary Value:** [TODO: Estimate]
- **Reputation Value:** [TODO: High/Medium/Low]

**Lifecycle:**
- **Creation:** [TODO: How is data created?]
- **Storage:** [TODO: Where is data stored?]
- **Processing:** [TODO: How is data processed?]
- **Transmission:** [TODO: How is data transmitted?]
- **Archiving:** [TODO: How is data archived?]
- **Deletion:** [TODO: How is data deleted?]

#### A.AUTHENTICATION_DATA
**Asset ID:** A.AUTHENTICATION_DATA  
**Category:** Credential  
**Type:** [TODO: Passwords / Tokens / Certificates]

**Description:**
[TODO: Authentication data such as passwords, tokens, certificates]

[TODO: Add more Data Assets]

### 2.3 Service Assets

#### A.AUTHENTICATION_SERVICE
**Asset ID:** A.AUTHENTICATION_SERVICE  
**Category:** Service  
**Type:** [TODO: Authentication / Authorization / Identity Management]

**Description:**
[TODO: Authentication service that verifies user identities]

**Properties:**
- **Availability:** [TODO: 99.9% SLA]
- **Performance:** [TODO: < 100ms Response Time]
- **Capacity:** [TODO: 1000 req/sec]

**Protection Needs:**
- **Availability:** [TODO: High - Critical for system access]
- **Integrity:** [TODO: High - False authentication compromises security]
- **Confidentiality:** [TODO: Medium - Metadata can be sensitive]

**Dependencies:**
- [TODO: A.AUTHENTICATION_DATA]
- [TODO: A.USER_DATABASE]
- [TODO: A.NETWORK_CONNECTIVITY]

**Value:**
- **Business Value:** [TODO: High - Fundamental security function]
- **Criticality:** [TODO: High - System unusable without authentication]

#### A.DATA_PROCESSING_SERVICE
**Asset ID:** A.DATA_PROCESSING_SERVICE  
**Category:** Service  
**Type:** [TODO: Processing / Computation / Transformation]

**Description:**
[TODO: Service for processing business data]

[TODO: Add more Service Assets]

### 2.4 System Assets

#### A.TOE_PLATFORM
**Asset ID:** A.TOE_PLATFORM  
**Category:** System  
**Type:** [TODO: Hardware / Software / Firmware]

**Description:**
[TODO: The platform on which the TOE runs]

**Components:**
- [TODO: Operating system]
- [TODO: Hardware platform]
- [TODO: Virtualization layer]
- [TODO: Container runtime]

**Protection Needs:**
- **Availability:** [TODO: High]
- **Integrity:** [TODO: High]
- **Confidentiality:** [TODO: Medium]

**Criticality:**
[TODO: High - Platform compromise endangers all assets]

#### A.CRYPTOGRAPHIC_KEYS
**Asset ID:** A.CRYPTOGRAPHIC_KEYS  
**Category:** System  
**Type:** [TODO: Encryption Keys / Signing Keys / Certificates]

**Description:**
[TODO: Cryptographic keys for encryption and signing]

[TODO: Add more System Assets]

### 2.5 Asset Classification

#### 2.5.1 Classification Scheme
**Classification Scheme:**

| Classification | Confidentiality | Integrity | Availability | Examples |
|----------------|----------------|-----------|--------------|----------|
| **Critical** | High | High | High | [TODO: A.001, A.003] |
| **High** | High | High | Medium | [TODO: A.002, A.005] |
| **Medium** | Medium | Medium | Medium | [TODO: A.004, A.006] |
| **Low** | Low | Low | Low | [TODO: A.007] |

#### 2.5.2 Asset Value Matrix
**Asset Value Matrix:**

| Asset ID | Business Value | Regulatory Value | Reputation Value | Total Value |
|----------|---------------|------------------|------------------|-------------|
| [TODO: A.001] | [TODO: High] | [TODO: High] | [TODO: High] | [TODO: Critical] |
| [TODO: A.002] | [TODO: Medium] | [TODO: High] | [TODO: Medium] | [TODO: High] |

### 2.6 Asset Dependencies

#### 2.6.1 Dependency Graph
**Asset Dependencies:**

[TODO: Create a diagram showing asset dependencies]

```
[TODO: Insert asset dependency diagram]
```

#### 2.6.2 Dependency Matrix
**Dependency Matrix:**

| Asset | Depends On | Impact if Unavailable |
|-------|------------|----------------------|
| [TODO: A.001] | [TODO: A.003, A.005] | [TODO: Service unavailable] |
| [TODO: A.002] | [TODO: A.004] | [TODO: Data processing not possible] |

## 3. Threat Agents

### 3.1 Threat Agent Identification

#### 3.1.1 Agent Categories
**Agent Categories:**
- **External Attackers**: External attackers without legitimate access
- **Insiders**: Employees with legitimate access
- **Privileged Insiders**: Administrators with privileged access
- **Nation-State Actors**: State-sponsored attackers
- **Organized Crime**: Organized crime
- **Hacktivists**: Ideologically motivated attackers
- **Script Kiddies**: Inexperienced attackers with pre-made tools

#### 3.1.2 Agent Inventory
**Agent Inventory:**

| Agent ID | Agent Type | Motivation | Capability | Resources | Description |
|----------|------------|------------|------------|-----------|-------------|
| [TODO: TA.001] | [TODO: External Attacker] | [TODO: Financial] | [TODO: High] | [TODO: High] | [TODO: Description] |
| [TODO: TA.002] | [TODO: Insider] | [TODO: Revenge] | [TODO: Medium] | [TODO: Medium] | [TODO: Description] |
| [TODO: TA.003] | [TODO: Nation-State] | [TODO: Espionage] | [TODO: Very High] | [TODO: Very High] | [TODO: Description] |

### 3.2 Threat Agent Profiles

#### TA.EXTERNAL_ATTACKER
**Agent ID:** TA.EXTERNAL_ATTACKER  
**Type:** External Attacker  
**Skill Level:** [TODO: Expert / Proficient / Layman]

**Description:**
[TODO: External attacker without legitimate system access attempting to intrude via network or other external interfaces]

**Motivation:**
- **Primary:** [TODO: e.g., Financial gain, data theft]
- **Secondary:** [TODO: e.g., Reputation, challenge]

**Capabilities:**
- **Technical Expertise:** [TODO: High - Knowledge in network security, exploitation]
- **Tools:** [TODO: Metasploit, Burp Suite, Custom Scripts]
- **Knowledge:** [TODO: Publicly available information, OSINT]
- **Access:** [TODO: Network access, no physical access]

**Resources:**
- **Time:** [TODO: Weeks to months]
- **Budget:** [TODO: $10,000 - $100,000]
- **Team:** [TODO: 1-5 people]
- **Infrastructure:** [TODO: Cloud resources, botnets]

**Attack Vectors:**
- [TODO: Network attacks (SQL Injection, XSS, etc.)]
- [TODO: Social engineering (phishing)]
- [TODO: Exploitation of known vulnerabilities]
- [TODO: Brute-force attacks]
- [TODO: DDoS attacks]

**Attack Potential:**
[TODO: High - Based on CCRA Attack Potential Methodology]

**Example Scenarios:**
1. [TODO: Scenario 1]
2. [TODO: Scenario 2]

#### TA.MALICIOUS_INSIDER
**Agent ID:** TA.MALICIOUS_INSIDER  
**Type:** Insider  
**Skill Level:** [TODO: Expert / Proficient / Layman]

**Description:**
[TODO: Malicious employee with legitimate system access]

**Motivation:**
- **Primary:** [TODO: e.g., Revenge, financial gain]
- **Secondary:** [TODO: e.g., Ideology, blackmail]

**Capabilities:**
- **Technical Expertise:** [TODO: Medium - Basic IT knowledge]
- **Tools:** [TODO: Standard user tools, USB drives]
- **Knowledge:** [TODO: Insider knowledge of systems and processes]
- **Access:** [TODO: Legitimate user access, physical access]

**Resources:**
- **Time:** [TODO: Days to weeks]
- **Budget:** [TODO: Minimal]
- **Team:** [TODO: Individual]
- **Infrastructure:** [TODO: Company resources]

**Attack Vectors:**
- [TODO: Data exfiltration via USB or email]
- [TODO: Sabotage of systems or data]
- [TODO: Abuse of access rights]
- [TODO: Sharing credentials with external parties]

**Attack Potential:**
[TODO: Medium-High - Insider access compensates for lower technical skills]

#### TA.PRIVILEGED_ADMIN
**Agent ID:** TA.PRIVILEGED_ADMIN  
**Type:** Privileged Insider  
**Skill Level:** [TODO: Expert]

**Description:**
[TODO: Malicious administrator with privileged access]

**Motivation:**
- **Primary:** [TODO: e.g., Financial gain, blackmail]
- **Secondary:** [TODO: e.g., Revenge, ideology]

**Capabilities:**
- **Technical Expertise:** [TODO: High - Deep system understanding]
- **Tools:** [TODO: Administrative tools, root access]
- **Knowledge:** [TODO: Complete insider knowledge, access to documentation]
- **Access:** [TODO: Privileged access, physical access]

**Resources:**
- **Time:** [TODO: Hours to days]
- **Budget:** [TODO: Minimal]
- **Team:** [TODO: Individual]
- **Infrastructure:** [TODO: Full access to company resources]

**Attack Vectors:**
- [TODO: Direct data manipulation]
- [TODO: Disabling security mechanisms]
- [TODO: Creating backdoors]
- [TODO: Manipulating audit logs]
- [TODO: Privilege escalation for other accounts]

**Attack Potential:**
[TODO: Very High - Privileged access enables almost all attacks]

#### TA.NATION_STATE
**Agent ID:** TA.NATION_STATE  
**Type:** Nation-State Actor  
**Skill Level:** [TODO: Expert]

**Description:**
[TODO: State-sponsored attacker with extensive resources]

[TODO: Add more Threat Agents]

### 3.3 Attack Potential Assessment

#### 3.3.1 CCRA Methodology
**Common Criteria Recognition Arrangement (CCRA) Attack Potential:**

| Factor | Level | Points | Description |
|--------|-------|--------|-------------|
| **Elapsed Time** | < 1 day | 0 | [TODO] |
| | < 1 week | 1 | [TODO] |
| | < 1 month | 4 | [TODO] |
| | < 6 months | 10 | [TODO] |
| | > 6 months | 17 | [TODO] |
| **Expertise** | Layman | 0 | [TODO] |
| | Proficient | 3 | [TODO] |
| | Expert | 6 | [TODO] |
| **Knowledge** | Public | 0 | [TODO] |
| | Restricted | 3 | [TODO] |
| | Sensitive | 7 | [TODO] |
| **Window of Opportunity** | Unnecessary | 0 | [TODO] |
| | Easy | 1 | [TODO] |
| | Moderate | 4 | [TODO] |
| | Difficult | 10 | [TODO] |
| **Equipment** | Standard | 0 | [TODO] |
| | Specialized | 4 | [TODO] |
| | Bespoke | 7 | [TODO] |

#### 3.3.2 Attack Potential Ratings
**Attack Potential Ratings:**

| Agent ID | Elapsed Time | Expertise | Knowledge | Window | Equipment | Total | Rating |
|----------|--------------|-----------|-----------|--------|-----------|-------|--------|
| [TODO: TA.001] | [TODO: 4] | [TODO: 6] | [TODO: 3] | [TODO: 1] | [TODO: 4] | [TODO: 18] | [TODO: Moderate] |
| [TODO: TA.002] | [TODO: 1] | [TODO: 3] | [TODO: 7] | [TODO: 0] | [TODO: 0] | [TODO: 11] | [TODO: Enhanced-Basic] |

**Rating Scale:**
- **0-9 points:** Basic
- **10-13 points:** Enhanced-Basic
- **14-19 points:** Moderate
- **20-24 points:** High
- **≥25 points:** Beyond High

### 3.4 Threat Agent Capabilities Matrix

**Capabilities Matrix:**

| Agent | Network Access | Physical Access | Insider Knowledge | Technical Skills | Resources | Persistence |
|-------|---------------|-----------------|-------------------|------------------|-----------|-------------|
| [TODO: TA.001] | [TODO: Yes] | [TODO: No] | [TODO: No] | [TODO: High] | [TODO: High] | [TODO: High] |
| [TODO: TA.002] | [TODO: Yes] | [TODO: Yes] | [TODO: Yes] | [TODO: Medium] | [TODO: Low] | [TODO: Medium] |
| [TODO: TA.003] | [TODO: Yes] | [TODO: No] | [TODO: No] | [TODO: Expert] | [TODO: Very High] | [TODO: Very High] |

## 4. Asset-Agent Relationships

### 4.1 Asset-Agent Threat Matrix
**Which agents threaten which assets:**

| Asset | TA.001 | TA.002 | TA.003 | TA.004 | TA.005 |
|-------|--------|--------|--------|--------|--------|
| [TODO: A.001] | [TODO: High] | [TODO: Medium] | [TODO: High] | [TODO: Low] | [TODO: Medium] |
| [TODO: A.002] | [TODO: Medium] | [TODO: High] | [TODO: Medium] | [TODO: Low] | [TODO: Low] |

### 4.2 High-Risk Combinations
**High-Risk Combinations:**

| Asset | Agent | Risk Level | Rationale |
|-------|-------|------------|-----------|
| [TODO: A.001] | [TODO: TA.003] | [TODO: Critical] | [TODO: High-value data + highly skilled attacker] |
| [TODO: A.002] | [TODO: TA.002] | [TODO: High] | [TODO: Critical service + insider access] |

## 5. Summary

### 5.1 Asset Summary
**Asset Summary:**
- Total number of assets: [TODO: Number]
- Critical assets: [TODO: Number]
- High-value assets: [TODO: Number]
- Medium-value assets: [TODO: Number]
- Low-value assets: [TODO: Number]

### 5.2 Threat Agent Summary
**Agent Summary:**
- Total number of agents: [TODO: Number]
- External attackers: [TODO: Number]
- Insiders: [TODO: Number]
- Privileged insiders: [TODO: Number]
- Nation-state actors: [TODO: Number]
- Other: [TODO: Number]

### 5.3 Risk Overview
**Risk Overview:**
- Critical risk combinations: [TODO: Number]
- High risk combinations: [TODO: Number]
- Medium risk combinations: [TODO: Number]
- Low risk combinations: [TODO: Number]

**Next Steps:**
1. Complete all [TODO] placeholders with TOE-specific assets and agents
2. Conduct complete asset identification
3. Document all relevant threat agents
4. Assess attack potential for all agents
5. Create asset dependency diagrams
6. Verify consistency with Threats (Template 0210) and Security Objectives (Template 0300)

