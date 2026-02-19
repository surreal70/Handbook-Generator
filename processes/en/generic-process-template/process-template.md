<!--
=============================================================================
PROCESS DOCUMENTATION TEMPLATE
=============================================================================

This template is used for structured documentation of business processes
according to BPMN standards with RACI matrix and compliance requirements.

CONFIGURATION FILES:
- meta-process.yaml: Process-specific metadata (in this directory)
- meta-global-process.yaml: Global process configuration (in processes/en/ directory)
- meta-organisation.yaml: Organization data (in main directory)
- meta-organisation-roles.yaml: Roles and contacts (in main directory)
- meta-global.yaml: Generator information (in main directory)

PLACEHOLDER SYNTAX:
- {{ meta-process.* }} - Values from meta-process.yaml
- {{ meta-global-process.* }} - Values from meta-global-process.yaml
- {{ meta-organisation.* }} - Values from meta-organisation.yaml
- {{ role_* }} - Roles from meta-organisation-roles.yaml
- {{ escalation.* }} - Escalation paths from meta-global-process.yaml

USAGE:
1. Copy this template directory
2. Rename it according to your process (e.g., "change-management")
3. Adapt meta-process.yaml to your requirements
4. Fill in the placeholder sections with your content
5. Generate the documentation with: python -m src.cli --language en --process your-process-name

=============================================================================
-->

<!-- 
DOCUMENT HEADER
This section is automatically populated from meta-process.yaml.
Adjust the values in meta-process.yaml, not here in the template.
-->
# Process: {{ meta-process.name }}

**Document ID:** {{ meta-process.id }}  
**Organization:** {{ meta-organisation.name }}  
**Process Owner:** {{ meta-process.owner }}  
**Process Manager:** {{ meta-process.manager }}  
**Approved by:** {{ meta-process.approver }}  
**Revision:** {{ meta-process.revision }}  
**Author:** {{ meta-process.author }}  
**Status:** {{ meta-process.status }}  
**Classification:** {{ meta-process.classification }}  
**Last Updated:** {{ meta-process.modifydate }}  
**Template Version:** {{ meta-process.version }}

---

<!--
=============================================================================
SECTION 1: PURPOSE AND OBJECTIVES
=============================================================================
Describe the fundamental purpose and strategic objectives of the process here.
This helps stakeholders understand why the process exists and what value it delivers.
-->

## 1. Purpose and Objectives

### 1.1 Purpose

<!--
Describe the main purpose of the process:
- What problem does the process solve?
- What business value does it deliver?
- Who is the process relevant for?
-->
[Description of the process purpose]

### 1.2 Objectives

<!--
List measurable objectives that the process should achieve:
- Use SMART criteria (Specific, Measurable, Achievable, Relevant, Time-bound)
- Link objectives to KPIs (see Section 10)
-->
- Objective 1: [Description]
- Objective 2: [Description]
- Objective 3: [Description]

<!--
=============================================================================
SECTION 2: SCOPE
=============================================================================
Clearly define what is included in the process and what is not.
Category and criticality are loaded from meta-process.yaml.
-->

## 2. Scope

**Category:** {{ meta-process.category }}  
**Criticality:** {{ meta-process.criticality }}

<!--
Describe the scope:
- Which departments/teams are affected?
- Which systems/applications are used?
- Which geographic locations are included?
- What is NOT in scope (delimitation)?
-->
[Detailed description of the scope]

<!--
=============================================================================
SECTION 3: TRIGGERS AND INPUTS
=============================================================================
Define what starts the process and what information/resources are needed.
-->

## 3. Triggers and Inputs

### 3.1 Triggers

<!--
List all events that trigger the process:
- Time-based triggers (e.g., monthly, quarterly)
- Event-based triggers (e.g., incident reported, change request submitted)
- Manual triggers (e.g., on management request)
-->
- Trigger 1: [Description]
- Trigger 2: [Description]
- Trigger 3: [Description]

### 3.2 Inputs

<!--
List all required inputs:
- Documents (e.g., forms, requests)
- Data (e.g., from other systems)
- Resources (e.g., personnel, budget)
- Information (e.g., from stakeholders)
-->
- Input 1: [Description]
- Input 2: [Description]
- Input 3: [Description]

<!--
=============================================================================
SECTION 4: RESULTS AND OUTPUTS
=============================================================================
Define what the process produces and how success is measured.
-->

## 4. Results and Outputs

### 4.1 Outputs

<!--
List all results of the process:
- Documents (e.g., reports, approvals)
- Data (e.g., updated records)
- Decisions (e.g., approvals, rejections)
- Actions (e.g., implemented changes)
-->
- Output 1: [Description]
- Output 2: [Description]
- Output 3: [Description]

### 4.2 Success Criteria

<!--
Define measurable success criteria:
- Quality criteria (e.g., error rate < 5%)
- Time criteria (e.g., cycle time < 24h)
- Satisfaction criteria (e.g., customer satisfaction > 90%)
-->
[Description of success criteria]

<!--
=============================================================================
SECTION 5: ROLES AND RESPONSIBILITIES (RACI)
=============================================================================
The RACI matrix is loaded from meta-process.yaml and shows who is responsible
for which activity. Adjust the RACI entries in meta-process.yaml.

RACI RULES:
- Each activity must have exactly ONE person/role as "Accountable"
- Multiple people can be "Responsible"
- "Consulted" and "Informed" are optional
- Avoid too many "Consulted" (slows down the process)
-->

## 5. Roles and Responsibilities (RACI)

### 5.1 RACI Matrix

<!--
This table is automatically populated from meta-process.yaml.
Add more rows for additional process steps.
Role references (role_*) are resolved from meta-organisation-roles.yaml.
-->
| Activity | Responsible | Accountable | Consulted | Informed |
|----------|-------------|-------------|-----------|----------|
| Incident Detection | {{ meta-process.raci.incident_detection.responsible }} | {{ meta-process.raci.incident_detection.accountable }} | {{ meta-process.raci.incident_detection.consulted }} | {{ meta-process.raci.incident_detection.informed }} |
| Incident Analysis | {{ meta-process.raci.incident_analysis.responsible }} | {{ meta-process.raci.incident_analysis.accountable }} | {{ meta-process.raci.incident_analysis.consulted }} | {{ meta-process.raci.incident_analysis.informed }} |
| Incident Resolution | {{ meta-process.raci.incident_resolution.responsible }} | {{ meta-process.raci.incident_resolution.accountable }} | {{ meta-process.raci.incident_resolution.consulted }} | {{ meta-process.raci.incident_resolution.informed }} |

**Legend:**
- **R = Responsible (Execution):** Performs the activity
- **A = Accountable (Responsible):** Has overall responsibility
- **C = Consulted (Consulted):** Is consulted before decisions
- **I = Informed (Informed):** Is informed about results

<!--
=============================================================================
SECTION 6: PROCESS FLOW DIAGRAM (BPMN)
=============================================================================
Insert your BPMN diagram here. Save the diagram file in the "diagrams/" subdirectory.

BPMN TOOLS:
- Camunda Modeler (free, recommended)
- draw.io / diagrams.net (free)
- Lucidchart (commercial)
- Microsoft Visio (commercial)

EXPORT FORMATS:
- .bpmn (XML format, editable)
- .png or .svg (for display in documentation)
-->

## 6. Process Flow Diagram (BPMN)

<!--
Replace "process-flow.bpmn" with the name of your diagram file.
If using an image, change the file extension (e.g., .png, .svg).
-->
![Process Flow](diagrams/process-flow.bpmn)

### 6.1 Process Steps

<!--
Describe each step in the process in detail:
- What is done?
- Who does it? (Reference to RACI matrix)
- Which systems are used?
- What decisions are made?
- What are the outputs?
-->
1. **Step 1:** [Detailed description of the first step]
2. **Step 2:** [Detailed description of the second step]
3. **Step 3:** [Detailed description of the third step]
4. **Step 4:** [Detailed description of the fourth step]
5. **Step 5:** [Detailed description of the fifth step]

<!--
=============================================================================
SECTION 7: SYSTEMS AND TOOLS
=============================================================================
List all IT systems and tools used in the process.
The system list can be loaded from meta-process.yaml.
-->

## 7. Systems and Tools

### 7.1 Systems Used

<!--
Adapt this list to your environment or use the placeholder {{ meta-process.systems }}
to load the list from meta-process.yaml. For each system, you should specify:
- Name and version
- Purpose in the process
- Access permissions
- Support contact
-->
- ServiceNow
- Zabbix
- Slack

[Or dynamically from meta-process.yaml: {{ meta-process.systems }}]

### 7.2 Interfaces

<!--
Describe interfaces to other systems:
- API integrations
- Data imports/exports
- Automations
- Notifications
-->
[Description of interfaces to other systems]

