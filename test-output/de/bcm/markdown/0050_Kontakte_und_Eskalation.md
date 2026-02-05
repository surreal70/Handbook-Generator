# Kontakte und Eskalation

**Dokument-ID:** BCM-0050  
**Organisation:** AdminSend GmbH  
**Owner:** IT Operations Manager  
**Genehmigt durch:** CIO  
**Version:** 1.0.0  
**Status:** Entwurf / In Review / Freigegeben  
**Klassifizierung:** Vertraulich  
**Letzte Aktualisierung:** {{ meta.document.last_updated }}  

---



## 1. Kontaktliste (intern)

> **Achtung:** Kontaktlisten enthalten personenbezogene Daten und unterliegen besonderen Datenschutzanforderungen (DSGVO). Zugriff nur für autorisierte Personen. Quartalsweise Aktualisierung erforderlich.

### 1.1 Krisenstab

| Funktion | Name | Telefon | Mobil | E-Mail | Stellvertretung |
|----------|------|---------|-------|--------|-----------------|
| **Krisenstabsleitung** | {{ meta.roles.ceo.name }} | {{ meta.roles.ceo.phone }} | [TODO: Mobil] | {{ meta.roles.ceo.email }} | {{ meta.roles.coo.name }} |
| **CIO** | {{ meta.roles.cio.name }} | {{ meta.roles.cio.phone }} | [TODO: Mobil] | {{ meta.roles.cio.email }} | [TODO] |
| **CISO** | {{ meta.roles.ciso.name }} | {{ meta.roles.ciso.phone }} | [TODO: Mobil] | {{ meta.roles.ciso.email }} | [TODO] |
| **CFO** | {{ meta.roles.cfo.name }} | {{ meta.roles.cfo.phone }} | [TODO: Mobil] | {{ meta.roles.cfo.email }} | [TODO] |
| **COO** | {{ meta.roles.coo.name }} | {{ meta.roles.coo.phone }} | [TODO: Mobil] | {{ meta.roles.coo.email }} | [TODO] |

### 1.2 BCM-Organisation

| Funktion | Name | Telefon | Mobil | E-Mail | Stellvertretung |
|----------|------|---------|-------|--------|-----------------|
| **BCM-Manager** | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| **Incident Commander** | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| **IT-DR-Lead** | {{ meta.roles.it_operations_manager.name }} | {{ meta.roles.it_operations_manager.phone }} | [TODO] | {{ meta.roles.it_operations_manager.email }} | [TODO] |
| **Kommunikation** | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

### 1.3 IT-Operations und Service Desk

| Funktion | Name | Telefon | Mobil | E-Mail | Verfügbarkeit |
|----------|------|---------|-------|--------|---------------|
| **Service Desk** | {{ meta.roles.service_desk_lead.name }} | [TODO] | [TODO] | {{ meta.roles.service_desk_lead.email }} | 24/7 |
| **IT-Operations Manager** | {{ meta.roles.it_operations_manager.name }} | {{ meta.roles.it_operations_manager.phone }} | [TODO] | {{ meta.roles.it_operations_manager.email }} | 24/7 Rufbereitschaft |
| **Netzwerk-Team** | [TODO] | [TODO] | [TODO] | [TODO] | 24/7 Rufbereitschaft |
| **Server-Team** | [TODO] | [TODO] | [TODO] | [TODO] | 24/7 Rufbereitschaft |
| **Security-Team** | [TODO] | [TODO] | [TODO] | [TODO] | 24/7 Rufbereitschaft |

### 1.4 Fachbereiche

| Fachbereich | Ansprechpartner | Telefon | Mobil | E-Mail | Stellvertretung |
|-------------|-----------------|---------|-------|--------|-----------------|
| **Produktion** | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| **Vertrieb** | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| **Finanzen** | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| **HR** | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |
| **Einkauf** | [TODO] | [TODO] | [TODO] | [TODO] | [TODO] |

## 2. Externe Kontakte

### 2.1 IT-Dienstleister und Provider

