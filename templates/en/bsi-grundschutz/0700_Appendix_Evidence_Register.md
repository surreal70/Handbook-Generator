# Appendix: Evidence Register

**Document ID:** 0700  
**Document Type:** Appendix/Template  
**Reference Framework:** BSI IT-Grundschutz (BSI Standards 200-1/200-2/200-3)  
**Owner:** {{ meta.document.owner }}  
**Version:** {{ meta.document.version }}  
**Status:** {{ meta.document.status }}  
**Classification:** {{ meta.document.classification }}  
**Last Updated:** {{ meta.document.last_updated }}  
**Next Review:** {{ meta.document.next_review }}

---

<!-- 
TEMPLATE AUTHOR NOTE:
This template provides a central evidence register for tracking compliance documentation.
Reference: BSI Standard 200-1 (Documentation and Evidence Management)
-->

## 1. Purpose and Objectives

The evidence register of **{{ meta.organization.name }}** provides a central overview of all evidence documenting the implementation of security measures, policies, and guidelines.

**Responsible:** {{ meta.ciso.name }} (CISO)

## 2. Evidence Register

| Evidence ID | Topic/Measure | Description | Document Type | Location/Link | Owner | Retention Period | Last Review | Next Review | Status |
|---|---|---|---|---|---|---|---|---|---|
| E-001 | Patch Compliance | Monthly Patch Status Report | Report | [TODO: SharePoint/CMDB] | {{ meta.cio.name }} | 3 years | [TODO] | [TODO] | Current |
| E-002 | Backup Tests | Quarterly Restore Tests | Test Protocol | [TODO] | {{ meta.cio.name }} | 3 years | [TODO] | [TODO] | Current |
| E-003 | Training Records | Attendance Lists Security Awareness | Attendance List | [TODO: LMS] | {{ meta.ciso.name }} | 5 years | [TODO] | [TODO] | Current |
| E-004 | Audit Reports | Internal Audit Reports | Audit Report | [TODO] | Internal Audit | 10 years | [TODO] | [TODO] | Current |
| E-005 | Risk Acceptances | Documented Risk Acceptances | Approval Document | [TODO] | {{ meta.ceo.name }} | 5 years | [TODO] | [TODO] | Current |
| E-006 | Vulnerability Scans | Monthly Vulnerability Scan Reports | Scan Report | [TODO: Vulnerability Management Tool] | {{ meta.ciso.name }} | 2 years | [TODO] | [TODO] | Current |
| E-007 | Penetration Tests | Annual Pentest Reports | Pentest Report | [TODO] | {{ meta.ciso.name }} | 5 years | [TODO] | [TODO] | Current |
| E-008 | Incident Documentation | Incident Reports and Postmortems | Incident Report | [TODO: ITSM] | {{ meta.cio.name }} | 3 years | [TODO] | [TODO] | Current |
| E-009 | Change Approvals | Change Approvals with Security Review | Change Record | [TODO: ITSM] | {{ meta.cio.name }} | 2 years | [TODO] | [TODO] | Current |
| E-010 | Access Logs | Privileged Access Logs | Log Archive | [TODO: SIEM] | {{ meta.ciso.name }} | 1 year | [TODO] | [TODO] | Current |
| E-011 | Supplier Assessments | Third-Party Risk Assessments | Assessment Report | [TODO] | {{ meta.ciso.name }} | 3 years | [TODO] | [TODO] | Current |
| E-012 | Management Review | Annual Management Review Minutes | Minutes | [TODO] | {{ meta.ceo.name }} | 10 years | [TODO] | [TODO] | Current |
| E-013 | Basic Security Check | BSI Basic Check Results | Gap Analysis | [TODO] | {{ meta.ciso.name }} | 3 years | [TODO] | [TODO] | Current |
| E-014 | Protection Needs Assessment | Documented Protection Needs | Assessment | [TODO] | {{ meta.ciso.name }} | 5 years | [TODO] | [TODO] | Current |
| E-015 | Emergency Exercises | BCM/DR Test Protocols | Test Protocol | [TODO] | {{ meta.ciso.name }} | 3 years | [TODO] | [TODO] | Current |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## 3. Evidence Categories

### 3.1 Technical Evidence
- Scan Reports (Vulnerability, Compliance)
- Log Data and SIEM Evaluations
- Backup Protocols
- Patch Status Reports
- Configuration Documentation

### 3.2 Organizational Evidence
- Policies and Guidelines (approved)
- Training Records
- Audit Reports
- Management Review Minutes
- Risk Acceptances

### 3.3 Process Evidence
- Incident Reports
- Change Records
- Problem Management Documentation
- Test Protocols (DR, Backup, etc.)

### 3.4 Compliance Evidence
- Certificates (ISO, BSI, etc.)
- External Audit Reports
- Penetration Tests
- Data Protection Impact Assessments (DPIA)

## 4. Retention Periods

| Document Type | Retention Period | Legal Basis |
|---|---|---|
| Audit Reports | 10 years | Commercial Law |
| Training Records | 5 years | Evidence Requirement |
| Incident Reports | 3 years | Best Practice |
| Log Data | 1 year (Standard), 3 years (Critical Systems) | GDPR, BSI |
| Risk Acceptances | 5 years | Evidence Requirement |
| Contracts (Suppliers) | Contract Duration + 3 years | Commercial Law |

## 5. Access Control

**Access to Evidence:**
- **CISO:** Full Access
- **Internal Audit:** Full Access (Read)
- **Executive Management:** Full Access
- **Area Managers:** Access to Own Evidence
- **External Auditors:** Temporary Read Access (after approval)

**Storage Locations:**
- Central Document Repository: [TODO: e.g., SharePoint, Confluence]
- ITSM System: [TODO: e.g., ServiceNow, Jira]
- SIEM/Log Management: [TODO]
- CMDB: [TODO]

## 6. Review and Updates

**Regular Review:**
- **Quarterly:** Completeness Check
- **Annually:** Retention Period Review
- **During Audits:** Check Availability and Currency

**Responsible:** {{ meta.ciso.name }}

## 7. Approval

| Role | Name | Date | Approval |
|---|---|---|---|
| CISO | {{ meta.ciso.name }} | {{ meta.document.approval_date }} | {{ meta.document.approval_status }} |
| IT Management | {{ meta.cio.name }} | {{ meta.document.approval_date }} | {{ meta.document.approval_status }} |

---

**References:**
- BSI Standard 200-1: ISMS (Documentation)
- BSI Standard 200-2: IT-Grundschutz Methodology (Evidence Management)
- All ISMS Documents (0010-0630)

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial Creation |

<!-- End of template -->