<!--
=============================================================================
SECTION 8: ARTIFACTS
=============================================================================
Document all artifacts created or used during the process.
-->

## 8. Artifacts

### 8.1 Tickets

<!--
Describe ticket types and their workflows:
- Which ticket types are used?
- Which fields are mandatory/optional?
- What status transitions exist?
- Who can create/edit tickets?
-->
[Description of ticket types and workflows]

### 8.2 Logs

<!--
Define logging requirements:
- What must be logged?
- Where are logs stored?
- How long are logs retained?
- Who has access to logs?
- Compliance requirements (e.g., GDPR, audit trail)
-->
[Description of logging requirements]

### 8.3 Reports

<!--
List all reports:
- Report name and purpose
- Frequency (daily, weekly, monthly)
- Recipients
- Data sources
-->
[Description of report types]

<!--
=============================================================================
SECTION 9: SLAs AND OLAs
=============================================================================
SLA values are loaded from meta-process.yaml.
Adjust the values there to match your requirements.

SLA vs. OLA:
- SLA (Service Level Agreement): Agreement with customers/end users
- OLA (Operational Level Agreement): Internal agreement between teams
-->

## 9. SLAs and OLAs

### 9.1 Service Level Agreements

<!--
These values are loaded from meta-process.yaml.
Define SLAs for different priority levels:
- P1: Critical (business operations impacted)
- P2: High (important functions impacted)
- P3: Medium (limited functionality)
- P4: Low (cosmetic issues)
-->
- **P1 Resolution:** {{ meta-process.sla.p1_resolution }}
- **P2 Resolution:** {{ meta-process.sla.p2_resolution }}
- **P3 Resolution:** {{ meta-process.sla.p3_resolution }}

### 9.2 Operational Level Agreements

<!--
Describe internal OLAs:
- Between which teams?
- What services are committed?
- What response times apply?
- How is compliance measured?
-->
[Description of OLA details]

<!--
=============================================================================
SECTION 10: KPIs AND METRICS
=============================================================================
KPI definitions are loaded from meta-process.yaml.
Define measurable metrics for process monitoring.
-->

## 10. KPIs and Metrics

### 10.1 Key Performance Indicators

<!--
These KPIs are loaded from meta-process.yaml.
Adapt the KPIs to your process objectives (see Section 1.2).

EXAMPLE KPIs:
- Efficiency: Cycle time, processing time, automation rate
- Quality: Error rate, rework rate, customer satisfaction
- Compliance: Audit findings, SLA compliance, documentation completeness
-->
- **MTTR:** {{ meta-process.kpis.mttr }}
- **MTBF:** {{ meta-process.kpis.mtbf }}
- **First Call Resolution:** {{ meta-process.kpis.first_call_resolution }}

### 10.2 Measurement and Reporting

<!--
Describe how KPIs are measured and reported:
- Data sources (from which systems?)
- Measurement frequency (daily, weekly, monthly?)
- Reporting format (dashboard, report, meeting?)
- Responsibilities (who collects/analyzes/reports?)
- Target values and thresholds
-->
[Description of measurement procedures and reporting mechanisms]

<!--
=============================================================================
SECTION 11: CONTROL POINTS
=============================================================================
Define control mechanisms for quality assurance and compliance.
Standard control points are loaded from meta-global-process.yaml.
-->

## 11. Control Points

### 11.1 Review Steps

<!--
These standard control points are loaded from meta-global-process.yaml.
Add process-specific control points:
- At which points in the process?
- Who performs the control?
- What is checked?
- How is the result documented?
-->
- Management approval
- Four-eyes principle
- Audit trail

[From meta-global-process.yaml]

### 11.2 Audit Requirements

<!--
Describe audit requirements:
- Which compliance frameworks apply? (see Section 12.1)
- What evidence must be available?
- How often do audits take place?
- Who conducts audits (internal/external)?
- How are audit findings handled?
-->
[Description of audit details]

<!--
=============================================================================
SECTION 12: RISKS AND COMPLIANCE
=============================================================================
Compliance frameworks and SoD rules are loaded from meta-process.yaml.
Document risks and their treatment.
-->

## 12. Risks and Compliance

### 12.1 Compliance Frameworks

<!--
This list is loaded from meta-process.yaml.
Add all relevant compliance frameworks:
- ISO 27001 (Information Security)
- BSI IT-Grundschutz (IT Security)
- GDPR (Data Protection)
- SOX (Financial Reporting)
- HIPAA (Health Data)
- PCI DSS (Payment Card Data)

