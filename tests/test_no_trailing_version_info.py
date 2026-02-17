"""
Property-based tests for no trailing version information.

**Property 13: No Trailing Version Information**
**Validates: Requirements 8.3**

For any template file, there should be no version information section at the end 
of the file (version info is now in the header).
"""

import pytest
from pathlib import Path
from hypothesis import given, strategies as st, settings, HealthCheck
import re


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


def has_trailing_version_info(content: str) -> tuple[bool, str]:
    """
    Check if content has trailing version information.
    
    Returns:
        Tuple of (has_trailing_version, matched_pattern)
    """
    # Patterns that indicate trailing version information
    patterns = [
        r'\*\*Dokumenthistorie:\*\*',
        r'\*\*Document History:\*\*',
        r'\*\*Version History:\*\*',
        r'\*\*Versionshistorie:\*\*',
        r'##\s+Dokumenthistorie',
        r'##\s+Document History',
        r'##\s+Version History',
        r'##\s+Versionshistorie',
    ]
    
    # Check last 500 characters of the file for version history
    tail = content[-500:] if len(content) > 500 else content
    
    for pattern in patterns:
        match = re.search(pattern, tail, re.IGNORECASE)
        if match:
            return True, match.group(0)
    
    return False, ""


@pytest.mark.parametrize('template_file', get_all_template_files())
def test_template_has_no_trailing_version_info(template_file):
    """
    Property 13: No Trailing Version Information
    
    For any template file, there should be no version information section at 
    the end of the file.
    """
    content = template_file.read_text(encoding='utf-8')
    
    has_trailing, matched_pattern = has_trailing_version_info(content)
    
    assert not has_trailing, (
        f"Template {template_file} has trailing version information: '{matched_pattern}'. "
        f"Version info should be in the header only."
    )


@given(st.sampled_from(get_all_template_files() or [Path('dummy.md')]))
@settings(
    max_examples=100,
    suppress_health_check=[HealthCheck.function_scoped_fixture],
    deadline=None
)
def test_property_no_trailing_version_sections(template_file):
    """
    Property-based test: Templates must not have trailing version information.
    
    **Property 13: No Trailing Version Information**
    **Validates: Requirements 8.3**
    """
    if template_file.name == 'dummy.md':
        pytest.skip("No template files found")
    
    if not template_file.exists():
        pytest.skip(f"Template file {template_file} does not exist")
    
    content = template_file.read_text(encoding='utf-8')
    
    has_trailing, matched_pattern = has_trailing_version_info(content)
    
    assert not has_trailing, (
        f"Template {template_file.name} has trailing version information: '{matched_pattern}'"
    )


def test_version_info_in_header_not_at_end():
    """Test that version/revision info is in header, not at end of file."""
    template_files = get_all_template_files()
    
    for template_file in template_files:
        content = template_file.read_text(encoding='utf-8')
        lines = content.split('\n')
        
        # Check that Revision/Version appears in first 20 lines (header area)
        header_area = '\n'.join(lines[:20])
        
        # Should have revision in header
        assert ('**Revision:**' in header_area or 
                '**Version:**' in header_area), (
            f"Template {template_file.name} should have Revision/Version in header"
        )
        
        # Should NOT have version history at the end
        tail_area = '\n'.join(lines[-20:])
        assert 'Dokumenthistorie' not in tail_area, (
            f"Template {template_file.name} should not have Dokumenthistorie at end"
        )
        assert 'Document History' not in tail_area, (
            f"Template {template_file.name} should not have Document History at end"
        )


def test_no_version_tables_at_end():
    """Test that there are no version history tables at the very end of templates."""
    template_files = get_all_template_files()
    
    for template_file in template_files:
        content = template_file.read_text(encoding='utf-8')
        
        # Skip templates that are specifically about document control/versioning
        # These legitimately contain version history as part of their content
        if 'Dokumentenlenkung' in template_file.name or 'Document_Control' in template_file.name:
            continue
        
        # Check last 300 characters for version history sections
        # This catches trailing version info but not content-related version tables
        tail = content[-300:] if len(content) > 300 else content
        
        # Version history at the very end (after <!-- End of template --> or at EOF)
        version_history_patterns = [
            r'##\s+(?:Versionshistorie|Version History|Dokumenthistorie|Document History)',
            r'\*\*(?:Versionshistorie|Version History|Dokumenthistorie|Document History):\*\*',
        ]
        
        for pattern in version_history_patterns:
            assert not re.search(pattern, tail, re.IGNORECASE), (
                f"Template {template_file.name} has version history section at the end"
            )


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
