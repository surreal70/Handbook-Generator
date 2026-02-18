
Document-ID: tisax-0120

Status: Draft
Classification: Internal

# Information Classification

**Document-ID:** [FRAMEWORK]-0120
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Approved by:** {{ meta-handbook.approver }}
**Revision:** [TODO]
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Classification:** {{ meta-handbook.classification }}
**Last Update:** {{ meta-handbook.modifydate }}
**Template Version:** [TODO]

---

---

## Purpose

This document defines the classification schema for information and assets and associated protection requirements according to TISAX requirements.

## Scope

This document applies to all information and assets of [TODO] that must be classified.

## Classification Schema

### Confidentiality Levels

[TODO] uses the following confidentiality levels:

#### Level 1: Public

**Definition:**
- Information intended for the public
- No negative impact upon disclosure

**Examples:**
- Public press releases
- Marketing materials
- Published product information
- Public website content

**Protection Requirements:**
- No special protection measures required
- Integrity protection to prevent manipulation

#### Level 2: Internal

**Definition:**
- Information for internal use
- Minor negative impact upon disclosure

**Examples:**
- Internal communications
- General process documentation
- Organizational structures
- Internal policies

**Protection Requirements:**
- Access only for employees and authorized service providers
- Basic access control
- No disclosure to third parties without approval

#### Level 3: Confidential

**Definition:**
- Sensitive business information
- Significant negative impact upon disclosure

**Examples:**
- Business plans and strategies
- Financial information
- Customer data
- Supplier contracts
- Technical specifications

**Protection Requirements:**
- Access only on need-to-know basis
- Encryption during transmission and storage
- Confidentiality agreements (NDAs)
- Logging of access
- Secure disposal

#### Level 4: Strictly Confidential

**Definition:**
- Highly sensitive information
- Severe negative impact upon disclosure

**Examples:**
- Prototypes and development data
- Trade secrets
- Strategic partnerships
- Special categories of personal data
- Security-relevant information

**Protection Requirements:**
- Strict access control with approval process
- Strong encryption (AES-256 or higher)
- Multi-factor authentication
- Comprehensive logging and monitoring
- Physical security measures
- Secure destruction after retention period

### Integrity Levels

Classification according to integrity requirements:

#### Low
- Errors have minor impact
- Manual correction possible
- Example: Internal notes

#### Medium
- Errors have noticeable impact
- Correction requires effort
- Example: Process documentation

#### High
- Errors have significant impact
- Correction is complex or critical
- Example: Financial data, contracts

#### Very High
- Errors have severe impact
- Correction is very complex or impossible
- Example: Production data, security configurations

### Availability Levels

Classification according to availability requirements:

#### Low
- Outage tolerable for several days
- No time-critical processes affected
- Example: Archive data

#### Medium
- Outage tolerable for hours
- Impairment of business processes
- Example: Internal communication systems

#### High
- Outage tolerable for minutes
- Significant impairment of business processes
- Example: Email system, ERP system

#### Critical
- Outage not tolerable
- Business-critical processes affected
- Example: Production systems, emergency systems

## Classification Process

### 1. Responsibility

**Information Owner:**
- Responsible for classification
- Determines protection requirements
- Approves access
- Reviews classification regularly

**Information Custodian:**
- Implements protection measures
- Provides technical controls
- Monitors compliance

### 2. Classification Criteria

Classification considers:

**Business Value:**
- Strategic importance
- Financial value
- Competitive relevance

**Regulatory Requirements:**
- Legal requirements (GDPR, etc.)
- Contractual obligations
- Industry standards (TISAX, ISO 27001)

**Impact of Damage:**
- Financial damage
- Reputational damage
- Legal consequences
- Operational impact

### 3. Classification Procedure

**Step 1: Identification**
- Identify information or asset
- Determine information owner
- Analyze context and use

**Step 2: Assessment**
- Assess confidentiality
- Assess integrity
- Assess availability
- Highest level determines overall classification

