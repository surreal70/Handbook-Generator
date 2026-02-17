
Document-ID: dora-0130

Status: Draft
Classification: Internal

# Deployment Pipeline

**Dokument-ID:** [FRAMEWORK]-0130
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

Dieses Dokument beschreibt den Aufbau, die Konfiguration und die Optimierung von Deployment-Pipelines für kontinuierliche Software-Delivery.

## Umfang

Dieses Dokument umfasst:
- Pipeline-Architektur und -Design
- Stage-Definitionen und -Konfiguration
- Quality Gates und Approval-Prozesse
- Pipeline-Optimierung und -Monitoring

## Pipeline-Architektur

### Organisationsinformationen

- **Organisation**: [TODO]
- **Pipeline-Verantwortlicher**: [TODO]
- **CI/CD-Plattform**: [TODO]
- **Pipeline-Repository**: [TODO]

## Pipeline-Stages

### 1. Source Stage

**Zweck**: Code-Checkout und Vorbereitung

**Aktivitäten**:
- Repository-Checkout
- Submodule-Initialisierung
- Dependency-Caching
- Workspace-Setup

**Konfiguration**:
```yaml
source:
  stage: source
  script:
    - git submodule update --init --recursive
    - echo "Source checkout complete"
  cache:
    key: ${CI_COMMIT_REF_SLUG}
    paths:
      - node_modules/
      - .cache/
```

### 2. Build Stage

**Zweck**: Kompilierung und Artefakt-Erstellung

**Aktivitäten**:
- Dependency-Installation
- Code-Kompilierung
- Asset-Generierung
- Artefakt-Packaging

**Konfiguration**:
```yaml
build:
  stage: build
  script:
    - npm ci
    - npm run build
    - npm run package
  artifacts:
    name: "${CI_PROJECT_NAME}-${CI_COMMIT_SHORT_SHA}"
    paths:
      - dist/
      - build/
    expire_in: 1 week
  only:
    - branches
    - tags
```

### 3. Test Stage

**Zweck**: Qualitätssicherung durch automatisierte Tests

**Unit Tests**:
```yaml
test:unit:
  stage: test
  script:
    - npm run test:unit
  coverage: '/Coverage: \d+\.\d+%/'
  artifacts:
    reports:
      junit: junit.xml
      coverage_report:
        coverage_format: cobertura
        path: coverage/cobertura-coverage.xml
```

**Integration Tests**:
```yaml
test:integration:
  stage: test
  services:
    - postgres:13
    - redis:6
  variables:
    DATABASE_URL: "postgresql://test:test@postgres:5432/testdb"
  script:
    - npm run test:integration
```

**E2E Tests**:
```yaml
test:e2e:
  stage: test
  script:
    - npm run test:e2e
  artifacts:
    when: on_failure
    paths:
      - cypress/screenshots/
      - cypress/videos/
```

### 4. Security Stage

**Zweck**: Sicherheitsüberprüfungen und Vulnerability-Scanning

**Dependency Scanning**:
```yaml
security:dependencies:
  stage: security
  script:
    - npm audit --audit-level=moderate
    - npm run security:check
  allow_failure: false
```

**SAST (Static Application Security Testing)**:
```yaml
security:sast:
  stage: security
  script:
    - semgrep --config=auto .
  artifacts:
    reports:
      sast: gl-sast-report.json
```

**Container Scanning**:
```yaml
security:container:
  stage: security
  script:
    - trivy image --severity HIGH,CRITICAL ${CI_REGISTRY_IMAGE}:${CI_COMMIT_SHA}
```

### 5. Quality Stage

**Zweck**: Code-Qualitätsprüfungen

**Linting**:
```yaml
quality:lint:
  stage: quality
  script:
    - npm run lint
    - npm run format:check
```

**Code Quality Analysis**:
```yaml
quality:sonar:
  stage: quality
  script:
    - sonar-scanner
      -Dsonar.projectKey=${CI_PROJECT_NAME}
      -Dsonar.sources=src
      -Dsonar.host.url=${SONAR_HOST_URL}
      -Dsonar.login=${SONAR_TOKEN}
```

### 6. Package Stage

**Zweck**: Container-Image-Erstellung und -Registrierung

**Docker Build**:
```yaml
package:docker:
  stage: package
  script:
    - docker build -t ${CI_REGISTRY_IMAGE}:${CI_COMMIT_SHA} .
    - docker tag ${CI_REGISTRY_IMAGE}:${CI_COMMIT_SHA} ${CI_REGISTRY_IMAGE}:latest
    - docker push ${CI_REGISTRY_IMAGE}:${CI_COMMIT_SHA}
    - docker push ${CI_REGISTRY_IMAGE}:latest
  only:
    - main
    - tags
```

### 7. Deploy Stage

**Zweck**: Deployment in Zielumgebungen

**Development Deployment**:
```yaml
deploy:dev:
  stage: deploy
  script:
    - kubectl set image deployment/${APP_NAME} ${APP_NAME}=${CI_REGISTRY_IMAGE}:${CI_COMMIT_SHA}
    - kubectl rollout status deployment/${APP_NAME}
  environment:
    name: development
    url: https://dev.[TODO]
  only:
    - develop
```

**Staging Deployment**:
```yaml
deploy:staging:
  stage: deploy
  script:
    - ./deploy.sh staging ${CI_COMMIT_SHA}
  environment:
    name: staging
    url: https://staging.[TODO]
  only:
    - main
  when: manual
```

