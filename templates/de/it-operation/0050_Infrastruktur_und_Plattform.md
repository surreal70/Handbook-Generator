# Infrastruktur und Plattform

**Dokument-ID:** [FRAMEWORK]-0050
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

## Überblick

### Infrastrukturlandschaft

Dieses Kapitel beschreibt die physische und virtuelle Infrastruktur, auf der die IT-Services betrieben werden.

**Organisation:** {{ meta-organisation.name }}  
**Standort:** {{ meta-organisation.city }}, {{ meta-organisation.country }}

**Kurzbeschreibung:**
[TODO: Beschreiben Sie die Infrastrukturlandschaft in 2-3 Sätzen. Welche Hauptkomponenten gibt es? Wo wird die Infrastruktur betrieben?]

### Infrastruktur-Übersicht

| Kategorie | Anzahl | Typ | Standort | Kritikalität |
|---|---:|---|---|---|
| **Physische Server** | [TODO] | [TODO: Rack/Blade] | [TODO] | ☐ L ☐ M ☐ H |
| **Virtuelle Maschinen** | [TODO] | [TODO: VMware/Hyper-V] | [TODO] | ☐ L ☐ M ☐ H |
| **Container** | [TODO] | [TODO: Docker/K8s] | [TODO] | ☐ L ☐ M ☐ H |
| **Cloud-Instanzen** | [TODO] | [TODO: AWS/Azure/GCP] | [TODO] | ☐ L ☐ M ☐ H |
| **Netzwerkgeräte** | [TODO] | [TODO: Switch/Router] | [TODO] | ☐ L ☐ M ☐ H |
| **Storage-Systeme** | [TODO] | [TODO: SAN/NAS] | [TODO] | ☐ L ☐ M ☐ H |

> **Legende:**
> - **L:** Low (Niedrig)
> - **M:** Medium (Mittel)
> - **H:** High (Hoch)

## Physische Infrastruktur

### Rechenzentren und Standorte

#### Primärer Standort

- **Standort-Name:** {{ netbox.site.name }}
- **Adresse:** {{ netbox.site.physical_address }}
- **Rechenzentrum:** {{ netbox.site.facility }}
- **Betreiber:** [TODO: RZ-Betreiber]
- **Zertifizierungen:** [TODO: z.B. ISO 27001, Tier III]

**Standort-Details:**
- **Verfügbarkeit:** [TODO: z.B. 99.99%]
- **Stromversorgung:** [TODO: z.B. Redundante USV, Notstrom]
- **Kühlung:** [TODO: z.B. Redundante Klimatisierung]
- **Brandschutz:** [TODO: z.B. Gaslöschanlage]
- **Zutrittskontrolle:** [TODO: z.B. Biometrisch, 24/7 Überwachung]

#### Sekundärer Standort (DR)

- **Standort-Name:** [TODO: DR-Standort]
- **Adresse:** [TODO: Adresse]
- **Rechenzentrum:** [TODO: RZ-Name]
- **Betreiber:** [TODO: RZ-Betreiber]
- **Entfernung zum Primärstandort:** [TODO: km]

**DR-Konfiguration:**
- **DR-Strategie:** [TODO: Hot/Warm/Cold Standby]
- **Replikation:** [TODO: Synchron/Asynchron]
- **RTO:** [TODO: Stunden]
- **RPO:** [TODO: Stunden]

### Rack-Übersicht

| Rack-ID | Standort | Höhe (HE) | Belegung | Stromversorgung | Netzwerk |
|---|---|---:|---:|---|---|
| [TODO: RACK-01] | {{ netbox.site.name }} | [TODO: 42] | [TODO: 80%] | [TODO: 2x 32A] | [TODO: 2x 10G] |
| [TODO: RACK-02] | {{ netbox.site.name }} | [TODO: 42] | [TODO: 60%] | [TODO: 2x 32A] | [TODO: 2x 10G] |
| [TODO: RACK-03] | {{ netbox.site.name }} | [TODO: 42] | [TODO: 40%] | [TODO: 2x 16A] | [TODO: 2x 1G] |

