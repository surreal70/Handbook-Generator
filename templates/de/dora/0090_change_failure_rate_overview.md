
Document-ID: dora-0400

Status: Draft
Classification: Internal

# Change Failure Rate Übersicht

**Dokument-ID:** [FRAMEWORK]-0090
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

Beschreibung der Change Failure Rate Metrik.

## Umfang

- CFR-Definition
- Messmethodik
- Aktuelle Performance

## Definition

Change Failure Rate misst den Prozentsatz der Deployments, die zu Service-Degradation führen und Remediation erfordern.

### Organisationskontext

- **Organisation**: [TODO]
- **Aktuelle CFR**: [TODO]
- **Performance-Level**: [TODO]

## Messmethodik

### Failure-Definition

Ein Deployment-Failure ist:
- Rollback erforderlich
- Hotfix erforderlich
- Service-Degradation

### Berechnung

```
CFR = (Anzahl fehlgeschlagener Deployments / Gesamtzahl Deployments) * 100%
```

## Aktuelle Performance

### Gesamtorganisation

- **CFR**: [TODO]
- **Performance-Level**: [TODO]

### Nach Team

| Team | CFR | Performance-Level |
|------|-----|-------------------|
| [TODO] | [TODO] | [TODO] |
| [TODO] | [TODO] | [TODO] |

<!-- Hinweis: CFR ist Indikator für Code-Qualität und Testing -->

