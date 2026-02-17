
Document-ID: dora-0440

Status: Draft
Classification: Internal

# CI/CD Best Practices

**Dokument-ID:** [FRAMEWORK]-0440
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Genehmigt durch:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Klassifizierung:** {{ meta-handbook.classification }}
**Letzte Aktualisierung:** {{ meta-handbook.modifydate }}

---

---

## Zweck

Best Practices für CI/CD zur Reduzierung der Change Failure Rate.

## Umfang

- CI/CD-Prinzipien
- Quality Gates
- Progressive Delivery
- Deployment-Strategien

## Organisationsinformationen

- **Organisation**: [TODO]
- **CI/CD-Verantwortlicher**: [TODO]
- **CI/CD-Plattform**: [TODO]

## CI/CD-Prinzipien

### Continuous Integration

**Kernprinzipien**:
- Häufige Integration (mehrmals täglich)
- Automatisierte Builds
- Automatisierte Tests
- Schnelles Feedback

**Best Practices**:
- Trunk-based Development
- Feature Flags
- Small Batch Sizes
- Fast Build Times

### Continuous Delivery

**Kernprinzipien**:
- Jeder Commit ist deploybar
- Automatisierte Deployment-Pipeline
- Production-like Environments
- Deployment auf Knopfdruck

**Best Practices**:
- Automated Rollback
- Blue-Green Deployments
- Canary Releases
- Feature Toggles

## Quality Gates

### Build Stage Gates

**Kriterien**:
- Build erfolgreich
- Keine Compiler-Fehler
- Dependency-Check erfolgreich

### Test Stage Gates

**Kriterien**:
- Unit Tests: 100% Pass
- Integration Tests: 100% Pass
- Test Coverage: > 80%
- No Flaky Tests

### Security Stage Gates

**Kriterien**:
- No High/Critical Vulnerabilities
- SAST Scan erfolgreich
- Dependency Scan erfolgreich
- Container Scan erfolgreich

### Quality Stage Gates

**Kriterien**:
- Code Quality Score > Threshold
- No Code Smells (Critical)
- Technical Debt Ratio < 5%
- Duplication < 3%

## Progressive Delivery

### Canary Deployments

**Prozess**:
1. Deploy zu 5% der Nutzer
2. Monitor Metriken
3. Erhöhe auf 25%
4. Monitor Metriken
5. Erhöhe auf 50%
6. Monitor Metriken
7. Vollständiges Rollout

**Konfiguration**:
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

**Prozess**:
1. Deploy zu Green Environment
2. Test Green Environment
3. Switch Traffic zu Green
4. Monitor
5. Decommission Blue

### Feature Flags

**Verwendung**:
```python
if feature_enabled('new_checkout'):
    new_checkout_flow()
else:
    old_checkout_flow()
```

**Rollout-Steuerung**:
```yaml
feature_flags:
  new_checkout:
    enabled: true
    rollout_percentage: 25
    target_users:
      - beta_testers
```

## Deployment-Strategien

### Rolling Deployment

**Konfiguration**:
```yaml
strategy:
  type: RollingUpdate
  rollingUpdate:
    maxSurge: 1
    maxUnavailable: 0
```

### Recreate Deployment

**Verwendung**: Für Stateful Applications

### Shadow Deployment

**Zweck**: Testen ohne User-Impact

## Monitoring und Validation

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

**Trigger-Kriterien**:
- Error Rate > 5%
- Response Time P95 > 1000ms
- Health Check Failures > 3
- Custom Metrics Threshold

## Pipeline-Optimierung

### Caching

```yaml
cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - node_modules/
    - .cache/
```

### Parallelisierung

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

<!-- Hinweis: Robuste CI/CD reduziert CFR -->

