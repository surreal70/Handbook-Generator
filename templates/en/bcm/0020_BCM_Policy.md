# BCM Policy

**Document-ID:** [FRAMEWORK]-0020
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Approved by:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Classification:** {{ meta-handbook.classification }}
**Last Update:** {{ meta-handbook.modifydate }}

---

---

<!-- 
TEMPLATE AUTHOR NOTE:
This template defines the Business Continuity Management Policy.
It aligns with ISO 22301:2019 Clause 5.2 (Policy) and demonstrates top management commitment.

Customization required:
- Adapt policy statement to your organization's context
- Define specific BCM objectives
- Establish governance structure and responsibilities
- Obtain formal approval from top management
-->

## 1. Policy Statement

The management of {{ meta-organisation.name }} commits to the implementation and continuous improvement of a Business Continuity Management System (BCMS) in accordance with **ISO 22301:2019**.

### 1.1 Management Commitment

The management, represented by **{{ meta-organisation-roles.role_CEO }}** (CEO), hereby declares:

- **Highest priority:** Business continuity has strategic importance for protecting our organization, employees, customers, and stakeholders
- **Resource provision:** Adequate financial, personnel, and technical resources are provided for the BCMS
- **Leadership responsibility:** Management assumes overall responsibility for the BCMS and its effectiveness
- **Continuous improvement:** The BCMS is regularly reviewed and continuously improved

### 1.2 BCMS Principles

The BCMS of {{ meta-organisation.name }} is based on the following principles:

1. **Risk-based approach:** Identification, assessment, and treatment of risks to business continuity
2. **Continuous improvement:** Systematic development of BCM capabilities through exercises, tests, and lessons learned
3. **Accountability:** Clear assignment of roles and responsibilities at all organizational levels
4. **Exercise and testing:** Regular exercises and tests to validate BCM measures
5. **Documentation and traceability:** Complete documentation of all BCM activities and decisions
6. **Compliance:** Adherence to all relevant legal, regulatory, and contractual requirements

### 1.3 Commitments

{{ meta-organisation.name }} commits to:

- **Protection of human life:** Safety and well-being of employees, customers, and visitors have top priority
- **Business continuity:** Maintaining critical business processes even during severe disruptions
- **Stakeholder communication:** Transparent and timely communication with all affected stakeholders
- **Supplier management:** Ensuring business continuity capabilities of critical suppliers
- **Compliance and evidence:** Fulfilling all relevant requirements and providing evidence

## 2. Objectives and Principles

### 2.1 Strategic BCM Objectives

{{ meta-organisation.name }} pursues the following strategic BCM objectives:

**Objective 1: Minimization of Downtime**
- Recovery of critical business processes within defined Recovery Time Objectives (RTO)
- Limitation of data loss within defined Recovery Point Objectives (RPO)
- Measurable reduction of average recovery time by [TODO: X%] per year

**Objective 2: Crisis Response Capability**
- Establishment of 24/7 crisis organization with clear escalation paths
- Training of all employees in BCM basics and emergency behavior
- Conducting at least [TODO: X] BCM exercises per year

**Objective 3: Compliance and Demonstrability**
- Fulfillment of all regulatory requirements for business continuity
- Provision of complete evidence for audits and certifications
- Maintenance of ISO 22301 certification (if pursued)

**Objective 4: Stakeholder Trust**
- Transparent communication of BCM capabilities to customers and partners
- Demonstration of business continuity capabilities in tenders and contracts
- Protection of reputation and brand value

**Objective 5: Continuous Improvement**
- Systematic evaluation of exercises, tests, and real incidents
- Implementation of lessons learned and best practices
- Regular updates of BCM documentation and plans

### 2.2 Operational Principles

**Principle 1: Safety First**
- Human life and health always take precedence over material values
- In emergencies: First bring people to safety, then minimize property damage

**Principle 2: Communication Before Action**
- Structured communication and coordination before uncoordinated individual actions
- Clear chains of command and escalation paths in crises

