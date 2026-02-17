"""
Property-based tests for metadata loader default values and validation.

Feature: config-separation-and-metadata-unification
Property 3: Default Values for Missing Configuration
Property 4: Configuration Validation
Property 14: English Role Identifiers

Validates: Requirements 1.3, 3.2, 4.2, 5.2, 6.5, 5.4, 1.4, 9.1, 9.2
"""

import pytest
import tempfile
import yaml
from pathlib import Path
from hypothesis import given, strategies as st, assume

from src.metadata_loader import MetadataLoader
from src.unified_metadata import (
    GlobalMetadata,
    OrganisationMetadata,
    RolesMetadata,
    HandbookMetadata,
    UnifiedMetadata
)


@given(
    config_dict=st.one_of(
        st.none(),
        st.dictionaries(
            st.sampled_from(['meta-global', 'meta-organisation', 'meta-organisation-roles']),
            st.text(min_size=1, max_size=50),
            max_size=3
        )
    )
)
def test_property_default_values_for_missing_global_metadata(config_dict):
    """
    Property 3: Default Values for Missing Configuration (Global Metadata)
    
    For any missing meta-global.yaml file, the system should use predefined
    default values:
    - source: "HandBook Generator"
    - version: "1.0.0"
    
    Validates: Requirements 1.3, 3.2
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        
        # Create loader with non-existent file paths
        loader = MetadataLoader(config_dict)
        loader.meta_global_path = tmpdir_path / "nonexistent-global.yaml"
        
        # Load global metadata (file doesn't exist)
        global_meta = loader._load_global_metadata()
        
        # Verify defaults are applied
        assert global_meta.source == "HandBook Generator"
        assert global_meta.version == "1.0.0"
        assert isinstance(global_meta, GlobalMetadata)


@given(
    config_dict=st.one_of(
        st.none(),
        st.dictionaries(
            st.sampled_from(['meta-global', 'meta-organisation', 'meta-organisation-roles']),
            st.text(min_size=1, max_size=50),
            max_size=3
        )
    )
)
def test_property_default_values_for_missing_organisation_metadata(config_dict):
    """
    Property 3: Default Values for Missing Configuration (Organisation Metadata)
    
    For any missing meta-organisation.yaml file, the system should use predefined
    default values:
    - name: "[TODO]"
    - address: "[TODO]"
    - web: "[TODO]"
    - phone: "[TODO]"
    - revision: 0
    
    Validates: Requirements 1.3, 4.2
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        
        # Create loader with non-existent file paths
        loader = MetadataLoader(config_dict)
        loader.meta_org_path = tmpdir_path / "nonexistent-org.yaml"
        
        # Load organisation metadata (file doesn't exist)
        org_meta = loader._load_organisation_metadata()
        
        # Verify defaults are applied
        assert org_meta.name == "[TODO]"
        assert org_meta.address == "[TODO]"
        assert org_meta.web == "[TODO]"
        assert org_meta.phone == "[TODO]"
        assert org_meta.revision == 0
        assert isinstance(org_meta, OrganisationMetadata)


@given(
    config_dict=st.one_of(
        st.none(),
        st.dictionaries(
            st.sampled_from(['meta-global', 'meta-organisation', 'meta-organisation-roles']),
            st.text(min_size=1, max_size=50),
            max_size=3
        )
    )
)
def test_property_default_values_for_missing_roles_metadata(config_dict):
    """
    Property 3: Default Values for Missing Configuration (Roles Metadata)
    
    For any missing meta-organisation-roles.yaml file, the system should use
    predefined default values: all role fields default to "[TODO]"
    
    Validates: Requirements 1.3, 5.2
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        
        # Create loader with non-existent file paths
        loader = MetadataLoader(config_dict)
        loader.meta_roles_path = tmpdir_path / "nonexistent-roles.yaml"
        
        # Load roles metadata (file doesn't exist)
        roles_meta = loader._load_roles_metadata()
        
        # Verify defaults are applied for all roles
        assert roles_meta.role_CEO == "[TODO]"
        assert roles_meta.role_CFO == "[TODO]"
        assert roles_meta.role_CTO == "[TODO]"
        assert roles_meta.role_CIO == "[TODO]"
        assert roles_meta.role_CISO == "[TODO]"
        assert roles_meta.role_HR_Manager == "[TODO]"
        assert roles_meta.role_Risk_Manager == "[TODO]"
        assert roles_meta.role_GDPR_Manager == "[TODO]"
        assert roles_meta.role_IT_Manager == "[TODO]"
        assert roles_meta.role_Compliance_Manager == "[TODO]"
        assert roles_meta.role_Internal_Auditor == "[TODO]"
        assert roles_meta.group_IT_Services == "[TODO]"
        assert roles_meta.group_DEVOPS == "[TODO]"
        assert roles_meta.group_Helpdesk == "[TODO]"
        assert isinstance(roles_meta, RolesMetadata)


@given(
    handbook_dir=st.text(min_size=1, max_size=20, alphabet=st.characters(whitelist_categories=('L', 'N')))
)
def test_property_default_values_for_missing_handbook_metadata(handbook_dir):
    """
    Property 3: Default Values for Missing Configuration (Handbook Metadata)
    
    For any missing meta-handbook.yaml file, the system should use predefined
    default values: all fields default to "[TODO]", revision=0, maintainer=author
    
    Validates: Requirements 1.3, 6.5
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        handbook_path = tmpdir_path / handbook_dir
        handbook_path.mkdir(exist_ok=True)
        
        # Create loader
        loader = MetadataLoader({})
        
        # Load handbook metadata (file doesn't exist)
        handbook_meta = loader.load_handbook_metadata(handbook_path)
        
        # Verify defaults are applied
        assert handbook_meta.author == "[TODO]"
        assert handbook_meta.classification == "[TODO]"
        assert handbook_meta.status == "[TODO]"
        assert handbook_meta.type == "[TODO]"
        # Check version is at least 0.2
        version_parts = handbook_meta.templateset_version.split('.')
        assert len(version_parts) >= 2
        assert int(version_parts[0]) >= 0
        assert int(version_parts[1]) >= 2
        assert handbook_meta.revision == 0
        assert handbook_meta.shortname == "[TODO]"
        assert handbook_meta.longname == "[TODO]"
        assert handbook_meta.maintainer == "[TODO]"  # Defaults to author
        assert handbook_meta.owner == "[TODO]"
        assert handbook_meta.approver == "[TODO]"
        assert handbook_meta.creationdate == "[TODO]"
        assert handbook_meta.modifydate == "[TODO]"
        assert handbook_meta.valid_from == "[TODO]"
        assert handbook_meta.next_review == "[TODO]"
        assert handbook_meta.scope == "[TODO]"
        assert isinstance(handbook_meta, HandbookMetadata)


@given(
    source=st.text(min_size=1, max_size=50),
    version=st.text(min_size=1, max_size=20)
)
def test_property_loaded_values_override_defaults_global(source, version):
    """
    Property: Loaded values override defaults (Global Metadata)
    
    For any valid meta-global.yaml file with values, those values should
    override the default values.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        meta_global_path = tmpdir_path / "meta-global.yaml"
        
        # Write test data
        with open(meta_global_path, 'w') as f:
            yaml.dump({'source': source, 'version': version}, f)
        
        # Create loader
        loader = MetadataLoader({})
        loader.meta_global_path = meta_global_path
        
        # Load global metadata
        global_meta = loader._load_global_metadata()
        
        # Verify loaded values are used
        assert global_meta.source == source
        assert global_meta.version == version


@given(
    name=st.text(min_size=1, max_size=50),
    address=st.text(min_size=1, max_size=100),
    web=st.text(min_size=1, max_size=50),
    phone=st.text(min_size=1, max_size=30),
    revision=st.integers(min_value=0, max_value=1000)
)
def test_property_loaded_values_override_defaults_organisation(name, address, web, phone, revision):
    """
    Property: Loaded values override defaults (Organisation Metadata)
    
    For any valid meta-organisation.yaml file with values, those values should
    override the default values.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        meta_org_path = tmpdir_path / "meta-organisation.yaml"
        
        # Write test data
        with open(meta_org_path, 'w') as f:
            yaml.dump({
                'name': name,
                'address': address,
                'web': web,
                'phone': phone,
                'revision': revision
            }, f)
        
        # Create loader
        loader = MetadataLoader({})
        loader.meta_org_path = meta_org_path
        
        # Load organisation metadata
        org_meta = loader._load_organisation_metadata()
        
        # Verify loaded values are used
        assert org_meta.name == name
        assert org_meta.address == address
        assert org_meta.web == web
        assert org_meta.phone == phone
        assert org_meta.revision == revision


def test_property_english_role_identifiers_validation():
    """
    Property 14: English Role Identifiers
    
    For any meta-organisation-roles.yaml file, all role field names should use
    English identifiers (role_CEO, role_CIO, etc., not rolle_CEO, rolle_CIO).
    
    The system should detect and reject German role prefixes.
    
    Validates: Requirements 5.4
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        meta_roles_path = tmpdir_path / "meta-organisation-roles.yaml"
        
        # Test case 1: German role prefix "rolle_"
        with open(meta_roles_path, 'w') as f:
            yaml.dump({'rolle_CEO': 'John Doe'}, f)
        
        loader = MetadataLoader({})
        loader.meta_roles_path = meta_roles_path
        
        with pytest.raises(ValueError, match="Non-English role identifier detected.*rolle_CEO"):
            loader._load_roles_metadata()
        
        # Test case 2: German group prefix "gruppe_"
        with open(meta_roles_path, 'w') as f:
            yaml.dump({'gruppe_IT': 'IT Team'}, f)
        
        loader = MetadataLoader({})
        loader.meta_roles_path = meta_roles_path
        
        with pytest.raises(ValueError, match="Non-English role identifier detected.*gruppe_IT"):
            loader._load_roles_metadata()
        
        # Test case 3: Valid English identifiers should work
        with open(meta_roles_path, 'w') as f:
            yaml.dump({
                'role_CEO': 'John Doe',
                'role_CIO': 'Jane Smith',
                'group_IT_Services': 'IT Team'
            }, f)
        
        loader = MetadataLoader({})
        loader.meta_roles_path = meta_roles_path
        
        # Should not raise an exception
        roles_meta = loader._load_roles_metadata()
        assert roles_meta.role_CEO == 'John Doe'
        assert roles_meta.role_CIO == 'Jane Smith'
        assert roles_meta.group_IT_Services == 'IT Team'


@given(
    role_values=st.dictionaries(
        st.sampled_from([
            'role_CEO', 'role_CFO', 'role_CTO', 'role_CIO', 'role_CISO',
            'role_HR_Manager', 'role_Risk_Manager', 'role_GDPR_Manager',
            'role_IT_Manager', 'role_Compliance_Manager', 'role_Internal_Auditor',
            'group_IT_Services', 'group_DEVOPS', 'group_Helpdesk'
        ]),
        st.text(min_size=1, max_size=50),
        min_size=1,
        max_size=14
    )
)
def test_property_partial_role_configuration_uses_defaults(role_values):
    """
    Property: Partial role configuration uses defaults for missing fields.
    
    For any meta-organisation-roles.yaml file with only some roles defined,
    the missing roles should use default "[TODO]" values.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        meta_roles_path = tmpdir_path / "meta-organisation-roles.yaml"
        
        # Write partial role data
        with open(meta_roles_path, 'w') as f:
            yaml.dump(role_values, f)
        
        # Create loader
        loader = MetadataLoader({})
        loader.meta_roles_path = meta_roles_path
        
        # Load roles metadata
        roles_meta = loader._load_roles_metadata()
        
        # Verify loaded values are used
        for role_key, role_value in role_values.items():
            assert getattr(roles_meta, role_key) == role_value
        
        # Verify missing roles have defaults
        all_roles = [
            'role_CEO', 'role_CFO', 'role_CTO', 'role_CIO', 'role_CISO',
            'role_HR_Manager', 'role_Risk_Manager', 'role_GDPR_Manager',
            'role_IT_Manager', 'role_Compliance_Manager', 'role_Internal_Auditor',
            'group_IT_Services', 'group_DEVOPS', 'group_Helpdesk'
        ]
        for role_key in all_roles:
            if role_key not in role_values:
                assert getattr(roles_meta, role_key) == "[TODO]"


def test_property_unified_metadata_assembly_with_defaults():
    """
    Property: Unified metadata assembly works with all defaults.
    
    For any configuration where all metadata files are missing,
    load_all_metadata() should return a UnifiedMetadata object with
    all default values properly set.
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        
        # Create loader with non-existent file paths
        loader = MetadataLoader({})
        loader.meta_global_path = tmpdir_path / "nonexistent-global.yaml"
        loader.meta_org_path = tmpdir_path / "nonexistent-org.yaml"
        loader.meta_roles_path = tmpdir_path / "nonexistent-roles.yaml"
        
        # Load all metadata
        unified = loader.load_all_metadata()
        
        # Verify it's a UnifiedMetadata object
        assert isinstance(unified, UnifiedMetadata)
        
        # Verify global defaults
        assert unified.global_info.source == "HandBook Generator"
        assert unified.global_info.version == "1.0.0"
        
        # Verify organisation defaults
        assert unified.organisation.name == "[TODO]"
        assert unified.organisation.revision == 0
        
        # Verify roles defaults
        assert unified.roles.role_CEO == "[TODO]"
        assert unified.roles.group_IT_Services == "[TODO]"
        
        # Verify handbook is None (not loaded yet)
        assert unified.handbook is None


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--hypothesis-show-statistics"])



# ============================================================================
# Property 4: Configuration Validation Tests
# ============================================================================

def test_property_yaml_syntax_validation_invalid_yaml():
    """
    Property 4: Configuration Validation (YAML Syntax)
    
    For any configuration file with invalid YAML syntax, the system should
    report specific validation errors including file name and line number.
    
    Validates: Requirements 1.4, 9.1, 9.2
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        meta_global_path = tmpdir_path / "meta-global.yaml"
        
        # Write invalid YAML (missing colon, bad indentation)
        with open(meta_global_path, 'w') as f:
            f.write("source HandBook Generator\n")  # Missing colon
            f.write("version: 1.0.0\n")
        
        loader = MetadataLoader({})
        loader.meta_global_path = meta_global_path
        
        # Should raise YAMLError with enhanced message
        with pytest.raises(yaml.YAMLError) as exc_info:
            loader._load_global_metadata()
        
        error_msg = str(exc_info.value)
        assert "ERROR ConfigLoader" in error_msg
        assert str(meta_global_path) in error_msg
        assert "Invalid YAML syntax" in error_msg
        assert "Suggestion" in error_msg


@given(
    invalid_revision=st.one_of(
        st.text(min_size=1, max_size=10),  # String instead of int
        st.floats(allow_nan=False, allow_infinity=False),  # Float instead of int
        st.lists(st.integers(), min_size=1, max_size=3)  # List instead of int
    )
)
def test_property_field_type_validation_organisation_revision(invalid_revision):
    """
    Property 4: Configuration Validation (Field Type Validation)
    
    For any configuration file with incorrect field types, the system should
    report type mismatches with expected vs actual type.
    
    Validates: Requirements 1.4, 9.1, 9.2
    """
    # Skip if the value happens to be an int (edge case)
    assume(not isinstance(invalid_revision, int))
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        meta_org_path = tmpdir_path / "meta-organisation.yaml"
        
        # Write data with wrong type for revision
        with open(meta_org_path, 'w') as f:
            yaml.dump({
                'name': 'Test Org',
                'address': 'Test Address',
                'web': 'https://test.com',
                'phone': '+1234567890',
                'revision': invalid_revision
            }, f)
        
        loader = MetadataLoader({})
        loader.meta_org_path = meta_org_path
        
        # Should raise TypeError with clear message
        with pytest.raises(TypeError) as exc_info:
            loader._load_organisation_metadata()
        
        error_msg = str(exc_info.value)
        assert "ERROR ConfigLoader" in error_msg
        assert str(meta_org_path) in error_msg
        assert "Field type mismatches" in error_msg
        assert "revision" in error_msg
        assert "expected int" in error_msg
        assert "Suggestion" in error_msg


