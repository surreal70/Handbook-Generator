# Design Document: Compliance Framework Templates

## Overview

This design document specifies the architecture and implementation approach for expanding the handbook generator system with seven new compliance framework template sets: PCI-DSS, HIPAA, NIST 800-53, TSC (SOC 2), Common Criteria (ISO/IEC 15408), ISO 9001, and GDPR.

The expansion builds upon the existing template architecture that successfully supports five handbook types (BCM, ISMS, BSI Grundschutz, IT-Operations, CIS Controls) with 240 templates. The new frameworks will follow established patterns for template structure, numbering, bilingual support, placeholder substitution, and integration with the Template_Manager, Validation_System, and Output_Generator components.

### Design Goals

1. **Consistency**: Maintain structural consistency with existing template sets
2. **Completeness**: Provide comprehensive coverage of each framework's requirements
3. **Usability**: Enable easy customization and organization-specific adaptation
4. **Integration**: Seamless integration with existing handbook generator components
5. **Quality**: Ensure high-quality, auditable documentation templates
6. **Bilingual**: Support both German and English with identical structure

### Key Design Decisions

- **Template Numbering**: Use 10-increment numbering (0010, 0020, 0030) to allow future insertions
- **Framework Organization**: Group templates by logical framework sections with number ranges
- **Bilingual Approach**: Parallel directory structure (templates/de/ and templates/en/) with identical file names
- **Placeholder Strategy**: Leverage existing {{ source.field }} syntax for organization-specific data
- **Documentation**: Include README.md and FRAMEWORK_MAPPING.md for each template set
- **Validation**: Extend existing validation system to cover new frameworks

## Architecture

### Component Overview

The compliance framework templates expansion integrates with the existing handbook generator architecture:

```
┌─────────────────────────────────────────────────────────────┐
│                    Handbook Generator System                 │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐  │
│  │   CLI        │───▶│  Template    │───▶│  Placeholder │  │
│  │   Interface  │    │  Manager     │    │  Processor   │  │
│  └──────────────┘    └──────────────┘    └──────────────┘  │
│         │                    │                    │          │
│         │                    ▼                    ▼          │
│         │            ┌──────────────┐    ┌──────────────┐  │
│         │            │  Validation  │    │  Data Source │  │
│         │            │  System      │    │  Adapter     │  │
│         │            └──────────────┘    └──────────────┘  │
│         │                                                    │
│         ▼                                                    │
│  ┌──────────────┐                                           │
│  │  Output      │                                           │
│  │  Generator   │                                           │
│  └──────────────┘                                           │
│         │                                                    │
│         ▼                                                    │
│  ┌──────────────────────────────────────────────────┐      │
│  │  Output Formats                                   │      │
│  │  • HTML (mini-website with navigation)           │      │
│  │  • PDF (with TOC and page breaks)                │      │
│  │  • Markdown (combined or separate files)         │      │
│  └──────────────────────────────────────────────────┘      │
│                                                               │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                    Template Storage                          │
├─────────────────────────────────────────────────────────────┤
│  templates/                                                  │
│  ├── de/                                                     │
│  │   ├── bcm/              (existing)                       │
│  │   ├── isms/             (existing)                       │
│  │   ├── bsi-grundschutz/  (existing)                       │
│  │   ├── it-operation/     (existing)                       │
│  │   ├── cis-controls/     (existing)                       │
│  │   ├── pci-dss/          (new)                            │
│  │   ├── hipaa/            (new)                            │
│  │   ├── nist-800-53/      (new)                            │
│  │   ├── tsc/              (new)                            │
│  │   ├── common-criteria/  (new)                            │
│  │   ├── iso-9001/         (new)                            │
│  │   └── gdpr/             (new)                            │
│  └── en/                                                     │
│      └── (same structure as de/)                            │
└─────────────────────────────────────────────────────────────┘
```

### Integration Points

1. **CLI Extension**: Add new framework names to CLI argument validation
2. **Template Manager**: Automatic discovery of new framework directories
3. **Validation System**: Extend validation rules to cover new frameworks
4. **Output Generator**: Apply existing HTML/PDF/Markdown generation to new frameworks
5. **Placeholder System**: Reuse existing placeholder processing for new templates

## Components and Interfaces

### Template Structure Component

Each compliance framework template set follows a standardized structure:

#### File Naming Convention
```
NNNN_descriptive_name.md
```
- `NNNN`: 4-digit number (0010, 0020, 0030, ...)
- `descriptive_name`: Kebab-case or underscore-separated description
- `.md`: Markdown file extension

#### Template Header Format
```markdown
# Template Title

**Dokument-ID:** NNNN  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** Entwurf / In Review / Freigegeben  
**Klassifizierung:** Intern / Vertraulich / Streng vertraulich  
**Letzte Aktualisierung:** {{ meta.date }}  

---

> **Hinweis:** Dieses Dokument ist ein Template. Ersetze alle `[TODO]`-Platzhalter.

## Section 1
Content...

## Section 2
Content...
```

#### Special Files

1. **Metadata Template** (`0000_metadata_{lang}_{framework}.md`)
   - Contains handbook metadata (author, version, date)
   - Rendered as first page
   - Language-specific naming

2. **README.md**
   - Template set overview
   - Numbering scheme explanation
   - Usage guidance
   - Framework compliance mapping reference

3. **FRAMEWORK_MAPPING.md**
   - Maps templates to framework requirements
   - Identifies coverage gaps
   - Provides audit trail

### Framework-Specific Template Structures

#### 1. PCI-DSS Template Structure

**Number Range**: 0010-0500  
**Total Templates**: ~40-50

