# Data Transfers to Third Countries

**Document-ID:** 0500
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

<!-- 
This template documents data transfers to third countries according to Art. 44-50 GDPR.
It describes requirements and safeguards for international data transfers.

Customization required:
- Identify all third country transfers
- Check adequacy decisions
- Implement appropriate safeguards (e.g., Standard Contractual Clauses)
- Document derogations
- Conduct Transfer Impact Assessments

Reference: GDPR Art. 44-50 (Transfers of personal data to third countries)
-->

## Purpose

This document regulates the transfer of personal data to third countries (outside EU/EEA) at {{ meta-organisation.name }} according to Art. 44-50 GDPR. It ensures that an adequate level of protection is guaranteed even for international data transfers.

## Principle (Art. 44)

A transfer of personal data to a third country may only take place if:
- The conditions of Art. 45-49 are complied with
- The other provisions of GDPR are complied with
- Including data subject rights and remedies

## Register of Third Country Transfers

### Overview

| ID | Recipient | Third Country | Purpose | Legal Basis | Safeguards | Volume |
|----|-----------|---------------|---------|-------------|------------|--------|
| T001 | [TODO: Name] | [TODO: Country] | [TODO: Purpose] | Art. 45/46/49 | [TODO] | [TODO: Number of data subjects] |

## Adequacy Decision (Art. 45)

### Countries with Adequacy Decision

The European Commission may decide that a third country provides an adequate level of protection.

**Current Adequacy Decisions (as of 2024):**

| Country/Region | Decision | Valid Since | Specifics |
|----------------|----------|-------------|-----------|
| Andorra | 2010/625/EU | 19.10.2010 | - |
| Argentina | 2003/490/EC | 30.06.2003 | - |
| Canada | 2002/2/EC | 20.12.2001 | Commercial organizations only |
| Faroe Islands | 2010/146/EU | 05.03.2010 | - |
| Guernsey | 2003/821/EC | 21.11.2003 | - |
| Israel | 2011/61/EU | 31.01.2011 | - |
| Isle of Man | 2004/411/EC | 28.04.2004 | - |
| Japan | 2019/419 | 23.01.2019 | - |
| Jersey | 2008/393/EC | 08.05.2008 | - |
| New Zealand | 2013/65/EU | 19.12.2012 | - |
| Republic of Korea | 2021/2216 | 17.12.2021 | - |
| Switzerland | 2000/518/EC | 26.07.2000 | - |
| United Kingdom | 2021/1772 | 28.06.2021 | Post-Brexit |
| Uruguay | 2012/484/EU | 21.08.2012 | - |

**USA - EU-U.S. Data Privacy Framework:**
- **Status:** [TODO: Check current status]
- **Certification Required:** Yes
- **Verification:** [TODO: Check list of certified companies]

### Transfers Based on Adequacy Decision

| Recipient | Country | Adequacy Decision | Additional Checks |
|-----------|---------|-------------------|-------------------|
| [TODO: Name] | [TODO: Country] | [TODO: Decision] | [TODO: e.g., Privacy Shield certification] |

**Documentation:** [TODO: Reference to evidence]

## Appropriate Safeguards (Art. 46)

Without an adequacy decision, a transfer is only permissible if appropriate safeguards have been provided and enforceable rights and effective remedies for data subjects are available.

### Standard Contractual Clauses (Art. 46(2)(c))

**Available Standard Contractual Clauses (SCC):**

#### New SCCs (2021)

- **Module 1:** Controller to Controller
- **Module 2:** Controller to Processor
- **Module 3:** Processor to Processor
- **Module 4:** Processor to Controller

**Used SCCs:**

| Transfer | Module | Conclusion Date | Contracting Party | Documentation |
|----------|--------|-----------------|-------------------|---------------|
| [TODO: Description] | [TODO: Module] | [TODO: Date] | [TODO: Name] | [TODO: Link] |

**Mandatory Content of SCCs:**
- Description of transfer
- List of sub-processors (for Module 2/3)
- Technical and organizational measures
- Docking clause (optional)

### Binding Corporate Rules (Art. 46(2)(b))

**Status:** [TODO: BCRs in place? Yes/No]

**If Yes:**
- **Approval Date:** [TODO: Date]
- **Approving Supervisory Authority:** [TODO: Authority]
- **Scope:** [TODO: Group companies]
- **Documentation:** [TODO: Link to BCRs]

### Codes of Conduct and Certification (Art. 46(2)(e), (f))

**Codes of Conduct with Enforcement Mechanism:**
- **Status:** [TODO: In place? Yes/No]
- **Code of Conduct:** [TODO: Name]

**Certification with Enforcement Mechanism:**
- **Status:** [TODO: In place? Yes/No]
- **Certification:** [TODO: Name]

### Other Safeguards (Art. 46(3))

**Ad-hoc Contractual Clauses (with supervisory authority approval):**
- **Status:** [TODO: In place? Yes/No]
- **Approval Date:** [TODO: Date]

## Transfer Impact Assessment (TIA)

### Requirement

Following the Schrems-II judgment (CJEU C-311/18), the controller must assess whether the level of protection in the third country is equivalent to that in the EU.

