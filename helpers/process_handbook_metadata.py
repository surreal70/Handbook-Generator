#!/usr/bin/env python3
"""
Process handbook metadata files for configuration separation.

This script:
1. Identifies all handbook directories
2. Creates meta-handbook.yaml files
3. Processes existing 0000_metadata files
4. Validates placeholders
5. Verifies bilingual consistency
"""

import os
import re
import yaml
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional
from collections import defaultdict


class HandbookMetadataProcessor:
    """Process handbook metadata for configuration separation."""
    
    def __init__(self, templates_root: Path = Path("templates")):
        self.templates_root = templates_root
        self.handbooks: Dict[str, Dict[str, Path]] = {}
        self.created_files: List[Path] = []
        
    def identify_handbooks(self) -> Dict[str, Dict[str, Path]]:
        """
        Identify all handbook directories across languages.
        
        Returns:
            Dict mapping handbook name to language paths:
            {
                'bcm': {'de': Path('templates/de/bcm'), 'en': Path('templates/en/bcm')},
                ...
            }
        """
        handbooks = defaultdict(dict)
        
        for lang in ['de', 'en']:
            lang_dir = self.templates_root / lang
            if not lang_dir.exists():
                continue
                
            for handbook_dir in sorted(lang_dir.iterdir()):
                if handbook_dir.is_dir():
                    handbook_name = handbook_dir.name
                    handbooks[handbook_name][lang] = handbook_dir
        
        self.handbooks = dict(handbooks)
        return self.handbooks
    
    def print_handbook_summary(self):
        """Print summary of identified handbooks."""
        print(f"\n{'='*70}")
        print(f"IDENTIFIED HANDBOOKS")
        print(f"{'='*70}\n")
        
        print(f"Total unique handbooks: {len(self.handbooks)}\n")
        
        for handbook_name in sorted(self.handbooks.keys()):
            langs = self.handbooks[handbook_name]
            lang_list = ', '.join(sorted(langs.keys()))
            print(f"  - {handbook_name:30s} [{lang_list}]")
        
        print(f"\n{'='*70}\n")
    
    def create_meta_handbook_yaml(self, handbook_name: str, handbook_path: Path) -> Path:
        """
        Create meta-handbook.yaml file for a handbook.
        
        Args:
            handbook_name: Name of the handbook (e.g., 'bcm')
            handbook_path: Path to the handbook directory
            
        Returns:
            Path to created meta-handbook.yaml file
        """
        meta_file = handbook_path / "meta-handbook.yaml"
        
        # Default metadata structure
        metadata = {
            'author': '[TODO]',
            'classification': '[TODO]',
            'status': '[TODO]',
            'type': '[TODO]',
            'templateset_version': '0.1',
            'revision': 0,
            'shortname': handbook_name,  # Use handbook directory name
            'longname': '[TODO]',
            'maintainer': '[TODO]',  # Will default to author in code
            'owner': '[TODO]',
            'approver': '[TODO]',
            'creationdate': '[TODO]',
            'modifydate': '[TODO]',
            'valid_from': '[TODO]',
            'next_review': '[TODO]',
            'scope': '[TODO]'
        }
        
        # Write YAML file with comments
        with open(meta_file, 'w', encoding='utf-8') as f:
            f.write("# Handbook-specific metadata\n")
            f.write(f"# Handbook: {handbook_name}\n")
            f.write("# This file contains metadata specific to this handbook\n\n")
            
            # Write fields with inline comments
            f.write("# Author of the handbook\n")
            f.write(f"author: \"{metadata['author']}\"\n\n")
            
            f.write("# Classification level (e.g., Internal, Confidential, Public)\n")
            f.write(f"classification: \"{metadata['classification']}\"\n\n")
            
            f.write("# Status (e.g., Draft, Review, Approved, Active)\n")
            f.write(f"status: \"{metadata['status']}\"\n\n")
            
            f.write("# Type of handbook\n")
            f.write(f"type: \"{metadata['type']}\"\n\n")
            
            f.write("# Template set version\n")
            f.write(f"templateset_version: \"{metadata['templateset_version']}\"\n\n")
            
            f.write("# Revision number (increment manually)\n")
            f.write(f"revision: {metadata['revision']}\n\n")
            
            f.write("# Short name (matches directory name)\n")
            f.write(f"shortname: \"{metadata['shortname']}\"\n\n")
            
            f.write("# Long descriptive name\n")
            f.write(f"longname: \"{metadata['longname']}\"\n\n")
            
            f.write("# Maintainer (defaults to author if not specified)\n")
            f.write(f"maintainer: \"{metadata['maintainer']}\"\n\n")
            
            f.write("# Owner responsible for the handbook\n")
            f.write(f"owner: \"{metadata['owner']}\"\n\n")
            
            f.write("# Approver of the handbook\n")
            f.write(f"approver: \"{metadata['approver']}\"\n\n")
            
            f.write("# Creation date (YYYY-MM-DD)\n")
            f.write(f"creationdate: \"{metadata['creationdate']}\"\n\n")
            
            f.write("# Last modification date (YYYY-MM-DD)\n")
            f.write(f"modifydate: \"{metadata['modifydate']}\"\n\n")
            
            f.write("# Valid from date (YYYY-MM-DD)\n")
            f.write(f"valid_from: \"{metadata['valid_from']}\"\n\n")
            
            f.write("# Next review date (YYYY-MM-DD)\n")
            f.write(f"next_review: \"{metadata['next_review']}\"\n\n")
            
            f.write("# Scope of the handbook\n")
            f.write(f"scope: \"{metadata['scope']}\"\n")
        
        return meta_file
    
    def create_all_meta_handbook_files(self) -> List[Path]:
        """
        Create meta-handbook.yaml files for all handbooks.
        
        Returns:
            List of created file paths
        """
        created_files = []
        
        for handbook_name in sorted(self.handbooks.keys()):
            for lang, handbook_path in self.handbooks[handbook_name].items():
                meta_file = self.create_meta_handbook_yaml(handbook_name, handbook_path)
                created_files.append(meta_file)
                print(f"  ✓ Created: {meta_file}")
        
        self.created_files = created_files
        return created_files
    
    def find_metadata_file(self, handbook_path: Path, lang: str) -> Optional[Path]:
        """
        Find the 0000_metadata file in a handbook directory.
        
        Args:
            handbook_path: Path to handbook directory
            lang: Language code (de or en)
            
        Returns:
            Path to metadata file or None if not found
        """
        handbook_name = handbook_path.name
        
        # Try different naming patterns
        patterns = [
            f"0000_metadata_{lang}_{handbook_name}.md",
            f"0000_metadata.md",
            "0000_metadata*.md"
        ]
        
        for pattern in patterns:
            matches = list(handbook_path.glob(pattern))
            if matches:
                return matches[0]
        
        return None
    
    def extract_metadata_from_file(self, metadata_file: Path) -> Dict[str, str]:
        """
        Extract metadata values from existing 0000_metadata file.
        
        Args:
            metadata_file: Path to metadata file
            
        Returns:
            Dictionary of extracted metadata values
        """
        content = metadata_file.read_text(encoding='utf-8')
        extracted = {}
        
        # Extract various metadata patterns
        patterns = {
            'owner': r'\*\*Owner:\*\*\s*\{\{\s*([^}]+)\s*\}\}',
            'status': r'\*\*Status:\*\*\s*\{\{\s*([^}]+)\s*\}\}',
            'classification': r'\*\*Klassifizierung:\*\*\s*\{\{\s*([^}]+)\s*\}\}|'
                            r'\*\*Classification:\*\*\s*\{\{\s*([^}]+)\s*\}\}',
            'revision': r'\*\*Revision:\*\*\s*(\d+)',
            'author': r'\*\*Autor:\*\*\s*\{\{\s*([^}]+)\s*\}\}|'
                     r'\*\*Author:\*\*\s*\{\{\s*([^}]+)\s*\}\}',
            'scope': r'\*\*Geltungsbereich:\*\*\s*\{\{\s*([^}]+)\s*\}\}|'
                    r'\*\*Scope:\*\*\s*\{\{\s*([^}]+)\s*\}\}',
            'valid_from': r'\*\*Gültig ab:\*\*\s*\{\{\s*([^}]+)\s*\}\}|'
                         r'\*\*Valid from:\*\*\s*\{\{\s*([^}]+)\s*\}\}',
            'next_review': r'\*\*Nächste Überprüfung:\*\*\s*\{\{\s*([^}]+)\s*\}\}|'
                          r'\*\*Next Review:\*\*\s*\{\{\s*([^}]+)\s*\}\}',
        }
        
        for key, pattern in patterns.items():
            match = re.search(pattern, content)
            if match:
                # Get first non-None group
                value = next((g for g in match.groups() if g), None)
                if value:
                    extracted[key] = value.strip()
        
        return extracted
    
    def create_standardized_metadata_content(self, handbook_name: str, lang: str) -> str:
        """
        Create standardized metadata file content.
        
        Args:
            handbook_name: Name of the handbook
            lang: Language code (de or en)
            
        Returns:
            Standardized metadata content
        """
        if lang == 'de':
            return f"""# {handbook_name.upper()} Handbuch - Metadaten

**Dokument-ID:** 0000  
**Owner:** {{{{ meta-handbook.owner }}}}  
**Revision:** {{{{ meta-handbook.revision }}}}  
**Status:** {{{{ meta-handbook.status }}}}  
**Klassifizierung:** {{{{ meta-handbook.classification }}}}  
**Letzte Aktualisierung:** {{{{ meta-handbook.modifydate }}}}  
**Template-Version:** {{{{ meta-handbook.templateset_version }}}}  

---

## Handbuch-Informationen

**Handbuch-Titel:** {{{{ meta-handbook.longname }}}}  
**Handbuch-Short:** {{{{ meta-handbook.shortname }}}}  
**Organisation:** {{{{ meta-organisation.name }}}}  
**Autor:** {{{{ meta-handbook.author }}}}  
**Geltungsbereich:** {{{{ meta-handbook.scope }}}}  
**Gültig ab:** {{{{ meta-handbook.valid_from }}}}  
**Nächste Überprüfung:** {{{{ meta-handbook.next_review }}}}  

---

## Dokumentenzweck

Dieses Dokument enthält die Metadaten für das {handbook_name.upper()} Handbuch.

## Änderungshistorie

| Version | Datum | Autor | Änderung |
|---------|-------|-------|----------|
| {{{{ meta-handbook.revision }}}} | {{{{ meta-handbook.modifydate }}}} | {{{{ meta-handbook.author }}}} | Initiale Version |
"""
        else:  # English
            return f"""# {handbook_name.upper()} Handbook - Metadata

**Document-ID:** 0000  
**Owner:** {{{{ meta-handbook.owner }}}}  
**Revision:** {{{{ meta-handbook.revision }}}}  
**Status:** {{{{ meta-handbook.status }}}}  
**Classification:** {{{{ meta-handbook.classification }}}}  
**Last Update:** {{{{ meta-handbook.modifydate }}}}  
**Template-Version:** {{{{ meta-handbook.templateset_version }}}}  

---

## Handbook Information

**Handbook Title:** {{{{ meta-handbook.longname }}}}  
**Handbook Short:** {{{{ meta-handbook.shortname }}}}  
**Organisation:** {{{{ meta-organisation.name }}}}  
**Author:** {{{{ meta-handbook.author }}}}  
**Scope:** {{{{ meta-handbook.scope }}}}  
**Valid from:** {{{{ meta-handbook.valid_from }}}}  
**Next Review:** {{{{ meta-handbook.next_review }}}}  

---

## Document Purpose

This document contains the metadata for the {handbook_name.upper()} handbook.

## Change History

| Version | Date | Author | Change |
|---------|------|--------|--------|
| {{{{ meta-handbook.revision }}}} | {{{{ meta-handbook.modifydate }}}} | {{{{ meta-handbook.author }}}} | Initial version |
"""
    
    def process_metadata_files(self) -> Dict[str, int]:
        """
        Process all existing 0000_metadata files.
        
        Returns:
            Statistics about processed files
        """
        stats = {
            'found': 0,
            'updated': 0,
            'not_found': 0
        }
        
        for handbook_name in sorted(self.handbooks.keys()):
            for lang, handbook_path in self.handbooks[handbook_name].items():
                metadata_file = self.find_metadata_file(handbook_path, lang)
                
                if metadata_file:
                    stats['found'] += 1
                    
                    # Extract existing metadata (for reference, not used in this task)
                    # extracted = self.extract_metadata_from_file(metadata_file)
                    
                    # Create standardized content
                    new_content = self.create_standardized_metadata_content(handbook_name, lang)
                    
                    # Write new content
                    metadata_file.write_text(new_content, encoding='utf-8')
                    stats['updated'] += 1
                    
                    print(f"  ✓ Updated: {metadata_file}")
                else:
                    stats['not_found'] += 1
                    print(f"  ⚠ Not found: {handbook_path} ({lang})")
        
        return stats
    
    def scan_template_placeholders(self, template_file: Path) -> Set[str]:
        """
        Scan a template file for placeholders.
        
        Args:
            template_file: Path to template file
            
        Returns:
            Set of placeholder strings found
        """
        content = template_file.read_text(encoding='utf-8')
        
        # Match {{ meta-handbook.* }} placeholders
        pattern = r'\{\{\s*meta-handbook\.(\w+)\s*\}\}'
        matches = re.findall(pattern, content)
        
        return set(matches)
    
    def get_meta_handbook_fields(self) -> Set[str]:
        """
        Get the set of fields defined in meta-handbook.yaml.
        
        Returns:
            Set of field names
        """
        # These are the fields defined in the meta-handbook.yaml structure
        return {
            'author', 'classification', 'status', 'type', 'templateset_version',
            'revision', 'shortname', 'longname', 'maintainer', 'owner',
            'approver', 'creationdate', 'modifydate', 'valid_from',
            'next_review', 'scope'
        }
    
    def validate_handbook_placeholders(self) -> Dict[str, any]:
        """
        Validate handbook-specific placeholders across all templates.
        
        Returns:
            Validation results with statistics and issues
        """
        results = {
            'total_templates': 0,
            'templates_with_placeholders': 0,
            'unique_placeholders': set(),
            'undefined_placeholders': set(),
            'issues': []
        }
        
        valid_fields = self.get_meta_handbook_fields()
        
        for handbook_name in sorted(self.handbooks.keys()):
            for lang, handbook_path in self.handbooks[handbook_name].items():
                # Scan all .md files in handbook
                for template_file in handbook_path.glob('*.md'):
                    results['total_templates'] += 1
                    
                    placeholders = self.scan_template_placeholders(template_file)
                    
                    if placeholders:
                        results['templates_with_placeholders'] += 1
                        results['unique_placeholders'].update(placeholders)
                        
                        # Check for undefined placeholders
                        undefined = placeholders - valid_fields
                        if undefined:
                            results['undefined_placeholders'].update(undefined)
                            results['issues'].append({
                                'file': str(template_file),
                                'undefined': list(undefined)
                            })
        
        return results
    
    def print_placeholder_validation_report(self, results: Dict[str, any]):
        """Print placeholder validation report."""
        print(f"\n{'='*70}")
        print(f"PLACEHOLDER VALIDATION REPORT")
        print(f"{'='*70}\n")
        
        print(f"Total templates scanned: {results['total_templates']}")
        print(f"Templates with meta-handbook placeholders: {results['templates_with_placeholders']}")
        print(f"Unique placeholders found: {len(results['unique_placeholders'])}")
        
        if results['unique_placeholders']:
            print(f"\nPlaceholders found:")
            for placeholder in sorted(results['unique_placeholders']):
                print(f"  - meta-handbook.{placeholder}")
        
        if results['undefined_placeholders']:
            print(f"\n⚠ UNDEFINED PLACEHOLDERS: {len(results['undefined_placeholders'])}")
            for placeholder in sorted(results['undefined_placeholders']):
                print(f"  - meta-handbook.{placeholder}")
            
            print(f"\nFiles with undefined placeholders:")
            for issue in results['issues']:
                print(f"  {issue['file']}")
                for placeholder in issue['undefined']:
                    print(f"    - meta-handbook.{placeholder}")
        else:
            print(f"\n✓ All placeholders are defined in meta-handbook.yaml")
        
        print(f"\n{'='*70}\n")
    
    def identify_unused_fields(self, validation_results: Dict[str, any]) -> Set[str]:
        """
        Identify meta-handbook.yaml fields that are not used in any template.
        
        Args:
            validation_results: Results from validate_handbook_placeholders()
            
        Returns:
            Set of unused field names
        """
        valid_fields = self.get_meta_handbook_fields()
        used_fields = validation_results['unique_placeholders']
        
        unused = valid_fields - used_fields
        return unused
    
    def print_unused_fields_report(self, unused_fields: Set[str]):
        """Print report of unused fields."""
        print(f"\n{'='*70}")
        print(f"UNUSED FIELDS REPORT")
        print(f"{'='*70}\n")
        
        if unused_fields:
            print(f"⚠ Fields defined in meta-handbook.yaml but not used in templates: {len(unused_fields)}")
            print(f"\nUnused fields:")
            for field in sorted(unused_fields):
                print(f"  - {field}")
            
            print(f"\nRecommendations:")
            print(f"  1. Consider adding placeholders for these fields in templates")
            print(f"  2. Or remove unused fields from meta-handbook.yaml")
        else:
            print(f"✓ All meta-handbook.yaml fields are used in templates")
        
        print(f"\n{'='*70}\n")


