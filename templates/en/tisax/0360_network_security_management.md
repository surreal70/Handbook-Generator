
Document-ID: tisax-0360

Status: Draft
Classification: Internal

# Network Security Management

**Document-ID:** [FRAMEWORK]-0360
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

## Purpose

This document describes measures for network security according to TISAX requirements.

## Scope

This document applies to all networks of [TODO].

## Network Segmentation

### Security Zones
**DMZ (Demilitarized Zone):** Publicly accessible systems
**Internal Networks:** Business, development, administration networks
**High Security Network:** Critical systems

### Network Access Control
- 802.1X authentication
- NAC (Network Access Control)
- VLAN segmentation
- Firewall rules

## Firewall Management

### Firewall Rules
**Principles:**
- Default Deny
- Least Privilege
- Documented rules
- Regular review

### Firewall Types
**Perimeter Firewall:** Protection of entire network
**Internal Firewalls:** Segmentation
**Host-based Firewalls:** Protection of individual systems

## Intrusion Detection/Prevention

### IDS/IPS Systems
- Detection of attacks
- Automatic blocking
- Alerting
- Reporting

## VPN Management

### Remote Access VPN
- Multi-factor authentication
- Strong encryption
- Endpoint compliance check
- Logging

### Site-to-Site VPN
- Encrypted connections
- Redundant connections
- Monitoring
- Documentation

## Wireless Security

### WLAN Security
- WPA3 encryption
- 802.1X authentication
- Separate SSIDs for guests
- Regular security scans

### Guest WLAN
- Isolated from internal network
- Bandwidth limitation
- Time limitation
- Acceptance of terms of use

## Network Monitoring

### Monitoring
**Monitored Parameters:**
- Network traffic
- Bandwidth usage
- Security events
- Performance

## TISAX-Specific Requirements

### VDA ISA Controls
- **6.6**: Network security management
- **7.1**: Network security

### Assessment Evidence
- Network diagrams
- Firewall rules
- IDS/IPS configuration
- Monitoring reports

## Metrics

[TODO] measures:
- Number of blocked attacks
- Network availability
- Number of firewall rule changes

<!-- End of template -->
