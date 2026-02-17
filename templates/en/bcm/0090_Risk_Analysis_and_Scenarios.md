# Risk Analysis and Scenarios

**Document-ID:** [FRAMEWORK]-0090
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

<!-- 
TEMPLATE AUTHOR NOTE:
This template defines risk analysis and disaster scenarios for BCM.
It aligns with ISO 22301:2019 Clause 8.2.3 (Business continuity strategy) and BSI Standard 200-4.

Customization required:
- Identify relevant disaster scenarios for your organization
- Assess probability and impact for each scenario
- Define risk treatment measures
- Establish risk tolerance thresholds
-->

## 1. Objective

The risk analysis of {{ meta-organisation.name }} serves to:

- **Identify** risks that can impair business continuity
- **Assess** probability of occurrence and impacts
- **Treat** through appropriate measures (avoidance, reduction, transfer, acceptance)
- **Monitor** and regularly review risks

The risk analysis complements the Business Impact Analysis (BIA) and forms the basis for the BCM strategy.

## 2. Scenario Catalog

### 2.1 IT and Cyber Risks

**2.1.1 Cyber Attack / Ransomware**
- **Description:** Encryption of data by ransomware, extortion
- **Affected Services:** All IT-dependent processes
- **Typical Impacts:** Data loss, system failure, extortion payment
- **Reference:** BSI Standard 200-4, Cyber Resilience section

**2.1.2 Data Center / Cloud Region Failure**
- **Description:** Complete failure of primary data center or cloud region
- **Affected Services:** All IT services
- **Typical Impacts:** Total IT system failure, data access not possible

**2.1.3 Network Failure / Internet Outage**
- **Description:** Failure of network infrastructure or internet connection
- **Affected Services:** All network-dependent services
- **Typical Impacts:** No communication, no data access

**2.1.4 Data Loss / Backup Failure**
- **Description:** Loss of critical data, backup not recoverable
- **Affected Services:** Data-dependent processes
- **Typical Impacts:** Permanent data loss, RPO exceedance

### 2.2 Infrastructure Risks

**2.2.1 Power Outage**
- **Description:** Failure of power supply at site
- **Affected Services:** All power-dependent systems and processes
- **Typical Impacts:** Production failure, IT failure, building technology failure

**2.2.2 Fire**
- **Description:** Fire in building or data center
- **Affected Services:** All services at affected site
- **Typical Impacts:** Site unusable, property damage, personal endangerment

**2.2.3 Water Damage**
- **Description:** Flooding, pipe burst, extinguishing water
- **Affected Services:** Services at affected site
- **Typical Impacts:** Building damage, IT hardware damage

**2.2.4 Site Not Accessible**
- **Description:** Evacuation, closure, natural event
- **Affected Services:** All site-dependent processes
- **Typical Impacts:** Employees cannot work, production stands still

### 2.3 Personnel Risks

**2.3.1 Personnel Loss / Pandemic**
- **Description:** Wave of illness, pandemic, mass absence
- **Affected Services:** Personnel-intensive processes
- **Typical Impacts:** Reduced capacity, key persons not available

**2.3.2 Loss of Key Persons**
- **Description:** Long-term loss of persons with specialized knowledge
- **Affected Services:** Processes with knowledge dependencies
- **Typical Impacts:** Processes cannot be performed

### 2.4 Supplier Risks

**2.4.1 Supplier Failure**
- **Description:** Critical supplier cannot deliver
- **Affected Services:** Production and procurement processes
- **Typical Impacts:** Production stop, delivery bottlenecks

**2.4.2 IT Service Provider Failure**
- **Description:** Failure of a critical IT service provider or cloud provider
- **Affected Services:** Outsourced IT services
- **Typical Impacts:** Service not available, no alternative

### 2.5 Natural Events and Environment

**2.5.1 Severe Weather / Storm**
- **Description:** Severe weather, storm, hail
- **Affected Services:** Site-dependent processes, logistics
- **Typical Impacts:** Building damage, traffic routes blocked

**2.5.2 Flooding**
- **Description:** Flooding by river or heavy rain
- **Affected Services:** Site-dependent processes
- **Typical Impacts:** Site flooded, massive property damage

**2.5.3 Earthquake** (depending on location)
- **Description:** Seismic event
- **Affected Services:** All services at site
- **Typical Impacts:** Building damage, infrastructure failure

[TODO: Add or remove scenarios according to your sites and risks]

## 3. Assessment Methodology

### 3.1 Assessment Scheme

**Probability of Occurrence (1-5):**
| Level | Designation | Description | Frequency |
|-------|-------------|-------------|-----------|
| 5 | Very High | Occurs regularly | Multiple times per year |
| 4 | High | Occurs occasionally | Once per year |
| 3 | Medium | Can occur | Once in 1-5 years |
| 2 | Low | Unlikely | Once in 5-10 years |
| 1 | Very Low | Very unlikely | Less than every 10 years |

**Impact (1-5):**
| Level | Designation | Description | Financial Impact |
|-------|-------------|-------------|------------------|
| 5 | Catastrophic | Existential threat | > 1 million € |
| 4 | Very High | Massive impact | 500,000 - 1 million € |
| 3 | High | Significant impact | 100,000 - 500,000 € |
| 2 | Medium | Noticeable impact | 10,000 - 100,000 € |
| 1 | Low | Minor impact | < 10,000 € |

**Risk Score:**
- Risk Score = Probability of Occurrence × Impact
- Value range: 1-25

### 3.2 Risk Tolerance and Thresholds

[TODO: Define your risk tolerance]

**Example:**

| Risk Score | Risk Level | Treatment | Escalation |
|------------|------------|-----------|------------|
| 15-25 | Critical (Red) | Immediate measures required | {{ meta-organisation-roles.role_CEO }} |
| 10-14 | High (Orange) | Measures within 3 months | BCM Manager |
| 5-9 | Medium (Yellow) | Measures within 12 months | Department |
| 1-4 | Low (Green) | Monitoring, no measures | Department |

### 3.3 Risk Matrix

```
Impact
    │
  5 │  10    15    20    25
    │ [Yellow][Orange][Red][Red]
  4 │   8    12    16    20
    │ [Yellow][Orange][Orange][Red]
  3 │   6     9    12    15
    │ [Yellow][Yellow][Orange][Orange]
  2 │   4     6     8    10
    │ [Green][Yellow][Yellow][Orange]
  1 │   2     3     4     5
    │ [Green][Green][Green][Yellow]
    └─────────────────────────
      1     2     3     4     5
           Probability
```

## 4. Risk Register

### 4.1 Assessed Risks

| Risk/Scenario | Affected Services | Prob. | Impact | Score | Risk Level | Controls (existing) | Measures (planned) | Owner |
|---------------|-------------------|-------|--------|-------|------------|---------------------|-------------------|-------|
| [TODO: Risk 1] | [TODO] | 3 | 5 | 15 | Orange | [TODO] | [TODO] | [TODO] |

**Examples:**

| Risk/Scenario | Affected Services | Prob. | Impact | Score | Risk Level | Controls (existing) | Measures (planned) | Owner |
|---------------|-------------------|-------|--------|-------|------------|---------------------|-------------------|-------|
| Ransomware Attack | All IT services | 4 | 5 | 20 | Red | Firewall, AV, Backup | EDR, Segmentation, Offline Backup | {{ meta-organisation-roles.role_CISO }} |
| Power Outage | Production, IT | 3 | 4 | 12 | Orange | UPS (15min) | Emergency generator | Facility Manager |
| Personnel Loss (Pandemic) | All processes | 2 | 4 | 8 | Yellow | Home office possible | Pandemic plan | HR |
| Supplier Failure | Production | 3 | 3 | 9 | Yellow | Inventory (2 weeks) | Second supplier | Procurement |
| Data Center Failure | All IT services | 2 | 5 | 10 | Orange | Backup available | DR site | {{ meta-organisation-roles.role_CIO }} |

### 4.2 Top Risks (Score ≥ 15)

[TODO: List the top risks requiring immediate measures]

1. **Ransomware Attack** (Score: 20)
   - Measures: EDR implementation, network segmentation, offline backups
   - Responsible: {{ meta-organisation-roles.role_CISO }}
   - Due: Q1 2026

2. [TODO: Additional top risk]

## 5. Risk Treatment

### 5.1 Treatment Strategies

**Risk Avoidance:**
- Activity is not performed or discontinued
- Example: Renounce use of insecure cloud services

**Risk Reduction:**
- Measures to reduce probability or impact
- Example: Implementation of redundancies, backup strategies

**Risk Transfer:**
- Transfer of risk to third parties (insurance, outsourcing)
- Example: Cyber insurance, SLA with service providers

**Risk Acceptance:**
- Conscious acceptance of residual risk
- Example: Low risks without measures

### 5.2 Measures Plan

| Measure | Risk | Strategy | Description | Owner | Priority | Cost | Due | Status |
|---------|------|----------|-------------|-------|----------|------|-----|--------|
| [TODO: Measure 1] | [TODO: Risk] | Reduction | [TODO: Description] | [TODO] | High | [TODO] | [TODO] | Open |

**Examples:**

| Measure | Risk | Strategy | Description | Owner | Priority | Cost | Due | Status |
|---------|------|----------|-------------|-------|----------|------|-----|--------|
| EDR Implementation | Ransomware | Reduction | Endpoint Detection & Response on all clients | {{ meta-organisation-roles.role_CISO }} | High | 50,000 € | Q1 2026 | In Progress |
| Emergency Generator | Power Outage | Reduction | Diesel generator for 48h operation | Facility | Medium | 80,000 € | Q2 2026 | Planned |
| Cyber Insurance | Ransomware | Transfer | Insurance for cyber incidents | CFO | High | 20,000 €/year | Q1 2026 | Open |

## 6. Monitoring and Review

### 6.1 Risk Monitoring

**Responsible:** BCM Manager

**Monitoring Interval:**
- Quarterly review of risk register
- Ad-hoc for new threats or incidents
- Annual complete risk analysis

**Indicators:**
- New threats (e.g., new ransomware variants)
- Incidents at comparable organizations
- Changes in threat landscape
- Technological developments

### 6.2 Escalation

**Escalation Criteria:**
- New risk with score ≥ 15
- Existing risk increases to score ≥ 15
- Risk occurs (incident)

**Escalation Paths:**
- Score ≥ 15: Immediate report to {{ meta-organisation-roles.role_CEO }}
- Score 10-14: Report to BCM manager
- Score < 10: Documentation in risk register

<!-- End of template -->
