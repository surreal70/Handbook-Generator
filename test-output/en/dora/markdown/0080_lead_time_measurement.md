
Document-ID: dora-0210

Status: Draft
Classification: Internal

# Lead Time Measurement

**Document-ID:** DORA-0080
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

## Purpose

Detailed measurement methodology for Lead Time for Changes.

## Scope

- Measurement procedures
- Data collection
- Calculation

## Measurement Procedures

### Timestamp Capture

- **Commit Time**: [TODO]
- **Deploy Time**: [TODO]

### Calculation

```
Lead Time = Deploy Timestamp - Commit Timestamp
```

### Aggregation

- Median (preferred)
- 95th Percentile
- Average

## Data Collection

### Automation

- Git hooks for commit tracking
- CI/CD integration for deploy tracking
- Automatic correlation

### Data Quality

- **Completeness**: [TODO]
- **Accuracy**: [TODO]