### Server-Hardware

| Hostname | Typ | CPU | RAM | Storage | Standort | Rack | Rolle |
|---|---|---|---|---|---|---|---|
| {{ netbox.device.server01.name }} | [TODO: Dell R740] | [TODO: 2x Xeon] | [TODO: 256GB] | [TODO: 2TB SSD] | {{ netbox.site.name }} | [TODO: RACK-01] | [TODO: Hypervisor] |
| {{ netbox.device.server02.name }} | [TODO: HP DL380] | [TODO: 2x Xeon] | [TODO: 128GB] | [TODO: 1TB SSD] | {{ netbox.site.name }} | [TODO: RACK-01] | [TODO: Hypervisor] |
| {{ netbox.device.server03.name }} | [TODO: Dell R640] | [TODO: 2x Xeon] | [TODO: 64GB] | [TODO: 500GB SSD] | {{ netbox.site.name }} | [TODO: RACK-02] | [TODO: Application] |

**Hardware-Lifecycle:**
- **Beschaffung:** [TODO: Prozess]
- **Garantie:** [TODO: z.B. 5 Jahre NBD]
- **Refresh-Zyklus:** [TODO: z.B. 5 Jahre]
- **End-of-Life:** [TODO: Prozess]

## Netzwerkinfrastruktur

### Netzwerkarchitektur

**Netzwerk-Topologie:** [TODO: z.B. Spine-Leaf, Three-Tier]

**Redundanz:** [TODO: z.B. Vollständig redundant, N+1]

### Core-Netzwerk

| Gerät | Typ | Modell | Standort | Rolle | Uplinks |
|---|---|---|---|---|---|
| {{ netbox.device.core_switch01.name }} | Core Switch | [TODO: Cisco Nexus] | {{ netbox.site.name }} | [TODO: Core] | [TODO: 4x 100G] |
| {{ netbox.device.core_switch02.name }} | Core Switch | [TODO: Cisco Nexus] | {{ netbox.site.name }} | [TODO: Core] | [TODO: 4x 100G] |

### Distribution-Layer

| Gerät | Typ | Modell | Standort | Rolle | Uplinks |
|---|---|---|---|---|---|
| [TODO: DIST-SW-01] | Distribution Switch | [TODO: Modell] | {{ netbox.site.name }} | [TODO: Distribution] | [TODO: 2x 40G] |
| [TODO: DIST-SW-02] | Distribution Switch | [TODO: Modell] | {{ netbox.site.name }} | [TODO: Distribution] | [TODO: 2x 40G] |

### Access-Layer

| Gerät | Typ | Modell | Standort | Ports | Uplinks |
|---|---|---|---|---|---|
| [TODO: ACC-SW-01] | Access Switch | [TODO: Modell] | {{ netbox.site.name }} | [TODO: 48x 1G] | [TODO: 2x 10G] |
| [TODO: ACC-SW-02] | Access Switch | [TODO: Modell] | {{ netbox.site.name }} | [TODO: 48x 1G] | [TODO: 2x 10G] |

### VLAN-Segmentierung

| VLAN-ID | Name | Zweck | Subnetz | Gateway |
|---:|---|---|---|---|
| {{ netbox.vlan.management.vid }} | Management | [TODO: Management-Netz] | {{ netbox.vlan.management.prefix }} | [TODO: Gateway] |
| {{ netbox.vlan.production.vid }} | Production | [TODO: Produktions-Netz] | {{ netbox.vlan.production.prefix }} | [TODO: Gateway] |
| [TODO: 30] | DMZ | [TODO: DMZ-Netz] | [TODO: 10.0.30.0/24] | [TODO: 10.0.30.1] |
| [TODO: 40] | Storage | [TODO: Storage-Netz] | [TODO: 10.0.40.0/24] | [TODO: 10.0.40.1] |
| [TODO: 50] | Backup | [TODO: Backup-Netz] | [TODO: 10.0.50.0/24] | [TODO: 10.0.50.1] |

