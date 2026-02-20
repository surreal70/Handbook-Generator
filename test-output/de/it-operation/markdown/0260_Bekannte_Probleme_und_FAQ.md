# Bekannte Probleme und FAQ

**Dokument-ID:** IT-OPERATION-0260
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

## Übersicht

Dieses Dokument enthält bekannte Probleme und Workarounds, häufig gestellte Fragen (FAQ) sowie Troubleshooting-Tipps für den IT-Service. Ziel ist es, schnelle Lösungen für wiederkehrende Probleme bereitzustellen und die Effizienz des Supports zu erhöhen.

**Dokumentverantwortlicher:** [TODO]  
**Genehmigt durch:** [TODO]  
**Version:** 0  
**Organisation:** AdminSend GmbH

## Bekannte Probleme

### Problem-Tracking

Alle bekannten Probleme werden im Ticketing-System mit dem Label "Known Issue" erfasst und hier dokumentiert.

**Verantwortlich:** {{ meta-organisation-roles.role_IT_Operations_Manager }}  
**Review-Zyklus:** Monatlich

### KI-001: [TODO: Problem-Titel]

**Status:** Offen / In Bearbeitung / Gelöst  
**Priorität:** P1 (Kritisch) / P2 (Hoch) / P3 (Mittel) / P4 (Niedrig)  
**Erstellt:** [TODO: Datum]  
**Letzte Aktualisierung:** [TODO: Datum]  
**Ticket-ID:** [TODO: Ticket-Nummer]

#### Beschreibung
[TODO: Detaillierte Beschreibung des Problems]

#### Betroffene Systeme
- [TODO: System 1]
- [TODO: System 2]

#### Symptome
- [TODO: Symptom 1]
- [TODO: Symptom 2]

#### Root Cause
[TODO: Ursache des Problems, falls bekannt]

#### Workaround
```
[TODO: Schritt-für-Schritt-Workaround]
1. Schritt 1
2. Schritt 2
3. Schritt 3
```

#### Permanente Lösung
- **Status:** Geplant / In Entwicklung / Getestet / Deployed
- **ETA:** [TODO: Voraussichtliches Datum]
- **Verantwortlich:** [TODO: Name]

#### Betroffene Benutzer
[TODO: Anzahl oder Beschreibung der betroffenen Benutzer]

#### Kommunikation
- [TODO: Datum] - Benutzer informiert
- [TODO: Datum] - Update kommuniziert
- [TODO: Datum] - Lösung kommuniziert

### KI-002: Intermittierende Netzwerk-Timeouts

**Status:** In Bearbeitung  
**Priorität:** P2 (Hoch)  
**Erstellt:** 2025-01-15  
**Letzte Aktualisierung:** 2025-01-28  
**Ticket-ID:** INC-12345

#### Beschreibung
Benutzer erleben sporadische Netzwerk-Timeouts beim Zugriff auf interne Anwendungen. Die Timeouts treten unregelmäßig auf und dauern 30-60 Sekunden.

#### Betroffene Systeme
- Intranet-Portal
- File-Server
- E-Mail-System

#### Symptome
- Verbindungsabbrüche ohne Fehlermeldung
- Langsame Ladezeiten
- Timeout-Fehler nach 30-60 Sekunden

#### Root Cause
Überlastung des Core-Switches während Backup-Zeiten (22:00-02:00 Uhr).

#### Workaround
```
1. Kritische Arbeiten außerhalb der Backup-Zeiten durchführen
2. Bei Timeout: Seite neu laden (F5)
3. Alternative Route über VPN nutzen (falls verfügbar)
```

#### Permanente Lösung
- **Status:** Geplant
- **ETA:** Q2 2026
- **Maßnahme:** Upgrade des Core-Switches auf höhere Bandbreite
- **Verantwortlich:** {{ meta-organisation-roles.role_IT_Operations_Manager }}

#### Betroffene Benutzer
Alle internen Benutzer während Backup-Zeiten

### KI-003: Langsame Datenbank-Queries

**Status:** Gelöst  
**Priorität:** P2 (Hoch)  
**Erstellt:** 2025-01-10  
**Gelöst:** 2025-01-25  
**Ticket-ID:** INC-12340

