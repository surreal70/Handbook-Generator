# Firewall-Konfiguration

**Dokument-ID:** PCI-0100
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Genehmigt durch:** {{ meta-handbook.approver }}
**Revision:** [TODO]
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Klassifizierung:** {{ meta-handbook.classification }}
**Letzte Aktualisierung:** {{ meta-handbook.modifydate }}
**Template Version:** [TODO]

---

---

<!-- 
TEMPLATE AUTHOR NOTE:
This template documents firewall configuration standards.
It aligns with PCI-DSS v4.0 Requirement 1 (Install and Maintain Network Security Controls).

Customization required:
- Document firewall standards and configurations
- Define rule management procedures
- Include change management process
- Document review procedures
-->

## 1. Zweck

Dieses Dokument definiert die Firewall-Konfigurationsstandards für {{ meta-organisation.name }} gemäß PCI-DSS Requirement 1.

### 1.1 Ziele

- **Netzwerksicherheit:** Schutz des CDE durch Firewall-Kontrollen
- **Zugriffskontrolle:** Restriktion unautorisierten Netzwerkzugriffs
- **Compliance:** Erfüllung von PCI-DSS Requirement 1
- **Dokumentation:** Nachvollziehbare Firewall-Konfiguration

### 1.2 Geltungsbereich

**Betroffene Systeme:**
- Perimeter-Firewalls (Internet-Grenze)
- Interne Firewalls (CDE-Segmentierung)
- Host-basierte Firewalls (Server, Workstations)
- Cloud-Firewalls (falls zutreffend)

## 2. Firewall-Standards

### 2.1 Grundprinzipien

**Default Deny:**
- Alle Verbindungen standardmäßig blockiert
- Nur explizit genehmigte Verbindungen erlaubt
- Dokumentation aller Ausnahmen erforderlich

**Least Privilege:**
- Minimale erforderliche Zugriffsrechte
- Spezifische Quell- und Ziel-IP-Adressen
- Spezifische Ports und Protokolle

**Defense in Depth:**
- Mehrere Firewall-Ebenen
- Perimeter + interne Segmentierung
- Host-basierte Firewalls als zusätzliche Schicht

### 2.2 Firewall-Architektur

**Firewall-Ebenen:**

1. **Perimeter Firewall:**
   - Schutz vor Internet-Bedrohungen
   - Eingehender und ausgehender Traffic
   - DMZ für öffentliche Dienste

2. **Internal Firewall:**
   - CDE-Segmentierung
   - Trennung von Corporate und CDE
   - Zugriffskontrolle zwischen Segmenten

3. **Host-based Firewall:**
   - Schutz einzelner Systeme
   - Zusätzliche Verteidigungsebene
   - Schutz bei Netzwerk-Kompromittierung

## 3. Firewall-Regelmanagement

### 3.1 Regel-Anforderungen

**Jede Firewall-Regel muss enthalten:**
- Eindeutige Regel-ID
- Quelle (IP-Adresse/Netzwerk)
- Ziel (IP-Adresse/Netzwerk)
- Port/Protokoll
- Aktion (Allow/Deny)
- Business-Begründung
- Genehmiger
- Erstellungsdatum
- Überprüfungsdatum

### 3.2 Regel-Genehmigungsprozess

**Prozess für neue Regeln:**

1. **Anfrage:** Change Request mit Begründung
2. **Security Review:** Bewertung durch IT Security
3. **Genehmigung:** CISO-Freigabe für CDE-Regeln
4. **Implementation:** Konfiguration durch Network Team
5. **Dokumentation:** Aktualisierung des Regelwerks
6. **Validation:** Test der Regel

**Genehmigungsmatrix:**

| Regel-Typ | Genehmiger | Dokumentation |
|-----------|------------|---------------|
| CDE-bezogen | CISO | Vollständig |
| Corporate | IT Manager | Standard |
| Temporär | IT Security | Mit Ablaufdatum |

### 3.3 Quartalsweise Regelüberprüfung

**Überprüfungsprozess:**

1. **Review aller Regeln:** Vollständige Durchsicht
2. **Validierung:** Business-Begründung noch gültig?
3. **Cleanup:** Entfernung ungenutzter Regeln
4. **Dokumentation:** Aktualisierung der Dokumentation
5. **Genehmigung:** CISO-Bestätigung

**Letzte Überprüfung:** [TODO: Datum]  
**Nächste Überprüfung:** [TODO: Datum]  
**Verantwortlich:** [TODO: Network Security Team]  

## 4. Firewall-Konfigurationsstandards

### 4.1 Perimeter-Firewall

**Eingehender Traffic (Inbound):**

| Service | Port | Protokoll | Quelle | Ziel | Erlaubt |
|---------|------|-----------|--------|------|---------|
| HTTPS | 443 | TCP | Any | Web Server (DMZ) | Ja |
| SSH | 22 | TCP | Admin IPs | Jump Server | Ja (mit MFA) |
| Alle anderen | * | * | Any | CDE | Nein |

**Ausgehender Traffic (Outbound):**

| Service | Port | Protokoll | Quelle | Ziel | Erlaubt |
|---------|------|-----------|--------|------|---------|
| HTTPS | 443 | TCP | CDE | Acquiring Bank | Ja |
| DNS | 53 | UDP | CDE | DNS Server | Ja |
| NTP | 123 | UDP | CDE | NTP Server | Ja |
| Alle anderen | * | * | CDE | Internet | Nein (Default Deny) |

### 4.2 Interne Firewall (CDE-Segmentierung)

**CDE → Corporate:**
- Standardmäßig blockiert
- Ausnahmen nur mit CISO-Genehmigung
- Logging aller Verbindungsversuche

**Corporate → CDE:**
- Nur autorisierte Admin-Zugriffe
- MFA erforderlich
- Über Jump Server/VPN
- Vollständiges Logging

### 4.3 Host-basierte Firewalls

**Anforderungen:**
- Aktiviert auf allen CDE-Systemen
- Konfiguration gemäß Hardening-Standards
- Zentrale Verwaltung (falls möglich)
- Logging aktiviert

**Beispiel-Konfiguration (Linux iptables):**
```bash
# Default Deny
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT DROP

# Allow established connections
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# Allow specific services
iptables -A INPUT -p tcp --dport 443 -j ACCEPT  # HTTPS
iptables -A INPUT -p tcp --dport 22 -s 10.1.102.0/24 -j ACCEPT  # SSH from Management

# Log dropped packets
iptables -A INPUT -j LOG --log-prefix "FW-DROP: "
```

## 5. Verbotene Konfigurationen

**Folgende Konfigurationen sind NICHT erlaubt:**

- **Any-Any-Regeln:** Keine Regeln mit Quelle=Any und Ziel=Any
- **Direkte Internet-Verbindungen:** CDE-Systeme dürfen nicht direkt mit Internet kommunizieren
- **Unverschlüsselte Protokolle:** Telnet, FTP, HTTP (außer Redirect zu HTTPS)
- **Veraltete Protokolle:** SSLv2, SSLv3, TLS 1.0, TLS 1.1
- **Undokumentierte Regeln:** Alle Regeln müssen dokumentiert sein

## 6. Änderungsmanagement

### 6.1 Emergency Changes

**Notfall-Änderungen erlaubt bei:**
- Aktiven Sicherheitsvorfällen
- Kritischen Systemausfällen
- Unmittelbarer Bedrohung

**Prozess:**
1. Mündliche Genehmigung durch CISO
2. Sofortige Implementation
3. Nachträgliche Dokumentation (innerhalb 24h)
4. Formale Genehmigung (innerhalb 48h)

### 6.2 Änderungshistorie

| Datum | Regel-ID | Änderung | Begründung | Genehmigt durch |
|-------|----------|----------|------------|-----------------|
| [TODO: 2026-01-15] | FW-105 | Neue Regel | Payment API | [TODO: CISO] |
| [TODO: 2026-02-01] | FW-042 | Entfernt | Nicht mehr benötigt | [TODO: CISO] |

## 7. Monitoring und Alerting

### 7.1 Firewall-Logging

**Logging-Anforderungen:**
- Alle blockierten Verbindungen
- Alle erlaubten Verbindungen zum/vom CDE
- Firewall-Konfigurationsänderungen
- Firewall-Systemereignisse (Start, Stop, Fehler)

**Log-Retention:** [TODO: 90 Tage online, 1 Jahr Archiv]  
**Log-Forwarding:** [TODO: SIEM-System]  

### 7.2 Alerting-Regeln

| Alert | Bedingung | Schweregrad | Benachrichtigung |
|-------|-----------|-------------|------------------|
| Unerlaubter CDE-Zugriff | Blockierte Verbindung zu CDE | Hoch | SOC + IT Security |
| Firewall-Regel-Änderung | Konfigurationsänderung | Mittel | Network Team |
| Firewall-Ausfall | Firewall nicht erreichbar | Kritisch | SOC + CISO |

## 8. Compliance-Validierung

### 8.1 Validierungsaktivitäten

**Quartalsweise:**
- Firewall-Regelüberprüfung
- Dokumentationsvalidierung
- Ungenutzter Regel-Cleanup

**Jährlich:**
- Penetrationstest der Firewall-Konfiguration
- Segmentierungsvalidierung
- Compliance-Audit

### 8.2 Validierungsdokumentation

**Erforderliche Nachweise:**
- Firewall-Konfigurationsdateien
- Regelüberprüfungsprotokolle
- Änderungsprotokolle
- Genehmigungsnachweise

<!-- End of template -->
