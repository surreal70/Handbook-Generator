# Problem Management and Postmortems

**Document-ID:** [FRAMEWORK]-0130
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

## Purpose and Scope

This document describes the problem management process for {{ meta-organisation.name }} according to ITIL v4 best practices. It defines the systematic analysis of recurring incidents, root cause analysis methods, postmortem processes, and the management of the Known Error Database.

**Scope:** All IT services and systems of {{ meta-organisation.name }}

**Responsible:** {{ meta-organisation-roles.role_it_operations_manager.name }} ({{ meta-organisation-roles.role_it_operations_manager.email }})

## Problem Definition

A **problem** is the unknown cause of one or more incidents. The goal of problem management is to identify and eliminate the root cause to prevent future incidents.

### Distinction: Incident vs. Problem

| Aspect | Incident | Problem |
|---|---|---|
| **Focus** | Symptoms | Causes |
| **Goal** | Quick restoration | Permanent solution |
| **Timeframe** | Immediate | Planned |
| **Approach** | Workaround | Root-Cause-Elimination |
| **Process** | Reactive | Proactive |

## Problem Management Process

### Process Overview (ITIL v4)

```
┌─────────────────┐
│ Problem         │
│ Detection       │
└────────┬────────┘
         │
┌────────▼────────┐
│ Problem         │
│ Logging         │
└────────┬────────┘
         │
┌────────▼────────┐
│ Problem         │
│ Categorization  │
└────────┬────────┘
         │
┌────────▼────────┐
│ Problem         │
│ Prioritization  │
└────────┬────────┘
         │
┌────────▼────────┐
│ Investigation   │
│ & Diagnosis     │
│ (RCA)           │
└────────┬────────┘
         │
┌────────▼────────┐
│ Workaround      │
│ Identification  │
└────────┬────────┘
         │
┌────────▼────────┐
│ Known Error     │
│ Recording       │
└────────┬────────┘
         │
┌────────▼────────┐
│ Problem         │
│ Resolution      │
└────────┬────────┘
         │
┌────────▼────────┐
│ Problem         │
│ Closure         │
└─────────────────┘
```

### 1. Problem Detection

**Detection Sources:**
- Recurring incidents (> 3x in 30 days)
- Trend analysis of incident data
- Proactive monitoring analyses
- Major incident reviews
- Vendor bulletins and security advisories

**Triggers for Problem Creation:**
- Multiple similar incidents
- Incidents with high business impact
- Incidents without known solution
- Structural weaknesses

**Responsible:** Problem Manager, IT Operations Team

### 2. Problem Logging

**Required Information:**
- Problem ID (automatically generated)
- Linked incident IDs
- Symptom description
- Affected services/systems
- Affected configuration items (CIs)
- Initial hypotheses about cause

**Tool:** {{ meta-handbook.ticketing_system }}

**Responsible:** Problem Manager

### 3. Problem Categorization

**Categories:**
- Hardware problems
- Software problems
- Network problems
- Process problems
- Documentation problems
- Capacity problems
- Security problems

**Responsible:** Problem Manager

### 4. Problem Prioritization

**Priority Factors:**
- Number of affected incidents
- Business impact
- Frequency of occurrence
- Availability of workarounds
- Resource availability

**Priority Levels:**

| Priority | Description | Processing Time |
|---|---|---|
| **P1 - Critical** | Frequent P1 incidents, no workaround | Immediate |
| **P2 - High** | Frequent P2 incidents, temporary workaround | 1 week |
| **P3 - Medium** | Moderate frequency, workaround available | 1 month |
| **P4 - Low** | Rare incidents, low impact | Planned |

### 5. Investigation & Diagnosis (Root Cause Analysis)

**RCA Methods:**
- 5-Why analysis
- Fishbone diagram (Ishikawa)
- Fault tree analysis
- Timeline analysis
- Log correlation

**Activities:**
- Collect data (logs, monitoring, configurations)
- Develop hypotheses
- Conduct tests
- Identify root cause
- Create documentation

**Responsible:** Problem Manager, Technical Specialists

### 6. Workaround Identification

**Workaround Criteria:**
- Reduces impact or frequency
- Practical for incident teams
- Documented and tested
- Temporary solution until permanent fix

**Documentation:**
- Workaround description
- Application steps
- Limitations
- Validity period

### 7. Known Error Recording

**Known Error Database (KEDB):**
- Problem description
- Root cause
- Workaround
- Permanent solution (if available)
- Linked incidents
- Linked CIs

**Access:** All IT staff (Read), Problem Manager (Write)

### 8. Problem Resolution

**Solution Approaches:**
- Software patch or update
- Configuration change
- Hardware replacement
- Process improvement
- Documentation update
- Training

**Change Management:**
- Permanent solutions require change request
- Change planning and approval
- Implementation via change process

### 9. Problem Closure

**Closure Criteria:**
- Root cause identified and documented
- Permanent solution implemented
- No new incidents occurred (monitoring period)
- Documentation complete
- Lessons learned documented

**Responsible:** Problem Manager

## Root Cause Analysis (RCA) Methods

### 5-Why Analysis

**Method:** Ask "Why?" five times to get to the root cause

**Example:**
1. **Why** did the database fail? → Disk full
2. **Why** was the disk full? → Log files not rotated
3. **Why** were logs not rotated? → Logrotate job failed
4. **Why** did the job fail? → Incorrect cron configuration
5. **Why** was the configuration incorrect? → No validation after change

**Root Cause:** Missing change validation

### Fishbone Diagram (Ishikawa)

**Categories:**
- **People:** Errors, knowledge, training
- **Methods:** Processes, procedures, standards
- **Machines:** Hardware, software, tools
- **Materials:** Data, configurations, documentation
- **Environment:** Infrastructure, network, location
- **Management:** Decisions, resources, priorities

**Application:**
1. Define problem as "fish head"
2. Draw main categories as "bones"
3. Identify causes per category
4. Add deeper causes as sub-bones
5. Identify root cause

### Timeline Analysis

**Method:** Chronological reconstruction of events

**Steps:**
1. Create timeline
2. Enter all relevant events
3. Identify causalities
4. Work out critical path
5. Find root cause at beginning of causal chain

**Data Sources:**
- Incident tickets
- Change records
- Monitoring logs
- System logs
- Deployment history

## Postmortem Process

### Postmortem Definition

A **postmortem** is a structured analysis of a major incident or critical problem with the goal of identifying lessons learned and implementing improvements.

### Postmortem Triggers

**Mandatory Postmortems for:**
- Major incidents (P1)
- Service outages > 4 hours
- Data loss or security breach
- Incidents with media attention
- Repeated incidents despite previous solution

**Optional Postmortems for:**
- P2 incidents with interesting lessons learned
- Successful incident management (best practices)
- Near-miss situations

### Postmortem Timeline

| Phase | Timing | Activity |
|---|---|---|
| **Initiation** | Within 24h | Announce postmortem, invite participants |
| **Data Collection** | 24-48h | Collect logs, timelines, facts |
| **Meeting** | Within 1 week | Conduct postmortem meeting |
| **Documentation** | Within 2 weeks | Finalize postmortem report |
| **Follow-up** | Ongoing | Implement and track action items |

### Postmortem Meeting

**Participants:**
- Incident Manager
- Affected teams
- Service Owner
- Management (for major incidents)
- Optional: External stakeholders

**Agenda:**
1. **Incident Overview** (5 min)
   - What happened?
   - When did it happen?
   - Who was affected?

2. **Timeline Review** (15 min)
   - Chronological events
   - Decision points
   - Communication

3. **Root Cause Analysis** (20 min)
   - 5-Why or Fishbone
   - Contributing factors
   - Root cause

4. **What Went Well** (10 min)
   - Successful measures
   - Good collaboration
   - Effective tools

5. **What Went Wrong** (10 min)
   - Problems and delays
   - Communication issues
   - Tool or process deficiencies

6. **Action Items** (15 min)
   - Improvement measures
   - Responsible parties
   - Deadlines

**Duration:** 60-90 minutes

**Moderator:** Problem Manager or neutral facilitator

### Postmortem Principles

**Blameless Culture:**
- Focus on systems and processes, not people
- No blame assignment
- Psychological safety
- Learning from mistakes

**Fact-Based:**
- Objective data (logs, metrics)
- No speculation
- Verifiable statements

**Constructive:**
- Solution-oriented
- Concrete action items
- Actionable improvements

## Postmortem Template

### 1. Executive Summary

**Incident Overview:**
- **Incident ID:** [ID]
- **Date/Time:** [Start] - [End]
- **Duration:** [Hours]
- **Priority:** P1 / P2
- **Affected Service:** [Service Name]
- **Impact:** [Number of users, business impact]

**Summary:**
[2-3 sentences: What happened and what was the cause?]

### 2. Timeline

| Time | Event | Action | Responsible |
|---|---|---|---|
| 10:00 | Alert: Database CPU 100% | Monitoring alert triggered | Monitoring System |
| 10:05 | Service Desk receives calls | Incident ticket created | Service Desk |
| 10:15 | Escalation to DBA team | Database analysis started | IT Operations |
| 10:30 | Root cause identified | Slow query found | DBA Team |
| 10:45 | Query optimized | Deployment performed | DBA Team |
| 11:00 | Service restored | Monitoring confirmed | IT Operations |

### 3. Root Cause Analysis

**5-Why Analysis:**
1. Why was the database overloaded? → Slow query
2. Why was there a slow query? → Missing index
3. Why was the index missing? → Not included in deployment
4. Why wasn't it in the deployment? → Not caught in code review
5. Why wasn't it caught? → No performance tests

**Root Cause:** Missing performance tests in CI/CD pipeline

**Contributing Factors:**
- Insufficient code review checklist
- No automated query analysis
- Missing staging environment with production data volume

### 4. Impact Assessment

**Technical Impact:**
- Database CPU: 100% for 60 minutes
- Response times: > 30 seconds (normal: < 1s)
- Service availability: 0% for 60 minutes

**Business Impact:**
- Affected users: 500 (100%)
- Blocked business processes: Order Processing
- Estimated revenue loss: [Amount]
- Reputation damage: Medium

**SLA Impact:**
- SLA target: 99.9% availability
- Actual availability: 99.86%
- SLA breach: Yes

### 5. What Went Well

- ✅ Quick escalation to DBA team (10 minutes)
- ✅ Effective communication between teams
- ✅ Root cause quickly identified (25 minutes)
- ✅ Solution successfully implemented
- ✅ No data loss

### 6. What Went Wrong

- ❌ Slow query not detected before deployment
- ❌ No automatic performance tests
- ❌ Staging environment not representative
- ❌ Monitoring alert too late (CPU threshold too high)
- ❌ Rollback procedure not documented

### 7. Action Items

| ID | Measure | Responsible | Deadline | Status |
|---|---|---|---|---|
| AI-001 | Integrate performance tests in CI/CD | DevOps Team | 2 weeks | Open |
| AI-002 | Extend code review checklist | Dev Team | 1 week | Open |
| AI-003 | Staging database with prod volume | DBA Team | 1 month | Open |
| AI-004 | Adjust monitoring thresholds | Ops Team | 1 week | Open |
| AI-005 | Create rollback runbook | DBA Team | 2 weeks | Open |

### 8. Lessons Learned

**Technical:**
- Performance tests are essential before deployments
- Staging environment must simulate production data volume
- Automated query analysis can detect problems early

**Process:**
- Code review checklists must cover performance aspects
- Rollback procedures must be documented and tested
- Monitoring thresholds must be reviewed regularly

**Organizational:**
- Team communication worked well
- Escalation processes were effective
- Documentation needs improvement

### 9. Follow-up

**Review Date:** [Date, 4 weeks after incident]

**Review Agenda:**
- Status of all action items
- Effectiveness of measures
- Further improvements

**Responsible:** Problem Manager

## Known Error Database (KEDB)

### KEDB Structure

**Required Fields:**
- **Known Error ID:** Unique identifier
- **Title:** Brief description
- **Symptoms:** How does the problem manifest?
- **Root Cause:** Identified root cause
- **Workaround:** Temporary solution
- **Permanent Solution:** Permanent fix (if available)
- **Affected CIs:** Configuration items
- **Linked Incidents:** Incident IDs
- **Linked Problems:** Problem IDs
- **Status:** Open, Workaround Available, Resolved, Closed
- **Priority:** P1-P4
- **Created:** Date, author
- **Updated:** Date, author

### KEDB Example

**Known Error ID:** KE-2024-001

**Title:** PostgreSQL Connection Pool Exhaustion

**Symptoms:**
- Application reports "Connection timeout"
- Database logs show "too many connections"
- Monitoring shows 100% connection pool utilization

**Root Cause:**
- Connection pool limit configured too low (max_connections=100)
- Application not releasing connections correctly (connection leak)
- Missing connection timeout configuration

**Workaround:**
1. Restart PostgreSQL service: `systemctl restart postgresql`
2. Restart application: `systemctl restart app-service`
3. Monitoring: Observe connection pool utilization

**Permanent Solution:**
1. Increase max_connections in postgresql.conf: `max_connections = 200`
2. Fix connection leak in application (code fix)
3. Configure connection timeout: `idle_in_transaction_session_timeout = 60000`
4. Improve connection pool monitoring

**Affected CIs:**
- {{ netbox.database.server }}
- {{ netbox.application.server }}

**Linked Incidents:** INC-2024-123, INC-2024-145, INC-2024-167

**Status:** Resolved

**Priority:** P2

### KEDB Usage

**Incident Handling:**
1. Match incident symptoms with KEDB
2. If match: Apply workaround
3. Link incident with known error
4. Reference problem ticket

**Problem Analysis:**
1. Enter new known errors in KEDB
2. Document workarounds
3. Track permanent solutions
4. Update status

**Knowledge Management:**
- Use KEDB as knowledge base
- Regular reviews (monthly)
- Archive outdated entries
- Document best practices

## Proactive Problem Management

### Trend Analysis

**Data Sources:**
- Incident statistics
- Monitoring metrics
- Performance data
- Capacity utilization

**Analysis Methods:**
- Time series analysis
- Correlation analysis
- Anomaly detection
- Predictive analytics

**Goal:** Identify problems before they become incidents

### Proactive Measures

**Regular Reviews:**
- Weekly incident trend reviews
- Monthly problem reviews
- Quarterly service reviews

**Preventive Measures:**
- Capacity upgrades
- Software updates and patches
- Configuration optimizations
- Process improvements
- Training and documentation

### Continuous Improvement

**Improvement Cycle:**
1. **Measure:** Capture metrics
2. **Analyze:** Identify trends
3. **Improve:** Implement measures
4. **Control:** Check effectiveness

**Improvement Areas:**
- Processes
- Tools
- Documentation
- Skills and training
- Infrastructure

## Metrics and Reporting

### Key Performance Indicators (KPIs)

| Metric | Target Value | Measurement |
|---|---|---|
| **Problem Resolution Rate** | > 80% | Resolved problems / Total problems |
| **Mean Time to Resolve Problem** | < 30 days | Average resolution time |
| **Known Error Utilization** | > 60% | Incidents with KEDB workaround |
| **Recurring Incident Rate** | < 10% | Incidents with known cause |
| **Postmortem Completion Rate** | 100% | Postmortems for major incidents |

### Reporting

**Monthly Problem Report:**
- Number of open problems (by priority)
- Newly created problems
- Resolved problems
- Top 5 problem categories
- KEDB statistics
- Action items status

**Quarterly Trend Analysis:**
- Problem trends over time
- Recurring problem patterns
- Effectiveness of improvement measures
- ROI of problem management

## Roles and Responsibilities

### Problem Manager

**Responsibilities:**
- Problem process ownership
- Problem prioritization
- RCA coordination
- KEDB management
- Postmortem moderation
- Reporting

**Person:** {{ meta-organisation-roles.role_it_operations_manager.name }}

### Technical Specialists

**Responsibilities:**
- Technical analysis
- RCA execution
- Solution development
- Workaround identification

**Teams:** Server Team, Network Team, DBA Team, Application Team

### Service Owner

**Responsibilities:**
- Business impact assessment
- Prioritization decisions
- Resource provisioning
- Stakeholder communication

## Tools and Systems

### Problem Management Tool
- **System:** {{ meta-handbook.ticketing_system }}
- **URL:** {{ meta-handbook.ticketing_system_url }}
- **Access:** IT Operations Team

### Known Error Database
- **System:** {{ meta-handbook.ticketing_system }} (KEDB module)
- **URL:** {{ meta-handbook.kedb_url }}
- **Access:** All IT staff (Read)

### RCA Tools
- **Collaboration:** {{ meta-handbook.collaboration_tool }}
- **Diagramming:** {{ meta-handbook.diagramming_tool }}
- **Log Analysis:** {{ meta-handbook.log_analysis_tool }}

## References

- ITIL v4 Foundation - Problem Management
- ISO/IEC 20000-1:2018 - Problem Management
- Site Reliability Engineering (SRE) - Postmortem Culture
- Internal Incident Management Processes
- Change Management Processes

**Document Owner:** {{ meta-handbook.owner }}  
**Approved by:** {{ meta-handbook.approver }}  
**Version:** {{ meta-handbook.revision }}  
**Classification:** {{ meta-handbook.classification }}  
**Last Updated:** {{ meta-handbook.date }}

