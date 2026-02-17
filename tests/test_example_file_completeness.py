"""
Property-based tests for example file completeness.

Feature: config-separation-and-metadata-unification
Property 17: Example File Completeness

Validates: Requirements 10.2
"""

import pytest
import yaml
from pathlib import Path
from hypothesis import given, strategies as st

# Expected example files
EXPECTED_EXAMPLE_FILES = [
    "config.example.yaml",
    "meta-global.example.yaml",
    "meta-organisation.example.yaml",
    "meta-organisation-roles.example.yaml",
    "meta-handbook.example.yaml"
]

# Required fields for each example file type
REQUIRED_FIELDS = {
    "config.example.yaml": ["data_sources", "defaults"],
    "meta-global.example.yaml": ["source", "version"],
    "meta-organisation.example.yaml": ["name", "address", "web", "phone", "revision"],
    "meta-organisation-roles.example.yaml": [
        "role_CEO", "role_CFO", "role_CTO", "role_CIO", "role_CISO",
        "role_HR_Manager", "role_Risk_Manager", "role_GDPR_Manager",
        "role_IT_Manager", "role_Compliance_Manager", "role_Internal_Auditor",
        "group_IT_Services", "group_DEVOPS", "group_Helpdesk"
    ],
    "meta-handbook.example.yaml": [
        "author", "classification", "status", "type", "templateset_version",
        "revision", "shortname", "longname", "owner", "approver",
        "creationdate", "modifydate", "valid_from", "next_review", "scope"
    ]
}


def test_property_all_example_files_exist():
    """
    Property 17: Example File Completeness (File Existence)
    
    For any installation, all required example configuration files should exist:
    - config.example.yaml
    - meta-global.example.yaml
    - meta-organisation.example.yaml
    - meta-organisation-roles.example.yaml
    - meta-handbook.example.yaml
    
    Validates: Requirements 10.2
    """
    project_root = Path(__file__).parent.parent
    
    for example_file in EXPECTED_EXAMPLE_FILES:
        file_path = project_root / example_file
        assert file_path.exists(), f"Example file missing: {example_file}"
        assert file_path.is_file(), f"Example file is not a file: {example_file}"


def test_property_example_files_have_complete_structure():
    """
    Property 17: Example File Completeness (Structure Completeness)
    
    For any example configuration file, it should contain complete structure
    with all required fields defined.
    
    Validates: Requirements 10.2
    """
    project_root = Path(__file__).parent.parent
    
    for example_file in EXPECTED_EXAMPLE_FILES:
        file_path = project_root / example_file
        
        # Load the YAML file
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
        
        assert data is not None, f"Example file is empty: {example_file}"
        
        # Check required fields
        required_fields = REQUIRED_FIELDS.get(example_file, [])
        for field in required_fields:
            assert field in data, f"Required field '{field}' missing in {example_file}"


def test_property_example_files_have_inline_comments():
    """
    Property 17: Example File Completeness (Inline Comments)
    
    For any example configuration file, it should include inline comments
    explaining each field.
    
    Validates: Requirements 10.2
    """
    project_root = Path(__file__).parent.parent
    
    for example_file in EXPECTED_EXAMPLE_FILES:
        file_path = project_root / example_file
        
        # Read the raw file content
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Check for comments (lines starting with #)
        comment_lines = [line for line in content.split('\n') if line.strip().startswith('#')]
        
        assert len(comment_lines) > 0, f"No comments found in {example_file}"
        
        # Should have substantial comments (at least 5 comment lines)
        assert len(comment_lines) >= 5, f"Insufficient comments in {example_file} (found {len(comment_lines)}, expected at least 5)"


def test_property_example_files_have_realistic_values():
    """
    Property 17: Example File Completeness (Realistic Example Values)
    
    For any example configuration file, it should include realistic example
    values (not just placeholders or empty strings).
    
    Validates: Requirements 10.2
    """
    project_root = Path(__file__).parent.parent
    
    # Files that should have realistic values (not [TODO])
    files_with_realistic_values = [
        "config.example.yaml",
        "meta-global.example.yaml",
        "meta-organisation.example.yaml",
        "meta-organisation-roles.example.yaml",
        "meta-handbook.example.yaml"
    ]
    
    for example_file in files_with_realistic_values:
        file_path = project_root / example_file
        
        # Load the YAML file
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f)
        
        # Check that at least some fields have non-empty, non-[TODO] values
        def has_realistic_values(obj, depth=0):
            """Recursively check for realistic values."""
            if depth > 10:  # Prevent infinite recursion
                return False
            
            if isinstance(obj, dict):
                for value in obj.values():
                    if has_realistic_values(value, depth + 1):
                        return True
            elif isinstance(obj, list):
                for item in obj:
                    if has_realistic_values(item, depth + 1):
                        return True
            elif isinstance(obj, str):
                # Check if it's a realistic value (not empty, not just [TODO])
                if obj and obj != "[TODO]" and len(obj) > 0:
                    return True
            elif obj is not None:
                # Numbers, booleans, etc. are considered realistic
                return True
            
            return False
        
        assert has_realistic_values(data), f"No realistic example values found in {example_file}"


