# NIST CSF 2.0 Framework Mapping

**Document-ID:** [FRAMEWORK]-9999
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Approved by:** {{ meta-handbook.approver }}
**Revision:** [TODO]
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Classification:** {{ meta-handbook.classification }}
**Last Update:** {{ meta-handbook.modifydate }}
**Template Version:** [TODO]

---

---

## Overview

This document maps the handbook templates to NIST Cybersecurity Framework 2.0 categories and subcategories.

## 1. Govern (GV)

### GV.OC: Organizational Context
**Templates:**
- 0020_organizational_context.md

**Subcategories:**
- GV.OC-01: Organizational context is understood
- GV.OC-02: Legal, regulatory, and contractual requirements are understood
- GV.OC-03: Critical objectives, stakeholders, and activities are understood
- GV.OC-04: Dependencies and critical functions are understood
- GV.OC-05: Organizational resilience objectives are established

### GV.RM: Risk Management Strategy
**Templates:**
- 0030_risk_management_strategy.md

**Subcategories:**
- GV.RM-01: Risk management objectives are established
- GV.RM-02: Risk appetite and risk tolerance are established
- GV.RM-03: Risk management roles and responsibilities are established
- GV.RM-04: Strategic direction informs risk management
- GV.RM-05: Cybersecurity risks are integrated into business decisions
- GV.RM-06: Risk management strategy is communicated
- GV.RM-07: Risk management strategy is regularly reviewed

### GV.RR: Roles, Responsibilities, and Authorities
**Templates:**
- 0040_roles_responsibilities.md

**Subcategories:**
- GV.RR-01: Cybersecurity roles and responsibilities are established
- GV.RR-02: Cybersecurity responsibilities are assigned
- GV.RR-03: Adequate resources are allocated
- GV.RR-04: Cybersecurity responsibilities are integrated into job descriptions

### GV.PO: Policy
**Templates:**
- 0050_policy_framework.md

**Subcategories:**
- GV.PO-01: Cybersecurity policies are established
- GV.PO-02: Policies are communicated
- GV.PO-03: Policies are enforced
- GV.PO-04: Policies are regularly reviewed and updated

### GV.OV: Oversight
**Templates:**
- 0060_oversight.md

**Subcategories:**
- GV.OV-01: Cybersecurity oversight is established
- GV.OV-02: Cybersecurity strategy is monitored
- GV.OV-03: Cybersecurity performance is measured
- GV.OV-04: Cybersecurity risks are reported to leadership

### GV.SC: Supply Chain Risk Management
**Templates:**
- 0070_supply_chain_risk_management.md

**Subcategories:**
- GV.SC-01: Supply chain cybersecurity risks are identified
- GV.SC-02: Suppliers are assessed
- GV.SC-03: Contracts include cybersecurity requirements
- GV.SC-04: Suppliers are monitored
- GV.SC-05: Supplier incidents are managed

## 2. Identify (ID)

### ID.AM: Asset Management
**Templates:**
- 0100_asset_management.md

**Subcategories:**
- ID.AM-01: Physical devices and systems are inventoried
- ID.AM-02: Software platforms and applications are inventoried
- ID.AM-03: Organizational communication and data flows are mapped
- ID.AM-04: External information systems are catalogued
- ID.AM-05: Resources are prioritized based on criticality
- ID.AM-07: Roles and responsibilities for assets are assigned
- ID.AM-08: Systems, hardware, and software are managed by lifecycle

### ID.BE: Business Environment
**Templates:**
- 0110_business_environment.md

**Subcategories:**
- ID.BE-01: Organization's role in the supply chain is identified
- ID.BE-02: Organization's place in critical infrastructure sector is identified
- ID.BE-03: Priorities for organizational mission are established
- ID.BE-04: Dependencies and critical functions are established
- ID.BE-05: Resilience requirements are established

### ID.GV: Governance
**Templates:**
- 0120_governance.md

**Subcategories:**
- ID.GV-01: Cybersecurity policies are established
- ID.GV-02: Cybersecurity roles are assigned
- ID.GV-03: Legal and regulatory requirements are understood
- ID.GV-04: Governance and risk management are integrated

