# Policy: Kryptografie und Schlüsselmanagement

**Dokument-ID:** 0260
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
This policy establishes the principles for cryptographic controls and key management.
It ensures that cryptography is used appropriately to protect information confidentiality,
integrity, and authenticity. Customize based on your organization's cryptographic
requirements and compliance obligations.

ISO 27001:2022 Annex A Reference: A.8.24
-->

## 1. Zweck

Diese Policy definiert die Grundsätze für den Einsatz kryptografischer Verfahren und das Management kryptografischer Schlüssel der **{{ meta-organisation.name }}**. Sie stellt sicher, dass Informationen durch angemessene kryptografische Kontrollen geschützt werden und Schlüssel sicher verwaltet werden.

## 2. Geltungsbereich

Diese Policy gilt für:

- **Organisationseinheiten:** Alle Abteilungen und Standorte der {{ meta-organisation.name }}
- **Systeme:** Alle IT-Systeme, Anwendungen, Datenbanken, Netzwerke, Cloud-Services
- **Daten:** Alle Daten in Ruhe (Data at Rest), in Bewegung (Data in Transit) und in Verarbeitung (Data in Use)
- **Kryptografische Verfahren:** Verschlüsselung, Hashing, digitale Signaturen, Zertifikate
- **Standorte:** [[ netbox.site.name ]] und alle weiteren Betriebsstandorte

**Ausnahmen:** Ausnahmen sind nur über den definierten Ausnahmenprozess (`0640_Policy_Ausnahmen_und_Risk_Waivers.md`) zulässig.

## 3. Grundsätze (Policy Statements)

### 3.1 Risikoorientierter Einsatz von Kryptografie
Kryptografische Verfahren werden auf Basis einer Risikoanalyse eingesetzt. Der Schutzbedarf der Informationen bestimmt die Stärke und Art der kryptografischen Kontrollen.

### 3.2 Verschlüsselung sensibler Daten
Sensible und vertrauliche Daten werden sowohl bei der Speicherung (Data at Rest) als auch bei der Übertragung (Data in Transit) verschlüsselt:
- **Data at Rest:** Verschlüsselung von Datenbanken, Dateisystemen, Backups, mobilen Geräten
- **Data in Transit:** TLS/SSL für Netzwerkkommunikation, VPN für Remote-Zugriffe
- **Data in Use:** Verschlüsselung im Arbeitsspeicher wo technisch möglich (z.B. Confidential Computing)

### 3.3 Verwendung anerkannter Algorithmen
Es werden ausschließlich anerkannte und standardisierte kryptografische Algorithmen eingesetzt:
- Symmetrische Verschlüsselung: AES-256 oder höher
- Asymmetrische Verschlüsselung: RSA-2048 oder höher, ECC mit mindestens 256 Bit
- Hashing: SHA-256 oder höher
- Veraltete Algorithmen (MD5, SHA-1, DES, 3DES) sind untersagt

### 3.4 Schlüsselmanagement-Lebenszyklus
Kryptografische Schlüssel werden über ihren gesamten Lebenszyklus sicher verwaltet:
- **Generierung:** Sichere Zufallszahlengeneratoren, ausreichende Schlüssellänge
- **Speicherung:** Hardware Security Modules (HSM), Key Management Systems (KMS)
- **Verteilung:** Sichere Übertragungskanäle, Authentifizierung der Empfänger
- **Rotation:** Regelmäßige Schlüsselrotation basierend auf Risiko und Compliance-Anforderungen
- **Archivierung:** Sichere Aufbewahrung für Entschlüsselung historischer Daten
- **Vernichtung:** Sichere Löschung nicht mehr benötigter Schlüssel

### 3.5 Trennung von Schlüsseln und Daten
Kryptografische Schlüssel werden getrennt von den verschlüsselten Daten gespeichert. Schlüssel dürfen nicht im Klartext in Konfigurationsdateien oder Quellcode abgelegt werden.

### 3.6 Zertifikatsmanagement
Digitale Zertifikate werden zentral verwaltet:
- Verwendung vertrauenswürdiger Certificate Authorities (CA)
- Regelmäßige Überprüfung und Erneuerung von Zertifikaten
- Überwachung ablaufender Zertifikate
- Sichere Speicherung privater Schlüssel

### 3.7 Kryptografische Protokolle
Sichere kryptografische Protokolle werden für die Kommunikation verwendet:
- TLS 1.2 oder höher (TLS 1.3 bevorzugt)
- SSH-2 für sichere Remote-Zugriffe
- IPsec für VPN-Verbindungen
- Veraltete Protokolle (SSL, TLS 1.0/1.1) sind untersagt

### 3.8 Compliance mit Export-Kontrollen
Der Einsatz von Kryptografie erfolgt in Übereinstimmung mit nationalen und internationalen Export-Kontrollvorschriften.

## 4. Rollen und Verantwortlichkeiten

### RACI-Matrix: Kryptografie und Schlüsselmanagement

| Aktivität | CISO | IT-Betrieb | Crypto Officer | Entwicklung | Compliance |
|-----------|------|------------|----------------|-------------|------------|
| Policy-Erstellung | R/A | C | C | C | C |
| Krypto-Architektur | A | C | R | C | I |
| Schlüssel-Generierung | C | R | R/A | I | I |
| Schlüssel-Rotation | C | R | R/A | I | I |
| Zertifikats-Management | C | R | R/A | I | I |
| Krypto-Monitoring | A | C | R | I | C |
| Compliance-Prüfung | C | I | C | I | R/A |

