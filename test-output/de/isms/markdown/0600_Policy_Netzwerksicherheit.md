# Policy: Netzwerksicherheit

**Dokument-ID:** 0600
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



## 1. Zweck

Diese Policy definiert die Anforderungen an die Netzwerksicherheit der **AdminSend GmbH**. Sie stellt sicher, dass Netzwerke angemessen gesichert, segmentiert und überwacht werden, um die Vertraulichkeit, Integrität und Verfügbarkeit von Informationen zu schützen.

## 2. Geltungsbereich

Diese Policy gilt für:

- **Organisationseinheiten:** Alle Abteilungen und Standorte der AdminSend GmbH
- **Netzwerke:** Alle internen und externen Netzwerke, LAN, WLAN, WAN, VPN
- **Systeme:** Firewalls, Router, Switches, Load Balancer, IDS/IPS
- **Verbindungen:** Alle Netzwerkverbindungen (intern, extern, Partner, Cloud)
- **Standorte:** [[ netbox.site.name ]] und alle weiteren Betriebsstandorte

**Ausnahmen:** Ausnahmen sind nur über den definierten Ausnahmenprozess (`0640_Policy_Ausnahmen_und_Risk_Waivers.md`) zulässig.

## 3. Grundsätze (Policy Statements)

### 3.1 Netzwerksegmentierung
Netzwerke werden nach Schutzbedarf und Funktion segmentiert. Segmentierung erfolgt durch Firewalls, VLANs und Zonen (z.B. DMZ, Produktionsnetz, Verwaltungsnetz).

### 3.2 Defense in Depth
Netzwerksicherheit folgt dem Defense-in-Depth-Prinzip. Mehrere Sicherheitsschichten schützen vor Angriffen (Perimeter, Segmentierung, Host-basiert).

### 3.3 Least Privilege Network Access
Netzwerkzugriffe folgen dem Least-Privilege-Prinzip. Nur erforderliche Verbindungen sind erlaubt (Default Deny, Whitelist-Ansatz).

### 3.4 Firewall-Management
Firewalls schützen Netzwerkgrenzen. Firewall-Regeln werden dokumentiert, regelmäßig überprüft und nach Change-Management-Prozess geändert.

### 3.5 Network Access Control (NAC)
Zugriffe auf Netzwerke werden kontrolliert. NAC stellt sicher, dass nur autorisierte und konforme Geräte Zugriff erhalten.

### 3.6 Intrusion Detection/Prevention (IDS/IPS)
Netzwerke werden auf Angriffe überwacht. IDS/IPS-Systeme erkennen und blockieren verdächtige Aktivitäten.

### 3.7 VPN und Remote Access
Remote-Zugriffe erfolgen über sichere VPN-Verbindungen. VPN-Verbindungen sind verschlüsselt und authentifiziert (MFA).

### 3.8 Wireless Security
WLAN-Netzwerke sind gesichert (WPA3, 802.1X). Gast-WLANs sind vom Produktionsnetz getrennt.

### 3.9 Network Monitoring und Logging
Netzwerkaktivitäten werden überwacht und protokolliert. Logs werden zentral gesammelt und analysiert (SIEM).

## 4. Rollen und Verantwortlichkeiten

### RACI-Matrix: Netzwerksicherheit

| Aktivität | CISO | Network Security | IT-Betrieb | SOC | Network Admin |
|-----------|------|------------------|------------|-----|---------------|
| Policy-Erstellung | R/A | R | C | C | C |
| Netzwerksegmentierung | R | R/A | R | C | R |
| Firewall-Management | C | R/A | R | C | R |
| NAC-Implementierung | C | R/A | R | C | R |
| IDS/IPS-Betrieb | C | R | C | R/A | C |
| VPN-Management | C | R/A | R | C | R |
| WLAN-Security | C | R/A | R | C | R |
| Network Monitoring | C | R | C | R/A | C |

**Legende:** R = Responsible (Durchführung), A = Accountable (Verantwortlich), C = Consulted (Konsultiert), I = Informed (Informiert)

### Schlüsselrollen

- **Policy Owner:** [TODO] (CISO)
- **Network Security Manager:** {{ meta-handbook.network_security_manager }}
- **Network Administrator:** {{ meta-handbook.network_admin }}
- **SOC Manager:** {{ meta-handbook.soc_manager }}
- **Umsetzungsverantwortliche:** IT-Betrieb, Network Team
- **Kontroll-/Prüfinstanz:** ISMS, Internal Audit, SOC

