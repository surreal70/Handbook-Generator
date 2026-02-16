# CIS Controls v8 Framework-Mapping

## Überblick

Dieses Dokument bildet die CIS Controls v8 Hardening Templates auf die CIS Controls v8 Framework-Komponenten ab.

## Template-Mapping zu CIS Controls v8

### Foundation Templates

| Template | CIS Controls | Beschreibung |
|----------|--------------|--------------|
| 0010_CIS_Controls_Ueberblick_und_Vorgehen.md | Alle Controls | Überblick und Implementierungsansatz |
| 0020_Geltungsbereich_Assetgruppen_und_Tiering.md | Control 1, 2 | Asset Inventory und Scoping |
| 0030_Hardening_Lifecycle_und_Prozesse.md | Control 4 | Secure Configuration Management |
| 0040_Ausnahmen_und_Risikoakzeptanz.md | Control 4 | Exception Management |
| 0050_Test_und_Validierung.md | Control 7, 18 | Testing und Validation |

### Betriebssystem-Hardening

| Template | CIS Controls | Beschreibung |
|----------|--------------|--------------|
| 0100_Windows_Server_Hardening_Baseline.md | Control 4, 5, 6 | Windows Server Secure Configuration |
| 0110_Windows_Client_Hardening_Baseline.md | Control 4, 5, 6 | Windows Client Secure Configuration |
| 0120_Linux_Hardening_Baseline.md | Control 4, 5, 6 | Linux Secure Configuration |
| 0130_macOS_Hardening_Baseline.md | Control 4, 5, 6 | macOS Secure Configuration |
| 0140_Container_Base_Images_Hardening.md | Control 4, 16 | Container Security |
| 0150_Mobile_Device_Hardening.md | Control 4, 6 | Mobile Device Security |

### Applikations-Hardening

| Template | CIS Controls | Beschreibung |
|----------|--------------|--------------|
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

### Anhänge

| Template | CIS Controls | Beschreibung |
|----------|--------------|--------------|
| 0400_Control_Mapping_Template.md | Alle Controls | Control-Mapping-Matrix |
| 0410_Checklisten_und_Evidence.md | Alle Controls | Compliance-Nachweise |

## CIS Controls v8 Implementation Groups

Die Templates unterstützen alle drei Implementation Groups:

- **IG1**: Essential Cyber Hygiene (Basis-Hardening)
- **IG2**: Foundational (Erweiterte Konfiguration)
- **IG3**: Advanced (Fortgeschrittene Sicherheitsmaßnahmen)

## CIS Benchmarks Alignment

Die Templates sind aligned mit folgenden CIS Benchmarks:

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

## Referenzen

- CIS Controls v8: https://www.cisecurity.org/controls/v8
- CIS Benchmarks: https://www.cisecurity.org/cis-benchmarks/

---

**Version:** 1.0.0  
**Datum:** 2026-02-10

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |

## Versionshistorie

| Version | Datum | Änderungen |
|---------|-------|------------|
| 0.1 | {{meta.document.last_updated}} | Initiale Erstellung |
