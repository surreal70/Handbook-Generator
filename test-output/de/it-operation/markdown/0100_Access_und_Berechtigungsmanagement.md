# Access und Berechtigungsmanagement

**Dokument-ID:** IT-OPERATION-0100
**Organisation:** AdminSend GmbH
**Owner:** [TODO]
**Genehmigt durch:** [TODO]
**Revision:** [TODO]
**Author:** Handbook-Generator
**Status:** Draft
**Klassifizierung:** Internal
**Letzte Aktualisierung:** [TODO]
**Template Version:** [TODO]

---

---

## Übersicht

Dieses Dokument beschreibt das Access- und Berechtigungsmanagement für den IT-Service. Es definiert Zugriffskontrollmodelle, Berechtigungskonzepte und rollenbasierte Zugriffskontrolle (RBAC).

**Service:** {{ meta-handbook.service_name }}  
**Verantwortlich:** {{ meta-organisation-roles.role_IT_Operations_Manager }}  
**Security Officer:** [TODO]  
**Stand:** 0

## Access Management Strategie

### Ziele

- **Least Privilege:** Minimale notwendige Berechtigungen
- **Separation of Duties:** Aufgabentrennung zur Risikominimierung
- **Need-to-Know:** Zugriff nur auf erforderliche Informationen
- **Accountability:** Nachvollziehbarkeit aller Zugriffe
- **Compliance:** Einhaltung regulatorischer Anforderungen

### Grundprinzipien

1. **Default Deny:** Standardmäßig kein Zugriff, explizite Freigabe erforderlich
2. **Time-Limited Access:** Zeitlich begrenzte Berechtigungen wo möglich
3. **Regular Review:** Regelmäßige Überprüfung von Berechtigungen
4. **Audit Trail:** Vollständige Protokollierung aller Zugriffe
5. **Multi-Factor Authentication:** MFA für privilegierte Zugriffe

## Zugriffskontrollmodell

### Authentifizierung

#### Authentifizierungsmethoden

| Methode | Verwendung | Sicherheitsstufe |
|---|---|---|
| **Username/Password** | Standard-Zugriff | Basis |
| **Multi-Factor Authentication (MFA)** | Privilegierter Zugriff | Hoch |
| **Certificate-Based** | System-zu-System | Sehr hoch |
| **SSO (Single Sign-On)** | Unternehmensanwendungen | Mittel-Hoch |
| **API Keys** | Programmatischer Zugriff | Mittel |
| **Biometric** | Hochsicherheitsbereiche | Sehr hoch |

#### Authentifizierungs-Infrastruktur

**Identity Provider:**
- **System:** [TODO: z.B. Active Directory, Azure AD, Okta]
- **URL:** [TODO: SSO-URL]
- **Verantwortlich:** {{ meta-organisation-roles.role_IT_Operations_Manager }}

**MFA-System:**
- **System:** [TODO: z.B. Duo, Microsoft Authenticator]
- **Pflicht für:** Administratoren, privilegierte Accounts
- **Verantwortlich:** [TODO]

### Autorisierung

#### Autorisierungsmodelle

**Role-Based Access Control (RBAC):**
- Berechtigungen werden Rollen zugewiesen
- Benutzer erhalten Rollen
- Vereinfacht Berechtigungsverwaltung

**Attribute-Based Access Control (ABAC):**
- Berechtigungen basieren auf Attributen
- Flexibler als RBAC
- Komplexere Implementierung

**Aktuelles Modell:** [TODO: RBAC/ABAC/Hybrid auswählen]

## Rollenbasierte Zugriffskontrolle (RBAC)

### Rollen-Hierarchie

```
┌─────────────────────────────────────────────────────────────┐
│                    Administrator                             │
│  (Vollzugriff auf alle Systeme und Daten)                   │
└────────────────────┬────────────────────────────────────────┘
                     │
         ┌───────────┴───────────┐
         │                       │
┌────────▼────────┐    ┌────────▼────────────────────────────┐
│  Power User     │    │     Operator                         │
│  (Erweiterte    │    │  (Betriebszugriff)                   │
│   Berechtigungen)│    └────────┬────────────────────────────┘
└─────────────────┘             │
                                │
                    ┌───────────┴───────────┐
                    │                       │
           ┌────────▼────────┐    ┌────────▼────────┐
           │   Standard User │    │   Read-Only     │
           │  (Basis-Zugriff)│    │  (Nur Lesen)    │
           └─────────────────┘    └─────────────────┘
```

### Rollen-Definition

