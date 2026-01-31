<!--
Template: IT-Betriebshandbuch
Hinweis: Platzhalter sind mit [TODO] gekennzeichnet. Bitte anpassen.
Versionierung: Nutzen Sie vorzugsweise SemVer oder Ihr internes Schema.
-->

# Access- und Berechtigungsmanagement

## Grundsätze
- Least Privilege / Need-to-Know
- Rollenbasiert (RBAC), keine individuellen Sonderrechte ohne Begründung
- MFA verpflichtend (wo möglich)
- Regelmäßige Rezertifizierung

## Rollenmodell
| Rolle | Rechteumfang | Zweck | Vergabe durch | Rezertifizierung |
|---|---|---|---|---|
| Viewer | Read-only | Analyse/Support | [TODO] | [TODO] |
| Operator | Operative Aktionen | Betrieb | [TODO] | [TODO] |
| Admin | Vollzugriff | Notfälle/Plattform | [TODO] | [TODO] |

## Provisioning/Deprovisioning
- **Antrag:** [TODO] (Ticket/Workflow)
- **Prüfung/Freigabe:** [TODO]
- **Dokumentation:** Ticket-ID + Zeitraum + Rolle
- **Offboarding:** Automatisiert/Checkliste [TODO]

## Break-Glass / Notfallzugang
- **Ablage der Credentials:** [TODO] (z. B. Passwort-Tresor)
- **Zugriffsprotokollierung:** [TODO]
- **Nachträgliche Genehmigung:** [TODO]
