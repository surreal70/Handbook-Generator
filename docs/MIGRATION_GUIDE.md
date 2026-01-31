# Migrations-Guide: IT-Operations Template-Erweiterung

## Überblick

Dieser Guide beschreibt die Migration von bestehenden Handbuch-Generator-Installationen zur erweiterten Version mit IT-Operations-Templates und Meta-Platzhalter-System.

**Version:** 2.0.0  
**Datum:** Januar 2025  
**Zielgruppe:** Bestehende Nutzer des Handbuch-Generators

## Was ist neu?

Die erweiterte Version bringt folgende neue Features:

### 1. Meta-Platzhalter-System
- Neue Datenquelle für organisationsweite Metadaten
- Zentrale Verwaltung von Organisationsinformationen
- Platzhalter im Format `{{ meta.feld }}`

### 2. Globale Metadaten-Konfiguration
- Neue Datei `metadata.yaml` für Organisationsdaten
- Rollen-Management (CEO, CIO, CISO, CFO, COO, etc.)
- Dokumentverantwortliche und Genehmiger

### 3. Erweiterte IT-Operations-Templates
- 29 neue fachspezifische Templates
- ITIL v4, ISO 20000 und COBIT 2019 konform
- Umbenannte und restrukturierte bestehende Templates

### 4. Generisches Service-Beschreibungs-Template
- Wiederverwendbares Template für individuelle Services
- Anpassbar für jeden IT-Service
- Integriert Meta- und NetBox-Platzhalter

## Abwärtskompatibilität

**Garantiert kompatibel:**
- ✅ Bestehende Templates funktionieren unverändert
- ✅ Bestehende `config.yaml` bleibt gültig
- ✅ Bestehende NetBox-Platzhalter funktionieren
- ✅ CLI-Befehle bleiben gleich
- ✅ Keine Breaking Changes in der API

**Optional:**
- ℹ️ `metadata.yaml` ist optional (wird automatisch erstellt)
- ℹ️ Meta-Platzhalter sind optional
- ℹ️ Neue IT-Operations-Templates sind zusätzlich verfügbar

## Migrations-Schritte

### Schritt 1: Backup erstellen

Erstellen Sie vor der Migration ein Backup Ihrer aktuellen Installation:

```bash
# Backup der Konfiguration
cp config.yaml config.yaml.backup

# Backup der Templates (falls angepasst)
cp -r templates/ templates.backup/

# Backup der generierten Handbücher
cp -r Handbook/ Handbook.backup/
```

### Schritt 2: Code aktualisieren

Aktualisieren Sie den Handbuch-Generator auf die neue Version:

```bash
# Git Repository aktualisieren
git pull origin main

# Oder: Neue Version herunterladen und entpacken
# wget https://github.com/your-repo/handbook-generator/archive/v2.0.0.zip
# unzip v2.0.0.zip
```

### Schritt 3: Dependencies aktualisieren

Die neue Version verwendet dieselben Dependencies, aber stellen Sie sicher, dass alles aktuell ist:

```bash
# Virtual Environment aktivieren
source venv/bin/activate  # Linux/Mac
# oder
venv\Scripts\activate  # Windows

# Dependencies aktualisieren
pip install -r requirements.txt --upgrade
```

**Hinweis:** Es werden keine neuen externen Dependencies benötigt!

### Schritt 4: Metadata.yaml erstellen

Die neue Version erstellt automatisch eine `metadata.yaml` beim ersten Start:

```bash
# Generator starten - metadata.yaml wird automatisch erstellt
python -m src.cli --language de --template it-operation
```

Sie sehen folgende Meldung:
```
INFO: Metadata configuration file 'metadata.yaml' not found.
INFO: Creating default metadata.yaml with example values.
INFO: Please edit metadata.yaml with your organization's information.
```

**Alternativ:** Manuell erstellen:

```bash
# Beispiel-Datei kopieren
cp metadata.example.yaml metadata.yaml

# Mit Editor öffnen und anpassen
nano metadata.yaml
# oder
code metadata.yaml
```

### Schritt 5: Metadata.yaml anpassen

Öffnen Sie `metadata.yaml` und passen Sie die Werte an Ihre Organisation an:

```yaml
# Global Metadata Configuration

organization:
  name: "Ihre Organisation GmbH"           # ← Anpassen
  address: "Ihre Straße 123"               # ← Anpassen
  city: "Ihre Stadt"                       # ← Anpassen
  postal_code: "12345"                     # ← Anpassen
  country: "Deutschland"                   # ← Anpassen
  website: "https://www.ihre-org.de"       # ← Anpassen
  phone: "+49 123 456789"                  # ← Anpassen
  email: "info@ihre-org.de"                # ← Anpassen

roles:
  ceo:
    name: "Max Mustermann"                 # ← Anpassen
    title: "Chief Executive Officer"       # ← Anpassen
    email: "max.mustermann@ihre-org.de"    # ← Anpassen
    phone: "+49 123 456789-100"            # ← Anpassen
    department: "Management"
  
  cio:
    name: "Anna Schmidt"                   # ← Anpassen
    title: "Chief Information Officer"
    email: "anna.schmidt@ihre-org.de"      # ← Anpassen
    phone: "+49 123 456789-200"            # ← Anpassen
    department: "IT"
  
  # ... weitere Rollen anpassen

document:
  owner: "IT Operations Manager"           # ← Anpassen
  approver: "CIO"                          # ← Anpassen
  version: "1.0.0"
  classification: "internal"               # public, internal, confidential, restricted

defaults:
  author: "Ihr Name [ihre.email@ihre-org.de]"  # ← Anpassen
  language: "de"
```

**Wichtige Felder:**
- `organization.name` - Pflichtfeld
- `document.owner` - Pflichtfeld
- Alle Rollen-E-Mails sollten gültig sein

### Schritt 6: Bestehende Templates prüfen (optional)

Wenn Sie eigene Templates erstellt oder angepasst haben, prüfen Sie diese:

```bash
# Template-Struktur validieren
python -m src.template_validator --check-structure

# Platzhalter-Syntax prüfen
python -m src.template_validator --check-placeholders
```

**Hinweis:** Bestehende Templates funktionieren ohne Änderungen!

### Schritt 7: Neue IT-Operations-Templates testen

Testen Sie die neuen IT-Operations-Templates:

```bash
# Deutsches IT-Operations-Handbuch generieren
python -m src.cli --language de --template it-operation --verbose

# Englisches IT-Operations-Handbuch generieren
python -m src.cli --language en --template it-operation --verbose
```

Prüfen Sie die Ausgabe in `Handbook/de/it-operation/` bzw. `Handbook/en/it-operation/`.

### Schritt 8: Meta-Platzhalter in eigenen Templates verwenden (optional)

Wenn Sie eigene Templates haben, können Sie jetzt Meta-Platzhalter verwenden:

**Vorher (nur NetBox):**
```markdown
# Geräteinformationen

Gerätename: {{ netbox.device_name }}
Standort: {{ netbox.site_name }}
```

**Nachher (mit Meta-Platzhaltern):**
```markdown
# Geräteinformationen

**Organisation:** {{ meta.organization.name }}
**Verantwortlich:** {{ meta.cio.name }} ({{ meta.cio.email }})

Gerätename: {{ netbox.device_name }}
Standort: {{ netbox.site_name }}
```

### Schritt 9: Konfiguration in Git aktualisieren (optional)

Wenn Sie Git verwenden, aktualisieren Sie Ihre `.gitignore`:

```bash
# .gitignore prüfen
cat .gitignore

# Sollte enthalten:
# config.yaml
# metadata.yaml  ← Neu (optional, enthält keine Credentials)
# Handbook/
# venv/
```

**Hinweis:** `metadata.yaml` enthält keine Credentials, kann aber sensible Informationen (Namen, E-Mails) enthalten. Entscheiden Sie selbst, ob Sie diese Datei committen möchten.

### Schritt 10: Dokumentation aktualisieren

Aktualisieren Sie Ihre interne Dokumentation:

- Neue `metadata.yaml` Konfiguration dokumentieren
- Meta-Platzhalter-Syntax erklären
- Neue IT-Operations-Templates auflisten
- Migrations-Guide für Ihr Team erstellen

## Template-Änderungen im Detail

### Umbenannte Templates

Die bestehenden IT-Operations-Templates wurden umbenannt:

| Alt | Neu | Grund |
|-----|-----|-------|
| `0100_einleitung.md` | `0010_Einleitung.md` | Neue Nummerierung |
| `0200_betriebsprozesse.md` | `0011_Rahmenbedingungen.md` | Neue Nummerierung + Umbenennung |
| `0100_introduction.md` (en) | `0010_Introduction.md` | Neue Nummerierung |
| `0200_operational_processes.md` (en) | `0011_Framework_Conditions.md` | Neue Nummerierung + Umbenennung |

