<!--
Template: IT-Betriebshandbuch
Hinweis: Platzhalter sind mit [TODO] gekennzeichnet. Bitte anpassen.
Versionierung: Nutzen Sie vorzugsweise SemVer oder Ihr internes Schema.
-->

# Log Management und Audit

## Ziele
- Troubleshooting, Nachvollziehbarkeit, Compliance
- Schutz sensibler Daten in Logs

## Logging-Standards
- Log-Level: ERROR/WARN/INFO/DEBUG
- Korrelations-ID/Trace-ID: [TODO]
- PII/Secrets dürfen nicht geloggt werden

## Log-Quellen
| Quelle | Format | Retention | Zugriff | SIEM |
|---|---|---:|---|---|
| App Logs | JSON | [TODO] Tage | [TODO] | ☐ ja ☐ nein |
| Audit Logs | [TODO] | [TODO] | [TODO] | ☐ ja ☐ nein |

## Aufbewahrung & Löschung
- Retention Policy: [TODO]
- Löschkonzept (DSGVO): [TODO]

## Audit-Anforderungen
- Welche Events sind auditpflichtig? [TODO]
- Wo werden Audit-Logs gespeichert? [TODO]
- Wer darf Audit-Logs einsehen? [TODO]
