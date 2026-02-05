# Policy: Incident Management



**Document ID:** 0400  
**Document Type:** Policy (abstract)  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.5.24-A.5.28 (incl. Amendment 1:2024)  
**Owner:** Thomas Weber  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** {{ meta.document.date }}  
**Next Review:** {{ meta.document.next_review }}

---

## 1. Purpose

This policy defines the principles for incident management and security incident response at **AdminSend GmbH**. It ensures that security incidents are detected, assessed, handled, and documented in a timely manner to minimize damage and learn from incidents.

## 2. Scope

This policy applies to:

- **Organizational Units:** All departments and locations of AdminSend GmbH
- **Incident Types:** Security incidents, data breaches, malware, phishing, DDoS, insider threats
- **Systems:** All IT systems, applications, networks, cloud services
- **Personnel:** All employees, contractors, suppliers
- **Locations:** {{ netbox.site.name }} and all other operational sites

**Exceptions:** Exceptions are only permitted through the defined exception process (`0640_Policy_Exceptions_and_Risk_Waivers.md`).

## 3. Principles (Policy Statements)

### 3.1 Incident Response Capability
The organization maintains an incident response capability with defined processes, roles, and tools for handling security incidents.

### 3.2 Reporting Obligation
All employees are required to report suspected or confirmed security incidents immediately. There are no negative consequences for good-faith reports.

### 3.3 Incident Categorization and Prioritization
Incidents are categorized by severity and impact:
- **Critical:** Severe impact on business operations or data protection
- **High:** Significant impact, but business operations not critically endangered
- **Medium:** Moderate impact, limited impairment
- **Low:** Minor impact, no immediate danger

### 3.4 Incident Response Lifecycle
Incidents are handled through a structured process:
- **Detection & Reporting:** Detection and reporting
- **Triage & Assessment:** Assessment and prioritization
- **Containment:** Containment for damage limitation
- **Eradication:** Elimination of the cause
- **Recovery:** Restoration of normal operations
- **Post-Incident Review:** Follow-up and lessons learned

### 3.5 Escalation and Communication
Critical incidents are escalated according to defined escalation paths to management, legal, PR, and authorities as appropriate. Communication follows established communication plans.

### 3.6 Forensics and Evidence Preservation
Forensic analysis is performed for severe incidents. Evidence is securely preserved and documented for possible legal action.

### 3.7 Data Breach Notification
Data breaches are reported to supervisory authorities and affected individuals within 72 hours in accordance with GDPR and other regulatory requirements.

### 3.8 Continuous Improvement
Lessons learned are derived from every incident. Insights flow into the improvement of processes, controls, and awareness.

## 4. Roles and Responsibilities

### RACI Matrix: Incident Management

| Activity | CISO | Incident Manager | SOC | IT Operations | Legal/DPO | Management |
|----------|------|------------------|-----|---------------|-----------|------------|
| Policy creation | R/A | C | C | C | C | I |
| Incident detection | A | C | R | C | I | I |
| Incident triage | A | R | R | C | I | I |
| Incident response | A | R | R | R | C | I |
| Escalation | A | R | C | I | C | I |
| Data breach notification | A | C | I | I | R | C |
| Forensics | A | C | R | C | C | I |
| Post-incident review | R/A | R | C | C | C | C |

**Legend:** R = Responsible (Execution), A = Accountable (Ownership), C = Consulted, I = Informed

### Key Roles

- **Policy Owner:** Thomas Weber (CISO)
- **Incident Manager:** {{ meta.security.incident_manager }}
- **SOC Manager:** {{ meta.security.soc_manager }}
- **Data Protection Officer:** {{ meta.dpo.name }}
- **Implementation Responsible:** SOC, IT Operations, Incident Response Team
- **Control/Audit Function:** ISMS, Internal Audit

## 5. Derivations (Guidelines/Standards/Processes)

Implementation details are defined in subordinate documents:

### Related Guidelines
- **0410_Guideline_Incident_Response_and_Major_Incident_Process.md** - Detailed implementation guideline
- `0320_Policy_Logging_and_Monitoring.md` - Logging and Monitoring Policy
- `0440_Policy_Business_Continuity_ICT_Readiness.md` - Business Continuity Policy
- `0560_Policy_Data_Protection_Interfaces.md` - Data Protection Policy

### Related Standards/Baselines
- Incident response playbooks
- Incident severity matrix
- Escalation paths
- Data breach notification process

### Related Processes
- Incident response process
- Major incident process
- Data breach notification process
- Post-incident review process

## 6. Compliance, Monitoring and Enforcement

### Metrics and KPIs
- Number of incidents per category and severity
- MTTD (Mean Time To Detect) - Average detection time
- MTTR (Mean Time To Respond) - Average response time
- MTTR (Mean Time To Resolve) - Average resolution time
- Number of data breaches and notifications
- Post-incident review completion rate (target: 100%)

### Evidence and Proof
- Incident tickets and documentation
- Incident response logs
- Forensics reports
- Data breach notifications
- Post-incident review reports
- Lessons learned documentation

### Consequences of Violations
Violations of this policy are handled according to applicable HR and compliance processes:
- **Unreported incident:** Retraining, warning
- **Delayed data breach notification:** Compliance investigation, possible fines
- **Evidence tampering:** Severe disciplinary action
- **Repeated violations:** Employment consequences

## 7. Exceptions

Exceptions to this policy are only permitted in justified cases:

- **Exception Process:** See `0640_Policy_Exceptions_and_Risk_Waivers.md`
- **Approval:** Exceptions must be approved by CISO
- **Documentation:** All exceptions are documented in the risk register
- **Time Limitation:** Exceptions are generally time-limited

## 8. References

### Internal Documents
- `0010_ISMS_Information_Security_Policy.md` - ISMS Policy
- `0410_Guideline_Incident_Response_and_Major_Incident_Process.md` - Detailed Guideline
- `0320_Policy_Logging_and_Monitoring.md` - Logging and Monitoring Policy
- `0080_ISMS_Risk_Register_Template.md` - Risk Register

### External Standards and Requirements
- **ISO/IEC 27001:2022 Annex A.5.24** - Information security incident management planning and preparation
- **ISO/IEC 27001:2022 Annex A.5.25** - Assessment and decision on information security events
- **ISO/IEC 27001:2022 Annex A.5.26** - Response to information security incidents
- **ISO/IEC 27001:2022 Annex A.5.27** - Learning from information security incidents
- **ISO/IEC 27001:2022 Annex A.5.28** - Collection of evidence
- **NIST SP 800-61** - Computer Security Incident Handling Guide
- **GDPR (EU 2016/679)** - Art. 33, 34 - Data Breach Notification
- **NIS2 Directive** - Network and Information Security Directive

---

**Approved by:**  
{{ meta.management.ceo }}, Management  
Date: {{ meta.document.approval_date }}

**Next Review:** {{ meta.document.next_review }} (annually or as needed)