### IP-Adressierung

**IP-Adressplan:**

| Netzwerk | Verwendung | CIDR | Verfügbare IPs | Belegung |
|---|---|---|---:|---:|
| [TODO: 10.0.0.0/16] | Gesamt | [TODO: /16] | [TODO: 65534] | [TODO: 40%] |
| [TODO: 10.0.10.0/24] | Management | [TODO: /24] | [TODO: 254] | [TODO: 60%] |
| [TODO: 10.0.20.0/24] | Production | [TODO: /24] | [TODO: 254] | [TODO: 80%] |
| [TODO: 10.0.30.0/24] | DMZ | [TODO: /24] | [TODO: 254] | [TODO: 30%] |

**IPAM (IP Address Management):**
- **Tool:** [TODO: z.B. NetBox, phpIPAM]
- **Verantwortlich:** {{ meta-organisation-roles.role_it_operations_manager.name }}

### Firewall und Security

| Gerät | Typ | Modell | Standort | Rolle | Durchsatz |
|---|---|---|---|---|---|
| [TODO: FW-01] | Firewall | [TODO: Palo Alto] | {{ netbox.site.name }} | [TODO: Perimeter] | [TODO: 10 Gbps] |
| [TODO: FW-02] | Firewall | [TODO: Palo Alto] | {{ netbox.site.name }} | [TODO: Perimeter] | [TODO: 10 Gbps] |

**Firewall-Regeln:**
- **Anzahl Regeln:** [TODO: z.B. 500]
- **Review-Zyklus:** [TODO: z.B. Quartalsweise]
- **Verantwortlich:** {{ meta-organisation-roles.role_ciso.name }}

### Load Balancer

| Gerät | Typ | Modell | Standort | Algorithmus | Kapazität |
|---|---|---|---|---|---|
| [TODO: LB-01] | Load Balancer | [TODO: F5/HAProxy] | {{ netbox.site.name }} | [TODO: Round-Robin] | [TODO: 10k RPS] |
| [TODO: LB-02] | Load Balancer | [TODO: F5/HAProxy] | {{ netbox.site.name }} | [TODO: Round-Robin] | [TODO: 10k RPS] |

### WAN-Verbindungen

| Provider | Typ | Bandbreite | Standort | SLA | Kosten/Monat |
|---|---|---|---|---|---|
| [TODO: Provider 1] | [TODO: MPLS] | [TODO: 1 Gbps] | {{ netbox.site.name }} | [TODO: 99.9%] | [TODO: EUR] |
| [TODO: Provider 2] | [TODO: Internet] | [TODO: 500 Mbps] | {{ netbox.site.name }} | [TODO: 99.5%] | [TODO: EUR] |

## Virtualisierung

### Virtualisierungsplattform

**Hypervisor:** [TODO: z.B. VMware vSphere 8.0, Microsoft Hyper-V, KVM]

**Management:** [TODO: z.B. vCenter Server, SCVMM]

### Cluster-Konfiguration

| Cluster-Name | Hypervisor | Hosts | vCPUs | RAM (GB) | Storage (TB) | VMs |
|---|---|---:|---:|---:|---:|---:|
| {{ netbox.cluster.prod.name }} | [TODO: VMware] | [TODO: 4] | [TODO: 128] | [TODO: 1024] | [TODO: 50] | [TODO: 80] |
| {{ netbox.cluster.test.name }} | [TODO: VMware] | [TODO: 2] | [TODO: 64] | [TODO: 512] | [TODO: 20] | [TODO: 40] |

