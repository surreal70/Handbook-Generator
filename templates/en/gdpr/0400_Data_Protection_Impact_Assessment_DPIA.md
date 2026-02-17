# Data Protection Impact Assessment (DPIA)

**Document-ID:** 0400
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
This template documents the Data Protection Impact Assessment according to Art. 35 GDPR.
It describes when a DPIA is required and how to conduct it.

Customization required:
- Identify processing requiring DPIA
- Conduct systematic risk assessment
- Document measures for risk mitigation
- Consult Data Protection Officer
- Consult supervisory authority for high-risk processing

Reference: GDPR Art. 35 (Data protection impact assessment), Art. 36 (Prior consultation)
-->

## Purpose

This document describes the Data Protection Impact Assessment (DPIA) process at {{ meta-organisation.name }} according to Art. 35 GDPR. A DPIA is required when processing is likely to result in a high risk to the rights and freedoms of natural persons.

## Requirement for DPIA (Art. 35(1))

### Principle

A DPIA is required when a type of processing, in particular using new technologies, is likely to result in a high risk to the rights and freedoms of natural persons, considering the nature, scope, context and purposes of the processing.

### Mandatory Cases (Art. 35(3))

A DPIA is required in particular for:

#### a) Systematic and Extensive Evaluation of Personal Aspects (Art. 35(3)(a))

**Examples:**
- Profiling with automated decisions having legal effect
- Scoring procedures (creditworthiness, health risk)
- Behavior-based advertising with comprehensive tracking

**Status for our organization:** [TODO: Applicable Yes/No]

#### b) Large-Scale Processing of Special Categories (Art. 35(3)(b))

**Special Categories (Art. 9):**
- Health data
- Genetic/biometric data
- Racial/ethnic origin
- Political opinions
- Religious beliefs
- Trade union membership
- Sex life/sexual orientation

**Status for our organization:** [TODO: Applicable Yes/No]

#### c) Systematic Large-Scale Monitoring of Publicly Accessible Areas (Art. 35(3)(c))

**Examples:**
- Video surveillance with facial recognition
- Tracking of movement profiles
- Comprehensive location data collection

**Status for our organization:** [TODO: Applicable Yes/No]

### Supervisory Authority Blacklist (Art. 35(4))

The supervisory authority establishes a list of processing operations for which a DPIA must be conducted.

**Relevant entries for our organization:**
- [TODO: Check list of competent supervisory authority]
- [TODO: Document applicable entries]

### Supervisory Authority Whitelist (Art. 35(5))

The supervisory authority may establish a list of processing operations for which no DPIA is required.

**Relevant entries for our organization:**
- [TODO: Check list of competent supervisory authority]
- [TODO: Document applicable entries]

### Additional Criteria (WP29 Guidelines)

**Additional indicators for high risk:**

| Criterion | Description | Applicable |
|-----------|-------------|------------|
| Evaluation or Scoring | Profiling, prediction of behavior | Yes/No |
| Automated Decisions | With legal or similar effect | Yes/No |
| Systematic Monitoring | Continuous observation | Yes/No |
| Sensitive Data | Special categories (Art. 9) | Yes/No |
| Large-Scale Processing | Many data subjects or large data volumes | Yes/No |
| Matching or Combining | Datasets from different sources | Yes/No |
| Vulnerable Data Subjects | Children, employees, patients | Yes/No |
| Innovative Use | New technologies or applications | Yes/No |
| Denial of Rights | Access to service or contract | Yes/No |

**Rule of Thumb:** If two or more criteria apply, a DPIA is recommended.

## DPIA Register

### Overview of Conducted DPIAs

| DPIA-ID | Processing | Conduct Date | Risk | Status | Next Review |
|---------|------------|--------------|------|--------|-------------|
| DPIA-001 | [TODO: Name] | [TODO: Date] | High/Medium/Low | Completed/Ongoing | [TODO: Date] |

## DPIA Process

### Phase 1: Threshold Analysis

**Objective:** Determine if a DPIA is required

**Steps:**
1. Describe processing
2. Check criteria (Art. 35(3), Blacklist, WP29 criteria)
3. Consult Data Protection Officer
4. Document decision

**Responsible:** [TODO: Department, Data Protection Officer]  
**Duration:** [TODO: e.g., 1-2 weeks]

### Phase 2: DPIA Execution

**Objective:** Systematic assessment of risks

#### Step 1: Description of Processing (Art. 35(7)(a))

**To be documented:**
- Purposes of processing
- Categories of personal data
- Categories of data subjects
- Recipients of data
- Storage duration
- Functional description of processing
- Technologies used
- Data flows (diagrams)

#### Step 2: Assessment of Necessity and Proportionality (Art. 35(7)(b))

**To be checked:**
- Is processing necessary to achieve purpose?
- Are means appropriate?
- Are data protection principles complied with?
- Are there less invasive alternatives?

**Lawfulness:**
- Legal basis (Art. 6)
- Legitimate interests (if Art. 6(1)(f))
- Balancing of interests

#### Step 3: Risk Assessment (Art. 35(7)(c))

**Risk Identification:**

