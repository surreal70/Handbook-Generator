# CIS Controls v8 Template Structure Design

## Overview

This document defines the structure and organization for CIS Controls v8 templates within the handbook generator system. The CIS Controls v8 framework provides a prioritized set of actions to protect organizations and data from known cyber attack vectors. This design document outlines the template structure, numbering scheme, placeholder strategy, and README organization for future implementation.

**Note**: This is a design-only document. No template files are implemented as part of this phase. Implementation will occur in a future phase.

## CIS Controls v8 Framework Overview

The CIS Controls v8 consists of 18 Controls organized into three Implementation Groups (IGs):

- **Implementation Group 1 (IG1)**: Essential cyber hygiene for small organizations with limited resources
- **Implementation Group 2 (IG2)**: Builds on IG1 for organizations with moderate resources and risk
- **Implementation Group 3 (IG3)**: Adds advanced controls for organizations with significant resources and high risk

### Implementation Group Philosophy

- **IG1**: Minimum security controls (56 Safeguards) - Essential for all organizations
- **IG2**: IG1 + additional controls (74 Safeguards) - For organizations with IT security staff
- **IG3**: IG1 + IG2 + advanced controls (153 Safeguards) - For organizations with dedicated security teams

## Template Structure Design

### Directory Organization

```
templates/
├── de/
│   └── cis-controls/
│       ├── README.md
│       ├── 0010_Einfuehrung_und_Geltungsbereich.md
│       ├── 0020_CIS_Controls_Uebersicht.md
│       ├── 0030_Implementation_Groups_Strategie.md
│       ├── 0100_Inventar_und_Kontrolle_von_Unternehmensassets.md
│       ├── 0200_Inventar_und_Kontrolle_von_Softwareassets.md
│       ├── 0300_Datenschutz.md
│       ├── 0400_Sichere_Konfiguration_von_Unternehmensassets.md
│       ├── 0500_Kontoverwaltung.md
│       ├── 0600_Zugriffskontrollverwaltung.md
│       ├── 0700_Kontinuierliche_Schwachstellenverwaltung.md
│       ├── 0800_Audit_Log_Management.md
│       ├── 0900_Email_und_Webbrowser_Schutz.md
│       ├── 1000_Malware_Abwehr.md
│       ├── 1100_Datenwiederherstellung.md
│       ├── 1200_Netzwerkinfrastruktur_Management.md
│       ├── 1300_Netzwerkueberwachung_und_Abwehr.md
│       ├── 1400_Sicherheitsbewusstsein_und_Kompetenztraining.md
│       ├── 1500_Service_Provider_Management.md
│       ├── 1600_Anwendungssoftware_Sicherheit.md
│       ├── 1700_Incident_Response_Management.md
│       ├── 1800_Penetrationstests.md
│       ├── 9000_Anhang_Safeguard_Matrix.md
│       ├── 9100_Anhang_Asset_Type_Mapping.md
│       ├── 9200_Anhang_Security_Functions_Mapping.md
│       └── 9900_Glossar_und_Abkuerzungen.md
└── en/
    └── cis-controls/
        └── (identical structure with English translations)
```


### Template Numbering Scheme

The CIS Controls templates use a systematic numbering scheme:

- **0010-0030**: Introduction and framework overview
- **0100-1800**: Individual CIS Controls (100 per control, e.g., Control 1 = 0100, Control 18 = 1800)
- **9000-9200**: Appendices with cross-reference matrices
- **9900**: Glossary and abbreviations

This numbering scheme:
- Provides clear separation between controls
- Allows for future expansion within each control section
- Maintains consistency with other template types (BCM, ISMS, BSI Grundschutz)
- Supports easy sorting and organization

### Template Count

**Total Templates per Language**: 25 templates
- 3 foundation templates (0010-0030)
- 18 control templates (0100-1800)
- 4 appendix templates (9000-9900)

**Total Templates**: 50 templates (25 German + 25 English)


## CIS Controls v8 Detailed Structure

### Foundation Templates (0010-0030)

#### 0010_Einfuehrung_und_Geltungsbereich.md
**Purpose**: Introduction to CIS Controls implementation
**Content**:
- Purpose and scope of CIS Controls handbook
- Target audience (IT security teams, management, auditors)
- Document structure and navigation
- Relationship to other security frameworks (ISO 27001, NIST CSF)
- Meta placeholders for organization information

#### 0020_CIS_Controls_Uebersicht.md
**Purpose**: Overview of CIS Controls v8 framework
**Content**:
- CIS Controls v8 history and evolution
- Framework structure (18 Controls, 153 Safeguards)
- Asset Types (Devices, Applications, Network, Data, Users)
- Security Functions (Identify, Protect, Detect, Respond, Recover)
- Benefits of CIS Controls implementation

#### 0030_Implementation_Groups_Strategie.md
**Purpose**: Implementation Group selection and strategy
**Content**:
- IG1, IG2, IG3 definitions and characteristics
- Self-assessment questionnaire for IG selection
- Implementation roadmap by IG level
- Resource requirements per IG
- RACI matrix for CIS Controls governance
- Meta placeholders for selected IG level


