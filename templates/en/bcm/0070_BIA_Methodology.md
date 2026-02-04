# Business Impact Analysis (BIA) – Methodology

**Document ID:** BCM-0070  
**Organization:** {{ meta.organization.name }}  
**Owner:** {{ meta.document.owner }}  
**Approved by:** {{ meta.document.approver }}  
**Version:** {{ meta.document.version }}  
**Status:** Draft / In Review / Approved  
**Classification:** {{ meta.document.classification }}  
**Last Updated:** {{ meta.document.last_updated }}  

---

<!-- 
TEMPLATE AUTHOR NOTE:
This template defines the Business Impact Analysis (BIA) methodology.
It aligns with ISO 22301:2019 Clause 8.2.2 (Business impact analysis and risk assessment).

Customization required:
- Define BIA process and timeline
- Establish assessment criteria and scales
- Define RTO/RPO determination methodology
- Plan workshops and interviews
-->

## 1. Purpose and Output

### 1.1 BIA Objectives

The Business Impact Analysis (BIA) of {{ meta.organization.name }} pursues the following objectives:

- **Identification of critical business processes:** Determination of business-critical processes and services
- **Quantification of impacts:** Assessment of financial, operational, and reputational impacts of outages
- **Definition of target values:** Definition of RTO (Recovery Time Objective) and RPO (Recovery Point Objective)
- **Prioritization:** Establishment of recovery prioritization
- **Resource planning:** Determination of resource requirements for business continuity

### 1.2 Expected Results

The BIA delivers the following results:

**RTO (Recovery Time Objective):**
- Maximum tolerable downtime for each critical process
- Point in time by which a process must be restored

**RPO (Recovery Point Objective):**
- Maximum tolerable data loss
- Point in time to which data must be restored

**MTPD (Maximum Tolerable Period of Disruption):**
- Maximum time period a process can be down before irreparable damage occurs
- Also: MAO (Maximum Acceptable Outage)

**Prioritization:**
- Sequence of recovery of processes and systems
- Dependencies between processes

**Resource Requirements:**
- Personnel, premises, IT systems, data, suppliers
- Minimum resources for emergency operations

## 2. Approach and Methodology

### 2.1 BIA Process

```
┌─────────────────┐
│ 1. Preparation  │
│ - Scope         │
│ - Stakeholders  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 2. Data         │
│    Collection   │
│ - Workshops     │
│ - Interviews    │
│ - Questionnaires│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 3. Analysis     │
│ - Assessment    │
│ - Dependencies  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 4. RTO/RPO      │
│ - Definition    │
│ - Validation    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 5. Documentation│
│ - Report        │
│ - Presentation  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 6. Approval     │
│ - Review        │
│ - Authorization │
└─────────────────┘
```

### 2.2 Workshops and Interviews

**Target Audience:**
- Department heads and process owners
- IT managers
- Key persons with specialized knowledge

**Format:**
- **Workshops:** Group format for cross-functional topics (2-4 hours)
- **Interviews:** One-on-one conversations for detailed process analysis (1-2 hours)
- **Questionnaires:** Standardized collection for less critical processes

**Execution:**
[TODO: Define workshop/interview plan]

**Example Schedule:**
| Week | Activity | Participants | Responsible |
|------|----------|--------------|-------------|
| 1 | Kick-off workshop | All department heads | BCM Manager |
| 2-3 | Individual department interviews | Process owners | BCM Manager |
| 4 | IT workshop | IT team | BCM Manager + {{ meta.roles.cio.name }} |
| 5 | Consolidation and analysis | BCM team | BCM Manager |
| 6 | Results presentation | Management | BCM Manager |

### 2.3 Data Sources

**Primary Data Sources:**
- Workshops and interviews with departments
- Existing process documentation
- IT service catalog and CMDB
- Financial reports and revenue data

**Secondary Data Sources:**
- Contract documents and SLAs
- Compliance requirements
- Historical incident data
- Benchmarks and best practices

### 2.4 Review and Validation Steps

**Validation by Departments:**
1. Draft BIA results sent to process owners
2. Departments review and comment within [TODO: X] days
3. Feedback is incorporated

**Management Review:**
1. Consolidated BIA results presented to management
2. RTO/RPO values discussed and validated
3. Prioritization established

**Formal Approval:**
- Approval by {{ meta.roles.ceo.name }} (CEO)
- Confirmation by department heads
- Documentation of approval

## 3. Assessment Dimensions

### 3.1 Financial Impact

**Direct Financial Losses:**
- Revenue loss per hour/day
- Contractual penalties and damage claims
- Additional costs for emergency measures

**Assessment Scale:**
[TODO: Define your assessment scale]

**Example:**
| Level | Description | Revenue Loss per Day |
|-------|-------------|---------------------|
| 5 - Critical | Existential threat | > 500,000 € |
| 4 - Very High | Massive impact | 100,000 - 500,000 € |
| 3 - High | Significant impact | 50,000 - 100,000 € |
| 2 - Medium | Noticeable impact | 10,000 - 50,000 € |
| 1 - Low | Minor impact | < 10,000 € |

### 3.2 Operational Impact

**Impairment of Business Operations:**
- Throughput and production capacity
- Backlog and rework effort
- Quality problems
- Impairment of other processes

**Assessment Scale:**
| Level | Description | Operational Impact |
|-------|-------------|-------------------|
| 5 - Critical | Complete standstill | All processes affected |
| 4 - Very High | Massive impairment | Multiple critical processes affected |
| 3 - High | Significant impairment | One critical process affected |
| 2 - Medium | Noticeable impairment | Delays, but operation possible |
| 1 - Low | Minor impairment | No significant impact |

### 3.3 Legal and Regulatory Impact

**Compliance Risks:**
- Legal obligations (e.g., GDPR, occupational safety)
- Contractual obligations (SLAs, supply contracts)
- Reporting obligations to authorities
- Liability risks

**Assessment Scale:**
| Level | Description | Legal Impact |
|-------|-------------|--------------|
| 5 - Critical | Severe legal violation | Criminal proceedings, license loss |
| 4 - Very High | Significant violation | Fines > 100,000 € |
| 3 - High | Violation | Fines 10,000 - 100,000 € |
| 2 - Medium | Contract violation | Contractual penalties |
| 1 - Low | No obligation | No legal consequences |

### 3.4 Safety Impact

**Endangerment of Persons and Facilities:**
- Personal safety (employees, customers, visitors)
- Environmental hazard
- Plant safety
- Data security

**Assessment Scale:**
| Level | Description | Safety Impact |
|-------|-------------|---------------|
| 5 - Critical | Life-threatening | Deaths or serious injuries |
| 4 - Very High | Significant hazard | Injuries, environmental damage |
| 3 - High | Hazard | Health risks |
| 2 - Medium | Minor hazard | Property damage |
| 1 - Low | No hazard | No safety risks |

### 3.5 Reputation Impact

**Image and Trust:**
- Customer trust and customer satisfaction
- Brand image and public perception
- Trust of partners and investors
- Media coverage

**Assessment Scale:**
| Level | Description | Reputation Impact |
|-------|-------------|-------------------|
| 5 - Critical | Irreparable damage | Massive negative media coverage, customer exodus |
| 4 - Very High | Severe damage | National media coverage, significant loss of trust |
| 3 - High | Significant damage | Regional media coverage, customer complaints |
| 2 - Medium | Noticeable damage | Social media criticism, individual complaints |
| 1 - Low | Minor damage | No public perception |

## 4. Time Dependency of Impacts

### 4.1 Time Window Analysis

The impacts of process outages are assessed for different time windows:

**Time Windows:**
- **0-4 hours:** Immediate impacts
- **4-24 hours:** Short-term impacts
- **1-3 days:** Medium-term impacts
- **> 3 days:** Long-term impacts

### 4.2 Impact Progression

[TODO: Document the time-dependent development of impacts]

**Example for process "Order Processing":**

| Time Window | Financial Impact | Operational Impact | Reputation Impact |
|-------------|------------------|-------------------|-------------------|
| 0-4h | Low (Level 1) | Medium (Level 2) | Low (Level 1) |
| 4-24h | Medium (Level 2) | High (Level 3) | Medium (Level 2) |
| 1-3d | High (Level 3) | Very High (Level 4) | High (Level 3) |
| > 3d | Critical (Level 5) | Critical (Level 5) | Very High (Level 4) |

### 4.3 MTPD Determination

**Maximum Tolerable Period of Disruption (MTPD):**

The MTPD is the point at which the impacts of an outage become unacceptable.

**Determination:**
- MTPD = Point at which impacts reach Level 4 or 5
- Or: Point at which multiple dimensions reach Level 3

**Example:**
- Process "Order Processing": MTPD = 24 hours (from then Level 4/5)
- Process "Email": MTPD = 4 hours (from then Level 3 in multiple dimensions)

## 5. RTO/RPO Definition

### 5.1 RTO Determination

**Recovery Time Objective (RTO):**
- RTO must be significantly below MTPD (safety buffer)
- Recommendation: RTO = 50-70% of MTPD

**Example:**
- MTPD = 24 hours → RTO = 12-16 hours
- MTPD = 4 hours → RTO = 2-3 hours

### 5.2 RPO Determination

**Recovery Point Objective (RPO):**
- Maximum tolerable data loss
- Dependent on data change rate and business criticality

**Example:**
- Transaction data: RPO = 15 minutes (continuous replication)
- Configuration data: RPO = 24 hours (daily backup)
- Archive data: RPO = 7 days (weekly backup)

## 6. Results Approval

### 6.1 Responsible for Acceptance

**Department Level:**
- Process owners confirm BIA results for their processes
- Validation of RTO/RPO values

**Management Level:**
- {{ meta.roles.ceo.name }} (CEO) approves overall BIA
- {{ meta.roles.cio.name }} (CIO) approves IT-related RTO/RPO
- Department heads approve their areas

### 6.2 Approval Process

1. **Draft:** BCM manager creates BIA report
2. **Department Review:** Process owners review (2 weeks)
3. **Revision:** Feedback is incorporated
4. **Management Presentation:** Presentation of results
5. **Formal Approval:** Signatures of responsible parties
6. **Publication:** BIA results are communicated

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial creation |

<!-- End of template -->
