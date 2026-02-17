# TISAX Framework Mapping

**Document-ID:** [FRAMEWORK]-9999
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

## Overview

This document maps the handbook templates to TISAX (Trusted Information Security Assessment Exchange) requirements based on VDA ISA Catalogue.

**Framework Status**: Partial Coverage (30% complete)
**Last Updated**: 2026-02-13

## 1. Framework Overview (0010-0099)

**Existing Templates:**
- 0010_tisax_framework_overview.md ✓
- 0020_information_security_policy.md ✓
- 0030_organization_of_information_security.md ✓
- 0040_risk_management.md ✓
- 0050_security_objectives_and_planning.md ✓

**TISAX Reference:**
- VDA ISA Catalogue: Information Security Management
- **VDA-ISA.1.1**: Information Security Policy
- **VDA-ISA.1.2**: Organization of Information Security
- **VDA-ISA.1.3**: Risk Management
- **VDA-ISA.1.4**: Security Objectives and Planning

## 2. Asset Management & Access Control (0060-0099)

**Existing Templates:**
- 0090_media_handling.md ✓

**TISAX Reference:**
- VDA ISA Catalogue: Asset Management
- VDA ISA Catalogue: Access Control
- **VDA-ISA.2.1**: Asset Inventory
- **VDA-ISA.2.2**: Information Classification
- **VDA-ISA.2.3**: Media Handling
- **VDA-ISA.3.1**: Access Control Policy
- **VDA-ISA.3.2**: User Access Management
- **VDA-ISA.3.3**: System and Application Access Control
- **VDA-ISA.3.4**: Privileged Access Rights

## 3. Operations Security (0060-0199)

**Existing Templates:**
- 0060_capacity_management.md ✓
- 0170_logging_and_monitoring.md ✓
- 0180_equipment_security.md ✓
- 0190_operations_security_overview.md ✓

**TISAX Reference:**
- VDA ISA Catalogue: Operations Security
- **VDA-ISA.6.1**: Change Management
- **VDA-ISA.6.2**: Capacity Management
- **VDA-ISA.6.3**: Malware Protection
- **VDA-ISA.6.4**: Backup and Recovery
- **VDA-ISA.6.5**: Logging and Monitoring
- **VDA-ISA.6.6**: Network Security Management
- **VDA-ISA.6.7**: Information Transfer

## 4. Business Continuity & Supplier Security (0070-0299)

**Existing Templates:**
- 0070_business_continuity_planning.md ✓
- 0080_ict_continuity.md ✓
- 0270_supplier_security.md ✓
- 0280_supplier_agreements.md ✓
- 0290_supplier_monitoring.md ✓

**TISAX Reference:**
- VDA ISA Catalogue: Business Continuity Management
- VDA ISA Catalogue: Supplier Relationships
- **VDA-ISA.8.1**: Supplier Security
- **VDA-ISA.8.2**: Supplier Agreements
- **VDA-ISA.8.3**: Supplier Monitoring
- **VDA-ISA.9.1**: Incident Management Procedures
- **VDA-ISA.9.2**: Incident Response
- **VDA-ISA.9.3**: Evidence Collection
- **VDA-ISA.10.1**: Business Continuity Planning
- **VDA-ISA.10.2**: ICT Continuity

## 5. Compliance & Data Protection (0260-0399)

**Existing Templates:**
- 0260_protection_of_records.md ✓
- 0380_privacy_and_personal_data_protection.md ✓

**TISAX Reference:**
- VDA ISA Catalogue: Compliance
- VDA ISA Catalogue: Privacy Information
- **VDA-ISA.11.1**: Compliance with Legal Requirements
- **VDA-ISA.11.2**: Intellectual Property Rights
- **VDA-ISA.11.3**: Protection of Records
- **VDA-ISA.11.4**: Privacy and Personal Data Protection

## Coverage Matrix

| Control Area | VDA ISA Controls | Existing Templates | Coverage |
|-------------|-----------------|-------------------|----------|
| Information Security Management | 1.1-1.4 | 5 templates | 100% |
| Asset Management | 2.1-2.3 | 1 template | 25% |
| Access Control | 3.1-3.4 | 0 templates | 0% |
| Cryptography | 4.1-4.2 | 0 templates | 0% |
| Physical Security | 5.1-5.4 | 1 template | 25% |
| Operations Security | 6.1-6.7 | 3 templates | 43% |
| Communications Security | 7.1-7.2 | 0 templates | 0% |
| Supplier Relationships | 8.1-8.3 | 3 templates | 100% |
| Incident Management | 9.1-9.3 | 0 templates | 0% |
| Business Continuity | 10.1-10.2 | 2 templates | 100% |
| Compliance | 11.1-11.4 | 2 templates | 50% |
| **Overall** | **All controls** | **18 templates** | **30%** |

## Existing Templates Summary

1. 0010_tisax_framework_overview.md
2. 0020_information_security_policy.md
3. 0030_organization_of_information_security.md
4. 0040_risk_management.md
5. 0050_security_objectives_and_planning.md
6. 0060_capacity_management.md
7. 0070_business_continuity_planning.md
8. 0080_ict_continuity.md
9. 0090_media_handling.md
10. 0170_logging_and_monitoring.md
11. 0180_equipment_security.md
12. 0190_operations_security_overview.md
13. 0260_protection_of_records.md
14. 0270_supplier_security.md
15. 0280_supplier_agreements.md
16. 0290_supplier_monitoring.md
17. 0380_privacy_and_personal_data_protection.md
18. 9999_Framework_Mapping.md

## Planned Templates

The following templates are planned for future development to achieve 100% coverage:

### Asset Management
- 0100_asset_management_overview.md
- 0110_asset_inventory.md
- 0120_information_classification.md

### Access Control
- 0140_access_control_policy.md
- 0150_user_access_management.md
- 0160_system_and_application_access_control.md

### Cryptography
- 0200_cryptographic_controls.md
- 0210_key_management.md

### Physical Security
- 0220_physical_security_perimeter.md
- 0230_physical_entry_controls.md
- 0240_securing_offices_and_facilities.md
- 0250_equipment_security.md

### Operations Security
- 0310_change_management.md
- 0320_capacity_management.md
- 0330_malware_protection.md
- 0340_backup_and_recovery.md
- 0350_logging_and_monitoring.md
- 0360_network_security_management.md
- 0370_information_transfer.md

### Supplier Relationships
- 0400_supplier_security.md
- 0410_supplier_agreements.md
- 0420_supplier_monitoring.md

### Incident Management
- 0430_incident_management_procedures.md
- 0440_incident_response.md
- 0450_evidence_collection.md

### Business Continuity
- 0500_business_continuity_planning.md
- 0510_ict_continuity.md

### Compliance
- 0520_compliance_with_legal_requirements.md
- 0530_intellectual_property_rights.md
- 0540_protection_of_records.md
- 0550_privacy_and_personal_data_protection.md

## References

- VDA ISA (Information Security Assessment) Catalogue
- TISAX Assessment Methodology
- ISO/IEC 27001:2013 (basis for VDA ISA)
- ENX Association TISAX Requirements

