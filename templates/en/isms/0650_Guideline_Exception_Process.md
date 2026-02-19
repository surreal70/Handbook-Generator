# Guideline: Exception Process

**Document-ID:** [FRAMEWORK]-0650
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

## 1. Purpose and Scope

This guideline implements `0640_Policy_Exceptions_and_Risk_Waivers.md` and defines:
- Exception process for security policies
- Risk waiver procedures
- Compensating controls

**Scope:** All security policies at **{{ meta-organisation.name }}**

## 2. Exception Categories

### 2.1 Temporary Exceptions

**Definition:** Time-limited deviation from policy

**Examples:**
- Delayed patching (due to compatibility issues)
- Temporary firewall rule for project
- Delayed compliance (during migration)

**Maximum Duration:** 12 months

### 2.2 Permanent Exceptions

**Definition:** Permanent deviation from policy

**Examples:**
- Legacy systems that cannot meet baseline
- Special business requirements
- Technical impossibility

**Review Frequency:** Annually

### 2.3 Emergency Exceptions

**Definition:** Immediate exception in emergencies

**Examples:**
- Critical business requirement
- System outage remediation
- Security incident response

**Retroactive Approval:** Within 48 hours

## 3. Exception Process

### 3.1 Request Submission

**Request via:** {{ meta-handbook.itsm_portal }} (ticketing system)

**Mandatory Information:**
- Affected policy/guideline
- Description of deviation
- Justification (business justification)
- Affected systems/processes
- Risk assessment
- Proposed compensating controls
- Desired duration

**Requester:** System owner or department head

### 3.2 Risk Assessment

**Conducted by:** IT Security Team

**Assessment Criteria:**
- Likelihood of security incident
- Potential impact
- Affected assets and data
- Existing controls
- Proposed compensating controls

**Risk Matrix:**
| Likelihood | Low Impact | Medium Impact | High Impact |
|------------|-----------|---------------|-------------|
| Low | Low | Low | Medium |
| Medium | Low | Medium | High |
| High | Medium | High | Critical |

### 3.3 Compensating Controls

**Definition:** Alternative security measures to minimize risk

**Examples:**
- Network isolation (for missing patches)
- Increased monitoring (for weaker authentication)
- Manual processes (for missing automation)
- Additional access restrictions

**Requirement:**
- Compensating controls must reduce risk to acceptable level
- Documentation of effectiveness

### 3.4 Approval

**Approval Levels:**

| Risk | Approver | SLA |
|------|----------|-----|
| Low | IT Security Manager | 3 business days |
| Medium | CISO | 5 business days |
| High | CISO + CIO | 7 business days |
| Critical | CISO + CIO + Executive Management | 10 business days |

**Approval Criteria:**
- Business justification comprehensible
- Risk acceptable (with compensating controls)
- No alternative available
- Time-limited (for temporary exceptions)

**Rejection:**
- Justification required
- Propose alternative solutions

### 3.5 Documentation

**Exception Register:**
- All approved exceptions
- Requester, approver, date
- Risk assessment
- Compensating controls
- Expiration date
- Review date

**Storage Location:** {{ meta-handbook.compliance_exception_register }}

## 4. Monitoring and Review

### 4.1 Ongoing Monitoring

**Responsibility:** IT Security Team

**Activities:**
- Verify effectiveness of compensating controls
- Compliance with exception conditions
- Incidents related to exceptions

**Frequency:** Monthly (for critical exceptions), quarterly (for others)

### 4.2 Regular Review

**Temporary Exceptions:**
- Review 30 days before expiration
- Decision: Extend, terminate, make permanent

**Permanent Exceptions:**
- Annual review
- Verify necessity
- Update risk assessment

**Emergency Exceptions:**
- Review within 7 days after approval
- Regularization or termination

### 4.3 Escalation

**In Case of Problems:**
- Compensating controls ineffective
- Risk increased
- Incidents related to exception

**Escalate to:**
- CISO (immediately)
- Risk Committee (for critical exceptions)

## 5. Exception Termination

### 5.1 Planned Termination

**Upon Expiration:**
1. Notification to requester (30 days in advance)
2. Create remediation plan
3. Implement remediation
4. Verification
5. Close exception

### 5.2 Early Termination

**Reasons:**
- Risk no longer acceptable
- Compensating controls ineffective
- Alternative solution available
- Business requirement no longer exists

**Process:**
1. Decision by CISO
2. Notification to requester
3. Immediate remediation (or system shutdown)
4. Documentation

## 6. Reporting

### 6.1 Monthly Exception Report

**Contents:**
- Number of active exceptions (by risk)
- New exceptions in month
- Expired exceptions
- Overdue reviews
- Top exceptions by risk

**Recipients:** CISO, CIO, Risk Committee

### 6.2 Quarterly Management Report

**Contents:**
- Trend analysis
- Exceptions by category/department
- Risk posture
- Improvement measures

**Recipients:** Executive Management, Audit Committee

## 7. Compliance and Audit

### 7.1 Metrics (KPIs)

| Metric | Target Value |
|--------|--------------|
| Exceptions with current review | 100% |
| Overdue exceptions | 0 |
| Exceptions with compensating controls | 100% |
| Average exception duration | < 6 months |

### 7.2 Audit Evidence

- Exception Register
- Requests and approvals
- Risk assessments
- Review protocols
- Monitoring reports

## 8. Examples

### 8.1 Example: Delayed Patching

**Scenario:** Critical patch causes compatibility issues with business application

**Request:**
- Policy: Patch Management (critical patches within 7 days)
- Deviation: Delay by 30 days
- Justification: Compatibility issue, vendor working on fix
- Risk: High (known exploit)

**Compensating Controls:**
- Network isolation of affected system
- IPS signature activated
- Increased monitoring
- Access restrictions

**Approval:** CISO + CIO  
**Duration:** 30 days  
**Review:** Weekly

### 8.2 Example: Legacy System

**Scenario:** Legacy system cannot meet security baseline

**Request:**
- Policy: Security Baseline (CIS Benchmark Level 1)
- Deviation: Outdated OS, no patches available
- Justification: Critical business application, no migration possible (short-term)
- Risk: High

**Compensating Controls:**
- Dedicated VLAN (isolated)
- Firewall rules (only required connections)
- No internet access
- Read-only access for standard users
- Increased monitoring and logging
- Annual penetration tests

**Approval:** CISO + CIO + Executive Management  
**Duration:** Permanent (until migration)  
**Review:** Annually

## 9. References

### Internal Documents
- `0640_Policy_Exceptions_and_Risk_Waivers.md`
- All security policies and guidelines

### External Standards
- **ISO/IEC 27001:2022 Annex A.5.1** - Policies for information security
- **NIST SP 800-53** - Security and Privacy Controls (Tailoring)

**Approved by:** {{ meta-organisation-roles.role_CISO }}, CISO  
**Next Review:** {{ meta-handbook.next_review }}

