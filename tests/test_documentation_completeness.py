"""
Property-based tests for documentation completeness.

Feature: config-separation-and-metadata-unification
Property 18: Documentation Completeness

Validates: Requirements 10.3
"""

import pytest
from pathlib import Path
from hypothesis import given, strategies as st

# Expected documentation files
EXPECTED_DOCUMENTATION_FILES = [
    "docs/CONFIGURATION_REFERENCE.md",
    "docs/PLACEHOLDER_REFERENCE.md",
    "docs/TEMPLATE_HEADER_SPECIFICATION.md"
]

# Required sections for each documentation file
REQUIRED_SECTIONS = {
    "docs/CONFIGURATION_REFERENCE.md": [
        "config.yaml",
        "meta-global.yaml",
        "meta-organisation.yaml",
        "meta-organisation-roles.yaml",
        "meta-handbook.yaml",
        "Default Values",
        "Validation",
        "Error Handling",
        "Best Practices",
        "Troubleshooting"
    ],
    "docs/PLACEHOLDER_REFERENCE.md": [
        "meta-global",
        "meta-organisation",
        "meta-organisation-roles",
        "meta-handbook",
        "Migration from Old Format",
        "Common Patterns",
        "Troubleshooting",
        "Best Practices"
    ],
    "docs/TEMPLATE_HEADER_SPECIFICATION.md": [
        "Document-ID",
        "Organisation",
        "Owner",
        "Approved by",
        "Revision",
        "Author",
        "Status",
        "Classification",
        "Last Update",
        "German Templates",
        "English Templates",
        "Validation",
        "Best Practices"
    ]
}


def test_property_all_documentation_files_exist():
    """
    Property 18: Documentation Completeness (File Existence)
    
    For any installation, all required documentation files should exist:
    - CONFIGURATION_REFERENCE.md
    - PLACEHOLDER_REFERENCE.md
    - TEMPLATE_HEADER_SPECIFICATION.md
    
    Validates: Requirements 10.3
    """
    project_root = Path(__file__).parent.parent
    
    for doc_file in EXPECTED_DOCUMENTATION_FILES:
        file_path = project_root / doc_file
        assert file_path.exists(), f"Documentation file missing: {doc_file}"
        assert file_path.is_file(), f"Documentation file is not a file: {doc_file}"


def test_property_documentation_files_have_required_sections():
    """
    Property 18: Documentation Completeness (Required Sections)
    
    For any documentation file, it should contain all required sections
    as specified in the requirements.
    
    Validates: Requirements 10.3
    """
    project_root = Path(__file__).parent.parent
    
    for doc_file in EXPECTED_DOCUMENTATION_FILES:
        file_path = project_root / doc_file
        
        # Read the documentation file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for required sections
        required_sections = REQUIRED_SECTIONS.get(doc_file, [])
        for section in required_sections:
            assert section in content, \
                f"Required section '{section}' missing in {doc_file}"


