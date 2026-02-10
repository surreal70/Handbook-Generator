# PCI-DSS Compliance Handbook Templates (English)

## Overview

These templates form the foundation for a complete PCI-DSS (Payment Card Industry Data Security Standard) compliance handbook according to **PCI-DSS v4.0**.

The PCI-DSS handbook of {{ meta.organization.name }} comprises structured documents covering all 12 PCI-DSS requirements to ensure the security of cardholder data.

## Template Structure

### Foundation (0010-0050)

| Document ID | Title | Description |
|-------------|-------|-------------|
| PCI-0010 | Scope and CDE Definition | Definition of Cardholder Data Environment (CDE) and scope |
| PCI-0020 | Network Segmentation | Documentation of network segmentation and CDE isolation |
| PCI-0030 | Roles and Responsibilities | PCI-DSS-specific roles and RACI matrices |
| PCI-0040 | Data Flow Diagrams | Visualization of cardholder data flows |
| PCI-0050 | Compliance Program | PCI-DSS compliance management and governance |

### Build and Maintain Secure Network (Requirements 1-2, 0100-0150)

| Document ID | Title | Description |
|-------------|-------|-------------|
| PCI-0100 | Firewall Configuration | Firewall and router configuration standards (Req 1) |
| PCI-0110 | Network Access Control | Network-level access control |
| PCI-0120 | System Hardening | Secure system configuration (Req 2) |
| PCI-0130 | Vendor Defaults | Changing vendor defaults |
| PCI-0140 | Wireless Security | Wireless network security |

### Protect Cardholder Data (Requirements 3-4, 0200-0250)

| Document ID | Title | Description |
|-------------|-------|-------------|
| PCI-0200 | Data Storage | Protection of stored cardholder data (Req 3) |
| PCI-0210 | Encryption | Encryption standards and key management |
| PCI-0220 | Data Transmission | Protection during transmission over public networks (Req 4) |
| PCI-0230 | Data Retention | Retention periods and secure deletion |
| PCI-0240 | Masking and Tokenization | PAN masking and tokenization procedures |

### Maintain Vulnerability Management (Requirements 5-6, 0300-0350)

| Document ID | Title | Description |
|-------------|-------|-------------|
| PCI-0300 | Malware Protection | Anti-malware programs and processes (Req 5) |
| PCI-0310 | Patch Management | Security patches and updates (Req 6) |
| PCI-0320 | Secure Development | Secure software development |
| PCI-0330 | Vulnerability Scanning | Quarterly vulnerability scans |
| PCI-0340 | Penetration Testing | Annual penetration tests |

### Implement Strong Access Control (Requirements 7-9, 0400-0450)

| Document ID | Title | Description |
|-------------|-------|-------------|
| PCI-0400 | Access Control | Need-to-know principle (Req 7) |
| PCI-0410 | Authentication | User identification and authentication (Req 8) |
| PCI-0420 | Multi-Factor Authentication | MFA for CDE access |
| PCI-0430 | Physical Security | Physical access to CDE (Req 9) |
| PCI-0440 | Media Handling | Secure handling of physical media |

### Monitor and Test Networks (Requirements 10-11, 0500-0550)

| Document ID | Title | Description |
|-------------|-------|-------------|
| PCI-0500 | Logging and Monitoring | Logging of all access (Req 10) |
| PCI-0510 | Log Review | Daily log review |
| PCI-0520 | Security Testing | Regular security testing (Req 11) |
| PCI-0530 | Intrusion Detection | IDS/IPS systems |
| PCI-0540 | File Integrity Monitoring | Monitoring of critical files |

### Maintain Information Security Policy (Requirement 12, 0600-0650)

| Document ID | Title | Description |
|-------------|-------|-------------|
| PCI-0600 | Security Policy | Information security policy (Req 12) |
| PCI-0610 | Risk Assessment | Annual risk assessment |
| PCI-0620 | Training Program | Security awareness training |
| PCI-0630 | Incident Response | Incident response plan |
| PCI-0640 | Service Provider Management | Management of service providers |

### Appendices (0700-0750)

| Document ID | Title | Description |
|-------------|-------|-------------|
| PCI-0700 | Compliance Evidence | Documentation for audits |
| PCI-0710 | Scan Reports | Quarterly vulnerability scan reports |
| PCI-0720 | Penetration Test Reports | Annual penetration test documentation |
| PCI-0730 | Checklists | PCI-DSS Self-Assessment Questionnaire (SAQ) |
| PCI-0740 | Glossary | PCI-DSS-specific terms and abbreviations |

## Placeholder Usage

### Meta Placeholders (Organization Data)

Templates use placeholders from the `metadata.yaml` file:

```markdown
**Organization:** {{ meta.organization.name }}
**QSA:** {{ meta.roles.qsa.name }} ({{ meta.roles.qsa.email }})
**CISO:** {{ meta.roles.ciso.name }} ({{ meta.roles.ciso.email }})
**Merchant ID:** {{ meta.pci.merchant_id }}
**Service Provider ID:** {{ meta.pci.service_provider_id }}
```

### [TODO] Markers

All templates contain `[TODO]` markers for organization-specific customizations:

```markdown
**CDE Systems:** [TODO: List of systems in CDE]
**Encryption Algorithm:** [TODO: AES-256]
**Scan Vendor:** [TODO: Approved Scanning Vendor Name]
```

## PCI-DSS v4.0 Compliance Mapping

| PCI-DSS Requirement | PCI Document | Description |
|---------------------|--------------|-------------|
| Req 1: Firewall Configuration | PCI-0100, PCI-0110 | Firewall and network security |
| Req 2: Secure Configuration | PCI-0120, PCI-0130, PCI-0140 | System hardening |
| Req 3: Protect Stored Data | PCI-0200, PCI-0210, PCI-0230 | Data storage |
| Req 4: Encrypt Transmission | PCI-0220 | Data transmission |
| Req 5: Protect Against Malware | PCI-0300 | Malware protection |
| Req 6: Secure Systems | PCI-0310, PCI-0320 | Patch management |
| Req 7: Restrict Access | PCI-0400 | Access control |
| Req 8: Identify Users | PCI-0410, PCI-0420 | Authentication |
| Req 9: Physical Access | PCI-0430, PCI-0440 | Physical security |
| Req 10: Log and Monitor | PCI-0500, PCI-0510 | Logging |
| Req 11: Test Security | PCI-0520, PCI-0530, PCI-0540 | Security testing |
| Req 12: Security Policy | PCI-0600-PCI-0640 | Policies |

## Important PCI-DSS Concepts

### Cardholder Data Environment (CDE)

The CDE includes:
- **Systems:** All systems that store, process, or transmit cardholder data
- **Networks:** Network segments connected to CDE systems
- **People:** Employees with access to cardholder data

### Cardholder Data (CHD)

- **Primary Account Number (PAN):** 13-19 digit card number
- **Cardholder Name:** Name of cardholder
- **Service Code:** 3-digit code
- **Expiration Date:** Expiration date

### Sensitive Authentication Data (SAD)

**Must NOT be stored after authorization:**
- **Full Track Data:** Magnetic stripe data
- **CAV2/CVC2/CVV2/CID:** Card verification value
- **PIN/PIN Block:** PIN data

### Merchant Levels

- **Level 1:** > 6 million transactions/year
- **Level 2:** 1-6 million transactions/year
- **Level 3:** 20,000-1 million e-commerce transactions/year
- **Level 4:** < 20,000 e-commerce transactions/year or < 1 million transactions/year

## Best Practices for PCI-DSS Compliance

### 1. Scope Reduction

- **Network Segmentation:** Isolate CDE from rest of network
- **Tokenization:** Replace PAN with tokens
- **Point-to-Point Encryption (P2PE):** Encryption at point of sale
- **Outsourcing:** Use PCI-DSS certified service providers

### 2. Quarterly Activities

- **Vulnerability Scans:** By Approved Scanning Vendor (ASV)
- **Log Review:** Daily review of critical logs
- **Firewall Rule Review:** Quarterly review

### 3. Annual Activities

- **Penetration Tests:** By qualified testers
- **Risk Assessment:** Formal risk assessment
- **Security Awareness Training:** For all employees
- **Policy Review:** Review of all security policies

### 4. Documentation

- **Network Diagrams:** Keep current
- **Data Flow Diagrams:** Document all CHD flows
- **System Inventory:** Capture all CDE systems
- **Change Logs:** Document all changes

## Handbook Generation

### CLI Usage

```bash
# Generate German PCI-DSS handbook
python -m src.cli --language de --template pci-dss --test

# Generate English PCI-DSS handbook
python -m src.cli --language en --template pci-dss --test

# Generate PDF with table of contents
python -m src.cli --language en --template pci-dss --output pdf --test --pdf-toc

# Generate all formats
python -m src.cli --language en --template pci-dss --output all --test --separate-files --pdf-toc
```

## Maintenance and Updates

### Update Intervals

- **Annually:** Complete review before re-assessment
- **Quarterly:** Scan reports and log reviews
- **Ad-hoc:** After CDE changes or incidents

### Versioning

- **MAJOR:** New PCI-DSS version (e.g., v4.0 → v5.0)
- **MINOR:** Additions and updates
- **PATCH:** Corrections and editorial changes

## Support and Feedback

For questions or issues:

- **Documentation:** See main README.md
- **PCI SSC:** https://www.pcisecuritystandards.org/
- **Issues:** GitHub Issues for bug reports

---

**Version:** 1.0.0  
**Last Updated:** 2026-02-06  
**Maintainer:** PCI-DSS Template Team
