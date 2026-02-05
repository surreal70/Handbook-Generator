# Policy: Asset Management



**Document ID:** 0300  
**Document Type:** Policy (abstract)  
**Standard Reference:** ISO/IEC 27001:2022 Annex A.5.9-A.5.11 (incl. Amendment 1:2024)  
**Owner:** Thomas Weber  
**Version:** 1.0  
**Status:** Approved  
**Classification:** Internal  
**Last Updated:** {{ meta.document.date }}  
**Next Review:** {{ meta.document.next_review }}

---

## 1. Purpose

This policy defines the principles for asset management and inventory control at **AdminSend GmbH**. It ensures that all information assets are identified, documented, classified, and appropriately protected throughout their entire lifecycle.

## 2. Scope

This policy applies to:

- **Organizational Units:** All departments and locations of AdminSend GmbH
- **Asset Types:** Hardware, software, data, information, services, people, intangible assets
- **Systems:** All IT systems, network components, endpoints, servers, cloud resources
- **Lifecycle:** Procurement, commissioning, operation, maintenance, decommissioning, disposal
- **Locations:** {{ netbox.site.name }} and all other operational sites

**Exceptions:** Exceptions are only permitted through the defined exception process (`0640_Policy_Ausnahmen_und_Risk_Waivers.md`).

## 3. Principles (Policy Statements)

### 3.1 Complete Asset Inventory
All organizational assets are recorded and documented in a central asset inventory. The inventory is regularly updated and checked for completeness.

### 3.2 Asset Owner Assignment
Each asset has a defined asset owner who is responsible for:
- Asset classification
- Definition of protection requirements
- Approval of access and usage rights
- Lifecycle management

### 3.3 Asset Classification and Tagging
Assets are classified and tagged with metadata:
- Classification by protection requirements (confidentiality, integrity, availability)
- Technical tags (environment, application, cost center)
- Compliance tags (GDPR, PCI-DSS, etc.)

### 3.4 Lifecycle Management
Assets are managed throughout their entire lifecycle:
- **Procurement:** Security requirements, approval process
- **Commissioning:** Configuration, hardening, documentation
- **Operation:** Maintenance, patching, monitoring
- **Decommissioning:** Data deletion, decommissioning
- **Disposal:** Secure destruction, recycling

### 3.5 Acceptable Use
Assets may only be used for approved business purposes. Personal use is only permitted within the framework of the Acceptable Use Policy (`0200_Policy_Akzeptable_Nutzung_IT.md`).

### 3.6 Return of Assets
Upon role change or departure, all assets must be returned. The return process is part of the leaver process.

### 3.7 Protection Against Loss and Theft
Assets are protected against loss, theft, and unauthorized access through appropriate measures:
- Physical security (access control, alarm systems)
- Encryption of mobile devices
- Remote wipe functionality
- Insurance of critical assets

### 3.8 Secure Disposal
Assets are securely disposed of at the end of their lifecycle:
- Data deletion per recognized standards
- Physical destruction for highly sensitive data
- Environmentally responsible recycling
- Documentation of disposal

## 4. Roles and Responsibilities

### RACI Matrix: Asset Management

| Activity | CISO | Asset Owner | IT Operations | Procurement | Facility Management |
|----------|------|-------------|---------------|-------------|---------------------|
| Policy Creation | R/A | C | C | C | I |
| Asset Inventory | A | R | R | C | C |
| Asset Owner Assignment | C | R/A | I | I | I |
| Classification | C | R/A | I | I | I |
| Lifecycle Management | A | R | R | C | C |
| Secure Disposal | C | A | R | I | R |
| Monitoring and Audits | R/A | C | C | I | I |

**Legend:** R = Responsible (Execution), A = Accountable (Accountable), C = Consulted (Consulted), I = Informed (Informed)

### Key Roles

- **Policy Owner:** Thomas Weber (CISO)
- **Asset Owners:** Department heads, system owners
- **Asset Manager:** {{ meta.it.asset_manager }}
- **Implementation Responsible:** IT operations, procurement, facility management
- **Control/Audit Function:** ISMS, internal audit

## 5. Derivations (Guidelines/Standards/Processes)

Implementation details are defined in subordinate documents:

### Related Guidelines
- **0310_Richtlinie_Asset_Inventory_Tagging_und_Entsorgung.md** - Detailed implementation guideline
- `0280_Policy_Datenklassifizierung_und_Informationshandling.md` - Data classification policy
- `0200_Policy_Akzeptable_Nutzung_IT.md` - Acceptable use policy
- `0480_Policy_Physische_Sicherheit.md` - Physical security policy

### Related Standards/Baselines
- Asset inventory schema (CMDB)
- Tagging standards
- Disposal standards
- Lifecycle management processes

### Related Processes
- Asset procurement process
- Asset onboarding and configuration
- Asset return process (leaver)
- Secure disposal process

## 6. Compliance, Monitoring, and Enforcement

### Metrics and KPIs
- Inventory rate (target: 100% of all assets recorded)
- Number of assets without asset owner
- Number of unclassified assets
- Average time to asset registration
- Number of lost or stolen assets
- Compliance rate with disposal standards

### Evidence and Proof
- Asset inventory (CMDB)
- Asset owner assignments
- Classification register
- Disposal certificates
- Audit reports on asset management
- Insurance certificates

### Consequences for Violations
Violations of this policy are handled according to applicable HR and compliance processes:
- **Unregistered assets:** Post-registration, retraining
- **Loss of assets:** Investigation, possible cost reimbursement
- **Improper disposal:** Retraining, disciplinary action
- **Repeated violations:** Employment law consequences

## 7. Exceptions

Exceptions to this policy are only permitted in justified exceptional cases:

- **Exception Process:** See `0640_Policy_Ausnahmen_und_Risk_Waivers.md`
- **Approval:** Exceptions must be approved by CISO and asset owner
- **Documentation:** All exceptions are documented in the risk register
- **Time Limit:** Exceptions are generally time-limited

## 8. References

### Internal Documents
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS policy
- `0310_Richtlinie_Asset_Inventory_Tagging_und_Entsorgung.md` - Detailed guideline
- `0720_Anhang_Asset_und_Systeminventar_Template.md` - Asset inventory template
- `0080_ISMS_Risikoregister_Template.md` - Risk register

### External Standards and Requirements
- **ISO/IEC 27001:2022 Annex A.5.9** - Inventory of information and other associated assets
- **ISO/IEC 27001:2022 Annex A.5.10** - Acceptable use of information and other associated assets
- **ISO/IEC 27001:2022 Annex A.5.11** - Return of assets
- **ISO/IEC 27002:2022** - Information security controls
- **ITIL 4** - IT Asset Management
- **ISO/IEC 19770** - IT Asset Management

---

**Approved by:**  
{{ meta.management.ceo }}, Management  
Date: {{ meta.document.approval_date }}

**Next Review:** {{ meta.document.next_review }} (annually or as needed)
