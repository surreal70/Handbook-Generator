# Framework Mapping Documentation

**Document Version:** 1.0  
**Last Updated:** 2026-02-18  
**Maintained By:** Documentation Team

---

## Overview

This document provides comprehensive mapping documentation for all frameworks supported by the Handbook Generator. It consolidates information from individual framework mapping files and provides cross-framework references.

The Handbook Generator currently supports **23 frameworks** across multiple domains, with templates available in both English and German.

## Purpose

This documentation serves to:
- Provide a central reference for all framework mappings
- Document how templates map to framework requirements
- Enable cross-framework compliance and integration
- Support audit and compliance activities
- Guide template selection and customization

## Framework Categories

### 1. IT Operations & Service Management

#### ITIL v4 / ISO 20000-1:2018 / COBIT 2019 (IT-Operation)

**Framework Mapping File:** [templates/en/it-operation/9999_Framework_Mapping.md](../templates/en/it-operation/9999_Framework_Mapping.md)

**Standards Covered:**
- ITIL v4 (Information Technology Infrastructure Library)
- ISO/IEC 20000-1:2018 (IT Service Management)
- COBIT 2019 (Control Objectives for Information and Related Technologies)

**Template Range:** 0010-0999  
**Total Templates:** ~60 per language

**Key Mappings:**
- Service Strategy → Templates 0010-0099
- Service Design → Templates 0100-0199
- Service Transition → Templates 0200-0299
- Service Operation → Templates 0300-0399
- Continual Service Improvement → Templates 0400-0499
- COBIT Governance → Templates 0500-0599

**ITIL v4 Practice Coverage:**
- Incident Management: Restore normal service operation as quickly as possible
- Problem Management: Reduce likelihood and impact of incidents by identifying root causes
- Change Management (Change Enablement): Ensure changes are assessed, authorized, and managed
- Monitoring and Event Management: Systematic observation of services and service components

**COBIT 2019 Domain Coverage:**
- **APO** (Align, Plan and Organize): Strategic alignment and planning
- **BAI** (Build, Acquire and Implement): Solution delivery and implementation
- **DSS** (Deliver, Service and Support): Operational service delivery and support
- **MEA** (Monitor, Evaluate and Assess): Performance monitoring and compliance
- **EDM** (Evaluate, Direct and Monitor): Governance framework and oversight

**ISO/IEC 20000-1:2018 Clause Alignment:**
- Clause 4: Context of the organization
- Clause 5: Leadership
- Clause 6: Planning
- Clause 7: Support
- Clause 8: Service management system operation
- Clause 9: Performance evaluation
- Clause 10: Improvement

**Primary Use Cases:**
- IT service management implementation
- Service catalog documentation
- ITSM process documentation
- IT governance frameworks

---

### 2. Information Security Management

#### ISO/IEC 27001:2022 (ISMS)

**Framework Mapping File:** [templates/en/isms/9999_Framework_Mapping.md](../templates/en/isms/9999_Framework_Mapping.md)

**Standards Covered:**
- ISO/IEC 27001:2022 (including Amendment 1:2024)
- ISO/IEC 27002:2022 (Annex A Controls)

**Template Range:** 0010-0999  
**Total Templates:** ~50 per language

**Key Mappings:**
- Context of Organization → Templates 0010-0040
- Leadership → Templates 0050-0080
- Planning → Templates 0090-0150
- Support → Templates 0160-0200
- Operation → Templates 0210-0400
- Performance Evaluation → Templates 0410-0450
- Improvement → Templates 0460-0499
- Annex A Controls → Templates 0500-0999

**Primary Use Cases:**
- ISO 27001 certification
- Information security management system
- Security policy framework
- Risk management

#### BSI Grundschutz

**Framework Mapping File:** [templates/en/bsi-grundschutz/9999_Framework_Mapping.md](../templates/en/bsi-grundschutz/9999_Framework_Mapping.md)

**Standards Covered:**
- BSI Standard 200-1 (ISMS)
- BSI Standard 200-2 (IT-Grundschutz Methodology)
- BSI Standard 200-3 (Risk Analysis)
- IT-Grundschutz Compendium

**Template Range:** 0010-0999  
**Total Templates:** ~80 per language