#### Beschreibung
Bestimmte Datenbank-Queries liefen sehr langsam (> 10 Sekunden), was zu Timeouts in der Anwendung führte.

#### Betroffene Systeme
- Produktions-Datenbank
- Web-Anwendung

#### Symptome
- Langsame Seitenladezeiten
- Timeout-Fehler
- Hohe CPU-Last auf DB-Server

#### Root Cause
Fehlende Indizes auf häufig abgefragten Tabellen.

#### Lösung
```sql
-- Fehlende Indizes hinzugefügt
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_orders_date ON orders(order_date);
CREATE INDEX idx_products_category ON products(category_id);

-- Statistiken aktualisiert
ANALYZE TABLE users;
ANALYZE TABLE orders;
ANALYZE TABLE products;
```

#### Ergebnis
- Query-Zeit reduziert von 10+ Sekunden auf < 100ms
- CPU-Last auf DB-Server normalisiert
- Keine Timeouts mehr

## Häufig gestellte Fragen (FAQ)

### Allgemeine Fragen

#### F: Wie erreiche ich den IT-Support?

**A:** Der IT-Support ist über folgende Kanäle erreichbar:
- **E-Mail:** {{ meta-organisation-roles.role_Service_Desk_Lead_email }}
- **Telefon:** {{ meta-organisation-roles.role_Service_Desk_Lead_phone }}
- **Ticketing-System:** [TODO: URL]
- **Chat:** [TODO: Chat-Kanal]

**Support-Zeiten:**
- Mo-Fr: 08:00-18:00 Uhr
- 24/7 für kritische Incidents (P1)

#### F: Wie erstelle ich ein Support-Ticket?

**A:** Support-Tickets können über folgende Wege erstellt werden:

1. **Web-Portal:**
   - [TODO: Ticketing-URL] aufrufen
   - Mit SSO anmelden
   - "Neues Ticket" klicken
   - Formular ausfüllen und absenden

2. **E-Mail:**
   - E-Mail an {{ meta-organisation-roles.role_Service_Desk_Lead_email }}
   - Betreff: Kurze Problembeschreibung
   - Inhalt: Detaillierte Beschreibung, Screenshots

3. **Telefon:**
   - {{ meta-organisation-roles.role_Service_Desk_Lead_phone }} anrufen
   - Problem schildern
   - Ticket-Nummer notieren

#### F: Wie priorisiert der Support Tickets?

**A:** Tickets werden nach folgenden Prioritäten bearbeitet:

| Priorität | Beschreibung | Reaktionszeit | Lösungszeit |
|---|---|---|---|
| P1 - Kritisch | Kompletter Systemausfall | 15 Minuten | 4 Stunden |
| P2 - Hoch | Teilausfall, viele Benutzer betroffen | 1 Stunde | 8 Stunden |
| P3 - Mittel | Einzelne Benutzer betroffen | 4 Stunden | 24 Stunden |
| P4 - Niedrig | Fragen, Feature-Requests | 8 Stunden | 72 Stunden |

### Zugriff und Authentifizierung

#### F: Ich habe mein Passwort vergessen. Was soll ich tun?

**A:** Passwort-Reset über Self-Service-Portal:

1. [TODO: Self-Service-URL] aufrufen
2. "Passwort vergessen" klicken
3. Benutzername oder E-Mail eingeben
4. Sicherheitsfragen beantworten oder Code per E-Mail/SMS erhalten
5. Neues Passwort setzen

**Alternativ:** IT-Support kontaktieren

#### F: Wie richte ich MFA (Multi-Faktor-Authentifizierung) ein?

**A:** MFA-Einrichtung:

1. [TODO: MFA-Portal-URL] aufrufen
2. Mit aktuellem Passwort anmelden
3. MFA-Methode wählen:
   - **Authenticator-App** (empfohlen): QR-Code scannen
   - **SMS:** Telefonnummer verifizieren
   - **Hardware-Token:** Token registrieren
4. Backup-Codes generieren und sicher speichern
5. MFA testen

**Wichtig:** Backup-Codes an sicherem Ort aufbewahren!

#### F: Ich kann mich nicht per VPN verbinden. Was kann ich tun?

**A:** VPN-Troubleshooting:

1. **Credentials prüfen:**
   - Benutzername korrekt?
   - Passwort korrekt?
   - MFA-Token aktuell?

2. **VPN-Client prüfen:**
   - Neueste Version installiert?
   - Profil korrekt konfiguriert?

3. **Netzwerk prüfen:**
   - Internet-Verbindung funktioniert?
   - Firewall blockiert VPN nicht?

4. **Alternativen:**
   - Anderen VPN-Gateway versuchen
   - VPN-Client neu installieren

**Wenn nichts hilft:** IT-Support kontaktieren mit:
- VPN-Client-Version
- Fehlermeldung (Screenshot)
- Zeitpunkt des Problems

### Anwendungen

#### F: Die Anwendung lädt sehr langsam. Was kann ich tun?

**A:** Performance-Troubleshooting:

1. **Browser-Cache leeren:**
   - Chrome: Strg+Shift+Entf
   - Firefox: Strg+Shift+Entf
   - Edge: Strg+Shift+Entf

2. **Browser-Erweiterungen deaktivieren:**
   - Temporär alle Erweiterungen deaktivieren
   - Testen ob Performance besser

3. **Anderen Browser testen:**
   - Chrome, Firefox, oder Edge versuchen

4. **Netzwerk prüfen:**
   - Speedtest durchführen
   - VPN-Verbindung prüfen

5. **System-Ressourcen prüfen:**
   - Task-Manager öffnen
   - CPU/RAM-Auslastung prüfen
   - Andere Programme schließen

**Wenn Problem weiterhin besteht:** Ticket erstellen mit:
- Browser und Version
- Betroffene Anwendung
- Zeitpunkt des Problems
- Screenshot

#### F: Ich erhalte einen "500 Internal Server Error". Was bedeutet das?

**A:** Ein 500-Fehler bedeutet, dass ein Problem auf dem Server aufgetreten ist.

**Sofortmaßnahmen:**
1. Seite neu laden (F5)
2. 5 Minuten warten und erneut versuchen
3. Browser-Cache leeren
4. Anderen Browser versuchen

**Wenn Fehler weiterhin auftritt:**
- Ticket erstellen (P2 - Hoch)
- Screenshot des Fehlers anhängen
- Genaue URL angeben
- Zeitpunkt notieren

**Für IT-Team:**
- Server-Logs prüfen
- Anwendungs-Logs prüfen
- Monitoring-Alerts prüfen

### E-Mail

#### F: Ich kann keine E-Mails senden. Was soll ich tun?

**A:** E-Mail-Versand-Troubleshooting:

1. **Postausgang prüfen:**
   - Sind E-Mails im Postausgang hängen geblieben?
   - Fehlermeldung vorhanden?

2. **Postfach-Größe prüfen:**
   - Ist das Postfach voll?
   - Alte E-Mails archivieren/löschen

3. **Anhänge prüfen:**
   - Sind Anhänge zu groß? (Max: [TODO: Größe])
   - Anhänge komprimieren oder über File-Sharing senden

4. **Empfänger-Adresse prüfen:**
   - Ist die E-Mail-Adresse korrekt?
   - Tippfehler?

5. **Spam-Filter:**
   - Wurde E-Mail als Spam markiert?

**Wenn Problem weiterhin besteht:** IT-Support kontaktieren

#### F: Ich erhalte viele Spam-E-Mails. Was kann ich tun?

**A:** Spam-Reduzierung:

1. **Spam-Filter trainieren:**
   - Spam-E-Mails als "Spam" markieren
   - Nicht als "Spam" markierte E-Mails als "Kein Spam" markieren

2. **Absender blockieren:**
   - Absender zur Blocklist hinzufügen

3. **E-Mail-Regeln erstellen:**
   - Automatische Filterung basierend auf Absender/Betreff

4. **Vorsicht bei E-Mail-Weitergabe:**
   - E-Mail-Adresse nicht öffentlich posten
   - Separate E-Mail für Newsletter verwenden

**Bei verdächtigen E-Mails:**
- **NICHT** auf Links klicken
- **NICHT** Anhänge öffnen
- An {{ meta-organisation-roles.role_CISO_email }} weiterleiten
- E-Mail löschen