## 5. Ableitungen (Richtlinien/Standards/Prozesse)

Details zur Umsetzung werden in nachgelagerten Dokumenten geregelt:

### Zugehörige Richtlinien
- **0610_Richtlinie_Segmentierung_Firewalling_und_Network_Access_Control.md** - Detaillierte Implementierungsrichtlinie
- `0220_Policy_Zugriffssteuerung_und_Identitaetsmanagement.md` - Access Control Policy
- `0320_Policy_Logging_und_Monitoring.md` - Logging and Monitoring Policy
- `0500_Policy_Mobile_Device_und_Remote_Work.md` - Remote Work Policy

### Zugehörige Standards/Baselines
- Netzwerksegmentierungskonzept
- Firewall-Regelwerk
- NAC-Konfiguration
- IDS/IPS-Signaturen und Regeln
- VPN-Konfiguration
- WLAN-Security-Baseline

### Zugehörige Prozesse
- Firewall Change Management
- NAC Onboarding/Offboarding
- IDS/IPS Alert Response
- VPN Access Request
- Network Security Monitoring

## 6. Compliance, Monitoring und Durchsetzung

### Messgrößen und KPIs
- Netzwerksegmentierung Coverage (Ziel: 100% kritischer Systeme)
- Firewall-Regel-Review-Frequenz (Ziel: quartalsweise)
- NAC Coverage (Ziel: 100% Produktionsnetz)
- IDS/IPS Alert Response Time (Ziel: < 15 Minuten für kritische Alerts)
- VPN-Verfügbarkeit (Ziel: 99.5%)
- WLAN-Security-Compliance (Ziel: 100% WPA3)
- Anzahl blockierter Angriffe (IDS/IPS)

### Nachweise und Evidence
- Netzwerkdiagramme und Segmentierungskonzept
- Firewall-Regelwerk und Change-Logs
- NAC-Konfiguration und Device-Inventory
- IDS/IPS-Logs und Alert-Reports
- VPN-Logs und Access-Logs
- WLAN-Konfiguration und Security-Scans
- Network Monitoring Dashboards

### Konsequenzen bei Verstößen
Verstöße gegen diese Policy werden nach den geltenden HR- und Compliance-Prozessen behandelt:
- **Nicht autorisierte Firewall-Änderungen:** Incident Response, Rollback, Disziplinarmaßnahmen
- **Fehlende Segmentierung:** Nachholung, Risikobewertung
- **Unsichere WLAN-Konfiguration:** Sofortige Korrektur, Incident Response
- **Wiederholte Verstöße:** Arbeitsrechtliche Konsequenzen, Zugriffsentzug

## 7. Ausnahmen

Ausnahmen von dieser Policy sind nur in begründeten Ausnahmefällen zulässig:

- **Ausnahmenprozess:** Siehe `0640_Policy_Ausnahmen_und_Risk_Waivers.md`
- **Genehmigung:** Ausnahmen müssen vom CISO und Network Security Manager genehmigt werden
- **Dokumentation:** Alle Ausnahmen werden im Risikoregister dokumentiert
- **Befristung:** Ausnahmen sind grundsätzlich zeitlich befristet

## 8. Referenzen

### Interne Dokumente
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS Policy
- `0610_Richtlinie_Segmentierung_Firewalling_und_Network_Access_Control.md` - Detailed Guideline
- `0220_Policy_Zugriffssteuerung_und_Identitaetsmanagement.md` - Access Control Policy
- `0080_ISMS_Risikoregister_Template.md` - Risk Register

### Externe Standards und Vorgaben
- **ISO/IEC 27001:2022 Annex A.8.20** - Networks security
- **ISO/IEC 27001:2022 Annex A.8.21** - Security of network services
- **ISO/IEC 27001:2022 Annex A.8.22** - Segregation of networks
- **ISO/IEC 27001:2022 Annex A.8.23** - Web filtering
- **NIST SP 800-41** - Guidelines on Firewalls and Firewall Policy
- **NIST SP 800-97** - Establishing Wireless Robust Security Networks
- **BSI IT-Grundschutz** - NET.1.1, NET.1.2, NET.3.2

**Genehmigt durch:**  
{{ meta-handbook.management_ceo }}, Geschäftsführung  
Datum: [TODO]

**Nächster Review:** [TODO] (jährlich oder anlassbezogen)

