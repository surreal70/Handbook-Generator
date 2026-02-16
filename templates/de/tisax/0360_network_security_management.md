---
Document-ID: tisax-0360
Owner: {{ meta.author }}
Version: {{ meta.version }}
Status: Draft
Classification: Internal
Last Update: {{ meta.date }}
---

# Netzwerksicherheitsmanagement

## Zweck

Dieses Dokument beschreibt die Maßnahmen für Netzwerksicherheit gemäß TISAX-Anforderungen.

## Geltungsbereich

Dieses Dokument gilt für alle Netzwerke von {{ source.organization_name }}.

## Netzwerksegmentierung

### Sicherheitszonen

**DMZ (Demilitarized Zone):**
- Öffentlich zugängliche Systeme
- Strenge Firewall-Regeln
- Überwachung

**Interne Netzwerke:**
- Geschäftsnetzwerk
- Entwicklungsnetzwerk
- Verwaltungsnetzwerk

**Hochsicherheitsnetzwerk:**
- Kritische Systeme
- Strenge Zugriffskontrolle
- Umfassende Überwachung

### Netzwerkzugriffskontrolle

**Anforderungen:**
- 802.1X Authentifizierung
- NAC (Network Access Control)
- VLAN-Segmentierung
- Firewall-Regeln

## Firewall-Management

### Firewall-Regeln

**Prinzipien:**
- Default Deny
- Least Privilege
- Dokumentierte Regeln
- Regelmäßige Überprüfung

**Genehmigungsprozess:**
- Antrag mit Begründung
- Risikoanalyse
- Genehmigung durch Netzwerksicherheit
- Dokumentation

### Firewall-Typen

**Perimeter-Firewall:**
- Schutz des Gesamtnetzwerks
- Redundante Konfiguration
- Hochverfügbarkeit

**Interne Firewalls:**
- Segmentierung
- Schutz kritischer Bereiche

**Host-basierte Firewalls:**
- Schutz einzelner Systeme
- Zentrale Verwaltung

## Intrusion Detection/Prevention

### IDS/IPS-Systeme

**Funktionen:**
- Erkennung von Angriffen
- Automatische Blockierung
- Alarmierung
- Reporting

**Platzierung:**
- Netzwerkgrenzen
- Kritische Segmente
- DMZ

## VPN-Management

### Remote Access VPN

**Anforderungen:**
- Multi-Faktor-Authentifizierung
- Starke Verschlüsselung
- Endpoint-Compliance-Check
- Protokollierung

### Site-to-Site VPN

**Anforderungen:**
- Verschlüsselte Verbindungen
- Redundante Verbindungen
- Überwachung
- Dokumentation

## Wireless Security

### WLAN-Sicherheit

**Anforderungen:**
- WPA3 Verschlüsselung
- 802.1X Authentifizierung
- Separate SSIDs für Gäste
- Regelmäßige Sicherheitsscans

### Gast-WLAN

**Anforderungen:**
- Isoliert vom internen Netzwerk
- Bandbreitenbegrenzung
- Zeitliche Begrenzung
- Akzeptanz von Nutzungsbedingungen

## Netzwerküberwachung

### Monitoring

**Überwachte Parameter:**
- Netzwerkverkehr
- Bandbreitennutzung
- Sicherheitsereignisse
- Performance

**Tools:**
- Network Monitoring System
- SIEM-Integration
- Flow-Analyse

## TISAX-spezifische Anforderungen

### VDA ISA Kontrollen

Dieses Dokument adressiert:
- **6.6**: Netzwerksicherheitsmanagement
- **7.1**: Netzwerksicherheit

### Assessment-Nachweise

- Netzwerkdiagramme
- Firewall-Regeln
- IDS/IPS-Konfiguration
- Monitoring-Berichte

## Kennzahlen

{{ source.organization_name }} misst:
- Anzahl blockierter Angriffe
- Netzwerkverfügbarkeit
- Anzahl Firewall-Regeländerungen

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.date }} | {{ meta.author }} | Erste Erstellung |

<!-- Ende des Templates -->
