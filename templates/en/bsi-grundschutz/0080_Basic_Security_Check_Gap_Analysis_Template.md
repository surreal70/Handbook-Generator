# Basic Security Check / Gap Analysis (Template)

**Document-ID:** [FRAMEWORK]-0080
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

<!-- 
TEMPLATE AUTHOR NOTE:
This template guides the basis security check (gap analysis) according to BSI IT-Grundschutz Standard 200-2.
Compare target state (IT-Grundschutz requirements) with actual state (current implementation).
Reference: BSI Standard 200-2 (Chapter 8: Basis Security Check)
-->

## 1. Objective and Purpose

The basic security check systematically assesses the extent to which the IT-Grundschutz requirements modeled for the information domain of **{{ meta-organisation.name }}** have been implemented. It forms the basis for:
- Identification of security gaps
- Prioritization of measures
- Measure planning (Document 0100)
- Compliance evidence

**Responsible:** {{ meta-organisation-roles.role_CISO }} (ISB)

## 2. Approach and Methodology

### 2.1 Data Sources

The following sources are used for the basic security check:

| Data Source | Type | Responsible | Usage |
|---|---|---|---|
| Interviews with stakeholders | Primary source | {{ meta-organisation-roles.role_CISO }} | Process and organizational requirements |
| Configuration evidence | Technical | {{ meta-organisation-roles.role_CIO }} | Technical requirements |
| Policies and guidelines | Document | {{ meta-organisation-roles.role_CISO }} | Organizational requirements |
| Tickets and change records | System | {{ meta-organisation-roles.role_CIO }} | Implementation evidence |
| Logs and monitoring data | System | {{ meta-organisation-roles.role_CIO }} | Operational requirements |
| Audit reports | Document | [TODO: Internal Audit] | External validation |

### 2.2 Assessment Logic

**Fulfillment Levels:**

| Status | Abbreviation | Description | Criteria |
|---|---|---|---|
| **Fulfilled** | F | Requirement fully implemented | All aspects of the requirement are implemented and evidenced |
| **Partially Fulfilled** | P | Requirement partially implemented | Essential aspects implemented, but gaps exist |
| **Not Fulfilled** | N | Requirement not implemented | Requirement not or only minimally implemented |
| **Not Applicable** | N/A | Requirement not relevant | Requirement does not apply to organization |
| **Not Assessed** | - | Not yet reviewed | Assessment pending |

### 2.3 Sample Size

**Review Depth:**
- **Critical Requirements (Protection Need "Very High"):** 100% review
- **Important Requirements (Protection Need "High"):** 50% sample
- **Standard Requirements (Protection Need "Normal"):** 25% sample

**Review Methods:**
- Document review
- Configuration review
- Interviews
- Technical tests (samples)

### 2.4 Execution

**Timeline:**
- **Start:** [TODO]
- **Data Collection:** [TODO: e.g., 4 weeks]
- **Assessment:** [TODO: e.g., 2 weeks]
- **Validation:** [TODO: e.g., 1 week]
- **Completion:** [TODO]

**Participants:**
- ISB: {{ meta-organisation-roles.role_CISO }}
- IT Management: {{ meta-organisation-roles.role_CIO }}
- Information Domain Responsible: [TODO]
- Departments: [TODO]

## 3. Basic Security Check: Results

### 3.1 ISMS and Organization (ISMS, ORP)

<!-- 
TEMPLATE AUTHOR NOTE:
Check all requirements from assigned modules in document 0070.
Reference the specific module requirements from IT-Grundschutz-Kompendium.
-->

