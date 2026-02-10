# Purpose Limitation

**Document-ID:** 0110  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** Draft  
**Classification:** Internal  
**Last Update:** {{ meta.date }}  

---

<!-- 
This template documents the principle of purpose limitation according to Art. 5(1)(b) GDPR.

Customization required:
- Define clear purposes for all processing activities
- Document processes for checking purpose compatibility
- Describe measures for purpose changes
- Link to records of processing activities

Reference: GDPR Art. 5(1)(b) (Purpose limitation)
-->

## Purpose

This document describes the implementation of the principle of purpose limitation in {{ meta.organization }}. Personal data may only be collected and processed for specified, explicit and legitimate purposes.

## Principle according to Art. 5(1)(b) GDPR

**Legal Requirement:**  
Personal data must be collected for specified, explicit and legitimate purposes and not further processed in a manner incompatible with those purposes.

### Core Elements

1. **Specified Purposes:** Purposes must be defined before collection
2. **Explicit Purposes:** Purposes must be clearly and precisely formulated
3. **Legitimate Purposes:** Purposes must be lawful and comprehensible
4. **No Incompatible Further Processing:** New purposes must be compatible or have new legal basis

## Purpose Definition

### Requirements for Purpose Descriptions

**Purposes must be:**
- Concrete and specific (not "business purposes")
- Understandable for data subjects
- Defined before data collection
- Documented in records of processing activities
- Communicated in privacy notices

### Examples of Purpose Definitions

| Well Defined | Poorly Defined |
|--------------|----------------|
| "Processing customer orders" | "Business purposes" |
| "Sending monthly newsletter" | "Marketing" |
| "Fulfilling tax obligations" | "Legal requirements" |
| "Processing job applications" | "HR administration" |

## Purpose Limitation in Our Organization

### Processing Purposes

| Processing Activity | Defined Purpose | Legal Basis | Data Types |
|--------------------|-----------------|-------------|------------|
| [TODO: Customer Management] | [TODO: Contract fulfillment, customer service] | Art. 6(1)(b) | [TODO: Master data] |
| [TODO: Newsletter] | [TODO: Sending product information] | Art. 6(1)(a) | [TODO: Email, name] |
| [TODO: Accounting] | [TODO: Fulfilling tax obligations] | Art. 6(1)(c) | [TODO: Invoice data] |
| [TODO: Applicant Management] | [TODO: Processing applications] | Art. 6(1)(b) | [TODO: Applicant data] |

### Process for Purpose Definition

**For new processing:**

1. **Clearly define purpose**
   - What should be achieved?
   - Why is the data needed?
   - How does processing contribute to the purpose?

2. **Document purpose**
   - In records of processing activities (Art. 30)
   - In privacy notices (Art. 13-14)
   - In internal processing policies

3. **Communicate purpose**
   - Inform data subjects
   - Train employees
   - Instruct processors

## Further Processing for Other Purposes

### Compatibility Assessment (Art. 6(4))

**When data is to be processed for a new purpose, it must be assessed:**

1. **Is the new purpose compatible with the original purpose?**

**Criteria for Compatibility (Art. 6(4)):**
- Link between original and new purpose
- Context of data collection
- Nature of personal data
- Possible consequences for data subjects
- Existing safeguards (e.g., encryption, pseudonymization)

2. **If compatible:** Further processing is permissible
3. **If not compatible:** New legal basis or consent required

### Compatibility Test

| Criterion | Assessment Question | Evaluation |
|-----------|-------------------|------------|
| Link | Is there a factual connection? | [TODO] |
| Context | Does it meet data subject expectations? | [TODO] |
| Data Type | Is the data suitable for the new purpose? | [TODO] |
| Consequences | What are the impacts of further processing? | [TODO] |
| Safeguards | What protective measures are in place? | [TODO] |

**Result:** Compatible / Not compatible

### Examples of Purpose Compatibility

**Compatible Further Processing:**
- Customer data for contract fulfillment → Further processing for warranty claims
- Employee data for payroll → Further processing for social security notifications
- Order data → Further processing for accounting and taxes

**Incompatible Further Processing (new legal basis required):**
- Customer data for contract fulfillment → Further processing for advertising (consent required)
- Applicant data → Further processing for other job offers (new consent required)
- Health data for treatment → Further processing for research (new legal basis required)

## Exceptions to Purpose Limitation

### Further Processing for Specific Purposes (Art. 5(1)(b))

**Always permissible (no compatibility assessment required):**
- Archiving purposes in the public interest
- Scientific or historical research purposes
- Statistical purposes

**Prerequisite:** Appropriate safeguards (e.g., pseudonymization, access restrictions)

## Measures to Ensure Purpose Limitation

### Organizational Measures

| Measure | Description | Responsible | Status |
|---------|-------------|-------------|--------|
| [TODO: Purpose Definition] | Clear purpose definition before data collection | Department | [TODO] |
| [TODO: Documentation] | Maintain Art. 30 records | DPO | [TODO] |
| [TODO: Compatibility Assessment] | Process for new purposes | DPO | [TODO] |
| [TODO: Training] | Employee training on purpose limitation | HR | [TODO] |

### Technical Measures

- [TODO: Access control by purposes]
- [TODO: Purpose-based database segmentation]
- [TODO: Automated purpose checking for data access]
- [TODO: Logging of purpose changes]

## Controls and Monitoring

### Regular Reviews

| Control | Frequency | Responsible | Documentation |
|---------|-----------|-------------|---------------|
| Purpose Definitions | Quarterly | DPO | Review protocol |
| Compatibility Assessments | As needed | DPO | Compatibility test |
| Records of Processing | Quarterly | DPO | Update protocol |
| Employee Training | Annually | HR | Training records |

## Documentation

### Evidence Requirements

**Document for each processing:**
- Defined purpose
- Legal basis for the purpose
- Data types required for the purpose
- Storage period in relation to the purpose
- For further processing: Compatibility test or new legal basis

### Checklist for New Processing

- [ ] Purpose clearly and explicitly defined
- [ ] Purpose is legitimate and lawful
- [ ] Purpose defined before data collection
- [ ] Purpose documented in Art. 30 records
- [ ] Purpose communicated in privacy notice
- [ ] Only data necessary for purpose collected
- [ ] Storage period oriented to purpose
- [ ] Employees informed about purpose

## Links to Other Documents

- **Data Protection Principles (Art. 5):** Purpose limitation as core principle
- **Legal Bases (Art. 6):** Legitimacy of purposes
- **Records (Art. 30):** Documentation of purposes
- **Information Obligations (Art. 13-14):** Communication of purposes
- **Data Minimization (Art. 5(1)(c)):** Purpose-related data collection

## Common Violations and Their Prevention

| Violation | Example | Prevention |
|-----------|---------|------------|
| Unclear purposes | "Business purposes" | Concrete purpose definition |
| Purpose misuse | Customer data for advertising without consent | Conduct compatibility assessment |
| Missing documentation | Purpose not in records | Maintain Art. 30 records |
| Retrospective purpose change | Purpose changed after collection | Define purpose before collection |

---

**Next Steps:**
1. Define clear purposes for all processing activities
2. Document purposes in records of processing activities
3. Implement compatibility assessment for new purposes
4. Train employees on purpose limitation
5. Regularly review compliance with purpose limitation

