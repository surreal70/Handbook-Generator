# Audit Events

**Document ID:** NIST-0230  
**Control Family:** Audit and Accountability (AU)  
**Control:** AU-2  
**Organization:** AdminSend GmbH  
**Owner:** IT Operations Manager  
**Version:** 1.0.0  
**Status:** Draft / In Review / Approved  
**Last Updated:** {{ meta.document.last_updated }}  

---

## 1. Control Description

**AU-2 Audit Events**

The organization determines that the information system is capable of auditing specified events and coordinates the security audit function with other organizational entities.

## 2. Control Implementation

### 2.1 Auditable Events

**Event Categories:**
- Account management events
- Authentication and authorization events
- Privilege escalation events
- System and application access events
- Configuration changes
- Security policy changes
- Data access and modification
- Network activity
- System startup and shutdown

[TODO: Specify auditable events for your organization]

### 2.2 Event Selection Criteria

**Selection Rationale:**
| Event Type | Rationale | Frequency |
|------------|-----------|-----------|
| Failed login attempts | Detect unauthorized access attempts | Real-time |
| Privilege changes | Monitor elevation of privileges | Real-time |
| Configuration changes | Track system modifications | Real-time |
| Data access | Monitor sensitive data access | Real-time |
| [TODO] | [TODO] | [TODO] |

### 2.3 Audit Coordination

**Coordination Activities:**
- Review audit requirements with stakeholders
- Coordinate with incident response team
- Align with compliance requirements
- Integrate with SIEM systems

[TODO: Describe coordination procedures]

### 2.4 Audit Review and Updates

**Review Schedule:** [TODO: e.g., Quarterly]  
**Update Triggers:**
- New threats identified
- Compliance requirement changes
- Incident lessons learned
- Technology changes

[TODO: Define review and update procedures]

## 3. Control Enhancements

- **AU-2(1):** Compilation of Audit Records from Multiple Sources
- **AU-2(2):** Selection of Audit Events by Component
- **AU-2(3):** Reviews and Updates
- **AU-2(4):** Privileged Functions

[TODO: Mark applicable enhancements]

## 4. Implementation Status

**Status:** [TODO: Implemented / Partially Implemented / Planned / Not Applicable]  
**Implementation Date:** [TODO: Date]  
**Responsible:** [TODO: Name/Role]  

## 5. Assessment

**Assessment Method:** Examine, Interview, Test  
**Assessment Status:** [TODO: Satisfied / Other than Satisfied / Not Applicable]  
**Findings:** [TODO: Description]  

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial creation |