### Control Templates (0100-1800)

Each control template follows a consistent structure:

#### 0100_Inventar_und_Kontrolle_von_Unternehmensassets.md
**CIS Control 1**: Inventory and Control of Enterprise Assets
**IG Level**: IG1 (5 Safeguards)
**Content Structure**:
- Control overview and importance
- Asset types covered (Devices)
- Safeguards list with IG mappings:
  - 1.1 Establish and Maintain Detailed Enterprise Asset Inventory (IG1)
  - 1.2 Address Unauthorized Assets (IG1)
  - 1.3 Utilize an Active Discovery Tool (IG2)
  - 1.4 Use Dynamic Host Configuration Protocol (DHCP) Logging (IG2)
  - 1.5 Use a Passive Asset Discovery Tool (IG3)
- Implementation guidance per safeguard
- NetBox placeholders for asset inventory
- [TODO] markers for organization-specific asset lists
- RACI matrix for asset management

#### 0200_Inventar_und_Kontrolle_von_Softwareassets.md
**CIS Control 2**: Inventory and Control of Software Assets
**IG Level**: IG1 (7 Safeguards)
**Content Structure**:
- Control overview and importance
- Asset types covered (Applications)
- Safeguards list with IG mappings (2.1-2.7)
- Software inventory management procedures
- Authorized/unauthorized software lists
- NetBox placeholders for software inventory
- [TODO] markers for approved software catalog

#### 0300_Datenschutz.md
**CIS Control 3**: Data Protection
**IG Level**: IG1 (14 Safeguards)
**Content Structure**:
- Control overview and importance
- Asset types covered (Data)
- Safeguards list with IG mappings (3.1-3.14)
- Data classification scheme
- Data handling procedures
- Encryption requirements
- Meta placeholders for data protection officer
- [TODO] markers for data classification matrix


#### 0400_Sichere_Konfiguration_von_Unternehmensassets.md
**CIS Control 4**: Secure Configuration of Enterprise Assets and Software
**IG Level**: IG1 (12 Safeguards)
**Content Structure**:
- Control overview and importance
- Asset types covered (Devices, Applications)
- Safeguards list with IG mappings (4.1-4.12)
- Configuration management procedures
- Hardening standards and baselines
- Configuration drift detection
- NetBox placeholders for configuration baselines

#### 0500_Kontoverwaltung.md
**CIS Control 5**: Account Management
**IG Level**: IG1 (6 Safeguards)
**Content Structure**:
- Control overview and importance
- Asset types covered (Users)
- Safeguards list with IG mappings (5.1-5.6)
- Account lifecycle management (Joiner-Mover-Leaver)
- Privileged account management
- Account review and recertification
- Meta placeholders for identity management system

#### 0600_Zugriffskontrollverwaltung.md
**CIS Control 6**: Access Control Management
**IG Level**: IG1 (8 Safeguards)
**Content Structure**:
- Control overview and importance
- Asset types covered (Users, Devices, Applications)
- Safeguards list with IG mappings (6.1-6.8)
- Access control policies
- Multi-factor authentication (MFA) requirements
- Remote access controls
- Meta placeholders for access control systems

#### 0700_Kontinuierliche_Schwachstellenverwaltung.md
**CIS Control 7**: Continuous Vulnerability Management
**IG Level**: IG1 (7 Safeguards)
**Content Structure**:
- Control overview and importance
- Asset types covered (Devices, Applications)
- Safeguards list with IG mappings (7.1-7.7)
- Vulnerability scanning procedures
- Patch management processes
- Remediation timelines by severity
- NetBox placeholders for vulnerability management tools


#### 0800_Audit_Log_Management.md
**CIS Control 8**: Audit Log Management
**IG Level**: IG1 (12 Safeguards)
**Content Structure**:
- Control overview and importance
- Asset types covered (Network, Devices, Applications)
- Safeguards list with IG mappings (8.1-8.12)
- Logging requirements and standards
- Log retention policies
- SIEM integration
- NetBox placeholders for logging infrastructure

#### 0900_Email_und_Webbrowser_Schutz.md
**CIS Control 9**: Email and Web Browser Protections
**IG Level**: IG1 (7 Safeguards)
**Content Structure**:
- Control overview and importance
- Asset types covered (Applications)
- Safeguards list with IG mappings (9.1-9.7)
- Email security controls (SPF, DKIM, DMARC)
- Web browser hardening
- DNS filtering
- Meta placeholders for email security gateway

#### 1000_Malware_Abwehr.md
**CIS Control 10**: Malware Defenses
**IG Level**: IG1 (7 Safeguards)
**Content Structure**:
- Control overview and importance
- Asset types covered (Devices, Applications)
- Safeguards list with IG mappings (10.1-10.7)
- Anti-malware deployment
- Endpoint detection and response (EDR)
- Malware incident response
- NetBox placeholders for security tools

#### 1100_Datenwiederherstellung.md
**CIS Control 11**: Data Recovery
**IG Level**: IG1 (5 Safeguards)
**Content Structure**:
- Control overview and importance
- Asset types covered (Data)
- Safeguards list with IG mappings (11.1-11.5)
- Backup strategy and procedures
- Backup testing and validation
- Recovery time objectives (RTO)
- Recovery point objectives (RPO)
- NetBox placeholders for backup infrastructure


