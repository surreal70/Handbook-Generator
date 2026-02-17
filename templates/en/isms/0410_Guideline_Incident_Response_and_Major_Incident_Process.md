# Guideline: Incident Response and Major Incident Process

**Document-ID:** [FRAMEWORK]-0410
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

## 1. Purpose and Scope

This guideline implements the `0400_Policy_Incident_Management.md` and defines:
- Incident response processes and workflows
- Major incident management
- Security incident response and forensics

**Scope:** All incidents at **{{ meta-organisation.name }}**

## 2. Incident Categories

### 2.1 Severity Levels

| Severity | Definition | Examples | Response Time |
|----------|------------|----------|---------------|
| P1 (Critical) | Critical service outage | Production outage, data loss, active cyberattack | 15 minutes |
| P2 (High) | Severe impairment | Performance issues, partial outage | 1 hour |
| P3 (Medium) | Moderate impairment | Individual users affected | 4 hours |
| P4 (Low) | Minor impairment | Cosmetic errors | 1 business day |

### 2.2 Security Incidents

**Categories:**
- Malware infections
- Phishing attacks
- Unauthorized access
- Data breaches
- DDoS attacks
- Insider threats

**All security incidents at least P2**

## 3. Incident Response Process

### 3.1 Detection & Reporting

**Reporting Channels:**
- **IT Support:** {{ meta.support.phone }}, {{ meta.support.email }}
- **Security Team:** {{ meta.security.email }}, {{ meta.security.phone }}
- **Self-Service Portal:** {{ meta.itsm.portal }}

**Required Information:**
- Description of problem
- Affected systems/users
- Time of occurrence
- Impact

### 3.2 Triage & Classification

**Process:**
1. Create incident ticket
2. Determine severity level
3. Assign category
4. Assign to responsible team
5. First response within SLA

**Escalation:**
- P1: Immediate escalation to on-call
- P2: Escalation after 1 hour without progress
- Security incidents: Parallel to security team

### 3.3 Investigation & Diagnosis

**Steps:**
1. Analyze symptoms
2. Check logs
3. Identify affected systems
4. Determine root cause
5. Identify workaround (if possible)

**Documentation:**
- Document all steps in ticket
- Attach logs and screenshots
- Timestamps for all actions

### 3.4 Resolution & Recovery

**Process:**
1. Implement fix or apply workaround
2. Perform functional test
3. Inform users
4. Monitor for recurrence

**Verification:**
- User confirms resolution
- Monitoring shows normal values
- No further reports

### 3.5 Closure & Post-Incident Review

**Closure:**
- Close ticket after user confirmation
- Complete documentation
- Verify categorization

**Post-Incident Review (PIR):**
- Mandatory for P1/P2 incidents
- Within 7 days after closure
- Document lessons learned
- Define improvement measures

## 4. Major Incident Management

### 4.1 Major Incident Criteria

**An incident is "Major" when:**
- Severity P1
- Multiple critical services affected
- Many users affected (> 100)
- Media attention possible
- Regulatory reporting obligation

### 4.2 Major Incident Team

**Roles:**
- **Incident Manager:** Coordination, communication
- **Technical Lead:** Technical solution
- **Communications Lead:** Stakeholder communication
- **Security Lead:** For security incidents
- **Management Representative:** Decisions

**Availability:** 24/7 on-call rotation

### 4.3 Major Incident Process

**Phase 1: Mobilization (0-15 minutes)**
1. Declare major incident
2. Alert major incident team
3. Establish war room (physical or virtual)
4. Set up incident bridge (conference call)

**Phase 2: Containment (15-60 minutes)**
1. Limit impact
2. Implement workaround (if possible)
3. Inform stakeholders
4. Intensify monitoring

**Phase 3: Resolution (variable)**
1. Identify root cause
2. Implement permanent solution
3. Gradual restoration
4. Verification

**Phase 4: Recovery (variable)**
1. All services restored
2. Monitoring at normal state
3. Inform users
4. End major incident

**Phase 5: Post-Incident Review (within 48 hours)**
1. Reconstruct timeline
2. Root cause analysis
3. Lessons learned
4. Define action items
5. Management report

### 4.4 Communication

**Internal Communication:**
- Status updates every 30 minutes
- Stakeholder notifications
- Intranet status page

**External Communication:**
- Customer notifications (if applicable)
- Media statement (if needed)
- Regulatory notifications

## 5. Security Incident Response

### 5.1 Security Incident Response Team (SIRT)

**Members:**
- CISO or Security Lead
- IT security analysts
- IT forensics expert
- Legal/Compliance
- HR (for insider threats)

### 5.2 Security Incident Process

**Phase 1: Preparation**
- Incident response plan current
- Tools and playbooks ready
- Team trained

**Phase 2: Identification**
- Security event detected (SIEM, EDR, etc.)
- Triage: Is it an incident?
- Determine severity

**Phase 3: Containment**
- **Short-term:** Immediate measures (lock account, isolate network)
- **Long-term:** Permanent isolation

**Phase 4: Eradication**
- Remove malware
- Patch vulnerabilities
- Change compromised credentials

**Phase 5: Recovery**
- Restore systems
- Intensify monitoring
- Gradual return to normal operations

**Phase 6: Lessons Learned**
- Post-incident review
- Playbook updates
- Identify training needs

### 5.3 Forensics

**When Required:**
- Data breaches
- Insider threats
- Legal investigations
- Severe security incidents

**Process:**
1. **Preservation:** Secure evidence
2. **Collection:** Collect data (disk images, logs, memory dumps)
3. **Analysis:** Forensic analysis
4. **Reporting:** Forensics report
5. **Chain of Custody:** Complete documentation

**Tools:** {{ meta.security.forensics_tools }}

### 5.4 Reporting Obligations

**Internal:**
- CISO: Immediately
- Management: Within 4 hours
- Data Protection Officer: For data breaches

**External:**
- **GDPR:** Data protection authority within 72 hours (for data breaches)
- **Affected Individuals:** Without undue delay
- **Law Enforcement:** For criminal acts

## 6. Incident Communication

### 6.1 Status Updates

**Frequency:**
- P1: Every 30 minutes
- P2: Every 2 hours
- P3/P4: Daily

**Channels:**
- Email to stakeholders
- Status page ({{ meta.status.url }})
- Intranet notifications

### 6.2 Stakeholder Matrix

| Stakeholder | P1 | P2 | P3 | P4 |
|-------------|----|----|----|----|
| Affected users | Immediately | 1h | 4h | 1d |
| Management | 15min | 2h | - | - |
| CISO (Security) | Immediately | Immediately | 4h | - |
| Customers (external) | 1h | 4h | - | - |

## 7. Compliance and Audit

### 7.1 Key Performance Indicators (KPIs)

| Metric | Target Value |
|--------|--------------|
| P1 response time | < 15 minutes |
| P1 resolution time | < 4 hours |
| Major incident PIR completion | 100% |
| Security incident detection time | < 1 hour |

### 7.2 Audit Evidence

- Incident tickets and logs
- Post-incident review reports
- Communication logs
- Forensics reports (for security incidents)

## 8. References

### Internal Documents
- `0400_Policy_Incident_Management.md`
- `0320_Policy_Logging_and_Monitoring.md`

### External Standards
- **ISO/IEC 27001:2022 Annex A.5.24** - Information security incident management planning
- **ISO/IEC 27001:2022 Annex A.5.25** - Assessment and decision on information security events
- **ISO/IEC 27001:2022 Annex A.5.26** - Response to information security incidents
- **NIST SP 800-61** - Computer Security Incident Handling Guide

**Approved by:** {{ meta.ciso.name }}, CISO  
**Next Review:** {{ meta-handbook.next_review }}

