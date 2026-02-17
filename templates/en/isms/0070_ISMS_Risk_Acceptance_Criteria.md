# Risk Criteria and Risk Acceptance

**Document-ID:** [FRAMEWORK]-0070
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
TEMPLATE AUTHOR NOTE:
This document defines risk acceptance criteria and the process for accepting risks.
It establishes thresholds for acceptable risk levels and defines who can accept
risks at different levels.
-->

**Document ID:** 0070  
**Document Type:** ISMS Foundation Document  
**Standard Reference:** ISO/IEC 27001:2022 Clause 6.1.2  
**Owner:** {{ meta.ciso.name }}  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** {{ meta-handbook.modifydate }}  
**Next Review:** {{ meta-handbook.next_review }}

## 1. Risk Appetite and Tolerance

### 1.1 Risk Appetite

**{{ meta-organisation.name }}** defines its risk appetite as follows:

**General Risk Appetite:** [TODO: Conservative / Moderate / Progressive]

**Tolerance Thresholds by Risk Level:**

| Risk Level | Risk Score | Acceptable | Treatment Required |
|------------|-------------|------------|-------------------|
| Very Low | 1-2 | Yes | Monitoring |
| Low | 3-6 | Yes | Monitoring |
| Medium | 7-12 | Conditional | Risk treatment recommended |
| High | 13-20 | No | Risk treatment required |
| Very High | 21-25 | No | Immediate risk treatment |

### 1.2 Acceptance Criteria

**Automatically Acceptable:**
- Risk score ≤ 6 (Low)
- No compliance violations
- No critical assets affected

**Conditionally Acceptable:**
- Risk score 7-12 (Medium)
- With compensating controls
- Time-limited (max. 12 months)

**Not Acceptable:**
- Risk score ≥ 13 (High/Very High)
- Compliance violations
- Critical assets without protection measures

## 2. Assessment Dimensions

### 2.1 CIA Triad

**Confidentiality:**
- Protection against unauthorized disclosure
- Classification: Public, Internal, Confidential, Strictly Confidential

**Integrity:**
- Protection against unauthorized modification
- Correctness and completeness of information

**Availability:**
- Ensuring access when needed
- RTO/RPO requirements

### 2.2 Additional Dimensions

**Legal and Regulatory:**
- GDPR compliance
- Industry-specific regulation
- Contractual obligations

**Reputation:**
- Impact on corporate image
- Customer trust
- Media coverage

## 3. Acceptance Process

### 3.1 Acceptance Authorities

| Risk Level | Accepted By | Documentation | Approval |
|------------|-------------|---------------|----------|
| Very Low / Low | CISO | Risk register | CISO |
| Medium | CISO | Risk register + justification | CISO + CIO |
| High | Management | Risk register + formal risk acceptance | Management |
| Very High | Management | Risk register + formal risk acceptance + action plan | Management |

### 3.2 Documentation Requirements

**Minimum Information:**
- Risk ID and description
- Risk assessment (likelihood, impact, score)
- Justification for acceptance
- Compensating controls (if any)
- Acceptance date and validity period
- Accepting person

**Document:** See `0080_ISMS_Risk_Register_Template.md`

### 3.3 Duration of Acceptances

**Time Limits:**
- Low risks: Unlimited (with annual review)
- Medium risks: Max. 12 months
- High risks: Max. 6 months
- Very high risks: Max. 3 months (exception)

**Renewal:**
- Requires re-assessment and approval
- Justification for renewal required

### 3.4 Review of Accepted Risks

**Regular Review:**
- Quarterly: All accepted risks
- Annually: Complete re-assessment

**Triggers for Unscheduled Review:**
- New threats or vulnerabilities
- Change in business environment
- Security incidents
- Audit findings

## 4. References

### Internal Documents
- `0060_ISMS_Risk_Management_Methodology.md` - Risk Management Methodology
- `0080_ISMS_Risk_Register_Template.md` - Risk Register
- `0090_ISMS_Risk_Treatment_Plan_RTP_Template.md` - Risk Treatment Plan

### External Standards
- **ISO/IEC 27001:2022** - Clause 6.1.2: Information security risk assessment
- **ISO/IEC 27005:2022** - Information security risk management

**Approved by:**  
{{ meta.management.ceo }}, Management  
Date: {{ meta-handbook.modifydate }}

**Next Review:** {{ meta-handbook.next_review }}

