# Geltungsbereich und Systemgrenzen

**Dokument-ID:** NIST-0020  
**Organisation:** {{ meta.organization.name }}  
**Owner:** {{ meta.document.owner }}  
**Genehmigt durch:** {{ meta.document.approver }}  
**Version:** {{ meta.document.version }}  
**Status:** Entwurf / In Review / Freigegeben  
**Klassifizierung:** {{ meta.document.classification }}  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  

---

## 1. Zweck

Dieses Dokument definiert den Geltungsbereich und die Autorisierungsgrenzen des Informationssystems {{ meta.nist.system_name }}.

### 1.1 Ziele

- **Scope-Definition:** Klare Abgrenzung des Systems
- **Autorisierungsgrenze:** Definition der Autorisierungsgrenze
- **Komponenten-Identifikation:** Identifikation aller Systemkomponenten
- **Schnittstellen:** Dokumentation externer Schnittstellen

### 1.2 Referenzen

- **NIST SP 800-37 Rev. 2:** Risk Management Framework for Information Systems and Organizations
- **NIST SP 800-53 Rev. 5:** Security and Privacy Controls
- **NIST SP 800-18 Rev. 1:** Guide for Developing Security Plans

## 2. Systemidentifikation

### 2.1 Systeminformationen

**Systemname:** {{ meta.nist.system_name }}  
**System-ID:** {{ meta.nist.system_id }}  
**FIPS 199 Kategorisierung:** [TODO: Low / Moderate / High]  
**System Owner:** [TODO: Name]  
**Authorizing Official (AO):** {{ meta.roles.ao.name }}  

### 2.2 Systembeschreibung

**Zweck:** [TODO: Beschreibung des Systemzwecks]

**Hauptfunktionen:**
- [TODO: Funktion 1]
- [TODO: Funktion 2]
- [TODO: Funktion 3]

**Geschäftsprozesse:**
- [TODO: Prozess 1]
- [TODO: Prozess 2]

## 3. Autorisierungsgrenze

### 3.1 Definition der Autorisierungsgrenze

Die Autorisierungsgrenze umfasst alle Komponenten, die unter einer einzigen Autorisierungsentscheidung fallen.

**Autorisierungsgrenze:** [TODO: Beschreibung der Grenze]

**Eingeschlossene Komponenten:**
- [TODO: Komponente 1]
- [TODO: Komponente 2]
- [TODO: Komponente 3]

**Ausgeschlossene Komponenten:**
- [TODO: Komponente 1 - Begründung]
- [TODO: Komponente 2 - Begründung]

### 3.2 Netzwerkdiagramm

[TODO: Fügen Sie Netzwerkdiagramm ein, das die Autorisierungsgrenze zeigt]

## 4. Systemkomponenten

### 4.1 Hardware-Komponenten

| Komponente | Typ | Standort | Funktion | Kritikalität |
|------------|-----|----------|----------|--------------|
| [TODO: Server 1] | Server | [TODO: RZ1] | [TODO: Funktion] | [TODO: H/M/L] |
| [TODO: Firewall 1] | Netzwerk | [TODO: RZ1] | [TODO: Funktion] | [TODO: H/M/L] |

### 4.2 Software-Komponenten

| Komponente | Version | Hersteller | Funktion | Lizenz |
|------------|---------|------------|----------|--------|
| [TODO: OS] | [TODO: Version] | [TODO: Vendor] | Betriebssystem | [TODO: Lizenz] |
| [TODO: App] | [TODO: Version] | [TODO: Vendor] | Anwendung | [TODO: Lizenz] |

### 4.3 Datenkomponenten

| Datentyp | Klassifizierung | Speicherort | Retention | Backup |
|----------|-----------------|-------------|-----------|--------|
| [TODO: Daten 1] | [TODO: Klassifizierung] | [TODO: Ort] | [TODO: Zeit] | [TODO: Ja/Nein] |

## 5. Externe Schnittstellen

### 5.1 Systemverbindungen

| Verbundenes System | Verbindungstyp | Protokoll | Zweck | Autorisierung |
|-------------------|----------------|-----------|-------|---------------|
| [TODO: System 1] | [TODO: Typ] | [TODO: Protokoll] | [TODO: Zweck] | [TODO: ATO-Nummer] |

### 5.2 Datenflüsse

**Eingehende Datenflüsse:**
- [TODO: Quelle → Ziel: Beschreibung]

**Ausgehende Datenflüsse:**
- [TODO: Quelle → Ziel: Beschreibung]

## 6. Standorte

### 6.1 Physische Standorte

| Standort-ID | Standortname | Adresse | Komponenten | Sicherheitslevel |
|-------------|--------------|---------|-------------|------------------|
| [TODO: LOC-01] | [TODO: Name] | [TODO: Adresse] | [TODO: Liste] | [TODO: Level] |

## 7. Personal

### 7.1 Benutzerrollen

| Rolle | Anzahl | Zugriffslevel | Begründung |
|-------|--------|---------------|------------|
| [TODO: Admin] | [TODO: Anzahl] | Privilegiert | Administration |
| [TODO: User] | [TODO: Anzahl] | Standard | Normale Nutzung |

### 7.2 Externe Benutzer

| Benutzergruppe | Organisation | Zugriffsmethode | Zweck |
|----------------|--------------|-----------------|-------|
| [TODO: Partner] | [TODO: Org] | [TODO: VPN] | [TODO: Zweck] |

## 8. Genehmigung

**Genehmigt durch:** {{ meta.roles.ao.name }}  
**Datum:** [TODO: Datum]  

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |

<!-- End of template -->
