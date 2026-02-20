# Data Breach Response Plan (Template)

**Document-ID:** 0600
**Organisation:** AdminSend GmbH
**Owner:** [TODO]
**Approved by:** [TODO]
**Revision:** [TODO]
**Author:** Handbook-Generator
**Status:** Draft
**Classification:** Internal
**Last Update:** [TODO]
**Template Version:** [TODO]

---

---



## Purpose

This response plan defines the steps for managing data breaches at AdminSend GmbH. It ensures that data breaches are quickly detected, assessed, and handled according to GDPR Art. 33-34.

## Scope

This plan applies to all data breaches affecting personal data processed by AdminSend GmbH.

## Breach Response Team

### Core Team

| Role | Name | Contact | Responsibilities |
|------|------|---------|-----------------|
| **Incident Commander** | [TODO] | [TODO: Phone, Email] | Overall responsibility, decisions |
| **Data Protection Officer** | [TODO] | [TODO: Phone, Email] | Legal assessment, notification obligation |
| **IT Security Lead** | [TODO] | [TODO: Phone, Email] | Technical analysis, containment |
| **Legal Counsel** | [TODO] | [TODO: Phone, Email] | Legal advice |
| **Communications Lead** | [TODO] | [TODO: Phone, Email] | Internal/external communication |

### Extended Stakeholders

| Role | Name | Contact | When to involve |
|------|------|---------|-----------------|
| **Management** | [TODO] | [TODO] | For high risk |
| **HR** | [TODO] | [TODO] | For employee data |
| **Compliance** | [TODO] | [TODO] | For regulatory questions |
| **PR/Marketing** | [TODO] | [TODO] | For public communication |

## Breach Response Process

### Phase 1: Detection and Reporting (0-2 hours)

#### 1.1 Detect Breach

**Detection Sources:**
- Monitoring systems and alerts
- Employee reports
- External reports (customers, partners)
- Audit findings
- Media reports

#### 1.2 Initial Report

**Who reports:**
- Any employee who discovers a potential data breach

**To whom:**
- IT Security: [TODO: Email/Phone]
- Data Protection Officer: [TODO: Email/Phone]

**Report Form:**
```
INITIAL BREACH REPORT

Reporter: [Name, Department, Contact]
Date/Time of Discovery: [YYYY-MM-DD HH:MM]
Discovery Method: [Monitoring / Employee / External / Audit / Other]

Brief Description:
[What happened?]

Affected Systems:
[Which systems are affected?]

Affected Data (initial assessment):
[What type of data?]

Number of Data Subjects (estimate):
[Approximate number]

Immediate Actions Taken:
[What has been done already?]
```

#### 1.3 Activate Breach Response Team

**Incident Commander:**
- Activates core team
- Schedules initial meeting (within 2 hours)
- Creates Breach-ID: `BREACH-[YYYY]-[NNN]`

### Phase 2: Assessment and Containment (2-12 hours)

#### 2.1 Initial Assessment

**Checklist:**
- [ ] Is there actually a data breach?
- [ ] Which category: Confidentiality / Integrity / Availability?
- [ ] What data is affected?
- [ ] How many persons are affected?
- [ ] Are special categories (Art. 9) affected?
- [ ] How did the breach occur?
- [ ] Is the breach still active?

**Documentation:**
- Document all findings in breach register
- Secure screenshots and logs
- Forensic preservation if needed

#### 2.2 Immediate Containment

**Technical Measures:**
- [ ] Isolate affected systems
- [ ] Block access
- [ ] Reset passwords
- [ ] Close security gaps
- [ ] Prevent further data loss

**Responsible:** IT Security Lead

**Timeframe:** Within 4 hours

#### 2.3 Scope Determination

**To clarify:**
- Exact number of affected persons
- Exact data categories
- Period of breach
- Cause of breach
- Potential impacts

**Methods:**
- Log analysis
- Database queries
- System forensics
- Interviews with involved parties

### Phase 3: Risk Assessment (12-24 hours)

#### 3.1 Assess Risk to Data Subjects

**Assessment Criteria:**

| Criterion | Assessment | Points |
|-----------|------------|--------|
| **Type of Data** | | |
| - General contact data | Low | 1 |
| - Financial data, credentials | Medium | 2 |
| - Special categories (Art. 9) | High | 3 |
| **Number of Data Subjects** | | |
| - < 100 persons | Low | 1 |
| - 100-1,000 persons | Medium | 2 |
| - > 1,000 persons | High | 3 |
| **Protective Measures** | | |
| - Encrypted, pseudonymized | Low | 1 |
| - Partially protected | Medium | 2 |
| - Unencrypted, plaintext | High | 3 |
| **Data Subjects** | | |
| - Employees (internal) | Low | 1 |
| - Customers, partners | Medium | 2 |
| - Children, vulnerable groups | High | 3 |

**Overall Risk:**
- 4-6 points: Low risk
- 7-9 points: Medium risk (notification required)
- 10-12 points: High risk (notification + communication required)

#### 3.2 Check Notification Obligation

**Decision Tree:**

```
Data breach confirmed?
├─ No → Document, no further action required
└─ Yes → Risk to rights and freedoms?
    ├─ No (< 7 points) → Only document
    └─ Yes (≥ 7 points) → Notification to supervisory authority required
        └─ High risk (≥ 10 points)?
            ├─ No → Only notification
            └─ Yes → Notification + Communication to data subjects
```