**TIA Required for:**
- All transfers based on Art. 46 (safeguards)
- Particularly for transfers to USA and other countries with government access possibilities

### TIA Process

#### Step 1: Map Data Transfer

- What data is transferred?
- To whom is data transferred?
- To which country is data transferred?
- Which legal basis is used?

#### Step 2: Assess Legal Situation in Third Country

**To be assessed:**
- Data protection laws in third country
- Government access possibilities (e.g., FISA 702, EO 12333)
- Legal remedies for data subjects
- Practical enforceability of rights

**Documentation:**
[TODO: Summary of legal situation in destination country]

#### Step 3: Evaluate Supplementary Measures

**Technical Measures:**
- End-to-end encryption
- Pseudonymization
- Anonymization
- Encryption in transit and at rest

**Organizational Measures:**
- Contractual commitments
- Transparency towards data subjects
- Training of recipient
- Audits and controls

**Legal Measures:**
- Challenge government requests
- Notification upon government requests
- Transparency reports

#### Step 4: Decision

**Is an adequate level of protection ensured?** [TODO: Yes / No]

**If No:**
- Stop transfer
- Seek alternative solutions (e.g., EU providers)
- Check derogation per Art. 49

### TIA Documentation

| Transfer | TIA Conducted | Date | Result | Supplementary Measures | Next Review |
|----------|---------------|------|--------|------------------------|-------------|
| [TODO] | Yes/No | [TODO] | Adequate/Not adequate | [TODO] | [TODO] |

## Derogations (Art. 49)

Without an adequacy decision or appropriate safeguards, a transfer is only permissible in exceptional cases.

### Derogation Grounds (Art. 49(1))

#### a) Consent

**Requirements:**
- Data subject informed about possible risks
- Consent is freely given, specific, informed and unambiguous

**Use:** [TODO: Yes/No - if Yes, document consents]

#### b) Contract Performance

**Requirements:**
- Transfer necessary for performance of contract
- Or for pre-contractual measures at data subject's request

**Use:** [TODO: Yes/No - if Yes, document cases]

#### c) Public Interest

**Requirements:**
- Transfer necessary for important reasons of public interest

**Use:** [TODO: Yes/No - if Yes, document cases]

#### d) Legal Claims

**Requirements:**
- Transfer necessary for establishment, exercise or defense of legal claims

**Use:** [TODO: Yes/No - if Yes, document cases]

#### e) Vital Interests

**Requirements:**
- Transfer necessary to protect vital interests
- Data subject physically or legally incapable of giving consent

**Use:** [TODO: Yes/No - if Yes, document cases]

#### f) Public Register

**Requirements:**
- Transfer from register intended to provide information to public

**Use:** [TODO: Yes/No - if Yes, document cases]

### Derogation for Occasional Transfers (Art. 49(1) subpara. 2)

**Requirements:**
- Transfer is not repetitive
- Concerns only limited number of persons
- Necessary for compelling legitimate interests
- Interests override data subject's interests
- Controller assessed all circumstances
- Appropriate safeguards provided

**Use:** [TODO: Yes/No - if Yes, document cases]

**Documentation Obligation:** Transfer must be notified to supervisory authority

## Information Obligations

### Information to Data Subjects

Data subjects must be informed about third country transfers:
- In privacy policy (Art. 13, 14)
- Upon access requests (Art. 15)

**To be informed about:**
- Recipients or categories of recipients in third countries
- Third country
- Legal basis of transfer
- Appropriate safeguards (with reference to copy or location)
- For derogations: Compelling legitimate interests

### Transparency

**Publication:**
- List of third country transfers on website
- Information on safeguards used
- Contact for inquiries

## Monitoring and Review

### Regular Review

**Review Frequency:** [TODO: e.g., annually]

**To be checked:**
- Are all third country transfers recorded?
- Are legal bases still current?
- Are safeguards still effective?
- Have legal situation or risks changed?
- Are TIAs current?

### Change Management

**Triggers for Review:**
- New third country transfer
- Change in legal situation in third country
- New court judgments (e.g., CJEU)
- Revocation of adequacy decisions
- Security incidents

## Responsibilities

| Task | Responsible | Accountable | Consulted | Informed |
|------|-------------|-------------|-----------|----------|
| Identification of Third Country Transfers | [TODO] | [TODO] | [TODO] | [TODO] |
| TIA Execution | [TODO] | [TODO] | [TODO] | [TODO] |
| SCC Conclusion | [TODO] | [TODO] | [TODO] | [TODO] |
| Monitoring | [TODO] | [TODO] | [TODO] | [TODO] |

## Links to Other Documents

- **Records of Processing Activities (Art. 30):** Documentation of transfers
- **Data Protection Impact Assessment (Art. 35):** TIA as part of DPIA
- **Processing by Processor (Art. 28):** SCCs with processors in third countries
- **Information Obligations (Art. 13-14):** Transparency towards data subjects

**Next Steps:**
1. Identify all third country transfers
2. Check adequacy decisions
3. Implement appropriate safeguards (SCCs, BCRs)
4. Conduct Transfer Impact Assessments
5. Inform data subjects transparently