### Dateien und Storage

#### F: Ich habe versehentlich eine Datei gelöscht. Kann sie wiederhergestellt werden?

**A:** Datei-Wiederherstellung:

1. **Papierkorb prüfen:**
   - Windows: Papierkorb auf Desktop
   - macOS: Papierkorb im Dock
   - Linux: Trash-Ordner

2. **Netzwerk-Laufwerk:**
   - Vorgängerversionen prüfen (Rechtsklick → Eigenschaften → Vorgängerversionen)
   - Shadow Copies verfügbar?

3. **Backup-Wiederherstellung:**
   - Ticket erstellen (P3 - Mittel)
   - Dateiname, Pfad und ungefähres Löschdatum angeben
   - IT-Team stellt aus Backup wieder her

**Wichtig:** Je schneller gemeldet, desto höher die Erfolgsaussicht!

**Backup-Retention:**
- Tägliche Backups: 30 Tage
- Wöchentliche Backups: 90 Tage
- Monatliche Backups: 1 Jahr

#### F: Mein Netzwerk-Laufwerk ist voll. Was soll ich tun?

**A:** Storage-Management:

1. **Speicherplatz analysieren:**
   - Große Dateien identifizieren
   - Alte/unnötige Dateien löschen

2. **Dateien archivieren:**
   - Alte Projekte archivieren
   - Auf Archiv-Storage verschieben

3. **Duplikate entfernen:**
   - Doppelte Dateien identifizieren und löschen

4. **Komprimierung:**
   - Große Dateien komprimieren (ZIP, 7z)

5. **Quota-Erhöhung beantragen:**
   - Ticket erstellen mit Begründung
   - Genehmigung durch Manager erforderlich

**Quota-Limits:**
- Standard-Benutzer: [TODO: Größe]
- Power-User: [TODO: Größe]
- Projekt-Shares: [TODO: Größe]

### Hardware

#### F: Mein Computer ist sehr langsam. Was kann ich tun?

**A:** Performance-Optimierung:

1. **Neustart:**
   - Computer neu starten
   - Oft löst dies bereits das Problem

2. **Programme schließen:**
   - Unnötige Programme beenden
   - Task-Manager prüfen (Strg+Shift+Esc)

3. **Disk-Cleanup:**
   - Temporäre Dateien löschen
   - Disk-Cleanup-Tool ausführen

4. **Updates prüfen:**
   - Windows-Updates installieren
   - Anwendungs-Updates installieren

5. **Malware-Scan:**
   - Antivirus-Scan durchführen

**Wenn Problem weiterhin besteht:**
- Ticket erstellen
- Hardware-Upgrade prüfen
- Neuinstallation erwägen

#### F: Wie beantrage ich neue Hardware?

**A:** Hardware-Anforderung:

1. **Ticket erstellen:**
   - Kategorie: "Hardware-Anfrage"
   - Gewünschte Hardware spezifizieren
   - Begründung angeben

2. **Genehmigung:**
   - Manager-Genehmigung erforderlich
   - Budget-Prüfung durch [TODO]

3. **Beschaffung:**
   - IT-Team bestellt Hardware
   - Lieferzeit: [TODO: Zeitraum]

4. **Installation:**
   - Termin mit IT-Team vereinbaren
   - Alte Hardware wird zurückgenommen

**Standard-Hardware:**
- Laptop: [TODO: Modell]
- Desktop: [TODO: Modell]
- Monitor: [TODO: Modell]
- Peripherie: Maus, Tastatur, Headset

## Troubleshooting-Tipps

### Allgemeine Troubleshooting-Schritte

1. **Neustart:**
   - Oft die einfachste Lösung
   - Computer, Anwendung, oder Service neu starten

2. **Fehler dokumentieren:**
   - Screenshot erstellen
   - Fehlermeldung notieren
   - Zeitpunkt festhalten

3. **Reproduzieren:**
   - Problem erneut auslösen
   - Schritte dokumentieren

4. **Isolieren:**
   - Anderer Computer?
   - Anderer Browser?
   - Anderes Netzwerk?

5. **Recherchieren:**
   - Bekannte Probleme prüfen (dieses Dokument)
   - Wiki durchsuchen
   - Kollegen fragen

