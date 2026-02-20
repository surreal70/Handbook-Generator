# Contacts and Escalation

**Document-ID:** BCM-0050
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



## 1. Contact List (Internal)

> **Attention:** Contact lists contain personal data and are subject to special data protection requirements (GDPR). Access only for authorized persons. Quarterly updates required.

### 1.1 Crisis Team

| Function | Name | Phone | Mobile | Email | Deputy |
|----------|------|-------|--------|-------|--------|
| **Crisis Team Lead** | [TODO] | [TODO] | [TODO: Mobile] | [TODO] | [TODO] |
| **CIO** | [TODO] | [TODO] | [TODO: Mobile] | [TODO] | [TODO] |
| **CISO** | [TODO] | [TODO] | [TODO: Mobile] | [TODO] | [TODO] |
| **CFO** | [TODO] | [TODO] | [TODO: Mobile] | [TODO] | [TODO] |
| **COO** | [TODO] | [TODO] | [TODO: Mobile] | [TODO] | [TODO] |

### 1.2 BCM Organization

| Function | Name | Phone | Mobile | Email | Deputy |
|----------|------|-------|--------|-------|--------|
| **BCM Manager** | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| **Incident Commander** | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| **IT-DR Lead** | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| **Communication** | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

### 1.3 IT Operations and Service Desk

| Function | Name | Phone | Mobile | Email | Availability |
|----------|------|-------|--------|-------|--------------|
| **Service Desk** | [TODO] | [TODO] | [TODO] | [TODO] | 24/7 |
| **IT Operations Manager** | [TODO] | [TODO] | [TODO] | [TODO] | 24/7 on-call |
| **Network Team** | [TODO] | [TODO] | [TODO] | [TODO] | 24/7 on-call |
| **Server Team** | [TODO] | [TODO] | [TODO] | [TODO] | 24/7 on-call |
| **Security Team** | [TODO] | [TODO] | [TODO] | [TODO] | 24/7 on-call |

### 1.4 Departments

| Department | Contact Person | Phone | Mobile | Email | Deputy |
|------------|----------------|-------|--------|-------|--------|
| **Production** | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| **Sales** | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| **Finance** | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| **HR** | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| **Procurement** | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## 2. External Contacts

### 2.1 IT Service Providers and Providers

| Organization | Role/Service | Contact | Phone | Email | Contract/Customer No. | Availability |
|--------------|--------------|---------|-------|-------|----------------------|--------------|
| [TODO: Cloud Provider] | Cloud Infrastructure | [TODO] | [TODO] | [TODO] | [TODO] | 24/7 |
| [TODO: ISP] | Internet Connection | [TODO] | [TODO] | [TODO] | [TODO] | 24/7 |
| [TODO: Telco] | Telephony | [TODO] | [TODO] | [TODO] | [TODO] | 24/7 |
| [TODO: Backup Provider] | Backup Services | [TODO] | [TODO] | [TODO] | [TODO] | 24/7 |
| [TODO: Security Provider] | Security Services | [TODO] | [TODO] | [TODO] | [TODO] | 24/7 |

### 2.2 Emergency Services and Authorities

| Organization | Purpose | Phone | Emergency Number | Address |
|--------------|---------|-------|------------------|---------|
| **Fire Department** | Fire, hazardous materials | [TODO: Local] | **112** | [TODO] |
| **Police** | Security, crimes | [TODO: Local] | **110** | [TODO] |
| **Emergency Medical Services** | Medical emergencies | [TODO: Local] | **112** | [TODO] |
| **Poison Control** | Hazardous material accidents | [TODO: Regional] | [TODO] | [TODO] |
| **BSI** | Cyber incidents | +49 228 99 9582-222 | - | Godesberger Allee 185-189, 53175 Bonn |

### 2.3 Critical Suppliers

| Supplier | Product/Service | Contact Person | Phone | Email | Criticality |
|----------|-----------------|----------------|-------|-------|-------------|
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | High / Medium / Low |

### 2.4 Customers and Partners (if needed)

| Organization | Contact Person | Phone | Email | Notify when |
|--------------|----------------|-------|-------|-------------|
| [TODO: Major Customer] | [TODO] | [TODO] | [TODO] | Service outage > 4h |

## 3. Escalation Matrix

### 3.1 Escalation Levels