**Aktion erforderlich:** Keine - Templates werden automatisch umbenannt.

### Neue Templates

29 neue IT-Operations-Templates wurden hinzugefügt (0020-0290):

**Grundlagen:**
- 0020: Dokumentenlenkung und Versionierung
- 0030: Servicebeschreibung und Kritikalität
- 0040: Systemübersicht und Architektur
- 0050: Infrastruktur und Plattform
- 0060: Rollen und Verantwortlichkeiten

**Betriebsprozesse:**
- 0070: Betriebskonzept und Betriebsprozesse
- 0080: Betriebsübergabe und Go-Live-Checkliste
- 0090: Konfigurationsmanagement und CMDB
- 0100: Access- und Berechtigungsmanagement
- 0110: Monitoring, Alerting und Observability

**Service Management:**
- 0120: Incident Management – Runbook
- 0130: Problem Management und Postmortems
- 0140: Change- und Release-Management
- 0150: Backup und Restore
- 0160: Disaster Recovery und Business Continuity

**Security & Compliance:**
- 0170: Sicherheitsbetrieb und Hardening
- 0180: Patch- und Update-Management
- 0190: Log Management und Audit
- 0280: Compliance und Audits

**Operations & Support:**
- 0200: Kapazitäts- und Performance-Management
- 0210: Verfügbarkeit und Service Level
- 0220: Datenmanagement und Datenschutz
- 0230: Wartung und Operations-Routinen
- 0240: Runbooks – Standardoperationen
- 0250: Tooling und Zugangswege
- 0260: Bekannte Probleme und FAQ
- 0270: Kontakte, Eskalation und Anbieter
- 0290: Anhang: Checklisten und Vorlagen

**Aktion erforderlich:** Keine - Templates sind automatisch verfügbar.

## Neue Features nutzen

### Meta-Platzhalter verwenden

Meta-Platzhalter ermöglichen den Zugriff auf organisationsweite Metadaten:

**Organisationsinformationen:**
```markdown
Organisation: {{ meta.organization.name }}
Adresse: {{ meta.organization.address }}
Stadt: {{ meta.organization.city }}
Website: {{ meta.organization.website }}
E-Mail: {{ meta.organization.email }}
Telefon: {{ meta.organization.phone }}
```

**Rollen und Verantwortliche:**
```markdown
CEO: {{ meta.ceo.name }} ({{ meta.ceo.email }})
CIO: {{ meta.cio.name }} ({{ meta.cio.email }})
CISO: {{ meta.ciso.name }} ({{ meta.ciso.email }})
CFO: {{ meta.cfo.name }} ({{ meta.cfo.email }})
COO: {{ meta.coo.name }} ({{ meta.coo.email }})

IT Operations Manager: {{ meta.it_operations_manager.name }}
Service Desk Lead: {{ meta.service_desk_lead.name }}
```

**Dokumentinformationen:**
```markdown
Dokumentverantwortlicher: {{ meta.document.owner }}
Genehmigt durch: {{ meta.document.approver }}
Version: {{ meta.document.version }}
Klassifizierung: {{ meta.document.classification }}
```

**Shortcuts:**
```markdown
Autor: {{ meta.author }}
Sprache: {{ meta.language }}
```

### Gemischte Platzhalter verwenden

Sie können Meta- und NetBox-Platzhalter kombinieren:

```markdown
# Service-Übersicht

**Organisation:** {{ meta.organization.name }}
**Verantwortlich:** {{ meta.cio.name }}

## Infrastruktur

**Standort:** {{ netbox.site.name }}
**Gerät:** {{ netbox.device.name }}
**IP-Adresse:** {{ netbox.primary_ip }}

## Kontakt

Bei Fragen wenden Sie sich an:
- **IT Operations:** {{ meta.it_operations_manager.name }} ({{ meta.it_operations_manager.email }})
- **Service Desk:** {{ meta.service_desk_lead.name }} ({{ meta.service_desk_lead.email }})
```

### Service-Beschreibungs-Template verwenden

Das neue generische Service-Template ermöglicht die Erstellung individueller Service-Dokumentationen:

**Schritt 1:** Template kopieren
```bash
# Deutsches Template
cp templates/de/service-templates/service_description_template.md \
   templates/de/service-templates/mein_service.md

# Englisches Template
cp templates/en/service-templates/service_description_template.md \
   templates/en/service-templates/my_service.md
```