6. **Eskalieren:**
   - Ticket erstellen
   - IT-Support kontaktieren

### Browser-Probleme

**Symptome:**
- Seite lädt nicht
- Fehlerhafte Darstellung
- Funktionen funktionieren nicht

**Lösungen:**
1. Cache leeren (Strg+Shift+Entf)
2. Cookies löschen
3. Browser-Erweiterungen deaktivieren
4. Inkognito-Modus testen
5. Anderen Browser testen
6. Browser neu installieren

### Netzwerk-Probleme

**Symptome:**
- Keine Verbindung
- Langsame Verbindung
- Intermittierende Verbindung

**Lösungen:**
1. Netzwerk-Kabel prüfen
2. WLAN-Verbindung prüfen
3. Router neu starten
4. IP-Konfiguration erneuern (ipconfig /renew)
5. DNS-Cache leeren (ipconfig /flushdns)
6. VPN-Verbindung prüfen

### Anwendungs-Probleme

**Symptome:**
- Anwendung startet nicht
- Anwendung stürzt ab
- Funktionen fehlen

**Lösungen:**
1. Anwendung neu starten
2. Computer neu starten
3. Anwendung neu installieren
4. Updates installieren
5. Kompatibilitätsmodus testen (Windows)
6. Logs prüfen

## Self-Service-Ressourcen

### Dokumentation
- **Wiki:** [TODO: Wiki-URL]
- **Video-Tutorials:** [TODO: Video-URL]
- **Handbücher:** [TODO: Handbuch-URL]

### Tools
- **Self-Service-Portal:** [TODO: Portal-URL]
- **Passwort-Reset:** [TODO: Reset-URL]
- **Software-Download:** [TODO: Download-URL]

### Schulungen
- **Online-Kurse:** [TODO: Kurs-URL]
- **Webinare:** [TODO: Webinar-Kalender]
- **Präsenz-Schulungen:** Anfrage über IT-Support

## Feedback und Verbesserungen

### Feedback geben

Haben Sie Vorschläge zur Verbesserung dieses Dokuments oder der IT-Services?

**Kontakt:**
- **E-Mail:** {{ meta-organisation-roles.role_IT_Operations_Manager_email }}
- **Feedback-Formular:** [TODO: Formular-URL]

### Dokument-Updates

Dieses Dokument wird regelmäßig aktualisiert basierend auf:
- Neuen bekannten Problemen
- Häufig gestellten Fragen
- Benutzer-Feedback
- Prozessverbesserungen

**Review-Zyklus:** Monatlich  
**Verantwortlich:** {{ meta-organisation-roles.role_IT_Operations_Manager }}

## Prozesse und Verantwortlichkeiten

### RACI-Matrix

| Aktivität | Ops Manager | Ops Team | Service Desk | Benutzer |
|---|---|---|---|---|
| Bekannte Probleme dokumentieren | A | R | C | I |
| FAQ aktualisieren | A | R | C | I |
| Workarounds entwickeln | A | R | C | - |
| Benutzer-Support | C | C | R | - |
| Feedback sammeln | A | C | R | R |

> **Legende:** R = Responsible, A = Accountable, C = Consulted, I = Informed

## Compliance und Standards

### Relevante Standards
- **ITIL v4:** Service Desk Practice, Knowledge Management
- **ISO 20000:** Clause 8.2 - Service Desk
- **COBIT 2019:** DSS02 - Managed Service Requests and Incidents

## Anhang

### Glossar

| Begriff | Definition |
|---|---|
| Known Issue | Bekanntes Problem mit dokumentiertem Workaround |
| FAQ | Frequently Asked Questions - Häufig gestellte Fragen |
| Workaround | Temporäre Lösung für ein Problem |
| Root Cause | Grundursache eines Problems |
| Self-Service | Benutzer löst Problem selbst ohne Support |

### Referenzen
- ITIL v4 Foundation Handbook
- ISO/IEC 20000-1:2018
- COBIT 2019 Framework

**Letzte Aktualisierung:** {{ meta-handbook.date }}  
**Nächste Review:** [TODO: Datum]  
**Kontakt:** {{ meta-organisation-roles.role_IT_Operations_Manager_email }}

