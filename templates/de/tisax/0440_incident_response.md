---
Document-ID: tisax-0440
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Incident Response

## Zweck

Dieses Dokument beschreibt die Incident Response Maßnahmen gemäß TISAX-Anforderungen.

## Geltungsbereich

Dieses Dokument gilt für alle Sicherheitsvorfälle in {{ source.organization_name }}.

## Incident Response Team

### Team-Struktur

**Kern-Team:**
- Incident Response Manager
- IT-Sicherheitsexperten
- Systemadministratoren
- Netzwerkspezialisten

**Erweitert Team:**
- Rechtsabteilung
- Datenschutzbeauftragter
- PR/Kommunikation
- Management

### Bereitschaft

**24/7 Verfügbarkeit:**
- Rufbereitschaft
- Eskalationsliste
- Kontaktinformationen
- Backup-Personen

## Response-Verfahren

### Sofortmaßnahmen

**Bei Malware-Infektion:**
1. Isolation des betroffenen Systems
2. Netzwerkverbindung trennen
3. Malware-Scan durchführen
4. Beweissicherung
5. Bereinigung oder Neuinstallation

**Bei unbefugtem Zugriff:**
1. Sperrung kompromittierter Konten
2. Änderung von Passwörtern
3. Überprüfung von Zugriffsprotokollen
4. Identifikation betroffener Daten
5. Forensische Analyse

**Bei Datenverlust:**
1. Umfang bestimmen
2. Ursache identifizieren
3. Wiederherstellung aus Backup
4. Validierung der Daten
5. Meldepflichten prüfen

### Eskalation

**Eskalationsstufen:**
- **Stufe 1**: IT-Support
- **Stufe 2**: Incident Response Team
- **Stufe 3**: Management
- **Stufe 4**: Externe Experten

**Eskalationskriterien:**
- Schweregrad
- Auswirkung
- Dauer
- Komplexität

## Forensische Analyse

### Beweissicherung

**Maßnahmen:**
- Speicherabbilder erstellen
- Logs sichern
- Netzwerkverkehr aufzeichnen
- Dokumentation
- Chain of Custody

### Analyse

**Aktivitäten:**
- Malware-Analyse
- Log-Analyse
- Netzwerkverkehr-Analyse
- Timeline-Erstellung
- Ursachenanalyse

## Wiederherstellung

### Recovery-Prozess

**Schritte:**
1. Validierung der Beseitigung
2. System-Wiederherstellung
3. Daten-Wiederherstellung
4. Funktionstest
5. Überwachung

### Validierung

**Überprüfung:**
- Keine Malware mehr vorhanden
- Sicherheitslücken geschlossen
- Systeme funktionsfähig
- Datenintegrität gewährleistet

## Kommunikation

### Interne Kommunikation

**Regelmäßige Updates:**
- Status-Updates
- Maßnahmen
- Zeitplan
- Nächste Schritte

### Externe Kommunikation

**Bei Bedarf:**
- Kunden
- Partner
- Behörden
- Öffentlichkeit

## TISAX-spezifische Anforderungen

### VDA ISA Kontrollen

Dieses Dokument adressiert:
- **9.2**: Incident Response

### Assessment-Nachweise

- Response-Pläne
- Incident-Berichte
- Forensische Analysen
- Kommunikationsprotokolle

## Kennzahlen

{{ source.organization_name }} misst:
- Durchschnittliche Response-Zeit
- Erfolgsrate der Wiederherstellung
- Anzahl eskalierter Incidents

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |

<!-- Ende des Templates -->
