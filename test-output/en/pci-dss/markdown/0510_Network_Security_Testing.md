# Network Security Testing

**Document-ID:** PCI-DSS-0510
**Organisation:** AdminSend GmbH
**Owner:** [TODO]
**Approved by:** [TODO]
**Revision:** [TODO]
**Author:** Handbook-Generator
**Status:** Draft
**Classification:** Internal
**Last Update:** [TODO]
**Template Version:** [TODO]

---

---



## 1. Purpose

This document defines the network security testing requirements for AdminSend GmbH in accordance with PCI-DSS Requirement 11.

### 1.1 Objectives

- **Vulnerability Identification:** Regular vulnerability scans
- **Penetration Testing:** Annual security tests
- **Intrusion Detection:** IDS/IPS implementation
- **Compliance:** Fulfillment of PCI-DSS Requirement 11

### 1.2 Scope

**Affected Systems:**
- All CDE systems
- Perimeter systems
- Internal networks
- Web applications

## 2. Vulnerability Scanning

### 2.1 Quarterly Scans

**Requirements:**
- Quarterly external scans by ASV
- Quarterly internal scans
- After significant changes
- All systems in CDE

**ASV (Approved Scanning Vendor):**
- Name: [TODO: ASV name]
- Contact: [TODO: Contact]
- Last scan: [TODO: Date]
- Next scan: [TODO: Date]

### 2.2 External Vulnerability Scans

**Process:**
1. Commission ASV scan
2. Perform scan
3. Analyze results
4. Remediate vulnerabilities
5. Perform re-scan
6. Achieve passing scan
7. Archive ASV report

**Passing Scan Criteria:**
- No vulnerabilities with CVSS ≥ 4.0
- All critical vulnerabilities remediated
- ASV confirmation

### 2.3 Internal Vulnerability Scans

**Process:**
- Quarterly scans of all internal systems
- Authenticated scans (with credentials)
- Complete network scans
- Vulnerability prioritization
- Remediation plan

**Scan Tool:** [TODO: Name of scan tool]

**Scan Scope:**
- All CDE systems
- All systems with CHD access
- Network components
- Databases
- Web applications

### 2.4 Vulnerability Management

**Prioritization:**

| CVSS Score | Severity | Remediation Deadline |
|------------|----------|---------------------|
| 9.0 - 10.0 | Critical | 7 days |
| 7.0 - 8.9 | High | 30 days |
| 4.0 - 6.9 | Medium | 90 days |
| 0.1 - 3.9 | Low | 180 days |

**Remediation Process:**
1. Vulnerability identified
2. Risk assessment
3. Create remediation plan
4. Implement patch/fix
5. Validation
6. Documentation

## 3. Penetration Testing

### 3.1 Annual Penetration Tests

**Requirements:**
- Annually by qualified testers
- After significant changes
- External and internal tests
- Network and application tests

**Penetration Testing Firm:**
- Name: [TODO: Company]
- Contact: [TODO: Contact]
- Last test: [TODO: Date]
- Next test: [TODO: Date]

### 3.2 External Penetration Tests

**Scope:**
- Perimeter systems
- Publicly accessible web applications
- VPN access
- Email systems

**Methodology:**
- Black-box testing
- Exploitation of vulnerabilities
- Social engineering (optional)
- Documentation of all findings

### 3.3 Internal Penetration Tests

**Scope:**
- CDE network
- Internal applications
- Lateral movement tests
- Privilege escalation

**Methodology:**
- Gray-box testing
- Authenticated tests
- Exploitation
- Post-exploitation

### 3.4 Segmentation Testing

**Requirements:**
- Validation of network segmentation
- Attempts to cross CDE boundaries
- Firewall rule validation
- Documentation of results

**Process:**
1. Document segmentation
2. Define test scenarios
3. Perform penetration test
4. Analyze results
5. Remediate vulnerabilities
6. Re-test
7. Documentation

## 4. Intrusion Detection/Prevention

### 4.1 IDS/IPS Implementation

**Requirements:**
- IDS/IPS at all CDE boundaries
- Real-time monitoring
- Automatic alerts
- Regular signature updates

**IDS/IPS Systems:**

| System | Type | Location | Function |
|--------|------|----------|----------|
| [TODO: IDS-01] | Network IDS | Perimeter | Detection |
| [TODO: IPS-01] | Network IPS | CDE boundary | Prevention |
| [TODO: HIDS-01] | Host IDS | CDE servers | Detection |