def verify_bilingual_consistency(processor: HandbookMetadataProcessor) -> Dict[str, any]:
    """
    Verify bilingual consistency for handbook metadata.
    
    Args:
        processor: HandbookMetadataProcessor instance
        
    Returns:
        Consistency check results
    """
    results = {
        'total_handbooks': 0,
        'consistent': 0,
        'inconsistent': 0,
        'issues': []
    }
    
    for handbook_name in sorted(processor.handbooks.keys()):
        langs = processor.handbooks[handbook_name]
        
        # Only check if both languages exist
        if 'de' not in langs or 'en' not in langs:
            continue
        
        results['total_handbooks'] += 1
        
        de_path = langs['de']
        en_path = langs['en']
        
        # Check meta-handbook.yaml structure
        de_meta = de_path / 'meta-handbook.yaml'
        en_meta = en_path / 'meta-handbook.yaml'
        
        de_fields = set()
        en_fields = set()
        
        if de_meta.exists():
            with open(de_meta, 'r', encoding='utf-8') as f:
                de_data = yaml.safe_load(f)
                if de_data:
                    de_fields = set(de_data.keys())
        
        if en_meta.exists():
            with open(en_meta, 'r', encoding='utf-8') as f:
                en_data = yaml.safe_load(f)
                if en_data:
                    en_fields = set(en_data.keys())
        
        # Check field consistency
        if de_fields != en_fields:
            results['inconsistent'] += 1
            missing_in_en = de_fields - en_fields
            missing_in_de = en_fields - de_fields
            
            results['issues'].append({
                'handbook': handbook_name,
                'type': 'field_mismatch',
                'missing_in_en': list(missing_in_en),
                'missing_in_de': list(missing_in_de)
            })
        else:
            # Check placeholder usage consistency
            de_placeholders = set()
            en_placeholders = set()
            
            for template_file in de_path.glob('*.md'):
                de_placeholders.update(processor.scan_template_placeholders(template_file))
            
            for template_file in en_path.glob('*.md'):
                en_placeholders.update(processor.scan_template_placeholders(template_file))
            
            if de_placeholders != en_placeholders:
                results['inconsistent'] += 1
                missing_in_en = de_placeholders - en_placeholders
                missing_in_de = en_placeholders - de_placeholders
                
                results['issues'].append({
                    'handbook': handbook_name,
                    'type': 'placeholder_mismatch',
                    'missing_in_en': list(missing_in_en),
                    'missing_in_de': list(missing_in_de)
                })
            else:
                results['consistent'] += 1
    
    return results


def print_bilingual_consistency_report(results: Dict[str, any]):
    """Print bilingual consistency report."""
    print(f"\n{'='*70}")
    print(f"BILINGUAL CONSISTENCY REPORT")
    print(f"{'='*70}\n")
    
    print(f"Total handbooks checked: {results['total_handbooks']}")
    print(f"Consistent: {results['consistent']}")
    print(f"Inconsistent: {results['inconsistent']}")
    
    if results['issues']:
        print(f"\n⚠ INCONSISTENCIES FOUND:\n")
        
        for issue in results['issues']:
            print(f"Handbook: {issue['handbook']}")
            print(f"  Issue type: {issue['type']}")
            
            if issue['type'] == 'field_mismatch':
                if issue['missing_in_en']:
                    print(f"  Missing in English meta-handbook.yaml:")
                    for field in issue['missing_in_en']:
                        print(f"    - {field}")
                if issue['missing_in_de']:
                    print(f"  Missing in German meta-handbook.yaml:")
                    for field in issue['missing_in_de']:
                        print(f"    - {field}")
            
            elif issue['type'] == 'placeholder_mismatch':
                if issue['missing_in_en']:
                    print(f"  Placeholders in German but not in English:")
                    for placeholder in issue['missing_in_en']:
                        print(f"    - meta-handbook.{placeholder}")
                if issue['missing_in_de']:
                    print(f"  Placeholders in English but not in German:")
                    for placeholder in issue['missing_in_de']:
                        print(f"    - meta-handbook.{placeholder}")
            
            print()
    else:
        print(f"\n✓ All handbooks have consistent bilingual metadata")
    
    print(f"{'='*70}\n")


