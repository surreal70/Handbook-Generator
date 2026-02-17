#!/usr/bin/env python3
"""
Script to update template files with new placeholder format and standardized headers.

This script:
1. Replaces old placeholder format with new format
2. Adds standardized document headers
3. Removes trailing version information
"""

import re
import sys
from pathlib import Path
from typing import Dict, Tuple

# Placeholder mapping from old to new format
PLACEHOLDER_MAPPINGS = {
    # Organization placeholders
    r'\{\{\s*meta\.organization\.name\s*\}\}': '{{ meta-organisation.name }}',
    r'\{\{\s*meta\.organisation\.name\s*\}\}': '{{ meta-organisation.name }}',
    r'\{\{\s*meta\.organization\.address\s*\}\}': '{{ meta-organisation.address }}',
    r'\{\{\s*meta\.organisation\.address\s*\}\}': '{{ meta-organisation.address }}',
    r'\{\{\s*meta\.organization\.web\s*\}\}': '{{ meta-organisation.web }}',
    r'\{\{\s*meta\.organisation\.web\s*\}\}': '{{ meta-organisation.web }}',
    r'\{\{\s*meta\.organization\.phone\s*\}\}': '{{ meta-organisation.phone }}',
    r'\{\{\s*meta\.organisation\.phone\s*\}\}': '{{ meta-organisation.phone }}',
    r'\{\{\s*meta\.organization\.revision\s*\}\}': '{{ meta-organisation.revision }}',
    r'\{\{\s*meta\.organisation\.revision\s*\}\}': '{{ meta-organisation.revision }}',
    
    # Document/Handbook placeholders
    r'\{\{\s*meta\.document\.owner\s*\}\}': '{{ meta-handbook.owner }}',
    r'\{\{\s*meta\.document\.approver\s*\}\}': '{{ meta-handbook.approver }}',
    r'\{\{\s*meta\.document\.version\s*\}\}': '{{ meta-handbook.revision }}',
    r'\{\{\s*meta\.document\.revision\s*\}\}': '{{ meta-handbook.revision }}',
    r'\{\{\s*meta\.document\.author\s*\}\}': '{{ meta-handbook.author }}',
    r'\{\{\s*meta\.document\.status\s*\}\}': '{{ meta-handbook.status }}',
    r'\{\{\s*meta\.document\.classification\s*\}\}': '{{ meta-handbook.classification }}',
    r'\{\{\s*meta\.document\.last_updated\s*\}\}': '{{ meta-handbook.modifydate }}',
    r'\{\{\s*meta\.document\.modifydate\s*\}\}': '{{ meta-handbook.modifydate }}',
    r'\{\{\s*meta\.document\.creationdate\s*\}\}': '{{ meta-handbook.creationdate }}',
    r'\{\{\s*meta\.document\.valid_from\s*\}\}': '{{ meta-handbook.valid_from }}',
    r'\{\{\s*meta\.document\.next_review\s*\}\}': '{{ meta-handbook.next_review }}',
    r'\{\{\s*meta\.document\.maintainer\s*\}\}': '{{ meta-handbook.maintainer }}',
    r'\{\{\s*meta\.document\.scope\s*\}\}': '{{ meta-handbook.scope }}',
    r'\{\{\s*meta\.document\.type\s*\}\}': '{{ meta-handbook.type }}',
    r'\{\{\s*meta\.document\.shortname\s*\}\}': '{{ meta-handbook.shortname }}',
    r'\{\{\s*meta\.document\.longname\s*\}\}': '{{ meta-handbook.longname }}',
    r'\{\{\s*meta\.document\.approval_date\s*\}\}': '{{ meta-handbook.modifydate }}',
    r'\{\{\s*meta\.document\.approval_status\s*\}\}': '{{ meta-handbook.status }}',
    
    # Role placeholders
    r'\{\{\s*meta\.roles\.ceo\.name\s*\}\}': '{{ meta-organisation-roles.role_CEO }}',
    r'\{\{\s*meta\.roles\.ceo\.email\s*\}\}': '{{ meta-organisation-roles.role_CEO }}',
    r'\{\{\s*meta\.roles\.cfo\.name\s*\}\}': '{{ meta-organisation-roles.role_CFO }}',
    r'\{\{\s*meta\.roles\.cfo\.email\s*\}\}': '{{ meta-organisation-roles.role_CFO }}',
    r'\{\{\s*meta\.roles\.cto\.name\s*\}\}': '{{ meta-organisation-roles.role_CTO }}',
    r'\{\{\s*meta\.roles\.cto\.email\s*\}\}': '{{ meta-organisation-roles.role_CTO }}',
    r'\{\{\s*meta\.roles\.cio\.name\s*\}\}': '{{ meta-organisation-roles.role_CIO }}',
    r'\{\{\s*meta\.roles\.cio\.email\s*\}\}': '{{ meta-organisation-roles.role_CIO }}',
    r'\{\{\s*meta\.roles\.ciso\.name\s*\}\}': '{{ meta-organisation-roles.role_CISO }}',
    r'\{\{\s*meta\.roles\.ciso\.email\s*\}\}': '{{ meta-organisation-roles.role_CISO }}',
    r'\{\{\s*meta\.roles\.hr_manager\.name\s*\}\}': '{{ meta-organisation-roles.role_HR_Manager }}',
    r'\{\{\s*meta\.roles\.hr_manager\.email\s*\}\}': '{{ meta-organisation-roles.role_HR_Manager }}',
    r'\{\{\s*meta\.roles\.risk_manager\.name\s*\}\}': '{{ meta-organisation-roles.role_Risk_Manager }}',
    r'\{\{\s*meta\.roles\.risk_manager\.email\s*\}\}': '{{ meta-organisation-roles.role_Risk_Manager }}',
    r'\{\{\s*meta\.roles\.gdpr_manager\.name\s*\}\}': '{{ meta-organisation-roles.role_GDPR_Manager }}',
    r'\{\{\s*meta\.roles\.gdpr_manager\.email\s*\}\}': '{{ meta-organisation-roles.role_GDPR_Manager }}',
    r'\{\{\s*meta\.roles\.it_manager\.name\s*\}\}': '{{ meta-organisation-roles.role_IT_Manager }}',
    r'\{\{\s*meta\.roles\.it_manager\.email\s*\}\}': '{{ meta-organisation-roles.role_IT_Manager }}',
    r'\{\{\s*meta\.roles\.it_operations_manager\.name\s*\}\}': '{{ meta-organisation-roles.role_IT_Manager }}',
    r'\{\{\s*meta\.roles\.it_operations_manager\.email\s*\}\}': '{{ meta-organisation-roles.role_IT_Manager }}',
    r'\{\{\s*meta\.roles\.compliance_manager\.name\s*\}\}': '{{ meta-organisation-roles.role_Compliance_Manager }}',
    r'\{\{\s*meta\.roles\.compliance_manager\.email\s*\}\}': '{{ meta-organisation-roles.role_Compliance_Manager }}',
    r'\{\{\s*meta\.roles\.internal_auditor\.name\s*\}\}': '{{ meta-organisation-roles.role_Internal_Auditor }}',
    r'\{\{\s*meta\.roles\.internal_auditor\.email\s*\}\}': '{{ meta-organisation-roles.role_Internal_Auditor }}',
    
    # Group placeholders
    r'\{\{\s*meta\.groups\.it_services\s*\}\}': '{{ meta-organisation-roles.group_IT_Services }}',
    r'\{\{\s*meta\.groups\.devops\s*\}\}': '{{ meta-organisation-roles.group_DEVOPS }}',
    r'\{\{\s*meta\.groups\.helpdesk\s*\}\}': '{{ meta-organisation-roles.group_Helpdesk }}',
    
    # Global placeholders
    r'\{\{\s*meta\.defaults\.author\s*\}\}': '{{ meta-handbook.author }}',
    r'\{\{\s*metadata\.version\s*\}\}': '{{ meta-global.version }}',
    r'\{\{\s*metadata\.source\s*\}\}': '{{ meta-global.source }}',
}

