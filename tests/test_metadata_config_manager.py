"""
Unit tests for Metadata Configuration Manager

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

import pytest
import yaml
from pathlib import Path
from src.metadata_config_manager import (
    MetadataConfigManager,
    MetadataConfig,
    OrganizationInfo,
    PersonRole,
    DocumentInfo,
    Classification
)


class TestOrganizationInfo:
    """Test OrganizationInfo dataclass."""
    
    def test_valid_organization_info(self):
        """Test creating valid organization info."""
        org = OrganizationInfo(
            name="Test Org",
            address="Test Street 123",
            city="Test City",
            postal_code="12345",
            country="Test Country",
            website="https://test.com",
            phone="+49 89 12345678",
            email="info@test.com"
        )
        assert org.name == "Test Org"
        assert org.email == "info@test.com"
    
    def test_invalid_email(self):
        """Test organization info with invalid email."""
        with pytest.raises(ValueError, match="Invalid email format"):
            OrganizationInfo(
                name="Test Org",
                address="Test Street 123",
                city="Test City",
                postal_code="12345",
                country="Test Country",
                website="https://test.com",
                phone="+49 89 12345678",
                email="invalid-email"
            )
    
    def test_invalid_phone(self):
        """Test organization info with invalid phone."""
        with pytest.raises(ValueError, match="Invalid phone format"):
            OrganizationInfo(
                name="Test Org",
                address="Test Street 123",
                city="Test City",
                postal_code="12345",
                country="Test Country",
                website="https://test.com",
                phone="abc",
                email="info@test.com"
            )


class TestPersonRole:
    """Test PersonRole dataclass."""
    
    def test_valid_person_role(self):
        """Test creating valid person role."""
        role = PersonRole(
            name="John Doe",
            title="CEO",
            email="john@test.com",
            phone="+49 89 12345678",
            department="Management"
        )
        assert role.name == "John Doe"
        assert role.title == "CEO"
        assert role.department == "Management"
    
    def test_person_role_without_department(self):
        """Test person role without optional department."""
        role = PersonRole(
            name="Jane Doe",
            title="CIO",
            email="jane@test.com",
            phone="+49 89 12345679"
        )
        assert role.department is None
    
    def test_invalid_email(self):
        """Test person role with invalid email."""
        with pytest.raises(ValueError, match="Invalid email format"):
            PersonRole(
                name="John Doe",
                title="CEO",
                email="not-an-email",
                phone="+49 89 12345678"
            )


class TestDocumentInfo:
    """Test DocumentInfo dataclass."""
    
    def test_valid_document_info(self):
        """Test creating valid document info."""
        doc = DocumentInfo(
            owner="IT Manager",
            approver="CIO",
            version="1.0.0",
            classification="internal"
        )
        assert doc.owner == "IT Manager"
        assert doc.classification == "internal"
    
    def test_invalid_classification(self):
        """Test document info with invalid classification."""
        with pytest.raises(ValueError, match="Invalid classification"):
            DocumentInfo(
                owner="IT Manager",
                approver="CIO",
                version="1.0.0",
                classification="invalid"
            )
    
    def test_all_valid_classifications(self):
        """Test all valid classification values."""
        for classification in ["public", "internal", "confidential", "restricted"]:
            doc = DocumentInfo(
                owner="IT Manager",
                approver="CIO",
                version="1.0.0",
                classification=classification
            )
            assert doc.classification == classification


class TestMetadataConfig:
    """Test MetadataConfig dataclass."""
    
    def test_get_role_case_insensitive(self):
        """Test getting role with case-insensitive lookup."""
        config = MetadataConfig(
            organization=OrganizationInfo(
                name="Test Org",
                address="Test Street",
                city="Test City",
                postal_code="12345",
                country="Test Country",
                website="https://test.com",
                phone="+49 89 12345678",
                email="info@test.com"
            ),
            roles={
                "ceo": PersonRole(
                    name="John Doe",
                    title="CEO",
                    email="john@test.com",
                    phone="+49 89 12345678"
                )
            },
            document=DocumentInfo(
                owner="IT Manager",
                approver="CIO",
                version="1.0.0",
                classification="internal"
            ),
            author="Test Author",
            language="de"
        )
        
        # Test case-insensitive lookup
        assert config.get_role("ceo") is not None
        assert config.get_role("CEO") is not None
        assert config.get_role("Ceo") is not None
        assert config.get_role("ceo").name == "John Doe"
    
    def test_get_role_not_found(self):
        """Test getting non-existent role."""
        config = MetadataConfig(
            organization=OrganizationInfo(
                name="Test Org",
                address="Test Street",
                city="Test City",
                postal_code="12345",
                country="Test Country",
                website="https://test.com",
                phone="+49 89 12345678",
                email="info@test.com"
            ),
            roles={},
            document=DocumentInfo(
                owner="IT Manager",
                approver="CIO",
                version="1.0.0",
                classification="internal"
            ),
            author="Test Author",
            language="de"
        )
        
        assert config.get_role("ceo") is None


class TestMetadataConfigManager:
    """Test MetadataConfigManager class."""
    
    @pytest.fixture
    def temp_metadata_file(self, tmp_path):
        """Create temporary metadata file."""
        metadata_path = tmp_path / "metadata.yaml"
        return metadata_path
    
    @pytest.fixture
    def valid_metadata_content(self):
        """Valid metadata YAML content."""
        return """
