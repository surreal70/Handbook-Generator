"""
Property-based tests for bilingual placeholder consistency.

**Property 10: Bilingual Placeholder Consistency**
**Validates: Requirements 7.3**

For any handbook that has both German (de) and English (en) template versions, 
the placeholders used in both language versions should be identical (same English identifiers).
"""

import pytest
from pathlib import Path
from hypothesis import given, strategies as st, settings, HealthCheck
import re
from collections import defaultdict


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


def extract_placeholders(content: str) -> set[str]:
    """Extract all placeholders from content."""
    # Pattern matches {{ placeholder.field }}
    pattern = r'\{\{\s*([a-zA-Z0-9_\-\.]+)\s*\}\}'
    matches = re.findall(pattern, content)
    return set(matches)


def get_bilingual_template_pairs():
    """Get pairs of German and English templates with the same name."""
    templates_dir = Path('templates')
    if not templates_dir.exists():
        return []
    
    # Group templates by framework and filename
    de_templates = defaultdict(dict)
    en_templates = defaultdict(dict)
    
    for template_file in get_all_template_files():
        parts = template_file.parts
        
        # Extract framework and filename
        if 'de' in parts:
            lang_idx = parts.index('de')
            if lang_idx + 1 < len(parts):
                framework = parts[lang_idx + 1]
                filename = template_file.name
                de_templates[framework][filename] = template_file
        elif 'en' in parts:
            lang_idx = parts.index('en')
            if lang_idx + 1 < len(parts):
                framework = parts[lang_idx + 1]
                filename = template_file.name
                en_templates[framework][filename] = template_file
    
    # Find matching pairs
    pairs = []
    for framework in de_templates:
        if framework in en_templates:
            for filename in de_templates[framework]:
                if filename in en_templates[framework]:
                    pairs.append((
                        de_templates[framework][filename],
                        en_templates[framework][filename]
                    ))
    
    return pairs


@pytest.mark.parametrize('de_template,en_template', get_bilingual_template_pairs())
def test_bilingual_templates_have_same_placeholders(de_template, en_template):
    """
    Property 10: Bilingual Placeholder Consistency
    
    For any handbook that has both German and English template versions, 
    the placeholders should be identical.
    """
    de_content = de_template.read_text(encoding='utf-8')
    en_content = en_template.read_text(encoding='utf-8')
    
    de_placeholders = extract_placeholders(de_content)
    en_placeholders = extract_placeholders(en_content)
    
    # Placeholders should be identical
    only_in_de = de_placeholders - en_placeholders
    only_in_en = en_placeholders - de_placeholders
    
    assert de_placeholders == en_placeholders, (
        f"Placeholder mismatch between {de_template.name} (de) and {en_template.name} (en):\n"
        f"Only in German: {only_in_de}\n"
        f"Only in English: {only_in_en}"
    )


@given(st.sampled_from(get_bilingual_template_pairs() or [(Path('dummy.md'), Path('dummy.md'))]))
@settings(
    max_examples=100,
    suppress_health_check=[HealthCheck.function_scoped_fixture],
    deadline=None
)
def test_property_bilingual_placeholder_consistency(template_pair):
    """
    Property-based test: Bilingual templates must use identical placeholders.
    
    **Property 10: Bilingual Placeholder Consistency**
    **Validates: Requirements 7.3**
    """
    de_template, en_template = template_pair
    
    if de_template.name == 'dummy.md':
        pytest.skip("No bilingual template pairs found")
    
    if not de_template.exists() or not en_template.exists():
        pytest.skip(f"Template files do not exist")
    
    de_content = de_template.read_text(encoding='utf-8')
    en_content = en_template.read_text(encoding='utf-8')
    
    de_placeholders = extract_placeholders(de_content)
    en_placeholders = extract_placeholders(en_content)
    
    assert de_placeholders == en_placeholders, (
        f"Placeholder mismatch between {de_template.name} (de) and {en_template.name} (en)"
    )


def test_all_placeholders_use_english_identifiers():
    """Test that all placeholders use English identifiers (not German)."""
    template_files = get_all_template_files()
    
    # German words that should NOT appear in placeholders
    german_words = [
        'organisation',  # Should be 'organisation' (English spelling)
        'dokument',
        'rolle',
        'gruppe',
        'version',
        'datum',
        'autor',
    ]
    
    for template_file in template_files:
        content = template_file.read_text(encoding='utf-8')
        placeholders = extract_placeholders(content)
        
        for placeholder in placeholders:
            placeholder_lower = placeholder.lower()
            
            # Check for German words (but allow 'organisation' which is valid English)
            for german_word in german_words:
                if german_word == 'organisation':
                    continue  # This is valid English
                
                assert german_word not in placeholder_lower, (
                    f"Template {template_file.name} has placeholder with German word: {placeholder}"
                )


def test_placeholders_use_new_format():
    """Test that placeholders use the new format (meta-source.field)."""
    template_files = get_all_template_files()
    
    # Old format patterns that should not exist
    old_patterns = [
        r'\{\{\s*meta\.organization\.',
        r'\{\{\s*meta\.document\.',
        r'\{\{\s*meta\.roles\.',
        r'\{\{\s*meta\.defaults\.',
        r'\{\{\s*metadata\.',
    ]
    
    for template_file in template_files:
        content = template_file.read_text(encoding='utf-8')
        
        for pattern in old_patterns:
            matches = re.findall(pattern, content)
            assert len(matches) == 0, (
                f"Template {template_file.name} uses old placeholder format: {matches}"
            )


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