def test_property_example_files_reference_documentation():
    """
    Property 17: Example File Completeness (Documentation References)
    
    For any example configuration file, it should include references to
    documentation for more detailed information.
    
    Validates: Requirements 10.2
    """
    project_root = Path(__file__).parent.parent
    
    # Documentation keywords to look for
    doc_keywords = [
        "documentation",
        "docs/",
        "see",
        "reference",
        "guide",
        "README"
    ]
    
    for example_file in EXPECTED_EXAMPLE_FILES:
        file_path = project_root / example_file
        
        # Read the raw file content
        with open(file_path, 'r') as f:
            content = f.read().lower()
        
        # Check for documentation references
        has_doc_reference = any(keyword in content for keyword in doc_keywords)
        
        assert has_doc_reference, f"No documentation reference found in {example_file}"


def test_property_config_example_has_data_source_references():
    """
    Property 17: Example File Completeness (Config Data Sources)
    
    For config.example.yaml, it should contain complete structure with
    data source references to all metadata files.
    
    Validates: Requirements 10.2
    """
    project_root = Path(__file__).parent.parent
    config_example_path = project_root / "config.example.yaml"
    
    with open(config_example_path, 'r') as f:
        data = yaml.safe_load(f)
    
    # Check data_sources section exists
    assert "data_sources" in data, "data_sources section missing"
    
    # Check required metadata file references
    data_sources = data["data_sources"]
    assert "meta-global" in data_sources, "meta-global reference missing"
    assert "meta-organisation" in data_sources, "meta-organisation reference missing"
    assert "meta-organisation-roles" in data_sources, "meta-organisation-roles reference missing"
    
    # Check that values are file paths
    assert isinstance(data_sources["meta-global"], str), "meta-global should be a string path"
    assert isinstance(data_sources["meta-organisation"], str), "meta-organisation should be a string path"
    assert isinstance(data_sources["meta-organisation-roles"], str), "meta-organisation-roles should be a string path"


def test_property_meta_handbook_example_notes_maintainer_default():
    """
    Property 17: Example File Completeness (Maintainer Default Note)
    
    For meta-handbook.example.yaml, it should include a note that maintainer
    defaults to author if not specified.
    
    Validates: Requirements 10.2
    """
    project_root = Path(__file__).parent.parent
    handbook_example_path = project_root / "meta-handbook.example.yaml"
    
    with open(handbook_example_path, 'r') as f:
        content = f.read().lower()
    
    # Check for maintainer default note
    assert "maintainer" in content, "No mention of maintainer field"
    assert "default" in content, "No mention of default behavior"
    assert "author" in content, "No mention of author field"
    
    # Should mention that maintainer defaults to author
    maintainer_related = any(
        "maintainer" in line and ("default" in line or "author" in line)
        for line in content.split('\n')
    )
    assert maintainer_related, "No clear note about maintainer defaulting to author"


