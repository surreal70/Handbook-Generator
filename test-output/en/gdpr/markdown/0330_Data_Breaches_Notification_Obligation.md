# Data Breaches and Notification Obligation

**Document-ID:** 0330
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



## Purpose

This document regulates handling of data breaches at AdminSend GmbH according to Art. 33-34 GDPR. It defines notification obligations, deadlines, and processes for managing data protection incidents.

## Definition of Data Breach (Art. 4(12))

A personal data breach means a breach of security leading to the accidental or unlawful destruction, loss, alteration, unauthorized disclosure of, or access to, personal data.

### Categories of Data Breaches

| Category | Description | Examples |
|----------|-------------|-----------|
| **Confidentiality Breach** | Unauthorized disclosure or access | Data leak, hacking, accidental disclosure |
| **Integrity Breach** | Unauthorized alteration | Manipulation, data corruption |
| **Availability Breach** | Loss or destruction | Ransomware, hardware failure, accidental deletion |

## Notification to Supervisory Authority (Art. 33)

### Principle (Art. 33(1))

The controller notifies a personal data breach to the competent supervisory authority without undue delay and, where feasible, not later than 72 hours, unless the breach is unlikely to result in a risk to the rights and freedoms of natural persons.

### Risk Assessment

**Criteria for Risk Assessment:**

| Criterion | Low Risk | High Risk |
|-----------|----------|-----------|
| Type of Data | General contact data | Special categories (Art. 9), Financial data |
| Scope | Few data subjects | Many data subjects |
| Severity | Minor impact | Severe impact |
| Protective Measures | Encrypted, pseudonymized | Unencrypted, plaintext |
| Data Subjects | Employees (internal) | Customers, Children, vulnerable groups |

**Decision Tree:**
1. Is there a data breach? → Yes/No
2. Is there a risk to rights and freedoms? → Yes/No
3. If Yes: Notification required
4. If high risk: Additionally notify data subjects

### Mandatory Content of Notification (Art. 33(3))

The notification must contain at least the following information:

#### a) Nature of Breach

- Description of the data breach
- Categories and approximate number of data subjects concerned
- Categories and approximate number of data records concerned

#### b) Contact Point

- Name and contact details of the Data Protection Officer or other contact point

#### c) Description of Consequences

- Description of the likely consequences of the data breach

#### d) Measures Taken

- Description of measures taken or proposed to address and mitigate the breach

### Notification Deadline

**72-Hour Deadline from Awareness**

| Time | Action |
|------|--------|
| T+0 (Discovery) | Activate incident response, initial assessment |
| T+24h | Risk assessment completed, notification obligation clarified |
| T+48h | Notification prepared |
| T+72h | Notification submitted to supervisory authority |

**If 72-Hour Deadline Exceeded:**
- Justification for delay required (Art. 33(1))

### Competent Supervisory Authority

**Supervisory Authority:** [TODO: Name of competent authority]  
**Address:** [TODO: Address]  
**Notification Portal:** [TODO: URL to online notification form]  
**Contact:** [TODO: Email, Phone]

## Communication to Data Subjects (Art. 34)

### Notification Obligation (Art. 34(1))

When the data breach is likely to result in a high risk to the rights and freedoms of natural persons, the controller communicates the breach to the data subject without undue delay.

### Criteria for High Risk

- **Special categories of personal data (Art. 9)**
- **Financial data, access credentials**
- **Large number of data subjects**
- **Vulnerable groups (children, patients)**
- **Severe consequences (identity theft, financial losses)**

### Content of Communication (Art. 34(2))

The communication must contain:

- Nature of the data breach
- Name and contact details of the Data Protection Officer
- Likely consequences of the data breach
- Measures taken or proposed to address and mitigate the breach
- Recommendations for data subjects (e.g., change password)

### Exceptions from Communication (Art. 34(3))

No communication required if:

**a) Protective Measures:** Data was encrypted or otherwise protected  
**b) Subsequent Measures:** Measures taken that eliminate high risk  
**c) Disproportionate Effort:** Public communication instead

## Incident Response Process

### Phase 1: Detection and Assessment

**Timeframe: 0-4 hours**

1. Detect and report incident
2. Activate incident response team
3. Conduct initial assessment
4. Confirm data breach

**Responsible:** [TODO: IT Security, Data Protection Officer]

### Phase 2: Containment

**Timeframe: 4-12 hours**

1. Immediate measures for damage control
2. Isolate affected systems
3. Prevent further data loss
4. Forensic preservation

**Responsible:** [TODO: IT Security]

### Phase 3: Analysis and Risk Assessment

**Timeframe: 12-24 hours**

1. Determine scope of breach
2. Identify affected data and persons
3. Conduct risk assessment
4. Check notification obligation

**Responsible:** [TODO: Data Protection Officer, IT Security]

### Phase 4: Notification and Communication

**Timeframe: 24-72 hours**

1. Notification to supervisory authority (if required)
2. Communication to data subjects (if required)
3. Internal communication
4. External communication (if required)

**Responsible:** [TODO: Data Protection Officer, Management]

### Phase 5: Recovery

**Timeframe: 72 hours - weeks**

1. Restore systems
2. Close security gaps
3. Implement preventive measures
4. Enhance monitoring

**Responsible:** [TODO: IT Security]

### Phase 6: Post-Incident Review

**Timeframe: After completion**

1. Document incident
2. Conduct lessons learned
3. Adapt processes
4. Update training

**Responsible:** [TODO: Data Protection Officer, IT Security]

## Documentation Obligation (Art. 33(5))

The controller documents all data breaches, including all facts, effects, and remedial action taken.

### Breach Register

| Date | Type of Breach | Affected Data | Number of Data Subjects | Risk | Notified | Communicated | Status |
|------|----------------|---------------|------------------------|------|----------|--------------|--------|
| [TODO] | [TODO] | [TODO] | [TODO] | Low/High | Yes/No | Yes/No | Open/Closed |

### Retention Period

**Documentation:** At least 3 years after incident closure

## Communication Plans

### Internal Communication

**Escalation Chain:**
1. Discoverer → IT Security
2. IT Security → Data Protection Officer
3. Data Protection Officer → Management
4. Management → Supervisory Board (for severe incidents)

### External Communication

**Stakeholders:**
- Supervisory authority
- Data subjects
- Media (for public interest)
- Business partners (if affected)
- Insurance

**Communication Responsible:** [TODO: Role]

## Responsibilities

| Task | Responsible | Accountable | Consulted | Informed |
|------|-------------|-------------|-----------|----------|
| Incident Detection | [TODO] | [TODO] | [TODO] | [TODO] |
| Risk Assessment | [TODO] | [TODO] | [TODO] | [TODO] |
| Notification to Authority | [TODO] | [TODO] | [TODO] | [TODO] |
| Communication to Data Subjects | [TODO] | [TODO] | [TODO] | [TODO] |
| Documentation | [TODO] | [TODO] | [TODO] | [TODO] |

## Links to Other Documents

- **Security of Processing (Art. 32):** Preventive measures
- **Processing by Processor (Art. 28):** Processor notification obligation
- **Data Protection Impact Assessment (Art. 35):** Risk assessment
- **Incident Response Plan:** Detailed technical processes

**Next Steps:**
1. Implement an incident response process
2. Define escalation paths and responsibilities
3. Create templates for notifications and communications
4. Conduct regular incident response exercises
5. Establish a breach register

