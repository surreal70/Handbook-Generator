---
Document-ID: tisax-0450
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Evidence Collection

## Purpose

This document describes procedures for evidence collection during security incidents according to TISAX requirements.

## Scope

This document applies to all security incidents at {{ source.organization_name }}.

## Evidence Collection Process

### Identification
**Potential Evidence:**
- Logs and protocols
- Memory images (RAM, hard drives)
- Network traffic
- Emails
- Documents
- Physical media

### Collection
**Methods:**
- Forensic copies
- Hash values for integrity assurance
- Write blockers for physical media
- Documentation of all steps

### Chain of Custody
**Documentation:**
- Who collected evidence
- When collected
- Where collected
- How collected
- Handovers and access

### Preservation
- Secure storage
- Access control
- Immutability
- Retention periods

## Forensic Tools

### Approved Tools
**Software:**
- {{ source.forensic_tool_1 }}
- {{ source.forensic_tool_2 }}
- Open-source tools (validated)

**Hardware:**
- Write blockers
- Forensic workstations
- Storage media

## Legal Aspects

### Compliance
- Observe data protection
- Legal admissibility
- Documentation
- Evidentiary value

### Cooperation with Authorities
**As needed:**
- Law enforcement agencies
- Data protection authorities
- Other supervisory authorities

## TISAX-Specific Requirements

### VDA ISA Controls
- **9.3**: Collection of evidence

### Assessment Evidence
- Evidence collection process
- Chain of custody documentation
- Forensic reports

## Metrics

{{ source.organization_name }} measures:
- Number of evidence collections
- Completeness of documentation
- Success rate in legal proceedings

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Initial creation |

<!-- End of template -->
