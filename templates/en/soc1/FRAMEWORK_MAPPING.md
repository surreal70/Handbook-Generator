# SOC 1 / SSAE 18 Framework Mapping

## Overview

This document maps the SOC 1 handbook templates to the COSO Internal Control Framework components and SOC 1 reporting requirements.

## COSO Framework Components

### 1. Control Environment

The control environment forms the foundation for all other components of internal control.

**COSO Principles**:
1. Integrity and ethical values
2. Board oversight
3. Organizational structure and authority
4. Competence
5. Accountability

**Mapped Templates**:
- 0100_control_environment.md → All principles
- 0110_integrity_and_ethical_values.md → Principle 1
- 0120_board_oversight.md → Principle 2

### 2. Risk Assessment

Identification and analysis of risks that could prevent achievement of control objectives.

**COSO Principles**:
6. Specification of objectives
7. Identification and analysis of risks
8. Assessment of fraud risks
9. Identification and analysis of significant changes

**Mapped Templates**:
- 0200_risk_assessment.md → Principles 6, 7, 9
- 0210_fraud_risk_assessment.md → Principle 8

### 3. Control Activities

Policies and procedures that help ensure management directives are carried out.

**COSO Principles**:
10. Selection and development of control activities
11. Selection and development of general controls over technology
12. Deployment through policies and procedures

**Mapped Templates**:
- 0300_control_activities.md → Principles 10, 12
- 0310_it_general_controls.md → Principle 11

### 4. Information and Communication

Capture and communication of relevant information to support internal control.

**COSO Principles**:
13. Use of relevant information
14. Internal communication
15. External communication

**Mapped Templates**:
- 0400_information_and_communication.md → Principles 13, 14, 15

### 5. Monitoring Activities

Ongoing and separate evaluations to determine whether components of internal control are present and functioning.

**COSO Principles**:
16. Conduct of ongoing and/or separate evaluations
17. Evaluation and communication of deficiencies

**Mapped Templates**:
- 0410_monitoring_activities.md → Principles 16, 17

## SOC 1 Report Elements

### Management Assertion

**Description**: Management's statement about the fairness of the system description and the design and operating effectiveness of controls.

**Mapped Templates**:
- 0010_soc1_framework_overview.md
- 0020_service_organization_description.md

### System Description

**Description**: Description of the service organization's system, including infrastructure, software, people, procedures, and data.

**Mapped Templates**:
- 0020_service_organization_description.md
- 0030_system_description.md

### Control Objectives

**Description**: Objectives to be achieved by the service organization's controls.

**Mapped Templates**:
- 0040_control_objectives.md

### Related Controls

**Description**: Controls designed to achieve the control objectives.

**Mapped Templates**:
- 0100-0199: Control Environment controls
- 0200-0299: Risk Assessment controls
- 0300-0399: Control Activities controls
- 0400-0499: Information and Communication controls

### Complementary User Entity Controls (CUECs)

**Description**: Controls that must be present at user organizations to achieve control objectives.

**Mapped Templates**:
- 0050_complementary_user_entity_controls.md

### Tests of Controls and Results

**Description**: Description of tests performed by the service auditor and their results (Type II).

**Note**: These are created by the service auditor, not the service organization.

## Control Objectives to Templates Mapping

### Control Objective: Access Control

**COSO Component**: Control Activities

**Relevant Templates**:
- 0300_control_activities.md (IT General Controls section)
- 0310_it_general_controls.md (Access Controls section)

**Control Activities**:
- User authentication
- User authorization
- Privileged access management
- Access reviews

### Control Objective: Change Management

**COSO Component**: Control Activities

**Relevant Templates**:
- 0310_it_general_controls.md (Change Management section)

**Control Activities**:
- Change request process
- Impact assessment
- Testing
- Approval
- Implementation

### Control Objective: Backup and Recovery

**COSO Component**: Control Activities

**Relevant Templates**:
- 0310_it_general_controls.md (Backup and Recovery section)

**Control Activities**:
- Backup procedures
- Recovery testing
- Retention

### Control Objective: Transaction Processing

**COSO Component**: Control Activities

**Relevant Templates**:
- 0300_control_activities.md (Transaction Processing Controls section)

**Control Activities**:
- Input controls (completeness, accuracy, validity)
- Processing controls (calculations, logic, error handling)
- Output controls (completeness, accuracy, distribution)

### Control Objective: Segregation of Duties

**COSO Component**: Control Activities

**Relevant Templates**:
- 0300_control_activities.md (Segregation of Duties section)

**Control Activities**:
- Critical segregations
- Compensating controls
- Conflict monitoring

### Control Objective: Monitoring of Control Effectiveness

**COSO Component**: Monitoring Activities

**Relevant Templates**:
- 0410_monitoring_activities.md

**Control Activities**:
- Ongoing monitoring
- Internal audits
- Deficiency remediation

## Compliance Mapping

### SSAE 18 Requirements

| SSAE 18 Requirement | Mapped Templates |
|---------------------|------------------|
| AT-C 320.09 - System Description | 0020, 0030 |
| AT-C 320.10 - Control Objectives | 0040 |
| AT-C 320.11 - Related Controls | 0100-0499 |
| AT-C 320.12 - Complementary User Entity Controls | 0050 |
| AT-C 320.13 - Management Assertion | 0010 |

### COSO 2013 Framework

| COSO Component | COSO Principles | Mapped Templates |
|----------------|-----------------|------------------|
| Control Environment | 1-5 | 0100-0199 |
| Risk Assessment | 6-9 | 0200-0299 |
| Control Activities | 10-12 | 0300-0399 |
| Information and Communication | 13-15 | 0400 |
| Monitoring Activities | 16-17 | 0410 |

## Gap Analysis

### Complete Coverage

The templates cover all five COSO components and all 17 COSO principles.

### Customization Needed

Organizations must customize the templates for:
- Specific control objectives based on their services
- Organization-specific controls
- Industry-specific requirements
- Subservice organizations

### Additional Documentation

In addition to these templates, you will need:
- Control evidence
- Test documentation (for Type II)
- Incident reports
- Change logs
- Audit reports

## References

- SSAE 18 (AT-C Section 320)
- COSO Internal Control - Integrated Framework (2013)
- SOC 1 Reporting Guide (AICPA)
- Service Organization Control Reports (AICPA)

---

**Note**: This mapping serves as a guide. Work with your service auditor to ensure all requirements are met.
