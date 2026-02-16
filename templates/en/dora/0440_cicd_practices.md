---
Document-ID: dora-0440
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# CI/CD Best Practices

## Purpose

Best practices for CI/CD to reduce Change Failure Rate.

## Scope

- CI/CD principles
- Quality gates
- Progressive delivery
- Deployment strategies

## Organization Information

- **Organization**: {{ source.organization_name }}
- **CI/CD Owner**: {{ source.cicd_owner }}
- **CI/CD Platform**: {{ source.cicd_platform }}

## CI/CD Principles

### Continuous Integration

**Core Principles**:
- Frequent integration (multiple times daily)
- Automated builds
- Automated tests
- Fast feedback

**Best Practices**:
- Trunk-based development
- Feature flags
- Small batch sizes
- Fast build times

### Continuous Delivery

**Core Principles**:
- Every commit is deployable
- Automated deployment pipeline
- Production-like environments
- Push-button deployment

**Best Practices**:
- Automated rollback
- Blue-green deployments
- Canary releases
- Feature toggles

## Quality Gates

### Build Stage Gates

**Criteria**:
- Build successful
- No compiler errors
- Dependency check successful

### Test Stage Gates

**Criteria**:
- Unit tests: 100% pass
- Integration tests: 100% pass
- Test coverage: > 80%
- No flaky tests

### Security Stage Gates

**Criteria**:
- No high/critical vulnerabilities
- SAST scan successful
- Dependency scan successful
- Container scan successful

### Quality Stage Gates

**Criteria**:
- Code quality score > threshold
- No code smells (critical)
- Technical debt ratio < 5%
- Duplication < 3%

## Progressive Delivery

### Canary Deployments

**Process**:
1. Deploy to 5% of users
2. Monitor metrics
3. Increase to 25%
4. Monitor metrics
5. Increase to 50%
6. Monitor metrics
7. Full rollout

**Configuration**:
```yaml
canary:
  steps:
    - weight: 5
      pause: 10m
    - weight: 25
      pause: 10m
    - weight: 50
      pause: 10m
    - weight: 100
```

### Blue-Green Deployments

**Process**:
1. Deploy to green environment
2. Test green environment
3. Switch traffic to green
4. Monitor
5. Decommission blue

### Feature Flags

**Usage**:
```python
if feature_enabled('new_checkout'):
    new_checkout_flow()
else:
    old_checkout_flow()
```

**Rollout Control**:
```yaml
feature_flags:
  new_checkout:
    enabled: true
    rollout_percentage: 25
    target_users:
      - beta_testers
```

## Deployment Strategies

### Rolling Deployment

**Configuration**:
```yaml
strategy:
  type: RollingUpdate
  rollingUpdate:
    maxSurge: 1
    maxUnavailable: 0
```

### Recreate Deployment

**Usage**: For stateful applications

### Shadow Deployment

**Purpose**: Testing without user impact

## Monitoring and Validation

### Deployment Verification

**Health Checks**:
```yaml
readinessProbe:
  httpGet:
    path: /health
    port: 8080
  initialDelaySeconds: 10
  periodSeconds: 5
```

**Smoke Tests**:
```bash
#!/bin/bash
# Post-deployment smoke tests

test_health_endpoint() {
    curl -f http://app/health || exit 1
}

test_critical_api() {
    curl -f http://app/api/critical || exit 1
}

test_health_endpoint
test_critical_api
```

### Automated Rollback

**Trigger Criteria**:
- Error rate > 5%
- Response time P95 > 1000ms
- Health check failures > 3
- Custom metrics threshold

## Pipeline Optimization

### Caching

```yaml
cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - node_modules/
    - .cache/
```

### Parallelization

```yaml
test:
  parallel: 4
  script:
    - npm run test -- --shard=${CI_NODE_INDEX}/${CI_NODE_TOTAL}
```

### Conditional Execution

```yaml
deploy:production:
  only:
    - main
  except:
    - schedules
```

<!-- Note: Robust CI/CD reduces CFR -->

---

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Initial creation |