**Cluster-Features:**
- **HA (High Availability):** [TODO: Ja/Nein, Konfiguration]
- **DRS (Distributed Resource Scheduler):** [TODO: Ja/Nein, Modus]
- **vMotion/Live Migration:** [TODO: Ja/Nein]
- **Fault Tolerance:** [TODO: Ja/Nein]

### Virtuelle Maschinen

| VM-Name | Cluster | vCPU | RAM (GB) | Storage (GB) | OS | Rolle | Status |
|---|---|---:|---:|---:|---|---|---|
| {{ netbox.vm.app01.name }} | {{ netbox.cluster.prod.name }} | [TODO: 4] | [TODO: 16] | [TODO: 200] | [TODO: Ubuntu 22.04] | [TODO: App-Server] | [TODO: Running] |
| {{ netbox.vm.db01.name }} | {{ netbox.cluster.prod.name }} | [TODO: 8] | [TODO: 32] | [TODO: 500] | [TODO: RHEL 9] | [TODO: DB-Server] | [TODO: Running] |
| {{ netbox.vm.web01.name }} | {{ netbox.cluster.prod.name }} | [TODO: 2] | [TODO: 8] | [TODO: 100] | [TODO: Ubuntu 22.04] | [TODO: Web-Server] | [TODO: Running] |

**VM-Lifecycle:**
- **Provisioning:** [TODO: Automatisiert/Manuell, Tool]
- **Template-Management:** [TODO: Prozess]
- **Snapshot-Policy:** [TODO: Richtlinie]
- **Decommissioning:** [TODO: Prozess]

### Resource Pools

| Pool-Name | Cluster | CPU-Shares | RAM-Reservation | Zweck |
|---|---|---|---|---|
| [TODO: Production] | {{ netbox.cluster.prod.name }} | [TODO: High] | [TODO: 50%] | [TODO: Produktions-VMs] |
| [TODO: Development] | {{ netbox.cluster.test.name }} | [TODO: Normal] | [TODO: 25%] | [TODO: Entwicklungs-VMs] |
| [TODO: Test] | {{ netbox.cluster.test.name }} | [TODO: Low] | [TODO: 10%] | [TODO: Test-VMs] |

## Container-Orchestrierung

### Kubernetes-Cluster

**Kubernetes-Version:** [TODO: z.B. 1.28.x]

**Distribution:** [TODO: z.B. Vanilla K8s, OpenShift, Rancher, EKS, AKS, GKE]

| Cluster-Name | Umgebung | Nodes | Pods | Namespaces | Ingress |
|---|---|---:|---:|---:|---|
| [TODO: k8s-prod] | Production | [TODO: 6] | [TODO: 200] | [TODO: 20] | [TODO: Nginx] |
| [TODO: k8s-test] | Test | [TODO: 3] | [TODO: 50] | [TODO: 10] | [TODO: Nginx] |

### Node-Konfiguration

| Node-Name | Rolle | CPU | RAM (GB) | Storage (GB) | Status |
|---|---|---:|---:|---:|---|
| [TODO: k8s-master-01] | Control Plane | [TODO: 4] | [TODO: 16] | [TODO: 100] | [TODO: Ready] |
| [TODO: k8s-worker-01] | Worker | [TODO: 8] | [TODO: 32] | [TODO: 200] | [TODO: Ready] |
| [TODO: k8s-worker-02] | Worker | [TODO: 8] | [TODO: 32] | [TODO: 200] | [TODO: Ready] |

### Container-Registry

- **Registry:** [TODO: z.B. Harbor, Docker Hub, ECR, ACR, GCR]
- **URL:** [TODO: registry.example.com]
- **Authentifizierung:** [TODO: z.B. LDAP, OAuth2]
- **Scanning:** [TODO: z.B. Trivy, Clair]

### Helm-Charts

- **Chart-Repository:** [TODO: URL]
- **Anzahl Charts:** [TODO: z.B. 50]
- **Versionierung:** [TODO: Prozess]

## Cloud-Infrastruktur

### Cloud-Provider