#### 1200_Netzwerkinfrastruktur_Management.md
**CIS Control 12**: Network Infrastructure Management
**IG Level**: IG1 (8 Safeguards)
**Content Structure**:
- Control overview and importance
- Asset types covered (Network, Devices)
- Safeguards list with IG mappings (12.1-12.8)
- Network segmentation strategy
- Network device hardening
- Network access control (NAC)
- NetBox placeholders for network topology

#### 1300_Netzwerkueberwachung_und_Abwehr.md
**CIS Control 13**: Network Monitoring and Defense
**IG Level**: IG1 (11 Safeguards)
**Content Structure**:
- Control overview and importance
- Asset types covered (Network)
- Safeguards list with IG mappings (13.1-13.11)
- Network traffic monitoring
- Intrusion detection/prevention systems (IDS/IPS)
- Network anomaly detection
- NetBox placeholders for security monitoring tools

#### 1400_Sicherheitsbewusstsein_und_Kompetenztraining.md
**CIS Control 14**: Security Awareness and Skills Training
**IG Level**: IG1 (9 Safeguards)
**Content Structure**:
- Control overview and importance
- Asset types covered (Users)
- Safeguards list with IG mappings (14.1-14.9)
- Security awareness program
- Role-based training requirements
- Phishing simulation exercises
- Training effectiveness metrics
- Meta placeholders for training coordinator

#### 1500_Service_Provider_Management.md
**CIS Control 15**: Service Provider Management
**IG Level**: IG1 (7 Safeguards)
**Content Structure**:
- Control overview and importance
- Asset types covered (N/A - Process control)
- Safeguards list with IG mappings (15.1-15.7)
- Third-party risk assessment
- Vendor security requirements
- Cloud service provider controls
- Contract security clauses
- [TODO] markers for vendor inventory


#### 1600_Anwendungssoftware_Sicherheit.md
**CIS Control 16**: Application Software Security
**IG Level**: IG2 (14 Safeguards)
**Content Structure**:
- Control overview and importance
- Asset types covered (Applications)
- Safeguards list with IG mappings (16.1-16.14)
- Secure software development lifecycle (SSDLC)
- Code review and testing (SAST, DAST)
- Application security testing
- Secrets management
- Meta placeholders for development tools

#### 1700_Incident_Response_Management.md
**CIS Control 17**: Incident Response Management
**IG Level**: IG1 (9 Safeguards)
**Content Structure**:
- Control overview and importance
- Asset types covered (N/A - Process control)
- Safeguards list with IG mappings (17.1-17.9)
- Incident response plan
- Incident classification and prioritization
- Incident response team (CSIRT) structure
- Incident communication procedures
- Post-incident review and lessons learned
- RACI matrix for incident response

#### 1800_Penetrationstests.md
**CIS Control 18**: Penetration Testing
**IG Level**: IG2 (5 Safeguards)
**Content Structure**:
- Control overview and importance
- Asset types covered (Network, Applications)
- Safeguards list with IG mappings (18.1-18.5)
- Penetration testing methodology
- Testing frequency and scope
- Red team exercises
- Vulnerability disclosure process
- [TODO] markers for testing schedule


### Appendix Templates (9000-9900)

#### 9000_Anhang_Safeguard_Matrix.md
**Purpose**: Complete safeguard reference matrix
**Content Structure**:
- Complete list of all 153 Safeguards
- IG level mapping for each safeguard
- Asset type mapping for each safeguard
- Security function mapping for each safeguard
- Implementation status tracking table
- [TODO] markers for implementation dates

#### 9100_Anhang_Asset_Type_Mapping.md
**Purpose**: Asset type cross-reference
**Content Structure**:
- Devices asset type: Controls and safeguards
- Applications asset type: Controls and safeguards
- Network asset type: Controls and safeguards
- Data asset type: Controls and safeguards
- Users asset type: Controls and safeguards
- NetBox integration for asset tracking

#### 9200_Anhang_Security_Functions_Mapping.md
**Purpose**: Security function cross-reference
**Content Structure**:
- Identify function: Controls and safeguards
- Protect function: Controls and safeguards
- Detect function: Controls and safeguards
- Respond function: Controls and safeguards
- Recover function: Controls and safeguards
- Mapping to NIST Cybersecurity Framework

#### 9900_Glossar_und_Abkuerzungen.md
**Purpose**: Terminology and abbreviations
**Content Structure**:
- CIS Controls-specific terminology
- Technical abbreviations
- Asset type definitions
- Security function definitions
- Implementation Group definitions


## Placeholder Strategy

The CIS Controls templates use the existing placeholder system with some CIS-specific extensions. All placeholders follow the `{{ source.field }}` syntax.

### Meta Placeholders (Organization-wide)

Meta placeholders provide organization-specific information that applies across all templates.

