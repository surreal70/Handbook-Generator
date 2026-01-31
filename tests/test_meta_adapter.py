"""
Unit tests for Meta Adapter

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

import pytest
from src.meta_adapter import MetaAdapter
from src.metadata_config_manager import (
    MetadataConfig,
    OrganizationInfo,
    PersonRole,
    DocumentInfo
)


class TestMetaAdapter:
    """Test MetaAdapter class."""
    
    @pytest.fixture
    def sample_metadata_config(self):
        """Create sample metadata configuration."""
        return MetadataConfig(
            organization=OrganizationInfo(
                name="Test Organization",
                address="Test Street 123",
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
                    title="Chief Executive Officer",
                    email="john@test.com",
                    phone="+49 89 12345678",
                    department="Management"
                ),
                "cio": PersonRole(
                    name="Jane Smith",
                    title="Chief Information Officer",
                    email="jane@test.com",
                    phone="+49 89 12345679",
                    department="IT"
                ),
                "ciso": PersonRole(
                    name="Bob Wilson",
                    title="Chief Information Security Officer",
                    email="bob@test.com",
                    phone="+49 89 12345680",
                    department="IT Security"
                ),
                "cfo": PersonRole(
                    name="Alice Brown",
                    title="Chief Financial Officer",
                    email="alice@test.com",
                    phone="+49 89 12345681",
                    department="Finance"
                ),
                "coo": PersonRole(
                    name="Charlie Davis",
                    title="Chief Operating Officer",
                    email="charlie@test.com",
                    phone="+49 89 12345682",
                    department="Operations"
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
    
    def test_connect_valid_metadata(self, sample_metadata_config):
        """Test connecting with valid metadata."""
        adapter = MetaAdapter(sample_metadata_config)
        assert adapter.connect() is True
    
    def test_connect_invalid_metadata(self):
        """Test connecting with invalid metadata."""
        adapter = MetaAdapter(None)
        assert adapter.connect() is False
    
    def test_disconnect(self, sample_metadata_config):
        """Test disconnecting."""
        adapter = MetaAdapter(sample_metadata_config)
        adapter.connect()
        adapter.disconnect()
        # Should be able to disconnect without errors
    
    def test_get_organization_field(self, sample_metadata_config):
        """Test getting organization fields."""
        adapter = MetaAdapter(sample_metadata_config)
        adapter.connect()
        
        assert adapter.get_field("organization.name") == "Test Organization"
        assert adapter.get_field("organization.email") == "info@test.com"
        assert adapter.get_field("organization.city") == "Test City"
        assert adapter.get_field("organization.phone") == "+49 89 12345678"
        assert adapter.get_field("organization.website") == "https://test.com"
        assert adapter.get_field("organization.address") == "Test Street 123"
        assert adapter.get_field("organization.postal_code") == "12345"
        assert adapter.get_field("organization.country") == "Test Country"
    
    def test_get_role_field_ceo(self, sample_metadata_config):
        """Test getting CEO role fields."""
        adapter = MetaAdapter(sample_metadata_config)
        adapter.connect()
        
        assert adapter.get_field("ceo.name") == "John Doe"
        assert adapter.get_field("ceo.title") == "Chief Executive Officer"
        assert adapter.get_field("ceo.email") == "john@test.com"
        assert adapter.get_field("ceo.phone") == "+49 89 12345678"
        assert adapter.get_field("ceo.department") == "Management"
    
    def test_get_role_field_cio(self, sample_metadata_config):
        """Test getting CIO role fields."""
        adapter = MetaAdapter(sample_metadata_config)
        adapter.connect()
        
        assert adapter.get_field("cio.name") == "Jane Smith"
        assert adapter.get_field("cio.email") == "jane@test.com"
    
    def test_get_role_field_ciso(self, sample_metadata_config):
        """Test getting CISO role fields."""
        adapter = MetaAdapter(sample_metadata_config)
        adapter.connect()
        
        assert adapter.get_field("ciso.name") == "Bob Wilson"
        assert adapter.get_field("ciso.email") == "bob@test.com"
    
    def test_get_role_field_cfo(self, sample_metadata_config):
        """Test getting CFO role fields."""
        adapter = MetaAdapter(sample_metadata_config)
        adapter.connect()
        
        assert adapter.get_field("cfo.name") == "Alice Brown"
        assert adapter.get_field("cfo.email") == "alice@test.com"
    
    def test_get_role_field_coo(self, sample_metadata_config):
        """Test getting COO role fields."""
        adapter = MetaAdapter(sample_metadata_config)
        adapter.connect()
        
        assert adapter.get_field("coo.name") == "Charlie Davis"
        assert adapter.get_field("coo.email") == "charlie@test.com"
    
    def test_get_document_field(self, sample_metadata_config):
        """Test getting document fields."""
        adapter = MetaAdapter(sample_metadata_config)
        adapter.connect()
        
        assert adapter.get_field("document.owner") == "IT Manager"
        assert adapter.get_field("document.approver") == "CIO"
        assert adapter.get_field("document.version") == "1.0.0"
        assert adapter.get_field("document.classification") == "internal"
    
    def test_get_top_level_fields(self, sample_metadata_config):
        """Test getting top-level metadata fields."""
        adapter = MetaAdapter(sample_metadata_config)
        adapter.connect()
        
        assert adapter.get_field("author") == "Test Author"
        assert adapter.get_field("language") == "de"
    
    def test_get_invalid_field_path(self, sample_metadata_config):
        """Test getting invalid field path."""
        adapter = MetaAdapter(sample_metadata_config)
        adapter.connect()
        
        assert adapter.get_field("invalid.field") is None
        assert adapter.get_field("organization.invalid") is None
    
    def test_get_missing_role(self, sample_metadata_config):
        """Test getting field from missing role."""
        adapter = MetaAdapter(sample_metadata_config)
        adapter.connect()
        
        assert adapter.get_field("cto.name") is None
        assert adapter.get_field("cto.email") is None
    
    def test_get_field_without_connect(self, sample_metadata_config):
        """Test getting field without connecting first."""
        adapter = MetaAdapter(sample_metadata_config)
        
        with pytest.raises(ConnectionError, match="Not connected to metadata"):
            adapter.get_field("organization.name")
    
    def test_get_field_empty_path(self, sample_metadata_config):
        """Test getting field with empty path."""
        adapter = MetaAdapter(sample_metadata_config)
        adapter.connect()
        
        with pytest.raises(ValueError, match="field_path cannot be empty"):
            adapter.get_field("")
    
    def test_context_manager(self, sample_metadata_config):
        """Test using adapter as context manager."""
        with MetaAdapter(sample_metadata_config) as adapter:
            assert adapter.get_field("organization.name") == "Test Organization"


# Property-Based Tests
from hypothesis import given, settings
import hypothesis.strategies as st


@st.composite
def valid_field_path_strategy(draw):
    """Generate valid field paths for metadata."""
    field_type = draw(st.sampled_from(['organization', 'role', 'document', 'top_level']))
    
    if field_type == 'organization':
        field = draw(st.sampled_from(['name', 'address', 'city', 'postal_code', 'country', 'website', 'phone', 'email']))
        return f"organization.{field}"
    elif field_type == 'role':
        role = draw(st.sampled_from(['ceo', 'cio', 'ciso', 'cfo', 'coo']))
        field = draw(st.sampled_from(['name', 'title', 'email', 'phone', 'department']))
        return f"{role}.{field}"
    elif field_type == 'document':
        field = draw(st.sampled_from(['owner', 'approver', 'version', 'classification']))
        return f"document.{field}"
    else:  # top_level
        return draw(st.sampled_from(['author', 'language']))


def _create_sample_metadata_config():
    """Create sample metadata configuration."""
    return MetadataConfig(
        organization=OrganizationInfo(
            name="Test Organization",
            address="Test Street 123",
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
                title="Chief Executive Officer",
                email="john@test.com",
                phone="+49 89 12345678",
                department="Management"
            ),
            "cio": PersonRole(
                name="Jane Smith",
                title="Chief Information Officer",
                email="jane@test.com",
                phone="+49 89 12345679",
                department="IT"
            ),
            "ciso": PersonRole(
                name="Bob Wilson",
                title="Chief Information Security Officer",
                email="bob@test.com",
                phone="+49 89 12345680",
                department="IT Security"
            ),
            "cfo": PersonRole(
                name="Alice Brown",
                title="Chief Financial Officer",
                email="alice@test.com",
                phone="+49 89 12345681",
                department="Finance"
            ),
            "coo": PersonRole(
                name="Charlie Davis",
                title="Chief Operating Officer",
                email="charlie@test.com",
                phone="+49 89 12345682",
                department="Operations"
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


class TestMetaAdapterProperties:
    """Property-based tests for MetaAdapter."""
    
    @settings(max_examples=100)
    @given(field_path=valid_field_path_strategy())
    def test_property_meta_field_resolution(self, field_path):
        """
        Feature: it-operation-template-extension, Property 2: Meta Field Resolution
        
        For any valid meta field path (e.g., "organization.name", "ceo.email"),
        the system should correctly resolve the field from the metadata configuration
        and return the corresponding value.
        
        Validates: Requirements 16.3, 17.2, 17.3
        """
        sample_metadata_config = _create_sample_metadata_config()
        adapter = MetaAdapter(sample_metadata_config)
        adapter.connect()
        
        # Get field value
        value = adapter.get_field(field_path)
        
        # Should return a non-None value for all valid paths
        assert value is not None
        assert isinstance(value, str)
        assert len(value) > 0

    
    @settings(max_examples=100)
    @given(
        base=st.text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=1, max_size=20),
        field=st.text(alphabet='abcdefghijklmnopqrstuvwxyz', min_size=1, max_size=20)
    )
    def test_property_meta_field_not_found_handling(self, base, field):
        """
        Feature: it-operation-template-extension, Property 3: Meta Field Not Found Handling
        
        For any meta placeholder referencing a non-existent field in the metadata configuration,
        the system should generate a warning and leave the placeholder unchanged.
        
        Validates: Requirements 16.4
        """
        sample_metadata_config = _create_sample_metadata_config()
        adapter = MetaAdapter(sample_metadata_config)
        adapter.connect()
        
        # Create an invalid field path (unlikely to exist)
        invalid_field_path = f"{base}_invalid.{field}_nonexistent"
        
        # Get field value - should return None for non-existent fields
        value = adapter.get_field(invalid_field_path)
        
        # Should return None for invalid paths
        assert value is None