**Primärer Cloud-Provider:** [TODO: z.B. AWS, Azure, Google Cloud]

**Cloud-Strategie:** [TODO: z.B. Cloud-First, Hybrid, Multi-Cloud]

### Cloud-Accounts

| Account-Name | Provider | Account-ID | Umgebung | Zweck | Kosten/Monat |
|---|---|---|---|---|---|
| [TODO: prod-account] | [TODO: AWS] | [TODO: 123456789012] | Production | [TODO: Produktions-Workloads] | [TODO: EUR] |
| [TODO: dev-account] | [TODO: AWS] | [TODO: 987654321098] | Development | [TODO: Entwicklung/Test] | [TODO: EUR] |

### Cloud-Regionen

| Region | Provider | Standort | Zweck | Services |
|---|---|---|---|---|
| [TODO: eu-central-1] | [TODO: AWS] | Frankfurt | [TODO: Primary] | [TODO: EC2, RDS, S3] |
| [TODO: eu-west-1] | [TODO: AWS] | Irland | [TODO: DR] | [TODO: EC2, RDS, S3] |

### Cloud-Ressourcen

#### Compute (IaaS)

| Ressource | Typ | Größe | Anzahl | Region | Zweck | Kosten/Monat |
|---|---|---|---:|---|---|---|
| [TODO: EC2 Instances] | [TODO: t3.large] | [TODO: 2vCPU/8GB] | [TODO: 10] | [TODO: eu-central-1] | [TODO: App-Server] | [TODO: EUR] |
| [TODO: Lambda Functions] | [TODO: Serverless] | [TODO: -] | [TODO: 50] | [TODO: eu-central-1] | [TODO: Microservices] | [TODO: EUR] |

#### Storage

| Ressource | Typ | Größe (TB) | Region | Zweck | Kosten/Monat |
|---|---|---:|---|---|---|
| [TODO: S3 Buckets] | [TODO: Object Storage] | [TODO: 10] | [TODO: eu-central-1] | [TODO: Backups] | [TODO: EUR] |
| [TODO: EBS Volumes] | [TODO: Block Storage] | [TODO: 5] | [TODO: eu-central-1] | [TODO: VM-Storage] | [TODO: EUR] |

#### Database (PaaS)

| Ressource | Typ | Größe | Region | Zweck | Kosten/Monat |
|---|---|---|---|---|---|
| [TODO: RDS PostgreSQL] | [TODO: db.r5.large] | [TODO: 500GB] | [TODO: eu-central-1] | [TODO: Produktions-DB] | [TODO: EUR] |
| [TODO: DynamoDB] | [TODO: NoSQL] | [TODO: On-Demand] | [TODO: eu-central-1] | [TODO: Session-Store] | [TODO: EUR] |

#### Networking

| Ressource | Typ | Konfiguration | Region | Zweck |
|---|---|---|---|---|
| [TODO: VPC] | [TODO: Virtual Network] | [TODO: 10.0.0.0/16] | [TODO: eu-central-1] | [TODO: Netzwerk-Isolation] |
| [TODO: VPN Gateway] | [TODO: Site-to-Site VPN] | [TODO: 1 Gbps] | [TODO: eu-central-1] | [TODO: Hybrid-Connectivity] |
| [TODO: Direct Connect] | [TODO: Dedicated Line] | [TODO: 10 Gbps] | [TODO: eu-central-1] | [TODO: Low-Latency] |

### Cloud-Kosten

**Gesamtkosten/Monat:** [TODO: EUR]

**Kostenoptimierung:**
- **Reserved Instances:** [TODO: Prozentsatz]
- **Spot Instances:** [TODO: Prozentsatz]
- **Auto-Scaling:** [TODO: Ja/Nein]
- **Cost-Monitoring:** [TODO: Tool]

## Storage-Infrastruktur

### Storage-Systeme

