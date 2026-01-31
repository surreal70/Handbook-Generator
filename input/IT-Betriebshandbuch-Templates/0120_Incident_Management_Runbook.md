<!--
Template: IT-Betriebshandbuch
Hinweis: Platzhalter sind mit [TODO] gekennzeichnet. Bitte anpassen.
Versionierung: Nutzen Sie vorzugsweise SemVer oder Ihr internes Schema.
-->

# Incident Management – Runbook

## Definitionen
- **Incident:** Ungeplante Unterbrechung oder Qualitätsminderung eines Services.
- **Major Incident:** Hohe Auswirkung (z. B. PROD-Ausfall) – erfordert beschleunigte Koordination.

## Schweregrade (Beispiel)
| Severity | Beschreibung | Reaktionszeit | Update-Frequenz |
|---|---|---:|---:|
| SEV1 | Kritischer Ausfall / viele Nutzer betroffen | [TODO] | [TODO] |
| SEV2 | Teilfunktion ausgefallen | [TODO] | [TODO] |
| SEV3 | Beeinträchtigung / Workaround vorhanden | [TODO] | [TODO] |

## Ablauf
1. **Erkennen & Triage** (Monitoring, Nutzer, Service Desk)
2. **Einstufung (Severity)** und **Ticket** erstellen
3. **Mitigation** (Schnellmaßnahmen) + **Kommunikation**
4. **Ursachenanalyse** (parallel/nachgelagert)
5. **Abschluss** + **Postmortem** (bei Major Incidents)

## Standard-Checks
- Systemstatus/Dashboards prüfen: [TODO]
- Letzte Deployments/Changes: [TODO]
- Kapazität: CPU/RAM/Disk/DB Connections: [TODO]
- Abhängigkeiten (DNS, IAM, Provider): [TODO]

## Kommunikationsvorlage
- **Was ist passiert?** [TODO]
- **Auswirkung:** [TODO]
- **Aktueller Status:** [TODO]
- **Nächster Update-Zeitpunkt:** [TODO]
- **Workaround:** [TODO]

## Postmortem
- Template-Link: [TODO]
- Action Items mit Owner & Due Date erfassen