# German document header template
GERMAN_HEADER_TEMPLATE = """**Dokument-ID:** {doc_id}
**Organisation:** {{{{ meta-organisation.name }}}}
**Owner:** {{{{ meta-handbook.owner }}}}
**Genehmigt durch:** {{{{ meta-handbook.approver }}}}
**Revision:** {{{{ meta-handbook.revision }}}}
**Author:** {{{{ meta-handbook.author }}}}
**Status:** {{{{ meta-handbook.status }}}}
**Klassifizierung:** {{{{ meta-handbook.classification }}}}
**Letzte Aktualisierung:** {{{{ meta-handbook.modifydate }}}}"""

# English document header template
ENGLISH_HEADER_TEMPLATE = """**Document-ID:** {doc_id}
**Organisation:** {{{{ meta-organisation.name }}}}
**Owner:** {{{{ meta-handbook.owner }}}}
**Approved by:** {{{{ meta-handbook.approver }}}}
**Revision:** {{{{ meta-handbook.revision }}}}
**Author:** {{{{ meta-handbook.author }}}}
**Status:** {{{{ meta-handbook.status }}}}
**Classification:** {{{{ meta-handbook.classification }}}}
**Last Update:** {{{{ meta-handbook.modifydate }}}}"""


def extract_doc_id(content: str, filename: str) -> str:
    """Extract document ID from existing header or generate from filename."""
    # Try to find existing Document-ID
    match = re.search(r'\*\*Dokument-ID:\*\*\s*([^\n]+)', content)
    if not match:
        match = re.search(r'\*\*Document-ID:\*\*\s*([^\n]+)', content)
    
    if match:
        return match.group(1).strip()
    
    # Generate from filename (e.g., 0020_BCM_Leitlinie_Policy.md -> BCM-0020)
    match = re.match(r'(\d{4})_', filename)
    if match:
        number = match.group(1)
        # Extract framework from path
        return f"[FRAMEWORK]-{number}"
    
    return "[TODO: Document-ID]"


