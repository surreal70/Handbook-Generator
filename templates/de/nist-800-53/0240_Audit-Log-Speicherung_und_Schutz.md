# Audit-Log-Speicherung und Schutz

**Dokument-ID:** NIST-0240
**Organisation:** {{ meta-organisation.name }}
**Owner:** {{ meta-handbook.owner }}
**Genehmigt durch:** {{ meta-handbook.approver }}
**Revision:** {{ meta-handbook.revision }}
**Author:** {{ meta-handbook.author }}
**Status:** {{ meta-handbook.status }}
**Klassifizierung:** {{ meta-handbook.classification }}
**Letzte Aktualisierung:** {{ meta-handbook.modifydate }}

---

---

## 1. Kontrollbeschreibung

**AU-4 Audit-Log-Speicherkapazität**

Die Organisation weist Audit-Log-Speicherkapazität gemäß den Anforderungen zur Aufbewahrung von Audit-Aufzeichnungen zu.

**AU-9 Schutz von Audit-Informationen**

Das Informationssystem schützt Audit-Informationen und Audit-Tools vor unbefugtem Zugriff, Änderung und Löschung.

## 2. Kontrollimplementierung

### 2.1 Speicherkapazitätsplanung

**Kapazitätsanforderungen:**
| System | Tägliches Volumen | Aufbewahrungsdauer | Erforderliche Kapazität |
|--------|-------------------|--------------------|-----------------------|
| [TODO] | [TODO] | [TODO] | [TODO] |

**Überwachung:**
- Automatische Kapazitätsüberwachung
- Warnungen bei Schwellenwertüberschreitung
- Automatische Archivierung

[TODO: Beschreiben Sie Kapazitätsplanung und -überwachung]

### 2.2 Schutzmaßnahmen

**Zugriffskontrollen:**
- Eingeschränkter Zugriff auf Audit-Logs
- Rollenbasierte Berechtigungen
- Privileged Access Management

**Integritätsschutz:**
- Digitale Signaturen
- Schreibgeschützte Speicherung
- Kryptografische Hashes

**Verfügbarkeitsschutz:**
- Redundante Speicherung
- Regelmäßige Backups
- Disaster Recovery

[TODO: Spezifizieren Sie Schutzmaßnahmen]

### 2.3 Audit-Tool-Schutz

**Geschützte Tools:**
[TODO: Liste der geschützten Audit-Tools]

**Schutzmaßnahmen:**
[TODO: Beschreiben Sie Schutzmaßnahmen für Tools]

## 3. Kontrollerweiterungen

**AU-4:**
- **AU-4(1):** Übertragung auf alternatives System

**AU-9:**
- **AU-9(1):** Hardware-Schreibschutz
- **AU-9(2):** Sicherung von Audit-Informationen
- **AU-9(3):** Kryptografischer Schutz
- **AU-9(4):** Zugriff durch Teilmenge privilegierter Benutzer
- **AU-9(5):** Dual-Autorisierung
- **AU-9(6):** Schreibzugriff auf Audit-Informationen

[TODO: Markieren Sie zutreffende Erweiterungen]

## 4. Implementierungsstatus

**Status:** [TODO: Implementiert / Teilweise implementiert / Geplant / Nicht zutreffend]  
**Implementierungsdatum:** [TODO: Datum]  
**Verantwortlich:** [TODO: Name/Rolle]  

## 5. Bewertung

**Bewertungsmethode:** Prüfen, Befragen, Testen  
**Bewertungsstatus:** [TODO: Erfüllt / Nicht erfüllt / Nicht zutreffend]  
**Feststellungen:** [TODO: Beschreibung]  

**Dokumentenhistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta-handbook.modifydate }} | {{ meta-handbook.author }} | Ersterstellung |

<!-- Ende des Templates -->