#### Administrator
**Beschreibung:** Vollzugriff auf alle Systeme und Funktionen  
**Berechtigungen:**
- Vollzugriff auf alle Systeme
- Benutzerverwaltung
- Konfigurationsänderungen
- System-Administration
- Backup/Restore

**Zugewiesen an:**
- {{ meta-organisation-roles.role_IT_Operations_Manager }}
- [TODO: Weitere Administratoren]

**MFA:** Pflicht

#### Power User
**Beschreibung:** Erweiterte Berechtigungen für spezielle Aufgaben  
**Berechtigungen:**
- Lesen und Schreiben in zugewiesenen Bereichen
- Erweiterte Funktionen nutzen
- Reports erstellen
- Konfiguration in eigenem Bereich

**Zugewiesen an:**
- [TODO: Power User auflisten]

**MFA:** Empfohlen

#### Operator
**Beschreibung:** Betriebszugriff für tägliche Aufgaben  
**Berechtigungen:**
- Monitoring-Zugriff
- Incident-Bearbeitung
- Standard-Operationen
- Log-Zugriff (Read-only)

**Zugewiesen an:**
- {{ meta-organisation-roles.role_Service_Desk_Lead }}
- [TODO: Weitere Operators]

**MFA:** Optional

#### Standard User
**Beschreibung:** Basis-Zugriff für normale Benutzer  
**Berechtigungen:**
- Zugriff auf eigene Daten
- Standard-Funktionen nutzen
- Tickets erstellen
- Eigenes Profil verwalten

**Zugewiesen an:**
- Alle Mitarbeiter

**MFA:** Optional

#### Read-Only
**Beschreibung:** Nur Lesezugriff für Reporting und Auditing  
**Berechtigungen:**
- Lesezugriff auf Daten
- Reports anzeigen
- Dashboards anzeigen
- Keine Änderungen möglich

**Zugewiesen an:**
- Auditoren
- Management
- [TODO: Weitere Read-Only-Benutzer]

**MFA:** Optional

## Berechtigungsmatrix

### System-Berechtigungen

| System/Ressource | Administrator | Power User | Operator | Standard User | Read-Only |
|---|---|---|---|---|---|
| **Server-Administration** | Vollzugriff | - | - | - | Lesen |
| **Netzwerk-Konfiguration** | Vollzugriff | - | - | - | Lesen |
| **Monitoring-System** | Vollzugriff | Lesen/Schreiben | Lesen | - | Lesen |
| **Ticketing-System** | Vollzugriff | Lesen/Schreiben | Lesen/Schreiben | Tickets erstellen | Lesen |
| **CMDB** | Vollzugriff | Lesen/Schreiben | Lesen | - | Lesen |
| **Backup-System** | Vollzugriff | - | Lesen | - | Lesen |
| **Log-Management** | Vollzugriff | Lesen | Lesen | - | Lesen |
| **Dokumentation** | Vollzugriff | Lesen/Schreiben | Lesen | Lesen | Lesen |

### Daten-Berechtigungen

| Datenklassifizierung | Administrator | Power User | Operator | Standard User | Read-Only |
|---|---|---|---|---|---|
| **Public** | Vollzugriff | Lesen/Schreiben | Lesen | Lesen | Lesen |
| **Internal** | Vollzugriff | Lesen/Schreiben | Lesen | Lesen | Lesen |
| **Confidential** | Vollzugriff | Nach Bedarf | - | - | Nach Bedarf |
| **Restricted** | Nach Bedarf | - | - | - | - |

## Access Request Prozess

### Zugriffs-Anforderung

```
┌─────────────────┐
│ 1. Antrag       │
│    stellen      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 2. Manager      │
│    Genehmigung  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 3. Security     │
│    Review       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 4. Provisionierung│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 5. Bestätigung  │
└─────────────────┘
```

### Antragsprozess

#### 1. Antrag stellen
**Wer:** Benutzer oder Manager  
**Wie:** Ticket im Service Desk System  
**Informationen:**
- Benutzername
- Angeforderte Rolle/Berechtigung
- Geschäftliche Begründung
- Zeitraum (falls temporär)
- Manager-Genehmigung

#### 2. Manager-Genehmigung
**Wer:** Direkter Vorgesetzter  
**Prüfung:**
- Geschäftliche Notwendigkeit
- Least Privilege Prinzip
- Separation of Duties

**Entscheidung:** Genehmigen / Ablehnen / Rückfragen

#### 3. Security Review
**Wer:** [TODO] oder Security Team  
**Prüfung:**
- Compliance-Anforderungen
- Risikobewertung
- Konfliktprüfung (Separation of Duties)

**Entscheidung:** Genehmigen / Ablehnen / Anpassen

#### 4. Provisionierung
**Wer:** {{ meta-organisation-roles.role_IT_Operations_Manager }} oder IT Operations  
**Aktivitäten:**
- Account erstellen/ändern
- Berechtigungen zuweisen
- MFA einrichten (falls erforderlich)
- Dokumentation in CMDB

**SLA:** Innerhalb 1 Arbeitstag

#### 5. Bestätigung
**Wer:** IT Operations  
**Aktivitäten:**
- Benutzer informieren
- Zugangsdaten bereitstellen
- Dokumentation abschließen
- Ticket schließen

## Privileged Access Management (PAM)

### Privilegierte Accounts

#### Definition
Privilegierte Accounts haben erweiterte Berechtigungen und Zugriff auf kritische Systeme.

**Beispiele:**
- Root/Administrator-Accounts
- Service-Accounts
- Database-Admin-Accounts
- Network-Admin-Accounts
- Backup-Admin-Accounts

### PAM-Anforderungen

| Anforderung | Beschreibung | Umsetzung |
|---|---|---|
| **Separate Accounts** | Privilegierte Accounts getrennt von Standard-Accounts | [TODO] |
| **MFA** | Multi-Faktor-Authentifizierung Pflicht | [TODO] |
| **Session Recording** | Aufzeichnung privilegierter Sessions | [TODO] |
| **Just-in-Time Access** | Temporäre Rechtevergabe | [TODO] |
| **Password Vault** | Zentrale Passwortverwaltung | [TODO] |
| **Regular Rotation** | Regelmäßige Passwort-Rotation | [TODO] |
| **Audit Logging** | Vollständige Protokollierung | [TODO] |

### PAM-System

**System:** [TODO: z.B. CyberArk, BeyondTrust, Thycotic]  
**Verantwortlich:** [TODO]  
**Zugriff:** [TODO: PAM-System-URL]

## Service Accounts

### Service Account Management

**Definition:** Accounts für automatisierte Prozesse und Systemintegrationen

**Anforderungen:**
- Eindeutige Benennung (z.B. `svc_backup`, `svc_monitoring`)
- Dokumentation in CMDB
- Minimale Berechtigungen
- Keine interaktiven Logins
- Regelmäßige Passwort-Rotation
- Überwachung der Nutzung

### Service Account Inventar

| Service Account | Verwendung | System | Berechtigungen | Owner |
|---|---|---|---|---|
| `svc_backup` | Backup-Prozesse | Backup-System | Lesen, Backup | Backup Admin |
| `svc_monitoring` | Monitoring | Monitoring-System | Lesen | Monitoring Team |
| `svc_integration` | System-Integration | Integration-Platform | API-Zugriff | Integration Team |
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## Access Review Prozess

### Regelmäßige Reviews

#### Quartalsweise Reviews
**Frequenz:** Alle 3 Monate  
**Umfang:** Alle Benutzer-Berechtigungen  
**Verantwortlich:** Manager + IT Operations  
**Prozess:**
1. Review-Report generieren
2. Manager prüfen Berechtigungen ihrer Mitarbeiter
3. Nicht mehr benötigte Berechtigungen entfernen
4. Änderungen dokumentieren

#### Jährliche Reviews
**Frequenz:** Jährlich  
**Umfang:** Vollständiger Access Review  
**Verantwortlich:** [TODO]  
**Prozess:**
1. Umfassender Audit aller Accounts
2. Privilegierte Accounts prüfen
3. Service Accounts validieren
4. Compliance-Check
5. Audit-Report erstellen

### Automatische Reviews

**Trigger:**
- Mitarbeiter-Wechsel (Abteilung/Rolle)
- Projekt-Ende
- Inaktive Accounts (> 90 Tage)
- Ablauf temporärer Berechtigungen

**Aktion:**
- Automatische Benachrichtigung an Manager
- Deaktivierung nach Frist
- Dokumentation

## Onboarding und Offboarding

### Onboarding-Prozess

#### Neuer Mitarbeiter
**Trigger:** HR-Benachrichtigung  
**Zeitrahmen:** Vor erstem Arbeitstag

**Aktivitäten:**
1. [ ] Account erstellen
2. [ ] Basis-Berechtigungen zuweisen
3. [ ] E-Mail-Account einrichten
4. [ ] VPN-Zugang bereitstellen
5. [ ] MFA einrichten
6. [ ] Zugangsdaten bereitstellen
7. [ ] Dokumentation in CMDB
8. [ ] Willkommens-E-Mail senden

**Verantwortlich:** {{ meta-organisation-roles.role_Service_Desk_Lead }}

### Offboarding-Prozess

#### Mitarbeiter-Austritt
**Trigger:** HR-Benachrichtigung  
**Zeitrahmen:** Am letzten Arbeitstag

**Aktivitäten:**
1. [ ] Account deaktivieren
2. [ ] Alle Berechtigungen entfernen
3. [ ] E-Mail-Weiterleitung einrichten (falls erforderlich)
4. [ ] VPN-Zugang sperren
5. [ ] Hardware zurücknehmen
6. [ ] Daten archivieren
7. [ ] Dokumentation aktualisieren
8. [ ] Manager informieren

**Verantwortlich:** {{ meta-organisation-roles.role_Service_Desk_Lead }}

#### Rollenwechsel
**Trigger:** HR-Benachrichtigung oder Manager-Anfrage  
**Zeitrahmen:** Zum Wechseldatum

**Aktivitäten:**
1. [ ] Alte Berechtigungen entfernen
2. [ ] Neue Berechtigungen zuweisen
3. [ ] Access Review durchführen
4. [ ] Dokumentation aktualisieren
5. [ ] Benutzer informieren

## Compliance und Auditing

### Compliance-Anforderungen

| Standard | Anforderung | Umsetzung |
|---|---|---|
| **DSGVO** | Zugriffskontrolle auf personenbezogene Daten | RBAC, Audit Logging |
| **ISO 27001** | Access Control Policy | Dieses Dokument |
| **SOX** | Separation of Duties | Rollen-Trennung |
| **PCI DSS** | Restricted Access to Cardholder Data | Berechtigungsmatrix |

### Audit-Logging

**Protokollierte Events:**
- Login-Versuche (erfolgreich und fehlgeschlagen)
- Berechtigungsänderungen
- Privilegierte Aktionen
- Zugriff auf sensible Daten
- Account-Erstellung/-Löschung
- Passwort-Änderungen

**Log-Retention:** [TODO: z.B. 1 Jahr]  
**Log-System:** [TODO: z.B. Splunk, ELK]  
**Verantwortlich:** [TODO]

### Audit-Reports

**Monatliche Reports:**
- Neue Accounts
- Gelöschte Accounts
- Berechtigungsänderungen
- Fehlgeschlagene Login-Versuche
- Privilegierte Zugriffe

**Quartalsweise Reports:**
- Access Review Ergebnisse
- Compliance-Status
- Risiko-Assessment
- Verbesserungsvorschläge

## Notfall-Zugriff

### Break-Glass-Accounts

**Definition:** Notfall-Accounts für kritische Situationen

**Verwendung:**
- Nur bei kritischen Ausfällen
- Wenn normale Zugriffswege nicht verfügbar
- Nach Genehmigung durch [TODO]

**Anforderungen:**
- Physisch gesicherte Passwörter
- Vollständige Protokollierung
- Sofortige Benachrichtigung an Management
- Post-Incident-Review

**Accounts:**
- `emergency_admin` - Vollzugriff auf alle Systeme
- `emergency_network` - Netzwerk-Notfallzugriff

**Passwort-Verwaltung:**
- Versiegelte Umschläge im Safe
- Zugriff nur durch [TODO] oder [TODO]

## Kontakte

**Access Management Team:**
- **IT Operations Manager:** {{ meta-organisation-roles.role_IT_Operations_Manager }} - {{ meta-organisation-roles.role_IT_Operations_Manager_email }}
- **CISO:** [TODO] - {{ meta-organisation-roles.role_CISO_email }}
- **Service Desk Lead:** {{ meta-organisation-roles.role_Service_Desk_Lead }} - {{ meta-organisation-roles.role_Service_Desk_Lead_email }}
- **CIO:** [TODO] - {{ meta-organisation-roles.role_CIO_email }}

**Notfall-Kontakte:**
- **Break-Glass-Freigabe:** [TODO] - {{ meta-organisation-roles.role_CIO_phone }}
- **Security-Incident:** [TODO] - {{ meta-organisation-roles.role_CISO_phone }}

**Dokumentverantwortlicher:** [TODO]  
**Genehmigt durch:** [TODO]  
**Version:** 0  
**Organisation:** AdminSend GmbH

