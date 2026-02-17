# Audit-Ereignisse

**Dokument-ID:** NIST-0230
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

**AU-2 Audit-Ereignisse**

Die Organisation bestimmt, dass das Informationssystem in der Lage ist, bestimmte Ereignisse zu auditieren, und koordiniert die Sicherheitsauditfunktion mit anderen Organisationseinheiten.

## 2. Kontrollimplementierung

### 2.1 Auditierbare Ereignisse

**Ereigniskategorien:**
- Kontoverwaltungsereignisse
- Authentifizierungs- und Autorisierungsereignisse
- Privilegienerweiterungsereignisse
- System- und Anwendungszugriffsereignisse
- Konfigurationsänderungen
- Sicherheitsrichtlinienänderungen
- Datenzugriff und -änderung
- Netzwerkaktivität
- Systemstart und -herunterfahren

[TODO: Spezifizieren Sie auditierbare Ereignisse für Ihre Organisation]

### 2.2 Ereignisauswahlkriterien

**Auswahlbegründung:**
| Ereignistyp | Begründung | Häufigkeit |
|-------------|------------|------------|
| Fehlgeschlagene Anmeldeversuche | Erkennung unbefugter Zugriffsversuche | Echtzeit |
| Privilegienänderungen | Überwachung der Privilegienerweiterung | Echtzeit |
| Konfigurationsänderungen | Verfolgung von Systemänderungen | Echtzeit |
| Datenzugriff | Überwachung des Zugriffs auf sensible Daten | Echtzeit |
| [TODO] | [TODO] | [TODO] |

### 2.3 Audit-Koordination

**Koordinationsaktivitäten:**
- Überprüfung der Auditanforderungen mit Stakeholdern
- Koordination mit dem Incident-Response-Team
- Abstimmung mit Compliance-Anforderungen
- Integration mit SIEM-Systemen

[TODO: Beschreiben Sie Koordinationsverfahren]

### 2.4 Audit-Überprüfung und -Aktualisierungen

**Überprüfungsplan:** [TODO: z.B. Vierteljährlich]  
**Aktualisierungsauslöser:**
- Neue identifizierte Bedrohungen
- Änderungen der Compliance-Anforderungen
- Erkenntnisse aus Vorfällen
- Technologieänderungen

[TODO: Definieren Sie Überprüfungs- und Aktualisierungsverfahren]

## 3. Kontrollerweiterungen

- **AU-2(1):** Zusammenstellung von Audit-Aufzeichnungen aus mehreren Quellen
- **AU-2(2):** Auswahl von Audit-Ereignissen nach Komponente
- **AU-2(3):** Überprüfungen und Aktualisierungen
- **AU-2(4):** Privilegierte Funktionen

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