def test_property_roles_example_uses_english_identifiers():
    """
    Property 17: Example File Completeness (English Role Identifiers)
    
    For meta-organisation-roles.example.yaml, all role identifiers should
    use English names (role_CEO, not rolle_CEO).
    
    Validates: Requirements 10.2, 5.4
    """
    project_root = Path(__file__).parent.parent
    roles_example_path = project_root / "meta-organisation-roles.example.yaml"
    
    with open(roles_example_path, 'r') as f:
        data = yaml.safe_load(f)
    
    # Check that all keys use English prefixes
    for key in data.keys():
        # Should start with role_ or group_
        assert key.startswith("role_") or key.startswith("group_"), \
            f"Role identifier '{key}' doesn't use standard prefix"
        
        # Should NOT use German prefixes
        assert not key.startswith("rolle_"), \
            f"Role identifier '{key}' uses German prefix 'rolle_'"
        assert not key.startswith("gruppe_"), \
            f"Role identifier '{key}' uses German prefix 'gruppe_'"


def test_property_example_files_are_valid_yaml():
    """
    Property 17: Example File Completeness (Valid YAML Syntax)
    
    For any example configuration file, it should be valid YAML that can
    be parsed without errors.
    
    Validates: Requirements 10.2
    """
    project_root = Path(__file__).parent.parent
    
    for example_file in EXPECTED_EXAMPLE_FILES:
        file_path = project_root / example_file
        
        # Should be able to parse without errors
        try:
            with open(file_path, 'r') as f:
                data = yaml.safe_load(f)
            assert data is not None, f"Parsed data is None for {example_file}"
        except yaml.YAMLError as e:
            pytest.fail(f"Invalid YAML in {example_file}: {e}")


@given(
    example_file=st.sampled_from(EXPECTED_EXAMPLE_FILES)
)
def test_property_example_file_can_be_copied_and_used(example_file):
    """
    Property 17: Example File Completeness (Usability)
    
    For any example configuration file, it should be in a state where it can
    be copied to the actual filename and used (possibly with customization).
    
    This means:
    - Valid YAML syntax
    - Complete structure
    - Reasonable default values
    
    Validates: Requirements 10.2
    """
    project_root = Path(__file__).parent.parent
    file_path = project_root / example_file
    
    # Should exist and be readable
    assert file_path.exists()
    
    # Should be valid YAML
    with open(file_path, 'r') as f:
        data = yaml.safe_load(f)
    
    assert data is not None
    assert isinstance(data, dict)
    
    # Should have required fields
    required_fields = REQUIRED_FIELDS.get(example_file, [])
    for field in required_fields:
        assert field in data, f"Required field '{field}' missing"


def test_property_example_files_have_header_comments():
    """
    Property 17: Example File Completeness (Header Comments)
    
    For any example configuration file, it should have header comments
    explaining what the file is and how to use it.
    
    Validates: Requirements 10.2
    """
    project_root = Path(__file__).parent.parent
    
    for example_file in EXPECTED_EXAMPLE_FILES:
        file_path = project_root / example_file
        
        # Read first few lines
        with open(file_path, 'r') as f:
            first_lines = [f.readline() for _ in range(10)]
        
        # First line should be a comment
        assert first_lines[0].strip().startswith('#'), \
            f"First line of {example_file} should be a comment"
        
        # Should have multiple comment lines at the start
        comment_count = sum(1 for line in first_lines if line.strip().startswith('#'))
        assert comment_count >= 3, \
            f"Expected at least 3 header comment lines in {example_file}, found {comment_count}"


def test_property_example_files_explain_field_purpose():
    """
    Property 17: Example File Completeness (Field Explanations)
    
    For any example configuration file with multiple fields, comments should
    explain the purpose of each field or section.
    
    Validates: Requirements 10.2
    """
    project_root = Path(__file__).parent.parent
    
    for example_file in EXPECTED_EXAMPLE_FILES:
        file_path = project_root / example_file
        
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Load YAML to get field count
        data = yaml.safe_load(content)
        field_count = len(data) if isinstance(data, dict) else 0
        
        # Count comment lines
        comment_lines = [line for line in content.split('\n') if line.strip().startswith('#')]
        
        # Should have reasonable ratio of comments to fields
        # At least 1 comment per 2 fields (rough heuristic)
        if field_count > 0:
            expected_min_comments = max(5, field_count // 2)
            assert len(comment_lines) >= expected_min_comments, \
                f"Insufficient field explanations in {example_file} " \
                f"({len(comment_lines)} comments for {field_count} fields)"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--hypothesis-show-statistics"])