**Responsible:** Data Protection Officer

### Phase 4: Notification and Communication (24-72 hours)

#### 4.1 Notification to Supervisory Authority (if required)

**Deadline:** 72 hours from awareness

**Competent Authority:**
- Name: [TODO: e.g., Data Protection Authority]
- Notification Portal: [TODO: URL]
- Contact: [TODO: Email, Phone]

**Prepare Notification:**
- Use Template 0610 (Breach Notification Template)
- Compile all required information
- Have Data Protection Officer review
- Obtain management approval

**Responsible:** Data Protection Officer

#### 4.2 Communication to Data Subjects (if required)

**Prerequisite:** High risk (≥ 10 points)

**Exceptions (no communication):**
- Data was encrypted/pseudonymized
- Subsequent measures eliminate high risk
- Disproportionate effort (then public communication)

**Prepare Communication:**
- Use Template 0620 (Breach Communication Template)
- Clear, understandable language
- Concrete action recommendations
- Contact options

**Communication Channels:**
- Email (preferred)
- Letter (if no email)
- Public announcement (if disproportionate effort)

**Responsible:** Communications Lead, Data Protection Officer

#### 4.3 Internal Communication

**To inform:**
- Management
- Affected departments
- Works council (for employee data)
- All employees (if needed)

**Communication Plan:**
- Initial information: Within 24 hours
- Regular updates: Daily during active phase
- Final report: After incident closure

### Phase 5: Recovery (72 hours - weeks)

#### 5.1 Restore Systems

**Checklist:**
- [ ] Security gaps closed
- [ ] Systems patched/updated
- [ ] Access controls reviewed
- [ ] Monitoring enhanced
- [ ] Backup strategy reviewed

**Responsible:** IT Security Lead

#### 5.2 Preventive Measures

**To implement:**
- Technical improvements
- Process adjustments
- Training
- Enhanced monitoring

### Phase 6: Post-Incident Review (After completion)

#### 6.1 Post-Breach Review

**Use Template 0640 (Post-Breach Review Template)**

**To be conducted within:** 2 weeks after incident closure

**Participants:**
- Breach Response Team
- Affected departments
- Management

**Topics:**
- What went well?
- What went poorly?
- Lessons learned
- Improvement measures

#### 6.2 Complete Documentation

**Checklist:**
- [ ] Breach register updated
- [ ] All notifications archived
- [ ] Timeline documented
- [ ] Costs recorded
- [ ] Measures documented

**Retention Period:** At least 3 years

## Communication Guidelines

### Internal Communication

**Principles:**
- Transparent but confidential
- Fact-based
- Regular updates
- Clear responsibilities

### External Communication

**Principles:**
- Only through authorized spokespersons
- Coordinated with Legal and Data Protection Officer
- No speculation
- Focus on measures and support

**Media Inquiries:**
- All inquiries to Communications Lead
- No spontaneous statements
- Preparation of Q&A

## Escalation

### Escalation Levels

**Level 1: Routine**
- Low risk
- < 100 data subjects
- No special categories
- Core team sufficient

**Level 2: Elevated**
- Medium risk
- 100-1,000 data subjects
- Notification obligation
- Inform management

**Level 3: Critical**
- High risk
- > 1,000 data subjects
- Special categories
- Communication obligation
- Actively involve management
- Consider external advisors

**Level 4: Crisis**
- Very high risk
- Massive impact
- Public interest
- Activate crisis management
- External PR support
- Inform supervisory board

## Contacts and Resources

### Internal Contacts

| Role | Name | Phone | Email | Availability |
|------|------|-------|-------|--------------|
| Incident Commander | [TODO] | [TODO] | [TODO] | 24/7 |
| Data Protection Officer | [TODO] | [TODO] | [TODO] | 24/7 |
| IT Security Lead | [TODO] | [TODO] | [TODO] | 24/7 |
| Legal Counsel | [TODO] | [TODO] | [TODO] | Business hours |
| Communications Lead | [TODO] | [TODO] | [TODO] | Business hours |

### External Contacts

| Organization | Contact | Phone | Email | Purpose |
|--------------|---------|-------|-------|---------|
| Supervisory Authority | [TODO] | [TODO] | [TODO] | Notification |
| Forensics Provider | [TODO] | [TODO] | [TODO] | Analysis |
| External Lawyer | [TODO] | [TODO] | [TODO] | Advice |
| PR Agency | [TODO] | [TODO] | [TODO] | Crisis communication |
| Cyber Insurance | [TODO] | [TODO] | [TODO] | Claim reporting |

### Tools and Systems

| Tool | Purpose | Access |
|------|---------|--------|
| [TODO: SIEM] | Monitoring, log analysis | [TODO: URL] |
| [TODO: Ticketing System] | Incident tracking | [TODO: URL] |
| [TODO: Breach Register] | Documentation | [TODO: URL/File] |
| [TODO: Communication Platform] | Team coordination | [TODO: URL] |

## Appendices

- **Template 0610:** Breach Notification Template (Supervisory Authority)
- **Template 0620:** Breach Communication Template (Data Subjects)
- **Template 0630:** Breach Register Template
- **Template 0640:** Post-Breach Review Template

**Next Steps:**
1. Adapt this plan to your organization
2. Define all roles and contacts
3. Conduct breach response exercises (at least annually)
4. Keep the plan current
5. Ensure all team members know the plan

