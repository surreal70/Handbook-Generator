# Data Minimization

**Document-ID:** 0120  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** Draft  
**Classification:** Internal  
**Last Update:** {{ meta.date }}  

---

<!-- 
This template documents the principle of data minimization according to Art. 5(1)(c) GDPR.

Customization required:
- Define necessity criteria for data collection
- Document processes for checking data minimization
- Describe measures to reduce data collection
- Implement Privacy by Design principles

Reference: GDPR Art. 5(1)(c) (Data minimization)
-->

## Purpose

This document describes the implementation of the principle of data minimization in {{ meta.organization }}. Only personal data that is actually necessary for the respective purpose may be collected.

## Principle according to Art. 5(1)(c) GDPR

**Legal Requirement:**  
Personal data must be adequate, relevant and limited to what is necessary in relation to the purposes for which they are processed.

### Three Criteria

1. **Adequate:** Data must be in reasonable proportion to the purpose
2. **Relevant:** Data must be relevant to the purpose
3. **Limited to Necessary:** Collect only minimally required data

## Necessity Assessment

### Assessment Process for Data Collection

**Before each data collection, assess:**

1. **Is data collection necessary for the purpose?**
   - Can the purpose be achieved without this data?
   - Are there milder means?
   - Is data collection proportionate?

2. **What data is minimally required?**
   - Which data is absolutely necessary?
   - Which data is "nice-to-have" (to avoid)?
   - Can data be anonymized or pseudonymized?

3. **Documentation of Necessity**
   - Justification in records of processing activities
   - Evidence of necessity assessment
   - Regular review

### Necessity Matrix

| Data Type | Purpose | Necessary? | Justification | Alternative |
|-----------|---------|------------|---------------|-------------|
| [TODO: Name] | [TODO: Contract fulfillment] | Yes | [TODO: Identification] | None |
| [TODO: Date of birth] | [TODO: Newsletter] | No | [TODO: Not required] | Omit |
| [TODO: Address] | [TODO: Delivery] | Yes | [TODO: Shipping] | Parcel station |
| [TODO: Phone] | [TODO: Contact] | Partially | [TODO: Alternative email] | Email |

## Implementation in Our Organization

### Data Collection by Categories

**Mandatory vs. voluntary information:**

| Processing Purpose | Mandatory Information | Voluntary Information | Not Required |
|-------------------|----------------------|----------------------|--------------|
| [TODO: Order] | [TODO: Name, address, payment] | [TODO: Phone] | [TODO: Date of birth] |
| [TODO: Newsletter] | [TODO: Email] | [TODO: Name] | [TODO: Address] |
| [TODO: Customer Account] | [TODO: Email, password] | [TODO: Profile picture] | [TODO: Social media] |

**Marking in Forms:**
- Mark mandatory fields with *
- Clearly mark voluntary fields
- Explain why data is needed

### Measures for Data Minimization

| Measure | Description | Responsible | Status |
|---------|-------------|-------------|--------|
| [TODO: Necessity Assessment] | Review before new processing | DPO | [TODO] |
| [TODO: Form Optimization] | Reduction of input fields | IT | [TODO] |
| [TODO: Anonymization] | Use anonymous data where possible | IT | [TODO] |
| [TODO: Pseudonymization] | Pseudonyms instead of clear data | IT | [TODO] |

## Technical Implementation

### Privacy by Design (Art. 25)

**Data minimization through design:**

- [TODO: Forms with only required fields]
- [TODO: Optional fields clearly marked]
- [TODO: Automatic anonymization after purpose fulfillment]
- [TODO: Pseudonymization of sensitive data]
- [TODO: Aggregation instead of individual data for statistics]

### Anonymization and Pseudonymization

**Anonymization:**
- Complete removal of personal reference
- No traceability to persons
- No GDPR application anymore

**Pseudonymization:**
- Separation of identification and content data
- Traceability only with additional information
- Still GDPR application, but lower risk

**Use Cases:**

| Purpose | Method | Example |
|---------|--------|---------|
| [TODO: Statistics] | Anonymization | Aggregated usage data |
| [TODO: Analysis] | Pseudonymization | User ID instead of name |
| [TODO: Research] | Anonymization | Removal of all identifiers |
| [TODO: Backup] | Pseudonymization | Encrypted personal data |

## Avoiding Excessive Data Collection

### Common Mistakes

| Mistake | Example | Correction |
|---------|---------|------------|
| "Nice-to-have" data | Date of birth for newsletter | Collect only email |
| Excessive profiling | Tracking all activities | Only necessary tracking |
| Data retention | "Might be useful someday" | Only with specific purpose |
| Missing differentiation | All data as mandatory | Separate mandatory vs. voluntary |

### Checklist Against Excessive Data Collection

- [ ] Each data field has documented purpose
- [ ] No "nice-to-have" data fields
- [ ] Mandatory and voluntary fields separated
- [ ] Anonymization/pseudonymization assessed
- [ ] No data retention
- [ ] Regular review of necessity
- [ ] Employees trained on data minimization

## Regular Review

### Data Inventory Review

**Quarterly review:**

1. **What data is collected?**
   - Inventory of all data fields
   - Assignment to processing purposes

2. **Is all data still necessary?**
   - Necessity assessment for existing data
   - Identification of superfluous data

3. **Can data be reduced?**
   - Possibilities for anonymization
   - Possibilities for pseudonymization
   - Deletion of no longer required data

### Controls

| Control | Frequency | Responsible | Documentation |
|---------|-----------|-------------|---------------|
| Necessity Assessment | For new processing | DPO | Review protocol |
| Data Inventory Review | Quarterly | DPO | Inventory list |
| Form Review | Annually | IT/DPO | Review report |
| Anonymization Potential | Annually | IT | Analysis report |

## Documentation

### Evidence Requirements

**Document for each processing:**
- What data is collected?
- Why is each data type necessary?
- Were alternatives assessed (anonymization, pseudonymization)?
- How is necessity regularly reviewed?

### Records of Processing Activities (Art. 30)

**Documentation of data minimization:**
- Categories of personal data
- Justification of necessity
- Minimization measures
- Anonymization/pseudonymization

## Links to Other Documents

- **Data Protection Principles (Art. 5):** Data minimization as core principle
- **Purpose Limitation (Art. 5(1)(b)):** Purpose-related necessity
- **Privacy by Design (Art. 25):** Technical implementation
- **Records (Art. 30):** Documentation of data types
- **Information Obligations (Art. 13-14):** Information about collected data

## Common Violations and Their Prevention

| Violation | Example | Prevention |
|-----------|---------|------------|
| Excessive data collection | All data "just in case" | Necessity assessment |
| Missing differentiation | All fields as mandatory | Mandatory vs. voluntary |
| Data retention | Data without specific purpose | Observe purpose limitation |
| No anonymization | Clear data where not needed | Assess anonymization |

---

**Next Steps:**
1. Conduct necessity assessment for all data collections
2. Optimize forms and reduce data fields
3. Implement anonymization and pseudonymization
4. Train employees on data minimization
5. Establish regular data inventory reviews

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial Creation |