| System | Typ | Kapazität (TB) | Nutzung (%) | Protokoll | Standort | Zweck |
|---|---|---:|---:|---|---|---|
| [TODO: SAN-01] | SAN | [TODO: 100] | [TODO: 70%] | [TODO: FC/iSCSI] | {{ netbox.site.name }} | [TODO: VM-Storage] |
| [TODO: NAS-01] | NAS | [TODO: 50] | [TODO: 60%] | [TODO: NFS/CIFS] | {{ netbox.site.name }} | [TODO: File-Shares] |
| [TODO: OBJ-01] | Object Storage | [TODO: 200] | [TODO: 40%] | [TODO: S3] | [TODO: Cloud] | [TODO: Backups] |

### Storage-Tiers

| Tier | Typ | Performance | Kapazität (TB) | Kosten/TB | Verwendung |
|---|---|---|---:|---|---|
| **Tier 0** | [TODO: NVMe SSD] | [TODO: >100k IOPS] | [TODO: 10] | [TODO: Hoch] | [TODO: Datenbanken] |
| **Tier 1** | [TODO: SAS SSD] | [TODO: 50k IOPS] | [TODO: 50] | [TODO: Mittel] | [TODO: VMs] |
| **Tier 2** | [TODO: SAS HDD] | [TODO: 5k IOPS] | [TODO: 100] | [TODO: Niedrig] | [TODO: Archive] |

### Storage-Netzwerk

**SAN-Fabric:**
- **Protokoll:** [TODO: z.B. Fibre Channel 32G, iSCSI 10G]
- **Switches:** [TODO: z.B. Brocade, Cisco MDS]
- **Redundanz:** [TODO: z.B. Dual-Fabric]

**NAS-Netzwerk:**
- **Protokoll:** [TODO: z.B. NFS v4, SMB 3.0]
- **Netzwerk:** [TODO: z.B. Dediziertes 10G-Netzwerk]

### Backup-Storage

| System | Typ | Kapazität (TB) | Retention | Standort | Zweck |
|---|---|---:|---|---|---|
| [TODO: BACKUP-01] | [TODO: Disk] | [TODO: 100] | [TODO: 30 Tage] | {{ netbox.site.name }} | [TODO: Disk-Backup] |
| [TODO: TAPE-01] | [TODO: Tape Library] | [TODO: 500] | [TODO: 7 Jahre] | {{ netbox.site.name }} | [TODO: Langzeit-Archiv] |
| [TODO: CLOUD-BACKUP] | [TODO: Cloud] | [TODO: Unlimited] | [TODO: 90 Tage] | [TODO: Cloud] | [TODO: Off-Site-Backup] |

## Stromversorgung

### Primäre Stromversorgung

- **Anschlussleistung:** [TODO: z.B. 200 kW]
- **Redundanz:** [TODO: z.B. N+1, 2N]
- **Provider:** [TODO: Energieversorger]

### USV (Unterbrechungsfreie Stromversorgung)

| USV-System | Kapazität (kVA) | Laufzeit (min) | Standort | Status |
|---|---:|---:|---|---|
| [TODO: USV-01] | [TODO: 100] | [TODO: 15] | {{ netbox.site.name }} | [TODO: Online] |
| [TODO: USV-02] | [TODO: 100] | [TODO: 15] | {{ netbox.site.name }} | [TODO: Online] |

**USV-Wartung:**
- **Wartungsintervall:** [TODO: z.B. Quartalsweise]
- **Batterietest:** [TODO: z.B. Monatlich]
- **Verantwortlich:** [TODO: Facility-Management]

### Notstromversorgung

- **Notstromaggregat:** [TODO: z.B. 250 kVA Diesel]
- **Kraftstoffvorrat:** [TODO: z.B. 1000 Liter]
- **Laufzeit:** [TODO: z.B. 48 Stunden]
- **Umschaltzeit:** [TODO: z.B. < 10 Sekunden]

## Kühlung und Klimatisierung

### Klimatisierung

