# RFC Reference Guide

**Document Version:** 1.0  
**Last Updated:** 2026-02-18  
**Purpose:** Quick reference for current Internet standards (RFCs) relevant to cybersecurity and network protocols

---

## Overview

This document catalogs current Request for Comments (RFCs) that define Internet standards, protocols, and best practices. Only the most recent versions are detailed; superseded RFCs are referenced for historical context.

**RFC Categories:**
- Internet Standards (STD)
- Best Current Practice (BCP)
- Informational
- Experimental

**URL:** https://www.rfc-editor.org/

---

## 1. Transport Layer Security (TLS/SSL)

### TLS 1.3
**RFC 8446** - The Transport Layer Security (TLS) Protocol Version 1.3 (August 2018)  
**Status:** Proposed Standard  
**Supersedes:** RFC 5246 (TLS 1.2), RFC 6176 (SSL 2.0 prohibition)  
**Key Features:** Improved security, reduced handshake latency, removed obsolete cryptography

### TLS 1.2
**RFC 5246** - The Transport Layer Security (TLS) Protocol Version 1.2 (August 2008)  
**Status:** Proposed Standard (still widely used)  
**Supersedes:** RFC 4346 (TLS 1.1), RFC 2246 (TLS 1.0)  
**Note:** Minimum acceptable version; TLS 1.0/1.1 deprecated

### TLS Extensions
**RFC 6066** - Transport Layer Security (TLS) Extensions (January 2011)  
**RFC 7301** - TLS Application-Layer Protocol Negotiation (ALPN) (July 2014)  
**RFC 8446** - Includes TLS 1.3 extensions

### TLS Best Practices
**RFC 7525** - Recommendations for Secure Use of TLS and DTLS (May 2015)  
**BCP 195**

---

## 2. HTTP and Web Protocols

### HTTP/2
**RFC 9113** - HTTP/2 (June 2022)  
**Status:** Proposed Standard  
**Supersedes:** RFC 7540

### HTTP/3
**RFC 9114** - HTTP/3 (June 2022)  
**Status:** Proposed Standard  
**Based on:** QUIC (RFC 9000)

### HTTP/1.1
**RFC 9110** - HTTP Semantics (June 2022)  
**RFC 9111** - HTTP Caching (June 2022)  
**RFC 9112** - HTTP/1.1 (June 2022)  
**Supersedes:** RFC 7230-7237 series

### HTTP Security Headers
**RFC 6797** - HTTP Strict Transport Security (HSTS) (November 2012)  
**RFC 7034** - HTTP Header Field X-Frame-Options (October 2013)

---

## 3. QUIC Protocol

**RFC 9000** - QUIC: A UDP-Based Multiplexed and Secure Transport (May 2021)  
**RFC 9001** - Using TLS to Secure QUIC (May 2021)  
**RFC 9002** - QUIC Loss Detection and Congestion Control (May 2021)

---

## 4. Email Protocols

### SMTP
**RFC 5321** - Simple Mail Transfer Protocol (October 2008)  
**STD 10**  
**Supersedes:** RFC 2821

### IMAP
**RFC 9051** - Internet Message Access Protocol (IMAP) Version 4rev2 (August 2021)  
**Supersedes:** RFC 3501

### POP3
**RFC 1939** - Post Office Protocol - Version 3 (May 1996)  
**STD 53**

### Email Security
**RFC 8314** - Cleartext Considered Obsolete: Use of TLS for Email (January 2018)  
**Requires:** TLS for SMTP, IMAP, POP3

---

## 5. Email Authentication and Security

### SPF (Sender Policy Framework)
**RFC 7208** - Sender Policy Framework (SPF) (April 2014)

### DKIM (DomainKeys Identified Mail)
**RFC 6376** - DomainKeys Identified Mail (DKIM) Signatures (September 2011)  
**STD 76**

### DMARC
**RFC 7489** - Domain-based Message Authentication, Reporting, and Conformance (March 2015)

### S/MIME
**RFC 8551** - Secure/Multipurpose Internet Mail Extensions (S/MIME) Version 4.0 (April 2019)  
**RFC 8550** - S/MIME Certificate Handling (April 2019)

### PGP/OpenPGP
**RFC 4880** - OpenPGP Message Format (November 2007)  
**RFC 9580** - OpenPGP (July 2023) - Updates RFC 4880

---

## 6. DNS and DNSSEC

### DNS
**RFC 1034** - Domain Names - Concepts and Facilities (November 1987)  
**RFC 1035** - Domain Names - Implementation and Specification (November 1987)  
**STD 13**

### DNSSEC
**RFC 4033** - DNS Security Introduction and Requirements (March 2005)  
**RFC 4034** - Resource Records for DNS Security Extensions (March 2005)  
**RFC 4035** - Protocol Modifications for DNS Security Extensions (March 2005)  
**RFC 5155** - NSEC3 (March 2008)

