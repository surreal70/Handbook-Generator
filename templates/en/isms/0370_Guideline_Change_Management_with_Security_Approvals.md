# Guideline: Change Management with Security Approvals

**Document-ID:** [FRAMEWORK]-0370
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

This guideline implements the `0360_Policy_Change_and_Release_Management.md` and defines:
- Change management processes with security reviews
- Change categories and approval workflows
- Rollback procedures and post-implementation reviews

**Scope:** All IT changes at **{{ meta-organisation.name }}**

## 2. Change Categories

### 2.1 Standard Changes
**Definition:** Pre-approved, low-risk, frequent changes

**Examples:**
- Password resets
- Software updates (tested)
- Adding users to standard groups

**Approval:** No individual approval required  
**Security Review:** Not required

### 2.2 Normal Changes
**Definition:** Planned changes with medium risk

**Examples:**
- Configuration changes
- Software installations
- Network changes

**Approval:** Change Advisory Board (CAB)  
**Security Review:** For security-relevant changes

### 2.3 Emergency Changes
**Definition:** Unplanned, urgent changes

**Examples:**
- Critical security patches
- System outages
- Active security incidents

**Approval:** Emergency CAB (ECAB)  
**Security Review:** Retrospectively

## 3. Change Management Process

### 3.1 Change Request (RFC)

**Mandatory Fields:**
- Change title and description
- Justification (business justification)
- Affected systems and services
- Risk assessment
- Rollback plan
- Test results
- Planned time window

**Security-Relevant Additional Fields:**
- Impact on security controls
- Changes to firewall rules
- New external connections
- Privileged access required

### 3.2 Risk Assessment

**Risk Matrix:**
| Likelihood | Impact Low | Impact Medium | Impact High |
|------------|------------|---------------|-------------|
| Low | Low | Low | Medium |
| Medium | Low | Medium | High |
| High | Medium | High | Critical |

**Impact:**
- **Low:** Single user affected
- **Medium:** Department affected
- **High:** Entire organization affected

### 3.3 Security Review

**Triggers:**
- Changes to security systems (firewall, IDS, etc.)
- New external connections
- Privileged access
- Changes to authentication/authorization
- Risk "High" or "Critical"

**Review by IT Security:**
- Review of change request
- Assess security impact
- Recommend additional controls
- Approval or rejection

**SLA:** Security review within 2 business days

### 3.4 Change Advisory Board (CAB)

**Members:**
- Change Manager (chair)
- IT Operations
- IT Security (for security-relevant changes)
- Application Owner (for application changes)
- Business Representative

**Frequency:** Weekly (Tuesday 10:00 AM)

**Tasks:**
- Review and approval of normal changes
- Prioritization in case of conflicts
- Risk assessment
- Schedule planning

### 3.5 Implementation

**Pre-Implementation:**
- Create backup
- Provide rollback plan
- Communication to affected users
- Prepare monitoring

**Implementation:**
- Execute change according to plan
- Document all steps
- Document deviations

**Post-Implementation:**
- Functional test
- Monitor for errors (24 hours)
- Update change status
- Complete documentation

### 3.6 Rollback

**Triggers:**
- Functional test failed
- Critical errors in production
- Security issues detected

**Process:**
1. Rollback decision by Change Manager
2. Rollback according to rollback plan
3. Verify restoration
4. Root cause analysis
5. New change request for retry

## 4. Emergency Changes

### 4.1 Emergency CAB (ECAB)

**Members:**
- Change Manager or deputy
- IT Operations (on-call)
- CISO or IT Security (on-call)

**Availability:** 24/7

**Approval Process:**
- Telephone or email approval
- Documentation retrospectively
- Review in next regular CAB

### 4.2 Emergency Change Process

**Accelerated Workflow:**
1. **Initiation:** Incident Manager creates emergency RFC
2. **Assessment:** ECAB assesses urgency and risk
3. **Approval:** ECAB approves (or rejects)
4. **Implementation:** Immediate execution
5. **Documentation:** Retrospective completion
6. **Review:** In next CAB

**Security Review:**
- For critical security patches: Retrospectively
- For other emergency changes: Before implementation (if possible)

## 5. Security Controls

### 5.1 Segregation of Duties

**Principle:** No person may request, approve, and implement a change

**Roles:**
- **Requester:** Requests change
- **Approver:** Approves change (CAB)
- **Implementer:** Executes change
- **Reviewer:** Reviews post-implementation

### 5.2 Privileged Changes

**Additional Requirements:**
- Four-eyes principle during implementation
- Session recording
- Detailed documentation
- Post-implementation security review

### 5.3 Firewall Changes

**Special Requirements:**
- Justification for each new rule
- Document source and destination IP/port
- Time limitation (where possible)
- Regular review (quarterly)

**Approval:**
- IT Security: Mandatory
- Network Team: Technical feasibility
- Application Owner: Business justification

## 6. Testing and Validation

### 6.1 Test Environments

**Requirements:**
- Dev/test environment for all critical systems
- As identical to production as possible
- Isolated from production

**Test Process:**
1. Implement change in dev/test
2. Perform functional test
3. Performance test (if needed)
4. Security test (for security-relevant changes)
5. Document test results

### 6.2 Security Testing

**For Security-Relevant Changes:**
- Vulnerability scan after change
- Penetration test (for critical changes)
- Code review (for software changes)
- Configuration review

## 7. Documentation and Audit

### 7.1 Change Documentation

**Mandatory Documentation:**
- Change Request (RFC)
- Approvals
- Implementation log
- Test results
- Post-implementation review

**Retention:** {{ meta-handbook.retention_change_years }} years

### 7.2 Post-Implementation Review (PIR)

**Execution:**
- Within 7 days after implementation
- For all normal and emergency changes

**Content:**
- Success of implementation
- Problems encountered
- Lessons learned
- Improvement suggestions

### 7.3 Compliance and Audit

**Key Performance Indicators (KPIs):**
| Metric | Target Value |
|--------|--------------|
| Successful changes | > 95% |
| Emergency changes | < 10% of all changes |
| Unauthorized changes | 0 |
| PIR completion rate | 100% |

**Audit Evidence:**
- Change logs
- Approvals
- Security reviews
- PIR reports

## 8. References

### Internal Documents
- `0360_Policy_Change_and_Release_Management.md`
- `0400_Policy_Incident_Management.md`

### External Standards
- **ISO/IEC 27001:2022 Annex A.8.32** - Change management
- **ITIL 4** - Change Enablement Practice

**Approved by:** {{ meta-organisation-roles.role_CISO }}, CISO  
**Next Review:** {{ meta-handbook.next_review }}