**Organization**:
- **0010-0050**: Foundation (Scope, CDE Definition, Network Segmentation, Roles)
- **0100-0150**: Build and Maintain Secure Network (Requirements 1-2)
- **0200-0250**: Protect Cardholder Data (Requirements 3-4)
- **0300-0350**: Maintain Vulnerability Management (Requirements 5-6)
- **0400-0450**: Implement Strong Access Control (Requirements 7-9)
- **0500-0550**: Monitor and Test Networks (Requirements 10-11)
- **0600-0650**: Maintain Information Security Policy (Requirement 12)
- **0700-0750**: Appendices (Evidence, Checklists, Audit Logs)

**Key Templates**:
- CDE Scope and Data Flow Mapping
- Network Segmentation Documentation
- Encryption Key Management
- Access Control Matrix
- Logging and Monitoring Standards
- Incident Response Procedures
- Vendor Management
- Quarterly Scan Reports
- Penetration Testing Documentation

#### 2. HIPAA Template Structure

**Number Range**: 0010-0500  
**Total Templates**: ~35-45

**Organization**:
- **0010-0050**: Foundation (Scope, Covered Entities, Business Associates, Roles)
- **0100-0200**: Administrative Safeguards (Security Management, Workforce Security, Information Access, Security Awareness, Contingency Planning)
- **0300-0350**: Physical Safeguards (Facility Access, Workstation Security, Device Controls)
- **0400-0450**: Technical Safeguards (Access Control, Audit Controls, Integrity, Transmission Security)
- **0500-0550**: Privacy Rule (Notice of Privacy Practices, Data Subject Rights, Minimum Necessary)
- **0600-0650**: Breach Notification and Incident Response
- **0700-0750**: Appendices (Risk Analysis, BAA Templates, Evidence)

**Key Templates**:
- Risk Analysis and Risk Management Plan
- Workforce Security Policies
- Access Management Procedures
- Audit Controls and Logging
- Encryption and Transmission Security
- Breach Notification Procedures
- Business Associate Agreements
- Training and Awareness Program
- Contingency and Disaster Recovery Plans

#### 3. NIST 800-53 Template Structure

**Number Range**: 0010-0700  
**Total Templates**: ~60-70

**Organization**:
- **0010-0050**: Foundation (System Categorization, Scope, Roles, RMF Process)
- **0100-0150**: Access Control (AC Family)
- **0200-0250**: Awareness and Training (AT), Audit and Accountability (AU)
- **0300-0350**: Configuration Management (CM), Contingency Planning (CP)
- **0400-0450**: Identification and Authentication (IA), Incident Response (IR)
- **0500-0550**: Maintenance (MA), Media Protection (MP), Physical Protection (PE)
- **0600-0650**: Planning (PL), Risk Assessment (RA), System Acquisition (SA)
- **0700-0750**: System Protection (SC), System Integrity (SI), Supply Chain (SR)
- **0800-0850**: Appendices (Control Mapping, Assessment Procedures, POA&M)

**Key Templates**:
- System Security Plan (SSP)
- Control Implementation Statements
- Assessment and Authorization Package
- Continuous Monitoring Strategy
- Plan of Action and Milestones (POA&M)
- Security Assessment Report (SAR)
- Control Traceability Matrix
- Privacy Impact Assessment
- Supply Chain Risk Management Plan

#### 4. TSC (SOC 2) Template Structure

**Number Range**: 0010-0450  
**Total Templates**: ~35-40

**Organization**:
- **0010-0050**: Foundation (System Description, Boundaries, Components, Roles)
- **0100-0150**: Common Criteria (Security - Required for all SOC 2)
- **0200-0230**: Availability Criteria (Optional)
- **0240-0270**: Processing Integrity Criteria (Optional)
- **0280-0310**: Confidentiality Criteria (Optional)
- **0320-0350**: Privacy Criteria (Optional)
- **0400-0450**: Appendices (Control Matrix, Evidence, Test Results)

**Key Templates**:
- System Description
- Control Environment Documentation
- Risk Assessment Process
- Logical and Physical Access Controls
- System Operations and Monitoring
- Change Management Procedures
- Data Backup and Recovery
- Incident Response Procedures
- Vendor Management
- Availability Commitments
- Processing Integrity Controls
- Confidentiality Agreements
- Privacy Notice and Consent

#### 5. Common Criteria Template Structure

**Number Range**: 0010-0500  
**Total Templates**: ~30-35

**Organization**:
- **0010-0050**: Security Target Introduction (ST Introduction, TOE Overview, Conformance Claims)
- **0100-0150**: TOE Description (Physical Scope, Logical Scope, Interfaces)
- **0200-0250**: Security Problem Definition (Threats, OSPs, Assumptions)
- **0300-0350**: Security Objectives (TOE Objectives, Environment Objectives)
- **0400-0450**: Security Requirements (SFRs, SARs, EAL Selection)
- **0500-0550**: TOE Summary Specification (Security Functions, Assurance Measures)
- **0600-0650**: Appendices (PP Conformance, Rationale, Glossary)

**Key Templates**:
- Security Target Document
- TOE Description and Boundaries
- Threat Analysis
- Security Functional Requirements (SFR)
- Security Assurance Requirements (SAR)
- Evaluation Assurance Level (EAL) Justification
- Protection Profile Conformance
- Security Functions Specification
- Assurance Measures Documentation
- Evaluation Evidence

#### 6. ISO 9001 Template Structure

**Number Range**: 0010-0500  
**Total Templates**: ~35-40

**Organization**:
- **0010-0050**: Context of Organization (Clause 4)
- **0100-0150**: Leadership (Clause 5)
- **0200-0250**: Planning (Clause 6)
- **0300-0350**: Support (Clause 7)
- **0400-0500**: Operation (Clause 8)
- **0550-0600**: Performance Evaluation (Clause 9)
- **0650-0700**: Improvement (Clause 10)
- **0750-0800**: Appendices (Process Maps, Forms, Records)

