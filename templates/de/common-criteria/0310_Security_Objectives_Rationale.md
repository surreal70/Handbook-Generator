# Rationale für Sicherheitsziele (Security Objectives Rationale)

**Dokument-ID:** 0310  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** Entwurf / In Review / Freigegeben  
**Klassifizierung:** Intern / Vertraulich / Streng vertraulich  
**Letzte Aktualisierung:** {{ meta.date }}  

---

> **Hinweis:** Dieses Dokument ist ein Template. Ersetze alle `[TODO]`-Platzhalter und passe die Inhalte an dein spezifisches TOE (Target of Evaluation) an.

<!-- 
ANLEITUNG FÜR TEMPLATE-AUTOREN:
Dieses Template dokumentiert die Rationale (Begründung) für die Sicherheitsziele gemäß ISO/IEC 15408 (Common Criteria).

Die Rationale muss nachweisen, dass:
1. Jede Bedrohung durch mindestens ein Sicherheitsziel adressiert wird
2. Jede organisatorische Sicherheitsrichtlinie (OSP) durch mindestens ein Sicherheitsziel umgesetzt wird
3. Jede Annahme durch mindestens ein Umgebungsziel erfüllt wird
4. Jedes Sicherheitsziel auf mindestens eine Bedrohung, OSP oder Annahme zurückgeführt werden kann

Struktur:
- Rationale für TOE-Sicherheitsziele: Wie jedes O.xxx Ziel Bedrohungen/OSPs adressiert
- Rationale für Umgebungsziele: Wie jedes OE.xxx Ziel Annahmen erfüllt
- Vollständigkeitsnachweis: Alle Bedrohungen/OSPs/Annahmen sind abgedeckt

Best Practices:
- Sei präzise und spezifisch in der Begründung
- Vermeide generische Aussagen
- Zeige klare Verbindungen zwischen Zielen und Sicherheitsproblemen
- Dokumentiere auch indirekte Beziehungen (z.B. unterstützende Ziele)
-->

## 1. Einleitung

Dieses Dokument liefert die Rationale (Begründung) für die Sicherheitsziele des TOE **{{ meta.toe_name }}** und dessen Betriebsumgebung. Die Rationale demonstriert, dass die definierten Sicherheitsziele ausreichend und angemessen sind, um:

- Alle identifizierten Bedrohungen zu bewältigen
- Alle organisatorischen Sicherheitsrichtlinien (OSPs) umzusetzen
- Alle Annahmen über die Betriebsumgebung zu erfüllen

### 1.1 Zweck

Die Rationale dient als Nachweis für:
- **Vollständigkeit**: Alle Elemente der Sicherheitsproblem-Definition sind durch Ziele abgedeckt
- **Angemessenheit**: Jedes Ziel ist geeignet, die zugeordneten Bedrohungen/OSPs/Annahmen zu adressieren
- **Rückverfolgbarkeit**: Klare Verbindung zwischen Sicherheitsproblemen und Zielen

### 1.2 Methodik

Für jedes Sicherheitsziel wird dokumentiert:
1. Welche Bedrohungen, OSPs oder Annahmen es adressiert
2. Wie es diese Sicherheitsprobleme bewältigt
3. Warum es angemessen und ausreichend ist

## 2. Rationale für TOE-Sicherheitsziele

<!-- 
ANLEITUNG: Für jedes TOE-Sicherheitsziel (O.xxx) aus Template 0300:
- Liste die adressierten Bedrohungen und OSPs auf
- Erkläre, wie das Ziel diese Bedrohungen/OSPs bewältigt
- Begründe, warum das Ziel angemessen ist
-->

### 2.1 O.ACCESS_CONTROL

**Adressierte Bedrohungen:**
- T.UNAUTHORIZED_ACCESS: Unbefugter Zugriff auf geschützte Ressourcen
- T.PRIVILEGE_ESCALATION: Erlangung höherer Berechtigungen

**Adressierte OSPs:**
- P.ACCESS_CONTROL: Zugriff muss basierend auf Berechtigungen kontrolliert werden

**Rationale:**
Das Ziel O.ACCESS_CONTROL bewältigt die Bedrohungen T.UNAUTHORIZED_ACCESS und T.PRIVILEGE_ESCALATION, indem es sicherstellt, dass das TOE den Zugriff auf geschützte Ressourcen basierend auf Benutzeridentität und zugewiesenen Berechtigungen kontrolliert. Nur authentifizierte Benutzer mit entsprechenden Berechtigungen können auf Ressourcen zugreifen. Dies setzt die organisatorische Sicherheitsrichtlinie P.ACCESS_CONTROL um, die eine rollenbasierte Zugriffskontrolle vorschreibt.

