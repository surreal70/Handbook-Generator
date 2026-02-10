# Metadata: Common Criteria Security Target

**Document-ID:** 0000  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** Draft  
**Classification:** Confidential  
**Last Update:** {{ meta.date }}  

---

## Handbook Information

**Handbook Title:** Common Criteria Security Target (ISO/IEC 15408)  
**Organization:** {{ meta.organization }}  
**Author:** Andreas Huemmer [andreas.huemmer@adminsend.de]  
**Creation Date:** {{ meta.date }}  
**Version:** {{ meta.version }}  
**Scope:** {{ meta.scope }}  

---

## Purpose

This Security Target (ST) documents the security properties of the Target of Evaluation (TOE) according to ISO/IEC 15408 (Common Criteria for Information Technology Security Evaluation). It describes the security functions, security objectives, and security requirements of the TOE as well as the Evaluation Assurance Level (EAL).

## Target Audience

- Evaluators and certification bodies
- Product developers and security architects
- Customers and procurers of security-critical IT products
- Auditors and compliance officers

## Document Structure

The Security Target follows the structure of ISO/IEC 15408-1:2022 and includes:

1. **ST Introduction** - Introduction, TOE overview, conformance claims
2. **TOE Description** - Detailed description of the evaluation object
3. **Security Problem Definition** - Threats, organizational security policies, assumptions
4. **Security Objectives** - Security objectives for TOE and environment
5. **Security Requirements** - Functional and assurance requirements (SFR, SAR)
6. **TOE Summary Specification** - Summary of security functions
7. **Appendices** - PP conformance, rationale, glossary

## Usage Notes

- All `[TODO]` placeholders must be replaced with specific information
- Placeholders in `{{ source.field }}` format are automatically populated from data sources
- Diagrams can be stored in the `diagrams/` subdirectory
- The ST must be consistent with the chosen Protection Profile (PP)
- All security requirements must be derived from ISO/IEC 15408-2 and 15408-3

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| {{ meta.version }} | {{ meta.date }} | Andreas Huemmer [andreas.huemmer@adminsend.de] | Initial version |