### DNS over TLS (DoT)
**RFC 7858** - Specification for DNS over TLS (May 2016)

### DNS over HTTPS (DoH)
**RFC 8484** - DNS Queries over HTTPS (DoH) (October 2018)

### DNS Privacy
**RFC 9076** - DNS Privacy Considerations (July 2021)

---

## 7. Routing Protocols

### BGP
**RFC 4271** - Border Gateway Protocol 4 (BGP-4) (January 2006)

### BGP Security
**RFC 8205** - BGPsec Protocol Specification (September 2017)  
**RFC 6480** - An Infrastructure to Support Secure Internet Routing (February 2012)

### OSPF
**RFC 2328** - OSPF Version 2 (April 1998)  
**STD 54**  
**RFC 5340** - OSPF for IPv6 (July 2008)

---

## 8. IP and ICMP

### IPv4
**RFC 791** - Internet Protocol (September 1981)  
**STD 5**

### IPv6
**RFC 8200** - Internet Protocol, Version 6 (IPv6) Specification (July 2017)  
**STD 86**  
**Supersedes:** RFC 2460

### ICMPv4
**RFC 792** - Internet Control Message Protocol (September 1981)  
**STD 5**

### ICMPv6
**RFC 4443** - Internet Control Message Protocol (ICMPv6) for IPv6 (March 2006)  
**STD 89**

---

## 9. VPN and Tunneling

### IPsec
**RFC 4301** - Security Architecture for the Internet Protocol (December 2005)  
**RFC 4302** - IP Authentication Header (AH) (December 2005)  
**RFC 4303** - IP Encapsulating Security Payload (ESP) (December 2005)

### IKEv2
**RFC 7296** - Internet Key Exchange Protocol Version 2 (IKEv2) (October 2014)  
**STD 79**  
**Supersedes:** RFC 5996

### WireGuard
**RFC 9180** - Hybrid Public Key Encryption (HPKE) (February 2022) - Used by WireGuard

---

## 10. SSH

**RFC 4251** - The Secure Shell (SSH) Protocol Architecture (January 2006)  
**RFC 4252** - SSH Authentication Protocol (January 2006)  
**RFC 4253** - SSH Transport Layer Protocol (January 2006)  
**RFC 4254** - SSH Connection Protocol (January 2006)

---

## 11. Cryptographic Algorithms

### Hash Functions
**RFC 6234** - US Secure Hash Algorithms (SHA and SHA-based HMAC and HKDF) (May 2011)

### AES
**RFC 3602** - The AES-CBC Cipher Algorithm and Its Use with IPsec (September 2003)  
**RFC 5116** - An Interface and Algorithms for Authenticated Encryption (January 2008)

### Elliptic Curve Cryptography
**RFC 6090** - Fundamental Elliptic Curve Cryptography Algorithms (February 2011)  
**RFC 7748** - Elliptic Curves for Security (January 2016) - Curve25519, Curve448

### ChaCha20 and Poly1305
**RFC 8439** - ChaCha20 and Poly1305 for IETF Protocols (June 2018)  
**Supersedes:** RFC 7539

---

## 12. Key Exchange and Agreement

### Diffie-Hellman
**RFC 2631** - Diffie-Hellman Key Agreement Method (June 1999)  
**RFC 7919** - Negotiated Finite Field Diffie-Hellman Ephemeral Parameters for TLS (August 2016)

### ECDH
**RFC 8422** - Elliptic Curve Cryptography (ECC) Cipher Suites for TLS (August 2018)

---

## 13. Public Key Infrastructure (PKI)

### X.509 Certificates
**RFC 5280** - Internet X.509 Public Key Infrastructure Certificate and CRL Profile (May 2008)

### PKIX
**RFC 6960** - X.509 Internet Public Key Infrastructure Online Certificate Status Protocol (OCSP) (June 2013)

### Certificate Transparency
**RFC 9162** - Certificate Transparency Version 2.0 (December 2021)  
**Supersedes:** RFC 6962

---

## 14. Authentication and Authorization

### OAuth 2.0
**RFC 6749** - The OAuth 2.0 Authorization Framework (October 2012)  
**RFC 6750** - OAuth 2.0 Bearer Token Usage (October 2012)

### OAuth 2.0 Extensions
**RFC 7636** - Proof Key for Code Exchange (PKCE) (September 2015)  
**RFC 8252** - OAuth 2.0 for Native Apps (October 2017)

### OpenID Connect
Built on OAuth 2.0 (not an RFC, but IETF-related)

### SAML
Not an IETF standard (OASIS standard)

### Kerberos
**RFC 4120** - The Kerberos Network Authentication Service (V5) (July 2005)

---

## 15. Time Protocols

### NTP
**RFC 5905** - Network Time Protocol Version 4 (June 2010)

### NTS (Network Time Security)
**RFC 8915** - Network Time Security for NTP (September 2020)

---

## 16. Syslog and Logging