def has_header(content: str) -> bool:
    """Check if content already has a document header."""
    return bool(re.search(r'\*\*Dokument-ID:\*\*|\*\*Document-ID:\*\*', content))


def remove_trailing_version_info(content: str) -> str:
    """Remove trailing version information section."""
    # Remove version history at the end
    content = re.sub(
        r'\n---\n\n\*\*Dokumenthistorie:\*\*.*?<!-- End of template -->',
        '\n\n<!-- End of template -->',
        content,
        flags=re.DOTALL
    )
    
    # Remove standalone version history
    content = re.sub(
        r'\n\*\*Dokumenthistorie:\*\*.*?$',
        '',
        content,
        flags=re.DOTALL
    )
    
    return content


def update_header(content: str, filename: str, is_german: bool) -> str:
    """Update or add standardized document header."""
    doc_id = extract_doc_id(content, filename)
    
    # Choose appropriate header template
    header_template = GERMAN_HEADER_TEMPLATE if is_german else ENGLISH_HEADER_TEMPLATE
    new_header = header_template.format(doc_id=doc_id)
    
    # Remove ALL existing headers (both formats)
    # Pattern matches from Document-ID/Dokument-ID to the next separator or section
    content = re.sub(
        r'\*\*(?:Dokument-ID|Document-ID):\*\*[^\n]*\n(?:\*\*[^*]+\*\*[^\n]*\n)*',
        '',
        content
    )
    
    # Remove multiple consecutive separators
    content = re.sub(r'(\n---\n)+', '\n---\n', content)
    
    # Remove extra blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # Add new header after title
    lines = content.split('\n')
    title_idx = -1
    for i, line in enumerate(lines):
        if line.startswith('# '):
            title_idx = i
            break
    
    if title_idx >= 0:
        # Insert header after title
        lines.insert(title_idx + 1, '')
        lines.insert(title_idx + 2, new_header)
        lines.insert(title_idx + 3, '')
        lines.insert(title_idx + 4, '---')
        content = '\n'.join(lines)
    
    return content