**Legende:** R = Responsible (Durchführung), A = Accountable (Verantwortlich), C = Consulted (Konsultiert), I = Informed (Informiert)

### Schlüsselrollen

- **Policy Owner:** {{ meta-organisation-roles.role_CISO }} (CISO)
- **Crypto Officer:** {{ meta-handbook.it_crypto_officer }}
- **Key Management Verantwortlicher:** {{ meta-handbook.it_key_manager }}
- **Umsetzungsverantwortliche:** IT-Betrieb, Entwicklung
- **Kontroll-/Prüfinstanz:** ISMS, Internal Audit, Compliance

## 5. Ableitungen (Richtlinien/Standards/Prozesse)

Details zur Umsetzung werden in nachgelagerten Dokumenten geregelt:

### Zugehörige Richtlinien
- **0270_Richtlinie_Key_Management_und_Verschluesselung.md** - Detaillierte Implementierungsrichtlinie
- `0280_Policy_Datenklassifizierung_und_Informationshandling.md` - Data Classification Policy
- `0460_Policy_Lieferanten_und_Cloud_Sicherheit.md` - Cloud Security Policy
- `0600_Policy_Netzwerksicherheit.md` - Network Security Policy

### Zugehörige Standards/Baselines
- Kryptografische Algorithmen-Standard
- Schlüssellängen-Anforderungen
- TLS/SSL-Konfigurationsstandard
- Zertifikats-Lifecycle-Standard

### Zugehörige Prozesse
- Schlüssel-Generierungs- und Rotationsprozess
- Zertifikats-Erneuerungsprozess
- Incident Response bei Schlüsselkompromittierung
- Krypto-Agility-Prozess (Migration zu neuen Algorithmen)

## 6. Compliance, Monitoring und Durchsetzung

### Messgrößen und KPIs
- Anzahl verschlüsselter Systeme und Datenbanken
- Verschlüsselungsrate sensibler Daten (Ziel: 100%)
- Anzahl ablaufender Zertifikate (Ziel: 0 abgelaufene Zertifikate)
- Durchschnittliche Schlüsselrotationszeit
- Anzahl Verstöße gegen Krypto-Standards
- Anzahl kompromittierter Schlüssel

### Nachweise und Evidence
- Verschlüsselungs-Inventar
- Schlüssel-Management-Logs
- Zertifikats-Register
- Krypto-Compliance-Reports
- Penetration-Test-Ergebnisse
- Audit-Berichte zu kryptografischen Kontrollen

### Konsequenzen bei Verstößen
Verstöße gegen diese Policy werden nach den geltenden HR- und Compliance-Prozessen behandelt:
- **Verwendung schwacher Algorithmen:** Sofortige Remediation, Nachschulung
- **Unsichere Schlüsselspeicherung:** Sofortige Schlüsselrotation, Untersuchung
- **Schlüsselkompromittierung:** Incident Response, Revocation, forensische Analyse
- **Wiederholte Verstöße:** Arbeitsrechtliche Konsequenzen

## 7. Ausnahmen

Ausnahmen von dieser Policy sind nur in begründeten Ausnahmefällen zulässig:

- **Ausnahmenprozess:** Siehe `0640_Policy_Ausnahmen_und_Risk_Waivers.md`
- **Genehmigung:** Ausnahmen müssen vom CISO und Crypto Officer genehmigt werden
- **Dokumentation:** Alle Ausnahmen werden im Risikoregister dokumentiert
- **Befristung:** Ausnahmen sind grundsätzlich zeitlich befristet und werden regelmäßig überprüft
- **Kompensationsmaßnahmen:** Ausnahmen erfordern alternative Sicherheitsmaßnahmen

## 8. Referenzen

### Interne Dokumente
- `0010_ISMS_Informationssicherheitsleitlinie.md` - ISMS Policy
- `0270_Richtlinie_Key_Management_und_Verschluesselung.md` - Detailed Guideline
- `0280_Policy_Datenklassifizierung_und_Informationshandling.md` - Data Classification Policy
- `0080_ISMS_Risikoregister_Template.md` - Risk Register

### Externe Standards und Vorgaben
- **ISO/IEC 27001:2022 Annex A.8.24** - Use of cryptography
- **ISO/IEC 27002:2022** - Information security controls
- **NIST SP 800-57** - Recommendation for Key Management
- **NIST SP 800-175B** - Guideline for Using Cryptographic Standards
- **BSI TR-02102** - Kryptographische Verfahren: Empfehlungen und Schlüssellängen
- **FIPS 140-2/140-3** - Security Requirements for Cryptographic Modules
- **eIDAS-Verordnung (EU 910/2014)** - Elektronische Identifizierung und Vertrauensdienste

**Genehmigt durch:**  
{{ meta-handbook.management_ceo }}, Geschäftsführung  
Datum: {{ meta-handbook.modifydate }}

**Nächster Review:** {{ meta-handbook.next_review }} (jährlich oder anlassbezogen)