| Module | Requirement (Short) | Object | Status | Evidence | Finding | Measure | Owner | Target Date |
|---|---|---|---|---|---|---|---|---|
| ISMS.1 | Security policy created | {{ meta-organisation.name }} | F | Document 0010 | - | - | {{ meta-organisation-roles.role_CISO }} | - |
| ISMS.1 | ISMS organization defined | {{ meta-organisation.name }} | F | Document 0020 | - | - | {{ meta-organisation-roles.role_CISO }} | - |
| ISMS.1 | Resources provided | {{ meta-organisation.name }} | P | Budget evidence | Budget insufficient | Increase budget | {{ meta-organisation-roles.role_CEO }} | [TODO] |
| ORP.1 | Roles and responsibilities defined | {{ meta-organisation.name }} | F | Document 0020 | - | - | {{ meta-organisation-roles.role_CISO }} | - |
| ORP.2 | Onboarding of new employees | {{ meta-organisation.name }} | P | HR process | No security training in onboarding | Integrate security training | [TODO: HR] | [TODO] |
| ORP.3 | Awareness program | {{ meta-organisation.name }} | N | - | No awareness program exists | Establish awareness program | {{ meta-organisation-roles.role_CISO }} | [TODO] |
| ORP.4 | IAM process | {{ meta-organisation.name }} | P | IAM guideline | Recertification missing | Implement recertification process | {{ meta-organisation-roles.role_CIO }} | [TODO] |

### 3.2 Conception and Approaches (CON)

| Module | Requirement (Short) | Object | Status | Evidence | Finding | Measure | Owner | Target Date |
|---|---|---|---|---|---|---|---|---|
| CON.1 | Crypto concept created | Crypto concept | N | - | No crypto concept exists | Create crypto concept | {{ meta-organisation-roles.role_CISO }} | [TODO] |
| CON.3 | Data backup concept created | Backup concept | F | Backup documentation | - | - | {{ meta-organisation-roles.role_CIO }} | - |
| CON.3 | Backup tests performed | Backup process | P | Test protocols | Tests not regular | Establish quarterly backup tests | {{ meta-organisation-roles.role_CIO }} | [TODO] |
| CON.6 | Deletion concept created | Deletion concept | N | - | No deletion concept exists | Create deletion concept | {{ meta-organisation-roles.role_CISO }} | [TODO] |

### 3.3 Operations (OPS)

| Module | Requirement (Short) | Object | Status | Evidence | Finding | Measure | Owner | Target Date |
|---|---|---|---|---|---|---|---|---|
| OPS.1.1.2 | Administration concept | IT administration | P | Admin guideline | Privileged Access Management missing | Implement PAM solution | {{ meta-organisation-roles.role_CIO }} | [TODO] |
| OPS.1.1.3 | Patch process established | Patch management | F | Patch documentation | - | - | {{ meta-organisation-roles.role_CIO }} | - |
| OPS.1.1.3 | Patch SLAs defined | Patch management | P | SLA document | Critical patches > 30 days | Reduce SLA to 7 days | {{ meta-organisation-roles.role_CIO }} | [TODO] |
| OPS.1.1.4 | Malware protection implemented | All systems | F | Antivirus solution | - | - | {{ meta-organisation-roles.role_CIO }} | - |
| OPS.1.1.5 | Logging activated | All systems | P | Log configuration | Central log collection missing | Implement SIEM | {{ meta-organisation-roles.role_CIO }} | [TODO] |
| OPS.2.2 | Cloud security concept | Cloud services | N | - | No cloud security concept | Create cloud security concept | {{ meta-organisation-roles.role_CISO }} | [TODO] |

### 3.4 Detection and Response (DER)

| Module | Requirement (Short) | Object | Status | Evidence | Finding | Measure | Owner | Target Date |
|---|---|---|---|---|---|---|---|---|
| DER.1 | Detection established | Monitoring | P | Monitoring tools | SIEM missing | Implement SIEM | {{ meta-organisation-roles.role_CIO }} | [TODO] |
| DER.2.1 | Incident response process | Incident management | P | IR guideline | No incident response exercises | Establish annual IR exercise | {{ meta-organisation-roles.role_CISO }} | [TODO] |
| DER.2.2 | Forensics preparation | Forensics | N | - | No forensics preparation | Create forensics concept | {{ meta-organisation-roles.role_CISO }} | [TODO] |

### 3.5 Applications (APP)