| Organisation | Rolle/Service | Kontakt | Telefon | E-Mail | Vertrags-/Kundennr. | Verfügbarkeit |
|--------------|---------------|---------|---------|--------|---------------------|---------------|
| [TODO: Cloud-Provider] | Cloud-Infrastruktur | [TODO] | [TODO] | [TODO] | [TODO] | 24/7 |
| [TODO: ISP] | Internet-Anbindung | [TODO] | [TODO] | [TODO] | [TODO] | 24/7 |
| [TODO: Telco] | Telefonie | [TODO] | [TODO] | [TODO] | [TODO] | 24/7 |
| [TODO: Backup-Provider] | Backup-Services | [TODO] | [TODO] | [TODO] | [TODO] | 24/7 |
| [TODO: Security-Provider] | Security-Services | [TODO] | [TODO] | [TODO] | [TODO] | 24/7 |

### 2.2 Notfalldienste und Behörden

| Organisation | Zweck | Telefon | Notrufnummer | Adresse |
|--------------|-------|---------|--------------|---------|
| **Feuerwehr** | Brand, Gefahrstoffe | [TODO: Lokal] | **112** | [TODO] |
| **Polizei** | Sicherheit, Straftaten | [TODO: Lokal] | **110** | [TODO] |
| **Rettungsdienst** | Medizinische Notfälle | [TODO: Lokal] | **112** | [TODO] |
| **Giftnotruf** | Gefahrstoffunfälle | [TODO: Regional] | [TODO] | [TODO] |
| **BSI** | Cyber-Vorfälle | +49 228 99 9582-222 | - | Godesberger Allee 185-189, 53175 Bonn |

### 2.3 Kritische Lieferanten

| Lieferant | Produkt/Service | Ansprechpartner | Telefon | E-Mail | Kritikalität |
|-----------|-----------------|-----------------|---------|--------|--------------|
| [TODO] | [TODO] | [TODO] | [TODO] | [TODO] | Hoch / Mittel / Niedrig |

### 2.4 Kunden und Partner (bei Bedarf)

| Organisation | Ansprechpartner | Telefon | E-Mail | Benachrichtigung bei |
|--------------|-----------------|---------|--------|----------------------|
| [TODO: Großkunde] | [TODO] | [TODO] | [TODO] | Serviceausfall > 4h |

## 3. Eskalationsmatrix

### 3.1 Eskalationsstufen

| Stufe | Bezeichnung | Auslöser | Verantwortlich | Reaktionszeit | Kommunikationspflicht |
|-------|-------------|----------|----------------|---------------|----------------------|
| **1** | Störung | Einzelne Systeme betroffen, keine Auswirkung auf kritische Services | IT-Operations | 4 Stunden | Service Desk informieren |
| **2** | Major Incident | Kritischer Service beeinträchtigt, RTO gefährdet | Incident Commander | 1 Stunde | Management informieren |
| **3** | BCM-Aktivierung | Mehrere kritische Services ausgefallen, Geschäftsbetrieb gefährdet | Krisenstab | 30 Minuten | Krisenstab aktivieren, externe Stakeholder informieren |
| **4** | Katastrophe | Standort nicht verfügbar, massive Auswirkungen | Krisenstabsleitung | Sofort | Alle Stakeholder, Behörden, Medien |

### 3.2 Eskalationskriterien

**Eskalation auf Stufe 2 (Major Incident):**
- RTO eines kritischen Services wird voraussichtlich überschritten
- Mehr als [TODO: X] Benutzer betroffen
- Finanzieller Schaden > [TODO: Betrag] pro Stunde
- Datenverlust droht (RPO-Überschreitung)
- Sicherheitsvorfall mit hohem Impact

**Eskalation auf Stufe 3 (BCM-Aktivierung):**
- Mehrere kritische Services gleichzeitig ausgefallen
- Wiederherstellung innerhalb RTO nicht möglich
- Standort nicht zugänglich
- Massive Cyber-Attacke (Ransomware, DDoS)
- Naturkatastrophe oder schwerer Unfall

**Eskalation auf Stufe 4 (Katastrophe):**
- Hauptstandort komplett ausgefallen
- Menschenleben in Gefahr
- Existenzbedrohende Situation für das Unternehmen
- Behördliche Anordnung (z.B. Evakuierung)

### 3.3 Eskalationsprozess

