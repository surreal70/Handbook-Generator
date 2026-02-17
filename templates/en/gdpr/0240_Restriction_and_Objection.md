# Restriction and Objection

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
This template documents the right to restriction of processing and right to object according to Art. 18 and 21 GDPR.

Customization required:
- Define processes for restriction and objection requests
- Document technical implementation of restriction
- Describe exceptions and special cases
- Implement notification obligations

Reference: GDPR Art. 18 (Right to restriction of processing), Art. 21 (Right to object)
-->

## Purpose

This document describes the implementation of the right to restriction of processing and the right to object in {{ meta-organisation.name }}.

## Right to Restriction (Art. 18)

### Grounds for Restriction

**Restriction is required when:**

| Ground | Description | Duration |
|--------|-------------|----------|
| Accuracy Contested | Data subject contests accuracy | Until verification |
| Unlawful Processing | Processing unlawful, but no erasure desired | Until clarification |
| No Longer Necessary | Data no longer necessary, but needed for legal claims | Until clarification |
| Objection Lodged | Objection according to Art. 21(1) | Until balancing of interests |

### Meaning of Restriction

**During restriction:**
- Data may only be stored
- No further processing (except storage)

**Exceptions (processing permissible with consent):**
- Establishment of legal claims
- Protection of rights of other persons
- Important reasons of public interest

### Technical Implementation

**Methods for Restriction:**

| Method | Description | Use Case |
|--------|-------------|----------|
| [TODO: Marking] | Mark record as "restricted" | Standard |
| [TODO: Access Lock] | Technical access restriction | Sensitive data |
| [TODO: Separation] | Move to separate system | Long-term restriction |
| [TODO: Pseudonymization] | Separation of identification data | Additional protection |

### Restriction Process

**Standard Process:**

1. **Receipt of Request (Day 0)**
   - Registration
   - Acknowledgment
   - Assignment

2. **Review (Day 1-10)**
   - Identification of data subject
   - Review of restriction grounds
   - Identification of affected data

3. **Implementation (Day 11-25)**
   - Technical restriction in all systems
   - Notification of recipients (Art. 19)
   - Documentation

4. **Response (Day 26-30)**
   - Information about restriction performed
   - Information about lifting of restriction

### Lifting of Restriction

**Restriction is lifted when:**
- Reason for restriction no longer applies
- Data subject consents
- Restriction reason clarified

**Before lifting:**
- Information to data subject required
- Documentation of lifting

## Right to Object (Art. 21)

### Objection to Processing (Art. 21(1))

**Right to object for:**
- Processing based on public interest (Art. 6(1)(e))
- Processing based on legitimate interests (Art. 6(1)(f))

**Consequence of Objection:**
- Processing must be stopped
- Unless: Compelling legitimate grounds override

### Balancing of Interests

**Assessment After Objection:**

| Criterion | Assessment Question | Evaluation |
|-----------|-------------------|------------|
| Compelling Grounds | Are there compelling legitimate grounds? | [TODO] |
| Legal Claims | Are legal claims affected? | [TODO] |
| Interests of Person | What interests does the data subject have? | [TODO] |
| Balancing | Do controller's grounds override? | [TODO] |

**Result:**
- Compelling grounds override: Processing permissible
- No compelling grounds: Stop processing

### Objection to Direct Marketing (Art. 21(2))

**Special Features:**
- Absolute right to object
- No balancing of interests required
- Processing must be stopped immediately

**Implementation:**
- Entry in suppression list
- No further advertising
- Information to all marketing channels

### Objection to Profiling (Art. 21(3))

**Right to object for:**
- Profiling in connection with direct marketing
- Profiling based on legitimate interests

### Objection Process

**Standard Process:**

1. **Receipt of Objection (Day 0)**
   - Registration
   - Acknowledgment
   - Immediate stop for direct marketing

2. **Review (Day 1-15)**
   - Identification of data subject
   - Review of legal basis
   - For Art. 6(1)(f): Balancing of interests

3. **Decision (Day 16-20)**
   - Stop processing or
   - Reasoned refusal (compelling grounds)

4. **Implementation (Day 21-25)**
   - Stop in all systems
   - Notification of recipients
   - Documentation

5. **Response (Day 26-30)**
   - Information about stop or refusal
   - If refusal: Justification and remedies

## Notification Obligation (Art. 19)

### Notification of Recipients

**Recipients must be informed of restriction or objection:**
- Processors
- Third party recipients
- Public authorities

**Exceptions:**
- Impossible
- Disproportionate effort

## Documentation

### Restriction and Objection Register

| Date | Data Subject | Type | Reason | Status | Lifting | Processor |
|------|--------------|------|--------|--------|---------|-----------|
| [TODO] | [TODO] | Restriction | Accuracy contested | Active | [TODO] | [TODO] |
| [TODO] | [TODO] | Objection | Direct marketing | Implemented | N/A | [TODO] |
| [TODO] | [TODO] | Objection | Legitimate interest | Refused | N/A | [TODO] |

### Evidence Requirements

**Documentation for Accountability:**
- All restriction and objection requests
- Performed restrictions
- Balancing of interests for objections
- Refusals and their justification
- Notifications to recipients
- Lifting of restrictions

## Links to Other Documents

- **Transparency (Art. 12):** Modalities of processing
- **Legitimate Interests (Art. 6(1)(f)):** Balancing of interests
- **Notification Obligation (Art. 19):** Notification of recipients
- **Erasure (Art. 17):** Alternative to restriction

## Common Violations and Their Prevention

| Violation | Example | Prevention |
|-----------|---------|------------|
| No Restriction | Continued processing despite request | Immediate implementation |
| Missing Balancing | Refusal without review | Careful balancing |
| Delayed Implementation | Advertising after objection | Immediate stop |
| No Notification | Recipients not informed | Notification process |

**Next Steps:**
1. Establish processes for restriction and objection requests
2. Implement technical restriction mechanisms
3. Define balancing of interests process
4. Train employees on restriction and objection rights
5. Document all requests in register