**[TODO: Passe die Rationale an dein spezifisches TOE an]**

### 2.2 O.IDENTIFICATION_AUTHENTICATION

**Adressierte Bedrohungen:**
- T.MASQUERADE: Vortäuschen einer falschen Identität

**Rationale:**
Das Ziel O.IDENTIFICATION_AUTHENTICATION bewältigt die Bedrohung T.MASQUERADE, indem es sicherstellt, dass alle Benutzer eindeutig identifiziert und authentifiziert werden, bevor Zugriff auf geschützte Funktionen gewährt wird. Dies verhindert, dass Angreifer sich als legitime Benutzer ausgeben können. Das Ziel unterstützt auch O.ACCESS_CONTROL, da eine zuverlässige Identifikation Voraussetzung für eine wirksame Zugriffskontrolle ist.

**[TODO: Ergänze weitere Details zur Authentifizierung]**

### 2.3 O.AUDIT_GENERATION

**Adressierte Bedrohungen:**
- T.AUDIT_COMPROMISE: Manipulation oder Löschung von Audit-Daten

**Adressierte OSPs:**
- P.ACCOUNTABILITY: Benutzeraktionen müssen nachvollziehbar sein

**Rationale:**
Das Ziel O.AUDIT_GENERATION bewältigt die Bedrohung T.AUDIT_COMPROMISE teilweise, indem es sicherstellt, dass sicherheitsrelevante Ereignisse aufgezeichnet werden. Die Aufzeichnung ermöglicht die Nachvollziehbarkeit von Benutzeraktionen und Sicherheitsereignissen, was die organisatorische Sicherheitsrichtlinie P.ACCOUNTABILITY umsetzt. In Kombination mit O.AUDIT_PROTECTION wird ein vollständiger Schutz der Audit-Daten erreicht.

**[TODO: Definiere welche Ereignisse aufgezeichnet werden]**

### 2.4 O.AUDIT_PROTECTION

**Adressierte Bedrohungen:**
- T.AUDIT_COMPROMISE: Manipulation oder Löschung von Audit-Daten

**Rationale:**
Das Ziel O.AUDIT_PROTECTION bewältigt die Bedrohung T.AUDIT_COMPROMISE, indem es sicherstellt, dass Audit-Aufzeichnungen vor unbefugter Änderung und Löschung geschützt sind. Dies gewährleistet die Integrität und Verfügbarkeit der Audit-Daten, die für forensische Analysen und Compliance-Nachweise erforderlich sind. Das Ziel ergänzt O.AUDIT_GENERATION und stellt einen vollständigen Audit-Schutz sicher.

**[TODO: Beschreibe Schutzmechanismen]**

### 2.5 O.DATA_CONFIDENTIALITY

**Adressierte Bedrohungen:**
- T.DATA_DISCLOSURE: Unbefugte Offenlegung sensibler Daten
- T.EAVESDROPPING: Abhören von Datenübertragungen

**Adressierte OSPs:**
- P.CONFIDENTIALITY: Sensible Daten müssen vertraulich behandelt werden

**Rationale:**
Das Ziel O.DATA_CONFIDENTIALITY bewältigt die Bedrohungen T.DATA_DISCLOSURE und T.EAVESDROPPING, indem es sicherstellt, dass sensible Benutzerdaten vor unbefugter Offenlegung geschützt werden. Dies wird durch Zugriffskontrolle, Verschlüsselung und sichere Datenübertragung erreicht. Das Ziel setzt die organisatorische Sicherheitsrichtlinie P.CONFIDENTIALITY um, die den Schutz vertraulicher Informationen vorschreibt.

**[TODO: Spezifiziere geschützte Datentypen]**

### 2.6 O.CRYPTOGRAPHIC_OPERATIONS

**Adressierte Bedrohungen:**
- T.DATA_DISCLOSURE: Unbefugte Offenlegung sensibler Daten
- T.DATA_MODIFICATION: Unbefugte Änderung von Daten

**Rationale:**
Das Ziel O.CRYPTOGRAPHIC_OPERATIONS unterstützt O.DATA_CONFIDENTIALITY und O.DATA_INTEGRITY, indem es kryptografische Mechanismen zur Verschlüsselung und Integritätssicherung von Daten bereitstellt. Kryptografische Operationen schützen Daten sowohl im Ruhezustand als auch während der Übertragung vor Offenlegung und Manipulation.

**[TODO: Definiere erforderliche kryptografische Algorithmen]**

### 2.7 O.DATA_INTEGRITY

**Adressierte Bedrohungen:**
- T.DATA_MODIFICATION: Unbefugte Änderung von Daten
- T.DATA_CORRUPTION: Beschädigung von Daten

**Adressierte OSPs:**
- P.INTEGRITY: Datenintegrität muss gewährleistet sein

**Rationale:**
Das Ziel O.DATA_INTEGRITY bewältigt die Bedrohungen T.DATA_MODIFICATION und T.DATA_CORRUPTION, indem es sicherstellt, dass Benutzerdaten und Systemdaten vor unbefugter Änderung geschützt sind. Dies wird durch Integritätsprüfungen, Zugriffskontrolle und kryptografische Mechanismen erreicht. Das Ziel setzt die organisatorische Sicherheitsrichtlinie P.INTEGRITY um.

**[TODO: Beschreibe Integritätsschutzmechanismen]**

### 2.8 O.SECURITY_MANAGEMENT

**Adressierte OSPs:**
- P.MANAGEMENT: Sicherheitsfunktionen müssen verwaltbar sein

**Rationale:**
Das Ziel O.SECURITY_MANAGEMENT setzt die organisatorische Sicherheitsrichtlinie P.MANAGEMENT um, indem es autorisierten Administratoren die Verwaltung von Sicherheitsfunktionen und -richtlinien ermöglicht. Dies umfasst die Konfiguration von Zugriffskontrollrichtlinien, Audit-Einstellungen und anderen Sicherheitsparametern. Eine wirksame Verwaltung ist Voraussetzung für die Aufrechterhaltung der Sicherheit über den gesamten Lebenszyklus des TOE.

**[TODO: Definiere Verwaltungsfunktionen]**

### 2.9 O.SECURE_STATE

**Adressierte Bedrohungen:**
- T.MALFUNCTION: Fehlfunktion des TOE

**Rationale:**
Das Ziel O.SECURE_STATE bewältigt die Bedrohung T.MALFUNCTION, indem es sicherstellt, dass das TOE in einem sicheren Zustand startet und bei Fehlern in einen sicheren Zustand übergeht. Dies verhindert, dass Fehlfunktionen zu Sicherheitsverletzungen führen. Das TOE muss auch bei unerwarteten Ereignissen seine Sicherheitseigenschaften aufrechterhalten.

**[TODO: Beschreibe sichere Zustände]**

### 2.10 O.TSF_PROTECTION

**Adressierte Bedrohungen:**
- T.TSF_COMPROMISE: Manipulation der Sicherheitsfunktionen
- T.TSF_BYPASS: Umgehung der Sicherheitsfunktionen

**Rationale:**
Das Ziel O.TSF_PROTECTION bewältigt die Bedrohungen T.TSF_COMPROMISE und T.TSF_BYPASS, indem es sicherstellt, dass die Sicherheitsfunktionen (TSF) des TOE vor Manipulation und Umgehung geschützt sind. Dies ist fundamental für die Wirksamkeit aller anderen Sicherheitsziele, da kompromittierte Sicherheitsfunktionen alle Schutzmechanismen unwirksam machen würden.

**[TODO: Beschreibe TSF-Schutzmechanismen]**

### 2.11 Weitere TOE-Sicherheitsziele

**[TODO: Ergänze Rationale für weitere spezifische Sicherheitsziele]**

#### O.[CUSTOM_OBJECTIVE_1]

**Adressierte Bedrohungen/OSPs:**
- [TODO: Liste Bedrohungen/OSPs auf]

**Rationale:**
[TODO: Erkläre, wie das Ziel die Bedrohungen/OSPs bewältigt]

## 3. Rationale für Umgebungsziele

<!-- 
ANLEITUNG: Für jedes Umgebungsziel (OE.xxx) aus Template 0300:
- Liste die erfüllten Annahmen auf
- Erkläre, wie das Ziel die Annahmen erfüllt
- Begründe, warum das Ziel angemessen ist
-->

### 3.1 OE.PHYSICAL_PROTECTION

**Erfüllte Annahmen:**
- A.PHYSICAL_SECURITY: Das TOE wird in einer physisch gesicherten Umgebung betrieben