**Step 3: Documentation**
- Document classification
- Record justification
- Enter in asset inventory

**Step 4: Labeling**
- Mark information accordingly
- Set metadata
- Apply physical labeling

**Step 5: Protection Measures**
- Implement required controls
- Define access authorization
- Activate technical protection measures

## Labeling of Information

### Electronic Documents

Labeling in:
- Document header/footer
- File metadata
- Email subject lines
- Watermarks

**Format:**
```
CLASSIFICATION: [LEVEL]
Example: CLASSIFICATION: CONFIDENTIAL
```

### Physical Documents

Labeling through:
- Stamps or stickers
- Color coding
- Special envelopes
- Visible marking on each page

### Digital Assets

Labeling through:
- Metadata tags
- File naming conventions
- Access control labels
- Encryption flags

## Protection Measures by Classification

### Technical Measures

| Classification | Access Control | Encryption | Backup | Logging |
|---------------|----------------|------------|--------|---------|
| Public | None | Optional | Standard | None |
| Internal | Basic | During transmission | Standard | Basic |
| Confidential | Extended | Always | Daily | Extended |
| Strictly Confidential | Strict | Strong (AES-256) | Multiple times daily | Comprehensive |

### Organizational Measures

**Public:**
- No special measures

**Internal:**
- Employee access
- Basic awareness

**Confidential:**
- Need-to-know principle
- NDAs required
- Training required
- Secure disposal

**Strictly Confidential:**
- Approval process
- Special NDAs
- Intensive training
- Clean desk policy
- Supervised disposal

### Handling Guidelines

**Storage:**
- Public: Any
- Internal: Approved systems
- Confidential: Encrypted systems
- Strictly Confidential: Highly secure, encrypted systems

**Transmission:**
- Public: Any
- Internal: Internal networks
- Confidential: Encrypted channels
- Strictly Confidential: Strongly encrypted, monitored channels

**Disposal:**
- Public: Normal disposal
- Internal: Trash/Delete
- Confidential: Shredding/Secure deletion
- Strictly Confidential: Certified destruction

## Declassification and Reclassification

### Declassification

Information can be declassified when:
- Protection requirement no longer applies
- Information becomes public
- Retention period expired
- Business value decreased

**Process:**
1. Request by information owner
2. Review by information security
3. Approval by management
4. Update classification
5. Adjust protection measures

### Reclassification

Information must be reclassified when:
- Protection requirement increases
- New regulatory requirements
- Change in business value
- Security incidents

**Process:**
1. Identification of change requirement
2. Reassessment by information owner
3. Documentation of change
4. Implementation of enhanced protection measures
5. Information to affected parties

## Review and Maintenance

### Regular Review

Classifications are reviewed:
- **Annually**: All classified information
- **Upon Changes**: Affected information
- **Upon Incidents**: Involved information
- **On Request**: Ad-hoc review

### Quality Assurance

[TODO] ensures:
- Consistent application of schema
- Appropriate protection measures
- Currency of classifications
- Compliance with requirements

## TISAX-Specific Requirements

### VDA ISA Controls

This document addresses:

- **2.3.1**: Classification of information
- **2.3.2**: Labeling of information
- **2.3.3**: Handling of assets

### Assessment Evidence

For TISAX assessments:

- Classification policy
- Classification schema documentation
- Examples of classified information
- Training evidence
- Process descriptions

## Training and Awareness

### Training Content

All employees are trained on:
- Classification schema
- Labeling obligations
- Handling guidelines
- Responsibilities
- Consequences of violations

### Target Groups

- **All Employees**: Basic training
- **Information Owners**: Extended training
- **IT Personnel**: Technical training
- **Management**: Strategic training

## Metrics

[TODO] measures:

- Percentage of classified information (Target: 100%)
- Correctness of classification (sampling)
- Compliance with labeling obligation (Target: >95%)
- Number of reclassifications
- Training participation (Target: 100%)

<!-- Note: Adapt classification schema to your organization -->

<!-- End of template -->