**Key Templates**:
- Quality Policy
- Context Analysis (Internal/External Issues)
- Interested Parties Analysis
- Scope of QMS
- Quality Objectives
- Risk and Opportunity Assessment
- Competence and Training Matrix
- Documented Information Control
- Operational Planning and Control
- Design and Development Process
- Production and Service Provision
- Release of Products and Services
- Control of Nonconforming Outputs
- Monitoring and Measurement
- Internal Audit Program
- Management Review
- Nonconformity and Corrective Action
- Continual Improvement Process

#### 7. GDPR Template Structure

**Number Range**: 0010-0600  
**Total Templates**: ~45-55

**Organization**:
- **0010-0050**: Foundation (Scope, Roles, Principles, Legal Basis)
- **0100-0150**: Data Protection Principles (Articles 5-11)
- **0200-0250**: Data Subject Rights (Articles 12-23)
- **0300-0350**: Controller and Processor Obligations (Articles 24-39)
- **0400-0450**: Data Protection Impact Assessment (Articles 35-36)
- **0500-0550**: Data Transfers and International Processing (Articles 44-50)
- **0600-0650**: Data Breach and Incident Management (Articles 33-34)
- **0700-0750**: Appendices (Article 30 Records, DPIA Templates, DPA Templates)

**Key Templates**:
- Data Protection Policy
- Legal Basis Assessment
- Records of Processing Activities (Article 30)
- Data Protection Impact Assessment (DPIA)
- Data Subject Rights Procedures
- Consent Management
- Data Retention and Deletion Schedule
- Data Breach Response Plan
- Data Transfer Mechanisms
- Processor Agreements (DPA)
- Privacy by Design and Default
- Data Protection Officer (DPO) Role
- Legitimate Interest Assessment (LIA)
- Privacy Notices
- Data Mapping and Flow Diagrams

### Template Manager Extension

The Template_Manager component requires minimal changes to support new frameworks:

```python
class TemplateManager:
    """Manages template loading, validation, and organization."""
    
    SUPPORTED_FRAMEWORKS = [
        'bcm',
        'isms',
        'bsi-grundschutz',
        'it-operation',
        'cis-controls',
        'pci-dss',           # NEW
        'hipaa',             # NEW
        'nist-800-53',       # NEW
        'tsc',               # NEW
        'common-criteria',   # NEW
        'iso-9001',          # NEW
        'gdpr'               # NEW
    ]
    
    def load_templates(self, language: str, framework: str) -> List[Template]:
        """
        Load templates for specified language and framework.
        
        Args:
            language: 'de' or 'en'
            framework: One of SUPPORTED_FRAMEWORKS
            
        Returns:
            List of Template objects sorted by numeric prefix
            
        Raises:
            ValueError: If framework not supported
            FileNotFoundError: If template directory doesn't exist
        """
        if framework not in self.SUPPORTED_FRAMEWORKS:
            raise ValueError(f"Unsupported framework: {framework}")
            
        template_dir = Path(f"templates/{language}/{framework}")
        if not template_dir.exists():
            raise FileNotFoundError(f"Template directory not found: {template_dir}")
            
        templates = []
        for file_path in sorted(template_dir.glob("*.md")):
            if file_path.name.startswith("0000_"):
                # Metadata template - handle separately
                continue
            if file_path.name == "README.md":
                # Skip README
                continue
                
            template = self._parse_template(file_path)
            templates.append(template)
            
        return sorted(templates, key=lambda t: t.number)
    
    def _parse_template(self, file_path: Path) -> Template:
        """Parse template file and extract metadata."""
        # Extract number from filename (e.g., "0010" from "0010_Title.md")
        number = int(file_path.name[:4])
        
        # Read content
        content = file_path.read_text(encoding='utf-8')
        
        # Extract title (first H1 heading)
        title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else file_path.stem
        
        return Template(
            number=number,
            title=title,
            file_path=file_path,
            content=content
        )
```

### Validation System Extension

The Validation_System extends to validate new framework templates:

```python
class TemplateValidator:
    """Validates template structure and content."""
    
    def validate_framework(self, language: str, framework: str) -> ValidationReport:
        """
        Validate all templates in a framework.
        
        Checks:
        - File naming convention (NNNN_name.md)
        - Unique template numbers
        - Metadata template exists
        - README.md exists
        - Placeholder syntax
        - Bilingual consistency (if both languages present)
        
        Returns:
            ValidationReport with errors and warnings
        """
        report = ValidationReport(framework=framework, language=language)
        
        template_dir = Path(f"templates/{language}/{framework}")
        
        # Check directory exists
        if not template_dir.exists():
            report.add_error(f"Template directory not found: {template_dir}")
            return report
            
        # Check README exists
        if not (template_dir / "README.md").exists():
            report.add_warning("README.md not found")
            
        # Check metadata template exists
        metadata_pattern = f"0000_metadata_{language}_{framework}.md"
        if not (template_dir / metadata_pattern).exists():
            report.add_error(f"Metadata template not found: {metadata_pattern}")
            
        # Validate each template file
        template_numbers = set()
        for file_path in template_dir.glob("*.md"):
            if file_path.name == "README.md":
                continue
                
            # Validate filename format
            if not re.match(r'^\d{4}_[\w-]+\.md$', file_path.name):
                report.add_error(f"Invalid filename format: {file_path.name}")
                continue
                
            # Check for duplicate numbers
            number = int(file_path.name[:4])
            if number in template_numbers:
                report.add_error(f"Duplicate template number: {number}")
            template_numbers.add(number)
            
            # Validate template content
            self._validate_template_content(file_path, report)
            
        # Check bilingual consistency
        if language == 'de':
            self._check_bilingual_consistency(framework, report)
            
        return report
    
    def _validate_template_content(self, file_path: Path, report: ValidationReport):
        """Validate individual template content."""
        content = file_path.read_text(encoding='utf-8')
        
        # Check for required header fields
        required_fields = ['Dokument-ID', 'Owner', 'Version', 'Status']
        for field in required_fields:
            if f"**{field}:**" not in content:
                report.add_warning(f"{file_path.name}: Missing header field '{field}'")
                
        # Validate placeholder syntax
        placeholders = re.findall(r'\{\{[^}]+\}\}', content)
        for placeholder in placeholders:
            if not re.match(r'\{\{\s*[\w.]+\s*\}\}', placeholder):
                report.add_error(f"{file_path.name}: Invalid placeholder syntax: {placeholder}")
    
    def _check_bilingual_consistency(self, framework: str, report: ValidationReport):
        """Check that German and English templates match in structure."""
        de_dir = Path(f"templates/de/{framework}")
        en_dir = Path(f"templates/en/{framework}")
        
        if not en_dir.exists():
            report.add_warning("English templates not found")
            return
            
        de_files = {f.name for f in de_dir.glob("*.md") if f.name != "README.md"}
        en_files = {f.name for f in en_dir.glob("*.md") if f.name != "README.md"}
        
        # Check for missing translations
        missing_en = de_files - en_files
        missing_de = en_files - de_files
        
        if missing_en:
            report.add_warning(f"Missing English translations: {missing_en}")
        if missing_de:
            report.add_warning(f"Missing German translations: {missing_de}")
```