### ID.RA: Risk Assessment
**Templates:**
- 0130_risk_assessment.md

**Subcategories:**
- ID.RA-01: Asset vulnerabilities are identified
- ID.RA-02: Cyber threat intelligence is received
- ID.RA-03: Threats are identified
- ID.RA-04: Potential business impacts are identified
- ID.RA-05: Threats, vulnerabilities, and impacts are used to determine risk
- ID.RA-06: Risk responses are identified and prioritized
- ID.RA-07: Risk assessments are performed
- ID.RA-08: Risk assessments are updated
- ID.RA-09: Risk assessments are communicated
- ID.RA-10: Critical cybersecurity risks are escalated

### ID.RM: Risk Management Strategy
**Templates:**
- 0140_risk_management_strategy.md

**Subcategories:**
- ID.RM-01: Risk management processes are established
- ID.RM-02: Risk tolerance is determined
- ID.RM-03: Risk tolerance is communicated

### ID.SC: Supply Chain Risk Management
**Templates:**
- 0150_supply_chain_risk_management.md

**Subcategories:**
- ID.SC-01: Supply chain partners are identified
- ID.SC-02: Supply chain contracts are established
- ID.SC-03: Suppliers are assessed
- ID.SC-04: Suppliers are monitored
- ID.SC-05: Supplier response plans are established

## 3. Protect (PR)

### PR.AA: Identity Management and Access Control
**Templates:**
- 0200_identity_access_control.md

**Subcategories:**
- PR.AA-01: Identities and credentials are managed for authorized devices
- PR.AA-02: Identities and credentials are managed for authorized users
- PR.AA-03: Identities are verified
- PR.AA-04: Identity and access management is enforced
- PR.AA-05: Physical access is managed
- PR.AA-06: Identities are correlated with credentials

### PR.AT: Awareness and Training
**Templates:**
- 0210_awareness_training.md

**Subcategories:**
- PR.AT-01: All users are trained in cybersecurity awareness
- PR.AT-02: Privileged users understand their roles
- PR.AT-03: Third-party stakeholders understand their roles
- PR.AT-04: Senior executives understand their roles
- PR.AT-05: Physical and cybersecurity personnel understand their roles

### PR.DS: Data Security
**Templates:**
- 0220_data_security.md

**Subcategories:**
- PR.DS-01: Data at rest is protected
- PR.DS-02: Data in transit is protected
- PR.DS-03: Assets are formally managed
- PR.DS-04: Adequate capacity is maintained
- PR.DS-05: Protection against data leaks is implemented
- PR.DS-06: Integrity checking mechanisms are used
- PR.DS-07: Development and testing environments are separated
- PR.DS-08: Integrity checks are performed
- PR.DS-10: Confidentiality, integrity, and availability are enforced
- PR.DS-11: Data is managed according to retention requirements

### PR.IP: Information Protection Processes
**Templates:**
- 0230_information_protection_processes.md

**Subcategories:**
- PR.IP-01: Baseline configurations are created
- PR.IP-02: System development lifecycle is managed
- PR.IP-03: Configuration change control is implemented
- PR.IP-04: Backups are performed
- PR.IP-05: Policies for physical operating environment are met
- PR.IP-06: Data is securely disposed
- PR.IP-07: Protection processes are continuously improved
- PR.IP-08: Effectiveness of protection technologies is shared
- PR.IP-09: Response plans are managed
- PR.IP-10: Response plans are tested
- PR.IP-11: Cybersecurity is integrated into HR practices
- PR.IP-12: Vulnerability management plan is developed

### PR.MA: Maintenance
**Templates:**
- 0240_maintenance.md

**Subcategories:**
- PR.MA-01: Maintenance is performed
- PR.MA-02: Remote maintenance is approved and logged

### PR.PT: Protective Technology
**Templates:**
- 0250_protective_technology.md