organization:
  name: "Test Organization"
  address: "Test Street 123"
  city: "Test City"
  postal_code: "12345"
  country: "Test Country"
  website: "https://test.com"
  phone: "+49 89 12345678"
  email: "info@test.com"

roles:
  ceo:
    name: "John Doe"
    title: "Chief Executive Officer"
    email: "john@test.com"
    phone: "+49 89 12345678"
    department: "Management"
  
  cio:
    name: "Jane Smith"
    title: "Chief Information Officer"
    email: "jane@test.com"
    phone: "+49 89 12345679"
    department: "IT"

document:
  owner: "IT Manager"
  approver: "CIO"
  version: "1.0.0"
  classification: "internal"

defaults:
  author: "Test Author"
  language: "de"
"""
    
    def test_load_valid_metadata(self, temp_metadata_file, valid_metadata_content):
        """Test loading valid metadata file."""
        # Write valid metadata
        temp_metadata_file.write_text(valid_metadata_content)
        
        # Load metadata
        manager = MetadataConfigManager(temp_metadata_file)
        config = manager.load_metadata()
        
        # Verify loaded data
        assert config.organization.name == "Test Organization"
        assert config.organization.email == "info@test.com"
        assert "ceo" in config.roles
        assert config.roles["ceo"].name == "John Doe"
        assert config.document.owner == "IT Manager"
        assert config.author == "Test Author"
        assert config.language == "de"
    
    def test_load_missing_file(self, temp_metadata_file):
        """Test loading non-existent metadata file."""
        manager = MetadataConfigManager(temp_metadata_file)
        
        with pytest.raises(FileNotFoundError):
            manager.load_metadata()
    
    def test_load_invalid_yaml(self, temp_metadata_file):
        """Test loading metadata with invalid YAML syntax."""
        # Write invalid YAML
        temp_metadata_file.write_text("invalid: yaml: syntax:")
        
        manager = MetadataConfigManager(temp_metadata_file)
        
        with pytest.raises(yaml.YAMLError):
            manager.load_metadata()
    
    def test_load_missing_required_fields(self, temp_metadata_file):
        """Test loading metadata with missing required fields."""
        # Write metadata without organization
        temp_metadata_file.write_text("""
document:
  owner: "IT Manager"
  approver: "CIO"
  version: "1.0.0"
  classification: "internal"