### 4.2 IDS/IPS Signatures

**Requirements:**
- Current signatures
- Daily updates
- Custom signatures for known threats
- Regular review

**Update Process:**
1. Download signature updates
2. Test in test environment
3. Deploy to production
4. Validation
5. Documentation

### 4.3 IDS/IPS Alerting

**Alert Categories:**
- Critical: Immediate action required
- High: Investigation within 1 hour
- Medium: Investigation within 4 hours
- Low: Review within 24 hours

**Alert Response:**
- Automatic notification to SOC
- Initial investigation
- Escalation if needed
- Incident response
- Documentation

## 5. File Integrity Monitoring (FIM)

### 5.1 FIM Implementation

**Requirements:**
- FIM on all CDE systems
- Monitoring of critical files
- Real-time monitoring
- Automatic alerts

**FIM Tool:** [TODO: Name of FIM tool]

### 5.2 Monitored Files

**Critical Files:**
- System files
- Configuration files
- Application files
- Log files
- Database files

**Examples:**
- `/etc/passwd`, `/etc/shadow` (Linux)
- `C:\Windows\System32\config\SAM` (Windows)
- Firewall configurations
- Web server configurations
- Database configurations

### 5.3 FIM Alerting

**Alerts on:**
- File changes
- File deletions
- New files
- Permission changes
- Owner changes

**Alert Response:**
1. Receive alert
2. Validate change
3. Authorized change? (Change Request)
4. If unauthorized: Incident response
5. Documentation

## 6. Change Detection

### 6.1 Change Detection Mechanisms

**Requirements:**
- Automatic detection of changes
- Comparison with baseline
- Alerting on unauthorized changes
- Documentation of all changes

**Monitored Changes:**
- Configuration changes
- Software installations
- Patch installations
- User changes
- Permission changes

### 6.2 Baseline Management

**Process:**
1. Create initial baseline
2. Document baseline
3. Regular validation
4. Update after approved changes
5. Documentation

**Baseline Components:**
- System configuration
- Installed software
- Network configuration
- Users and permissions
- Services and processes

## 7. Wireless Security Testing

### 7.1 Wireless Access Point Detection

**Requirements:**
- Quarterly scans for wireless APs
- Detection of rogue APs
- Validation of authorized APs
- Documentation

**Scan Methods:**
- Wireless scanners
- Physical inspections
- Network scans

### 7.2 Wireless Security Standards

**Requirements for Authorized WLANs:**
- WPA3 or WPA2 with AES
- Strong authentication (802.1X)
- Separate VLAN for WLAN
- No connection to CDE without additional controls

## 8. Web Application Security Testing

### 8.1 Application Security Tests

**Requirements:**
- Annual security tests
- After significant changes
- OWASP Top 10 coverage
- Authenticated and unauthenticated tests

**Test Methods:**
- Automated scans (DAST)
- Manual penetration tests
- Code reviews (SAST)
- Fuzzing

### 8.2 OWASP Top 10

**Vulnerabilities to Test:**
1. Broken Access Control
2. Cryptographic Failures
3. Injection
4. Insecure Design
5. Security Misconfiguration
6. Vulnerable and Outdated Components
7. Identification and Authentication Failures
8. Software and Data Integrity Failures
9. Security Logging and Monitoring Failures
10. Server-Side Request Forgery (SSRF)

## 9. Social Engineering Testing

### 9.1 Phishing Simulations

**Requirements:**
- Regular phishing tests
- Various scenarios
- Employee awareness
- Documentation of results

**Process:**
1. Plan phishing campaign
2. Send emails
3. Measure click rates
4. Train employees
5. Documentation

### 9.2 Physical Social Engineering

**Tests:**
- Tailgating attempts
- Badge cloning
- Dumpster diving
- Pretexting

**Documentation:**
- Successful attacks
- Identify vulnerabilities
- Improvement measures
- Employee awareness

## 10. Compliance Validation

### 10.1 Validation Activities

**Quarterly:**
- Vulnerability scans (external and internal)
- Wireless AP scans
- FIM validation

**Annually:**
- Penetration tests (external and internal)
- Segmentation tests
- Web application security tests
- Social engineering tests

### 10.2 Validation Documentation

**Required Evidence:**
- ASV scan reports (4 per year)
- Internal scan reports (4 per year)
- Penetration test reports (1 per year)
- Segmentation test reports
- FIM configuration and logs
- IDS/IPS configuration and logs


