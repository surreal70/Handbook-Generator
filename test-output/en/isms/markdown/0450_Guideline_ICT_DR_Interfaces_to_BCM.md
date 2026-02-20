# Guideline: ICT Disaster Recovery - Interfaces to BCM

**Document-ID:** [FRAMEWORK]-0450
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

## 1. Purpose and Scope

This guideline implements the `0440_Policy_Business_Continuity_ICT_Readiness.md` and defines:
- ICT disaster recovery plans and processes
- Interfaces to Business Continuity Management (BCM)
- ICT readiness for emergency situations

**Scope:** All IT systems and services at **AdminSend GmbH**

## 2. ICT Disaster Recovery Strategy

### 2.1 Recovery Objectives

**RTO (Recovery Time Objective):**
| System Tier | RTO | Rationale |
|-------------|-----|-----------|
| Tier 1 (Critical) | 4 hours | Business-critical systems |
| Tier 2 (Important) | 24 hours | Important business functions |
| Tier 3 (Standard) | 72 hours | Standard IT services |

**RPO (Recovery Point Objective):**
| System Tier | RPO | Backup Frequency |
|-------------|-----|------------------|
| Tier 1 | 1 hour | Hourly |
| Tier 2 | 24 hours | Daily |
| Tier 3 | 7 days | Weekly |

### 2.2 DR Strategies

**Hot Site:**
- Fully redundant infrastructure
- Real-time replication
- Immediate failover capability
- For Tier 1 systems

**Warm Site:**
- Partially pre-configured infrastructure
- Regular backups
- Activation within hours
- For Tier 2 systems

**Cold Site:**
- Basic infrastructure available
- Recovery from backups
- Activation within days
- For Tier 3 systems

## 3. DR Infrastructure

### 3.1 Primary Data Center

**Location:** [[ netbox.site.primary ]]  
**Systems:** All production systems  
**Redundancy:** N+1 for critical components

### 3.2 DR Site

**Location:** [[ netbox.site.dr ]]  
**Distance:** > 50 km from primary site  
**Systems:** Replicated Tier 1 systems, backup infrastructure

### 3.3 Cloud DR

**Cloud Provider:** {{ meta-handbook.cloud_dr_provider }}  
**Regions:** {{ meta-handbook.cloud_primary_region }}, {{ meta-handbook.cloud_dr_region }}  
**Services:** IaaS for DR workloads

## 4. Interfaces to BCM

### 4.1 Business Impact Analysis (BIA)

**ICT Input for BIA:**
- System dependencies
- RTO/RPO capabilities
- Single points of failure
- Recovery costs

**BIA Output for ICT:**
- Criticality of business processes
- Maximum tolerable downtime (MTD)
- Recovery prioritization

### 4.2 BCM Plans

**ICT Contributions:**
- IT Disaster Recovery Plan (DRP)
- Technical recovery procedures
- IT personnel contact lists
- Escalation paths

**BCM Coordination:**
- Alignment with Business Continuity Plans (BCP)
- Joint exercises and tests
- Consistent communication

### 4.3 Crisis Management

**ICT Role in Crisis Team:**
- IT representative in crisis team
- Status updates on IT systems
- Technical decision support
- Coordination of IT recovery

## 5. DR Activation

### 5.1 Activation Criteria

**Automatic Activation:**
- Complete failure of primary site
- Critical infrastructure components failed
- Natural disasters

**Manual Activation:**
- Decision by crisis team
- Planned failover tests
- Maintenance activities

### 5.2 Activation Process

**Phase 1: Assessment (0-30 minutes)**
1. Assess extent of damage
2. Decide on DR activation
3. Inform crisis team
4. Mobilize DR team

**Phase 2: Activation (30 minutes - 4 hours)**
1. Activate DR infrastructure
2. Restore systems (by priority)
3. Switch network routing
4. Functional test

**Phase 3: Operation (variable)**
1. Operation in DR mode
2. Intensify monitoring
3. Regular status updates
4. Prepare return

**Phase 4: Failback (planned)**
1. Restore primary site
2. Synchronize data
3. Planned failback
4. Verification

## 6. DR Tests

### 6.1 Test Types

**Tabletop Exercise:**
- Frequency: Quarterly
- Walkthrough of DR plan
- No technical activation

**Partial Failover:**
- Frequency: Semi-annually
- Individual systems failover
- Minimal business impact

**Full DR Drill:**
- Frequency: Annually
- Complete failover of all Tier 1 systems
- Planned downtime required

### 6.2 Test Documentation

**Test Protocol:**
- Date, participants, scope
- Steps performed
- Measured RTO/RPO
- Problems and lessons learned
- Improvement measures

## 7. Compliance and Audit

### 7.1 Key Performance Indicators (KPIs)

| Metric | Target Value |
|--------|--------------|
| DR test success rate | 100% |
| RTO compliance (test) | 100% |
| RPO compliance (test) | 100% |
| DR plan currency | < 6 months |

### 7.2 Audit Evidence

- DR plans and procedures
- Test protocols
- BIA documentation
- Failover logs

## 8. References

### Internal Documents
- `0440_Policy_Business_Continuity_ICT_Readiness.md`
- `0430_Guideline_Backup_Restore_and_Regular_Tests.md`
- BCM Handbook (if available)

### External Standards
- **ISO/IEC 27001:2022 Annex A.5.29** - Information security during disruption
- **ISO/IEC 27001:2022 Annex A.5.30** - ICT readiness for business continuity
- **ISO 22301** - Business Continuity Management

**Approved by:** [TODO], CISO  
**Next Review:** [TODO]