### CLI Extension

The CLI component adds new framework options:

```python
def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description='Handbook Generator')
    
    parser.add_argument(
        '--language', '-l',
        choices=['de', 'en'],
        required=True,
        help='Language for handbook generation'
    )
    
    parser.add_argument(
        '--template', '-t',
        choices=[
            'bcm',
            'isms',
            'bsi-grundschutz',
            'it-operation',
            'cis-controls',
            'pci-dss',           # NEW
            'hipaa',             # NEW
            'nist-800-53',       # NEW
            'tsc',               # NEW
            'common-criteria',   # NEW
            'iso-9001',          # NEW
            'gdpr'               # NEW
        ],
        required=True,
        help='Handbook type to generate'
    )
    
    parser.add_argument(
        '--output', '-o',
        choices=['markdown', 'pdf', 'html', 'both', 'all'],
        default='both',
        help='Output format'
    )
    
    # ... rest of CLI implementation
```

## Data Models

### Template Data Model

```python
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Dict, Any

@dataclass
class Template:
    """Represents a single template file."""
    number: int                    # Template number (e.g., 10, 20, 30)
    title: str                     # Template title
    file_path: Path                # Path to template file
    content: str                   # Raw template content
    metadata: Dict[str, Any]       # Extracted metadata from header
    
    def __lt__(self, other):
        """Enable sorting by template number."""
        return self.number < other.number


@dataclass
class FrameworkConfig:
    """Configuration for a compliance framework."""
    name: str                      # Framework identifier (e.g., 'pci-dss')
    display_name: str              # Human-readable name (e.g., 'PCI-DSS')
    description: str               # Framework description
    template_count: int            # Expected number of templates
    number_ranges: Dict[str, str]  # Number ranges and their purposes
    
    # Example:
    # number_ranges = {
    #     '0010-0050': 'Foundation',
    #     '0100-0150': 'Build Secure Network',
    #     '0200-0250': 'Protect Cardholder Data'
    # }


@dataclass
class ValidationReport:
    """Results of template validation."""
    framework: str
    language: str
    errors: List[str]
    warnings: List[str]
    template_count: int
    validated_at: datetime
    
    def add_error(self, message: str):
        """Add validation error."""
        self.errors.append(message)
    
    def add_warning(self, message: str):
        """Add validation warning."""
        self.warnings.append(message)
    
    def is_valid(self) -> bool:
        """Check if validation passed (no errors)."""
        return len(self.errors) == 0
    
    def summary(self) -> str:
        """Generate validation summary."""
        status = "PASSED" if self.is_valid() else "FAILED"
        return f"""
Validation Report: {self.framework} ({self.language})
Status: {status}
Templates: {self.template_count}
Errors: {len(self.errors)}
Warnings: {len(self.warnings)}
"""


@dataclass
class HandbookMetadata:
    """Metadata for generated handbook."""
    framework: str
    language: str
    author: str
    version: str
    date: str
    organization: str
    
    @classmethod
    def from_config(cls, framework: str, language: str, config: Dict[str, Any]):
        """Create metadata from configuration."""
        return cls(
            framework=framework,
            language=language,
            author=config.get('author', '[TODO]'),
            version=config.get('version', '1.0.0'),
            date=datetime.now().strftime('%Y-%m-%d'),
            organization=config.get('organization', '[TODO]')
        )
```

### Framework Registry