**Adressierte Bedrohungen:**
- T.PHYSICAL_ATTACK: Physischer Angriff auf das TOE

**Rationale:**
Das Ziel OE.PHYSICAL_PROTECTION erfüllt die Annahme A.PHYSICAL_SECURITY, indem es sicherstellt, dass die Betriebsumgebung das TOE vor physischem Zugriff durch unbefugte Personen schützt. Dies bewältigt auch die Bedrohung T.PHYSICAL_ATTACK. Physische Schutzmaßnahmen wie Zugangskontrollen, Überwachung und sichere Räumlichkeiten verhindern, dass Angreifer direkten Zugriff auf die Hardware erhalten.

**[TODO: Definiere erforderliche physische Schutzmaßnahmen]**

### 3.2 OE.TRUSTED_ADMIN

**Erfüllte Annahmen:**
- A.TRUSTED_ADMIN: Administratoren sind vertrauenswürdig und kompetent

**Rationale:**
Das Ziel OE.TRUSTED_ADMIN erfüllt die Annahme A.TRUSTED_ADMIN, indem es sicherstellt, dass Administratoren vertrauenswürdig, geschult und kompetent sind. Dies reduziert das Risiko von Insider-Bedrohungen und Fehlkonfigurationen. Vertrauenswürdige Administratoren sind essentiell, da sie weitreichende Berechtigungen haben und Sicherheitsmechanismen umgehen könnten.

**[TODO: Beschreibe Anforderungen an Administratoren]**

### 3.3 OE.USER_TRAINING

**Erfüllte Annahmen:**
- A.USER_TRAINING: Benutzer sind in der sicheren Verwendung des TOE geschult

**Rationale:**
Das Ziel OE.USER_TRAINING erfüllt die Annahme A.USER_TRAINING, indem es sicherstellt, dass Benutzer in der sicheren Verwendung des TOE geschult sind. Dies reduziert das Risiko von Benutzerfehlern, Social Engineering und unbeabsichtigten Sicherheitsverletzungen. Geschulte Benutzer verstehen Sicherheitsrichtlinien und können verdächtige Aktivitäten erkennen.

**[TODO: Definiere Schulungsanforderungen]**

### 3.4 OE.NETWORK_PROTECTION

**Erfüllte Annahmen:**
- A.NETWORK_SECURITY: Das Netzwerk ist durch Firewalls und andere Mechanismen geschützt

**Rationale:**
Das Ziel OE.NETWORK_PROTECTION erfüllt die Annahme A.NETWORK_SECURITY, indem es sicherstellt, dass die Betriebsumgebung das TOE vor Netzwerkangriffen schützt. Firewalls, Intrusion Detection Systeme und Netzwerksegmentierung reduzieren die Angriffsfläche und verhindern unbefugten Netzwerkzugriff auf das TOE.

**[TODO: Spezifiziere erforderliche Netzwerkschutzmaßnahmen]**

### 3.5 OE.EXTERNAL_SYSTEMS

**Erfüllte Annahmen:**
- A.EXTERNAL_SYSTEMS: Externe Systeme sind vertrauenswürdig und sicher

**Rationale:**
Das Ziel OE.EXTERNAL_SYSTEMS erfüllt die Annahme A.EXTERNAL_SYSTEMS, indem es sicherstellt, dass externe Systeme, mit denen das TOE interagiert, vertrauenswürdig und sicher sind. Dies reduziert Risiken durch kompromittierte Drittanbieter-Komponenten oder unsichere Schnittstellen. Die Umgebung muss die Sicherheit externer Systeme bewerten und überwachen.

**[TODO: Definiere Anforderungen an externe Systeme]**

### 3.6 OE.TIME_STAMPS

**Erfüllte Annahmen:**
- A.TIME_SOURCE: Eine zuverlässige Zeitquelle ist verfügbar

**Rationale:**
Das Ziel OE.TIME_STAMPS erfüllt die Annahme A.TIME_SOURCE, indem es sicherstellt, dass die Betriebsumgebung zuverlässige Zeitstempel für Audit-Aufzeichnungen und Sicherheitsereignisse bereitstellt. Genaue Zeitstempel sind essentiell für forensische Analysen, Korrelation von Ereignissen und Compliance-Nachweise. Das Ziel unterstützt O.AUDIT_GENERATION.

**[TODO: Beschreibe Anforderungen an Zeitquellen]**

### 3.7 Weitere Umgebungsziele

