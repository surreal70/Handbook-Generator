<!--
Template: IT-Betriebshandbuch
Hinweis: Platzhalter sind mit [TODO] gekennzeichnet. Bitte anpassen.
Versionierung: Nutzen Sie vorzugsweise SemVer oder Ihr internes Schema.
-->

# Backup und Restore

## Backup-Ziele
- **RPO:** [TODO]
- **RTO:** [TODO]
- **Aufbewahrungsfristen:** [TODO]
- **Verschlüsselung:** ☐ at-rest ☐ in-transit

## Was wird gesichert?
| Daten/Komponente | Methode | Intervall | Aufbewahrung | Speicherort | Verantwortlich |
|---|---|---|---|---|---|
| DB [TODO] | Snapshot/Logical | [TODO] | [TODO] | [TODO] | [TODO] |
| Dateien [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## Restore-Prozedur (Runbook)
1. Incident/Change Ticket erstellen: [TODO]
2. Betroffene Umgebung bestätigen: [TODO]
3. Restore-Schritte:
   - [TODO]
4. Validierung:
   - Datenintegrität prüfen: [TODO]
   - Applikationstest: [TODO]
5. Abschlussdokumentation inkl. Zeiten, Logs, Lessons Learned

## Backup-Tests
- Frequenz: [TODO]
- Letzter erfolgreicher Test: [TODO]
- Nachweis/Protokoll: [TODO]
