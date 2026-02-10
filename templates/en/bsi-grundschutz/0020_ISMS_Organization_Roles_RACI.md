# ISMS Organization, Roles and Responsibilities

**Document ID:** 0020  
**Document Type:** Foundation Document  
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
This template defines the ISMS organization structure, roles, and responsibilities according to BSI IT-Grundschutz.
Customize all [TODO] placeholders based on your organization's specific structure.
Reference: BSI Standard 200-1 (ISMS Organization Requirements)
-->

## 1. ISMS Organization

### 1.1 ISMS Owner/Sponsor

**Responsible:** {{ meta.ceo.name }} ({{ meta.ceo.email }})

The ISMS Owner bears overall responsibility for the Information Security Management System and ensures that:
- Sufficient resources are provided
- The information security policy is approved
- Strategic decisions on information security are made
- The ISMS is integrated into business processes

### 1.2 Information Security Officer (ISO)

**Responsible:** {{ meta.ciso.name }} ({{ meta.ciso.email }})

The ISO is the central coordination point for all information security activities:
- Coordination and management of the ISMS
- Advising executive management and departments
- Conducting risk analyses and security assessments
- Monitoring the implementation of security measures
- Reporting to executive management
- Coordination of security incidents
- Conducting awareness measures

### 1.3 ISMS Team / Information Security Committee

The ISMS Team supports the ISO in implementing the ISMS:

| Role | Name | Area of Responsibility |
|---|---|---|
| ISO (Lead) | {{ meta.ciso.name }} | Overall ISMS coordination |
| IT Management | {{ meta.cio.name }} | Technical security measures |
| Data Protection Officer | [TODO] | Data protection interface |
| BCM Manager | [TODO] | Business Continuity |
| Risk Manager | [TODO] | Risk management |
| HR Representative | [TODO] | Personnel and awareness topics |
| Legal/Compliance | [TODO] | Legal requirements |

**Meeting Frequency:** [TODO: e.g. monthly, quarterly]

### 1.4 Interfaces to Other Areas

#### 1.4.1 IT Service Management (ITSM)

**Contact:** {{ meta.cio.name }}

Interfaces:
- Change Management: Security assessment of changes
- Incident Management: Security incidents
- Problem Management: Security vulnerabilities
- Configuration Management: Asset inventory

#### 1.4.2 Data Protection

**Contact:** [TODO: Data Protection Officer]

Interfaces:
- Record of processing activities (ROPA)
- Data Protection Impact Assessment (DPIA)
- Technical and organizational measures (TOM)
- Reporting of data breaches

#### 1.4.3 Business Continuity Management (BCM)

**Contact:** [TODO: BCM Manager]

Interfaces:
- Business Impact Analysis (BIA)
- IT Disaster Recovery Plans
- Emergency exercises and tests
- Crisis management

#### 1.4.4 Risk Management

**Contact:** [TODO: Risk Manager]

Interfaces:
- Enterprise-wide risk management
- Risk register and assessment
- Risk reporting
- Risk acceptance decisions

#### 1.4.5 Internal Audit

**Contact:** [TODO: Internal Audit]

Interfaces:
- ISMS audits
- Compliance reviews
- Follow-up of audit findings
- Reporting to management

## 2. Roles and Responsibilities

### 2.1 Information Domain Manager

**Role:** Responsible for a specific information domain (e.g. business application, IT system)

**Tasks:**
- Definition of the information domain scope
- Conducting structure analysis
- Protection needs assessment
- Modeling and module assignment
- Coordination of measure implementation
- Monitoring the security of the information domain

[TODO: Designate specific information domain managers]

### 2.2 Asset Owner / System Owner

**Role:** Responsible for specific assets or IT systems

**Tasks:**
- Classification and assessment of assets
- Definition of security requirements
- Approval of access rights
- Monitoring asset usage
- Decision on decommissioning

[TODO: Define asset owners for critical systems]

### 2.3 Measure/Control Owner

**Role:** Responsible for implementing specific security measures

**Tasks:**
- Implementation of assigned security measures
- Documentation of implementation
- Evidence of effectiveness
- Continuous monitoring and improvement

[TODO: Assignment of measure owners]

### 2.4 Administrators / Operators

**Role:** Technical implementation and operation of IT systems

**Tasks:**
- Configuration and hardening of systems
- Patch and update management
- Monitoring and logging
- Backup and recovery
- Incident response (technical)

**Responsible:** {{ meta.cio.name }} (IT Management)

### 2.5 All Employees

**Role:** Users of IT systems and information

**Tasks:**
- Compliance with security guidelines
- Reporting security incidents
- Participation in training
- Responsible handling of information
- Protection of access credentials

## 3. RACI Matrix for BSI IT-Grundschutz Processes

<!-- 
RACI Legend:
R = Responsible (Implementation responsibility)
A = Accountable (Overall responsibility, decision authority)
C = Consulted (Consulted, subject matter expertise)
I = Informed (Informed)
-->

| Activity | Executive Management | ISO | IT Management | Information Domain Managers | Departments | Internal Audit |
|---|---|---|---|---|---|---|
| **Structure Analysis** | I | A | C | R | C | I |
| **Protection Needs Assessment** | A | C | C | R | C | I |
| **Modeling (Module Assignment)** | I | A | C | R | C | I |
| **Basic Security Check** | I | A | C | R | C | I |
| **Risk Analysis (BSI 200-3)** | A | R | C | C | C | I |
| **Measure Planning** | A | R | C | C | C | I |
| **Measure Implementation** | I | C | R | R | R | I |
| **Effectiveness Review** | I | A | C | R | C | I |
| **ISMS Audit** | I | C | C | C | C | R/A |
| **Management Review** | A | R | C | I | I | C |
| **Incident Management** | I | A | R | C | C | I |
| **Awareness Training** | I | A | C | C | R | I |
| **Documentation** | I | A | R | R | C | I |

## 4. Escalation Paths

### 4.1 Operational Escalation

1. **Level 1:** Information Domain Managers / System Owner
2. **Level 2:** ISO / IT Management
3. **Level 3:** Executive Management

### 4.2 Security Incidents

1. **Report:** All Employees → ISO / IT Management
2. **Assessment:** ISO / IT Management
3. **Escalation (for Major Incidents):** Executive Management
4. **External Reporting (if required):** BSI, Data Protection Authority, Law Enforcement

## 5. Communication and Reporting

### 5.1 Regular Reports

| Report | Frequency | Creator | Recipient |
|---|---|---|---|
| ISMS Status Report | Monthly | ISO | Executive Management, ISMS Team |
| Security Incidents | Monthly | ISO | Executive Management |
| Risk Dashboard | Quarterly | ISO | Executive Management |
| Management Review | Annually | ISO | Executive Management |
| Audit Results | After Audit | Internal Audit | Executive Management, ISO |

### 5.2 Ad-hoc Communication

- **Security Incidents:** Immediate report to ISO
- **Critical Vulnerabilities:** Immediate report to ISO and IT Management
- **Compliance Violations:** Report to ISO and Legal/Compliance

## 6. Resources and Budget

[TODO: Define budget and resources for ISMS activities]

- **ISMS Budget:** [TODO]
- **Personnel Resources:** [TODO]
- **External Support:** [TODO]
- **Tools and Systems:** [TODO]

## 7. Review and Update

This organizational structure is reviewed and updated at least annually or in case of significant changes.

**Next Review:** {{ meta.document.next_review }}

---

**References:**
- BSI Standard 200-1: Management Systems for Information Security (ISMS)
- BSI Standard 200-2: IT-Grundschutz Methodology
- BSI IT-Grundschutz Compendium

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial Creation |

<!-- End of template -->