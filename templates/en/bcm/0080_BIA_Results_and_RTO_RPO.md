# BIA – Results and Target Values (RTO/RPO)

**Document-ID:** [FRAMEWORK]-0080
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

<!-- 
TEMPLATE AUTHOR NOTE:
This template documents the Business Impact Analysis results including RTO/RPO values.
It aligns with ISO 22301:2019 Clause 8.2.2 (Business impact analysis).

Customization required:
- Document all critical processes with their RTO/RPO values
- List dependencies for each process
- Define manual workarounds where possible
- Track open actions and measures
-->

## 1. Summary

### 1.1 Top-Critical Processes and Services

The following processes have been identified as business-critical (RTO < 24 hours):

[TODO: List the top-critical processes]

**Examples:**
1. **Order Processing** - RTO: 4 hours, RPO: 15 minutes
2. **Customer Service (24/7)** - RTO: 2 hours, RPO: 1 hour
3. **Production Control** - RTO: 8 hours, RPO: 30 minutes
4. **Payment Transactions** - RTO: 4 hours, RPO: 15 minutes
5. **Email and Communication** - RTO: 4 hours, RPO: 1 hour

### 1.2 Key Findings

[TODO: Document the most important findings from the BIA]

**Example Findings:**
- **Single Points of Failure:** ERP system has no redundancy, critical dependency
- **Personnel Dependencies:** Key persons in production without adequate backup
- **Supplier Risks:** Critical supplier has no own BCM
- **IT Infrastructure:** Network infrastructure partially not redundantly designed

## 2. BIA Results Table

### 2.1 Business-Critical Processes (Criticality: HIGH)

| Service/Process | MTPD/MAO | RTO | RPO | Manual Workarounds Possible? | Remarks |
|-----------------|----------|-----|-----|------------------------------|---------|
| [TODO: Process 1] | [TODO: 24h] | [TODO: 4h] | [TODO: 15min] | Yes/No/Partially | [TODO: Remarks] |
| [TODO: Process 2] | [TODO] | [TODO] | [TODO] | Yes/No/Partially | [TODO] |

**Example:**
| Service/Process | MTPD/MAO | RTO | RPO | Manual Workarounds Possible? | Remarks |
|-----------------|----------|-----|-----|------------------------------|---------|
| Order Processing | 24h | 4h | 15min | Partially (Excel lists) | ERP system critical |
| Customer Service | 8h | 2h | 1h | Yes (phone, email) | CRM system helpful but not mandatory |
| Production Control | 48h | 8h | 30min | No | Fully automated, no manual alternative |

### 2.2 Important Processes (Criticality: MEDIUM)

| Service/Process | MTPD/MAO | RTO | RPO | Manual Workarounds Possible? | Remarks |
|-----------------|----------|-----|-----|------------------------------|---------|
| [TODO: Process 1] | [TODO] | [TODO] | [TODO] | Yes/No/Partially | [TODO] |

### 2.3 Supporting Processes (Criticality: LOW)

| Service/Process | MTPD/MAO | RTO | RPO | Manual Workarounds Possible? | Remarks |
|-----------------|----------|-----|-----|------------------------------|---------|
| [TODO: Process 1] | [TODO] | [TODO] | [TODO] | Yes/No/Partially | [TODO] |

## 3. Dependencies per Critical Process

### 3.1 Process: [TODO: Process Name]

**People (Personnel):**
- [TODO: Minimum staffing, key persons, specialized knowledge]
- Example: At least 3 order processors, backup arrangement required

**Facilities (Locations and Premises):**
- [TODO: Required locations, rooms, infrastructure]
- Example: Office workstations, home office as alternative possible

**Technology (IT Systems):**
- [TODO: Critical IT systems and applications]
- Example: ERP system (SAP), email, network access

**Information (Data):**
- [TODO: Critical data and information]
- Example: Order database, customer master data, product configurations

**Suppliers (Suppliers and Partners):**
- [TODO: Critical suppliers and service providers]
- Example: Logistics service provider, cloud provider, payment service provider

### 3.2 Dependency Matrix

[TODO: Create a dependency matrix for all critical processes]

| Process | People | Facilities | Technology | Information | Suppliers |
|---------|--------|------------|------------|-------------|-----------|
| Order Processing | 3 employees | Office/Home-Office | ERP, Email | Order data | Logistics |
| Customer Service | 5 employees | Call center | CRM, Phone | Customer data | Telco |
| Production | 10 employees | Production hall | MES, SCADA | Production data | Suppliers |

## 4. Manual Workarounds and Emergency Operations

### 4.1 Workaround Strategies

[TODO: Document manual workarounds for critical processes]

**Example for process "Order Processing":**

**In case of ERP system failure:**
- **Workaround:** Manual order entry in Excel lists
- **Capacity:** Reduced to 30% of normal operations
- **Duration:** Maximum 24 hours (then data entry backlog too large)
- **Prerequisites:** Excel templates available, employees trained
- **Limitations:** No real-time inventory check, no automatic invoicing

**In case of site failure:**
- **Workaround:** Home office for order processing
- **Capacity:** 80% of normal operations
- **Duration:** Unlimited
- **Prerequisites:** VPN access, laptops, telephony via softphone
- **Limitations:** No physical document processing

### 4.2 Emergency Operations Capacities

| Process | Normal Operations | Emergency Operations (manual) | Emergency Operations (IT-DR) | Remarks |
|---------|-------------------|------------------------------|------------------------------|---------|
| Order Processing | 100% | 30% | 80% | Manual entry very labor-intensive |
| Customer Service | 100% | 70% | 90% | Phone as fallback |
| Production | 100% | 0% | 100% | No manual alternative |

## 5. Open Items and Measures

### 5.1 Identified Risks and Measures

| Measure | Description | Owner | Priority | Due | Status | Cost (estimated) |
|---------|-------------|-------|----------|-----|--------|------------------|
| [TODO: Measure 1] | [TODO: Description] | [TODO: Owner] | High/Medium/Low | [TODO: Date] | Open/In Progress/Done | [TODO: Amount] |

**Examples:**

| Measure | Description | Owner | Priority | Due | Status | Cost (estimated) |
|---------|-------------|-------|----------|-----|--------|------------------|
| ERP Redundancy | Implementation of high-availability cluster | {{ meta-organisation-roles.role_CIO }} | High | Q2 2026 | In Progress | 150,000 € |
| Backup Personnel | Training of backups for key persons | HR | High | Q1 2026 | Open | 20,000 € |
| Supplier BCM | Request BCM evidence from critical suppliers | Procurement | Medium | Q2 2026 | Open | 5,000 € |
| Network Redundancy | Second internet connection | {{ meta-organisation-roles.role_IT_Manager }} | High | Q1 2026 | In Progress | 30,000 € |

### 5.2 Prioritization of Measures

**Priority HIGH (implement immediately):**
- Measures to eliminate single points of failure
- Measures to meet critical RTO/RPO values
- Measures to fulfill regulatory requirements

**Priority MEDIUM (within 6-12 months):**
- Measures to improve resilience
- Measures to reduce dependencies
- Measures to improve workarounds

**Priority LOW (Nice-to-have):**
- Measures for further optimization
- Measures for less critical processes

## 6. Recovery Prioritization

### 6.1 Prioritization Matrix

In case of comprehensive failure, recovery occurs in the following order:

**Priority 1 (0-4 hours):**
1. Network infrastructure and internet connection
2. Email and communication
3. Authentication and access control

**Priority 2 (4-8 hours):**
4. ERP system (order processing, finance)
5. CRM system (customer service)
6. Production control systems

**Priority 3 (8-24 hours):**
7. Other business applications
8. Development and test environments
9. Reporting and analytics

### 6.2 Dependencies in Recovery

```
┌─────────────────────┐
│ Network/Internet    │
└──────────┬──────────┘
           │
    ┌──────┴──────┬──────────────┐
    │             │              │
┌───▼────┐  ┌────▼─────┐  ┌────▼─────┐
│ Email  │  │ Authenti-│  │ Firewall │
│        │  │ cation   │  │          │
└───┬────┘  └────┬─────┘  └────┬─────┘
    │            │             │
    └────────────┴─────────────┘
                 │
         ┌───────┴───────┐
         │               │
    ┌────▼────┐    ┌────▼────┐
    │ ERP     │    │ CRM     │
    └─────────┘    └─────────┘
```

## 7. Approval and Authorization

### 7.1 Approval by Departments

| Department | Responsible | Date | Signature |
|------------|--------------|------|-----------|
| [TODO: Department 1] | [TODO: Name] | [TODO: Date] | [TODO] |
| [TODO: Department 2] | [TODO: Name] | [TODO: Date] | [TODO] |

### 7.2 Management Approval

| Role | Name | Date | Signature |
|------|------|------|-----------|
| CEO | {{ meta-organisation-roles.role_CEO }} | [TODO: Date] | [TODO] |
| CIO | {{ meta-organisation-roles.role_CIO }} | [TODO: Date] | [TODO] |
| BCM Manager | [TODO: Name] | [TODO: Date] | [TODO] |

<!-- End of template -->
