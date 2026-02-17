# Scope, Asset Groups and Tiering

**Document-ID:** [FRAMEWORK]-0020
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Approved by:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Classification:** {{ meta-handbook.classification }}
**Last Update:** {{ meta-handbook.modifydate }}

---

---

> **Note:** Template. Replace all `[TODO]` placeholders and remove non-applicable sections.  
> **Important:** This template does not paraphrase CIS original texts. Use it to derive and demonstrably implement **internal baselines/standards**.

## 1. Scope
- Organization/Locations/Cloud Accounts: [TODO]
- In-Scope Asset Types: [TODO]

## 2. Asset Groups (Examples)
| Group | Examples | Tooling/Source |
|---|---|---|
| Servers | Windows/Linux | CMDB/Cloud Inventory |
| Clients | Windows/macOS | MDM |
| Containers | Base Images / Runtimes | Registry/Scanner |
| Network | Firewalls/Switches | NMS |

## 3. Tiering / Criticality
> Classify baselines by tiers (e.g., Tier 0/1/2) or protection needs.
| Tier | Description | Minimum Requirements |
|---|---|---|
| T0 | Identity/Security Core (IAM, PKI, SIEM) | strictest baseline |
| T1 | Production-critical | high baseline |
| T2 | Standard | baseline |
| T3 | Dev/Test | potentially reduced baseline (risk-based) |

## 4. Responsibilities
- Asset Owner: [TODO]
- Platform Team: [TODO]
- Security/ISMS: [TODO]