**Schritt 2:** Template anpassen
```bash
# Template öffnen und [TODO] Markierungen ersetzen
nano templates/de/service-templates/mein_service.md
```

**Schritt 3:** Handbuch generieren
```bash
python -m src.cli --language de --template service-templates
```

## Fehlerbehebung

### Problem: metadata.yaml wird nicht gefunden

**Symptom:**
```
WARNING: Metadata configuration file 'metadata.yaml' not found.
```

**Lösung:**
```bash
# Default-Datei wird automatisch erstellt
# Oder manuell erstellen:
cp metadata.example.yaml metadata.yaml
```

### Problem: Meta-Platzhalter werden nicht ersetzt

**Symptom:**
```
{{ meta.organization.name }} bleibt im generierten Handbuch stehen
```

**Ursachen und Lösungen:**

1. **Feld nicht in metadata.yaml definiert:**
```bash
# Prüfen Sie metadata.yaml
cat metadata.yaml | grep "organization:"
cat metadata.yaml | grep "name:"
```

2. **Falscher Feldpfad:**
```markdown
# Falsch:
{{ meta.org.name }}

# Richtig:
{{ meta.organization.name }}
```

3. **Rolle nicht definiert:**
```bash
# Prüfen Sie, ob die Rolle existiert
cat metadata.yaml | grep "ceo:"
```

### Problem: Validierungsfehler in metadata.yaml

**Symptom:**
```
ERROR: Invalid metadata configuration: Missing required field 'organization.name'
```

**Lösung:**
```bash
# Prüfen Sie die YAML-Syntax
python -c "import yaml; yaml.safe_load(open('metadata.yaml'))"

# Prüfen Sie Pflichtfelder
grep "organization:" metadata.yaml
grep "name:" metadata.yaml
grep "document:" metadata.yaml
grep "owner:" metadata.yaml
```

### Problem: Templates nicht gefunden

**Symptom:**
```
ERROR: Template directory not found: templates/de/it-operation/
```

**Lösung:**
```bash
# Prüfen Sie die Template-Struktur
ls -la templates/de/it-operation/

# Falls fehlend, Git-Repository aktualisieren
git pull origin main

# Oder Templates manuell kopieren
cp -r input/IT-Betriebshandbuch-Templates/* templates/de/it-operation/
```

### Problem: Umbenannte Templates nicht gefunden

**Symptom:**
```
ERROR: Template file not found: 0100_einleitung.md
```

**Lösung:**
```bash
# Templates wurden umbenannt
# Alte Namen: 0100_einleitung.md, 0200_betriebsprozesse.md
# Neue Namen: 0010_Einleitung.md, 0011_Rahmenbedingungen.md

# Prüfen Sie die neuen Dateinamen
ls -la templates/de/it-operation/00*.md
```

### Problem: RACI-Matrix-Warnung

**Symptom:**
```
WARNING: RACI matrix in template '0060_Rollen_und_Verantwortlichkeiten.md' has incomplete cells.
```

**Lösung:**
```bash
# Öffnen Sie das Template und füllen Sie alle RACI-Zellen aus
nano templates/de/it-operation/0060_Rollen_und_Verantwortlichkeiten.md

# Jede Zelle sollte R, A, C oder I enthalten
```

## Best Practices

### 1. Metadata.yaml pflegen

- ✅ Halten Sie `metadata.yaml` aktuell
- ✅ Validieren Sie E-Mail-Adressen
- ✅ Verwenden Sie konsistente Telefonnummern-Formate
- ✅ Dokumentieren Sie Änderungen in der Versionstabelle

### 2. Meta-Platzhalter konsistent verwenden

- ✅ Verwenden Sie Meta-Platzhalter für organisationsweite Informationen
- ✅ Verwenden Sie NetBox-Platzhalter für technische Details
- ✅ Kombinieren Sie beide Quellen für vollständige Dokumentation

### 3. Templates anpassen

- ✅ Kopieren Sie Templates vor Anpassungen
- ✅ Behalten Sie die Nummerierung bei
- ✅ Dokumentieren Sie Änderungen
- ✅ Testen Sie nach Anpassungen

### 4. Versionierung

- ✅ Verwenden Sie Git für Template-Versionierung
- ✅ Taggen Sie Releases (v1.0.0, v2.0.0)
- ✅ Dokumentieren Sie Breaking Changes
- ✅ Erstellen Sie Backups vor Updates

### 5. Sicherheit

- ✅ Schützen Sie `config.yaml` (enthält API-Token)
- ℹ️ Entscheiden Sie, ob `metadata.yaml` committed werden soll
- ✅ Verwenden Sie `.gitignore` für sensible Dateien
- ✅ Setzen Sie Dateiberechtigungen (640 für Konfigurationsdateien)

## Rollback-Strategie

Falls Probleme auftreten, können Sie zur alten Version zurückkehren:

### Schritt 1: Backup wiederherstellen

```bash
# Konfiguration wiederherstellen
cp config.yaml.backup config.yaml

# Templates wiederherstellen (falls angepasst)
rm -rf templates/
cp -r templates.backup/ templates/

# Handbücher wiederherstellen
rm -rf Handbook/
cp -r Handbook.backup/ Handbook/
```

### Schritt 2: Alte Version wiederherstellen

```bash
# Git: Zur alten Version zurückkehren
git checkout v1.0.0

# Oder: Alte Version neu installieren
# Download und entpacken der alten Version
```

### Schritt 3: Dependencies wiederherstellen

```bash
# Virtual Environment neu erstellen
rm -rf venv/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Support und Hilfe

### Dokumentation

- **README.md** - Allgemeine Nutzung
- **docs/MIGRATION_GUIDE.md** - Dieser Guide
- **templates/de/it-operation/README.md** - Template-Dokumentation
- **docs/FRAMEWORK_MAPPING.md** - ITIL/ISO/COBIT Mapping

### Logs und Debugging

```bash
# Verbose Logging aktivieren
python -m src.cli --verbose --language de --template it-operation

# Log-Datei prüfen
cat handbook_generator.log

# Platzhalter-Statistiken anzeigen
python -m src.cli --verbose --language de --template it-operation | grep "Placeholder"
```

### Häufige Fragen

**F: Muss ich metadata.yaml erstellen?**  
A: Nein, die Datei wird automatisch erstellt. Sie sollten sie aber mit Ihren Daten anpassen.

**F: Funktionieren meine alten Templates noch?**  
A: Ja, alle bestehenden Templates funktionieren ohne Änderungen.

**F: Muss ich Meta-Platzhalter verwenden?**  
A: Nein, Meta-Platzhalter sind optional. NetBox-Platzhalter funktionieren weiterhin.

**F: Kann ich beide Platzhalter-Typen mischen?**  
A: Ja, Sie können Meta- und NetBox-Platzhalter im selben Template verwenden.

**F: Was passiert, wenn ein Meta-Feld fehlt?**  
A: Das System gibt eine Warnung aus und lässt den Platzhalter unverändert.

**F: Sind die neuen Templates Pflicht?**  
A: Nein, die neuen IT-Operations-Templates sind optional und zusätzlich verfügbar.

**F: Kann ich die neuen Templates anpassen?**  
A: Ja, Sie können alle Templates nach Ihren Bedürfnissen anpassen.

**F: Wie aktualisiere ich nur die Templates?**  
A: Kopieren Sie die neuen Templates aus `input/IT-Betriebshandbuch-Templates/` nach `templates/de/it-operation/`.

## Kontakt

Bei Fragen oder Problemen:

**Autor:** Andreas Huemmer  
**E-Mail:** andreas.huemmer@adminsend.de  
**GitHub:** [Repository-URL]

## Changelog

### Version 2.0.0 (Januar 2025)

**Neue Features:**
- ✨ Meta-Platzhalter-System
- ✨ Globale Metadaten-Konfiguration (metadata.yaml)
- ✨ 29 neue IT-Operations-Templates
- ✨ Generisches Service-Beschreibungs-Template
- ✨ ITIL v4, ISO 20000, COBIT 2019 Compliance

**Änderungen:**
- 🔄 IT-Operations-Templates umbenannt (0100→0010, 0200→0011)
- 🔄 Template-Nummerierung erweitert (0010-0290)
- 🔄 Bilinguale Templates (de/en) für alle neuen Templates

**Verbesserungen:**
- 📈 Erweiterte Template-Validierung
- 📈 RACI-Matrix-Vollständigkeitsprüfung
- 📈 Framework-Compliance-Validierung
- 📈 Bessere Fehlerbehandlung und Warnungen

**Abwärtskompatibilität:**
- ✅ Keine Breaking Changes
- ✅ Bestehende Templates funktionieren unverändert
- ✅ Bestehende Konfiguration bleibt gültig

---

**Letzte Aktualisierung:** Januar 2025  
**Version:** 2.0.0