**Principle 3: Documentation and Traceability**
- All decisions and measures are documented
- Traceability for post-incident reviews and audits

**Principle 4: Flexibility and Adaptability**
- BCM plans are guidelines, not rigid requirements
- Situation-appropriate adaptation of measures is allowed and desired

## 3. Scope

The scope of the BCMS is defined in:

→ **See document:** `0010_Purpose_and_Scope.md`

The BCMS covers all critical business processes, IT systems, and locations of {{ meta-organisation.name }} according to the scope defined in the scope document.

## 4. Governance and Responsibilities

### 4.1 RACI Matrix BCM Governance

| Activity | CEO | CIO | CISO | BCM Manager | Department | IT Ops |
|----------|-----|-----|------|-------------|------------|--------|
| Approve BCM policy | **A** | C | C | R | I | I |
| Define BCM strategy | **A** | R | C | R | C | I |
| Approve BCM budget | **A** | C | I | R | I | I |
| Conduct BIA | I | C | I | **A** | R | C |
| Create BCM plans | I | C | C | **A** | R | R |
| Conduct BCM exercises | I | C | C | **A** | R | R |
| Activate crisis | **A** | R | R | R | I | I |
| Management review | **A** | R | C | R | I | I |

**Legend:**
- **R** = Responsible (execution responsibility)
- **A** = Accountable (overall responsibility, decision authority)
- **C** = Consulted (consulted, subject matter expertise)
- **I** = Informed (informed)

### 4.2 Roles and Responsibilities

**Executive Management (CEO)**
- **Responsible:** {{ meta-organisation-roles.role_CEO }} ({{ meta-organisation-roles.role_CEO }})
- **Tasks:** Overall responsibility for BCMS, approval of BCM policy, release of resources, crisis activation

**Chief Information Officer (CIO)**
- **Responsible:** {{ meta-organisation-roles.role_CIO }} ({{ meta-organisation-roles.role_CIO }})
- **Tasks:** Responsibility for IT continuity, IT disaster recovery, technical BCM measures

**Chief Information Security Officer (CISO)**
- **Responsible:** {{ meta-organisation-roles.role_CISO }} ({{ meta-organisation-roles.role_CISO }})
- **Tasks:** ISMS-BCMS interface, security incident response, cyber resilience

**BCM Manager**
- **Responsible:** [TODO: BCM Manager name and contact]
- **Tasks:** Operational management of BCMS, coordination of BIA and risk analysis, BCM exercises, maintenance of BCM documentation

**Departments**
- **Responsible:** Respective department heads
- **Tasks:** Identification of critical processes, participation in BIA, creation of functional BCM plans, participation in exercises

**IT Operations**
- **Responsible:** {{ meta-organisation-roles.role_IT_Manager }} ({{ meta-organisation-roles.role_IT_Manager }})
- **Tasks:** Implementation of technical BCM measures, IT disaster recovery, backup and restore

## 5. Approvals and Authorizations

This BCM policy has been reviewed and approved by:

| Role | Name | Function | Date | Signature/Approval |
|------|------|----------|------|-------------------|
| **Executive Management** | {{ meta-organisation-roles.role_CEO }} | CEO | [TODO: Date] | [TODO: Signature] |
| **BCM Owner** | [TODO: BCM Manager] | BCM Manager | [TODO: Date] | [TODO: Signature] |
| **IT Management** | {{ meta-organisation-roles.role_CIO }} | CIO | [TODO: Date] | [TODO: Signature] |
| **Information Security** | {{ meta-organisation-roles.role_CISO }} | CISO | [TODO: Date] | [TODO: Signature] |
| **Compliance** | [TODO: Compliance Officer] | Compliance Officer | [TODO: Date] | [TODO: Signature] |

## 6. Review and Update

This BCM policy is:

- **Annually** reviewed by management as part of the management review
- Updated when **significant changes** occur in the organization, business processes, or regulatory requirements
- Reviewed for adaptation needs after **severe incidents** or exercises

**Next planned review:** [TODO: Date]

<!-- End of template -->
