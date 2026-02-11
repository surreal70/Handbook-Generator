---
Document-ID: tisax-0420
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Supplier Monitoring

## Purpose

This document describes the monitoring of suppliers at {{ source.organization_name }}.

## Monitoring Activities

### Regular Review
- Security evidence
- Certifications
- Incident reports
- SLA compliance

### Audits
- Frequency: {{ source.supplier_audit_frequency }}
- On-site audits for critical suppliers
- Remote audits

## Performance Measurement

| KPI | Target | Actual |
|-----|--------|--------|
| SLA Compliance | {{ source.sla_target }}% | {{ source.sla_actual }}% |
| Incident Response Time | < {{ source.incident_response_target }} | {{ source.incident_response_actual }} |
| Availability | {{ source.availability_target }}% | {{ source.availability_actual }}% |

## Escalation

In case of non-compliance:
1. Notification to supplier
2. Corrective actions
3. Escalation to management
4. Contract termination (last resort)

<!-- Note: Monitor suppliers continuously -->

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Initial creation |

<!-- End of template -->