#### Organization Information
```markdown
**Organization:** {{ meta.organization.name }}
**Industry:** {{ meta.organization.industry }}
**Size:** {{ meta.organization.employee_count }} employees
**Selected Implementation Group:** {{ meta.cis.implementation_group }}
```

#### Leadership and Governance
```markdown
**Chief Information Security Officer (CISO):** {{ meta.ciso.name }}
**Email:** {{ meta.ciso.email }}
**Phone:** {{ meta.ciso.phone }}

**Chief Information Officer (CIO):** {{ meta.cio.name }}
**Email:** {{ meta.cio.email }}

**CIS Controls Program Manager:** {{ meta.cis.program_manager.name }}
**Email:** {{ meta.cis.program_manager.email }}
```

#### Document Control
```markdown
**Document Owner:** {{ meta.document.owner }}
**Document Approver:** {{ meta.document.approver }}
**Version:** {{ meta.document.version }}
**Last Review Date:** {{ meta.document.last_review }}
**Next Review Date:** {{ meta.document.next_review }}
```


### NetBox Placeholders (Infrastructure Data)

NetBox placeholders provide dynamic infrastructure and asset information from the NetBox DCIM/IPAM system.

#### Asset Inventory (Control 1 & 2)
```markdown
**Total Devices:** {{ netbox.devices.count }}
**Active Devices:** {{ netbox.devices.active_count }}
**Device Types:** {{ netbox.devices.types }}

**Primary Site:** {{ netbox.site.primary.name }}
**Location:** {{ netbox.site.primary.location }}
**Data Center:** {{ netbox.site.primary.facility }}
```

#### Network Infrastructure (Control 12 & 13)
```markdown
**Core Switch:** {{ netbox.device.core_switch.name }}
**Model:** {{ netbox.device.core_switch.model }}
**Management IP:** {{ netbox.device.core_switch.primary_ip }}

**Management VLAN:** {{ netbox.vlan.management.vid }}
**Server VLAN:** {{ netbox.vlan.server.vid }}
**User VLAN:** {{ netbox.vlan.user.vid }}

**Firewall:** {{ netbox.device.firewall.name }}
**Firewall IP:** {{ netbox.device.firewall.primary_ip }}
```

#### Security Tools (Control 7, 8, 10, 13)
```markdown
**Vulnerability Scanner:** {{ netbox.device.vuln_scanner.name }}
**SIEM System:** {{ netbox.device.siem.name }}
**Backup Server:** {{ netbox.device.backup_server.name }}
**EDR Platform:** {{ netbox.device.edr_server.name }}
```


### CIS-Specific Placeholders (Optional Extension)

For CIS Controls-specific data that doesn't fit into meta or netbox categories, optional CIS-specific placeholders can be introduced.

#### Implementation Status
```markdown
**IG1 Safeguards Implemented:** {{ cis.ig1.implemented_count }} / {{ cis.ig1.total_count }}
**IG1 Implementation Percentage:** {{ cis.ig1.percentage }}%

**IG2 Safeguards Implemented:** {{ cis.ig2.implemented_count }} / {{ cis.ig2.total_count }}
**IG2 Implementation Percentage:** {{ cis.ig2.percentage }}%

**IG3 Safeguards Implemented:** {{ cis.ig3.implemented_count }} / {{ cis.ig3.total_count }}
**IG3 Implementation Percentage:** {{ cis.ig3.percentage }}%
```

#### Control-Specific Status
```markdown
**Control 1 Status:** {{ cis.control_01.status }}
**Control 1 Completion:** {{ cis.control_01.completion_percentage }}%
**Control 1 Last Assessment:** {{ cis.control_01.last_assessment_date }}
```

#### Assessment and Audit
```markdown
**Last CIS Assessment Date:** {{ cis.assessment.last_date }}
**Next CIS Assessment Date:** {{ cis.assessment.next_date }}
**Assessment Tool:** {{ cis.assessment.tool }}
**Overall Maturity Level:** {{ cis.assessment.maturity_level }}
```

**Note**: CIS-specific placeholders are optional and would require extending the data source adapter system. Initial implementation can use meta and netbox placeholders exclusively, with [TODO] markers for CIS-specific data.


### Placeholder Usage Examples

#### Example 1: Control 1 Template Header
```markdown
# Control 1: Inventar und Kontrolle von Unternehmensassets

**Organisation:** {{ meta.organization.name }}
**Implementation Group:** {{ meta.cis.implementation_group }}
**Verantwortlicher:** {{ meta.cis.control_01.owner }}

## Übersicht

Dieses Dokument beschreibt die Implementierung von CIS Control 1 für {{ meta.organization.name }}.

**Aktuelle Asset-Statistik:**
- Gesamtanzahl Geräte: {{ netbox.devices.count }}
- Aktive Geräte: {{ netbox.devices.active_count }}
- Letzte Inventarisierung: {{ meta.cis.control_01.last_inventory_date }}
```