@given(
    invalid_source=st.one_of(
        st.integers(),  # Int instead of string
        st.lists(st.text(), min_size=1, max_size=3),  # List instead of string
        st.dictionaries(st.text(), st.text(), min_size=1, max_size=2)  # Dict instead of string
    )
)
def test_property_field_type_validation_global_source(invalid_source):
    """
    Property 4: Configuration Validation (Field Type Validation - Global)
    
    For any meta-global.yaml with incorrect field types, the system should
    report type mismatches.
    
    Validates: Requirements 1.4, 9.1, 9.2
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        meta_global_path = tmpdir_path / "meta-global.yaml"
        
        # Write data with wrong type for source
        with open(meta_global_path, 'w') as f:
            yaml.dump({
                'source': invalid_source,
                'version': '1.0.0'
            }, f)
        
        loader = MetadataLoader({})
        loader.meta_global_path = meta_global_path
        
        # Should raise TypeError with clear message
        with pytest.raises(TypeError) as exc_info:
            loader._load_global_metadata()
        
        error_msg = str(exc_info.value)
        assert "ERROR ConfigLoader" in error_msg
        assert "Field type mismatches" in error_msg
        assert "source" in error_msg
        assert "expected str" in error_msg


@given(
    invalid_revision=st.one_of(
        st.text(min_size=1, max_size=10),
        st.floats(allow_nan=False, allow_infinity=False)
    )
)
def test_property_field_type_validation_handbook_revision(invalid_revision):
    """
    Property 4: Configuration Validation (Field Type Validation - Handbook)
    
    For any meta-handbook.yaml with incorrect field types, the system should
    report type mismatches.
    
    Validates: Requirements 1.4, 9.1, 9.2
    """
    assume(not isinstance(invalid_revision, int))
    
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        handbook_path = tmpdir_path / "test_handbook"
        handbook_path.mkdir()
        meta_handbook_path = handbook_path / "meta-handbook.yaml"
        
        # Write data with wrong type for revision
        with open(meta_handbook_path, 'w') as f:
            yaml.dump({
                'author': 'Test Author',
                'revision': invalid_revision,
                'status': 'Draft'
            }, f)
        
        loader = MetadataLoader({})
        
        # Should raise TypeError with clear message
        with pytest.raises(TypeError) as exc_info:
            loader.load_handbook_metadata(handbook_path)
        
        error_msg = str(exc_info.value)
        assert "ERROR ConfigLoader" in error_msg
        assert "Field type mismatches" in error_msg
        assert "revision" in error_msg
        assert "expected int" in error_msg


def test_property_validation_error_messages_include_suggestions():
    """
    Property 4: Configuration Validation (Error Message Quality)
    
    For any validation error, the error message should include:
    - File name
    - Specific field or issue
    - Corrective action suggestion
    
    Validates: Requirements 9.1, 9.2
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        meta_org_path = tmpdir_path / "meta-organisation.yaml"
        
        # Write data with type error
        with open(meta_org_path, 'w') as f:
            yaml.dump({
                'name': 'Test',
                'revision': 'not-a-number'  # Should be int
            }, f)
        
        loader = MetadataLoader({})
        loader.meta_org_path = meta_org_path
        
        with pytest.raises(TypeError) as exc_info:
            loader._load_organisation_metadata()
        
        error_msg = str(exc_info.value)
        
        # Verify error message structure
        assert "ERROR ConfigLoader" in error_msg
        assert str(meta_org_path) in error_msg
        assert "Context:" in error_msg
        assert "Suggestion:" in error_msg
        assert "example.yaml" in error_msg.lower()