**[TODO: Ergänze Rationale für weitere Umgebungsziele]**

#### OE.[CUSTOM_ENV_OBJECTIVE]

**Erfüllte Annahmen:**
- [TODO: Liste Annahmen auf]

**Rationale:**
[TODO: Erkläre, wie das Ziel die Annahmen erfüllt]

## 4. Vollständigkeitsnachweis

<!-- 
ANLEITUNG: Demonstriere, dass alle Bedrohungen, OSPs und Annahmen durch Sicherheitsziele abgedeckt sind.
Dies ist ein kritischer Nachweis für die Common Criteria Evaluation.
-->

### 4.1 Abdeckung der Bedrohungen

Die folgende Tabelle zeigt, dass jede identifizierte Bedrohung durch mindestens ein Sicherheitsziel adressiert wird:

| Bedrohung | Adressierende Ziele | Status |
|-----------|---------------------|--------|
| T.UNAUTHORIZED_ACCESS | O.ACCESS_CONTROL | ✓ Abgedeckt |
| T.PRIVILEGE_ESCALATION | O.ACCESS_CONTROL | ✓ Abgedeckt |
| T.MASQUERADE | O.IDENTIFICATION_AUTHENTICATION | ✓ Abgedeckt |
| T.AUDIT_COMPROMISE | O.AUDIT_GENERATION, O.AUDIT_PROTECTION | ✓ Abgedeckt |
| T.DATA_DISCLOSURE | O.DATA_CONFIDENTIALITY, O.CRYPTOGRAPHIC_OPERATIONS | ✓ Abgedeckt |
| T.EAVESDROPPING | O.DATA_CONFIDENTIALITY, O.CRYPTOGRAPHIC_OPERATIONS | ✓ Abgedeckt |
| T.DATA_MODIFICATION | O.DATA_INTEGRITY, O.CRYPTOGRAPHIC_OPERATIONS | ✓ Abgedeckt |
| T.DATA_CORRUPTION | O.DATA_INTEGRITY | ✓ Abgedeckt |
| T.MALFUNCTION | O.SECURE_STATE | ✓ Abgedeckt |
| T.TSF_COMPROMISE | O.TSF_PROTECTION | ✓ Abgedeckt |
| T.TSF_BYPASS | O.TSF_PROTECTION | ✓ Abgedeckt |
| T.PHYSICAL_ATTACK | OE.PHYSICAL_PROTECTION | ✓ Abgedeckt |
| **[TODO: Weitere Bedrohungen]** | | |

**Ergebnis:** Alle Bedrohungen sind durch Sicherheitsziele abgedeckt. ✓

### 4.2 Abdeckung der organisatorischen Sicherheitsrichtlinien

Die folgende Tabelle zeigt, dass jede OSP durch mindestens ein Sicherheitsziel umgesetzt wird:

| OSP | Umsetzende Ziele | Status |
|-----|------------------|--------|
| P.ACCESS_CONTROL | O.ACCESS_CONTROL | ✓ Abgedeckt |
| P.ACCOUNTABILITY | O.AUDIT_GENERATION, O.AUDIT_PROTECTION | ✓ Abgedeckt |
| P.CONFIDENTIALITY | O.DATA_CONFIDENTIALITY | ✓ Abgedeckt |
| P.INTEGRITY | O.DATA_INTEGRITY | ✓ Abgedeckt |
| P.MANAGEMENT | O.SECURITY_MANAGEMENT | ✓ Abgedeckt |
| **[TODO: Weitere OSPs]** | | |

**Ergebnis:** Alle OSPs sind durch Sicherheitsziele umgesetzt. ✓

### 4.3 Abdeckung der Annahmen

Die folgende Tabelle zeigt, dass jede Annahme durch mindestens ein Umgebungsziel erfüllt wird:

| Annahme | Erfüllende Ziele | Status |
|---------|------------------|--------|
| A.PHYSICAL_SECURITY | OE.PHYSICAL_PROTECTION | ✓ Abgedeckt |
| A.TRUSTED_ADMIN | OE.TRUSTED_ADMIN | ✓ Abgedeckt |
| A.USER_TRAINING | OE.USER_TRAINING | ✓ Abgedeckt |
| A.NETWORK_SECURITY | OE.NETWORK_PROTECTION | ✓ Abgedeckt |
| A.EXTERNAL_SYSTEMS | OE.EXTERNAL_SYSTEMS | ✓ Abgedeckt |
| A.TIME_SOURCE | OE.TIME_STAMPS | ✓ Abgedeckt |
| **[TODO: Weitere Annahmen]** | | |

