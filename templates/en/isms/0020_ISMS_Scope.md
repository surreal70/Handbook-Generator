# ISMS Scope

**Document-ID:** [FRAMEWORK]-0020
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
The ISMS scope defines the boundaries of your information security management 
system. It should clearly specify what is included and excluded, and provide 
justification for any exclusions. The scope must be appropriate to the nature, 
scale, and complexity of your organization.

ISO 27001:2022 Reference: Clause 4.3 - Determining the scope of the ISMS
-->

**Document ID:** 0020  
**Document Type:** ISMS Foundation Document  
**Standard Reference:** ISO/IEC 27001:2022 Clause 4.3  
**Owner:** {{ meta-organisation-roles.role_CISO }}  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** {{ meta-handbook.modifydate }}  
**Next Review:** {{ meta-handbook.next_review }}

## 1. Scope Definition

The scope of the Information Security Management System (ISMS) of **{{ meta-organisation.name }}** includes:

### 1.1 Organization
- **Organization Name:** {{ meta-organisation.name }}
- **Legal Form:** [TODO]
- **Headquarters:** {{ meta-organisation.address }}
- **Number of Employees:** [TODO]
- **Industry:** [TODO]

### 1.2 Locations
The ISMS applies to the following locations:

- **Main Location:** [[ netbox.site.name ]]
  - Address: [[ netbox.site.address ]]
  - Function: Data center, offices, development
  
[TODO: Add additional locations]

<!-- 
List all physical locations covered by the ISMS. Include data centers, 
offices, and any remote work arrangements if applicable.
-->

### 1.3 Processes and Services
The ISMS covers the following business processes and IT services:

**Core Processes:**
- IT operations and infrastructure management
- Software development and DevOps
- Data processing and data management
- Customer service and support
- [TODO: Additional core processes]

**IT Services:**
- Network infrastructure ([[ netbox.device.core_switch.name ]])
- Server and virtualization platforms
- Cloud services and SaaS applications
- Database systems
- Backup and recovery systems
- [TODO: Additional IT services]

### 1.4 Information Assets
The ISMS protects the following categories of information assets:

**Data and Information:**
- Customer data (personal data according to GDPR)
- Business data (contracts, financial data, strategic documents)
- Technical data (source code, system documentation, configurations)
- Employee data (HR data, access credentials)

**IT Systems and Infrastructure:**
- Production systems and development environments
- Network components (routers, switches, firewalls)
- Endpoints (laptops, workstations, mobile devices)
- Cloud infrastructure and virtual machines

**Applications and Software:**
- Business applications (ERP, CRM, etc.)
- Development tools and CI/CD pipelines
- Communication platforms (email, collaboration tools)

<!-- 
Classify information assets according to your data classification scheme 
(see 0280_Policy_Data_Classification_and_Information_Handling.md)
-->

### 1.5 Systems and Platforms
The ISMS includes the following technical platforms:

**Network Infrastructure:**
- Core Switch: [[ netbox.device.core_switch.name ]]
- Management VLAN: [[ netbox.vlan.management.vid ]]
- [TODO: Additional network components from NetBox]

**Servers and Virtualization:**
- [TODO: Server list from asset inventory]

**Cloud Platforms:**
- [TODO: AWS/Azure/GCP accounts and services]

**Security Systems:**
- Firewall, IDS/IPS, SIEM
- Endpoint Protection (EDR/AV)
- Identity and Access Management (IAM)

## 2. Scope Boundaries and Exclusions

### 2.1 Excluded Areas
The following areas are explicitly excluded from the ISMS scope:

[TODO: Define exclusions, e.g.:]
- Production facilities (if not IT-relevant)
- External supplier systems (outside our control)
- Legacy systems being phased out (with decommission date)

### 2.2 Justification for Exclusions
A justification is documented for each exclusion:

[TODO: Justifications for exclusions]
- **Example:** Legacy system XYZ will be decommissioned on [date] and no longer contains critical data.

### 2.3 Risks and Dependencies from Exclusions
Exclusions are recorded and assessed in the risk register:

[TODO: Risk assessment for exclusions]
- See `0080_ISMS_Risk_Register_Template.md` for details

<!-- 
ISO 27001:2022 requires that exclusions do not affect the organization's 
ability to provide assurance that information security requirements are met.
Document any residual risks from exclusions.
-->

## 3. Interfaces

### 3.1 External Organizations and Providers
The ISMS has interfaces with the following external parties:

**Cloud Providers:**
- [TODO: AWS/Azure/GCP - services and responsibilities]

**Managed Service Providers:**
- [TODO: MSP partners and their access]

**Suppliers and Service Providers:**
- [TODO: Critical suppliers with access to information assets]

<!-- 
Document third-party relationships and their security requirements.
See 0460_Policy_Suppliers_and_Cloud_Security.md for details.
-->

### 3.2 Other Management Systems
The ISMS is integrated with the following other management systems:

**Business Continuity Management (BCM):**
- Interface to BCM handbook (see `0440_Policy_Business_Continuity_ICT_Readiness.md`)
- Joint risk analysis and BIA

**Data Protection Management System (DPMS):**
- Interface to GDPR compliance (see `0560_Policy_Data_Protection_Interfaces.md`)
- Joint processing records and data protection impact assessments

**Quality Management System (QMS):**
- [TODO: Interfaces to ISO 9001 or other QMS]

## 4. Scope Diagram

The following diagram visualizes the ISMS scope:

```
┌─────────────────────────────────────────────────────────────────┐
│                    ISMS Scope - {{ meta-organisation.name }}     │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │  Location 1  │  │  Location 2  │  │ Remote Work  │         │
│  │ (Headquarters)│  │   (Branch)   │  │ (Employees)  │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐    │
│  │              IT Infrastructure                         │    │
│  │  • Network (Core, Access, DMZ)                        │    │
│  │  • Servers (Prod, Dev, Test)                          │    │
│  │  • Cloud (AWS/Azure/GCP)                              │    │
│  │  • Endpoints (Laptops, Workstations, Mobile)          │    │
│  └────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐    │
│  │              Business Processes                        │    │
│  │  • IT Operations & Support                            │    │
│  │  • Software Development                               │    │
│  │  • Data Processing                                    │    │
│  │  • Customer Service                                   │    │
│  └────────────────────────────────────────────────────────┘    │
│                                                                  │
│  ┌────────────────────────────────────────────────────────┐    │
│  │              Information Assets                        │    │
│  │  • Customer Data (GDPR-relevant)                      │    │
│  │  • Business Data (Contracts, Finances)                │    │
│  │  • Technical Data (Code, Configs)                     │    │
│  │  • Employee Data (HR)                                 │    │
│  └────────────────────────────────────────────────────────┘    │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘

External Interfaces:
├─ Cloud Providers (AWS/Azure/GCP)
├─ Managed Service Providers
├─ Suppliers and Service Providers
└─ Customers and Partners

Exclusions:
├─ [TODO: Excluded areas]
└─ [TODO: Legacy systems being phased out]
```

<!-- 
Create a detailed scope diagram using your preferred diagramming tool 
(e.g., draw.io, Visio, PlantUML) and save it as diagrams/isms_scope.png
-->

[TODO: Create detailed scope diagram and link]
- File: `diagrams/isms_scope.png`

## 5. Scope Changes and Review

### 5.1 Change Management
Changes to the ISMS scope must be made through the change management process:
- See `0360_Policy_Change_and_Release_Management.md`
- Scope changes require approval by CISO and management
- Impacts on risk analysis and SoA must be assessed

### 5.2 Regular Review
The ISMS scope is regularly reviewed:
- **Annual Review:** As part of management review (see `0140_ISMS_Management_Review_Template.md`)
- **Event-Driven Review:** For significant organizational changes (mergers, acquisitions, new locations, new services)

## 6. References

### Internal Documents
- `0010_ISMS_Information_Security_Policy.md` - ISMS Policy
- `0030_ISMS_Context_and_Interested_Parties.md` - Context of Organization
- `0050_ISMS_Structure_Analysis_Template.md` - Structure Analysis (if available)
- `0080_ISMS_Risk_Register_Template.md` - Risk Register
- `0100_ISMS_Statement_of_Applicability_SoA_Template.md` - SoA

### External Standards
- **ISO/IEC 27001:2022** - Clause 4.3: Determining the scope of the ISMS
- **ISO/IEC 27002:2022** - Information security controls

**Approved by:**  
{{ meta-organisation-roles.role_CISO }}, CISO  
{{ meta-handbook.management_ceo }}, Management  
Date: {{ meta-handbook.modifydate }}

**Next Review:** {{ meta-handbook.next_review }}