@given(
    valid_data=st.fixed_dictionaries({
        'name': st.text(min_size=1, max_size=50),
        'address': st.text(min_size=1, max_size=100),
        'web': st.text(min_size=1, max_size=50),
        'phone': st.text(min_size=1, max_size=30),
        'revision': st.integers(min_value=0, max_value=1000)
    })
)
def test_property_validation_passes_for_valid_data(valid_data):
    """
    Property 4: Configuration Validation (Valid Data Acceptance)
    
    For any configuration file with valid YAML syntax and correct field types,
    the system should load the data without errors.
    
    Validates: Requirements 1.4, 9.1, 9.2
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        meta_org_path = tmpdir_path / "meta-organisation.yaml"
        
        # Write valid data
        with open(meta_org_path, 'w') as f:
            yaml.dump(valid_data, f)
        
        loader = MetadataLoader({})
        loader.meta_org_path = meta_org_path
        
        # Should not raise any exception
        org_meta = loader._load_organisation_metadata()
        
        # Verify data was loaded correctly
        assert org_meta.name == valid_data['name']
        assert org_meta.address == valid_data['address']
        assert org_meta.web == valid_data['web']
        assert org_meta.phone == valid_data['phone']
        assert org_meta.revision == valid_data['revision']


def test_property_validation_allows_none_for_optional_fields():
    """
    Property 4: Configuration Validation (Optional Fields)
    
    For any configuration file where optional fields are set to None,
    the validation should pass (None is allowed for optional fields).
    
    Validates: Requirements 1.4
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        handbook_path = tmpdir_path / "test_handbook"
        handbook_path.mkdir()
        meta_handbook_path = handbook_path / "meta-handbook.yaml"
        
        # Write data with None for maintainer (optional field)
        with open(meta_handbook_path, 'w') as f:
            yaml.dump({
                'author': 'Test Author',
                'maintainer': None,  # Optional field
                'status': 'Draft'
            }, f)
        
        loader = MetadataLoader({})
        
        # Should not raise any exception
        handbook_meta = loader.load_handbook_metadata(handbook_path)
        
        # Verify maintainer defaults to author
        assert handbook_meta.author == 'Test Author'
        assert handbook_meta.maintainer == 'Test Author'  # Defaults to author


# ============================================================================
# Property 15: Circular Reference Detection Tests
# ============================================================================

def test_property_circular_reference_detection_direct_cycle():
    """
    Property 15: Circular Reference Detection
    
    For any configuration with circular file references, the system should
    detect the circular reference, report an error, and halt processing.
    
    This test simulates a direct circular reference by loading the same file twice.
    
    Validates: Requirements 9.3
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        meta_global_path = tmpdir_path / "meta-global.yaml"
        
        # Write valid YAML
        with open(meta_global_path, 'w') as f:
            yaml.dump({'source': 'Test', 'version': '1.0'}, f)
        
        loader = MetadataLoader({})
        loader.meta_global_path = meta_global_path
        
        # Manually simulate circular reference by adding to stack
        abs_path = meta_global_path.resolve()
        loader._loading_stack.append(abs_path)
        
        # Try to load the same file again (circular reference)
        with pytest.raises(ValueError) as exc_info:
            loader._load_yaml(meta_global_path)
        
        error_msg = str(exc_info.value)
        assert "ERROR ConfigLoader" in error_msg
        assert "Circular reference detected" in error_msg
        assert str(meta_global_path) in error_msg
        assert "Suggestion" in error_msg


def test_property_circular_reference_error_message_shows_cycle():
    """
    Property 15: Circular Reference Detection (Error Message)
    
    For any circular reference, the error message should show the complete
    cycle path to help users understand the problem.
    
    Validates: Requirements 9.3
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        file1 = tmpdir_path / "file1.yaml"
        file2 = tmpdir_path / "file2.yaml"
        
        # Write valid YAML files
        with open(file1, 'w') as f:
            yaml.dump({'key': 'value1'}, f)
        with open(file2, 'w') as f:
            yaml.dump({'key': 'value2'}, f)
        
        loader = MetadataLoader({})
        
        # Simulate a cycle: file1 -> file2 -> file1
        loader._loading_stack.append(file1.resolve())
        loader._loading_stack.append(file2.resolve())
        
        # Try to load file1 again (completes the cycle)
        with pytest.raises(ValueError) as exc_info:
            loader._load_yaml(file1)
        
        error_msg = str(exc_info.value)
        
        # Verify cycle is shown in error message
        assert "Circular reference detected" in error_msg
        assert str(file1) in error_msg
        assert str(file2) in error_msg
        assert "->" in error_msg  # Shows the cycle path