""")
        
        manager = MetadataConfigManager(temp_metadata_file)
        
        with pytest.raises(ValueError, match="Missing required section 'organization'"):
            manager.load_metadata()
    
    def test_create_default_metadata(self, temp_metadata_file):
        """Test creating default metadata file."""
        manager = MetadataConfigManager(temp_metadata_file)
        manager.create_default_metadata()
        
        # Verify file was created
        assert temp_metadata_file.exists()
        
        # Verify it can be loaded
        config = manager.load_metadata()
        assert config.organization.name == "AdminSend GmbH"
        assert "ceo" in config.roles
        assert "cio" in config.roles
        assert "ciso" in config.roles
        assert "cfo" in config.roles
        assert "coo" in config.roles
    
    def test_create_default_metadata_file_exists(self, temp_metadata_file):
        """Test creating default metadata when file already exists."""
        # Create file first
        temp_metadata_file.write_text("existing content")
        
        manager = MetadataConfigManager(temp_metadata_file)
        
        with pytest.raises(FileExistsError):
            manager.create_default_metadata()
    
    def test_validate_metadata_valid(self):
        """Test validating valid metadata."""
        config = MetadataConfig(
            organization=OrganizationInfo(
                name="Test Org",
                address="Test Street",
                city="Test City",
                postal_code="12345",
                country="Test Country",
                website="https://test.com",
                phone="+49 89 12345678",
                email="info@test.com"
            ),
            roles={
                "ceo": PersonRole(
                    name="John Doe",
                    title="CEO",
                    email="john@test.com",
                    phone="+49 89 12345678"
                ),
                "cio": PersonRole(
                    name="Jane Smith",
                    title="CIO",
                    email="jane@test.com",
                    phone="+49 89 12345679"
                ),
                "ciso": PersonRole(
                    name="Bob Wilson",
                    title="CISO",
                    email="bob@test.com",
                    phone="+49 89 12345680"
                ),
                "cfo": PersonRole(
                    name="Alice Brown",
                    title="CFO",
                    email="alice@test.com",
                    phone="+49 89 12345681"
                ),
                "coo": PersonRole(
                    name="Charlie Davis",
                    title="COO",
                    email="charlie@test.com",
                    phone="+49 89 12345682"
                )
            },
            document=DocumentInfo(
                owner="IT Manager",
                approver="CIO",
                version="1.0.0",
                classification="internal"
            ),
            author="Test Author",
            language="de"
        )
        
        manager = MetadataConfigManager()
        warnings = manager.validate_metadata(config)
        
        # Should have no warnings
        assert len(warnings) == 0
    
    def test_validate_metadata_missing_fields(self):
        """Test validating metadata with missing required fields."""
        config = MetadataConfig(
            organization=OrganizationInfo(
                name="",  # Missing name
                address="Test Street",
                city="Test City",
                postal_code="12345",
                country="Test Country",
                website="https://test.com",
                phone="+49 89 12345678",
                email="info@test.com"
            ),
            roles={},  # Missing standard roles
            document=DocumentInfo(
                owner="",  # Missing owner
                approver="CIO",
                version="1.0.0",
                classification="internal"
            ),
            author="Test Author",
            language="de"
        )
        
        manager = MetadataConfigManager()
        warnings = manager.validate_metadata(config)
        
        # Should have warnings for missing fields
        assert len(warnings) > 0
        assert any("organization.name" in w for w in warnings)
        assert any("document.owner" in w for w in warnings)
        assert any("ceo" in w for w in warnings)
    
    def test_validate_metadata_missing_roles(self):
        """Test validating metadata with missing standard roles."""
        config = MetadataConfig(
            organization=OrganizationInfo(
                name="Test Org",
                address="Test Street",
                city="Test City",
                postal_code="12345",
                country="Test Country",
                website="https://test.com",
                phone="+49 89 12345678",
                email="info@test.com"
            ),
            roles={
                "ceo": PersonRole(
                    name="John Doe",
                    title="CEO",
                    email="john@test.com",
                    phone="+49 89 12345678"
                )
                # Missing cio, ciso, cfo, coo
            },
            document=DocumentInfo(
                owner="IT Manager",
                approver="CIO",
                version="1.0.0",
                classification="internal"
            ),
            author="Test Author",
            language="de"
        )
        
        manager = MetadataConfigManager()
        warnings = manager.validate_metadata(config)
        
        # Should warn about missing standard roles
        assert any("cio" in w for w in warnings)
        assert any("ciso" in w for w in warnings)
        assert any("cfo" in w for w in warnings)
        assert any("coo" in w for w in warnings)


# Property-Based Tests
from hypothesis import given, settings
import hypothesis.strategies as st


@st.composite
def valid_email_strategy(draw):
    """Generate valid email addresses."""
    # Use only ASCII letters and digits for username
    username = draw(st.text(alphabet='abcdefghijklmnopqrstuvwxyz0123456789', min_size=1, max_size=20))
    domain = draw(st.text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=1, max_size=20))
    tld = draw(st.sampled_from(['com', 'de', 'org', 'net', 'io']))
    return f"{username}@{domain}.{tld}"


@st.composite
def valid_phone_strategy(draw):
    """Generate valid phone numbers."""
    country_code = draw(st.sampled_from(['+49', '+1', '+44', '+33']))
    area_code = draw(st.integers(min_value=10, max_value=999))
    number = draw(st.integers(min_value=1000000, max_value=99999999))
    return f"{country_code} {area_code} {number}"


@st.composite
def metadata_config_strategy(draw):
    """Generate valid metadata configurations."""
    org_name = draw(st.text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ', min_size=1, max_size=100))
    
    return {
        'organization': {
            'name': org_name,
            'address': draw(st.text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ', min_size=1, max_size=200)),
            'city': draw(st.text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ', min_size=1, max_size=100)),
            'postal_code': draw(st.text(alphabet='0123456789', min_size=1, max_size=20)),
            'country': draw(st.text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ', min_size=1, max_size=100)),
            'website': f"https://{draw(st.text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=1, max_size=20))}.com",
            'phone': draw(valid_phone_strategy()),
            'email': draw(valid_email_strategy())
        },
        'roles': {
            'ceo': {
                'name': draw(st.text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ', min_size=1, max_size=100)),
                'title': 'Chief Executive Officer',
                'email': draw(valid_email_strategy()),
                'phone': draw(valid_phone_strategy()),
                'department': 'Management'
            }
        },
        'document': {
            'owner': draw(st.text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ', min_size=1, max_size=100)),
            'approver': draw(st.text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ', min_size=1, max_size=100)),
            'version': '1.0.0',
            'classification': draw(st.sampled_from(['public', 'internal', 'confidential', 'restricted']))
        },
        'defaults': {
            'author': draw(st.text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ', min_size=1, max_size=100)),
            'language': draw(st.sampled_from(['de', 'en']))
        }
    }


class TestMetadataConfigManagerProperties:
    """Property-based tests for MetadataConfigManager."""
    
    @settings(max_examples=100)
    @given(metadata_data=metadata_config_strategy())
    def test_property_metadata_configuration_loading(self, metadata_data):
        """
        Feature: it-operation-template-extension, Property 5: Metadata Configuration Loading
        
        For any valid metadata.yaml file, the system should correctly parse all sections
        (organization, roles, document) and create a complete MetadataConfig object.
        
        Validates: Requirements 17.1, 17.2
        """
        import tempfile
        import os
        
        # Create temporary metadata file
        with tempfile.NamedTemporaryFile(mode='w', suffix='.yaml', delete=False, encoding='utf-8') as f:
            yaml.dump(metadata_data, f)
            metadata_path = Path(f.name)
        
        try:
            # Load metadata
            manager = MetadataConfigManager(metadata_path)
            config = manager.load_metadata()
            
            # Verify all sections are loaded
            assert config.organization is not None
            assert config.organization.name == metadata_data['organization']['name']
            assert config.organization.email == metadata_data['organization']['email']
            
            assert config.roles is not None
            assert 'ceo' in config.roles
            assert config.roles['ceo'].name == metadata_data['roles']['ceo']['name']
            assert config.roles['ceo'].email == metadata_data['roles']['ceo']['email']
            
            assert config.document is not None
            assert config.document.owner == metadata_data['document']['owner']
            assert config.document.classification == metadata_data['document']['classification']
            
            assert config.author == metadata_data['defaults']['author']
            assert config.language == metadata_data['defaults']['language']
        finally:
            # Clean up temporary file
            if metadata_path.exists():
                os.unlink(metadata_path)
    
    @settings(max_examples=100)
    @given(
        role_name=st.text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ', min_size=1, max_size=100),
        role_title=st.text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ', min_size=1, max_size=100),
        role_email=valid_email_strategy(),
        role_phone=valid_phone_strategy()
    )
    def test_property_organization_role_validation(self, role_name, role_title, role_email, role_phone):
        """
        Feature: it-operation-template-extension, Property 6: Organization Role Validation
        
        For any metadata configuration, if a role (ceo, cio, ciso, cfo, coo) is defined,
        it should contain at minimum name, title, and email fields.
        
        Validates: Requirements 18.1, 18.2, 18.5
        """
        # Create a role with all required fields
        role = PersonRole(
            name=role_name,
            title=role_title,
            email=role_email,
            phone=role_phone
        )
        
        # Verify all required fields are present
        assert role.name is not None and len(role.name.strip()) > 0
        assert role.title is not None and len(role.title.strip()) > 0
        assert role.email is not None and len(role.email.strip()) > 0
        
        # Verify email is valid format
        assert '@' in role.email
        assert '.' in role.email.split('@')[1]
    
    @settings(max_examples=100)
    @given(
        role_key=st.sampled_from(['ceo', 'cio', 'ciso', 'cfo', 'coo']),
        field_name=st.sampled_from(['name', 'title', 'email', 'phone', 'department'])
    )
    def test_property_role_field_access(self, role_key, field_name):
        """
        Feature: it-operation-template-extension, Property 7: Role Field Access
        
        For any defined role in the metadata configuration, the system should support
        accessing role fields via placeholders like "{{ meta.ceo.name }}" and "{{ meta.ciso.email }}".
        
        Validates: Requirements 18.3
        """
        # Create a metadata config with the role
        config = MetadataConfig(
            organization=OrganizationInfo(
                name="Test Org",
                address="Test Street",
                city="Test City",
                postal_code="12345",
                country="Test Country",
                website="https://test.com",
                phone="+49 89 12345678",
                email="info@test.com"
            ),
            roles={
                role_key: PersonRole(
                    name="Test Person",
                    title="Test Title",
                    email="test@test.com",
                    phone="+49 89 12345678",
                    department="Test Department"
                )
            },
            document=DocumentInfo(
                owner="IT Manager",
                approver="CIO",
                version="1.0.0",
                classification="internal"
            ),
            author="Test Author",
            language="de"
        )
        
        # Get the role
        role = config.get_role(role_key)
        assert role is not None
        
        # Verify field access
        field_value = getattr(role, field_name, None)
        
        # All fields except department should have values
        if field_name != 'department':
            assert field_value is not None
            assert len(str(field_value).strip()) > 0
    
    @settings(max_examples=100)
    @given(
        undefined_role=st.text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=1, max_size=20).filter(
            lambda x: x not in ['ceo', 'cio', 'ciso', 'cfo', 'coo']
        )
    )
    def test_property_missing_role_handling(self, undefined_role):
        """
        Feature: it-operation-template-extension, Property 8: Missing Role Handling
        
        For any placeholder referencing an undefined role, the system should use a
        default placeholder text or generate a warning.
        
        Validates: Requirements 18.4
        """
        # Create a metadata config without the undefined role
        config = MetadataConfig(
            organization=OrganizationInfo(
                name="Test Org",
                address="Test Street",
                city="Test City",
                postal_code="12345",
                country="Test Country",
                website="https://test.com",
                phone="+49 89 12345678",
                email="info@test.com"
            ),
            roles={
                "ceo": PersonRole(
                    name="Test CEO",
                    title="CEO",
                    email="ceo@test.com",
                    phone="+49 89 12345678"
                )
            },
            document=DocumentInfo(
                owner="IT Manager",
                approver="CIO",
                version="1.0.0",
                classification="internal"
            ),
            author="Test Author",
            language="de"
        )
        
        # Try to get the undefined role
        role = config.get_role(undefined_role)
        
        # Should return None for undefined roles
        assert role is None
    
    @settings(max_examples=100)
    @given(
        org_name=st.one_of(
            st.just(""),  # Empty name
            st.text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ', min_size=1, max_size=100)
        ),
        doc_owner=st.one_of(
            st.just(""),  # Empty owner
            st.text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ', min_size=1, max_size=100)
        ),
        doc_approver=st.text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ', min_size=1, max_size=100),
        author=st.text(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ', min_size=1, max_size=100),
        include_standard_roles=st.booleans()
    )
    def test_property_metadata_configuration_validation(self, org_name, doc_owner, doc_approver, author, include_standard_roles):
        """
        Feature: it-operation-template-extension, Property 15: Metadata Configuration Validation
        
        For any metadata.yaml file, the validation process should check for required fields
        (organization.name, document.owner) and report missing fields as warnings.
        
        Validates: Requirements 17.4, 17.5
        """
        # Create roles based on whether to include standard roles
        roles = {}
        if include_standard_roles:
            for role_key in ['ceo', 'cio', 'ciso', 'cfo', 'coo']:
                roles[role_key] = PersonRole(
                    name=f"Test {role_key.upper()}",
                    title=f"Chief {role_key.upper()} Officer",
                    email=f"{role_key}@test.com",
                    phone="+49 89 12345678"
                )
        
        # Create metadata config
        config = MetadataConfig(
            organization=OrganizationInfo(
                name=org_name,
                address="Test Street",
                city="Test City",
                postal_code="12345",
                country="Test Country",
                website="https://test.com",
                phone="+49 89 12345678",
                email="info@test.com"
            ),
            roles=roles,
            document=DocumentInfo(
                owner=doc_owner,
                approver=doc_approver,
                version="1.0.0",
                classification="internal"
            ),
            author=author,
            language="de"
        )
        
        # Validate metadata
        manager = MetadataConfigManager()
        warnings = manager.validate_metadata(config)
        
        # Property: Validation should detect missing required fields
        
        # Check organization.name validation
        if not org_name or not org_name.strip():
            assert any("organization.name" in w for w in warnings), \
                "Validation should warn about missing organization.name"
        else:
            assert not any("organization.name" in w for w in warnings), \
                "Validation should not warn about organization.name when it's present"
        
        # Check document.owner validation (Requirement 17.4)
        if not doc_owner or not doc_owner.strip():
            assert any("document.owner" in w for w in warnings), \
                "Validation should warn about missing document.owner (Requirement 17.4)"
        else:
            assert not any("document.owner" in w for w in warnings), \
                "Validation should not warn about document.owner when it's present"
        
        # Check standard roles validation
        if not include_standard_roles:
            # Should warn about missing standard roles
            assert any("ceo" in w for w in warnings), \
                "Validation should warn about missing CEO role"
            assert any("cio" in w for w in warnings), \
                "Validation should warn about missing CIO role"
            assert any("ciso" in w for w in warnings), \
                "Validation should warn about missing CISO role"
            assert any("cfo" in w for w in warnings), \
                "Validation should warn about missing CFO role"
            assert any("coo" in w for w in warnings), \
                "Validation should warn about missing COO role"
        else:
            # Should not warn about standard roles when they're present
            standard_role_warnings = [w for w in warnings if any(role in w for role in ['ceo', 'cio', 'ciso', 'cfo', 'coo'])]
            # Filter out warnings about missing roles (we only care about presence)
            missing_role_warnings = [w for w in standard_role_warnings if "Missing standard role" in w]
            assert len(missing_role_warnings) == 0, \
                "Validation should not warn about standard roles when they're all present"
        
        # Property: Validation should always return a list (even if empty)
        assert isinstance(warnings, list), \
            "Validation should always return a list of warnings"
        
        # Property: All warnings should be non-empty strings
        for warning in warnings:
            assert isinstance(warning, str), \
                "Each warning should be a string"
            assert len(warning.strip()) > 0, \
                "Each warning should be a non-empty string"
