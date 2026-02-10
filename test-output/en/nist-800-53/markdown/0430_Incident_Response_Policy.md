# Incident Response Policy

**Document-ID:** NIST-0430  
**Control Family:** Incident Response (IR)  
**Control:** IR-1, IR-4, IR-5, IR-6  
**Organization:** AdminSend GmbH  
**Owner:** IT Operations Manager  
**Version:** 1.0.0  
**Status:** Draft / In Review / Approved  
**Last Updated:** {{ meta.document.last_updated }}  

---

## 1. Control Description

**IR-1 Policy and Procedures**  
**IR-4 Incident Handling**  
**IR-5 Incident Monitoring**  
**IR-6 Incident Reporting**  

The organization implements incident response capabilities.

## 2. Control Implementation

### 2.1 Incident Response Process

**Incident Response Phases:**
1. **Preparation:** Training, tools, procedures
2. **Detection and Analysis:** Identify and assess incidents
3. **Containment, Eradication, and Recovery:** Limit damage and restore
4. **Post-Incident Activity:** Lessons learned

### 2.2 Incident Categories

| Category | Severity | Response Time | Escalation |
|----------|----------|---------------|------------|
| Critical | High | Immediate | ISSO, ISSM, AO |
| Major | Medium | 1 hour | ISSO, ISSM |
| Minor | Low | 4 hours | ISSO |

### 2.3 Incident Response Team

**Team Members:**
- Incident Response Manager: [TODO: Name]
- ISSO: {{ meta.roles.isso.name }}
- System Administrator: [TODO: Name]
- Legal: [TODO: Name]
- Public Relations: [TODO: Name]

### 2.4 Incident Reporting

**Internal Reporting:**
- ISSO: Immediate
- ISSM: Within 1 hour
- AO: Within 4 hours

**External Reporting:**
- US-CERT: Within 1 hour for major incidents
- Law Enforcement: As required
- Affected Parties: As required

### 2.5 Incident Documentation

**Required Information:**
- Incident date/time
- Detection method
- Incident description
- Systems affected
- Actions taken
- Lessons learned

## 3. Implementation Status

**Status:** [TODO: Implemented / Partially Implemented / Planned]  
**Incident Response Plan:** [TODO: Document reference]  
**Last Incident:** [TODO: Date or None]  

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial creation |