**Key Mappings:**
- ISMS Organization → Templates 0010-0099
- Security Policies → Templates 0200-0599
- Awareness & Training → Templates 0600-0699
- Appendices → Templates 0700-0799

**Primary Use Cases:**
- German government compliance
- BSI certification
- IT-Grundschutz implementation
- Structured security approach

#### CIS Controls v8.1

**Framework Mapping File:** [templates/en/cis-controls/9999_Framework_Mapping.md](../templates/en/cis-controls/9999_Framework_Mapping.md)

**Standards Covered:**
- CIS Controls v8.1
- CIS Benchmarks (various platforms)

**Template Range:** 0010-0999  
**Total Templates:** ~40 per language

**Key Mappings:**
- Framework Overview → Templates 0010-0099
- Operating Systems → Templates 0100-0199
- Applications → Templates 0200-0299
- Network Devices → Templates 0300-0399
- Cloud Services → Templates 0400-0499
- Databases → Templates 0500-0599

**Primary Use Cases:**
- System hardening
- Security baselines
- Configuration management
- Compliance validation

#### NIST SP 800-53 Rev. 5

**Framework Mapping File:** [templates/en/nist-800-53/9999_Framework_Mapping.md](../templates/en/nist-800-53/9999_Framework_Mapping.md)

**Standards Covered:**
- NIST SP 800-53 Rev. 5 (Security and Privacy Controls)
- NIST SP 800-53B (Control Baselines)

**Template Range:** 0010-0999  
**Total Templates:** ~45 per language

**Key Mappings:**
- Control Families (AC, AT, AU, etc.) → Templates organized by family
- Low/Moderate/High Baselines → Documented in templates
- Privacy Controls → Integrated throughout

**Primary Use Cases:**
- Federal compliance (FedRAMP, FISMA)
- Security control implementation
- Risk management framework
- Privacy compliance

#### NIST Cybersecurity Framework 2.0

**Framework Mapping File:** [templates/en/nist-csf/9999_Framework_Mapping.md](../templates/en/nist-csf/9999_Framework_Mapping.md)

**Standards Covered:**
- NIST CSF 2.0 (Cybersecurity Framework)

**Template Range:** 0010-0699  
**Total Templates:** ~35 per language

**Key Mappings:**
- Govern (GV) → Templates 0100-0199
- Identify (ID) → Templates 0200-0299
- Protect (PR) → Templates 0300-0399
- Detect (DE) → Templates 0400-0499
- Respond (RS) → Templates 0500-0599
- Recover (RC) → Templates 0600-0699

**Primary Use Cases:**
- Cybersecurity program development
- Risk assessment
- Maturity assessment
- Framework alignment

---

### 3. Business Continuity & Resilience

#### ISO 22301:2019 (BCM)

**Framework Mapping File:** [templates/en/bcm/9999_Framework_Mapping.md](../templates/en/bcm/9999_Framework_Mapping.md)

**Standards Covered:**
- ISO 22301:2019 (Business Continuity Management)
- BSI Standard 100-4 (BCM)

**Template Range:** 0010-0299  
**Total Templates:** ~30 per language

**Key Mappings:**
- BCM Framework → Templates 0010-0050
- Business Impact Analysis → Templates 0060-0090
- BCM Strategy → Templates 0100-0110
- BCM Plans → Templates 0120-0210
- Testing & Maintenance → Templates 0220-0270
- Appendices → Templates 0280-0299

**Primary Use Cases:**
- Business continuity planning
- Disaster recovery
- Crisis management
- Resilience programs

---

### 4. Data Protection & Privacy

#### GDPR (EU General Data Protection Regulation)

**Framework Mapping File:** [templates/en/gdpr/9999_Framework_Mapping.md](../templates/en/gdpr/9999_Framework_Mapping.md)

**Standards Covered:**
- EU GDPR (Regulation 2016/679)
- National data protection laws

**Template Range:** 0010-0799  
**Total Templates:** ~40 per language

**Key Mappings:**
- Principles & Lawfulness → Templates 0100-0199
- Rights of Data Subjects → Templates 0200-0299
- Controller & Processor → Templates 0300-0399
- Data Protection Officer → Templates 0400-0499
- Data Transfers → Templates 0500-0599
- Supervisory Authority → Templates 0600-0699
- Appendices → Templates 0700-0799

**Primary Use Cases:**
- GDPR compliance
- Privacy program
- Data protection impact assessments
- Records of processing activities

#### HIPAA (Health Insurance Portability and Accountability Act)

**Framework Mapping File:** [templates/en/hipaa/9999_Framework_Mapping.md](../templates/en/hipaa/9999_Framework_Mapping.md)

**Standards Covered:**
- HIPAA Privacy Rule
- HIPAA Security Rule
- HIPAA Breach Notification Rule

**Template Range:** 0010-0699  
**Total Templates:** ~35 per language

**Key Mappings:**
- Privacy Rule → Templates 0100-0299
- Security Rule → Templates 0300-0599
- Breach Notification → Templates 0600-0699

**Primary Use Cases:**
- Healthcare compliance
- Protected health information (PHI)
- Business associate agreements
- Security risk analysis

---

### 5. Financial & Audit Frameworks

#### SOC 1 (SSAE 18 / ISAE 3402)

**Framework Mapping File:** [templates/en/soc1/9999_Framework_Mapping.md](../templates/en/soc1/9999_Framework_Mapping.md)

**Standards Covered:**
- SSAE 18 (US)
- ISAE 3402 (International)

**Template Range:** 0010-0499  
**Total Templates:** ~25 per language

**Key Mappings:**
- System Description → Templates 0010-0099
- Control Environment → Templates 0100-0199
- Control Activities → Templates 0200-0399
- Monitoring → Templates 0400-0499

**Primary Use Cases:**
- Service organization controls
- Financial reporting controls
- Outsourcing assurance
- Third-party attestation

#### TSC (Trust Services Criteria - SOC 2)

**Framework Mapping File:** [templates/en/tsc/9999_Framework_Mapping.md](../templates/en/tsc/9999_Framework_Mapping.md)

**Standards Covered:**
- AICPA Trust Services Criteria
- SOC 2 Type I / Type II

**Template Range:** 0010-0499  
**Total Templates:** ~25 per language

**Key Mappings:**
- Common Criteria (CC) → Templates 0100-0199
- Availability (A) → Templates 0200-0239
- Processing Integrity (PI) → Templates 0240-0279
- Confidentiality (C) → Templates 0280-0319
- Privacy (P) → Templates 0320-0399
- Control Matrix → Templates 0400-0499

**Primary Use Cases:**
- SOC 2 certification
- Trust services
- Cloud service assurance
- Vendor assessments

#### IDW PS 951

**Framework Mapping File:** [templates/en/idw-ps-951/9999_Framework_Mapping.md](../templates/en/idw-ps-951/9999_Framework_Mapping.md)

**Standards Covered:**
- IDW PS 951 (German IT audit standard)

**Template Range:** 0010-0999  
**Total Templates:** ~50 per language

**Key Mappings:**
- Audit Framework → Templates 0010-0099
- IT General Controls → Templates 0100-0399
- Application Controls → Templates 0400-0699
- Audit Documentation → Templates 0700-0999

**Primary Use Cases:**
- German IT audits
- Financial statement audits
- IT control assessments
- Compliance documentation

#### COSO Internal Control Framework

**Framework Mapping File:** [templates/en/coso/9999_Framework_Mapping.md](../templates/en/coso/9999_Framework_Mapping.md)

**Standards Covered:**
- COSO Internal Control - Integrated Framework
- COSO ERM Framework

**Template Range:** 0010-0599  
**Total Templates:** ~30 per language

**Key Mappings:**
- Control Environment → Templates 0100-0199
- Risk Assessment → Templates 0200-0299
- Control Activities → Templates 0300-0399
- Information & Communication → Templates 0400-0499
- Monitoring Activities → Templates 0500-0599

**Primary Use Cases:**
- Internal control systems
- Enterprise risk management
- SOX compliance
- Governance frameworks

---

### 6. Industry-Specific Compliance

#### PCI DSS (Payment Card Industry Data Security Standard)

**Framework Mapping File:** [templates/en/pci-dss/9999_Framework_Mapping.md](../templates/en/pci-dss/9999_Framework_Mapping.md)

