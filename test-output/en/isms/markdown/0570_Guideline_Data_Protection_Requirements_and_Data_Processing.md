# Guideline: Data Protection Requirements and Data Processing

**Document ID:** 0570  
**Document Type:** Guideline (detailed)  
**Associated Policy:** 0560_Policy_Data_Protection_Interfaces.md  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.5.34  
**Owner:** {{ meta.dpo.name }}  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** {{ meta.document.date }}

---

## 1. Purpose and Scope

This guideline specifies the `0560_Policy_Data_Protection_Interfaces.md` and defines:
- GDPR compliance requirements
- Data processing processes
- Data subject rights and their implementation

**Scope:** All personal data at **AdminSend GmbH**

## 2. GDPR Principles

### 2.1 Lawfulness, Fairness and Transparency

**Legal Bases (Art. 6 GDPR):**
- Consent (Art. 6(1)(a))
- Contract performance (Art. 6(1)(b))
- Legal obligation (Art. 6(1)(c))
- Legitimate interest (Art. 6(1)(f))

**Documentation:**
- Document legal basis for each processing
- Record of processing activities (RoPA)

### 2.2 Purpose Limitation

**Principle:**
- Collect data only for specified, explicit purposes
- No further processing for other purposes (without new legal basis)

### 2.3 Data Minimization

**Principle:**
- Collect only necessary data
- Regular review of necessity

### 2.4 Accuracy

**Measures:**
- Keep data current
- Correct inaccurate data
- Processes for data updates

### 2.5 Storage Limitation

**Deletion Concept:**
- Define retention periods
- Automatic deletion after expiration
- Documentation of deletion

**Details:** See `0590_Guideline_Records_Retention_and_Secure_Deletion.md`

### 2.6 Integrity and Confidentiality

**Technical Measures:**
- Encryption
- Access control
- Logging and monitoring

### 2.7 Accountability

**Proof Obligation:**
- Documentation of all measures
- Data Protection Impact Assessment (DPIA)
- Record of processing activities (RoPA)

## 3. Record of Processing Activities (RoPA)

### 3.1 Mandatory Information (Art. 30 GDPR)

**For Each Processing:**
- Name and contact details of controller
- Purposes of processing
- Categories of data subjects
- Categories of personal data
- Categories of recipients
- Third country transfers
- Deletion periods
- Technical and organizational measures (TOMs)

### 3.2 RoPA Maintenance

**Responsibility:**
- Data Protection Officer coordinates
- Departments provide information
- Annual update (minimum)

**Tool:** {{ meta.dpo.vvt_tool }}

## 4. Data Protection Impact Assessment (DPIA)

### 4.1 When Required?

**Mandatory for (Art. 35 GDPR):**
- Systematic extensive evaluation of personal aspects (profiling)
- Extensive processing of special categories (Art. 9)
- Systematic extensive monitoring of public areas

**Examples:**
- New CRM systems with profiling
- Video surveillance
- Biometric authentication

### 4.2 DPIA Process

**Steps:**
1. Description of processing
2. Assessment of necessity and proportionality
3. Risk assessment for data subjects
4. Remedial measures
5. Consultation with Data Protection Officer
6. Documentation

**For High Risk:**
- Consultation with supervisory authority before processing

## 5. Data Subject Rights

### 5.1 Right of Access (Art. 15 GDPR)

**Process:**
1. Request via email to {{ meta.dpo.email }}
2. Identity verification
3. Compilation of information
4. Response within 1 month

**Information to Provide:**
- Processing purposes
- Categories of personal data
- Recipients
- Storage duration
- Data subject rights
- Copy of data

### 5.2 Right to Rectification (Art. 16 GDPR)

**Process:**
1. Request for rectification
2. Verification of accuracy
3. Correction within 1 month
4. Notification to recipients (if required)

### 5.3 Right to Erasure (Art. 17 GDPR)

**Deletion Grounds:**
- Purpose fulfilled
- Consent withdrawn
- Objection to processing
- Unlawful processing

**Exceptions:**
- Legal retention obligations
- Assertion of legal claims

### 5.4 Right to Restriction (Art. 18 GDPR)

**Restriction Instead of Deletion:**
- When accuracy is contested
- For unlawful processing (data subject does not want deletion)
- For objection (during review)

### 5.5 Right to Data Portability (Art. 20 GDPR)

**Prerequisites:**
- Processing based on consent or contract
- Automated processing

**Format:**
- Structured, commonly used, machine-readable (e.g., CSV, JSON)

### 5.6 Right to Object (Art. 21 GDPR)

**For Legitimate Interest:**
- Data subject can object
- Balancing required
- Stop processing (unless compelling grounds)

**For Direct Marketing:**
- Objection possible at any time
- Stop processing immediately

## 6. Data Processing

### 6.1 Data Processing Agreement (DPA)

**Mandatory for:**
- Service provider processes personal data on behalf
- Cloud providers, IT service providers, etc.

**Mandatory Contents (Art. 28 GDPR):**
- Subject matter and duration
- Nature and purpose of processing
- Categories of personal data
- Obligations and rights of controller
- Technical and organizational measures (TOMs)
- Sub-processors
- Support obligations

### 6.2 Technical and Organizational Measures (TOMs)

**Categories:**
- Physical access control
- System access control
- Data access control
- Disclosure control
- Input control
- Job control
- Availability control
- Separation control

**Documentation:**
- TOMs for each processing
- Regular review and adjustment

## 7. Data Breaches

### 7.1 Notification Obligation (Art. 33 GDPR)

**To Supervisory Authority:**
- Within 72 hours of becoming aware
- If risk to data subjects

**Exceptions:**
- No risk to data subjects (e.g., encrypted data)

### 7.2 Notification to Data Subjects (Art. 34 GDPR)

**Mandatory for:**
- High risk to data subjects
- Without undue delay

**Content:**
- Nature of breach
- Contact point (Data Protection Officer)
- Likely consequences
- Measures taken

### 7.3 Documentation

**Register of Data Breaches:**
- Document all breaches (including non-notifiable)
- Facts, impacts, remedial measures
- Proof for supervisory authority

## 8. International Data Transfers

### 8.1 Third Country Transfer

**Permitted with:**
- EU Commission adequacy decision
- Standard Contractual Clauses (SCCs)
- Binding Corporate Rules (BCRs)
- Consent

### 8.2 Schrems II Compliance

**Transfer Impact Assessment (TIA):**
- Review legal situation in third country
- Implement additional measures (e.g., encryption)
- Documentation

## 9. Compliance and Audit

### 9.1 Metrics (KPIs)

| Metric | Target Value |
|--------|--------------|
| Data subject requests (response time) | < 1 month |
| RoPA currency | < 12 months |
| DPIA completion (new systems) | 100% |
| Data breaches (notification) | < 72 hours |

### 9.2 Audit Evidence

- Record of processing activities (RoPA)
- Data Protection Impact Assessments (DPIA)
- Data Processing Agreements (DPA)
- Data subject requests and responses
- Register of data breaches

## 10. References

### Internal Documents
- `0560_Policy_Data_Protection_Interfaces.md`
- `0590_Guideline_Records_Retention_and_Secure_Deletion.md`

### External Standards
- **ISO/IEC 27001:2022 Annex A.5.34** - Privacy and protection of PII
- **GDPR (EU 2016/679)** - General Data Protection Regulation
- **BDSG** - German Federal Data Protection Act

---

**Approved by:** {{ meta.dpo.name }}, Data Protection Officer  
**Next Review:** {{ meta.document.next_review }}