**Production Deployment**:
```yaml
deploy:production:
  stage: deploy
  script:
    - ./deploy.sh production ${CI_COMMIT_SHA}
  environment:
    name: production
    url: https://[TODO]
  only:
    - tags
  when: manual
```

## Quality Gates

### Automatische Quality Gates

**Test Coverage Gate**:
```yaml
coverage_gate:
  stage: quality
  script:
    - |
      COVERAGE=$(cat coverage/coverage-summary.json | jq '.total.lines.pct')
      if (( $(echo "$COVERAGE < 80" | bc -l) )); then
        echo "Coverage $COVERAGE% is below threshold 80%"
        exit 1
      fi
```

**Performance Gate**:
```yaml
performance_gate:
  stage: quality
  script:
    - npm run test:performance
    - |
      RESPONSE_TIME=$(cat performance-report.json | jq '.avg_response_time')
      if (( $(echo "$RESPONSE_TIME > 200" | bc -l) )); then
        echo "Response time ${RESPONSE_TIME}ms exceeds threshold 200ms"
        exit 1
      fi
```

**Security Gate**:
```yaml
security_gate:
  stage: security
  script:
    - |
      VULNERABILITIES=$(npm audit --json | jq '.metadata.vulnerabilities.high + .metadata.vulnerabilities.critical')
      if [ "$VULNERABILITIES" -gt 0 ]; then
        echo "Found $VULNERABILITIES high/critical vulnerabilities"
        exit 1
      fi
```

### Manuelle Approval Gates

**Staging Approval**:
```yaml
approve:staging:
  stage: approve
  script:
    - echo "Awaiting staging approval"
  when: manual
  only:
    - main
```

**Production Approval**:
```yaml
approve:production:
  stage: approve
  script:
    - echo "Awaiting production approval"
  when: manual
  allow_failure: false
  only:
    - tags
```

## Pipeline-Optimierung

### Parallelisierung

**Parallel Test Execution**:
```yaml
test:unit:
  stage: test
  parallel: 4
  script:
    - npm run test:unit -- --shard=${CI_NODE_INDEX}/${CI_NODE_TOTAL}
```

**Matrix Builds**:
```yaml
test:compatibility:
  stage: test
  parallel:
    matrix:
      - NODE_VERSION: ['14', '16', '18']
        OS: ['ubuntu', 'alpine']
  image: node:${NODE_VERSION}-${OS}
  script:
    - npm run test
```

### Caching-Strategien

**Dependency Caching**:
```yaml
cache:
  key:
    files:
      - package-lock.json
  paths:
    - node_modules/
    - .npm/
  policy: pull-push
```

**Build Caching**:
```yaml
cache:
  key: ${CI_COMMIT_REF_SLUG}
  paths:
    - .cache/
    - dist/
  policy: pull
```

### Conditional Execution

**Path-based Triggers**:
```yaml
test:frontend:
  stage: test
  script:
    - npm run test:frontend
  only:
    changes:
      - src/frontend/**/*
      - package.json
```

**Branch-based Execution**:
```yaml
deploy:production:
  stage: deploy
  script:
    - ./deploy.sh production
  only:
    - main
    - /^release-.*$/
  except:
    - schedules
```

## Pipeline-Monitoring

### Metriken

**Pipeline-Performance**:
- Durchschnittliche Pipeline-Dauer
- Success/Failure-Rate
- Stage-spezifische Dauer
- Queue-Zeit

**Deployment-Metriken**:
- Deployment Frequency
- Lead Time
- Change Failure Rate
- Mean Time to Recovery

### Alerting

**Pipeline-Failures**:
```yaml
notify:failure:
  stage: .post
  script:
    - |
      curl -X POST ${SLACK_WEBHOOK_URL} \
        -H 'Content-Type: application/json' \
        -d "{
          \"text\": \"Pipeline failed for ${CI_PROJECT_NAME} on ${CI_COMMIT_REF_NAME}\",
          \"attachments\": [{
            \"color\": \"danger\",
            \"fields\": [{
              \"title\": \"Commit\",
              \"value\": \"${CI_COMMIT_SHORT_SHA}\",
              \"short\": true
            }]
          }]
        }"
  when: on_failure
```

### Dashboard

**Metriken-Visualisierung**:
- Grafana-Dashboards
- Pipeline-Trends
- Deployment-Statistiken
- Quality-Metriken

## Best Practices

### Pipeline-Design

1. **Fail Fast**: Schnelle Tests zuerst
2. **Parallelisierung**: Unabhängige Stages parallel ausführen
3. **Caching**: Wiederverwendung von Artefakten
4. **Idempotenz**: Wiederholbare Ausführung
5. **Observability**: Umfassendes Logging und Monitoring

### Security

1. **Secrets Management**: Keine Secrets im Code
2. **Least Privilege**: Minimale Berechtigungen
3. **Audit Logging**: Vollständige Nachvollziehbarkeit
4. **Vulnerability Scanning**: Automatische Sicherheitsprüfungen

### Maintenance

1. **Pipeline as Code**: Versionskontrolle
2. **Documentation**: Inline-Kommentare
3. **Regular Updates**: Tool- und Dependency-Updates
4. **Monitoring**: Kontinuierliche Überwachung

<!-- Hinweis: Eine gut designte Pipeline ist Grundlage für schnelle Delivery -->

