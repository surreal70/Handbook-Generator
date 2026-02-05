# Policy: Exceptions and Risk Waivers



**Document ID:** 0640  
**Document Type:** Policy (abstract)  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.5.1, A.6.1.2 (incl. Amendment 1:2024)  
**Owner:** Thomas Weber  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** {{ meta.document.date }}  
**Next Review:** {{ meta.document.next_review }}

---

## 1. Purpose

This policy defines the process for exceptions and risk waivers from security policies of **AdminSend GmbH**. It ensures that exceptions are appropriately justified, approved, documented, and monitored.

## 2. Scope

This policy applies to:

- **Organizational Units:** All departments and locations of AdminSend GmbH
- **Policies:** All security policies and standards
- **Systems:** All IT systems and applications
- **Processes:** All security-relevant processes
- **Locations:** {{ netbox.site.name }} and all other operational sites

**Exceptions:** This policy itself is not subject to an exception process.

## 3. Policy Statements

### 3.1 Exceptions as Exception
Exceptions to security policies are the exception, not the rule. Policies must generally be complied with.

### 3.2 Formal Exception Process
Exceptions must be requested through a formal process. Informal or verbal exceptions are not permitted.

### 3.3 Justification Requirement
Every exception must be justified:
- Business necessity
- Technical impossibility
- Disproportionate effort
- Time limitation

### 3.4 Risk Assessment
A risk assessment is conducted for every exception. Risks are identified, evaluated, and documented.

### 3.5 Compensating Controls
Exceptions require compensating controls. Compensating controls reduce residual risk to an acceptable level.

### 3.6 Approval Requirement
Exceptions must be approved by authorized persons:
- **Low Risk:** CISO or deputy
- **Medium Risk:** CISO + Business Owner
- **High Risk:** CISO + CIO + Management

### 3.7 Time Limitation
Exceptions are generally time-limited. Maximum duration: 12 months. Extensions require renewed approval.

### 3.8 Documentation
All exceptions are centrally documented (exception register). Documentation includes:
- Requester and date
- Affected policy/standard
- Justification
- Risk assessment
- Compensating controls
- Approver and date
- Duration and review date

### 3.9 Monitoring and Review
Exceptions are reviewed regularly (at least quarterly). Exceptions no longer needed are withdrawn.

## 4. Roles and Responsibilities

### RACI Matrix: Exceptions and Risk Waivers

| Activity | CISO | CIO | Business Owner | Risk Manager | ISMS Team |
|----------|------|-----|----------------|--------------|-----------|
| Policy Creation | R/A | C | C | C | C |
| Exception Request | I | I | R | I | C |
| Risk Assessment | R/A | C | C | R | C |
| Compensating Controls | R/A | C | R | C | C |
| Approval (Low) | R/A | I | I | I | I |
| Approval (Medium) | R/A | I | R/A | C | I |
| Approval (High) | R/A | R/A | R/A | C | I |
| Exception Register | C | I | I | C | R/A |
| Monitoring & Review | R/A | C | C | C | R |

**Legend:** R = Responsible (Execution), A = Accountable (Ownership), C = Consulted, I = Informed

### Key Roles

- **Policy Owner:** Thomas Weber (CISO)
- **CIO:** Anna Schmidt
- **Risk Manager:** {{ meta.risk.manager }}
- **ISMS Team:** {{ meta.isms.team }}
- **Requester:** Business Owner, IT Operations
- **Control/Audit Function:** ISMS, Internal Audit

## 5. Derived Documents (Guidelines/Standards/Processes)

Implementation details are defined in subordinate documents:

### Related Guidelines
- **0650_Guideline_Exception_Process.md** - Detailed implementation guideline
- `0060_ISMS_Risk_Management_Methodology.md` - Risk Management Methodology
- `0080_ISMS_Risk_Register_Template.md` - Risk Register

### Related Standards/Baselines
- Exception Request Template
- Risk Assessment Template
- Compensating Controls Catalog
- Exception Register

### Related Processes
- Exception Request Process
- Risk Assessment Process
- Approval Process
- Monitoring and Review Process

## 6. Compliance, Monitoring and Enforcement

### Metrics and KPIs
- Number of active exceptions
- Average duration of exceptions
- Number of expired exceptions (Target: 0)
- Number of extended exceptions
- Exceptions by risk category (Low/Medium/High)
- Review compliance (Target: 100% quarterly)
- Number of withdrawn exceptions

### Evidence and Proof
- Exception Register
- Exception requests and approvals
- Risk assessments
- Compensating controls documentation
- Review protocols
- Audit logs for exceptions

### Consequences of Violations
Violations of this policy are handled according to applicable HR and compliance processes:
- **Unapproved Exceptions:** Immediate compliance establishment or system shutdown
- **Missing Documentation:** Remediation, compliance investigation
- **Expired Exceptions:** Immediate compliance establishment or extension request
- **Repeated Violations:** Employment consequences, escalation to management

## 7. Exceptions

This policy itself is not subject to an exception process. Changes to this policy require management approval.

## 8. References

### Internal Documents
- `0010_ISMS_Information_Security_Policy.md` - ISMS Policy
- `0650_Guideline_Exception_Process.md` - Detailed Guideline
- `0060_ISMS_Risk_Management_Methodology.md` - Risk Management Methodology
- `0080_ISMS_Risk_Register_Template.md` - Risk Register

### External Standards and Regulations
- **ISO/IEC 27001:2022 Annex A.5.1** - Policies for information security
- **ISO/IEC 27001:2022 Annex A.6.1.2** - Segregation of duties
- **ISO/IEC 27005** - Information security risk management
- **NIST SP 800-37** - Risk Management Framework
- **COBIT 2019** - APO12 (Managed Risk)

---

**Approved by:**  
{{ meta.management.ceo }}, Executive Management  
Date: {{ meta.document.approval_date }}

**Next Review:** {{ meta.document.next_review }} (annually or as needed)
