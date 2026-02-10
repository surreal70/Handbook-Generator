# Processing by Processor

**Document-ID:** 0310  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** Draft  
**Classification:** Internal  
**Last Update:** {{ meta.date }}  

---

<!-- 
This template documents processing by processor according to Art. 28 GDPR.
It describes requirements for processor agreements and control of processors.

Customization required:
- List all processors
- Document Data Processing Agreements (DPA)
- Define selection criteria for processors
- Implement control mechanisms
- Document sub-processors

Reference: GDPR Art. 28 (Processor), Art. 29 (Processing under the authority of the controller or processor)
-->

## Purpose

This document regulates processing by processor at {{ meta.organization }} according to Art. 28 GDPR. It defines requirements for processors, contract design, and control mechanisms.

## Processor Register

### Active Processors

| Processor | Service | Processed Data | DPA Date | Next Review |
|-----------|---------|----------------|----------|-------------|
| [TODO: Name] | [TODO: Service] | [TODO: Data Categories] | [TODO: Date] | [TODO: Date] |

### Categories of Processors

- **IT Service Providers:** [TODO: e.g., Cloud providers, Hosting]
- **HR Service Providers:** [TODO: e.g., Payroll, Recruiting]
- **Marketing Service Providers:** [TODO: e.g., Email marketing, CRM]
- **Support Service Providers:** [TODO: e.g., Helpdesk, Call center]
- **Others:** [TODO: Other categories]

## Requirements for Processors (Art. 28(1))

### Selection Criteria

The processor must provide sufficient guarantees to implement appropriate technical and organizational measures.

**Assessment Criteria:**

| Criterion | Description | Assessment Method |
|-----------|-------------|-------------------|
| Expertise | Data protection expertise | Certificates, References |
| Reliability | Proven compliance | Audits, Reports |
| Resources | Sufficient capacities | Documentation, Evidence |
| TOM | Appropriate security measures | TOM Documentation |
| Certifications | ISO 27001, SOC 2, etc. | Certificates |

### Selection Process

1. **Needs Analysis:** Define requirements
2. **Market Analysis:** Identify potential providers
3. **Pre-selection:** Based on selection criteria
4. **Due Diligence:** Detailed review
5. **Contract Negotiation:** DPA conclusion
6. **Approval:** By Data Protection Officer
7. **Onboarding:** Integration and training

## Data Processing Agreement (DPA)

### Mandatory Content per Art. 28(3)

The agreement must regulate the following:

#### 1. Subject Matter and Duration

- **Subject Matter:** [TODO: Type of processing]
- **Duration:** [TODO: Contract term]
- **Nature and Purpose of Processing:** [TODO: Description]

#### 2. Type of Personal Data

- **Data Categories:** [TODO: e.g., Contact data, Contract data]
- **Categories of Data Subjects:** [TODO: e.g., Customers, Employees]

#### 3. Obligations and Rights of Controller

- Right to issue instructions
- Right to control
- Right to information
- Right to deletion

#### 4. Obligations of Processor

**According to Art. 28(3)(a)-(h):**

| Obligation | Description | Implementation |
|------------|-------------|----------------|
| a) Instructions | Process only on documented instructions | [TODO: Process] |
| b) Confidentiality | Commitment to confidentiality | [TODO: Evidence] |
| c) Security | Measures according to Art. 32 | [TODO: TOM Documentation] |
| d) Sub-processors | Authorization and conditions | [TODO: Process] |
| e) Data Subject Rights | Support with requests | [TODO: Process] |
| f) Support | With compliance obligations | [TODO: Agreement] |
| g) Deletion/Return | After contract end | [TODO: Process] |
| h) Demonstration | Make information available | [TODO: Reporting] |

### Contract Template

**Standard DPA Template:** [TODO: Link to template]  
**Approval Process:** [TODO: Describe approval process]

## Sub-Processors (Art. 28(2), (4))

### Authorization Procedure

**Authorization Type:** [TODO: General or specific authorization]

#### General Authorization

- List of authorized sub-processors maintained
- Information obligation upon changes
- Controller's right to object

#### Specific Authorization

- Individual case authorization required
- Review before engagement
- Documentation of authorization

### Sub-Processor Register

| Sub-Processor | Main Processor | Service | Authorization Date |
|---------------|----------------|---------|-------------------|
| [TODO: Name] | [TODO: Name] | [TODO: Service] | [TODO: Date] |

## Control and Monitoring

### Control Rights (Art. 28(3)(h))

**Control Measures:**
- On-site audits
- Document review
- Certificate review
- Questionnaire assessments
- Penetration tests

### Control Plan

| Processor | Control Type | Frequency | Next Control | Responsible |
|-----------|-------------|-----------|--------------|-------------|
| [TODO: Name] | [TODO: Type] | [TODO: Frequency] | [TODO: Date] | [TODO: Role] |

### Audit Checklist

- [ ] DPA complete and current
- [ ] TOM documentation available and appropriate
- [ ] Sub-processors authorized
- [ ] Certifications valid
- [ ] Incident response process defined
- [ ] Training records available
- [ ] Data deletion/return regulated
- [ ] Insurance coverage sufficient

## Instructions

### Issuing Instructions

**Authorized Persons:**
- [TODO: Role/Name]
- [TODO: Role/Name]

**Form of Instructions:**
- Written (email, document)
- Documented and traceable
- With date and signature

### Instruction Register

| Date | Processor | Instruction | Issued By | Status |
|------|-----------|-------------|-----------|--------|
| [TODO] | [TODO: Name] | [TODO: Content] | [TODO: Person] | Implemented/Open |

## Data Breaches

### Processor's Notification Obligation

The processor must inform the controller without undue delay about data breaches.

**Notification Process:**
1. Immediate notification to: [TODO: Contact]
2. Information: Type of breach, affected data, measures
3. Deadline: Within [TODO: e.g., 24 hours]

### Incident Response Coordination

- Joint incident response plans
- Regular tests and exercises
- Clear communication channels
- Documentation of incidents

## Contract End

### Deletion or Return (Art. 28(3)(g))

**After Contract End:**

| Data Type | Measure | Deadline | Evidence |
|-----------|---------|----------|----------|
| [TODO: Data Type] | Deletion/Return | [TODO: Deadline] | [TODO: Evidence] |

**Deletion Certificate:** [TODO: Describe certification procedure]

### Offboarding Process

1. Contract end notification
2. Data return or deletion
3. Revoke access rights
4. Obtain deletion certificate
5. Complete documentation

## Responsibilities

| Task | Responsible | Accountable | Consulted | Informed |
|------|-------------|-------------|-----------|----------|
| DPA Conclusion | [TODO] | [TODO] | [TODO] | [TODO] |
| Control | [TODO] | [TODO] | [TODO] | [TODO] |
| Issuing Instructions | [TODO] | [TODO] | [TODO] | [TODO] |
| Incident Management | [TODO] | [TODO] | [TODO] | [TODO] |

## Links to Other Documents

- **Controller Obligations (Art. 24):** Overall responsibility
- **Security of Processing (Art. 32):** TOM requirements
- **Data Breaches (Art. 33):** Notification obligations
- **Records of Processing Activities (Art. 30):** Documentation

---

**Next Steps:**
1. Create a complete register of all processors
2. Review all existing contracts for GDPR compliance
3. Implement a control plan for regular audits
4. Define instruction processes and authorizations
5. Establish an instruction register

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial Creation |
