# Protection Needs Assessment (Template)

**Document-ID:** [FRAMEWORK]-0060
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



## 1. Objective and Purpose

The protection needs assessment systematically determines the protection requirements for business processes, information, applications, and IT systems of **AdminSend GmbH**. It forms the basis for:
- Selection of appropriate security measures
- Prioritization of security investments
- Risk analysis (Document 0090)
- Compliance evidence

**Responsible:** [TODO] (ISB)

## 2. Protection Needs Categories and Criteria

### 2.1 Protection Objectives

The protection needs assessment is conducted for the following protection objectives:

#### 2.1.1 Confidentiality

Protection against unauthorized disclosure of information.

| Category | Description | Damage Examples |
|---|---|---|
| **Normal** | Limited negative impacts | Minor impairment, internal embarrassment |
| **High** | Considerable negative impacts | Violation of laws, significant financial damage, reputational damage |
| **Very High** | Existential impacts | Existential threat, catastrophic reputational damage, criminal consequences |

#### 2.1.2 Integrity

Protection against unauthorized modification of information.

| Category | Description | Damage Examples |
|---|---|---|
| **Normal** | Limited negative impacts | Correctable errors, minor impact on business processes |
| **High** | Considerable negative impacts | Significant business process disruptions, financial losses, compliance violations |
| **Very High** | Existential impacts | Critical business process failures, existential financial damage |

#### 2.1.3 Availability

Ensuring the availability of information and systems.

| Category | Description | Tolerable Downtime | Damage Examples |
|---|---|---|---|
| **Normal** | Limited negative impacts | > 24 hours | Minor productivity losses, inconveniences |
| **High** | Considerable negative impacts | 4-24 hours | Significant productivity losses, customer complaints, financial losses |
| **Very High** | Existential impacts | < 4 hours | Critical business process failures, massive financial losses, existential threat |

#### 2.1.4 Authenticity (Optional)

Ensuring the genuineness and credibility of information.

| Category | Description | Damage Examples |
|---|---|---|
| **Normal** | Limited negative impacts | Minor doubts about authenticity, correctable |
| **High** | Considerable negative impacts | Significant legal or financial consequences |
| **Very High** | Existential impacts | Existential legal or financial consequences |

#### 2.1.5 Accountability (Optional)

Ensuring the traceability of actions.

| Category | Description | Damage Examples |
|---|---|---|
| **Normal** | Limited negative impacts | Difficult troubleshooting, minor compliance risks |
| **High** | Considerable negative impacts | Compliance violations, difficult incident investigation |
| **Very High** | Existential impacts | Severe compliance violations, impossible incident investigation |

### 2.2 Assessment Scale

**Assessment Criteria:**
- Legal and regulatory requirements (GDPR, IT Security Act, etc.)
- Contractual obligations
- Business criticality
- Financial impacts
- Reputational risks
- Personal data
- Trade secrets

## 3. Protection Needs Assessment

### 3.1 Business Processes



| Process ID | Process | Owner | C | I | A | Justification | Overall Protection Need |
|---|---|---|---|---|---|---|---|
| P-001 | [TODO: Process 1] | [TODO] | Normal/High/Very High | Normal/High/Very High | Normal/High/Very High | [TODO: Justification] | [TODO: Maximum Principle] |
| P-002 | [TODO: Process 2] | [TODO] | Normal/High/Very High | Normal/High/Very High | Normal/High/Very High | [TODO] | [TODO] |
| P-003 | [TODO: Process 3] | [TODO] | Normal/High/Very High | Normal/High/Very High | Normal/High/Very High | [TODO] | [TODO] |

**Total Number of Processes:** [TODO]  
**Distribution:**
- Normal: [TODO]
- High: [TODO]
- Very High: [TODO]

### 3.2 Information and Data

| Info ID | Information/Data Type | Process | C | I | A | Justification | Overall Protection Need |
|---|---|---|---|---|---|---|---|
| I-001 | Personal Data (GDPR) | [TODO] | High | High | Normal | GDPR requirements | High |
| I-002 | Trade Secrets | [TODO] | Very High | High | Normal | Competitive advantage | Very High |
| I-003 | Financial Data | [TODO] | High | Very High | High | Legal requirements | Very High |
| I-004 | [TODO: Additional Data] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

**Total Number of Information Types:** [TODO]

### 3.3 Applications

| Application ID | Application | Process | C | I | A | Justification | Overall Protection Need |
|---|---|---|---|---|---|---|---|
| A-001 | [TODO: Application 1] | P-001 | [TODO] | [TODO] | [TODO] | Inherited from Process P-001 | [TODO] |
| A-002 | [TODO: Application 2] | P-002 | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| A-003 | [TODO: Application 3] | P-003 | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

**Total Number of Applications:** [TODO]

### 3.4 IT Systems and Components

| System ID | System/Component | Application | C | I | A | Justification | Overall Protection Need |
|---|---|---|---|---|---|---|---|
| S-001 | [[ netbox.device.server_001 ]] | A-001 | [TODO] | [TODO] | [TODO] | Inherited from Application A-001 | [TODO] |
| S-002 | [TODO: System 2] | A-002 | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| S-003 | [TODO: System 3] | A-003 | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

