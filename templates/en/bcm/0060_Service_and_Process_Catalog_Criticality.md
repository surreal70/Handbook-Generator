# Service and Process Catalog with Criticality

**Document-ID:** [FRAMEWORK]-0060
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
This template documents the service and process catalog with criticality assessment.
It serves as the foundation for BIA, strategies, and BCM plans.

Customization required:
- List all business-critical services and processes
- Assign owners and criticality levels
- Document dependencies
- Identify stakeholders
-->

## 1. Objective

This document documents all services and business processes of {{ meta-organisation.name }} considered in BCM including:

- **Criticality assessment:** Classification by business criticality (High/Medium/Low)
- **Ownership:** Clear assignment of responsibilities
- **Dependencies:** Identification of critical dependencies
- **Stakeholders:** Affected customers and internal/external stakeholders

The service and process catalog forms the basis for:
- Business Impact Analysis (BIA)
- BCM strategies and continuity options
- Business Continuity Plans (BCP)
- IT Disaster Recovery Plans (DRP)

## 2. Service and Process Catalog

### 2.1 Business-Critical Services (Criticality: HIGH)

| Service/Process | Owner | Description | Top 5 Dependencies | Customers/Stakeholders |
|-----------------|-------|-------------|-------------------|------------------------|
| [TODO: Service 1] | [TODO: Owner] | [TODO: Description] | [TODO: 1. IT System, 2. Supplier, 3. Personnel, 4. Location, 5. Data] | [TODO: External customers, partners] |
| [TODO: Service 2] | [TODO: Owner] | [TODO: Description] | [TODO: Dependencies] | [TODO: Stakeholders] |

**Examples of business-critical services:**
- Customer service and support (24/7)
- Production control and execution
- Order processing and logistics
- Payment transactions and financial processes
- E-commerce platform

### 2.2 Important Services (Criticality: MEDIUM)

| Service/Process | Owner | Description | Top 5 Dependencies | Customers/Stakeholders |
|-----------------|-------|-------------|-------------------|------------------------|
| [TODO: Service 1] | [TODO: Owner] | [TODO: Description] | [TODO: Dependencies] | [TODO: Stakeholders] |

**Examples of important services:**
- Personnel administration and HR processes
- Procurement and purchasing
- Marketing and sales (not time-critical)
- Controlling and reporting
- Quality management

### 2.3 Supporting Services (Criticality: LOW)

| Service/Process | Owner | Description | Top 5 Dependencies | Customers/Stakeholders |
|-----------------|-------|-------------|-------------------|------------------------|
| [TODO: Service 1] | [TODO: Owner] | [TODO: Description] | [TODO: Dependencies] | [TODO: Stakeholders] |

**Examples of supporting services:**
- Development environments
- Training and learning platforms
- Archiving and document management
- Internal communication tools (not time-critical)

## 3. Criticality Assessment Criteria

### 3.1 Assessment Dimensions

Criticality is assessed based on the following dimensions:

**1. Financial Impact**
- Direct revenue loss per hour/day
- Contractual penalties and damage claims
- Additional costs for emergency measures

**2. Operational Impact**
- Impairment of other business processes
- Production failure or quality problems
- Backlog and rework effort

**3. Legal and Regulatory Requirements**
- Legal obligations and compliance
- Contractual obligations (SLAs)
- Reporting obligations to authorities

**4. Safety**
- Endangerment of human life
- Environmental hazard
- Plant safety

**5. Reputation and Trust**
- Customer trust and customer satisfaction
- Brand image and public perception
- Trust of partners and investors

### 3.2 Assessment Logic and Scoring

[TODO: Define your assessment logic]

**Example Scoring:**

| Criticality | Financial Impact | Operational Impact | Legal Impact | Safety Impact | Reputation Impact |
|-------------|------------------|-------------------|--------------|---------------|-------------------|
| **HIGH** | > 50,000 €/day | Multiple processes affected | Legal violation | Personal endangerment | Massive media coverage |
| **MEDIUM** | 10,000-50,000 €/day | One process affected | Contract violation | Property damage | Customer complaints |
| **LOW** | < 10,000 €/day | No impact | No obligation | No damage | No impact |

**Overall Assessment:**
- If at least one dimension "HIGH" → Overall criticality: **HIGH**
- If at least two dimensions "MEDIUM" → Overall criticality: **MEDIUM**
- Otherwise → Overall criticality: **LOW**

### 3.3 Criticality Matrix

```
Impact
  │
H │  [Service A]  [Service B]
  │  [Service C]
  │
M │              [Service D]
  │  [Service E]
  │
L │              [Service F]  [Service G]
  │
  └─────────────────────────────────────
    L           M           H
              Probability
```

[TODO: Place your services in the matrix]

## 4. IT Services and Systems

### 4.1 Critical IT Services

| IT Service | Supported Business Processes | Criticality | IT Owner | Technology |
|------------|----------------------------|--------------|----------|------------|
| [TODO: ERP System] | Order processing, finance, production | HIGH | {{ meta-organisation-roles.role_IT_Manager }} | [TODO: SAP/Oracle/etc.] |
| [TODO: Email] | All business processes | HIGH | {{ meta-organisation-roles.role_IT_Manager }} | [TODO: Exchange/M365/etc.] |
| [TODO: CRM] | Sales, customer service | MEDIUM | [TODO] | [TODO: Salesforce/etc.] |

### 4.2 IT Infrastructure

| Infrastructure Component | Dependent Services | Criticality | Location | Redundancy |
|-------------------------|-------------------|--------------|----------|------------|
| [TODO: Core Switch] | All IT services | HIGH | [TODO] | Yes/No |
| [TODO: Firewall] | Internet access | HIGH | [TODO] | Yes/No |
| [TODO: Storage] | All data | HIGH | [TODO] | Yes/No |

## 5. Dependency Analysis

### 5.1 Dependency Types

**People (Personnel):**
- Key persons and specialized knowledge
- Minimum staffing for operations
- External service providers

**Facilities (Locations and Premises):**
- Office buildings and production facilities
- Data centers
- Warehouses and logistics centers

**Technology (IT Systems and Technology):**
- Business applications (ERP, CRM, etc.)
- IT infrastructure (network, servers, storage)
- Cloud services

**Information (Data and Information):**
- Business data and customer data
- Configuration data
- Documentation and knowledge

**Suppliers (Suppliers and Partners):**
- Critical suppliers
- IT service providers and cloud providers
- Logistics partners

### 5.2 Dependency Matrix (Example)

[TODO: Create a dependency matrix for your critical services]

**Example for service "Order Processing":**

| Dependency Type | Concrete Dependency | Criticality | Fallback Option |
|-----------------|---------------------|--------------|-----------------|
| People | Order processors (min. 3) | HIGH | Training of backup personnel |
| Facilities | Office location headquarters | MEDIUM | Home office possible |
| Technology | ERP system | HIGH | None (single point of failure) |
| Information | Order database | HIGH | Backup available |
| Suppliers | Logistics service provider | HIGH | Alternative provider available |

## 6. Stakeholder Overview

### 6.1 Internal Stakeholders

| Stakeholder Group | Affected Services | Communication Need | Contact Person |
|-------------------|-------------------|-------------------|----------------|
| Executive Management | All critical services | Strategic decisions | {{ meta-organisation-roles.role_CEO }} |
| IT Department | All IT-dependent services | Technical coordination | {{ meta-organisation-roles.role_CIO }} |
| Departments | Respective services | Operational implementation | [TODO: Department heads] |
| Employees | All services | Information and instructions | [TODO: HR/Communication] |

### 6.2 External Stakeholders

| Stakeholder Group | Affected Services | Communication Need | Contact Person |
|-------------------|-------------------|-------------------|----------------|
| Customers | Customer service, production, delivery | Status updates, alternative solutions | [TODO: Customer service] |
| Suppliers | Procurement, production | Coordination, adjustments | [TODO: Procurement] |
| Partners | Joint services | Coordination, alignment | [TODO: Partner manager] |
| Authorities | Regulated services | Reports, evidence | [TODO: Compliance] |
| Media | All services (in crisis) | Press releases | [TODO: PR/Communication] |

## 7. Maintenance and Updates

**Responsible:** BCM Manager

**Update Interval:**
- Annual review of all services and criticality assessments
- Ad-hoc for organizational changes (new services, process changes)
- After BIA execution

**Review Process:**
1. BCM manager initiates review
2. Service owners review and update their services
3. Criticality assessment is validated
4. Changes are documented and communicated

<!-- End of template -->