```
┌─────────────────┐
│  Störung erkannt│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Erstbewertung   │
│ (IT-Operations) │
└────────┬────────┘
         │
    ┌────┴────┐
    │ Stufe 1?│
    └────┬────┘
         │ Nein
         ▼
┌─────────────────┐      ┌──────────────────┐
│ Major Incident? │─Ja──>│ Incident         │
│ (Stufe 2)       │      │ Commander        │
└────────┬────────┘      │ alarmieren       │
         │ Nein          └──────────────────┘
         ▼
┌─────────────────┐      ┌──────────────────┐
│ BCM-Aktivierung?│─Ja──>│ Krisenstab       │
│ (Stufe 3)       │      │ aktivieren       │
└────────┬────────┘      └──────────────────┘
         │ Nein
         ▼
┌─────────────────┐      ┌──────────────────┐
│ Katastrophe?    │─Ja──>│ Krisenstabsleitung│
│ (Stufe 4)       │      │ sofort informieren│
└─────────────────┘      └──────────────────┘
```

## 4. Alarmierungsprozess

### 4.1 Alarmierungskanäle

**Primär:** Telefon (Mobiltelefon)
- Direktanruf an definierte Kontaktpersonen
- Bei Nichterreichbarkeit: Stellvertreter kontaktieren

**Sekundär:** SMS / Messenger
- Parallele Benachrichtigung via SMS
- Messenger-Gruppen für schnelle Koordination

**Tertiär:** E-Mail
- Dokumentation und Nachvollziehbarkeit
- Nicht für zeitkritische Alarmierung geeignet

### 4.2 Alarmierungsablauf

1. **Ersterkennung:** Störung wird erkannt (Monitoring, Meldung, Beobachtung)
2. **Erstbewertung:** IT-Operations bewertet Schweregrad und Auswirkungen
3. **Alarmierung:** Kontaktaufnahme gemäß Eskalationsstufe
4. **Bestätigung:** Empfänger bestätigt Empfang und Verfügbarkeit
5. **Briefing:** Kurze Lagebeschreibung und erste Maßnahmen
6. **Dokumentation:** Alarmierung wird im Logbuch dokumentiert

### 4.3 Alarmierungsliste Krisenstab

Bei BCM-Aktivierung (Stufe 3) werden folgende Personen alarmiert:

1. {{ meta.roles.ceo.name }} (Krisenstabsleitung)
2. {{ meta.roles.cio.name }} (CIO)
3. {{ meta.roles.ciso.name }} (CISO)
4. [TODO: BCM-Manager]
5. [TODO: Kommunikationsverantwortlicher]
6. Weitere Krisenstabsmitglieder je nach Situation

**Alarmierungsreihenfolge:** Parallel, nicht sequenziell

## 5. Rufbereitschaft und On-Call

### 5.1 Rufbereitschaftsplan

[TODO: Definieren Sie Rufbereitschaftspläne für kritische Rollen]

**Beispiel IT-Operations:**

| KW | Primär | Sekundär | Tertiär |
|----|--------|----------|---------|
| 01 | [Name 1] | [Name 2] | [Name 3] |
| 02 | [Name 2] | [Name 3] | [Name 1] |
| 03 | [Name 3] | [Name 1] | [Name 2] |

**Aktualisierung:** Wöchentlich, spätestens Freitag 12:00 Uhr

### 5.2 On-Call-Verpflichtungen

**Während der Rufbereitschaft:**
- Mobiltelefon eingeschaltet und erreichbar (24/7)
- Reaktionszeit: Innerhalb von 30 Minuten
- Nüchtern und einsatzfähig
- Zugriff auf Laptop und VPN
- Kenntnis der aktuellen Runbooks und Eskalationswege

**Vergütung:** Gemäß Betriebsvereinbarung / Arbeitsvertrag

## 6. Kontaktlistenpflege

### 6.1 Aktualisierungsprozess

**Verantwortlich:** BCM-Manager

**Aktualisierungsintervall:**
- Quartalsweise Überprüfung aller Kontaktdaten
- Ad-hoc bei personellen Änderungen
- Nach jeder BCM-Übung

**Prozess:**
1. BCM-Manager fordert Aktualisierung an
2. Fachbereiche prüfen und melden Änderungen
3. BCM-Manager aktualisiert Kontaktlisten
4. Neue Version wird verteilt und alte Version archiviert

### 6.2 Datenschutz

Kontaktlisten unterliegen der DSGVO:
- Zugriff nur für autorisierte Personen
- Verschlüsselte Speicherung
- Keine Weitergabe an Dritte ohne Einwilligung
- Löschung bei Ausscheiden von Mitarbeitern

---

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |


