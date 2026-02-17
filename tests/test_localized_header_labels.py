"""
Property-based tests for localized header labels.

**Property 12: Localized Header Labels**
**Validates: Requirements 8.2**

For any template file, the document header labels should match the template language 
(German labels for de/ templates, English labels for en/ templates).
"""

import pytest
from pathlib import Path
from hypothesis import given, strategies as st, settings, HealthCheck
import re


# German header labels
GERMAN_LABELS = [
    'Dokument-ID',
    'Genehmigt durch',
    'Klassifizierung',
    'Letzte Aktualisierung'
]

# English header labels
ENGLISH_LABELS = [
    'Document-ID',
    'Approved by',
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


def check_header_language(content: str, is_german: bool) -> tuple[bool, list[str]]:
    """
    Check if header uses correct language labels.
    
    Returns:
        Tuple of (correct_language, wrong_labels)
    """
    expected_labels = GERMAN_LABELS if is_german else ENGLISH_LABELS
    wrong_language_labels = ENGLISH_LABELS if is_german else GERMAN_LABELS
    
    found_wrong_labels = []
    
    for label in wrong_language_labels:
        pattern = rf'\*\*{re.escape(label)}:\*\*'
        if re.search(pattern, content):
            found_wrong_labels.append(label)
    
    return len(found_wrong_labels) == 0, found_wrong_labels


@pytest.mark.parametrize('template_file', get_all_template_files())
def test_template_has_correct_language_labels(template_file):
    """
    Property 12: Localized Header Labels
    
    For any template file, the document header labels should match the template language.
    """
    content = template_file.read_text(encoding='utf-8')
    
    # Determine language from path
    is_german = '/de/' in str(template_file)
    
    correct_language, wrong_labels = check_header_language(content, is_german)
    
    language = "German" if is_german else "English"
    wrong_language = "English" if is_german else "German"
    
    assert correct_language, (
        f"Template {template_file} should use {language} labels but contains "
        f"{wrong_language} labels: {wrong_labels}"
    )


@given(st.sampled_from(get_all_template_files() or [Path('dummy.md')]))
@settings(
    max_examples=100,
    suppress_health_check=[HealthCheck.function_scoped_fixture],
    deadline=None
)
def test_property_templates_use_correct_language(template_file):
    """
    Property-based test: Templates must use labels matching their language directory.
    
    **Property 12: Localized Header Labels**
    **Validates: Requirements 8.2**
    """
    if template_file.name == 'dummy.md':
        pytest.skip("No template files found")
    
    if not template_file.exists():
        pytest.skip(f"Template file {template_file} does not exist")
    
    content = template_file.read_text(encoding='utf-8')
    is_german = '/de/' in str(template_file)
    
    correct_language, wrong_labels = check_header_language(content, is_german)
    
    language = "German" if is_german else "English"
    wrong_language = "English" if is_german else "German"
    
    assert correct_language, (
        f"Template {template_file.name} should use {language} labels but contains "
        f"{wrong_language} labels: {wrong_labels}"
    )


def test_german_templates_use_german_labels():
    """Test that all German templates use German labels."""
    templates_dir = Path('templates/de')
    if not templates_dir.exists():
        pytest.skip("German templates directory not found")
    
    for template_file in get_all_template_files():
        if '/de/' not in str(template_file):
            continue
        
        content = template_file.read_text(encoding='utf-8')
        
        # Check for German-specific labels
        assert 'Dokument-ID' in content or '**Dokument-ID:**' in content, (
            f"German template {template_file.name} should use 'Dokument-ID'"
        )


def test_english_templates_use_english_labels():
    """Test that all English templates use English labels."""
    templates_dir = Path('templates/en')
    if not templates_dir.exists():
        pytest.skip("English templates directory not found")
    
    for template_file in get_all_template_files():
        if '/en/' not in str(template_file):
            continue
        
        content = template_file.read_text(encoding='utf-8')
        
        # Check for English-specific labels
        assert 'Document-ID' in content or '**Document-ID:**' in content, (
            f"English template {template_file.name} should use 'Document-ID'"
        )


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