- **Kühlleistung:** [TODO: z.B. 150 kW]
- **Redundanz:** [TODO: z.B. N+1]
- **Zieltemperatur:** [TODO: z.B. 22°C ±2°C]
- **Luftfeuchtigkeit:** [TODO: z.B. 45% ±5%]

### Monitoring

- **Temperatur-Sensoren:** [TODO: Anzahl und Positionen]
- **Luftfeuchtigkeits-Sensoren:** [TODO: Anzahl und Positionen]
- **Alarme:** [TODO: Schwellwerte und Eskalation]

## Physische Sicherheit

### Zutrittskontrolle

- **System:** [TODO: z.B. Biometrisch, Chipkarte]
- **Zutrittsberechtigte:** [TODO: Anzahl Personen]
- **Protokollierung:** [TODO: Aufbewahrungsdauer]
- **Vier-Augen-Prinzip:** [TODO: Ja/Nein, für welche Bereiche]

### Videoüberwachung

- **Kameras:** [TODO: Anzahl und Positionen]
- **Aufzeichnung:** [TODO: Aufbewahrungsdauer]
- **Überwachung:** [TODO: 24/7 oder zeitgesteuert]

### Brandschutz

- **Brandmeldeanlage:** [TODO: Typ]
- **Löschanlage:** [TODO: z.B. Gaslöschanlage, Sprinkler]
- **Brandabschnitte:** [TODO: Anzahl]
- **Fluchtwege:** [TODO: Anzahl und Kennzeichnung]

## Kapazitätsplanung

### Aktuelle Auslastung

| Ressource | Kapazität | Genutzt | Verfügbar | Auslastung (%) | Schwellwert (%) |
|---|---|---|---|---:|---:|
| **CPU (Cores)** | [TODO: 500] | [TODO: 300] | [TODO: 200] | [TODO: 60%] | [TODO: 80%] |
| **RAM (GB)** | [TODO: 4000] | [TODO: 2800] | [TODO: 1200] | [TODO: 70%] | [TODO: 85%] |
| **Storage (TB)** | [TODO: 200] | [TODO: 140] | [TODO: 60] | [TODO: 70%] | [TODO: 80%] |
| **Netzwerk (Gbps)** | [TODO: 100] | [TODO: 40] | [TODO: 60] | [TODO: 40%] | [TODO: 70%] |

### Wachstumsprognose

**Prognosezeitraum:** [TODO: z.B. 12 Monate]

| Ressource | Aktuell | Prognose (+12M) | Wachstum (%) | Maßnahmen |
|---|---|---|---:|---|
| **CPU** | [TODO: 300 Cores] | [TODO: 360 Cores] | [TODO: +20%] | [TODO: Beschreibung] |
| **RAM** | [TODO: 2800 GB] | [TODO: 3360 GB] | [TODO: +20%] | [TODO: Beschreibung] |
| **Storage** | [TODO: 140 TB] | [TODO: 182 TB] | [TODO: +30%] | [TODO: Beschreibung] |

### Skalierungsstrategien

**Vertikale Skalierung:**
- [TODO: Beschreibung der Strategie]
- [TODO: Maximale Grenzen]

**Horizontale Skalierung:**
- [TODO: Beschreibung der Strategie]
- [TODO: Auto-Scaling-Konfiguration]

**Cloud-Bursting:**
- [TODO: Ja/Nein, Beschreibung]

## Lifecycle-Management

### Hardware-Lifecycle

| Phase | Dauer | Aktivitäten | Verantwortlich |
|---|---|---|---|
| **Beschaffung** | [TODO: 4-8 Wochen] | [TODO: Anforderung, Bestellung, Lieferung] | {{ meta-organisation-roles.role_it_operations_manager.name }} |
| **Inbetriebnahme** | [TODO: 1-2 Wochen] | [TODO: Installation, Konfiguration, Tests] | [TODO: Team] |
| **Betrieb** | [TODO: 5 Jahre] | [TODO: Monitoring, Wartung, Support] | [TODO: Team] |
| **Refresh** | [TODO: 1-2 Wochen] | [TODO: Migration, Austausch] | [TODO: Team] |
| **Entsorgung** | [TODO: 1 Woche] | [TODO: Datenlöschung, Recycling] | [TODO: Team] |