def main():
    """Main execution."""
    processor = HandbookMetadataProcessor()
    
    # Task 9.51.1: Identify all handbook directories
    print("Task 9.51.1: Identifying handbook directories...")
    handbooks = processor.identify_handbooks()
    processor.print_handbook_summary()
    print(f"✓ Task 9.51.1 complete: Identified {len(handbooks)} unique handbooks\n")
    
    # Task 9.51.2: Create meta-handbook.yaml for each handbook
    print("Task 9.51.2: Creating meta-handbook.yaml files...")
    created_files = processor.create_all_meta_handbook_files()
    print(f"\n✓ Task 9.51.2 complete: Created {len(created_files)} meta-handbook.yaml files\n")
    
    # Task 9.51.3: Process existing 0000_metadata files
    print("Task 9.51.3: Processing existing 0000_metadata files...")
    stats = processor.process_metadata_files()
    print(f"\n✓ Task 9.51.3 complete:")
    print(f"  - Found: {stats['found']}")
    print(f"  - Updated: {stats['updated']}")
    print(f"  - Not found: {stats['not_found']}\n")
    
    # Task 9.51.4: Validate handbook-specific placeholders
    print("Task 9.51.4: Validating handbook-specific placeholders...")
    validation_results = processor.validate_handbook_placeholders()
    processor.print_placeholder_validation_report(validation_results)
    print(f"✓ Task 9.51.4 complete\n")
    
    # Task 9.51.5: Identify missing placeholders in templates
    print("Task 9.51.5: Identifying unused fields...")
    unused_fields = processor.identify_unused_fields(validation_results)
    processor.print_unused_fields_report(unused_fields)
    print(f"✓ Task 9.51.5 complete\n")
    
    # Task 9.51.6: Verify bilingual consistency for handbook metadata
    print("Task 9.51.6: Verifying bilingual consistency...")
    consistency_results = verify_bilingual_consistency(processor)
    print_bilingual_consistency_report(consistency_results)
    print(f"✓ Task 9.51.6 complete\n")


if __name__ == "__main__":
    main()