def test_property_configuration_reference_documents_all_files():
    """
    Property 18: Documentation Completeness (Configuration Files)
    
    CONFIGURATION_REFERENCE.md should document all configuration files:
    - config.yaml
    - meta-global.yaml
    - meta-organisation.yaml
    - meta-organisation-roles.yaml
    - meta-handbook.yaml
    
    Validates: Requirements 10.3
    """
    project_root = Path(__file__).parent.parent
    config_ref_path = project_root / "docs/CONFIGURATION_REFERENCE.md"
    
    with open(config_ref_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for all configuration files
    config_files = [
        "config.yaml",
        "meta-global.yaml",
        "meta-organisation.yaml",
        "meta-organisation-roles.yaml",
        "meta-handbook.yaml"
    ]
    
    for config_file in config_files:
        assert config_file in content, \
            f"Configuration file '{config_file}' not documented in CONFIGURATION_REFERENCE.md"


def test_property_configuration_reference_has_field_descriptions():
    """
    Property 18: Documentation Completeness (Field Descriptions)
    
    CONFIGURATION_REFERENCE.md should include field descriptions and
    valid values for all configuration fields.
    
    Validates: Requirements 10.3
    """
    project_root = Path(__file__).parent.parent
    config_ref_path = project_root / "docs/CONFIGURATION_REFERENCE.md"
    
    with open(config_ref_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for field description keywords
    description_keywords = [
        "Description:",
        "Type:",
        "Default:",
        "Example:",
        "Valid Values:",
        "Usage:"
    ]
    
    found_keywords = sum(1 for keyword in description_keywords if keyword in content)
    
    # Should have most of these keywords (at least 4 out of 6)
    assert found_keywords >= 4, \
        f"Insufficient field descriptions in CONFIGURATION_REFERENCE.md " \
        f"(found {found_keywords} out of {len(description_keywords)} keywords)"


def test_property_configuration_reference_has_default_values_table():
    """
    Property 18: Documentation Completeness (Default Values Table)
    
    CONFIGURATION_REFERENCE.md should include a default values table
    showing defaults for all configuration fields.
    
    Validates: Requirements 10.3
    """
    project_root = Path(__file__).parent.parent
    config_ref_path = project_root / "docs/CONFIGURATION_REFERENCE.md"
    
    with open(config_ref_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for default values section
    assert "Default Values" in content, "Default Values section missing"
    
    # Check for table markers (markdown tables use |)
    lines = content.split('\n')
    table_lines = [line for line in lines if '|' in line]
    
    assert len(table_lines) > 0, "No tables found in CONFIGURATION_REFERENCE.md"
    
    # Should mention common default values
    default_keywords = ["[TODO]", "0", "HandBook Generator", "1.0.0"]
    found_defaults = sum(1 for keyword in default_keywords if keyword in content)
    
    assert found_defaults >= 2, \
        f"Default values not adequately documented (found {found_defaults} out of {len(default_keywords)})"


def test_property_configuration_reference_has_examples():
    """
    Property 18: Documentation Completeness (Examples)
    
    CONFIGURATION_REFERENCE.md should include examples for each
    configuration file.
    
    Validates: Requirements 10.3
    """
    project_root = Path(__file__).parent.parent
    config_ref_path = project_root / "docs/CONFIGURATION_REFERENCE.md"
    
    with open(config_ref_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for example keywords
    example_keywords = ["Example:", "example", "```yaml", "```"]
    found_examples = sum(1 for keyword in example_keywords if keyword in content)
    
    assert found_examples >= 3, \
        f"Insufficient examples in CONFIGURATION_REFERENCE.md " \
        f"(found {found_examples} example indicators)"
    
    # Should have YAML code blocks
    assert "```yaml" in content, "No YAML examples found"


def test_property_placeholder_reference_documents_all_sources():
    """
    Property 18: Documentation Completeness (Placeholder Sources)
    
    PLACEHOLDER_REFERENCE.md should document all placeholder sources:
    - meta-global
    - meta-organisation
    - meta-organisation-roles
    - meta-handbook
    
    Validates: Requirements 10.3
    """
    project_root = Path(__file__).parent.parent
    placeholder_ref_path = project_root / "docs/PLACEHOLDER_REFERENCE.md"
    
    with open(placeholder_ref_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for all placeholder sources
    placeholder_sources = [
        "meta-global",
        "meta-organisation",
        "meta-organisation-roles",
        "meta-handbook"
    ]
    
    for source in placeholder_sources:
        assert source in content, \
            f"Placeholder source '{source}' not documented in PLACEHOLDER_REFERENCE.md"


def test_property_placeholder_reference_has_usage_examples():
    """
    Property 18: Documentation Completeness (Usage Examples)
    
    PLACEHOLDER_REFERENCE.md should include usage examples for
    placeholders.
    
    Validates: Requirements 10.3
    """
    project_root = Path(__file__).parent.parent
    placeholder_ref_path = project_root / "docs/PLACEHOLDER_REFERENCE.md"
    
    with open(placeholder_ref_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for usage examples
    assert "Example:" in content or "example" in content.lower(), \
        "No usage examples found in PLACEHOLDER_REFERENCE.md"
    
    # Should have markdown code blocks
    assert "```markdown" in content or "```" in content, \
        "No code examples found in PLACEHOLDER_REFERENCE.md"
    
    # Should show placeholder syntax
    assert "{{ meta-" in content, \
        "No placeholder syntax examples found"


def test_property_placeholder_reference_has_migration_mapping():
    """
    Property 18: Documentation Completeness (Migration Mapping)
    
    PLACEHOLDER_REFERENCE.md should include mapping from old to new
    placeholder format.
    
    Validates: Requirements 10.3
    """
    project_root = Path(__file__).parent.parent
    placeholder_ref_path = project_root / "docs/PLACEHOLDER_REFERENCE.md"
    
    with open(placeholder_ref_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for migration section
    assert "Migration" in content or "Old Format" in content, \
        "Migration section missing in PLACEHOLDER_REFERENCE.md"
    
    # Should have mapping indicators
    mapping_indicators = ["→", "->", "Old", "New", "|"]
    found_indicators = sum(1 for indicator in mapping_indicators if indicator in content)
    
    assert found_indicators >= 2, \
        f"Migration mapping not adequately documented (found {found_indicators} indicators)"


def test_property_template_header_spec_documents_all_fields():
    """
    Property 18: Documentation Completeness (Header Fields)
    
    TEMPLATE_HEADER_SPECIFICATION.md should document all required
    header fields.
    
    Validates: Requirements 10.3
    """
    project_root = Path(__file__).parent.parent
    header_spec_path = project_root / "docs/TEMPLATE_HEADER_SPECIFICATION.md"
    
    with open(header_spec_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for all required header fields
    required_fields = [
        "Document-ID",
        "Organisation",
        "Owner",
        "Approved by",
        "Revision",
        "Author",
        "Status",
        "Classification",
        "Last Update"
    ]
    
    for field in required_fields:
        assert field in content, \
            f"Header field '{field}' not documented in TEMPLATE_HEADER_SPECIFICATION.md"


def test_property_template_header_spec_has_language_variations():
    """
    Property 18: Documentation Completeness (Language Variations)
    
    TEMPLATE_HEADER_SPECIFICATION.md should document language-specific
    variations for German and English templates.
    
    Validates: Requirements 10.3
    """
    project_root = Path(__file__).parent.parent
    header_spec_path = project_root / "docs/TEMPLATE_HEADER_SPECIFICATION.md"
    
    with open(header_spec_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for language-specific sections
    assert "German" in content, "German templates not documented"
    assert "English" in content, "English templates not documented"
    
    # Check for German labels
    german_labels = ["Dokument-ID", "Genehmigt durch", "Klassifizierung", "Letzte Aktualisierung"]
    found_german = sum(1 for label in german_labels if label in content)
    
    assert found_german >= 2, \
        f"German labels not adequately documented (found {found_german} out of {len(german_labels)})"


def test_property_template_header_spec_has_examples():
    """
    Property 18: Documentation Completeness (Header Examples)
    
    TEMPLATE_HEADER_SPECIFICATION.md should include examples for
    German and English template headers.
    
    Validates: Requirements 10.3
    """
    project_root = Path(__file__).parent.parent
    header_spec_path = project_root / "docs/TEMPLATE_HEADER_SPECIFICATION.md"
    
    with open(header_spec_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for examples
    assert "Example:" in content or "example" in content.lower(), \
        "No examples found in TEMPLATE_HEADER_SPECIFICATION.md"
    
    # Should have markdown code blocks
    assert "```markdown" in content or "```" in content, \
        "No code examples found"
    
    # Should show both German and English examples
    assert "Dokument-ID" in content, "No German example found"
    assert "Document-ID" in content, "No English example found"


def test_property_documentation_has_troubleshooting_sections():
    """
    Property 18: Documentation Completeness (Troubleshooting)
    
    For any documentation file, it should include a troubleshooting
    section with common issues and solutions.
    
    Validates: Requirements 10.3
    """
    project_root = Path(__file__).parent.parent
    
    for doc_file in EXPECTED_DOCUMENTATION_FILES:
        file_path = project_root / doc_file
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for troubleshooting section
        troubleshooting_keywords = [
            "Troubleshooting",
            "Common Issues",
            "Problems",
            "Solutions",
            "Problem:",
            "Solution:"
        ]
        
        found_keywords = sum(1 for keyword in troubleshooting_keywords if keyword in content)
        
        assert found_keywords >= 1, \
            f"No troubleshooting section found in {doc_file}"


def test_property_documentation_has_best_practices():
    """
    Property 18: Documentation Completeness (Best Practices)
    
    For any documentation file, it should include best practices
    or recommendations.
    
    Validates: Requirements 10.3
    """
    project_root = Path(__file__).parent.parent
    
    for doc_file in EXPECTED_DOCUMENTATION_FILES:
        file_path = project_root / doc_file
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for best practices section
        best_practice_keywords = [
            "Best Practices",
            "Recommendations",
            "Guidelines",
            "Tips",
            "Should",
            "Recommended"
        ]
        
        found_keywords = sum(1 for keyword in best_practice_keywords if keyword in content)
        
        assert found_keywords >= 2, \
            f"Insufficient best practices in {doc_file} " \
            f"(found {found_keywords} indicators)"


def test_property_documentation_files_are_markdown():
    """
    Property 18: Documentation Completeness (Markdown Format)
    
    For any documentation file, it should be in Markdown format with
    proper structure (headings, lists, code blocks).
    
    Validates: Requirements 10.3
    """
    project_root = Path(__file__).parent.parent
    
    for doc_file in EXPECTED_DOCUMENTATION_FILES:
        file_path = project_root / doc_file
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for markdown elements
        assert content.startswith('#'), f"{doc_file} should start with a heading"
        
        # Should have multiple headings
        heading_count = content.count('\n#')
        assert heading_count >= 5, \
            f"Insufficient structure in {doc_file} (found {heading_count} headings)"
        
        # Should have lists or code blocks
        has_lists = '-' in content or '*' in content or '1.' in content
        has_code_blocks = '```' in content
        
        assert has_lists or has_code_blocks, \
            f"No lists or code blocks found in {doc_file}"


def test_property_documentation_has_cross_references():
    """
    Property 18: Documentation Completeness (Cross-References)
    
    Documentation files should reference each other for related
    information (See Also sections).
    
    Validates: Requirements 10.3
    """
    project_root = Path(__file__).parent.parent
    
    # Check that at least some docs reference other docs
    cross_references_found = 0
    
    for doc_file in EXPECTED_DOCUMENTATION_FILES:
        file_path = project_root / doc_file
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for references to other documentation files
        other_docs = [d for d in EXPECTED_DOCUMENTATION_FILES if d != doc_file]
        
        for other_doc in other_docs:
            doc_name = Path(other_doc).name
            if doc_name in content:
                cross_references_found += 1
                break
    
    # At least 2 out of 3 docs should reference other docs
    assert cross_references_found >= 2, \
        f"Insufficient cross-references between documentation files " \
        f"(found {cross_references_found} out of {len(EXPECTED_DOCUMENTATION_FILES)})"


def test_property_documentation_is_comprehensive():
    """
    Property 18: Documentation Completeness (Comprehensiveness)
    
    For any documentation file, it should be comprehensive with
    substantial content (not just stubs).
    
    Validates: Requirements 10.3
    """
    project_root = Path(__file__).parent.parent
    
    # Minimum expected sizes (in characters) for comprehensive documentation
    min_sizes = {
        "docs/CONFIGURATION_REFERENCE.md": 10000,  # Should be detailed
        "docs/PLACEHOLDER_REFERENCE.md": 8000,     # Should list all placeholders
        "docs/TEMPLATE_HEADER_SPECIFICATION.md": 6000  # Should have examples and rules
    }
    
    for doc_file in EXPECTED_DOCUMENTATION_FILES:
        file_path = project_root / doc_file
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        min_size = min_sizes.get(doc_file, 5000)
        actual_size = len(content)
        
        assert actual_size >= min_size, \
            f"{doc_file} is too short ({actual_size} chars, expected at least {min_size})"


@given(
    doc_file=st.sampled_from(EXPECTED_DOCUMENTATION_FILES)
)
def test_property_documentation_file_is_readable(doc_file):
    """
    Property 18: Documentation Completeness (Readability)
    
    For any documentation file, it should be readable and well-structured
    with clear headings and sections.
    
    Validates: Requirements 10.3
    """
    project_root = Path(__file__).parent.parent
    file_path = project_root / doc_file
    
    # Should exist and be readable
    assert file_path.exists()
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Should not be empty
    assert len(content) > 0
    
    # Should have proper structure
    assert content.startswith('#'), "Should start with a heading"
    
    # Should have multiple sections
    section_count = content.count('\n## ')
    assert section_count >= 3, \
        f"Insufficient sections in {doc_file} (found {section_count})"


def test_property_documentation_has_table_of_contents_or_overview():
    """
    Property 18: Documentation Completeness (Navigation)
    
    Documentation files should have an overview or table of contents
    to help users navigate.
    
    Validates: Requirements 10.3
    """
    project_root = Path(__file__).parent.parent
    
    for doc_file in EXPECTED_DOCUMENTATION_FILES:
        file_path = project_root / doc_file
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check for overview or navigation aids
        navigation_keywords = [
            "Overview",
            "Table of Contents",
            "Contents",
            "## ",  # Multiple sections serve as navigation
        ]
        
        found_navigation = sum(1 for keyword in navigation_keywords if keyword in content)
        
        assert found_navigation >= 2, \
            f"Insufficient navigation aids in {doc_file}"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--hypothesis-show-statistics"])