| Level | Designation | Trigger | Responsible | Response Time | Communication Obligation |
|-------|-------------|---------|-------------|---------------|-------------------------|
| **1** | Disruption | Individual systems affected, no impact on critical services | IT Operations | 4 hours | Inform service desk |
| **2** | Major Incident | Critical service impaired, RTO at risk | Incident Commander | 1 hour | Inform management |
| **3** | BCM Activation | Multiple critical services failed, business operations at risk | Crisis Team | 30 minutes | Activate crisis team, inform external stakeholders |
| **4** | Disaster | Site unavailable, massive impact | Crisis Team Lead | Immediate | All stakeholders, authorities, media |

### 3.2 Escalation Criteria

**Escalation to Level 2 (Major Incident):**
- RTO of a critical service will likely be exceeded
- More than [TODO: X] users affected
- Financial damage > [TODO: Amount] per hour
- Data loss threatens (RPO exceedance)
- Security incident with high impact

**Escalation to Level 3 (BCM Activation):**
- Multiple critical services simultaneously failed
- Recovery within RTO not possible
- Site not accessible
- Massive cyber attack (ransomware, DDoS)
- Natural disaster or severe accident

**Escalation to Level 4 (Disaster):**
- Main site completely failed
- Human lives at risk
- Existential threat to the company
- Official order (e.g., evacuation)

### 3.3 Escalation Process

```
┌─────────────────┐
│ Disruption      │
│ detected        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Initial         │
│ assessment      │
│ (IT Operations) │
└────────┬────────┘
         │
    ┌────┴────┐
    │ Level 1?│
    └────┬────┘
         │ No
         ▼
┌─────────────────┐      ┌──────────────────┐
│ Major Incident? │─Yes─>│ Alert Incident   │
│ (Level 2)       │      │ Commander        │
└────────┬────────┘      └──────────────────┘
         │ No
         ▼
┌─────────────────┐      ┌──────────────────┐
│ BCM Activation? │─Yes─>│ Activate Crisis  │
│ (Level 3)       │      │ Team             │
└────────┬────────┘      └──────────────────┘
         │ No
         ▼
┌─────────────────┐      ┌──────────────────┐
│ Disaster?       │─Yes─>│ Inform Crisis    │
│ (Level 4)       │      │ Team Lead        │
│                 │      │ immediately      │
└─────────────────┘      └──────────────────┘
```

## 4. Alerting Process

### 4.1 Alerting Channels

**Primary:** Phone (Mobile Phone)
- Direct call to defined contact persons
- If unreachable: Contact deputy

**Secondary:** SMS / Messenger
- Parallel notification via SMS
- Messenger groups for quick coordination

**Tertiary:** Email
- Documentation and traceability
- Not suitable for time-critical alerting

### 4.2 Alerting Procedure

1. **Initial detection:** Disruption detected (monitoring, report, observation)
2. **Initial assessment:** IT operations assesses severity and impact
3. **Alerting:** Contact according to escalation level
4. **Confirmation:** Recipient confirms receipt and availability
5. **Briefing:** Brief situation description and initial measures
6. **Documentation:** Alerting documented in logbook

### 4.3 Crisis Team Alerting List

For BCM activation (Level 3), the following persons are alerted:

1. [TODO] (Crisis Team Lead)
2. [TODO] (CIO)
3. [TODO] (CISO)
4. [TODO: BCM Manager]
5. [TODO: Communications Manager]
6. Additional crisis team members depending on situation

**Alerting sequence:** Parallel, not sequential

## 5. On-Call and On-Call Duty

### 5.1 On-Call Schedule

[TODO: Define on-call schedules for critical roles]

**Example IT Operations:**

| Week | Primary | Secondary | Tertiary |
|------|---------|-----------|----------|
| 01 | [Name 1] | [Name 2] | [Name 3] |
| 02 | [Name 2] | [Name 3] | [Name 1] |
| 03 | [Name 3] | [Name 1] | [Name 2] |

**Update:** Weekly, by Friday 12:00 PM latest

### 5.2 On-Call Obligations

**During on-call duty:**
- Mobile phone switched on and reachable (24/7)
- Response time: Within 30 minutes
- Sober and ready for duty
- Access to laptop and VPN
- Knowledge of current runbooks and escalation paths

**Compensation:** According to company agreement / employment contract

## 6. Contact List Maintenance

### 6.1 Update Process

**Responsible:** BCM Manager

**Update Interval:**
- Quarterly review of all contact data
- Ad-hoc for personnel changes
- After each BCM exercise

**Process:**
1. BCM manager requests update
2. Departments review and report changes
3. BCM manager updates contact lists
4. New version distributed and old version archived

### 6.2 Data Protection

Contact lists are subject to GDPR:
- Access only for authorized persons
- Encrypted storage
- No disclosure to third parties without consent
- Deletion upon employee departure