| Risk | Description | Affected Rights | Likelihood | Severity |
|------|-------------|-----------------|------------|----------|
| [TODO] | [TODO] | [TODO: e.g., Right to privacy] | Low/Medium/High | Low/Medium/High |

**Risk Assessment Matrix:**

| Severity / Likelihood | Low | Medium | High |
|----------------------|-----|--------|------|
| **High** | Medium | High | Very High |
| **Medium** | Low | Medium | High |
| **Low** | Very Low | Low | Medium |

**Affected Rights and Freedoms:**
- Right to privacy
- Right to data protection
- Right to non-discrimination
- Right to freedom of expression
- Other fundamental rights

#### Step 4: Measures for Risk Mitigation (Art. 35(7)(d))

**Technical Measures:**

| Measure | Description | Risk Mitigation | Status |
|---------|-------------|-----------------|--------|
| Encryption | [TODO] | [TODO: Reduces risk from X to Y] | Implemented/Planned |
| Pseudonymization | [TODO] | [TODO] | Implemented/Planned |
| Access Controls | [TODO] | [TODO] | Implemented/Planned |

**Organizational Measures:**

| Measure | Description | Risk Mitigation | Status |
|---------|-------------|-----------------|--------|
| Training | [TODO] | [TODO] | Implemented/Planned |
| Policies | [TODO] | [TODO] | Implemented/Planned |
| Audits | [TODO] | [TODO] | Implemented/Planned |

**Residual Risk After Measures:**

| Risk | Original Risk | Measures | Residual Risk | Acceptable |
|------|--------------|----------|---------------|------------|
| [TODO] | [TODO: High] | [TODO: Measures] | [TODO: Medium] | Yes/No |

### Phase 3: Consultation of Data Protection Officer (Art. 35(2))

**Obligation:** The Data Protection Officer is consulted during the DPIA.

**Consultation:**
- **Date:** [TODO: Date]
- **Opinion:** [TODO: Summary of recommendations]
- **Consideration:** [TODO: How recommendations were implemented]

### Phase 4: Seeking Views of Data Subjects (Art. 35(9))

**Where appropriate:** Seek views of data subjects or their representatives.

**Conducted:** [TODO: Yes/No]  
**Method:** [TODO: e.g., Survey, Focus group]  
**Results:** [TODO: Summary]

### Phase 5: Documentation and Approval

**Create DPIA Report:**
- Document all steps
- Summarize risk assessment
- List measures
- Assess residual risk

**Approval:**
- **Responsible:** [TODO: Management]
- **Date:** [TODO: Date]
- **Decision:** Approved / Approved with conditions / Rejected

## Prior Consultation with Supervisory Authority (Art. 36)

### Consultation Obligation (Art. 36(1))

If the DPIA indicates that processing would result in a high risk if the controller does not take measures to mitigate the risk, the controller consults the supervisory authority prior to processing.

**Criteria for Consultation:**
- Residual risk after measures is high
- No further measures possible to mitigate risk
- Uncertainty about appropriateness of measures

**Consultation Required:** [TODO: Yes/No]

### Consultation Process

**Information to be Provided (Art. 36(3)):**
- Responsibilities
- Purposes and means of processing
- Measures to protect rights and freedoms
- Contact details of Data Protection Officer
- DPIA report
- Other relevant information

**Supervisory Authority Deadline:** 8 weeks (extendable to 14 weeks for complex processing)

**Consultation Documentation:**
- **Request Date:** [TODO: Date]
- **Supervisory Authority Opinion:** [TODO: Summary]
- **Implementation of Recommendations:** [TODO: Measures]

## Review and Update

### Review Obligation (Art. 35(11))

The DPIA is reviewed when:
- Changes in risk of processing
- Changes in processing activity
- New technologies are used
- New insights about risks emerge

**Review Frequency:** [TODO: e.g., annually or upon changes]

### Update Process

1. Identify changes
2. Update risk assessment
3. Adapt measures
4. Consult Data Protection Officer
5. Update documentation
6. Obtain approval

## DPIA Template

**Standard Template:** [TODO: Link to DPIA template]  
**Industry-Specific Templates:** [TODO: If available]

## Responsibilities

| Task | Responsible | Accountable | Consulted | Informed |
|------|-------------|-------------|-----------|----------|
| Threshold Analysis | [TODO] | [TODO] | [TODO] | [TODO] |
| DPIA Execution | [TODO] | [TODO] | [TODO] | [TODO] |
| Risk Assessment | [TODO] | [TODO] | [TODO] | [TODO] |
| Measure Planning | [TODO] | [TODO] | [TODO] | [TODO] |
| Approval | [TODO] | [TODO] | [TODO] | [TODO] |

## Links to Other Documents

- **Controller Obligations (Art. 24):** Accountability
- **Security of Processing (Art. 32):** Technical measures
- **Records of Processing Activities (Art. 30):** Documentation
- **Data Protection Officer (Art. 39):** Advisory role

**Next Steps:**
1. Identify all processing requiring DPIA
2. Conduct systematic DPIAs
3. Document risks and measures
4. Consult Data Protection Officer
5. Review DPIAs regularly