**Total Number of IT Systems:** [TODO]

### 3.5 Networks

| Network ID | Network/Zone | Systems | C | I | A | Justification | Overall Protection Need |
|---|---|---|---|---|---|---|---|
| N-001 | Management Network | S-001, S-002 | Very High | Very High | High | Critical administrative access | Very High |
| N-002 | Production Network | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| N-003 | DMZ | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

**Total Number of Networks:** [TODO]

### 3.6 Rooms and Locations

| Room ID | Room/Location | Systems | C | I | A | Justification | Overall Protection Need |
|---|---|---|---|---|---|---|---|
| R-001 | Data Center | All critical servers | Very High | Very High | Very High | Hosting critical systems | Very High |
| R-002 | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

**Total Number of Rooms:** [TODO]

## 4. Protection Needs Inheritance and Dependencies

### 4.1 Inheritance Principle

Protection needs are inherited according to the **Maximum Principle**:

```
Business Process
    ↓ (inherits protection need)
Information
    ↓ (inherits protection need)
Applications
    ↓ (inherits protection need)
IT Systems
    ↓ (inherits protection need)
Networks, Rooms
```

**Example:**
- Process P-001 has protection need "Very High" for confidentiality
- Application A-001 supports Process P-001
- → Application A-001 inherits protection need "Very High" for confidentiality
- Server S-001 hosts Application A-001
- → Server S-001 inherits protection need "Very High" for confidentiality

### 4.2 Inheritance Table

| From (Source) | To (Target) | Inherited Protection Need | Justification |
|---|---|---|---|
| P-001 | A-001 | C: Very High, I: High, A: High | Application supports critical process |
| A-001 | S-001 | C: Very High, I: High, A: High | Server hosts critical application |
| [TODO] | [TODO] | [TODO] | [TODO] |

### 4.3 Exceptions and Justifications

**Exceptions to the Maximum Principle:**

| Object | Expected Protection Need | Actual Protection Need | Justification | Approved By |
|---|---|---|---|---|
| [TODO: Object] | [TODO] | [TODO] | [TODO: Justification for deviation] | [TODO] |

**Important:** Exceptions must be documented and approved.

### 4.4 Cumulative Effects

When a system hosts multiple applications with different protection needs, the **Maximum Principle** applies:

| System | Application 1 | Application 2 | Application 3 | Resulting Protection Need |
|---|---|---|---|---|
| S-001 | C: High | C: Very High | C: Normal | C: Very High (Maximum) |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## 5. Validation and Quality Assurance

### 5.1 Validation Process

The protection needs assessment is validated by:

1. **Review by Process Owners:** Confirmation of business criticality
2. **Review by IT Management:** [TODO] - Technical feasibility
3. **Review by Legal/Compliance:** Legal requirements
4. **Review by Data Protection:** GDPR compliance
5. **Approval by ISB:** [TODO]

### 5.2 Consistency Check

| Check Criterion | Status | Comments |
|---|---|---|
| All processes assessed | [TODO: ✓/✗] | [TODO] |
| All applications assessed | [TODO: ✓/✗] | [TODO] |
| All IT systems assessed | [TODO: ✓/✗] | [TODO] |
| Inheritance consistent | [TODO: ✓/✗] | [TODO] |
| Exceptions documented | [TODO: ✓/✗] | [TODO] |
| Justifications complete | [TODO: ✓/✗] | [TODO] |

## 6. Impact on Security Measures

### 6.1 Measures by Protection Need

| Protection Need | Exemplary Measures |
|---|---|
| **Normal** | Standard security measures, basic hardening, standard backup |
| **High** | Enhanced security measures, encryption, MFA, extended monitoring, redundant systems |
| **Very High** | Maximum security measures, end-to-end encryption, hardware tokens, 24/7 monitoring, high availability, disaster recovery |

### 6.2 Prioritization of Measures

Security measures are prioritized according to:
1. **Very High Protection Need:** Highest priority
2. **High Protection Need:** High priority
3. **Normal Protection Need:** Normal priority

## 7. Documentation and Evidence

The following documents and evidence are maintained:
- This protection needs assessment document
- Assessment workshop protocols
- Process owner approvals
- Exception approvals
- Change logs

## 8. Update and Maintenance

The protection needs assessment is updated when:
- New business processes or applications are introduced
- Significant changes to existing processes occur
- New legal requirements emerge
- Security incidents occur
- At least annually as part of the ISMS review

**Responsible:** [TODO] (ISB)  
**Next Review:** [TODO]

## 9. Approval

| Role | Name | Date | Approval |
|---|---|---|---|
| ISB | [TODO] | [TODO] | Draft |
| IT Management | [TODO] | [TODO] | Draft |
| Executive Management | [TODO] | [TODO] | Draft |

**References:**
- BSI Standard 200-2: IT-Grundschutz Methodology (Chapter 6: Protection Needs Assessment)
- BSI IT-Grundschutz Compendium

