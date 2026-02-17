
Document-ID: dora-0210

Status: Draft
Classification: Internal

# Lead Time Measurement

**Document-ID:** [FRAMEWORK]-0080
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

<!-- Note: Median is more robust against outliers than average -->

<!-- End of template -->
