# Guideline: Asset Inventory, Tagging and Disposal

**Document-ID:** [FRAMEWORK]-0310
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

## 1. Purpose and Scope

This guideline implements the `0300_Policy_Asset_Management.md` and defines:
- Asset inventory and CMDB management
- Asset tagging and labeling
- Lifecycle management and disposal

**Scope:** All IT assets at **{{ meta-organisation.name }}**

## 2. Asset Categories

### 2.1 Hardware Assets
- Laptops, desktops, servers
- Network devices (switches, routers, firewalls)
- Mobile devices (smartphones, tablets)
- Peripherals (monitors, printers, scanners)
- Storage media (USB drives, external hard drives)

### 2.2 Software Assets
- Operating systems and licenses
- Application software
- Cloud subscriptions (SaaS)
- Development tools

### 2.3 Information Assets
- Databases
- File systems and shares
- Document collections
- Backup media

### 2.4 Services
- Cloud services (IaaS, PaaS, SaaS)
- Managed services
- Support contracts

## 3. Asset Inventory

### 3.1 CMDB (Configuration Management Database)

**System:** {{ meta.itsm.cmdb }} (e.g., ServiceNow, Jira Service Management)

**Mandatory Fields per Asset:**
- Asset ID (unique)
- Asset type and category
- Manufacturer, model, serial number
- Location, room
- Owner, user
- Purchase date, cost
- Maintenance contract, end of support
- Status (In operation, storage, defective, disposed)

**Additional Fields:**
- IP address, MAC address (network devices)
- Operating system, patch level
- Installed software
- Classification (criticality)
- Dependencies to other assets

### 3.2 Automatic Inventory

**Tools:**
- **Endpoint Management:** {{ meta.endpoint.management }} (e.g., Microsoft Intune, Jamf)
- **Network Discovery:** {{ meta.network.discovery }} (e.g., Nmap, Lansweeper)
- **Cloud Asset Inventory:** Native cloud tools (Azure Resource Graph, AWS Config)

**Process:**
- Daily automatic scans
- Comparison with CMDB
- Alerts for unknown assets (shadow IT)
- Automatic update of attributes

### 3.3 Manual Inventory

**Occasions:**
- New asset procurement
- Asset handover to employee
- Location change
- Maintenance or repair
- Decommissioning

**Process:**
1. Physically inspect asset
2. Create/update CMDB entry
3. Attach asset tag
4. Documentation (photos if needed)
5. Handover protocol (for employee assignment)

## 4. Asset Tagging

### 4.1 Tagging Schema

**Asset ID Format:** `{{ meta.asset.id_format }}`  
Example: `LAP-2024-001234` (Laptop, year, sequential number)

**Prefixes:**
- LAP: Laptop
- DSK: Desktop
- SRV: Server
- NET: Network device
- MOB: Mobile device
- PER: Peripheral

### 4.2 Physical Tags

**Barcode/QR Code Labels:**
- Self-adhesive, tamper-proof
- Placement in visible location
- Contains asset ID and QR code for CMDB link

**RFID Tags (optional):**
- For high-value assets
- Automatic capture during location change
- Integration with access control system

### 4.3 Digital Tags

**Hostname Convention:**
- Format: `{{ meta.naming.hostname_format }}`
- Example: `lap-jdoe-001` (type-user-number)

**Metadata:**
- Cloud resources: Tags for owner, cost center, environment
- Virtual machines: Tags for application, criticality

## 5. Asset Lifecycle Management

### 5.1 Procurement

**Process:**
1. Requirement request via ticket system
2. Approval by supervisor and IT management
3. Procurement through approved suppliers
4. Goods receipt and quality check
5. Create CMDB entry
6. Attach asset tag
7. Provision to user

**Documentation:**
- Order, invoice
- Warranty and maintenance contracts
- Handover protocol

### 5.2 Operation

**Maintenance:**
- Regular maintenance per manufacturer specifications
- Documentation in CMDB
- Firmware and software updates

