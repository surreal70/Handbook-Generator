---
Document-ID: nist-csf-0310
Owner: {{ meta.owner }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Sicherheitsüberwachung (DE.CM)

## Zweck

This document describes continuous security monitoring processes.

## Geltungsbereich

{{ meta.scope }}

## Monitoring Activities

### Continuous Monitoring
- Network monitoring
- System monitoring
- Application monitoring
- User activity monitoring

### Monitoring Tools
- SIEM: {{ meta.siem_tool }}
- IDS/IPS: {{ meta.ids_tool }}
- Log management: {{ meta.log_tool }}

## Dokumentenverweise

- 0300_anomalies_events.md
- 0400_response_planning.md (Respond)

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | {{ meta.date }} | {{ meta.author }} | Initiale Erstellung |

<!-- Author Notes: Monitor 24/7 for critical systems -->
