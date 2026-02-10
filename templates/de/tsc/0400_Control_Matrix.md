# Anhang: Control Matrix

**Dokument-ID:** TSC-0400  
**Organisation:** {{ meta.organization.name }}  
**Owner:** {{ meta.document.owner }}  
**Version:** {{ meta.document.version }}  
**Status:** Entwurf / In Review / Freigegeben  
**Klassifizierung:** {{ meta.document.classification }}  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  

---

## 1. Zweck

Dieses Dokument enthält die vollständige TSC Control Matrix mit allen implementierten Kontrollen.

## 2. Common Criteria (Security) - Pflicht

| Control ID | Control Description | Control Owner | Test Frequency |
|------------|---------------------|---------------|----------------|
| CC1.1 | Integrity and ethical values | CISO | Annual |
| CC1.2 | Board independence | CEO | Annual |
| CC2.1 | Internal communication | CISO | Quarterly |
| CC3.1 | Risk identification | CISO | Annual |
| CC4.1 | Ongoing monitoring | Security Team | Continuous |
| CC5.1 | Control activities | Operations | Quarterly |
| CC6.1 | Logical access | Security Team | Quarterly |
| CC7.1 | Detection and monitoring | Security Team | Continuous |
| CC8.1 | Change authorization | Change Manager | Per change |
| CC9.1 | Risk assessment | CISO | Annual |

## 3. Availability (Optional)

| Control ID | Control Description | Control Owner | Test Frequency |
|------------|---------------------|---------------|----------------|
| A1.1 | Availability commitments | Operations | Monthly |
| A1.2 | System monitoring | Operations | Continuous |
| A1.3 | Incident management | Operations | Per incident |
| A1.4 | Recovery procedures | Operations | Quarterly |

## 4. Processing Integrity (Optional)

| Control ID | Control Description | Control Owner | Test Frequency |
|------------|---------------------|---------------|----------------|
| PI1.1 | Processing commitments | Development | Quarterly |
| PI1.2 | Input validation | Development | Per release |
| PI1.3 | Processing controls | Development | Per release |
| PI1.4 | Output controls | Development | Per release |

## 5. Confidentiality (Optional)

| Control ID | Control Description | Control Owner | Test Frequency |
|------------|---------------------|---------------|----------------|
| C1.1 | Confidentiality commitments | CISO | Annual |
| C1.2 | Access controls | Security Team | Quarterly |
| C1.3 | Encryption | Security Team | Quarterly |
| C1.4 | Data disposal | Operations | Per disposal |

## 6. Privacy (Optional)

| Control ID | Control Description | Control Owner | Test Frequency |
|------------|---------------------|---------------|----------------|
| P1 | Notice and communication | Legal/Privacy | Annual |
| P2-P3 | Choice and consent | Legal/Privacy | Per collection |
| P4-P5 | Collection and use | Legal/Privacy | Quarterly |
| P6 | Access | Legal/Privacy | Per request |
| P7 | Disclosure | Legal/Privacy | Per disclosure |
| P8 | Quality | Data Team | Quarterly |

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |
