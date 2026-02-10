# CIS Controls v8 Hardening Templates (Deutsch)

## Überblick

Diese Templates bilden die Grundlage für ein vollständiges CIS Controls v8 Hardening-Handbuch. Das Handbuch umfasst 27 strukturierte Dokumente, die Hardening-Baselines für Betriebssysteme und Applikationen nach den **CIS Controls v8** Framework abdecken.

## Template-Struktur

### Foundation (0010-0050) - 5 Templates
- **0010**: CIS Controls Überblick und Vorgehen
- **0020**: Geltungsbereich, Assetgruppen und Tiering
- **0030**: Hardening-Lifecycle und Prozesse
- **0040**: Ausnahmen und Risikoakzeptanz
- **0050**: Test und Validierung

### Betriebssysteme (0100-0150) - 6 Templates
- **0100**: Windows Server Hardening Baseline
- **0110**: Windows Client Hardening Baseline
- **0120**: Linux Hardening Baseline
- **0130**: macOS Hardening Baseline
- **0140**: Container Base Images Hardening
- **0150**: Mobile Device Hardening

### Applikationen (0200-0330) - 14 Templates
- **0200**: Nginx Webserver Hardening
- **0210**: Apache Webserver Hardening
- **0220**: IIS Webserver Hardening
- **0230**: Tomcat Application Server Hardening
- **0240**: PostgreSQL Database Hardening
- **0250**: MySQL/MariaDB Database Hardening
- **0260**: MS SQL Server Database Hardening
- **0270**: MongoDB Database Hardening
- **0280**: Kubernetes Cluster Hardening
- **0290**: Docker Engine Hardening
- **0300**: SSH Service Hardening
- **0310**: Active Directory Hardening
- **0320**: Identity Provider Hardening
- **0330**: Cloud Platform Hardening

### Anhänge (0400-0410) - 2 Templates
- **0400**: Control Mapping Template
- **0410**: Checklisten und Evidence

## Nummerierungsschema

- Templates verwenden 4-stellige Nummern mit 10er-Schritten (0010, 0020, 0030, ...)
- Dies ermöglicht spätere Einfügungen zwischen bestehenden Templates
- Nummernbereiche gruppieren zusammengehörige Themen

## Verwendung

1. **Vorbereitung**: Bestimmen Sie die Asset-Gruppen und Tiering-Stufen
2. **Baseline-Auswahl**: Wählen Sie relevante Hardening-Baselines
3. **Anpassung**: Passen Sie die Templates an Ihre Umgebung an
4. **Platzhalter**: Ersetzen Sie alle `[TODO]`-Markierungen
5. **Testing**: Validieren Sie Hardening-Maßnahmen in Testumgebung
6. **Rollout**: Implementieren Sie schrittweise in Produktion

## Platzhalter

Templates unterstützen zwei Arten von Platzhaltern:

- **Manuelle Platzhalter**: `[TODO: Beschreibung]` - müssen manuell ersetzt werden
- **Automatische Platzhalter**: `{{ source.field }}` - werden aus Datenquellen befüllt

Beispiele für automatische Platzhalter:
- `{{ meta.organization }}` - Organisationsname
- `Andreas Huemmer [andreas.huemmer@adminsend.de]` - Autor
- `{{ meta.version }}` - Versionsnummer
- `{{ meta.date }}` - Datum

## CIS Controls v8 Framework

Die Templates basieren auf dem CIS Controls v8 Framework mit 18 Controls:

- **CIS Control 1**: Inventory and Control of Enterprise Assets
- **CIS Control 2**: Inventory and Control of Software Assets
- **CIS Control 3**: Data Protection
- **CIS Control 4**: Secure Configuration of Enterprise Assets and Software
- **CIS Control 5**: Account Management
- **CIS Control 6**: Access Control Management
- **CIS Control 7**: Continuous Vulnerability Management
- **CIS Control 8**: Audit Log Management
- **CIS Control 9**: Email and Web Browser Protections
- **CIS Control 10**: Malware Defenses
- **CIS Control 11**: Data Recovery
- **CIS Control 12**: Network Infrastructure Management
- **CIS Control 13**: Network Monitoring and Defense
- **CIS Control 14**: Security Awareness and Skills Training
- **CIS Control 15**: Service Provider Management
- **CIS Control 16**: Application Software Security
- **CIS Control 17**: Incident Response Management
- **CIS Control 18**: Penetration Testing

## Implementation Groups (IG)

Die CIS Controls definieren drei Implementation Groups:

- **IG1**: Essential Cyber Hygiene (für kleine Organisationen)
- **IG2**: Foundational (für mittlere Organisationen)
- **IG3**: Advanced (für große Organisationen mit hohem Risiko)

## Generierung des Handbuchs

### CLI-Verwendung

```bash
# Deutsches CIS Controls-Handbuch generieren
./handbook-generator --language de --template cis-controls --test

# Englisches CIS Controls-Handbuch generieren
./handbook-generator --language en --template cis-controls --test

# Alle Formate mit allen Features generieren
./handbook-generator --language de --template cis-controls --output all --test --separate-files --pdf-toc
```

## Framework Mapping

Siehe `FRAMEWORK_MAPPING.md` für eine detaillierte Zuordnung der Templates zu CIS Controls v8 Komponenten.

## Weitere Ressourcen

- CIS Controls Website: https://www.cisecurity.org/controls/
- CIS Benchmarks: https://www.cisecurity.org/cis-benchmarks/
- CIS-CAT Pro Tool für automatisierte Compliance-Prüfung

## Support

Bei Fragen zur Verwendung dieser Templates oder zu CIS Controls:
- Ihr internes Sicherheitsteam
- CIS Community: https://www.cisecurity.org/community/

---

**Version:** 1.0.0  
**Letzte Aktualisierung:** 2026-02-10  
**Maintainer:** CIS Controls Template-Team
