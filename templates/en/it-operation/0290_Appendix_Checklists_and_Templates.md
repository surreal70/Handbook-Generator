# Appendix: Checklists and Templates

**Document-ID:** [FRAMEWORK]-0290
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

## Overview

This document contains a collection of checklists, templates for standard documents, and forms for IT operations. The goal is to ensure consistent and efficient execution of standard processes.

**Document Owner:** {{ meta-handbook.owner }}  
**Approved by:** {{ meta-handbook.approver }}  
**Version:** {{ meta-handbook.revision }}  
**Organization:** {{ meta-organisation.name }}

## Checklists

### Incident Management Checklists

#### Incident Response Checklist

```markdown
# Incident Response Checklist

**Incident ID:** [INC-XXXXX]
**Date/Time:** [YYYY-MM-DD HH:MM]
**Reporter:** [Name]
**Priority:** P1 / P2 / P3 / P4

## Phase 1: Detection and Recording
- [ ] Incident detected and documented
- [ ] Priority assessed (P1-P4)
- [ ] Ticket created
- [ ] Affected systems identified
- [ ] Affected users identified
- [ ] Initial symptoms documented

## Phase 2: Classification and Prioritization
- [ ] Incident category assigned
- [ ] Business impact assessed
- [ ] Urgency assessed
- [ ] Priority confirmed
- [ ] Assigned to responsible person

## Phase 3: Diagnosis and Investigation
- [ ] Logs analyzed
- [ ] Monitoring data checked
- [ ] Similar incidents searched
- [ ] Known issues checked
- [ ] Root cause identified (if possible)

## Phase 4: Resolution and Recovery
- [ ] Solution approach defined
- [ ] Approval obtained (if required)
- [ ] Solution implemented
- [ ] Functionality validated
- [ ] Users informed

## Phase 5: Closure
- [ ] Incident resolved
- [ ] Documentation completed
- [ ] User confirmation obtained
- [ ] Ticket closed
- [ ] Lessons learned documented (for P1/P2)

## Communication
- [ ] Stakeholders informed
- [ ] Status updates communicated
- [ ] Solution communicated

**Processed by:** [Name]
**Completed on:** [YYYY-MM-DD HH:MM]
**Duration:** [HH:MM]
```

### Change Management Checklists

#### Standard Change Checklist

```markdown
# Standard Change Checklist

**Change ID:** [CHG-XXXXX]
**Date:** [YYYY-MM-DD]
**Change Manager:** [Name]

## Planning
- [ ] Change request created
- [ ] Description complete
- [ ] Justification documented
- [ ] Risk assessment performed
- [ ] Affected systems identified
- [ ] Dependencies identified
- [ ] Time window defined
- [ ] Resources allocated

## Approval
- [ ] Change category determined (Standard/Normal/Emergency)
- [ ] Approver identified
- [ ] Approval obtained
- [ ] CAB review (if required)

## Preparation
- [ ] Implementation plan created
- [ ] Rollback plan created
- [ ] Test plan created
- [ ] Communication plan created
- [ ] Backup performed
- [ ] Test environment validated

## Implementation
- [ ] Maintenance window started
- [ ] Users informed
- [ ] Change implemented
- [ ] Step-by-step documented
- [ ] Problems documented

## Validation
- [ ] Functionality tested
- [ ] Performance validated
- [ ] Monitoring checked
- [ ] No errors in logs
- [ ] User acceptance test (if required)

## Closure
- [ ] Change successful
- [ ] Documentation updated
- [ ] CMDB updated
- [ ] Users informed
- [ ] Change closed
- [ ] Lessons learned (if problems)

## Rollback (if required)
- [ ] Rollback decision made
- [ ] Rollback plan executed
- [ ] System restored
- [ ] Validation performed
- [ ] Incident created for analysis

**Change Manager:** [Name]
**Implemented by:** [Name]
**Status:** Successful / Rollback / Cancelled
```

### Backup and Recovery Checklists

#### Backup Verification Checklist