#### Example 2: Control 12 Network Infrastructure
```markdown
# Control 12: Netzwerkinfrastruktur Management

## Netzwerktopologie

**Primärer Standort:** {{ netbox.site.primary.name }}
**Core Switch:** {{ netbox.device.core_switch.name }} ({{ netbox.device.core_switch.model }})
**Management IP:** {{ netbox.device.core_switch.primary_ip }}

**VLAN-Segmentierung:**
- Management VLAN: {{ netbox.vlan.management.vid }}
- Server VLAN: {{ netbox.vlan.server.vid }}
- User VLAN: {{ netbox.vlan.user.vid }}
- DMZ VLAN: {{ netbox.vlan.dmz.vid }}

**Firewall:** {{ netbox.device.firewall.name }}
**Firewall Management IP:** {{ netbox.device.firewall.primary_ip }}
```

#### Example 3: [TODO] Markers for Customization
```markdown
## Safeguard 1.1: Establish and Maintain Detailed Enterprise Asset Inventory

[TODO: Liste Sie hier alle autorisierten Asset-Typen für Ihre Organisation auf]

**Autorisierte Asset-Typen:**
- Laptops (Windows, macOS, Linux)
- Desktop-Computer
- Server (physisch und virtuell)
- Netzwerkgeräte (Switches, Router, Firewalls)
- Mobile Geräte (Smartphones, Tablets)
- [TODO: Weitere organisationsspezifische Asset-Typen hinzufügen]

**Asset-Inventarisierungstool:** [TODO: Name des verwendeten Tools eintragen]
**Inventarisierungsfrequenz:** [TODO: Frequenz definieren, z.B. täglich, wöchentlich]
```


## README Structure for CIS Controls

The README.md file in each CIS Controls template directory (templates/de/cis-controls/README.md and templates/en/cis-controls/README.md) provides comprehensive guidance for using the templates.

### README Sections

#### 1. Introduction
- Purpose of CIS Controls templates
- Target audience (security teams, compliance officers, auditors)
- Relationship to CIS Controls v8 framework
- Benefits of using these templates

#### 2. Template Organization
- Overview of template numbering scheme (0010-9900)
- Foundation templates (0010-0030)
- Control templates (0100-1800)
- Appendix templates (9000-9900)
- Template file naming conventions

#### 3. Implementation Groups Guide
- **IG1 (Essential Cyber Hygiene)**:
  - Characteristics: Small organizations, limited IT resources
  - Safeguard count: 56 safeguards
  - Recommended for: Organizations with <100 employees
  - Focus: Basic security controls, foundational protections
  
- **IG2 (Intermediate Security)**:
  - Characteristics: Medium organizations, dedicated IT staff
  - Safeguard count: 74 additional safeguards (130 total)
  - Recommended for: Organizations with 100-1000 employees
  - Focus: Enhanced monitoring, centralized management
  
- **IG3 (Advanced Security)**:
  - Characteristics: Large organizations, dedicated security teams
  - Safeguard count: 23 additional safeguards (153 total)
  - Recommended for: Organizations with >1000 employees or high-risk profiles
  - Focus: Advanced threat detection, security automation

#### 4. Placeholder Usage
- Meta placeholders for organization information
- NetBox placeholders for infrastructure data
- CIS-specific placeholders (optional)
- Examples of placeholder usage in templates
- How to configure metadata.yaml for CIS Controls


#### 5. CIS Controls v8 Compliance Mapping
- Complete list of 18 Controls with descriptions
- Safeguard count per control
- IG level requirements per control
- Asset type coverage per control
- Security function mapping per control

**Example Compliance Table:**

| Control | Title | Safeguards | IG1 | IG2 | IG3 | Asset Types |
|---------|-------|------------|-----|-----|-----|-------------|
| 1 | Inventory and Control of Enterprise Assets | 5 | ✓ | ✓ | ✓ | Devices |
| 2 | Inventory and Control of Software Assets | 7 | ✓ | ✓ | ✓ | Applications |
| 3 | Data Protection | 14 | ✓ | ✓ | ✓ | Data |
| 4 | Secure Configuration | 12 | ✓ | ✓ | ✓ | Devices, Applications |
| 5 | Account Management | 6 | ✓ | ✓ | ✓ | Users |
| 6 | Access Control Management | 8 | ✓ | ✓ | ✓ | Users, Devices, Applications |
| 7 | Continuous Vulnerability Management | 7 | ✓ | ✓ | ✓ | Devices, Applications |
| 8 | Audit Log Management | 12 | ✓ | ✓ | ✓ | Network, Devices, Applications |
| 9 | Email and Web Browser Protections | 7 | ✓ | ✓ | ✓ | Applications |
| 10 | Malware Defenses | 7 | ✓ | ✓ | ✓ | Devices, Applications |
| 11 | Data Recovery | 5 | ✓ | ✓ | ✓ | Data |
| 12 | Network Infrastructure Management | 8 | ✓ | ✓ | ✓ | Network, Devices |
| 13 | Network Monitoring and Defense | 11 | ✓ | ✓ | ✓ | Network |
| 14 | Security Awareness and Skills Training | 9 | ✓ | ✓ | ✓ | Users |
| 15 | Service Provider Management | 7 | ✓ | ✓ | ✓ | N/A |
| 16 | Application Software Security | 14 | - | ✓ | ✓ | Applications |
| 17 | Incident Response Management | 9 | ✓ | ✓ | ✓ | N/A |
| 18 | Penetration Testing | 5 | - | ✓ | ✓ | Network, Applications |

