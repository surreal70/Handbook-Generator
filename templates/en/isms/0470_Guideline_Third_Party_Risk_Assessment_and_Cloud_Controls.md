# Guideline: Third-Party Risk Assessment and Cloud Controls

**Document ID:** 0470  
**Document Type:** Guideline (detailed)  
**Associated Policy:** 0460_Policy_Supplier_and_Cloud_Security.md  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.5.19, A.5.20, A.5.21, A.5.22, A.5.23  
**Owner:** {{ meta.procurement.manager }}  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** {{ meta.document.date }}

---

## 1. Purpose and Scope

This guideline specifies the `0460_Policy_Supplier_and_Cloud_Security.md` and defines:
- Third-Party Risk Assessment processes
- Cloud Security Controls and Compliance
- Supplier management and monitoring

**Scope:** All suppliers and cloud services at **{{ meta.organization.name }}**

## 2. Third-Party Risk Assessment

### 2.1 Supplier Categorization

**Criticality:**
| Category | Definition | Examples | Assessment Depth |
|----------|------------|----------|------------------|
| Critical | Access to confidential data or critical systems | Cloud providers, Managed Security Services | Comprehensive |
| High | Important business services | ERP vendors, Payment providers | Detailed |
| Medium | Standard services | Office software, Marketing tools | Standard |
| Low | Minimal impact | Office supplies, Catering | Minimal |

### 2.2 Pre-Contract Assessment

**Phase 1: Initial Screening**
- Security controls questionnaire
- Certifications (ISO 27001, SOC 2)
- Data protection compliance (GDPR)
- Financial stability

**Phase 2: Detailed Assessment (Critical/High)**
- Security audit or on-site visit
- Penetration test reports
- Incident response capabilities
- Business continuity plans

**Phase 3: Contract Negotiation**
- Security clauses in contract
- SLAs for security and availability
- Audit rights
- Incident notification obligations

### 2.3 Ongoing Monitoring

**Frequency:**
- Critical: Quarterly review
- High: Semi-annually
- Medium: Annually
- Low: At contract renewal

**Monitoring Activities:**
- Check certification status
- Security incidents at supplier
- Request compliance reports
- Performance against SLAs

### 2.4 Offboarding

**Process:**
1. Data return or deletion
2. Revoke access
3. Confirm confidentiality obligations
4. Final documentation

## 3. Cloud Security Controls

### 3.1 Cloud Service Models

**IaaS (Infrastructure as a Service):**
- Shared Responsibility Model
- Customer responsible for OS, applications, data
- Provider responsible for infrastructure

**PaaS (Platform as a Service):**
- Provider responsible for platform
- Customer responsible for applications, data

**SaaS (Software as a Service):**
- Provider responsible for everything except data
- Customer responsible for data and access control

### 3.2 Cloud Security Assessment

**Before Cloud Adoption:**
- Cloud Security Posture Assessment
- Check data residency and compliance
- Evaluate encryption options
- Backup and DR capabilities

**Cloud Security Controls:**
- Identity and Access Management (IAM)
- Network segmentation
- Encryption (at rest, in transit)
- Logging and monitoring
- Compliance certifications

### 3.3 Cloud Access Security Broker (CASB)

**Functions:**
- Visibility into cloud usage
- Data Loss Prevention (DLP)
- Threat Protection
- Compliance monitoring

**CASB System:** {{ meta.security.casb_solution }}

### 3.4 Multi-Cloud and Hybrid-Cloud

**Governance:**
- Unified security policies across all clouds
- Central identity provider (SSO)
- Consistent monitoring

**Cloud Providers:**
- Primary: {{ meta.cloud.primary_provider }}
- Secondary: {{ meta.cloud.secondary_provider }}

## 4. Contract Management

### 4.1 Security Clauses

**Mandatory Clauses:**
- Data protection and GDPR compliance
- Security controls and standards
- Incident notification (within 24 hours)
- Audit rights
- Data return at contract end
- Liability for data breaches

### 4.2 Service Level Agreements (SLAs)

**Security SLAs:**
- Availability (e.g., 99.9%)
- Incident response time
- Patch management timeframe
- Backup frequency and retention

### 4.3 Data Processing Agreements (DPA)

**GDPR Requirements:**
- Data Processing Agreement (DPA)
- Technical and organizational measures (TOMs)
- Sub-processor list
- Data transfer to third countries

## 5. Supplier Risk Management

### 5.1 Risk Register

**Documentation:**
- Supplier, service, criticality
- Identified risks
- Mitigation measures
- Residual risk
- Review date

### 5.2 Incident Management

**For Supplier Incidents:**
1. Notification by supplier (SLA: 24h)
2. Impact assessment
3. Coordinate mitigation measures
4. Inform own customers (if required)
5. Post-incident review

### 5.3 Business Continuity

**Supplier Failure Scenarios:**
- Identify alternative suppliers
- Define exit strategy
- Ensure data portability

## 6. Compliance and Audit

### 6.1 Metrics (KPIs)

| Metric | Target Value |
|--------|--------------|
| Suppliers with current assessment | 100% |
| Critical suppliers with ISO 27001 | > 90% |
| SLA compliance | > 95% |
| Incident notification compliance | 100% |

### 6.2 Audit Evidence

- Supplier assessments
- Contracts with security clauses
- SLA reports
- Incident documentation

## 7. References

### Internal Documents
- `0460_Policy_Supplier_and_Cloud_Security.md`
- `0400_Policy_Incident_Management.md`

### External Standards
- **ISO/IEC 27001:2022 Annex A.5.19** - Information security in supplier relationships
- **ISO/IEC 27001:2022 Annex A.5.20** - Addressing information security within supplier agreements
- **ISO/IEC 27001:2022 Annex A.5.21** - Managing information security in the ICT supply chain
- **ISO/IEC 27001:2022 Annex A.5.22** - Monitoring, review and change management of supplier services
- **ISO/IEC 27001:2022 Annex A.5.23** - Information security for use of cloud services

---

**Approved by:** {{ meta.ciso.name }}, CISO  
**Next Review:** {{ meta.document.next_review }}

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial Creation |