```python
# Framework registry with configuration for each compliance framework
FRAMEWORK_REGISTRY = {
    'pci-dss': FrameworkConfig(
        name='pci-dss',
        display_name='PCI-DSS',
        description='Payment Card Industry Data Security Standard',
        template_count=45,
        number_ranges={
            '0010-0050': 'Foundation',
            '0100-0150': 'Build and Maintain Secure Network',
            '0200-0250': 'Protect Cardholder Data',
            '0300-0350': 'Maintain Vulnerability Management',
            '0400-0450': 'Implement Strong Access Control',
            '0500-0550': 'Monitor and Test Networks',
            '0600-0650': 'Maintain Information Security Policy',
            '0700-0750': 'Appendices'
        }
    ),
    'hipaa': FrameworkConfig(
        name='hipaa',
        display_name='HIPAA',
        description='Health Insurance Portability and Accountability Act',
        template_count=40,
        number_ranges={
            '0010-0050': 'Foundation',
            '0100-0200': 'Administrative Safeguards',
            '0300-0350': 'Physical Safeguards',
            '0400-0450': 'Technical Safeguards',
            '0500-0550': 'Privacy Rule',
            '0600-0650': 'Breach Notification',
            '0700-0750': 'Appendices'
        }
    ),
    'nist-800-53': FrameworkConfig(
        name='nist-800-53',
        display_name='NIST 800-53',
        description='Security and Privacy Controls for Information Systems',
        template_count=65,
        number_ranges={
            '0010-0050': 'Foundation',
            '0100-0150': 'Access Control',
            '0200-0250': 'Awareness, Training, Audit',
            '0300-0350': 'Configuration, Contingency',
            '0400-0450': 'Identification, Incident Response',
            '0500-0550': 'Maintenance, Media, Physical',
            '0600-0650': 'Planning, Risk, Acquisition',
            '0700-0750': 'System Protection, Integrity',
            '0800-0850': 'Appendices'
        }
    ),
    'tsc': FrameworkConfig(
        name='tsc',
        display_name='TSC (SOC 2)',
        description='Trust Services Criteria for SOC 2',
        template_count=38,
        number_ranges={
            '0010-0050': 'Foundation',
            '0100-0150': 'Common Criteria (Security)',
            '0200-0230': 'Availability',
            '0240-0270': 'Processing Integrity',
            '0280-0310': 'Confidentiality',
            '0320-0350': 'Privacy',
            '0400-0450': 'Appendices'
        }
    ),
    'common-criteria': FrameworkConfig(
        name='common-criteria',
        display_name='Common Criteria',
        description='ISO/IEC 15408 Security Evaluation',
        template_count=32,
        number_ranges={
            '0010-0050': 'Security Target Introduction',
            '0100-0150': 'TOE Description',
            '0200-0250': 'Security Problem Definition',
            '0300-0350': 'Security Objectives',
            '0400-0450': 'Security Requirements',
            '0500-0550': 'TOE Summary Specification',
            '0600-0650': 'Appendices'
        }
    ),
    'iso-9001': FrameworkConfig(
        name='iso-9001',
        display_name='ISO 9001',
        description='Quality Management System',
        template_count=38,
        number_ranges={
            '0010-0050': 'Context of Organization',
            '0100-0150': 'Leadership',
            '0200-0250': 'Planning',
            '0300-0350': 'Support',
            '0400-0500': 'Operation',
            '0550-0600': 'Performance Evaluation',
            '0650-0700': 'Improvement',
            '0750-0800': 'Appendices'
        }
    ),
    'gdpr': FrameworkConfig(
        name='gdpr',
        display_name='GDPR',
        description='General Data Protection Regulation',
        template_count=50,
        number_ranges={
            '0010-0050': 'Foundation',
            '0100-0150': 'Data Protection Principles',
            '0200-0250': 'Data Subject Rights',
            '0300-0350': 'Controller and Processor Obligations',
            '0400-0450': 'Data Protection Impact Assessment',
            '0500-0550': 'Data Transfers',
            '0600-0650': 'Data Breach Management',
            '0700-0750': 'Appendices'
        }
    )
}
```



## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system—essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*

### Property Reflection

After analyzing all acceptance criteria, I identified several areas where properties can be consolidated:

**Redundancy Analysis**:
1. Requirements 1-7 follow identical patterns for different frameworks - these can be unified into framework-agnostic properties
2. File existence checks (README, metadata, FRAMEWORK_MAPPING) can be combined into a single comprehensive property
3. Bilingual consistency checks (filenames, structure, placeholders) are related and can be consolidated
4. Validation system checks overlap significantly and can be unified
5. Template numbering and naming conventions can be combined into structural validation properties

**Consolidated Properties**:
- Instead of 7 separate "framework coverage" properties (one per framework), use one property that applies to all frameworks
- Instead of separate properties for README, metadata, and mapping files, use one property for required documentation
- Instead of separate properties for German/English filename matching, structure matching, and placeholder matching, use one comprehensive bilingual consistency property

### Core Properties

#### Property 1: Template Naming Convention Compliance
*For any* template file in any framework, the filename must match the pattern `NNNN_descriptive_name.md` where NNNN is a 4-digit number.

**Validates: Requirements 8.1**

#### Property 2: Template Number Uniqueness
*For any* framework and language combination, all template numbers within that framework must be unique (no duplicate NNNN prefixes).

**Validates: Requirements 13.2**

#### Property 3: Template Number Increment Pattern
*For any* sequence of template numbers within a framework, consecutive numbers should differ by 10 (allowing for future insertions between templates).

**Validates: Requirements 8.2**

#### Property 4: Required Documentation Files Existence
*For any* framework, the template set must include README.md, FRAMEWORK_MAPPING.md, and a diagrams/ subdirectory.

**Validates: Requirements 1.4, 1.8, 8.6, 14.1**

#### Property 5: Metadata Template Existence
*For any* framework and language combination, a metadata template file named `0000_metadata_{language}_{framework}.md` must exist.

**Validates: Requirements 1.3, 9.6, 13.3**

#### Property 6: Template Header Structure
*For any* template file (excluding metadata and README), the content must include header fields for Dokument-ID, Owner, Version, Status, Klassifizierung, and Letzte Aktualisierung.

**Validates: Requirements 8.3**