#### 6. Cross-Framework Mapping
- Mapping to ISO 27001:2022 Annex A controls
- Mapping to NIST Cybersecurity Framework
- Mapping to NIST SP 800-53
- Mapping to BSI IT-Grundschutz
- Mapping to ITIL v4 practices

#### 7. Customization Best Practices
- How to adapt templates for your organization
- Using [TODO] markers effectively
- Maintaining template updates
- Version control recommendations
- Review and approval workflows


#### 8. Implementation Roadmap
- Phase 1: IG1 Implementation (Months 1-6)
  - Controls 1-5: Foundation controls
  - Controls 6-11: Core security controls
  - Controls 12-15: Infrastructure and process controls
  
- Phase 2: IG2 Enhancement (Months 7-12)
  - Enhanced monitoring and detection
  - Centralized management
  - Advanced logging and analysis
  - Application security (Control 16)
  - Penetration testing (Control 18)
  
- Phase 3: IG3 Advanced Controls (Months 13-18)
  - Security automation
  - Advanced threat detection
  - Behavioral analytics
  - Continuous improvement

#### 9. Assessment and Measurement
- Self-assessment questionnaire
- Maturity model (Initial, Developing, Defined, Managed, Optimizing)
- Key performance indicators (KPIs) per control
- Metrics collection and reporting
- Continuous monitoring approach

#### 10. Tools and Resources
- CIS Controls Assessment Tool (CIS-CAT)
- Asset inventory tools
- Vulnerability scanners
- SIEM platforms
- Configuration management tools
- Recommended vendor solutions by control

#### 11. Frequently Asked Questions (FAQ)
- How to select the appropriate Implementation Group?
- Can we implement controls out of order?
- How often should we reassess our CIS Controls implementation?
- What if we can't implement all IG1 safeguards?
- How do CIS Controls relate to compliance requirements (GDPR, PCI DSS, HIPAA)?

#### 12. References and Resources
- CIS Controls v8 official documentation
- CIS Controls v8 Community Defense Model
- CIS Benchmarks
- CIS Hardened Images
- Training and certification resources
- Community forums and support


## Implementation Considerations

### No Template Files in This Phase

**Important**: This design document defines the structure for CIS Controls v8 templates but does NOT include actual template file creation. Template implementation will occur in a future phase after:

1. Successful completion of BCM, ISMS, and BSI Grundschutz templates
2. Validation of the template system architecture
3. User feedback on existing template types
4. Resource allocation for CIS Controls implementation

### Integration with Existing System

The CIS Controls templates will integrate seamlessly with the existing handbook generator system:

- **CLI Integration**: Add `cis-controls` as a valid template type
- **Directory Structure**: Follow established pattern (templates/{language}/cis-controls/)
- **Placeholder System**: Use existing meta and netbox placeholder infrastructure
- **Output Generation**: Generate handbooks using existing output generator
- **Validation**: Apply existing template validation rules

### Backward Compatibility

Adding CIS Controls templates will not affect existing template types:
- IT-Operation templates remain unchanged
- BCM templates remain unchanged
- ISMS templates remain unchanged
- BSI Grundschutz templates remain unchanged


## CIS Controls v8 Safeguard Summary

### Safeguard Distribution by Implementation Group

| Implementation Group | Safeguard Count | Cumulative Total | Target Organizations |
|---------------------|-----------------|------------------|---------------------|
| IG1 | 56 | 56 | Small organizations, limited IT resources |
| IG2 | 74 | 130 | Medium organizations, dedicated IT staff |
| IG3 | 23 | 153 | Large organizations, dedicated security teams |

### Safeguard Distribution by Control

| Control | Title | Total Safeguards | IG1 | IG2 | IG3 |
|---------|-------|------------------|-----|-----|-----|
| 1 | Inventory and Control of Enterprise Assets | 5 | 2 | 2 | 1 |
| 2 | Inventory and Control of Software Assets | 7 | 4 | 2 | 1 |
| 3 | Data Protection | 14 | 6 | 5 | 3 |
| 4 | Secure Configuration of Enterprise Assets and Software | 12 | 7 | 4 | 1 |
| 5 | Account Management | 6 | 4 | 1 | 1 |
| 6 | Access Control Management | 8 | 5 | 2 | 1 |
| 7 | Continuous Vulnerability Management | 7 | 4 | 2 | 1 |
| 8 | Audit Log Management | 12 | 5 | 5 | 2 |
| 9 | Email and Web Browser Protections | 7 | 3 | 3 | 1 |
| 10 | Malware Defenses | 7 | 2 | 3 | 2 |
| 11 | Data Recovery | 5 | 3 | 1 | 1 |
| 12 | Network Infrastructure Management | 8 | 4 | 3 | 1 |
| 13 | Network Monitoring and Defense | 11 | 3 | 6 | 2 |
| 14 | Security Awareness and Skills Training | 9 | 4 | 4 | 1 |
| 15 | Service Provider Management | 7 | 2 | 4 | 1 |
| 16 | Application Software Security | 14 | 0 | 11 | 3 |
| 17 | Incident Response Management | 9 | 2 | 6 | 1 |
| 18 | Penetration Testing | 5 | 0 | 4 | 1 |
| **Total** | | **153** | **56** | **74** | **23** |


## Asset Type Coverage

CIS Controls v8 organizes safeguards around five asset types:

### Devices
**Definition**: End-user devices (laptops, desktops, mobile devices) and network devices (routers, switches, firewalls)

**Covered by Controls**: 1, 4, 7, 10, 12

**Key Safeguards**:
- Maintain detailed asset inventory
- Secure device configuration
- Vulnerability management
- Malware defenses
- Network device hardening

### Applications
**Definition**: Software applications including operating systems, business applications, and custom software

**Covered by Controls**: 2, 4, 7, 9, 10, 16

**Key Safeguards**:
- Software inventory and control
- Secure application configuration
- Application vulnerability management
- Email and web browser protections
- Secure software development

### Network
**Definition**: Network infrastructure including physical and virtual networks, network segments, and network services

**Covered by Controls**: 8, 12, 13, 18

**Key Safeguards**:
- Network logging and monitoring
- Network segmentation
- Network access control
- Intrusion detection and prevention
- Network penetration testing

### Data
**Definition**: Information stored, processed, or transmitted by the organization

**Covered by Controls**: 3, 11

**Key Safeguards**:
- Data classification and handling
- Data encryption
- Data loss prevention
- Backup and recovery
- Secure data disposal

### Users
**Definition**: Individuals with access to organizational assets

**Covered by Controls**: 5, 6, 14

**Key Safeguards**:
- Account lifecycle management
- Access control and authentication
- Multi-factor authentication
- Security awareness training
- Role-based access control


## Security Function Mapping

CIS Controls v8 aligns with the NIST Cybersecurity Framework's five security functions:

### Identify
**Purpose**: Develop organizational understanding to manage cybersecurity risk

**Covered by Controls**: 1, 2, 4, 15

**Key Activities**:
- Asset inventory and management
- Software inventory and management
- Configuration management
- Third-party risk assessment

### Protect
**Purpose**: Develop and implement appropriate safeguards

**Covered by Controls**: 3, 4, 5, 6, 7, 9, 10, 11, 12, 14, 16

**Key Activities**:
- Data protection and encryption
- Secure configuration
- Access control and authentication
- Vulnerability management
- Malware defenses
- Security awareness training
- Secure software development

### Detect
**Purpose**: Develop and implement activities to identify cybersecurity events

**Covered by Controls**: 7, 8, 13

**Key Activities**:
- Vulnerability scanning
- Audit log management
- Network monitoring
- Anomaly detection
- Security event correlation

### Respond
**Purpose**: Develop and implement activities to take action regarding detected cybersecurity incidents

**Covered by Controls**: 17

**Key Activities**:
- Incident response planning
- Incident detection and analysis
- Incident containment and eradication
- Incident communication
- Post-incident review

### Recover
**Purpose**: Develop and implement activities to maintain resilience and restore capabilities

**Covered by Controls**: 11, 17

**Key Activities**:
- Data backup and recovery
- Disaster recovery planning
- Business continuity
- Recovery testing
- Lessons learned integration


## Cross-Framework Alignment

### CIS Controls v8 to ISO 27001:2022 Annex A Mapping

| CIS Control | ISO 27001:2022 Annex A Controls |
|-------------|--------------------------------|
| 1 - Enterprise Asset Inventory | A.5.9, A.8.1, A.8.2 |
| 2 - Software Asset Inventory | A.5.9, A.8.1, A.8.2 |
| 3 - Data Protection | A.5.33, A.5.34, A.8.11, A.8.24 |
| 4 - Secure Configuration | A.8.9, A.8.19 |
| 5 - Account Management | A.5.15, A.5.16, A.5.17, A.5.18 |
| 6 - Access Control Management | A.5.15, A.5.16, A.5.17, A.5.18, A.8.5 |
| 7 - Vulnerability Management | A.8.8, A.8.19 |
| 8 - Audit Log Management | A.8.15, A.8.16 |
| 9 - Email and Web Browser Protections | A.8.23 |
| 10 - Malware Defenses | A.8.7 |
| 11 - Data Recovery | A.8.13, A.8.14 |
| 12 - Network Infrastructure Management | A.8.20, A.8.21, A.8.22 |
| 13 - Network Monitoring and Defense | A.8.16, A.8.25 |
| 14 - Security Awareness Training | A.6.3 |
| 15 - Service Provider Management | A.5.19, A.5.20, A.5.21, A.5.22 |
| 16 - Application Software Security | A.8.25, A.8.26, A.8.27, A.8.28, A.8.29, A.8.30, A.8.31, A.8.32 |
| 17 - Incident Response Management | A.5.24, A.5.25, A.5.26, A.5.27, A.5.28 |
| 18 - Penetration Testing | A.8.8, A.8.29 |

### CIS Controls v8 to NIST CSF Mapping