**Standards Covered:**
- PCI DSS v4.0

**Template Range:** 0010-0999  
**Total Templates:** ~40 per language

**Key Mappings:**
- Requirements 1-12 → Templates organized by requirement
- Appendices → Templates 0900-0999

**Primary Use Cases:**
- Payment card processing
- Cardholder data protection
- PCI compliance
- Merchant/service provider certification

#### TISAX (Trusted Information Security Assessment Exchange)

**Framework Mapping File:** [templates/en/tisax/9999_Framework_Mapping.md](../templates/en/tisax/9999_Framework_Mapping.md)

**Standards Covered:**
- TISAX (based on ISO 27001 + VDA ISA)
- VDA Information Security Assessment

**Template Range:** 0010-0999  
**Total Templates:** ~45 per language

**Key Mappings:**
- Information Security → Templates 0100-0499
- Prototype Protection → Templates 0500-0699
- Data Protection → Templates 0700-0899

**Primary Use Cases:**
- Automotive industry compliance
- Supplier assessments
- Information security in supply chain
- VDA requirements

#### DORA (Digital Operational Resilience Act)

**Framework Mapping File:** [templates/en/dora/9999_Framework_Mapping.md](../templates/en/dora/9999_Framework_Mapping.md)

**Standards Covered:**
- EU Regulation 2022/2554 (DORA)

**Template Range:** 0010-0599  
**Total Templates:** ~30 per language

**Key Mappings:**
- ICT Risk Management → Templates 0100-0199
- ICT Incident Management → Templates 0200-0299
- Digital Resilience Testing → Templates 0300-0399
- Third-Party Risk → Templates 0400-0499
- Information Sharing → Templates 0500-0599

**Primary Use Cases:**
- Financial sector compliance
- Operational resilience
- ICT risk management
- Third-party oversight

---

### 7. Cloud Security

#### CSA CCM (Cloud Security Alliance Cloud Controls Matrix)

**Framework Mapping File:** [templates/en/csa-ccm/9999_Framework_Mapping.md](../templates/en/csa-ccm/9999_Framework_Mapping.md)

**Standards Covered:**
- CSA CCM v4.0
- Cloud security controls

**Template Range:** 0010-0999  
**Total Templates:** ~95 per language

**Key Mappings:**
- Control domains (16 domains) → Templates organized by domain
- Each control → Individual template

**Primary Use Cases:**
- Cloud security assessment
- Cloud provider evaluation
- Multi-cloud governance
- STAR certification

---

### 8. Quality & Governance

#### ISO 9001:2015 (Quality Management)

**Framework Mapping File:** [templates/en/iso-9001/9999_Framework_Mapping.md](../templates/en/iso-9001/9999_Framework_Mapping.md)

**Standards Covered:**
- ISO 9001:2015 (Quality Management Systems)

**Template Range:** 0010-0999  
**Total Templates:** ~40 per language

**Key Mappings:**
- Clauses 4-10 → Templates organized by clause
- Quality processes → Documented throughout

**Primary Use Cases:**
- Quality management system
- ISO 9001 certification
- Process documentation
- Continuous improvement

#### ISO 31000:2018 (Risk Management)

**Framework Mapping File:** [templates/en/iso-31000/9999_Framework_Mapping.md](../templates/en/iso-31000/9999_Framework_Mapping.md)

**Standards Covered:**
- ISO 31000:2018 (Risk Management)
- ISO 31000:2009 (previous version)

**Template Range:** 0010-0599  
**Total Templates:** ~30 per language

**Key Mappings:**
- Risk Management Framework → Templates 0100-0299
- Risk Management Process → Templates 0300-0599

**Primary Use Cases:**
- Enterprise risk management
- Risk framework implementation
- Risk assessment methodology
- Risk governance

#### ISO/IEC 38500:2015 (IT Governance)

**Framework Mapping File:** [templates/en/iso-38500/9999_Framework_Mapping.md](../templates/en/iso-38500/9999_Framework_Mapping.md)

**Standards Covered:**
- ISO/IEC 38500:2015 (Governance of IT)

**Template Range:** 0010-0399  
**Total Templates:** ~20 per language

**Key Mappings:**
- Governance Principles → Templates 0100-0199
- Governance Model → Templates 0200-0299
- Governance Processes → Templates 0300-0399

**Primary Use Cases:**
- IT governance framework
- Board-level IT oversight
- Strategic IT alignment
- IT decision-making

#### TOGAF (The Open Group Architecture Framework)

**Framework Mapping File:** [templates/en/togaf/9999_Framework_Mapping.md](../templates/en/togaf/9999_Framework_Mapping.md)

**Standards Covered:**
- TOGAF 9.2
- Architecture Development Method (ADM)

**Template Range:** 0010-0799  
**Total Templates:** ~35 per language

**Key Mappings:**
- Architecture Vision → Templates 0100-0199
- Business/Data/Application/Technology Architecture → Templates 0200-0500
- Implementation & Migration → Templates 0600-0799

**Primary Use Cases:**
- Enterprise architecture
- Architecture governance
- ADM implementation
- Architecture repository

---

### 9. Product Security

#### Common Criteria (ISO/IEC 15408)

**Framework Mapping File:** [templates/en/common-criteria/9999_Framework_Mapping.md](../templates/en/common-criteria/9999_Framework_Mapping.md)

**Standards Covered:**
- ISO/IEC 15408-1:2022 (Introduction and general model)
- ISO/IEC 15408-2:2022 (Security functional components)
- ISO/IEC 15408-3:2022 (Security assurance components)

**Template Range:** 0010-0699  
**Total Templates:** ~50 per language

**Key Mappings:**
- ST Introduction → Templates 0010-0050
- TOE Description → Templates 0100-0140
- Security Problem Definition → Templates 0200-0240
- Security Objectives → Templates 0300-0330
- Security Requirements → Templates 0400-0440
- TOE Summary Specification → Templates 0500-0540
- Appendices → Templates 0600-0699

**Primary Use Cases:**
- Security Target documentation
- Common Criteria evaluation
- Product security certification
- EAL certification (EAL1-EAL7)

---

### 10. Service Documentation

#### Service Directory

**Framework Mapping File:** [templates/en/service-directory/9999_Framework_Mapping.md](../templates/en/service-directory/9999_Framework_Mapping.md)

**Purpose:** Service catalog and documentation templates

**Template Range:** 0010-0999  
**Total Templates:** Variable (service-specific)

**Key Mappings:**
- Service metadata → 0000_metadata files
- Service documentation → Service-specific templates

**Primary Use Cases:**
- Service catalog
- Service documentation
- CMDB integration
- Service portfolio management

---

## Cross-Framework Mappings

### Security Frameworks Alignment

| Control Area | ISO 27001 | NIST 800-53 | CIS Controls | CSA CCM |
|---|---|---|---|---|
| Access Control | A.5.15-A.5.18 | AC Family | Control 6 | IAM Domain |
| Cryptography | A.8.24 | SC Family | Control 3 | EKM Domain |
| Incident Management | A.5.24-A.5.28 | IR Family | Control 17 | SEF Domain |
| Vulnerability Management | A.8.8 | RA, SI Families | Control 7 | TVM Domain |
| Backup | A.8.13 | CP-9 | Control 11 | BCR Domain |

### Compliance Framework Relationships

```
ISO 27001 ←→ BSI Grundschutz (German implementation)
ISO 27001 ←→ TISAX (Automotive + ISO 27001)
NIST CSF ←→ NIST 800-53 (CSF references 800-53 controls)
SOC 2 (TSC) ←→ ISO 27001 (Overlapping controls)
PCI DSS ←→ ISO 27001 (Security controls alignment)
GDPR ←→ ISO 27001 (Privacy + Security)
HIPAA ←→ NIST 800-53 (Healthcare + Federal)
```

### Governance Framework Integration

```
ISO 38500 (IT Governance)
    ↓
COBIT 2019 (IT Management)
    ↓
ITIL v4 (Service Management)
    ↓
ISO 27001 (Security Management)
```

---

## Template Numbering Conventions

All frameworks follow a consistent numbering scheme:

- **0000-0009**: Metadata files (not rendered in handbooks)
- **0010-0099**: Framework overview, scope, and introduction
- **0100-0899**: Main content organized by framework structure
- **0900-0998**: Appendices, glossaries, and supporting documentation
- **9999**: Framework mapping documentation

### Special Files

- `0000_metadata_[lang]_[framework].md`: Framework metadata (not included in output)
- `README.md`: Framework-specific readme (not included in output)
- `9999_Framework_Mapping.md`: Framework mapping documentation

---

## Language Support

All frameworks are available in:
- **English (en)**: Primary language for international use
- **German (de)**: Full translation for German-speaking markets

Template structure and numbering are identical across languages to ensure consistency.

---

## Using Framework Mappings

### For Compliance Teams

1. Identify required frameworks for your organization
2. Review framework mapping files for each applicable framework
3. Use cross-framework mappings to identify overlapping requirements
4. Customize templates to match organizational context

### For Auditors

1. Reference framework mapping files to understand template coverage
2. Use cross-framework mappings to assess multi-framework compliance
3. Verify template completeness against framework requirements
4. Review evidence documentation in appendix templates

### For Implementation Teams

1. Start with framework overview templates (0010-0099)
2. Follow template sequence for systematic implementation
3. Use framework mapping to understand requirement coverage
4. Leverage cross-framework mappings for integrated implementations

---

## Framework Selection Guide

### Single Framework Implementation

Choose one primary framework based on:
- **Regulatory requirements**: GDPR, HIPAA, PCI DSS, DORA
- **Industry standards**: TISAX (automotive), Common Criteria (product security)
- **Certification goals**: ISO 27001, ISO 9001, SOC 2
- **Geographic location**: BSI Grundschutz (Germany), NIST (US Federal)

### Multi-Framework Implementation

Common combinations:
- **ISO 27001 + GDPR**: Security + Privacy
- **ISO 27001 + ISO 22301**: Security + Business Continuity
- **NIST CSF + NIST 800-53**: Framework + Controls
- **ISO 27001 + SOC 2**: Certification + Customer assurance
- **ITIL + ISO 27001**: Service Management + Security

### Framework Maturity Path

Recommended progression:
1. **Foundation**: ISO 27001 or NIST CSF
2. **Operational**: ITIL v4 or COBIT
3. **Specialized**: Industry-specific (PCI DSS, HIPAA, TISAX)
4. **Advanced**: Multiple certifications and integrations

---

## Maintenance and Updates

### Framework Version Tracking

Each framework mapping file documents:
- Framework version (e.g., ISO 27001:2022)
- Template version
- Last update date
- Change history

### Update Process

1. Monitor framework standard updates
2. Review impact on existing templates
3. Update framework mapping documentation
4. Revise affected templates
5. Update cross-framework mappings
6. Communicate changes to users

### Contributing

To contribute framework mappings:
1. Follow existing template structure
2. Document all framework requirements
3. Provide cross-references
4. Include implementation guidance
5. Submit for review

---

## Additional Resources

### Framework Standards

- **ISO Standards**: https://www.iso.org/
- **DIN (Deutsches Institut für Normung)**: https://www.din.de/
  - German standards organization
  - National member of ISO
  - DIN ISO standards (German versions of ISO standards)
- **BSI (Bundesamt für Sicherheit in der Informationstechnik)**: https://www.bsi.bund.de/
  - German Federal Office for Information Security
  - BSI Standards (200-1, 200-2, 200-3, 100-4)
  - IT-Grundschutz Compendium: https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/it-grundschutz_node.html
- **NIST Publications**: https://csrc.nist.gov/
- **CIS Controls**: https://www.cisecurity.org/
- **CSA (Cloud Security Alliance)**: https://cloudsecurityalliance.org/
- **Common Criteria**: https://www.commoncriteriaportal.org/

### Implementation Guides

- See individual framework mapping files in `templates/[lang]/[framework]/9999_Framework_Mapping.md`
- Refer to `docs/` directory for additional guidance
- Review example implementations in test outputs

### Support

For questions about framework mappings:
- Review framework-specific mapping files
- Check cross-framework alignment tables
- Consult framework standards documentation
- Contact framework certification bodies

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-02-18 | Documentation Team | Initial comprehensive framework mapping |

---

**End of Document**