#### Property 7: Markdown Section Structure
*For any* template file, the content must include at least one markdown section header (## or ###).

**Validates: Requirements 8.4**

#### Property 8: Placeholder Syntax Validity
*For any* placeholder in any template, it must match the pattern `{{ source.field }}` where source and field are valid identifiers.

**Validates: Requirements 8.5, 11.1, 11.5, 13.5**

#### Property 9: Bilingual Directory Structure
*For any* framework, both `templates/de/{framework}/` and `templates/en/{framework}/` directories must exist.

**Validates: Requirements 9.1, 9.2**

#### Property 10: Bilingual Filename Consistency
*For any* framework, the set of template filenames in the German directory must match the set of template filenames in the English directory (excluding language-specific metadata files).

**Validates: Requirements 9.3**

#### Property 11: Bilingual Structural Consistency
*For any* pair of corresponding German and English templates, the markdown header structure (H1, H2, H3 hierarchy) must be identical.

**Validates: Requirements 9.4**

#### Property 12: Bilingual Placeholder Consistency
*For any* pair of corresponding German and English templates, the placeholders must appear in the same positions (same line numbers or same section locations).

**Validates: Requirements 9.5**

#### Property 13: Framework Discovery
*For any* new framework directory added to `templates/de/` or `templates/en/`, the Template_Manager must automatically discover and load it without code changes.

**Validates: Requirements 10.1**

#### Property 14: Template Sorting by Number
*For any* set of templates loaded by Template_Manager, the returned list must be sorted in ascending order by template number.

**Validates: Requirements 10.3**

#### Property 15: Placeholder Recognition
*For any* template containing valid `{{ source.field }}` syntax, the Placeholder_System must recognize and extract all placeholders.

**Validates: Requirements 11.1, 11.2, 11.3**

#### Property 16: Placeholder Preservation on Missing Data
*For any* placeholder where the data source is unavailable, the original placeholder text must be preserved in the output (not replaced with empty string or error message).

**Validates: Requirements 11.4**

#### Property 17: Multi-Format Output Generation
*For any* framework, the Output_Generator must be able to produce HTML, PDF, and Markdown outputs without errors.

**Validates: Requirements 10.6, 12.1, 12.3, 12.5**

#### Property 18: Output Directory Structure
*For any* generated handbook, output files must be placed in `test-output/{language}/{framework}/{format}/` directory structure.

**Validates: Requirements 12.7**

#### Property 19: Validation Report Generation
*For any* framework and language combination, running validation must produce a ValidationReport object with error and warning lists.

**Validates: Requirements 13.7**

#### Property 20: CLI Framework Acceptance
*For any* framework in the SUPPORTED_FRAMEWORKS list, the CLI must accept it as a valid `--template` argument without raising an error.

**Validates: Requirements 10.7**

### Framework-Specific Properties

#### Property 21: PCI-DSS Requirement Coverage
*For any* PCI-DSS template set, templates must exist covering all 12 PCI-DSS requirements (Requirements 1-12).

**Validates: Requirements 1.1**

#### Property 22: HIPAA Safeguard Coverage
*For any* HIPAA template set, templates must exist covering Administrative, Physical, and Technical Safeguards plus Privacy Rule.

**Validates: Requirements 2.1**

#### Property 23: NIST 800-53 Control Family Coverage
*For any* NIST 800-53 template set, templates must exist covering all 20 control families (AC, AT, AU, CA, CM, CP, IA, IR, MA, MP, PE, PL, PM, PS, PT, RA, SA, SC, SI, SR).

**Validates: Requirements 3.1**

#### Property 24: TSC Category Coverage
*For any* TSC template set, templates must exist covering all 5 Trust Services Criteria categories (Security, Availability, Processing Integrity, Confidentiality, Privacy).

**Validates: Requirements 4.1**

#### Property 25: Common Criteria Security Target Structure
*For any* Common Criteria template set, templates must exist covering ST Introduction, TOE Description, Security Problem Definition, Security Objectives, Security Requirements, and TOE Summary Specification.

**Validates: Requirements 5.1**

#### Property 26: ISO 9001 Clause Coverage
*For any* ISO 9001 template set, templates must exist covering clauses 4-10 (Context, Leadership, Planning, Support, Operation, Performance Evaluation, Improvement).

**Validates: Requirements 6.1**

#### Property 27: GDPR Article Coverage
*For any* GDPR template set, templates must exist covering key GDPR articles including Article 30 (Records), Article 35 (DPIA), Articles 12-23 (Data Subject Rights), and Articles 33-34 (Breach Notification).

**Validates: Requirements 7.1**

### Integration Properties

#### Property 28: Template Loading Round-Trip
*For any* framework and language, loading templates then extracting their numbers and re-sorting should produce the same order as the original load.

**Validates: Requirements 10.3, 10.4**

#### Property 29: Validation Idempotence
*For any* template set, running validation twice should produce identical ValidationReport results (same errors and warnings).

**Validates: Requirements 13.1-13.7**

#### Property 30: Output Format Consistency
*For any* framework, generating output in all three formats (HTML, PDF, Markdown) should produce files with the same template content (only formatting differs).

**Validates: Requirements 12.1-12.7**

## Error Handling

### Template Loading Errors

**Error Scenarios**:
1. Framework directory not found
2. No templates found in directory
3. Malformed template filename
4. Template file cannot be read (permissions, encoding)
5. Duplicate template numbers

**Handling Strategy**:
```python
class TemplateLoadError(Exception):
    """Base exception for template loading errors."""
    pass

class FrameworkNotFoundError(TemplateLoadError):
    """Framework directory does not exist."""
    pass

class NoTemplatesFoundError(TemplateLoadError):
    """No valid templates found in framework directory."""
    pass

class DuplicateTemplateNumberError(TemplateLoadError):
    """Multiple templates with same number."""
    pass

def load_templates(language: str, framework: str) -> List[Template]:
    """Load templates with comprehensive error handling."""
    try:
        template_dir = Path(f"templates/{language}/{framework}")
        
        if not template_dir.exists():
            raise FrameworkNotFoundError(
                f"Framework directory not found: {template_dir}"
            )
        
        templates = []
        seen_numbers = set()
        
        for file_path in template_dir.glob("*.md"):
            if not re.match(r'^\d{4}_[\w-]+\.md$', file_path.name):
                logger.warning(f"Skipping malformed filename: {file_path.name}")
                continue
            
            try:
                template = parse_template(file_path)
                
                if template.number in seen_numbers:
                    raise DuplicateTemplateNumberError(
                        f"Duplicate template number {template.number} in {file_path.name}"
                    )
                
                seen_numbers.add(template.number)
                templates.append(template)
                
            except UnicodeDecodeError as e:
                logger.error(f"Cannot read {file_path.name}: {e}")
                continue
        
        if not templates:
            raise NoTemplatesFoundError(
                f"No valid templates found in {template_dir}"
            )
        
        return sorted(templates, key=lambda t: t.number)
        
    except PermissionError as e:
        raise TemplateLoadError(f"Permission denied accessing templates: {e}")
```

### Validation Errors

**Error Scenarios**:
1. Missing required files (README, metadata, FRAMEWORK_MAPPING)
2. Invalid placeholder syntax
3. Bilingual inconsistency
4. Missing header fields
5. Invalid template numbering

**Handling Strategy**:
- Validation errors are collected in ValidationReport, not raised as exceptions
- Errors prevent handbook generation
- Warnings allow generation but indicate quality issues
- Validation runs before any output generation

```python
def validate_framework(language: str, framework: str) -> ValidationReport:
    """Validate framework with error collection."""
    report = ValidationReport(framework=framework, language=language)
    
    try:
        # Collect all validation issues
        check_required_files(framework, language, report)
        check_template_structure(framework, language, report)
        check_placeholder_syntax(framework, language, report)
        check_bilingual_consistency(framework, report)
        
    except Exception as e:
        report.add_error(f"Validation failed with exception: {e}")
    
    return report
```

### Placeholder Processing Errors

**Error Scenarios**:
1. Invalid placeholder syntax
2. Data source unavailable
3. Field not found in data source
4. Data type mismatch

**Handling Strategy**:
```python
def process_placeholder(placeholder: str, data_sources: Dict[str, Any]) -> str:
    """Process placeholder with graceful fallback."""
    try:
        # Parse placeholder: {{ source.field }}
        match = re.match(r'\{\{\s*([\w]+)\.([\w.]+)\s*\}\}', placeholder)
        if not match:
            logger.warning(f"Invalid placeholder syntax: {placeholder}")
            return placeholder  # Preserve original
        
        source, field = match.groups()
        
        # Check data source exists
        if source not in data_sources:
            logger.debug(f"Data source '{source}' not available")
            return placeholder  # Preserve original
        
        # Navigate field path
        value = data_sources[source]
        for part in field.split('.'):
            if isinstance(value, dict) and part in value:
                value = value[part]
            else:
                logger.debug(f"Field '{field}' not found in source '{source}'")
                return placeholder  # Preserve original
        
        return str(value)
        
    except Exception as e:
        logger.error(f"Error processing placeholder {placeholder}: {e}")
        return placeholder  # Preserve original on any error
```

### Output Generation Errors

**Error Scenarios**:
1. Output directory cannot be created
2. File write permission denied
3. PDF generation fails (Pandoc not installed)
4. HTML template rendering fails
5. Disk space exhausted

**Handling Strategy**:
```python
class OutputGenerationError(Exception):
    """Base exception for output generation errors."""
    pass

def generate_output(templates: List[Template], format: str, output_dir: Path):
    """Generate output with error handling."""
    try:
        # Ensure output directory exists
        output_dir.mkdir(parents=True, exist_ok=True)
        
        if format == 'html':
            generate_html(templates, output_dir)
        elif format == 'pdf':
            try:
                generate_pdf(templates, output_dir)
            except FileNotFoundError:
                raise OutputGenerationError(
                    "PDF generation requires Pandoc. Install with: apt-get install pandoc"
                )
        elif format == 'markdown':
            generate_markdown(templates, output_dir)
        else:
            raise ValueError(f"Unsupported output format: {format}")
            
    except PermissionError as e:
        raise OutputGenerationError(f"Cannot write to {output_dir}: {e}")
    except OSError as e:
        if e.errno == 28:  # ENOSPC
            raise OutputGenerationError("Disk space exhausted")
        raise OutputGenerationError(f"OS error during output generation: {e}")
```

## Testing Strategy

### Dual Testing Approach

The compliance framework templates feature requires both unit testing and property-based testing:

**Unit Tests**: Focus on specific examples, edge cases, and integration points
- Test specific framework template loading (e.g., load PCI-DSS templates)
- Test specific validation scenarios (e.g., missing README file)
- Test specific placeholder substitutions (e.g., {{ meta.author }})
- Test error conditions (e.g., malformed filename)
- Test CLI argument parsing
- Test output file creation

**Property-Based Tests**: Verify universal properties across all inputs
- Test template naming convention for randomly generated filenames
- Test template number uniqueness for randomly generated template sets
- Test bilingual consistency for randomly generated template pairs
- Test placeholder syntax validation for randomly generated placeholders
- Test sorting behavior for randomly ordered template lists
- Test validation idempotence for randomly generated template sets

### Property-Based Testing Configuration

**Library**: Use `hypothesis` for Python property-based testing

**Configuration**:
- Minimum 100 iterations per property test
- Each test tagged with feature name and property number
- Tag format: `# Feature: compliance-framework-templates, Property N: [property text]`

**Example Property Test**:
```python
from hypothesis import given, strategies as st
import pytest

@given(st.lists(st.integers(min_value=10, max_value=9990, step=10), unique=True))
def test_property_14_template_sorting(template_numbers):
    """
    Feature: compliance-framework-templates, Property 14: Template Sorting by Number
    
    For any set of templates loaded by Template_Manager, the returned list
    must be sorted in ascending order by template number.
    """
    # Create mock templates with random numbers
    templates = [
        Template(number=num, title=f"Template {num}", file_path=Path(f"{num:04d}_test.md"), content="")
        for num in template_numbers
    ]
    
    # Shuffle templates
    import random
    shuffled = templates.copy()
    random.shuffle(shuffled)
    
    # Sort using Template_Manager logic
    sorted_templates = sorted(shuffled, key=lambda t: t.number)
    
    # Verify sorted order
    sorted_numbers = [t.number for t in sorted_templates]
    assert sorted_numbers == sorted(template_numbers)
```

### Unit Test Examples

```python
def test_load_pci_dss_templates():
    """Test loading PCI-DSS templates."""
    manager = TemplateManager()
    templates = manager.load_templates('de', 'pci-dss')
    
    assert len(templates) >= 40  # Expected minimum template count
    assert all(t.number >= 10 for t in templates)  # All have valid numbers
    assert templates[0].number < templates[-1].number  # Sorted order

def test_missing_metadata_template_detected():
    """Test validation detects missing metadata template."""
    validator = TemplateValidator()
    
    # Create test framework without metadata template
    test_dir = Path("test_templates/de/test-framework")
    test_dir.mkdir(parents=True, exist_ok=True)
    (test_dir / "0010_test.md").write_text("# Test")
    
    report = validator.validate_framework('de', 'test-framework')
    
    assert not report.is_valid()
    assert any('metadata' in error.lower() for error in report.errors)

def test_placeholder_substitution():
    """Test placeholder substitution with metadata."""
    processor = PlaceholderProcessor()
    template_content = "Author: {{ meta.author }}\nVersion: {{ meta.version }}"
    
    data_sources = {
        'meta': {
            'author': 'John Doe',
            'version': '1.0.0'
        }
    }
    
    result = processor.process(template_content, data_sources)
    
    assert "Author: John Doe" in result
    assert "Version: 1.0.0" in result

def test_cli_accepts_new_frameworks():
    """Test CLI accepts new framework names."""
    from src.cli import parse_arguments
    
    for framework in ['pci-dss', 'hipaa', 'nist-800-53', 'tsc', 'common-criteria', 'iso-9001', 'gdpr']:
        args = parse_arguments(['--language', 'de', '--template', framework, '--test'])
        assert args.template == framework
```

### Integration Tests

```python
def test_end_to_end_handbook_generation():
    """Test complete handbook generation for new framework."""
    # Load templates
    manager = TemplateManager()
    templates = manager.load_templates('de', 'pci-dss')
    
    # Validate
    validator = TemplateValidator()
    report = validator.validate_framework('de', 'pci-dss')
    assert report.is_valid()
    
    # Process placeholders
    processor = PlaceholderProcessor()
    data_sources = {'meta': {'author': 'Test', 'version': '1.0', 'date': '2025-01-01'}}
    processed_templates = [
        processor.process(t.content, data_sources) for t in templates
    ]
    
    # Generate output
    generator = OutputGenerator()
    output_dir = Path("test-output/de/pci-dss")
    generator.generate_html(processed_templates, output_dir / "html")
    generator.generate_pdf(processed_templates, output_dir / "pdf")
    generator.generate_markdown(processed_templates, output_dir / "markdown")
    
    # Verify outputs exist
    assert (output_dir / "html" / "index.html").exists()
    assert (output_dir / "pdf" / "pci-dss_handbook_de.pdf").exists()
    assert (output_dir / "markdown" / "TOC.md").exists()

def test_bilingual_consistency():
    """Test German and English templates are consistent."""
    manager = TemplateManager()
    de_templates = manager.load_templates('de', 'gdpr')
    en_templates = manager.load_templates('en', 'gdpr')
    
    # Same number of templates
    assert len(de_templates) == len(en_templates)
    
    # Same template numbers
    de_numbers = {t.number for t in de_templates}
    en_numbers = {t.number for t in en_templates}
    assert de_numbers == en_numbers
    
    # Same structure for each pair
    for de_t, en_t in zip(de_templates, en_templates):
        assert de_t.number == en_t.number
        
        # Extract markdown headers
        de_headers = re.findall(r'^#{1,3} ', de_t.content, re.MULTILINE)
        en_headers = re.findall(r'^#{1,3} ', en_t.content, re.MULTILINE)
        assert len(de_headers) == len(en_headers)
```

### Test Coverage Goals

- **Overall Coverage**: Minimum 80% code coverage for new functionality
- **Critical Paths**: 100% coverage for template loading, validation, and placeholder processing
- **Error Handling**: All error paths must be tested
- **Property Tests**: Minimum 100 iterations per property
- **Integration Tests**: End-to-end tests for each new framework

### Continuous Integration

```yaml
# .github/workflows/test.yml
name: Test Compliance Framework Templates

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.11'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
          pip install pytest pytest-cov hypothesis
      
      - name: Run unit tests
        run: pytest tests/ -v --cov=src --cov-report=html
      
      - name: Run property-based tests
        run: pytest tests/ -v -m property --hypothesis-show-statistics
      
      - name: Check coverage
        run: |
          coverage report --fail-under=80
      
      - name: Validate all frameworks
        run: |
          for framework in pci-dss hipaa nist-800-53 tsc common-criteria iso-9001 gdpr; do
            python -m src.cli --language de --template $framework --validate-only
            python -m src.cli --language en --template $framework --validate-only
          done
```

