# TISAX Framework Mapping

**Dokument-ID:** [FRAMEWORK]-9999
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Genehmigt durch:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Klassifizierung:** {{ meta-handbook.classification }}
**Letzte Aktualisierung:** {{ meta-handbook.modifydate }}

---

---

## Überblick

Dieses Dokument mappt die Handbook-Templates zu TISAX (Trusted Information Security Assessment Exchange) Anforderungen basierend auf VDA ISA Katalog.

**Framework-Status**: Teilweise Abdeckung (30% vollständig)
**Letzte Aktualisierung**: 2026-02-13

## 1. Framework-Übersicht (0010-0099)

**Vorhandene Templates:**
- 0010_tisax_framework_overview.md ✓
- 0020_information_security_policy.md ✓
- 0030_organization_of_information_security.md ✓
- 0040_risk_management.md ✓
- 0050_security_objectives_and_planning.md ✓

**TISAX Referenz:**
- VDA ISA Katalog: Informationssicherheitsmanagement
- **VDA-ISA.1.1**: Informationssicherheitsleitlinie
- **VDA-ISA.1.2**: Organisation der Informationssicherheit
- **VDA-ISA.1.3**: Risikomanagement
- **VDA-ISA.1.4**: Sicherheitsziele und Planung

## 2. Asset Management & Zugriffskontrolle (0060-0099)

**Vorhandene Templates:**
- 0090_media_handling.md ✓

**TISAX Referenz:**
- VDA ISA Katalog: Asset Management
- VDA ISA Katalog: Zugriffskontrolle
- **VDA-ISA.2.1**: Asset-Inventar
- **VDA-ISA.2.2**: Informationsklassifizierung
- **VDA-ISA.2.3**: Medienhandhabung
- **VDA-ISA.3.1**: Zugriffskontrollrichtlinie
- **VDA-ISA.3.2**: Benutzerzugriffsverwaltung
- **VDA-ISA.3.3**: System- und Anwendungszugriffskontrolle
- **VDA-ISA.3.4**: Privilegierte Zugriffsrechte

## 3. Betriebssicherheit (0060-0199)

**Vorhandene Templates:**
- 0060_capacity_management.md ✓
- 0170_logging_and_monitoring.md ✓
- 0180_equipment_security.md ✓
- 0190_operations_security_overview.md ✓

**TISAX Referenz:**
- VDA ISA Katalog: Betriebssicherheit
- **VDA-ISA.6.1**: Änderungsmanagement
- **VDA-ISA.6.2**: Kapazitätsmanagement
- **VDA-ISA.6.3**: Malware-Schutz
- **VDA-ISA.6.4**: Backup und Wiederherstellung
- **VDA-ISA.6.5**: Protokollierung und Überwachung
- **VDA-ISA.6.6**: Netzwerksicherheitsmanagement
- **VDA-ISA.6.7**: Informationsübertragung

## 4. Business Continuity & Lieferantensicherheit (0070-0299)

**Vorhandene Templates:**
- 0070_business_continuity_planning.md ✓
- 0080_ict_continuity.md ✓
- 0270_supplier_security.md ✓
- 0280_supplier_agreements.md ✓
- 0290_supplier_monitoring.md ✓

**TISAX Referenz:**
- VDA ISA Katalog: Business Continuity Management
- VDA ISA Katalog: Lieferantenbeziehungen
- **VDA-ISA.8.1**: Lieferantensicherheit
- **VDA-ISA.8.2**: Lieferantenvereinbarungen
- **VDA-ISA.8.3**: Lieferantenüberwachung
- **VDA-ISA.9.1**: Incident-Management-Verfahren
- **VDA-ISA.9.2**: Incident-Response
- **VDA-ISA.9.3**: Beweissicherung
- **VDA-ISA.10.1**: Business-Continuity-Planung
- **VDA-ISA.10.2**: IKT-Kontinuität

## 5. Compliance & Datenschutz (0260-0399)

**Vorhandene Templates:**
- 0260_protection_of_records.md ✓
- 0380_privacy_and_personal_data_protection.md ✓

**TISAX Referenz:**
- VDA ISA Katalog: Compliance
- VDA ISA Katalog: Datenschutzinformationen
- **VDA-ISA.11.1**: Einhaltung gesetzlicher Anforderungen
- **VDA-ISA.11.2**: Rechte an geistigem Eigentum
- **VDA-ISA.11.3**: Schutz von Aufzeichnungen
- **VDA-ISA.11.4**: Datenschutz und Schutz personenbezogener Daten

## Abdeckungsmatrix

| Kontrollbereich | VDA ISA Kontrollen | Vorhandene Templates | Abdeckung |
|----------------|-------------------|---------------------|----------|
| Informationssicherheitsmanagement | 1.1-1.4 | 5 Templates | 100% |
| Asset Management | 2.1-2.3 | 1 Template | 25% |
| Zugriffskontrolle | 3.1-3.4 | 0 Templates | 0% |
| Kryptographie | 4.1-4.2 | 0 Templates | 0% |
| Physische Sicherheit | 5.1-5.4 | 1 Template | 25% |
| Betriebssicherheit | 6.1-6.7 | 3 Templates | 43% |
| Kommunikationssicherheit | 7.1-7.2 | 0 Templates | 0% |
| Lieferantenbeziehungen | 8.1-8.3 | 3 Templates | 100% |
| Incident Management | 9.1-9.3 | 0 Templates | 0% |
| Business Continuity | 10.1-10.2 | 2 Templates | 100% |
| Compliance | 11.1-11.4 | 2 Templates | 50% |
| **Gesamt** | **Alle Kontrollen** | **18 Templates** | **30%** |

## Zusammenfassung vorhandener Templates

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

## Geplante Templates

Die folgenden Templates sind für die zukünftige Entwicklung geplant, um 100% Abdeckung zu erreichen:

### Asset Management
- 0100_asset_management_overview.md
- 0110_asset_inventory.md
- 0120_information_classification.md

### Zugriffskontrolle
- 0140_access_control_policy.md
- 0150_user_access_management.md
- 0160_system_and_application_access_control.md

### Kryptographie
- 0200_cryptographic_controls.md
- 0210_key_management.md

### Physische Sicherheit
- 0220_physical_security_perimeter.md
- 0230_physical_entry_controls.md
- 0240_securing_offices_and_facilities.md
- 0250_equipment_security.md

### Betriebssicherheit
- 0310_change_management.md
- 0320_capacity_management.md
- 0330_malware_protection.md
- 0340_backup_and_recovery.md
- 0350_logging_and_monitoring.md
- 0360_network_security_management.md
- 0370_information_transfer.md

### Lieferantenbeziehungen
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

## Referenzen

- VDA ISA (Information Security Assessment) Katalog
- TISAX Assessment Methodology
- ISO/IEC 27001:2013 (Basis für VDA ISA)
- ENX Association TISAX Requirements

