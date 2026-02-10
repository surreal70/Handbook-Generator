# Geringste Privilegien

**Dokument-ID:** NIST-0150  
**Kontrollfamilie:** Zugriffskontrolle (AC)  
**Kontrolle:** AC-6  
**Organisation:** {{ meta.organization.name }}  
**Verantwortlich:** {{ meta.document.owner }}  
**Version:** {{ meta.document.version }}  
**Status:** Entwurf / In Prüfung / Genehmigt  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  

---

## 1. Kontrollbeschreibung

**AC-6 Geringste Privilegien**

Die Organisation wendet das Prinzip der geringsten Privilegien an und erlaubt nur autorisierte Zugriffe für Benutzer (oder Prozesse, die im Namen von Benutzern handeln), die für die Erfüllung zugewiesener Aufgaben notwendig sind.

## 2. Kontrollimplementierung

### 2.1 Prinzip der geringsten Privilegien

**Implementierungsansatz:**
- Standardbenutzerkonten ohne administrative Rechte
- Privilegierte Zugriffe nur bei Bedarf
- Zeitlich begrenzte Privilegienerweiterungen
- Regelmäßige Überprüfung von Berechtigungen

[TODO: Beschreiben Sie die Implementierung]

### 2.2 Privilegierte Funktionen

**Privilegierte Rollen:**
| Rolle | Privilegien | Begründung | Genehmigung |
|-------|-------------|------------|-------------|
| [TODO] | [TODO] | [TODO] | [TODO] |

### 2.3 Zugriffskontrollmechanismen

**Mechanismen:**
- Rollenbasierte Zugriffskontrolle (RBAC)
- Just-in-Time (JIT) Zugriff
- Privileged Access Management (PAM)
- Regelmäßige Zugriffszertifizierung

[TODO: Spezifizieren Sie verwendete Mechanismen]

### 2.4 Überwachung privilegierter Zugriffe

**Überwachungsmaßnahmen:**
[TODO: Beschreiben Sie Überwachungsverfahren]

## 3. Kontrollerweiterungen

- **AC-6(1):** Autorisierung von Zugriff auf Sicherheitsfunktionen
- **AC-6(2):** Nicht-privilegierter Zugriff für nicht sicherheitsrelevante Funktionen
- **AC-6(3):** Netzwerkzugriff auf privilegierte Befehle
- **AC-6(5):** Privilegierte Konten
- **AC-6(7):** Überprüfung von Benutzerrechten
- **AC-6(9):** Protokollierung der Verwendung privilegierter Funktionen
- **AC-6(10):** Verbot nicht-privilegierter Benutzer, Sicherheitsfunktionen auszuführen

[TODO: Markieren Sie zutreffende Erweiterungen]

## 4. Implementierungsstatus

**Status:** [TODO: Implementiert / Teilweise implementiert / Geplant / Nicht zutreffend]  
**Implementierungsdatum:** [TODO: Datum]  
**Verantwortlich:** [TODO: Name/Rolle]  

## 5. Bewertung

**Bewertungsmethode:** Prüfen, Befragen, Testen  
**Bewertungsstatus:** [TODO: Erfüllt / Nicht erfüllt / Nicht zutreffend]  
**Feststellungen:** [TODO: Beschreibung]  

---

**Dokumentenhistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Ersterstellung |

<!-- Ende des Templates -->
