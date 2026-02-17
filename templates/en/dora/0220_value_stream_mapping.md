
Document-ID: dora-0220

Status: Draft
Classification: Internal

# Value Stream Mapping

**Document-ID:** [FRAMEWORK]-0220
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

## Purpose

This document describes the application of Value Stream Mapping to visualize and optimize the software delivery process.

## Scope

- Value Stream Mapping fundamentals
- Process mapping methodology
- Identification of waste
- Optimization approaches

## Organization Information

- **Organization**: [TODO]
- **VSM Owner**: [TODO]
- **Mapping Frequency**: [TODO]

## Value Stream Mapping Fundamentals

### Definition

Value Stream Mapping is a Lean management method for visualizing and analyzing the flow of materials and information required to bring a product or service to the customer.

### Goals

- **Transparency**: Visualize the entire process
- **Identify waste**: Recognize non-value-adding activities
- **Find bottlenecks**: Locate process constraints
- **Prioritize improvements**: Focus on biggest levers

## Process Mapping Methodology

### Step 1: Identify Process Steps

**Typical Steps in Software Delivery**:
1. Requirements analysis
2. Design
3. Implementation
4. Code review
5. Build
6. Automated tests
7. Manual tests
8. Security scan
9. Approval
10. Deployment
11. Verification

### Step 2: Capture Times

**For each step capture**:
- **Process Time**: Active processing time
- **Wait Time**: Waiting time until next step
- **Lead Time**: Total time (Process + Wait)

**Example**:
```
Step: Code Review
- Process Time: 2 hours
- Wait Time: 16 hours (waiting for reviewer)
- Lead Time: 18 hours
```

### Step 3: Create Value Stream Map

**Visualization**:
```
[Commit] → [Build: 10min] → [Wait: 2h] → [Test: 30min] → [Wait: 4h] → 
[Review: 2h] → [Wait: 16h] → [Approval: 1h] → [Wait: 8h] → [Deploy: 15min]

Total Process Time: 3h 55min
Total Wait Time: 30h
Total Lead Time: 33h 55min
```

### Step 4: Calculate Metrics

**Process Efficiency**:
```
Efficiency = Process Time / Lead Time × 100%
Efficiency = 3.92h / 33.92h × 100% = 11.6%
```

**Value-Added Ratio**:
```
VA Ratio = Value-Added Time / Total Time × 100%
```

## Types of Waste (Muda)

### 1. Waiting

**Examples**:
- Waiting for code reviews
- Waiting for approvals
- Waiting for test environments
- Waiting for deployment windows

**Solutions**:
- Automated approvals
- Self-service environments
- On-demand deployments
- Asynchronous reviews

### 2. Overprocessing

**Examples**:
- Redundant approvals
- Duplicate tests
- Unnecessary documentation
- Excessive meetings

**Solutions**:
- Process streamlining
- Automation
- Standardization
- Lean documentation

### 3. Defects

**Examples**:
- Bugs in production
- Failed deployments
- Rollbacks
- Rework

**Solutions**:
- Test automation
- Shift-left testing
- Quality gates
- Continuous monitoring

### 4. Motion

**Examples**:
- Context switching
- Tool changes
- Information search
- Handoffs between teams

**Solutions**:
- Integrated toolchains
- Single source of truth
- Cross-functional teams
- Automated workflows

## Bottleneck Identification

### Analysis Methods

**Queue Analysis**:
- Where do tasks accumulate?
- Which steps have the longest wait times?

**Throughput Analysis**:
- Which steps limit throughput?
- Where is capacity lowest?

**Variability Analysis**:
- Which steps have high variation?
- Where is predictability lowest?

### Prioritization

**Impact-Effort Matrix**:
```
High Impact, Low Effort → Implement immediately
High Impact, High Effort → Plan and implement
Low Impact, Low Effort → When convenient
Low Impact, High Effort → Avoid
```

## Optimization Approaches

### Short-term Measures

1. **Reduce wait times**
   - Automated notifications
   - SLA for reviews
   - Parallel processes

2. **Reduce batch sizes**
   - Smaller pull requests
   - More frequent deployments
   - Continuous integration

3. **Increase automation**
   - Automated tests
   - Automated deployments
   - Automated approvals

### Long-term Measures

1. **Process redesign**
   - Eliminate unnecessary steps
   - Parallelization
   - Self-service models

2. **Organizational structure**
   - Cross-functional teams
   - Reduce handoffs
   - Increased autonomy

3. **Technology modernization**
   - Modern CI/CD platforms
   - Cloud infrastructure
   - Microservices architecture

## Continuous Improvement

### Regular VSM Sessions

**Frequency**: [TODO]

**Participants**:
- Developers
- Operations
- Product Owner
- QA

**Agenda**:
1. Review current value stream
2. Analyze metrics
3. Identify improvements
4. Prioritize actions
5. Plan implementation

### Success Measurement

**KPIs**:
- Lead time reduction
- Process efficiency improvement
- Wait time reduction
- Throughput increase

<!-- Note: VSM makes waste visible and enables targeted optimization -->