**Subcategories:**
- PR.PT-01: Audit/log records are determined
- PR.PT-02: Removable media is protected
- PR.PT-03: Least functionality is configured
- PR.PT-04: Communications and control networks are protected
- PR.PT-05: Mechanisms are implemented to achieve resilience

## 4. Detect (DE)

### DE.AE: Anomalies and Events
**Templates:**
- 0300_anomalies_events.md

**Subcategories:**
- DE.AE-01: Network baseline is established
- DE.AE-02: Detected events are analyzed
- DE.AE-03: Event data is aggregated
- DE.AE-04: Impact of events is determined
- DE.AE-06: Information about threats is received
- DE.AE-07: Threat data is used
- DE.AE-08: Incident thresholds are established

### DE.CM: Security Continuous Monitoring
**Templates:**
- 0310_security_monitoring.md

**Subcategories:**
- DE.CM-01: Network is monitored
- DE.CM-02: Physical environment is monitored
- DE.CM-03: Personnel activity is monitored
- DE.CM-04: Malicious code is detected
- DE.CM-06: External service provider activity is monitored
- DE.CM-07: Unauthorized activity is monitored
- DE.CM-09: Vulnerabilities are identified

### DE.DP: Detection Processes
**Templates:**
- 0320_detection_processes.md

**Subcategories:**
- DE.DP-01: Roles and responsibilities for detection are defined
- DE.DP-02: Detection activities comply with requirements
- DE.DP-03: Detection processes are tested
- DE.DP-04: Event detection information is communicated
- DE.DP-05: Detection processes are continuously improved

## 5. Respond (RS)

### RS.RP: Response Planning
**Templates:**
- 0400_response_planning.md

**Subcategories:**
- RS.RP-01: Response plan is executed

### RS.CO: Communications
**Templates:**
- 0410_communications.md

**Subcategories:**
- RS.CO-01: Personnel know their roles
- RS.CO-02: Incidents are reported
- RS.CO-03: Information is shared
- RS.CO-04: Coordination with stakeholders occurs
- RS.CO-05: Voluntary information sharing occurs

### RS.AN: Analysis
**Templates:**
- 0420_analysis.md

**Subcategories:**
- RS.AN-01: Notifications are investigated
- RS.AN-02: Impact of incidents is understood
- RS.AN-03: Forensics are performed
- RS.AN-04: Incidents are categorized
- RS.AN-05: Processes are established

### RS.MI: Mitigation
**Templates:**
- 0430_mitigation.md

**Subcategories:**
- RS.MI-01: Incidents are contained
- RS.MI-02: Incidents are eradicated
- RS.MI-03: Newly identified vulnerabilities are mitigated

### RS.IM: Improvements
**Templates:**
- 0440_improvements.md

**Subcategories:**
- RS.IM-01: Response plans incorporate lessons learned
- RS.IM-02: Response strategies are updated

## 6. Recover (RC)

### RC.RP: Recovery Planning
**Templates:**
- 0500_recovery_planning.md

**Subcategories:**
- RC.RP-01: Recovery plan is executed

### RC.IM: Improvements
**Templates:**
- 0510_improvements.md

**Subcategories:**
- RC.IM-01: Recovery plans incorporate lessons learned
- RC.IM-02: Recovery strategies are updated

### RC.CO: Communications
**Templates:**
- 0520_communications.md

**Subcategories:**
- RC.CO-01: Public relations are managed
- RC.CO-02: Reputation is repaired
- RC.CO-03: Recovery activities are communicated

## 7. Implementation and Assessment

### Implementation Tiers
**Templates:**
- 0600_implementation_tiers.md

**Description:**
Assessment of organizational cybersecurity maturity across four tiers (Partial, Risk Informed, Repeatable, Adaptive).

### Profiles
**Templates:**
- 0610_current_profile.md - Current state
- 0620_target_profile.md - Target state
- 0630_gap_analysis.md - Gap analysis
- 0640_action_plan.md - Action plan

**Description:**
Profiles enable assessment of current cybersecurity posture and planning for improvements.

## Coverage

These templates cover all core functions and categories of NIST CSF 2.0. Organizations should adapt the templates to their specific requirements and risk profiles.

