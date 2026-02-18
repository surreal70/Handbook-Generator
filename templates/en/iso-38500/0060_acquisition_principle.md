
Document-ID: iso-38500-0060
Owner: {{ meta-handbook.owner }}

Status: Draft
Classification: Internal

# Principle 3: Acquisition

**Document-ID:** [FRAMEWORK]-0060
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

This document describes the application of the Acquisition principle in the organization's IT governance.

## Scope

This document applies to:
- {{ meta-organisation.name }}
- All IT acquisitions (hardware, software, services)
- Acquisition processes and decisions

## Principle Definition

IT acquisitions are made for valid reasons, based on appropriate analysis, with clear and transparent decisions.

## Evaluate

### Assess Acquisition Needs

- Is the acquisition business-justified?
- Were alternatives analyzed?
- Are costs and benefits appropriate?
- Were risks assessed?

### Assessment Criteria

| Criterion | Requirement |
|-----------|-------------|
| Business Case | Required for acquisitions >{{ meta-handbook.business_case_threshold }} EUR |
| Cost-Benefit Analysis | Required |
| Risk Analysis | Required |
| Alternative Assessment | Minimum 3 options |

## Direct

### Acquisition Process

1. **Needs Assessment**: Identify business need
2. **Business Case**: Create justification
3. **Market Analysis**: Evaluate options
4. **Evaluation**: Analyze costs, benefits, risks
5. **Approval**: Decision by governance body
6. **Procurement**: Execution
7. **Implementation**: Deployment
8. **Review**: Post-implementation evaluation

### Approval Thresholds

| Acquisition Value | Approval by |
|-------------------|-------------|
| < {{ meta.threshold_1 }} EUR | IT Management |
| {{ meta.threshold_1 }} - {{ meta.threshold_2 }} EUR | CIO |
| {{ meta.threshold_2 }} - {{ meta.threshold_3 }} EUR | Executive Management |
| > {{ meta.threshold_3 }} EUR | Board |

### Acquisition Criteria

- **Functionality**: Meets requirements
- **Cost**: Total Cost of Ownership
- **Quality**: Reliability and performance
- **Risk**: Technical and business risks
- **Compliance**: Regulatory requirements
- **Sustainability**: Long-term viability

## Monitor

#### Acquisition Criteria

- **Functionality**: Meets requirements
- **Cost**: Total Cost of Ownership
- **Quality**: Reliability and performance
- **Risk**: Technical and business risks
- **Compliance**: Regulatory requirements
- **Sustainability**: Long-term viability

## Monitoring Measures

1. **Acquisition Reviews**: Quarterly
2. **Benefit Realization**: Post-implementation
3. **Supplier Performance**: Continuous
4. **Lessons Learned**: After project completion

### KPIs

- Acquisitions with business case: {{ meta-handbook.acquisitions_with_bc }}%
- Average acquisition time: {{ meta-handbook.avg_acquisition_time }} days
- Benefit realization: {{ meta-handbook.benefit_realization }}%
- Supplier satisfaction: {{ meta-handbook.supplier_satisfaction }}/10

## Document References

- 0010_governance_framework.md
- 0020_governance_model.md

