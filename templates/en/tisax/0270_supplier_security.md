---
Document-ID: tisax-0400
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Supplier Security

## Purpose

This document describes the security requirements for suppliers at {{ source.organization_name }}.

## Supplier Assessment

### Selection Criteria
- Security certifications
- Data protection compliance
- Financial stability
- References

### Risk Assessment
- Criticality of service
- Access to sensitive data
- Supplier location

## Security Requirements

### Minimum Requirements
- Information security policy
- Access control
- Encryption
- Incident management
- Business continuity

### TISAX Requirements
Suppliers with access to confidential information must be TISAX certified:
- Assessment Level: {{ source.supplier_tisax_level }}

## Supplier Register

| Supplier | Service | Risk Level | TISAX Status |
|----------|---------|------------|--------------|
| {{ source.supplier_1 }} | {{ source.supplier_1_service }} | {{ source.supplier_1_risk }} | {{ source.supplier_1_tisax }} |
| {{ source.supplier_2 }} | {{ source.supplier_2_service }} | {{ source.supplier_2_risk }} | {{ source.supplier_2_tisax }} |

<!-- Note: Maintain the supplier register -->

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Initial creation |

<!-- End of template -->