### Software-Lifecycle

| Phase | Dauer | Aktivitäten | Verantwortlich |
|---|---|---|---|
| **Evaluation** | [TODO: 2-4 Wochen] | [TODO: Anforderungsanalyse, PoC] | [TODO: Team] |
| **Beschaffung** | [TODO: 2-4 Wochen] | [TODO: Lizenzierung, Verträge] | [TODO: Team] |
| **Implementierung** | [TODO: 4-8 Wochen] | [TODO: Installation, Konfiguration] | [TODO: Team] |
| **Betrieb** | [TODO: 3-5 Jahre] | [TODO: Support, Updates] | [TODO: Team] |
| **Ablösung** | [TODO: 8-12 Wochen] | [TODO: Migration, Decommissioning] | [TODO: Team] |

### End-of-Life-Management

**Hardware:**
- **Datenlöschung:** [TODO: Prozess, z.B. DoD 5220.22-M]
- **Zertifikat:** [TODO: Ja/Nein]
- **Recycling:** [TODO: Zertifizierter Partner]

**Software:**
- **Lizenz-Rückgabe:** [TODO: Prozess]
- **Datenexport:** [TODO: Prozess]
- **Dokumentation:** [TODO: Archivierung]

## Compliance und Zertifizierungen

### Rechenzentrum-Zertifizierungen

- **ISO 27001:** [TODO: Ja/Nein, Gültig bis]
- **ISO 9001:** [TODO: Ja/Nein, Gültig bis]
- **Tier-Zertifizierung:** [TODO: Tier I/II/III/IV]
- **PCI-DSS:** [TODO: Ja/Nein, Level]

### Compliance-Anforderungen

- **DSGVO:** [TODO: Maßnahmen]
- **BSI Grundschutz:** [TODO: Ja/Nein, Baustein]
- **KRITIS:** [TODO: Ja/Nein, Sektor]

## Verantwortlichkeiten

| Rolle | Verantwortung | Person | Kontakt |
|---|---|---|---|
| **Infrastructure Manager** | Gesamtverantwortung Infrastruktur | {{ meta-organisation-roles.role_it_operations_manager.name }} | {{ meta-organisation-roles.role_it_operations_manager.email }} |
| **Network Administrator** | Netzwerkinfrastruktur | [TODO: Name] | [TODO: E-Mail] |
| **Storage Administrator** | Storage-Systeme | [TODO: Name] | [TODO: E-Mail] |
| **Virtualization Admin** | Virtualisierung | [TODO: Name] | [TODO: E-Mail] |
| **Cloud Architect** | Cloud-Infrastruktur | [TODO: Name] | [TODO: E-Mail] |
| **Facility Manager** | Physische Infrastruktur | [TODO: Name] | [TODO: E-Mail] |

## Kontakte

**Bei Fragen zur Infrastruktur:**
- **IT Operations Manager:** {{ meta-organisation-roles.role_it_operations_manager.name }} ({{ meta-organisation-roles.role_it_operations_manager.email }})
- **CIO:** {{ meta-organisation-roles.role_cio.name }} ({{ meta-organisation-roles.role_cio.email }})

**Notfallkontakte:**
- **Rechenzentrum:** [TODO: Telefon 24/7]
- **Stromversorger:** [TODO: Telefon]
- **Facility Management:** [TODO: Telefon]

**Dokumentverantwortlicher:** {{ meta-handbook.owner }}  
**Genehmigt durch:** {{ meta-handbook.approver }}  
**Version:** {{ meta-handbook.revision }}  
**Organisation:** {{ meta-organisation.name }}

