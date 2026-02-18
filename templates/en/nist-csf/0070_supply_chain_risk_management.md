
Document-ID: nist-csf-0070
Owner: {{ meta-handbook.owner }}

Status: Draft
Classification: Internal

# Supply Chain Risk Management (GV.SC)

**Document-ID:** [FRAMEWORK]-0070
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

## Purpose

This document describes the organization's approach to managing cybersecurity risks in the supply chain, including supplier assessment, contract requirements, and ongoing monitoring.

## Scope

{{ meta-handbook.scope }}

## Supply Chain Risk Strategy

### Strategic Objectives
- Identification and assessment of supplier risks
- Minimization of cybersecurity risks through third parties
- Ensuring supplier compliance
- Continuous monitoring of supplier performance

### Risk Categories

| Category | Description | Risk Level |
|----------|-------------|------------|
| Critical Suppliers | Access to critical systems/data | High |
| IT Service Providers | Managed services, Cloud providers | High |
| Software Suppliers | Applications, Components | Medium |
| Hardware Suppliers | IT equipment, Network devices | Medium |
| Other Suppliers | No IT involvement | Low |

## Supplier Lifecycle

### 1. Supplier Selection

**Due Diligence:**
- Security assessment
- Financial stability
- Reputation and references
- Compliance evidence

**Assessment Criteria:**
- ISO 27001 certification
- SOC 2 report
- Data protection compliance (GDPR)
- Incident response capabilities
- Business continuity planning

### 2. Contractual Requirements

**Security Clauses:**
- Non-disclosure agreements (NDA)
- Data protection provisions
- Security requirements
- Audit rights
- Incident reporting obligations
- Liability and insurance

**Service Level Agreements (SLAs):**
- Availability: {{ meta-handbook.sla_availability }}
- Incident response time: {{ meta-handbook.sla_response_time }}
- Patch management: {{ meta-handbook.sla_patch_time }}
- Backup and recovery: {{ meta-handbook.sla_recovery_time }}

### 3. Onboarding

**Security Requirements:**
- Access control and authentication
- Network segmentation
- Encryption
- Logging and monitoring
- Training of supplier employees

**Documentation:**
- Security policies
- Access documentation
- Contact information
- Escalation processes

### 4. Ongoing Monitoring

**Monitoring Activities:**
- Quarterly security reviews
- Annual audits
- Continuous compliance monitoring
- Incident tracking
- Performance metrics

**Key Performance Indicators:**
| KPI | Target | Measurement Frequency |
|-----|--------|----------------------|
| SLA Compliance | > 99% | Monthly |
| Security Incidents | 0 critical | Monthly |
| Patch Compliance | > 95% | Monthly |
| Audit Findings | < 5 High | Annually |

### 5. Offboarding

**Process:**
- Access revocation
- Data return/deletion
- Archive documentation
- Lessons learned
- Post-termination contractual obligations

## Supplier Categorization

### Tier 1: Critical Suppliers
**Criteria:**
- Access to critical systems or data
- High dependency
- Difficult to replace

**Requirements:**
- Comprehensive due diligence
- ISO 27001 certification required
- Quarterly reviews
- Annual audits
- Incident response plan required

**Examples:**
- {{ meta.critical_supplier_1 }}
- {{ meta.critical_supplier_2 }}

### Tier 2: Important Suppliers
**Criteria:**
- Access to non-critical systems
- Moderate dependency
- Replaceable with effort

**Requirements:**
- Standard due diligence
- SOC 2 or equivalent
- Semi-annual reviews
- Audits every 2 years

**Examples:**
- {{ meta.important_supplier_1 }}
- {{ meta.important_supplier_2 }}

### Tier 3: Standard Suppliers
**Criteria:**
- No direct system access
- Low dependency
- Easily replaceable

**Requirements:**
- Basic security assessment
- Annual reviews
- Self-assessment

## Risk Assessment

### Assessment Matrix

| Factor | Weight | Rating |
|--------|--------|--------|
| Data Access | 30% | 1-5 |
| System Access | 25% | 1-5 |
| Business Criticality | 20% | 1-5 |
| Compliance Status | 15% | 1-5 |
| Security Maturity | 10% | 1-5 |

**Total Risk = Σ (Factor × Weight)**

### Risk Treatment

| Risk Score | Category | Actions |
|------------|----------|---------|
| 4.0 - 5.0 | Critical | Immediate action, possible contract termination |
| 3.0 - 3.9 | High | Improvement plan required |
| 2.0 - 2.9 | Medium | Monitoring and regular reviews |
| 1.0 - 1.9 | Low | Standard monitoring |

## Incident Management

### Supplier Incidents

**Reporting Requirements:**
- Critical incidents: Immediate (< 1 hour)
- High incidents: < 4 hours
- Medium incidents: < 24 hours
- Low incidents: < 72 hours

**Response Process:**
1. Incident report by supplier
2. Assessment by SOC
3. Response coordination
4. Stakeholder communication
5. Post-incident review
6. Lessons learned

### Escalation
- Critical incidents → CISO + Executive Management
- Data breaches → DPO + Legal
- Contract violations → Procurement + Legal

## Compliance and Audits

### Audit Requirements

**Internal Audits:**
- Tier 1: Annually
- Tier 2: Every 2 years
- Tier 3: Risk-based

**External Audits:**
- ISO 27001 certification (Tier 1)
- SOC 2 reports (Tier 1-2)
- Penetration testing (as needed)

### Compliance Monitoring
- Continuous monitoring of certifications
- Tracking of audit findings
- Review of improvement actions

## Software Supply Chain

### Software Components
- Software Bill of Materials (SBOM)
- Vulnerability scanning
- License compliance
- Update management

### Open Source Software
- Approval process
- Vulnerability monitoring
- License review
- Community support assessment

## Document References

- 0020_organizational_context.md
- 0030_risk_management_strategy.md
- 0050_policy_framework.md
- 0150_supply_chain_risk_management.md (Identify)