def replace_placeholders(content: str) -> str:
    """Replace old placeholder format with new format."""
    for old_pattern, new_placeholder in PLACEHOLDER_MAPPINGS.items():
        content = re.sub(old_pattern, new_placeholder, content)
    
    return content


def process_template_file(file_path: Path, is_german: bool) -> Tuple[bool, str]:
    """
    Process a single template file.
    
    Returns:
        Tuple of (success, message)
    """
    try:
        content = file_path.read_text(encoding='utf-8')
        
        # Skip metadata files and README files
        if file_path.name.startswith('0000_metadata') or file_path.name == 'README.md':
            return True, f"Skipped {file_path.name} (metadata/README)"
        
        # Replace placeholders
        content = replace_placeholders(content)
        
        # Update header
        content = update_header(content, file_path.name, is_german)
        
        # Remove trailing version info
        content = remove_trailing_version_info(content)
        
        # Write back
        file_path.write_text(content, encoding='utf-8')
        
        return True, f"Updated {file_path.name}"
    
    except Exception as e:
        return False, f"Error processing {file_path.name}: {str(e)}"


def process_framework_directory(framework_dir: Path, is_german: bool) -> Dict[str, int]:
    """
    Process all template files in a framework directory.
    
    Returns:
        Dictionary with counts of processed, skipped, and failed files
    """
    stats = {'processed': 0, 'skipped': 0, 'failed': 0}
    
    # Find all markdown files
    for md_file in framework_dir.glob('*.md'):
        success, message = process_template_file(md_file, is_german)
        
        if 'Skipped' in message:
            stats['skipped'] += 1
        elif success:
            stats['processed'] += 1
        else:
            stats['failed'] += 1
            print(f"  ❌ {message}", file=sys.stderr)
    
    return stats


def main():
    """Main entry point."""
    templates_dir = Path('templates')
    
    if not templates_dir.exists():
        print("Error: templates directory not found", file=sys.stderr)
        sys.exit(1)
    
    # Process German templates
    print("Processing German templates...")
    de_dir = templates_dir / 'de'
    total_stats = {'processed': 0, 'skipped': 0, 'failed': 0}
    
    for framework_dir in sorted(de_dir.iterdir()):
        if framework_dir.is_dir():
            print(f"  Processing {framework_dir.name}...")
            stats = process_framework_directory(framework_dir, is_german=True)
            for key in total_stats:
                total_stats[key] += stats[key]
    
    print(f"\nGerman templates: {total_stats['processed']} processed, "
          f"{total_stats['skipped']} skipped, {total_stats['failed']} failed")
    
    # Process English templates
    print("\nProcessing English templates...")
    en_dir = templates_dir / 'en'
    en_stats = {'processed': 0, 'skipped': 0, 'failed': 0}
    
    if en_dir.exists():
        for framework_dir in sorted(en_dir.iterdir()):
            if framework_dir.is_dir():
                print(f"  Processing {framework_dir.name}...")
                stats = process_framework_directory(framework_dir, is_german=False)
                for key in en_stats:
                    en_stats[key] += stats[key]
        
        print(f"\nEnglish templates: {en_stats['processed']} processed, "
              f"{en_stats['skipped']} skipped, {en_stats['failed']} failed")
    else:
        print("  No English templates directory found")
    
    # Overall summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    print(f"Total processed: {total_stats['processed'] + en_stats['processed']}")
    print(f"Total skipped: {total_stats['skipped'] + en_stats['skipped']}")
    print(f"Total failed: {total_stats['failed'] + en_stats['failed']}")
    
    if total_stats['failed'] + en_stats['failed'] > 0:
        sys.exit(1)


if __name__ == '__main__':
    main()