| Module | Requirement (Short) | Object | Status | Evidence | Finding | Measure | Owner | Target Date |
|---|---|---|---|---|---|---|---|---|
| APP.3.1 | Secure web application development | [TODO: Web application] | P | SDLC process | SAST/DAST missing | Integrate security testing | [TODO] | [TODO] |
| APP.3.2 | Web server hardening | [TODO: Web server] | F | Hardening checklist | - | - | {{ meta-organisation-roles.role_CIO }} | - |
| APP.4.3 | Database hardening | [TODO: Database] | P | DB configuration | Encryption at rest missing | Activate TDE | {{ meta-organisation-roles.role_CIO }} | [TODO] |

### 3.6 IT Systems (SYS)

| Module | Requirement (Short) | Object | Status | Evidence | Finding | Measure | Owner | Target Date |
|---|---|---|---|---|---|---|---|---|
| SYS.1.1 | Server hardening | [[ netbox.device.server_001 ]] | F | Hardening baseline | - | - | {{ meta-organisation-roles.role_CIO }} | - |
| SYS.1.3 | Linux hardening | [TODO: Linux server] | P | CIS Benchmark | Not all CIS controls implemented | Complete CIS implementation | {{ meta-organisation-roles.role_CIO }} | [TODO] |
| SYS.1.5 | Virtualization security | [TODO: VMware] | P | VMware configuration | Network segmentation insufficient | Implement microsegmentation | {{ meta-organisation-roles.role_CIO }} | [TODO] |
| SYS.2.1 | Client hardening | Workstations | P | GPO configuration | BitLocker not comprehensive | Activate BitLocker on all clients | {{ meta-organisation-roles.role_CIO }} | [TODO] |
| SYS.3.2.1 | Mobile device management | Mobile devices | N | - | No MDM exists | Implement MDM solution | {{ meta-organisation-roles.role_CIO }} | [TODO] |

### 3.7 Networks and Communication (NET)

| Module | Requirement (Short) | Object | Status | Evidence | Finding | Measure | Owner | Target Date |
|---|---|---|---|---|---|---|---|---|
| NET.1.1 | Network segmentation | Network architecture | P | Network diagram | Segmentation insufficient | Implement microsegmentation | {{ meta-organisation-roles.role_CIO }} | [TODO] |
| NET.1.2 | Network monitoring | Network management | F | Monitoring tools | - | - | {{ meta-organisation-roles.role_CIO }} | - |
| NET.3.1 | Router/switch hardening | Network devices | P | Configuration evidence | SNMP v3 not everywhere | SNMP v3 comprehensive | {{ meta-organisation-roles.role_CIO }} | [TODO] |
| NET.3.2 | Firewall ruleset | Firewall | F | Firewall rules | - | - | {{ meta-organisation-roles.role_CIO }} | - |
| NET.3.3 | VPN security | VPN | P | VPN configuration | MFA for VPN missing | Implement MFA for VPN | {{ meta-organisation-roles.role_CIO }} | [TODO] |
| NET.2.1 | WLAN security | WLAN | F | WLAN configuration | - | - | {{ meta-organisation-roles.role_CIO }} | - |

### 3.8 Infrastructure (INF)

| Module | Requirement (Short) | Object | Status | Evidence | Finding | Measure | Owner | Target Date |
|---|---|---|---|---|---|---|---|---|
| INF.1 | Building security | [TODO] | P | Security concept | Visitor management insufficient | Visitor management system | [TODO: Facility] | [TODO] |
| INF.2 | Data center security | Data center | F | DC documentation | - | - | [TODO: Facility] | - |

## 4. Summary and Statistics

### 4.1 Fulfillment Statistics

| Module Layer | Total | Fulfilled (F) | Partial (P) | Not Fulfilled (N) | N/A | Fulfillment Rate |
|---|---|---|---|---|---|---|
| ISMS | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO: %] |
| ORP | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO: %] |
| CON | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO: %] |
| OPS | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO: %] |
| DER | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO: %] |
| APP | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO: %] |
| SYS | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO: %] |
| NET | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO: %] |
| INF | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO: %] |
| **Total** | **[TODO]** | **[TODO]** | **[TODO]** | **[TODO]** | **[TODO]** | **[TODO: %]** |

**Overall Fulfillment Rate:** [TODO: %]

### 4.2 Critical Gaps (Priority 1)

| ID | Requirement | Object | Risk | Measure | Owner | Target Date |
|---|---|---|---|---|---|---|
| GAP-001 | [TODO: Critical gap 1] | [TODO] | Very high | [TODO] | [TODO] | [TODO] |
| GAP-002 | [TODO: Critical gap 2] | [TODO] | Very high | [TODO] | [TODO] | [TODO] |

### 4.3 Quick Wins (Priority 2)

| ID | Requirement | Object | Effort | Benefit | Measure | Owner | Target Date |
|---|---|---|---|---|---|---|---|
| QW-001 | [TODO: Quick win 1] | [TODO] | Low | High | [TODO] | [TODO] | [TODO] |
| QW-002 | [TODO: Quick win 2] | [TODO] | Low | High | [TODO] | [TODO] | [TODO] |

### 4.4 Medium-Term Measures (Priority 3)

| ID | Requirement | Object | Effort | Measure | Owner | Target Date |
|---|---|---|---|---|---|---|
| MF-001 | [TODO: Medium-term measure 1] | [TODO] | Medium | [TODO] | [TODO] | [TODO] |
| MF-002 | [TODO: Medium-term measure 2] | [TODO] | Medium | [TODO] | [TODO] | [TODO] |

## 5. Management Summary

### 5.1 Overall Assessment

**Fulfillment Rate:** [TODO: %]

**Assessment:**
- [TODO: Summary assessment of security level]
- [TODO: Main findings]
- [TODO: Critical action areas]

### 5.2 Top 5 Findings

1. **[TODO: Finding 1]:** [TODO: Description and impact]
2. **[TODO: Finding 2]:** [TODO: Description and impact]
3. **[TODO: Finding 3]:** [TODO: Description and impact]
4. **[TODO: Finding 4]:** [TODO: Description and impact]
5. **[TODO: Finding 5]:** [TODO: Description and impact]

### 5.3 Resource Requirements

**Estimated Effort for Measure Implementation:**
- **Person-days:** [TODO]
- **Budget:** [TODO]
- **External Support:** [TODO]
- **Timeframe:** [TODO]

### 5.4 Dependencies

| Measure | Dependency | Impact | Mitigation |
|---|---|---|---|
| [TODO: Measure 1] | [TODO: Dependency] | [TODO] | [TODO] |
| [TODO: Measure 2] | [TODO: Dependency] | [TODO] | [TODO] |

## 6. Next Steps

1. **Measure Planning (Document 0100):** Detailed planning of identified measures
2. **Risk Analysis (Document 0090):** For objects with increased protection needs or non-modelable risks
3. **Management Presentation:** Presentation of results to executive management
4. **Measure Implementation:** Start of implementation of prioritized measures

## 7. Update and Maintenance

The basic security check is repeated:
- After completion of significant measures
- When significant changes occur in IT infrastructure
- At least annually as part of the ISMS review

**Responsible:** {{ meta-organisation-roles.role_CISO }} (ISB)  
**Next Check:** {{ meta-handbook.next_review }}

## 8. Approval

| Role | Name | Date | Approval |
|---|---|---|---|
| ISB | {{ meta-organisation-roles.role_CISO }} | {{ meta-handbook.modifydate }} | {{ meta-handbook.status }} |
| IT Management | {{ meta-organisation-roles.role_CIO }} | {{ meta-handbook.modifydate }} | {{ meta-handbook.status }} |
| Executive Management | {{ meta-organisation-roles.role_CEO }} | {{ meta-handbook.modifydate }} | {{ meta-handbook.status }} |

**References:**
- BSI Standard 200-2: IT-Grundschutz Methodology (Chapter 8: Basic Security Check)
- BSI IT-Grundschutz Compendium

<!-- End of template -->