| CIS Control | NIST CSF Categories |
|-------------|---------------------|
| 1 - Enterprise Asset Inventory | ID.AM-1, ID.AM-2 |
| 2 - Software Asset Inventory | ID.AM-2, ID.AM-5 |
| 3 - Data Protection | PR.DS-1, PR.DS-2, PR.DS-5 |
| 4 - Secure Configuration | PR.IP-1, PR.PT-3 |
| 5 - Account Management | PR.AC-1, PR.AC-4 |
| 6 - Access Control Management | PR.AC-1, PR.AC-3, PR.AC-4, PR.AC-7 |
| 7 - Vulnerability Management | ID.RA-1, DE.CM-8, RS.MI-3 |
| 8 - Audit Log Management | PR.PT-1, DE.AE-3, DE.CM-1, DE.CM-7 |
| 9 - Email and Web Browser Protections | PR.PT-2 |
| 10 - Malware Defenses | DE.CM-4, PR.DS-8 |
| 11 - Data Recovery | PR.IP-4, RC.RP-1 |
| 12 - Network Infrastructure Management | PR.AC-5, PR.PT-4 |
| 13 - Network Monitoring and Defense | DE.AE-1, DE.CM-1, DE.CM-7 |
| 14 - Security Awareness Training | PR.AT-1, PR.AT-2 |
| 15 - Service Provider Management | ID.SC-1, ID.SC-2, ID.SC-3, ID.SC-4 |
| 16 - Application Software Security | PR.DS-6, PR.IP-2 |
| 17 - Incident Response Management | RS.RP-1, RS.CO-1, RS.AN-1, RS.MI-1 |
| 18 - Penetration Testing | ID.RA-3, DE.DP-2 |


## Future Implementation Roadmap

### Phase 1: Design and Planning (Current Phase)
- ✅ Document CIS Controls v8 structure
- ✅ Define template numbering scheme
- ✅ Design placeholder strategy
- ✅ Define README structure
- ✅ Create design document

### Phase 2: Template Creation (Future)
- Create 25 German templates (0010-9900)
- Create 25 English templates (0010-9900)
- Implement RACI matrices for governance
- Add framework cross-references
- Include [TODO] markers for customization

### Phase 3: Integration and Testing (Future)
- Extend CLI to support `--template cis-controls`
- Add CIS Controls to template discovery
- Create unit tests for CIS Controls templates
- Create property tests for CIS Controls validation
- Generate example handbooks

### Phase 4: Documentation and Release (Future)
- Create comprehensive README files (de/en)
- Update main project documentation
- Add CIS Controls to framework mapping document
- Create migration guide for existing users
- Publish release notes

## Maintenance and Updates

### CIS Controls Version Tracking
- **Current Version**: CIS Controls v8 (May 2021)
- **Previous Version**: CIS Controls v7.1 (April 2019)
- **Update Frequency**: Major versions every 2-3 years
- **Template Review**: Annual review recommended

### Template Maintenance Strategy
- Monitor CIS Controls updates and amendments
- Review templates when new CIS Controls versions are released
- Incorporate user feedback and lessons learned
- Maintain alignment with other frameworks (ISO 27001, NIST CSF)
- Update cross-framework mappings as frameworks evolve


## References

### CIS Controls v8 Official Resources
- Center for Internet Security. (2021). *CIS Controls v8*. Retrieved from https://www.cisecurity.org/controls/v8
- Center for Internet Security. (2021). *CIS Controls v8 Implementation Guide*. CIS.
- Center for Internet Security. (2021). *CIS Controls v8 Community Defense Model*. CIS.
- Center for Internet Security. (2021). *CIS Controls v8 Measures and Metrics*. CIS.

### Related Frameworks
- ISO/IEC. (2022). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection*. International Organization for Standardization.
- NIST. (2018). *Framework for Improving Critical Infrastructure Cybersecurity, Version 1.1*. National Institute of Standards and Technology.
- NIST. (2020). *NIST SP 800-53 Rev. 5: Security and Privacy Controls*. National Institute of Standards and Technology.

### Additional Resources
- CIS Benchmarks: https://www.cisecurity.org/cis-benchmarks/
- CIS Hardened Images: https://www.cisecurity.org/cis-hardened-images/
- CIS-CAT Pro Assessment Tool: https://www.cisecurity.org/cybersecurity-tools/cis-cat-pro/
- CIS Controls Self Assessment Tool (CIS CSAT): https://www.cisecurity.org/controls/cis-controls-self-assessment-tool/

## Document Information

**Document Title**: CIS Controls v8 Template Structure Design  
**Document Version**: 1.0  
**Document Date**: 2024-02-03  
**Document Owner**: Template System Extension Project  
**Document Status**: Design Complete - Implementation Pending  

**Review Schedule**:
- Next Review Date: Upon CIS Controls v8.1 release or 2025-02-03 (whichever comes first)
- Review Frequency: Annual or upon major framework updates

**Change History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2024-02-03 | Template System Extension Project | Initial design document created |

---

**Note**: This is a design-only document. No template files have been created as part of this phase. Implementation will occur in a future phase after successful completion and validation of BCM, ISMS, and BSI Grundschutz templates.