def test_property_no_circular_reference_for_different_files():
    """
    Property 15: Circular Reference Detection (No False Positives)
    
    For any configuration loading different files sequentially (no cycle),
    the system should not report circular reference errors.
    
    Validates: Requirements 9.3
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        file1 = tmpdir_path / "file1.yaml"
        file2 = tmpdir_path / "file2.yaml"
        file3 = tmpdir_path / "file3.yaml"
        
        # Write valid YAML files
        for f in [file1, file2, file3]:
            with open(f, 'w') as file:
                yaml.dump({'key': 'value'}, file)
        
        loader = MetadataLoader({})
        
        # Load files sequentially (no cycle)
        data1 = loader._load_yaml(file1)
        assert data1 is not None
        
        data2 = loader._load_yaml(file2)
        assert data2 is not None
        
        data3 = loader._load_yaml(file3)
        assert data3 is not None
        
        # Loading stack should be empty after each load
        assert len(loader._loading_stack) == 0


def test_property_circular_reference_stack_cleanup_on_error():
    """
    Property 15: Circular Reference Detection (Stack Cleanup)
    
    For any error during file loading (including circular reference),
    the loading stack should be properly cleaned up.
    
    Validates: Requirements 9.3
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        meta_global_path = tmpdir_path / "meta-global.yaml"
        
        # Write invalid YAML to trigger an error
        with open(meta_global_path, 'w') as f:
            f.write("invalid: yaml: syntax:\n")
        
        loader = MetadataLoader({})
        loader.meta_global_path = meta_global_path
        
        # Try to load (will fail due to YAML error)
        try:
            loader._load_yaml(meta_global_path)
        except yaml.YAMLError:
            pass  # Expected error
        
        # Verify stack is cleaned up even after error
        assert len(loader._loading_stack) == 0


def test_property_circular_reference_detection_with_metadata_loading():
    """
    Property 15: Circular Reference Detection (Integration)
    
    For any metadata loading operation, circular reference detection
    should work correctly during normal metadata loading flow.
    
    Validates: Requirements 9.3
    """
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir_path = Path(tmpdir)
        meta_global_path = tmpdir_path / "meta-global.yaml"
        meta_org_path = tmpdir_path / "meta-organisation.yaml"
        
        # Write valid YAML files
        with open(meta_global_path, 'w') as f:
            yaml.dump({'source': 'Test', 'version': '1.0'}, f)
        with open(meta_org_path, 'w') as f:
            yaml.dump({'name': 'Test Org', 'revision': 0}, f)
        
        loader = MetadataLoader({})
        loader.meta_global_path = meta_global_path
        loader.meta_org_path = meta_org_path
        
        # Load all metadata (should work without circular reference errors)
        unified = loader.load_all_metadata()
        
        assert unified is not None
        assert unified.global_info.source == 'Test'
        assert unified.organisation.name == 'Test Org'
        
        # Verify stack is clean after loading
        assert len(loader._loading_stack) == 0
