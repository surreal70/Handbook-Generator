"""
Property-based tests for template header validation.

**Property 11: Standardized Document Headers**
**Validates: Requirements 8.1**

For any template file, it should contain a document header section with the required 
metadata fields (Document-ID, Organisation, Owner, Approved by, Revision, Author, 
Status, Classification, Last Update).
"""

import pytest
from pathlib import Path
from hypothesis import given, strategies as st, settings, HealthCheck
import re


# Required header fields for all templates
REQUIRED_HEADER_FIELDS_DE = [
    'Dokument-ID',
    'Organisation',
    'Owner',
    'Genehmigt durch',
    'Revision',
    'Author',
    'Status',
    'Klassifizierung',
    'Letzte Aktualisierung'
]

REQUIRED_HEADER_FIELDS_EN = [
    'Document-ID',
    'Organisation',
    'Owner',
    'Approved by',
    'Revision',
    'Author',
    'Status',
    'Classification',
    'Last Update'
]


def get_all_template_files():
    """Get all template markdown files (excluding metadata and README)."""
    templates_dir = Path('templates')
    if not templates_dir.exists():
        return []
    
    template_files = []
    for md_file in templates_dir.rglob('*.md'):
        # Skip metadata files and README files
        if md_file.name.startswith('0000_metadata') or md_file.name == 'README.md':
            continue
        
        # Skip service directory template files (they're templates within templates)
        if 'service-templates' in str(md_file) or 'email-service' in str(md_file):
            continue
        
        # Skip empty files
        if md_file.stat().st_size == 0:
            continue
        
        template_files.append(md_file)
    
    return template_files


def has_standardized_header(content: str, is_german: bool) -> tuple[bool, list[str]]:
    """
    Check if content has a standardized document header with all required fields.
    
    Returns:
        Tuple of (has_header, missing_fields)
    """
    required_fields = REQUIRED_HEADER_FIELDS_DE if is_german else REQUIRED_HEADER_FIELDS_EN
    missing_fields = []
    
    for field in required_fields:
        # Check if field exists in header format: **Field:** value
        pattern = rf'\*\*{re.escape(field)}:\*\*'
        if not re.search(pattern, content):
            missing_fields.append(field)
    
    return len(missing_fields) == 0, missing_fields


@pytest.mark.parametrize('template_file', get_all_template_files())
def test_template_has_standardized_header(template_file):
    """
    Property 11: Standardized Document Headers
    
    For any template file, it should contain a document header section with 
    the required metadata fields.
    """
    content = template_file.read_text(encoding='utf-8')
    
    # Determine language from path
    is_german = '/de/' in str(template_file)
    
    has_header, missing_fields = has_standardized_header(content, is_german)
    
    assert has_header, (
        f"Template {template_file} is missing required header fields: {missing_fields}"
    )


@given(st.sampled_from(get_all_template_files() or [Path('dummy.md')]))
@settings(
    max_examples=100,
    suppress_health_check=[HealthCheck.function_scoped_fixture],
    deadline=None
)
def test_property_all_templates_have_headers(template_file):
    """
    Property-based test: All templates must have standardized headers.
    
    **Property 11: Standardized Document Headers**
    **Validates: Requirements 8.1**
    """
    if template_file.name == 'dummy.md':
        pytest.skip("No template files found")
    
    if not template_file.exists():
        pytest.skip(f"Template file {template_file} does not exist")
    
    content = template_file.read_text(encoding='utf-8')
    is_german = '/de/' in str(template_file)
    
    has_header, missing_fields = has_standardized_header(content, is_german)
    
    assert has_header, (
        f"Template {template_file.name} is missing required header fields: {missing_fields}"
    )


def test_header_appears_after_title():
    """Test that headers appear immediately after the title."""
    template_files = get_all_template_files()
    
    for template_file in template_files:
        content = template_file.read_text(encoding='utf-8')
        lines = content.split('\n')
        
        # Find title line
        title_idx = -1
        for i, line in enumerate(lines):
            if line.startswith('# '):
                title_idx = i
                break
        
        if title_idx < 0:
            continue
        
        # Check that header starts within next few lines (allowing for blank line)
        header_found = False
        for i in range(title_idx + 1, min(title_idx + 5, len(lines))):
            if lines[i].strip().startswith('**'):
                header_found = True
                break
        
        assert header_found, (
            f"Template {template_file.name} does not have header immediately after title"
        )


def test_header_followed_by_separator():
    """Test that headers are followed by a separator line (---)."""
    template_files = get_all_template_files()
    
    for template_file in template_files:
        content = template_file.read_text(encoding='utf-8')
        
        # Check if there's a separator after the header
        # Pattern: header fields followed by --- separator
        pattern = r'\*\*[^*]+\*\*[^\n]*\n(?:\*\*[^*]+\*\*[^\n]*\n)*\n---'
        
        assert re.search(pattern, content), (
            f"Template {template_file.name} does not have separator (---) after header"
        )


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
