
Document-ID: tisax-0150

Status: Draft
Classification: Internal

# Benutzerzugriffsverwaltung

**Dokument-ID:** TISAX-0150
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

## Zweck

Dieses Dokument beschreibt die Prozesse und Verfahren für die Verwaltung von Benutzerzugriffen gemäß TISAX-Anforderungen.

## Geltungsbereich

Dieses Dokument gilt für alle Benutzerkonten und Zugriffe in [TODO].

## Benutzer-Lebenszyklus

### 1. Onboarding

**Neue Mitarbeiter:**
- Antrag durch HR-Abteilung
- Genehmigung durch Vorgesetzten
- Erstellung von Benutzerkonten
- Zuweisung von Standard-Berechtigungen
- Schulung vor Zugriffsvergabe

**Externe Benutzer:**
- Vertragliche Vereinbarung erforderlich
- Sponsorship durch internen Mitarbeiter
- Zeitlich begrenzte Zugriffe
- Erweiterte Überwachung

### 2. Änderungen

**Rollenwechsel:**
- Überprüfung bestehender Berechtigungen
- Anpassung an neue Rolle
- Entfernung nicht mehr benötigter Rechte
- Dokumentation der Änderungen

**Zusätzliche Berechtigungen:**
- Antrag mit Begründung
- Genehmigung durch Vorgesetzten und Information Owner
- Zeitlich begrenzt oder permanent
- Regelmäßige Überprüfung

### 3. Offboarding

**Geplanter Austritt:**
- Deaktivierung am letzten Arbeitstag
- Rückgabe von Zugangsmitteln
- Archivierung von Daten
- Dokumentation des Prozesses

**Ungeplanter Austritt:**
- Sofortige Sperrung aller Zugriffe
- Sicherstellung der Datenintegrität
- Überprüfung auf Sicherheitsvorfälle
- Dokumentation

## Benutzerkonto-Verwaltung

### Konto-Typen

**Standard-Benutzerkonten:**
- Für reguläre Mitarbeiter
- Standard-Berechtigungen
- Normale Überwachung

**Privilegierte Konten:**
- Für administrative Tätigkeiten
- Erhöhte Sicherheitsanforderungen
- Intensive Überwachung

**Service-Konten:**
- Für Anwendungen und Services
- Technische Konten ohne interaktive Anmeldung
- Automatisierte Verwaltung

**Gast-Konten:**
- Für temporäre Zugriffe
- Zeitlich begrenzt
- Eingeschränkte Berechtigungen

### Konto-Richtlinien

**Namenskonventionen:**
- Format: [TODO]
- Eindeutige Identifikation
- Keine persönlichen Informationen in Service-Konten

**Passwort-Richtlinien:**
- Siehe Zugriffskontroll-Richtlinie
- Regelmäßige Änderung
- Keine Weitergabe

**Konto-Sperrung:**
- Nach [TODO] Fehlversuchen
- Automatische Entsperrung nach [TODO] Minuten
- Manuelle Entsperrung durch IT-Support

## Berechtigungsverwaltung

### Berechtigungsmodell

**Rollenbasiert:**
- Vordefinierte Rollen
- Basierend auf Jobfunktionen
- Regelmäßig überprüft

**Gruppenbasiert:**
- Active Directory Gruppen
- Vereinfachte Verwaltung
- Automatische Vererbung

### Berechtigungsantrag

**Prozess:**
1. Benutzer oder Vorgesetzter stellt Antrag
2. Geschäftliche Begründung erforderlich
3. Genehmigung durch Vorgesetzten
4. Genehmigung durch Information Owner (bei Datenzugriff)
5. Implementierung durch IT
6. Bestätigung an Antragsteller

**Dokumentation:**
- Alle Anträge werden dokumentiert
- Genehmigungen werden archiviert
- Audit-Trail wird geführt

### Berechtigungsentzug

**Automatisch:**
- Bei Austritt
- Bei Ablauf zeitlich begrenzter Rechte
- Bei Inaktivität ([TODO] Tage)

**Manuell:**
- Bei Rollenwechsel
- Bei Sicherheitsvorfällen
- Auf Antrag

## Access Reviews

### Regelmäßige Überprüfung

**Quartalsweise:**
- Überprüfung durch Vorgesetzte
- Bestätigung der Notwendigkeit
- Entfernung nicht benötigter Rechte

**Jährlich:**
- Vollständige Rezertifizierung
- Überprüfung aller Berechtigungen
- Dokumentation der Ergebnisse

### Prozess

1. Automatische Generierung von Review-Listen
2. Versand an Vorgesetzte
3. Überprüfung und Bestätigung
4. Eskalation bei fehlender Rückmeldung
5. Implementierung von Änderungen
6. Dokumentation und Reporting

## Privilegierte Zugriffe

### Verwaltung

**Separate Konten:**
- Getrennt von Standard-Konten
- Erhöhte Sicherheitsanforderungen
- Umfassende Protokollierung

**Just-in-Time Access:**
- Temporäre Aktivierung
- Zeitlich begrenzt
- Automatische Deaktivierung

**Privileged Access Management (PAM):**
- Zentrale Verwaltung
- Session-Aufzeichnung
- Automatische Passwortrotation

### Überwachung

- Echtzeit-Monitoring
- Alarmierung bei Anomalien
- Regelmäßige Auditierung
- Compliance-Reporting

## Externe Benutzer

### Anforderungen

**Vertragliche Basis:**
- NDA erforderlich
- Vertragliche Vereinbarung
- Haftungsregelung

**Sponsorship:**
- Interner Sponsor erforderlich
- Verantwortung für externe Benutzer
- Regelmäßige Überprüfung

### Verwaltung

**Zugriffsvergabe:**
- Antrag durch Sponsor
- Genehmigung durch Management
- Zeitlich begrenzt
- Eingeschränkte Berechtigungen

**Überwachung:**
- Erweiterte Protokollierung
- Regelmäßige Überprüfung
- Automatische Benachrichtigung bei Ablauf

## Service-Konten

### Verwaltung

**Erstellung:**
- Antrag mit technischer Begründung
- Genehmigung durch IT-Manager
- Dokumentation des Verwendungszwecks
- Zuweisung eines Verantwortlichen

**Sicherheit:**
- Starke, zufällige Passwörter
- Regelmäßige Passwortrotation
- Minimale Berechtigungen
- Keine interaktive Anmeldung

**Überwachung:**
- Protokollierung aller Aktivitäten
- Regelmäßige Überprüfung der Nutzung
- Identifikation ungenutzter Konten
- Deaktivierung nicht benötigter Konten

## Inaktive Konten

### Erkennung

Konten gelten als inaktiv nach:
- [TODO] Tagen ohne Anmeldung
- Keine Aktivität in Systemen
- Keine geplante Nutzung

### Maßnahmen

**Warnung:**
- Benachrichtigung an Benutzer und Vorgesetzten
- [TODO] Tage vor Deaktivierung

**Deaktivierung:**
- Automatische Deaktivierung
- Benachrichtigung an Stakeholder
- Möglichkeit zur Reaktivierung

**Löschung:**
- Nach [TODO] Tagen Inaktivität
- Archivierung relevanter Daten
- Endgültige Entfernung

## Notfallzugriffe

### Break-Glass-Konten

**Zweck:**
- Zugriff bei Notfällen
- Wenn normale Authentifizierung nicht möglich
- Für kritische Systemwiederherstellung

**Verwaltung:**
- Passwörter in versiegelten Umschlägen
- Mehrere Personen erforderlich
- Umfassende Protokollierung
- Sofortige Eskalation bei Nutzung

**Nachbereitung:**
- Überprüfung der Nutzung
- Passwortänderung
- Dokumentation
- Management-Reporting

## Überwachung und Reporting

### Monitoring

**Echtzeit:**
- Fehlgeschlagene Anmeldeversuche
- Privilegierte Zugriffe
- Ungewöhnliche Aktivitäten
- Zugriffe außerhalb der Geschäftszeiten

**Regelmäßig:**
- Anzahl aktiver Konten
- Anzahl inaktiver Konten
- Anzahl privilegierter Konten
- Anzahl externer Benutzer

### Reporting

**Monatlich:**
- Konto-Statistiken
- Access Review Status
- Inaktive Konten
- Sicherheitsvorfälle

**Quartalsweise:**
- Compliance-Status
- Trend-Analysen
- Verbesserungsempfehlungen

## TISAX-spezifische Anforderungen

### VDA ISA Kontrollen

Dieses Dokument adressiert:
- **3.2.1**: Benutzerzugriffsverwaltung
- **3.2.2**: Bereitstellung von Benutzerzugriffen
- **3.2.3**: Verwaltung privilegierter Zugriffsrechte
- **3.2.4**: Verwaltung geheimer Authentifizierungsinformationen

### Assessment-Nachweise

- Prozessdokumentation
- Beispiele für Zugriffsgenehmigungen
- Access Review Berichte
- Audit-Logs
- Schulungsnachweise

## Verantwortlichkeiten

- **Identity & Access Management Team**: Tägliche Verwaltung
- **IT-Support**: Erste Anlaufstelle für Benutzer
- **Vorgesetzte**: Genehmigung und Rezertifizierung
- **Information Owner**: Genehmigung von Datenzugriffen
- **CISO**: Überwachung und Compliance

## Kennzahlen

[TODO] misst:
- Anzahl aktiver Benutzerkonten
- Durchschnittliche Zeit bis zur Zugriffsvergabe (Ziel: <4 Stunden)
- Anzahl überfälliger Access Reviews (Ziel: 0)
- Anzahl inaktiver Konten (Ziel: <5%)
- Anzahl Zugriffsverletzungen (Ziel: 0)