**Monitoring:**
- Hardware health checks
- Capacity planning
- End-of-life tracking

### 5.3 Decommissioning

**Trigger:**
- End of useful life (typically 3-5 years)
- Defective, not repairable
- Technology change
- Employee offboarding

**Process:**
1. Take asset out of operation
2. Back up data (if required)
3. Securely delete data (see section 6)
4. Set CMDB status to "Decommissioned"
5. Decision: Reuse, sale, or disposal

## 6. Secure Data Destruction

### 6.1 Data Carrier Deletion

**Methods per DIN 66399:**

| Data Carrier | Classification | Method | Standard |
|--------------|----------------|--------|----------|
| HDD | Internal | Software deletion (3-pass) | DIN 66399 H-3 |
| HDD | Confidential | Degaussing + deletion | DIN 66399 H-4 |
| HDD | Highly Confidential | Physical destruction | DIN 66399 H-5 |
| SSD | Internal | Secure Erase (ATA) | DIN 66399 H-3 |
| SSD | Confidential/Highly Confidential | Cryptographic deletion + destruction | DIN 66399 H-5 |
| USB/SD | All | Physical destruction | DIN 66399 H-4 |

**Tools:**
- **Software:** DBAN, Blancco, Parted Magic
- **Hardware:** Degausser, shredder

**Documentation:**
- Deletion protocol with asset ID, date, method, executor
- Certificate for third-party disposal

### 6.2 Mobile Devices

**Process:**
1. Remote wipe via MDM ({{ meta.mdm.system }})
2. Factory reset on-site
3. Removal of SIM cards and SD cards
4. Physical verification of deletion
5. Documentation

### 6.3 Cloud Data

**Deletion:**
- Logical deletion in cloud service
- Wait for retention period expiration
- Confirmation of final deletion by provider
- Documentation (deletion confirmation)

## 7. Asset Disposal

### 7.1 Reuse

**Internal:**
- Refurbishment and reinstallation
- Assignment to another employee
- Use as test or development device

**Donation:**
- Data destruction per section 6
- Removal of all asset tags and company logos
- Documentation of donation (tax)

### 7.2 Sale

**Remarketing:**
- Only after complete data destruction
- Sale through certified remarketing partners
- Revenue documentation

### 7.3 Disposal

**Certified Disposal Partners:**
- WEEE-certified (Waste Electrical and Electronic Equipment)
- Disposal certificate required
- Environmentally responsible disposal

**Process:**
1. Data destruction (see section 6)
2. Handover to disposal partner
3. Receive disposal certificate
4. Set CMDB status to "Disposed"
5. Archive documentation

## 8. Compliance and Audit

### 8.1 Key Performance Indicators (KPIs)

| Metric | Target Value |
|--------|--------------|
| CMDB Completeness | > 95% |
| Asset Tagging Rate | 100% |
| Inventory Discrepancies | < 2% |
| Disposal Certificates | 100% |

### 8.2 Regular Inventories

**Frequency:**
- Complete inventory: Annually
- Spot checks: Quarterly
- Ad-hoc on suspected loss

**Process:**
1. CMDB export
2. Physical on-site inspection
3. Comparison CMDB vs. reality
4. Clarification of discrepancies
5. CMDB correction
6. Report to management

### 8.3 Audit Evidence

- CMDB reports
- Asset handover protocols
- Deletion protocols
- Disposal certificates
- Inventory reports

## 9. References

### Internal Documents
- `0300_Policy_Asset_Management.md`
- `0280_Policy_Data_Classification_and_Information_Handling.md`

### External Standards
- **ISO/IEC 27001:2022 Annex A.5.9** - Inventory of information and other associated assets
- **ISO/IEC 27001:2022 Annex A.5.10** - Acceptable use of information
- **DIN 66399** - Destruction of data carriers
- **WEEE Directive** - Electrical and electronic equipment disposal

**Approved by:** {{ meta.ciso.name }}, CISO  
**Next Review:** {{ meta-handbook.next_review }}

