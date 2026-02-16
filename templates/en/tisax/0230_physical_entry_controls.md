---
Document-ID: tisax-0230
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Physical Entry Controls

## Purpose

This document describes measures for physical entry control according to TISAX requirements.

## Scope

This document applies to all controlled areas of {{ source.organization_name }}.

## Access Control Systems

### Electronic Access Control
- Card readers
- Biometric scanners
- PIN pads
- Central management software

### Mechanical Security
- High-security locks
- Locking systems
- Key management
- Emergency access

## Access Permissions

### Permission Assignment
1. Request by supervisor
2. Approval by facility management
3. Configuration in system
4. Issuance of access credentials
5. Employee training

### Permission Revocation
- Upon departure
- Upon role change
- Upon expiration
- Upon security incident

## Visitor Management

### Visitor Registration
1. Pre-registration by host
2. Identity verification at reception
3. Issuance of visitor badge
4. Security briefing
5. Escort by employee

### Visitor Escort
- Constant escort in sensitive areas
- Visible visitor badge
- No unattended access
- Logging of visited areas

## Monitoring

### Logging
- Successful access
- Failed access attempts
- Door openings outside business hours
- Alarm triggers

**Retention:** At least {{ source.access_log_retention_days }} days

### Monitoring
- Unauthorized access attempts
- Doors open longer than {{ source.door_open_timeout }} seconds
- Access outside business hours
- Multiple card usage (tailgating detection)

## TISAX-Specific Requirements

### VDA ISA Controls
- **5.2**: Physical entry controls

### Assessment Evidence
- Access control system documentation
- Permission concept
- Access logs
- Visitor lists

## Metrics

{{ source.organization_name }} measures:
- Number of active access permissions
- Number of failed access attempts
- Number of visitors per month
- Compliance rate in audits

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Initial creation |

<!-- End of template -->