**RFC 5424** - The Syslog Protocol (March 2009)  
**RFC 5425** - TLS Transport Mapping for Syslog (March 2009)  
**RFC 5426** - Transmission of Syslog Messages over UDP (March 2009)

---

## 17. SNMP

**RFC 3410** - Introduction and Applicability Statements for SNMPv3 (December 2002)  
**RFC 3411-3418** - SNMPv3 specifications (December 2002)  
**STD 62**

---

## 18. WebSocket

**RFC 6455** - The WebSocket Protocol (December 2011)

---

## 19. JSON and Data Formats

### JSON
**RFC 8259** - The JavaScript Object Notation (JSON) Data Interchange Format (December 2017)  
**STD 90**  
**Supersedes:** RFC 7159

### JSON Web Token (JWT)
**RFC 7519** - JSON Web Token (JWT) (May 2015)

### JSON Web Signature (JWS)
**RFC 7515** - JSON Web Signature (JWS) (May 2015)

### JSON Web Encryption (JWE)
**RFC 7516** - JSON Web Encryption (JWE) (May 2015)

### JSON Web Key (JWK)
**RFC 7517** - JSON Web Key (JWK) (May 2015)

### JSON Web Algorithms (JWA)
**RFC 7518** - JSON Web Algorithms (JWA) (May 2015)

---

## 20. URI and URL

**RFC 3986** - Uniform Resource Identifier (URI): Generic Syntax (January 2005)  
**STD 66**

---

## 21. MIME and Content Types

**RFC 2045** - MIME Part One: Format of Internet Message Bodies (November 1996)  
**RFC 2046** - MIME Part Two: Media Types (November 1996)  
**STD 11**

---

## 22. Best Current Practices (BCP)

**BCP 14** - RFC 2119 - Key words for RFCs (MUST, SHOULD, etc.)  
**BCP 38** - RFC 2827 - Network Ingress Filtering  
**BCP 84** - RFC 3704 - Ingress Filtering for Multihomed Networks  
**BCP 195** - RFC 7525 - TLS/DTLS Recommendations  
**BCP 212** - RFC 8996 - Deprecating TLS 1.0 and TLS 1.1

---

## 23. Security Considerations

### General Security
**RFC 3552** - Guidelines for Writing RFC Text on Security Considerations (July 2003)  
**BCP 72**

### Randomness
**RFC 4086** - Randomness Requirements for Security (June 2005)  
**BCP 106**

---

## Quick Reference Table

| Protocol | Current RFC | Status | Supersedes |
|----------|-------------|--------|------------|
| TLS 1.3 | RFC 8446 | Standard | RFC 5246 |
| HTTP/3 | RFC 9114 | Standard | - |
| HTTP/2 | RFC 9113 | Standard | RFC 7540 |
| HTTP/1.1 | RFC 9110-9112 | Standard | RFC 7230-7237 |
| QUIC | RFC 9000-9002 | Standard | - |
| SMTP | RFC 5321 | STD 10 | RFC 2821 |
| IMAP | RFC 9051 | Standard | RFC 3501 |
| SPF | RFC 7208 | Standard | - |
| DKIM | RFC 6376 | STD 76 | - |
| DMARC | RFC 7489 | Standard | - |
| DNS | RFC 1034-1035 | STD 13 | - |
| DNSSEC | RFC 4033-4035 | Standard | - |
| DoT | RFC 7858 | Standard | - |
| DoH | RFC 8484 | Standard | - |
| IPv6 | RFC 8200 | STD 86 | RFC 2460 |
| IPsec | RFC 4301-4303 | Standard | - |
| IKEv2 | RFC 7296 | STD 79 | RFC 5996 |
| SSH | RFC 4251-4254 | Standard | - |
| OAuth 2.0 | RFC 6749 | Standard | - |
| JWT | RFC 7519 | Standard | - |
| JSON | RFC 8259 | STD 90 | RFC 7159 |

---

## Framework Integration

**Network Security Templates:**
- TLS/SSL configuration → Network security, communications protection
- IPsec/VPN → Remote access, network security
- DNS/DNSSEC → Network infrastructure, DNS security

**Email Security Templates:**
- SPF/DKIM/DMARC → Email security policies
- S/MIME/PGP → Email encryption policies

**Authentication Templates:**
- OAuth 2.0 → API security, access control
- Kerberos → Identity management, authentication

**Application Security Templates:**
- HTTP security headers → Web application security
- WebSocket → Real-time application security

---

## Resources

**RFC Editor:** https://www.rfc-editor.org/  
**RFC Search:** https://www.rfc-editor.org/search/rfc_search.php  
**IETF Datatracker:** https://datatracker.ietf.org/  
**IANA Protocol Registry:** https://www.iana.org/protocols

---

**Document Maintenance:**

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-02-18 | Initial RFC reference guide |

**Review Schedule:** Quarterly review for new RFCs and updates

---

**End of Document**