Specify the relevant clauses/controls for each framework.
-->
- ISO 27001:2022 - Clause 5.24
- BSI IT-Grundschutz - DER.2.1

[From meta-process.yaml: {{ meta-process.compliance.frameworks }}]

### 12.2 Segregation of Duties (SoD)

<!--
SoD rules are loaded from meta-process.yaml.
Segregation of Duties prevents conflicts of interest and fraud.

EXAMPLES OF SOD RULES:
- Who requests changes cannot approve them
- Who develops code cannot deploy it to production
- Who initiates payments cannot approve them
- Who creates logs cannot delete/modify them
-->
- Incident handler cannot approve own escalations
- Security analyst cannot modify audit logs

[From meta-process.yaml: {{ meta-process.compliance.sod_rules }}]

### 12.3 Risks

<!--
Conduct a risk analysis and document:
- Risk description (what can go wrong?)
- Probability (High/Medium/Low or 1-5)
- Impact (High/Medium/Low or 1-5)
- Risk score (Probability × Impact)
- Mitigation (how is the risk reduced?)
- Responsible (who monitors the risk?)
-->
| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| [Risk 1] | [High/Medium/Low] | [High/Medium/Low] | [Measure] |
| [Risk 2] | [High/Medium/Low] | [High/Medium/Low] | [Measure] |
| [Risk 3] | [High/Medium/Low] | [High/Medium/Low] | [Measure] |

<!--
=============================================================================
SECTION 13: ESCALATIONS AND EXCEPTIONS
=============================================================================
Escalation paths are loaded from meta-global-process.yaml.
Role references are resolved from meta-organisation-roles.yaml.
-->

## 13. Escalations and Exceptions

### 13.1 Escalation Path

<!--
This table is automatically populated from meta-global-process.yaml.
Escalation paths are defined globally for all processes.
Adjust the values in meta-global-process.yaml if needed.

ESCALATION CRITERIA:
- Level 1: First point of contact, normal processing
- Level 2: For delays or complex problems
- Level 3: For critical problems or management decisions
- Level 4: For business-critical escalations or crises
-->
| Level | Role | Contact |
|-------|------|---------|
| 1 | {{ escalation.level_1 }} | {{ escalation.level_1_email }} |
| 2 | {{ escalation.level_2 }} | {{ escalation.level_2_email }} |
| 3 | {{ escalation.level_3 }} | {{ escalation.level_3_email }} |
| 4 | {{ escalation.level_4 }} | {{ escalation.level_4_email }} |

### 13.2 Exceptions

<!--
Describe the process for exceptions:
- When is an exception justified?
- Who can approve exceptions?
- How are exceptions documented?
- How long are exceptions valid?
- How are exceptions monitored?

EXAMPLES OF EXCEPTIONS:
- Emergency changes without change ticket
- Deviation from standard procedures
- Temporary bypass of controls
-->
[Description of exception process]

<!--
=============================================================================
SECTION 14: APPENDICES
=============================================================================
Link to additional documents and resources here.
-->

## 14. Appendices

### 14.1 Checklists

<!--
Link to checklists for recurring tasks:
- Pre-flight checklists
- Quality assurance checklists
- Acceptance checklists
- Audit checklists

Store checklists in the same directory or in a "checklists/" subdirectory.
-->
[Links to relevant checklists]

### 14.2 Runbooks

<!--
Link to detailed runbooks/playbooks:
- Step-by-step instructions
- Troubleshooting guides
- Emergency procedures
- Recovery procedures

Store runbooks in the same directory or in a "runbooks/" subdirectory.
-->
[Links to relevant runbooks]

### 14.3 Forms

<!--
Link to forms and templates:
- Request forms
- Approval forms
- Documentation templates
- Report templates

Store forms in the same directory or in a "forms/" subdirectory.
-->
[Links to relevant forms]

---

<!--
=============================================================================
DOCUMENT HISTORY
=============================================================================
Maintain the version history of the process.
Add a new row for each change.
-->

## Document History

<!-- 
INSTRUCTIONS: Document History
- Maintain the version history
- Document significant changes
- Add new rows for each version
-->

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 19.02.2026 | Handbook Generator | Initial version |
| [TODO] | [TODO] | [TODO] | [TODO] |
| [TODO] | [TODO] | [TODO] | [TODO] |

---
