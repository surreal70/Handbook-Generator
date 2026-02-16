# CIS Controls v8 Framework Mapping

## Overview

This document maps the CIS Controls v8 Hardening Templates to the CIS Controls v8 framework components.

## Template Mapping to CIS Controls v8

### Foundation Templates

| Template | CIS Controls | Description |
|----------|--------------|-------------|
| 0010_CIS_Controls_Overview_and_Approach.md | All Controls | Overview and Implementation Approach |
| 0020_Scope_Asset_Groups_and_Tiering.md | Control 1, 2 | Asset Inventory and Scoping |
| 0030_Hardening_Lifecycle_and_Processes.md | Control 4 | Secure Configuration Management |
| 0040_Exceptions_and_Risk_Acceptance.md | Control 4 | Exception Management |
| 0050_Testing_and_Validation.md | Control 7, 18 | Testing and Validation |

### Operating System Hardening

| Template | CIS Controls | Description |
|----------|--------------|-------------|
| 0100_Windows_Server_Hardening_Baseline.md | Control 4, 5, 6 | Windows Server Secure Configuration |
| 0110_Windows_Client_Hardening_Baseline.md | Control 4, 5, 6 | Windows Client Secure Configuration |
| 0120_Linux_Hardening_Baseline.md | Control 4, 5, 6 | Linux Secure Configuration |
| 0130_macOS_Hardening_Baseline.md | Control 4, 5, 6 | macOS Secure Configuration |
| 0140_Container_Base_Images_Hardening.md | Control 4, 16 | Container Security |
| 0150_Mobile_Device_Hardening.md | Control 4, 6 | Mobile Device Security |

### Application Hardening

| Template | CIS Controls | Description |
|----------|--------------|-------------|
| 0200_Nginx_Webserver_Hardening.md | Control 4, 16 | Nginx Secure Configuration |
| 0210_Apache_Webserver_Hardening.md | Control 4, 16 | Apache Secure Configuration |
| 0220_IIS_Webserver_Hardening.md | Control 4, 16 | IIS Secure Configuration |
| 0230_Tomcat_Application_Server_Hardening.md | Control 4, 16 | Tomcat Secure Configuration |
| 0240_PostgreSQL_Database_Hardening.md | Control 3, 4, 6 | PostgreSQL Security |
| 0250_MySQL_MariaDB_Database_Hardening.md | Control 3, 4, 6 | MySQL/MariaDB Security |
| 0260_MS_SQL_Server_Database_Hardening.md | Control 3, 4, 6 | MS SQL Server Security |
| 0270_MongoDB_Database_Hardening.md | Control 3, 4, 6 | MongoDB Security |
| 0280_Kubernetes_Cluster_Hardening.md | Control 4, 12, 13 | Kubernetes Security |
| 0290_Docker_Engine_Hardening.md | Control 4, 16 | Docker Security |
| 0300_SSH_Service_Hardening.md | Control 4, 6 | SSH Secure Configuration |
| 0310_Active_Directory_Hardening.md | Control 5, 6 | Active Directory Security |
| 0320_Identity_Provider_Hardening.md | Control 5, 6 | Identity Provider Security |
| 0330_Cloud_Platform_Hardening.md | Control 4, 14 | Cloud Security |

### Appendices

| Template | CIS Controls | Description |
|----------|--------------|-------------|
| 0400_Control_Mapping_Template.md | All Controls | Control Mapping Matrix |
| 0410_Checklists_and_Evidence.md | All Controls | Compliance Evidence |

## CIS Controls v8 Implementation Groups

The templates support all three Implementation Groups:

- **IG1**: Essential Cyber Hygiene (Basic Hardening)
- **IG2**: Foundational (Extended Configuration)
- **IG3**: Advanced (Advanced Security Measures)

## CIS Benchmarks Alignment

The templates are aligned with the following CIS Benchmarks:

- CIS Microsoft Windows Server Benchmark
- CIS Microsoft Windows Desktop Benchmark
- CIS Distribution Independent Linux Benchmark
- CIS Apple macOS Benchmark
- CIS Docker Benchmark
- CIS Kubernetes Benchmark
- CIS PostgreSQL Benchmark
- CIS MySQL Benchmark
- CIS Microsoft SQL Server Benchmark
- CIS MongoDB Benchmark
- CIS Apache HTTP Server Benchmark
- CIS NGINX Benchmark
- CIS Microsoft IIS Benchmark

## References

- CIS Controls v8: https://www.cisecurity.org/controls/v8
- CIS Benchmarks: https://www.cisecurity.org/cis-benchmarks/

---

**Version:** 1.0.0  
**Date:** 2026-02-10

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial Creation |

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 0.1 | {{meta.document.last_updated}} | Initial creation |