```markdown
# Backup Verification Checklist

**Date:** [YYYY-MM-DD]
**Performed by:** [Name]

## Backup Status
- [ ] All scheduled backups performed
- [ ] Backup logs checked
- [ ] No errors in logs
- [ ] Backup sizes plausible
- [ ] Backup times acceptable

## Backup Integrity
- [ ] Checksums validated
- [ ] Backup files readable
- [ ] No corruption detected
- [ ] Encryption working

## Restore Test
- [ ] Random backup selected
- [ ] Test environment prepared
- [ ] Restore performed
- [ ] Data validated
- [ ] Functionality tested
- [ ] Restore time measured

## Documentation
- [ ] Test result documented
- [ ] Problems documented
- [ ] Improvements identified
- [ ] Report created

## Systems Checked
- [ ] Databases
- [ ] File servers
- [ ] Application servers
- [ ] Configurations
- [ ] Virtualization hosts

**Result:** Successful / With Problems / Failed
**Next Test:** [YYYY-MM-DD]
```

## Templates

### Incident Report Template

```markdown
# Incident Report

**Incident ID:** [INC-XXXXX]
**Date:** [YYYY-MM-DD]
**Created by:** [Name]

## Executive Summary
[Brief summary of the incident for management]

## Incident Details
- **Priority:** P1 / P2 / P3 / P4
- **Category:** [Category]
- **Affected Systems:** [List]
- **Affected Users:** [Number/Description]
- **Start:** [YYYY-MM-DD HH:MM]
- **End:** [YYYY-MM-DD HH:MM]
- **Duration:** [HH:MM]

## Timeline
| Time | Event | Action |
|---|---|---|
| HH:MM | [Event] | [Action] |
| HH:MM | [Event] | [Action] |

## Root Cause
[Detailed description of the cause]

## Impact
- **Business Impact:** [Description]
- **Financial Impact:** [Estimate]
- **Reputation Damage:** [Assessment]
- **Affected Services:** [List]

## Solution
[Description of implemented solution]

## Improvement Measures
1. [Measure 1] - Responsible: [Name] - Deadline: [Date]
2. [Measure 2] - Responsible: [Name] - Deadline: [Date]
3. [Measure 3] - Responsible: [Name] - Deadline: [Date]

## Lessons Learned
- [Lesson 1]
- [Lesson 2]
- [Lesson 3]

## Attachments
- [Logs]
- [Screenshots]
- [Monitoring Data]

**Created by:** [Name]
**Approved by:** {{ meta-organisation-roles.role_IT_Operations_Manager }}
**Date:** [YYYY-MM-DD]
```

### Change Request Template

```markdown
# Change Request

**Change ID:** [CHG-XXXXX]
**Date:** [YYYY-MM-DD]
**Requester:** [Name]

## Change Details
- **Title:** [Short title]
- **Category:** Standard / Normal / Emergency
- **Priority:** Low / Medium / High / Critical
- **Planned Date:** [YYYY-MM-DD]
- **Planned Time:** [HH:MM - HH:MM]
- **Duration:** [Estimated duration]

## Description
[Detailed description of the change]

## Justification
[Why is this change necessary?]

## Affected Systems
- [System 1]
- [System 2]
- [System 3]

## Affected Users
[Number and description of affected users]

## Risk Assessment
- **Risk:** Low / Medium / High
- **Impact:** Low / Medium / High
- **Probability:** Low / Medium / High

## Risks and Mitigations
| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| [Risk 1] | [L/M/H] | [L/M/H] | [Measure] |
| [Risk 2] | [L/M/H] | [L/M/H] | [Measure] |

## Implementation Plan
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Rollback Plan
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Test Plan
1. [Test 1]
2. [Test 2]
3. [Test 3]

## Communication Plan
- **Before Change:** [Who, When, How]
- **During Change:** [Who, When, How]
- **After Change:** [Who, When, How]

## Approvals
- [ ] Technical Approval: [Name] - [Date]
- [ ] Business Approval: [Name] - [Date]
- [ ] CAB Approval: [Name] - [Date]

**Requester:** [Name]
**Change Manager:** {{ meta-organisation-roles.role_IT_Operations_Manager }}
**Status:** Requested / Approved / Rejected / Implemented
```

## Forms

### Access Request Form

```markdown
# Access Request

**Requester:** [Name]
**Date:** [YYYY-MM-DD]
**Department:** [Department]

## User Information
- **Name:** [Full Name]
- **Email:** [Email Address]
- **Phone:** [Phone Number]
- **Department:** [Department]
- **Position:** [Position]
- **Manager:** [Manager Name]

## Access Details
- **System/Application:** [Name]
- **Access Level:** Read / Write / Admin
- **Justification:** [Business justification]
- **Duration:** Permanent / Temporary until [Date]

## Required Permissions
- [ ] [Permission 1]
- [ ] [Permission 2]
- [ ] [Permission 3]

## Approvals
- [ ] Manager Approval: [Name] - [Date]
- [ ] Data Owner Approval: [Name] - [Date]
- [ ] Security Approval: [Name] - [Date]

## IT Processing
- **Processed by:** [Name]
- **Date:** [YYYY-MM-DD]
- **Access Granted:** Yes / No
- **Comments:** [Comments]

**Status:** Requested / Approved / Rejected / Implemented
```

## Processes and Responsibilities

### RACI Matrix

| Activity | Ops Manager | Ops Team | Service Desk | User |
|---|---|---|---|---|
| Checklist Creation | A | R | C | - |
| Template Creation | A | R | C | - |
| Checklist Usage | C | R | R | - |
| Template Usage | C | R | R | R |
| Update | A | R | C | - |

> **Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

**Last Update:** {{ meta-handbook.date }}  
**Next Review:** [TODO: Date]  
**Contact:** {{ meta-organisation-roles.role_IT_Operations_Manager_email }}


### Change Request Template

```markdown
# Change Request

**Change ID:** [CHG-XXXXX]
**Date:** [YYYY-MM-DD]
**Requester:** [Name]

## Change Details
- **Title:** [Short title]
- **Category:** Standard / Normal / Emergency
- **Priority:** Low / Medium / High / Critical
- **Planned Date:** [YYYY-MM-DD]
- **Planned Time:** [HH:MM - HH:MM]
- **Duration:** [Estimated duration]

## Description
[Detailed description of the change]

## Justification
[Why is this change necessary?]

## Affected Systems
- [System 1]
- [System 2]
- [System 3]

## Affected Users
[Number and description of affected users]

## Risk Assessment
- **Risk:** Low / Medium / High
- **Impact:** Low / Medium / High
- **Probability:** Low / Medium / High

## Risks and Mitigations
| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| [Risk 1] | [L/M/H] | [L/M/H] | [Measure] |
| [Risk 2] | [L/M/H] | [L/M/H] | [Measure] |

## Implementation Plan
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Rollback Plan
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Test Plan
1. [Test 1]
2. [Test 2]
3. [Test 3]

## Communication Plan
- **Before Change:** [Who, When, How]
- **During Change:** [Who, When, How]
- **After Change:** [Who, When, How]

## Approvals
- [ ] Technical Approval: [Name] - [Date]
- [ ] Business Approval: [Name] - [Date]
- [ ] CAB Approval: [Name] - [Date]

**Requester:** [Name]
**Change Manager:** {{ meta-organisation-roles.role_IT_Operations_Manager }}
**Status:** Requested / Approved / Rejected / Implemented
```

### Post-Incident Review Template

```markdown
# Post-Incident Review

**Incident ID:** [INC-XXXXX]
**Date:** [YYYY-MM-DD]
**Facilitator:** [Name]
**Participants:** [Names]

## Incident Summary
[Brief summary of the incident]

## Timeline
| Time | Event | Who | Action |
|---|---|---|---|
| HH:MM | [Event] | [Name] | [Action] |
| HH:MM | [Event] | [Name] | [Action] |

## What Went Well?
- [Point 1]
- [Point 2]
- [Point 3]

## What Didn't Go Well?
- [Point 1]
- [Point 2]
- [Point 3]

## Root Cause
[5-Why analysis or other root cause method]

1. **Why did the problem occur?** [Answer]
2. **Why?** [Answer]
3. **Why?** [Answer]
4. **Why?** [Answer]
5. **Why?** [Answer]

**Root Cause:** [Final cause]

## Action Items
| # | Action | Responsible | Due Date | Status |
|---|---|---|---|---|
| 1 | [Action] | [Name] | [Date] | Open |
| 2 | [Action] | [Name] | [Date] | Open |
| 3 | [Action] | [Name] | [Date] | Open |

## Lessons Learned
- [Lesson 1]
- [Lesson 2]
- [Lesson 3]

## Improvements
### Short-term (< 1 month)
- [Improvement 1]
- [Improvement 2]

### Medium-term (1-3 months)
- [Improvement 1]
- [Improvement 2]

### Long-term (> 3 months)
- [Improvement 1]
- [Improvement 2]

**Facilitator:** [Name]
**Date:** [YYYY-MM-DD]
**Follow-Up:** [Date for action items review]
```

## Forms

### Access Request Form

```markdown
# Access Request

**Requester:** [Name]
**Date:** [YYYY-MM-DD]
**Department:** [Department]

## User Information
- **Name:** [Full name]
- **Email:** [Email address]
- **Phone:** [Phone number]
- **Department:** [Department]
- **Position:** [Position]
- **Manager:** [Manager name]

## Access Details
- **System/Application:** [Name]
- **Access Level:** Read / Write / Admin
- **Justification:** [Business justification]
- **Duration:** Permanent / Temporary until [Date]

## Required Permissions
- [ ] [Permission 1]
- [ ] [Permission 2]
- [ ] [Permission 3]

## Approvals
- [ ] Manager Approval: [Name] - [Date]
- [ ] Data Owner Approval: [Name] - [Date]
- [ ] Security Approval: [Name] - [Date]

## IT Processing
- **Processed by:** [Name]
- **Date:** [YYYY-MM-DD]
- **Access Granted:** Yes / No
- **Comments:** [Comments]

**Status:** Requested / Approved / Rejected / Implemented
```

### Hardware Request Form

```markdown
# Hardware Request

**Requester:** [Name]
**Date:** [YYYY-MM-DD]
**Department:** [Department]

## User Information
- **Name:** [Full name]
- **Email:** [Email address]
- **Department:** [Department]
- **Location:** [Location]
- **Manager:** [Manager name]

## Hardware Details
- **Type:** Laptop / Desktop / Monitor / Peripherals / Other
- **Specification:** [Desired specification]
- **Justification:** [Business justification]
- **Urgency:** Normal / High / Critical

## Old Hardware (if replacement)
- **Type:** [Type]
- **Model:** [Model]
- **Serial Number:** [Serial number]
- **Condition:** [Condition]
- **Return:** Yes / No

## Costs
- **Estimated Cost:** [Amount]
- **Budget Code:** [Budget code]
- **Cost Center:** [Cost center]

## Approvals
- [ ] Manager Approval: [Name] - [Date]
- [ ] Budget Approval: [Name] - [Date]
- [ ] IT Approval: [Name] - [Date]

## IT Processing
- **Processed by:** [Name]
- **Order Date:** [YYYY-MM-DD]
- **Delivery Date:** [YYYY-MM-DD]
- **Installation Date:** [YYYY-MM-DD]
- **Asset Tag:** [Asset tag]

**Status:** Requested / Approved / Ordered / Delivered / Installed
```

## Processes and Responsibilities

### RACI Matrix

| Activity | Ops Manager | Ops Team | Service Desk | Users |
|---|---|---|---|---|
| Checklist Creation | A | R | C | - |
| Template Creation | A | R | C | - |
| Checklist Usage | C | R | R | - |
| Template Usage | C | R | R | R |
| Updates | A | R | C | - |

> **Legend:** R = Responsible, A = Accountable, C = Consulted, I = Informed

## Compliance and Standards

### Relevant Standards
- **ITIL v4:** Service Operation Practice
- **ISO 20000:** Clause 8.1 - Operational Planning and Control
- **COBIT 2019:** DSS01 - Managed Operations

## Appendix

### Glossary

| Term | Definition |
|---|---|
| Checklist | Structured list of tasks or checkpoints |
| Template | Standardized document format |
| Form | Structured input document |
| Post-Incident Review | Retrospective analysis of an incident |

### References
- ITIL v4 Foundation Handbook
- ISO/IEC 20000-1:2018
- COBIT 2019 Framework

**Last Update:** {{ meta-handbook.date }}  
**Next Review:** [TODO: Date]  
**Contact:** {{ meta-organisation-roles.role_IT_Operations_Manager_email }}
