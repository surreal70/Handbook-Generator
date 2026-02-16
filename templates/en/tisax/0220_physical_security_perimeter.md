---
Document-ID: tisax-0220
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Physical Security Perimeter

## Purpose

This document defines requirements for physical security perimeters according to TISAX requirements.

## Scope

This document applies to all locations and facilities of {{ source.organization_name }}.

## Security Zones

### Zone Classification
**Zone 1: Public Area** - Reception, visitor areas
**Zone 2: General Business Area** - Offices, meeting rooms
**Zone 3: Restricted Area** - Development areas, laboratories
**Zone 4: High Security Area** - Data centers, server rooms

## Perimeter Protection

### Outer Perimeter
- Fencing of premises
- Controlled access points
- Lighting
- Video surveillance
- Regular patrols

### Inner Perimeter
- Demarcation of sensitive areas
- Access control systems
- Monitoring
- Alerting

## Access Control

### Employees
- Personalized access cards
- Permissions based on need-to-know
- Regular recertification
- Logging

### Visitors
- Pre-registration
- Identity verification
- Visitor badge
- Escort by employee
- Logging

### External Service Providers
- Contractual agreement
- Security screening
- Time-limited access
- Monitoring of activities

## Physical Security Measures

### Doors and Windows
- Intrusion-resistant doors (RC2 or higher)
- Secured windows
- Automatic locking
- Alerting upon unauthorized opening

### Video Surveillance
- Monitoring of all access points
- Recording for at least {{ source.video_retention_days }} days
- Data protection compliant implementation
- Regular review

### Alarm System
- Intrusion detection system
- Fire alarm system
- Direct alerting of security service
- Regular maintenance and tests

### Lighting
- Adequate lighting of all outdoor areas
- Emergency lighting
- Motion-controlled lighting
- Regular maintenance

## Monitoring and Control

### Security Service
- Monitoring of access points
- Patrols
- Response to alarms
- Visitor management

**Availability:** {{ source.security_service_hours }}

### Logging
- All access
- Alarm triggers
- Security incidents
- Maintenance work

### Audits
- Monthly review of access logs
- Quarterly security audits
- Annual full review
- Ad-hoc upon incidents

## TISAX-Specific Requirements

### VDA ISA Controls
- **5.1**: Physical security perimeter
- **5.2**: Physical entry controls

### Assessment Evidence
- Security concept
- Access control system documentation
- Audit reports
- Security incident logs

## Metrics

{{ source.organization_name }} measures:
- Number of security incidents
- Number of unauthorized access attempts
- Average response time to alarms
- Compliance rate in audits

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Initial creation |

<!-- End of template -->