**Ergebnis:** Alle Annahmen sind durch Umgebungsziele erfüllt. ✓

### 4.4 Rückverfolgbarkeit der Sicherheitsziele

Die folgende Tabelle zeigt, dass jedes Sicherheitsziel auf mindestens eine Bedrohung, OSP oder Annahme zurückgeführt werden kann:

| Sicherheitsziel | Bedrohungen | OSPs | Annahmen | Status |
|-----------------|-------------|------|----------|--------|
| O.ACCESS_CONTROL | T.UNAUTHORIZED_ACCESS, T.PRIVILEGE_ESCALATION | P.ACCESS_CONTROL | - | ✓ Gerechtfertigt |
| O.IDENTIFICATION_AUTHENTICATION | T.MASQUERADE | - | - | ✓ Gerechtfertigt |
| O.AUDIT_GENERATION | T.AUDIT_COMPROMISE | P.ACCOUNTABILITY | - | ✓ Gerechtfertigt |
| O.AUDIT_PROTECTION | T.AUDIT_COMPROMISE | - | - | ✓ Gerechtfertigt |
| O.DATA_CONFIDENTIALITY | T.DATA_DISCLOSURE, T.EAVESDROPPING | P.CONFIDENTIALITY | - | ✓ Gerechtfertigt |
| O.CRYPTOGRAPHIC_OPERATIONS | T.DATA_DISCLOSURE, T.DATA_MODIFICATION | - | - | ✓ Gerechtfertigt |
| O.DATA_INTEGRITY | T.DATA_MODIFICATION, T.DATA_CORRUPTION | P.INTEGRITY | - | ✓ Gerechtfertigt |
| O.SECURITY_MANAGEMENT | - | P.MANAGEMENT | - | ✓ Gerechtfertigt |
| O.SECURE_STATE | T.MALFUNCTION | - | - | ✓ Gerechtfertigt |
| O.TSF_PROTECTION | T.TSF_COMPROMISE, T.TSF_BYPASS | - | - | ✓ Gerechtfertigt |
| OE.PHYSICAL_PROTECTION | T.PHYSICAL_ATTACK | - | A.PHYSICAL_SECURITY | ✓ Gerechtfertigt |
| OE.TRUSTED_ADMIN | - | - | A.TRUSTED_ADMIN | ✓ Gerechtfertigt |
| OE.USER_TRAINING | - | - | A.USER_TRAINING | ✓ Gerechtfertigt |
| OE.NETWORK_PROTECTION | - | - | A.NETWORK_SECURITY | ✓ Gerechtfertigt |
| OE.EXTERNAL_SYSTEMS | - | - | A.EXTERNAL_SYSTEMS | ✓ Gerechtfertigt |
| OE.TIME_STAMPS | - | - | A.TIME_SOURCE | ✓ Gerechtfertigt |
| **[TODO: Weitere Ziele]** | | | | |

**Ergebnis:** Alle Sicherheitsziele sind gerechtfertigt. ✓

## 5. Zusammenfassung

Die Rationale demonstriert, dass die definierten Sicherheitsziele:

1. **Vollständig** sind: Alle Bedrohungen, OSPs und Annahmen sind abgedeckt
2. **Angemessen** sind: Jedes Ziel ist geeignet, die zugeordneten Sicherheitsprobleme zu bewältigen
3. **Rückverfolgbar** sind: Jedes Ziel kann auf Sicherheitsprobleme zurückgeführt werden
4. **Konsistent** sind: Keine Widersprüche zwischen Zielen

Die Sicherheitsziele bilden eine solide Grundlage für die Ableitung der Sicherheitsanforderungen (SFRs und SARs) im nächsten Schritt des Security Target.

## 6. Nächste Schritte

Nach der Rationale für Sicherheitsziele:
1. Erstelle die Coverage Matrix (siehe Template 0320)
2. Leite die Sicherheitsanforderungen (SFRs und SARs) aus den Zielen ab (siehe Template 0400-0450)

## 7. Referenzen

- ISO/IEC 15408-1: Security Target Evaluation
- Template 0200-0240: Sicherheitsproblem-Definition
- Template 0300: Sicherheitsziele
- Template 0320: Security Objectives Coverage Matrix
- Template 0400-0450: Sicherheitsanforderungen

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |

