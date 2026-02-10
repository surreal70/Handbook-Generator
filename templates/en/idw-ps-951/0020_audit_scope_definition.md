# Audit Scope and Scope Definition

**Document-ID:** idw-ps-951-0020  
**Owner:** {{ meta.audit_lead }}  
**Version:** {{ meta.version }}  
**Status:** {{ meta.status }}  
**Classification:** {{ meta.classification }}  
**Last Update:** {{ meta.date }}

---

## 1. Purpose

This document defines the scope of the IT audit and specifies which IT systems, processes, and controls will be examined as part of the audit according to IDW PS 951.

## 2. Scope Definition

### Organizational Scope
- **Audited Organizational Units:** {{ source.audited_units }}
- **Locations:** {{ source.audited_locations }}
- **Business Areas:** {{ source.business_areas }}

### Technical Scope

#### IT Systems in Scope
| System | Description | Criticality | Audit Depth |
|--------|-------------|-------------|-------------|
| {{ source.system_1_name }} | {{ source.system_1_desc }} | {{ source.system_1_criticality }} | {{ source.system_1_depth }} |
| {{ source.system_2_name }} | {{ source.system_2_desc }} | {{ source.system_2_criticality }} | {{ source.system_2_depth }} |
| {{ source.system_3_name }} | {{ source.system_3_desc }} | {{ source.system_3_criticality }} | {{ source.system_3_depth }} |

#### IT Processes in Scope
- Change Management
- Incident Management
- Access Management
- Backup and Recovery
- {{ source.additional_processes }}

## 3. Audit Focus Areas

### Audit Areas according to IDW PS 951

#### IT Strategy and IT Organization
- IT governance structure
- IT organizational structure
- Roles and responsibilities
- IT steering committees

#### IT Processes
- IT service management processes
- Change and release management
- Problem and incident management
- Configuration management

#### IT Systems and Applications
- Application landscape
- System architecture
- Application controls
- Interface management

#### IT Infrastructure
- Server and storage systems
- Network infrastructure
- Database systems
- Backup systems

#### IT Security
- Access control
- Encryption
- Security monitoring
- Vulnerability management

#### Data Protection
- GDPR compliance
- Data protection controls
- Privacy by design

## 4. Exclusions and Boundaries

### Out of Scope
- {{ source.out_of_scope_1 }}
- {{ source.out_of_scope_2 }}
- {{ source.out_of_scope_3 }}

### Rationale for Exclusions
{{ source.exclusion_rationale }}

## 5. Materiality and Audit Depth

### Materiality Criteria
- **Financial:** {{ source.materiality_financial }}
- **Operational:** {{ source.materiality_operational }}
- **Compliance:** {{ source.materiality_compliance }}

### Audit Depth by Risk
- **High:** Detailed audit with extensive testing
- **Medium:** Standard audit with sampling
- **Low:** Overview audit

## 6. Interfaces to Other Audits

### Coordination with
- Annual financial statement audit
- Internal audit
- Data protection audit
- Compliance audits

### Coordination Approach
{{ source.coordination_approach }}

## 7. Scope Changes

### Change Process
Changes to the audit scope must be documented and approved:
- **Requestor:** {{ source.change_requestor }}
- **Approver:** {{ source.change_approver }}
- **Documentation:** Change log

### Change History
| Date | Change | Rationale | Approved by |
|------|--------|-----------|-------------|
| {{ source.change_date }} | {{ source.change_description }} | {{ source.change_reason }} | {{ source.change_approver }} |

## 8. References

- IDW PS 951 - Audit Standard
- Audit Engagement Letter
- IT System Documentation
- Risk Analysis

---

**Approved by:**  
{{ meta.audit_lead }}, Audit Lead  
Date: {{ meta.approval_date }}

**Next Review:** {{ meta.next_review }}

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | {{ meta.date }} | {{ meta.author }} | Initial creation |
