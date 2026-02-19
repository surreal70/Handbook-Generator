"""
Unit tests for Meta Adapter

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
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



class TestMetaAdapterServiceProcessExtension:
    """Test MetaAdapter service and process extensions."""
    
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
    
    def test_set_service_type_initializes_attributes(self, sample_metadata_config):
        """Test that set_service_type initializes service type attributes."""
        adapter = MetaAdapter(sample_metadata_config)
        adapter.connect()
        
        # Set service type
        adapter.set_service_type('generic-service-template', 'de')
        
        # Verify attributes are set
        assert adapter._current_service_type == 'generic-service-template'
        # Config may be None if files don't exist, but attribute should be set
        assert hasattr(adapter, '_service_config')
        assert hasattr(adapter, '_global_service_config')
    
    def test_set_process_type_initializes_attributes(self, sample_metadata_config):
        """Test that set_process_type initializes process type attributes."""
        adapter = MetaAdapter(sample_metadata_config)
        adapter.connect()
        
        # Set process type
        adapter.set_process_type('generic-process-template', 'de')
        
        # Verify attributes are set
        assert adapter._current_process_type == 'generic-process-template'
        # Config may be None if files don't exist, but attribute should be set
        assert hasattr(adapter, '_process_config')
        assert hasattr(adapter, '_global_process_config')
    
    def test_service_field_resolution_with_existing_config(self, sample_metadata_config, tmp_path):
        """Test service field resolution when config files exist."""
        import yaml
        from pathlib import Path
        
        # Create temporary service config structure
        service_dir = tmp_path / 'services' / 'de' / 'test-service'
        service_dir.mkdir(parents=True)
        
        # Create meta-service.yaml
        service_config = {
            'service': {
                'id': 'SVC-001',
                'name': 'Test Service',
                'category': 'infrastructure',
                'criticality': 'High'
            }
        }
        with open(service_dir / 'meta-service.yaml', 'w') as f:
            yaml.dump(service_config, f)
        
        # Create global service config
        global_service_config = {
            'service': {
                'default_sla': '99.5%'
            }
        }
        with open(tmp_path / 'services' / 'de' / 'meta-global-service.yaml', 'w') as f:
            yaml.dump(global_service_config, f)
        
        # Change to tmp directory for testing
        import os
        original_dir = os.getcwd()
        try:
            os.chdir(tmp_path)
            
            adapter = MetaAdapter(sample_metadata_config)
            adapter.connect()
            adapter.set_service_type('test-service', 'de')
            
            # Test service-specific field resolution
            assert adapter.get_field('service.id') == 'SVC-001'
            assert adapter.get_field('service.name') == 'Test Service'
            assert adapter.get_field('service.category') == 'infrastructure'
            
            # Test global service field resolution
            assert adapter.get_field('service.default_sla') == '99.5%'
        finally:
            os.chdir(original_dir)
    
    def test_process_field_resolution_with_existing_config(self, sample_metadata_config, tmp_path):
        """Test process field resolution when config files exist."""
        import yaml
        from pathlib import Path
        
        # Create temporary process config structure
        process_dir = tmp_path / 'processes' / 'de' / 'test-process'
        process_dir.mkdir(parents=True)
        
        # Create meta-process.yaml
        process_config = {
            'process': {
                'id': 'PROC-001',
                'name': 'Test Process',
                'category': 'core',
                'criticality': 'Critical'
            }
        }
        with open(process_dir / 'meta-process.yaml', 'w') as f:
            yaml.dump(process_config, f)
        
        # Create global process config
        global_process_config = {
            'process': {
                'default_escalation': 'Level 1'
            }
        }
        with open(tmp_path / 'processes' / 'de' / 'meta-global-process.yaml', 'w') as f:
            yaml.dump(global_process_config, f)
        
        # Change to tmp directory for testing
        import os
        original_dir = os.getcwd()
        try:
            os.chdir(tmp_path)
            
            adapter = MetaAdapter(sample_metadata_config)
            adapter.connect()
            adapter.set_process_type('test-process', 'de')
            
            # Test process-specific field resolution
            assert adapter.get_field('process.id') == 'PROC-001'
            assert adapter.get_field('process.name') == 'Test Process'
            assert adapter.get_field('process.category') == 'core'
            
            # Test global process field resolution
            assert adapter.get_field('process.default_escalation') == 'Level 1'
        finally:
            os.chdir(original_dir)
    
    def test_hierarchical_resolution_priority(self, sample_metadata_config, tmp_path):
        """Test that service-specific config overrides global config."""
        import yaml
        import os
        
        # Create service config structure
        service_dir = tmp_path / 'services' / 'de' / 'test-service'
        service_dir.mkdir(parents=True)
        
        # Create meta-service.yaml with specific value
        service_config = {
            'service': {
                'sla': '99.9%'  # Specific value
            }
        }
        with open(service_dir / 'meta-service.yaml', 'w') as f:
            yaml.dump(service_config, f)
        
        # Create global service config with default value
        global_service_config = {
            'service': {
                'sla': '99.5%'  # Default value
            }
        }
        with open(tmp_path / 'services' / 'de' / 'meta-global-service.yaml', 'w') as f:
            yaml.dump(global_service_config, f)
        
        original_dir = os.getcwd()
        try:
            os.chdir(tmp_path)
            
            adapter = MetaAdapter(sample_metadata_config)
            adapter.connect()
            adapter.set_service_type('test-service', 'de')
            
            # Should return service-specific value, not global
            assert adapter.get_field('service.sla') == '99.9%'
        finally:
            os.chdir(original_dir)
    
    def test_fallback_to_organization_fields(self, sample_metadata_config):
        """Test that organization fields still work with service/process types set."""
        adapter = MetaAdapter(sample_metadata_config)
        adapter.connect()
        
        # Set service type
        adapter.set_service_type('generic-service-template', 'de')
        
        # Organization fields should still resolve
        assert adapter.get_field('organization.name') == 'Test Organization'
        assert adapter.get_field('organization.email') == 'info@test.com'
    
    def test_fallback_to_role_fields(self, sample_metadata_config):
        """Test that role fields still work with service/process types set."""
        adapter = MetaAdapter(sample_metadata_config)
        adapter.connect()
        
        # Set process type
        adapter.set_process_type('generic-process-template', 'de')
        
        # Role fields should still resolve
        assert adapter.get_field('ceo.name') == 'John Doe'
        assert adapter.get_field('cio.email') == 'jane@test.com'
    
    def test_nested_value_extraction(self, sample_metadata_config):
        """Test _get_nested_value helper method."""
        adapter = MetaAdapter(sample_metadata_config)
        
        test_config = {
            'service': {
                'sla': {
                    'availability': '99.9%',
                    'response_time': {
                        'p1': '15 minutes'
                    }
                }
            }
        }
        
        # Test simple nested path
        assert adapter._get_nested_value(test_config, 'service.sla.availability') == '99.9%'
        
        # Test deeply nested path
        assert adapter._get_nested_value(test_config, 'service.sla.response_time.p1') == '15 minutes'
        
        # Test non-existent path
        assert adapter._get_nested_value(test_config, 'service.invalid.path') is None
    
    def test_config_caching(self, sample_metadata_config, tmp_path):
        """Test that YAML configs are cached after first load."""
        import yaml
        import os
        
        # Create service config
        service_dir = tmp_path / 'services' / 'de' / 'test-service'
        service_dir.mkdir(parents=True)
        
        service_config = {'service': {'id': 'SVC-001'}}
        config_path = service_dir / 'meta-service.yaml'
        with open(config_path, 'w') as f:
            yaml.dump(service_config, f)
        
        original_dir = os.getcwd()
        try:
            os.chdir(tmp_path)
            
            adapter = MetaAdapter(sample_metadata_config)
            adapter.connect()
            
            # First load
            adapter.set_service_type('test-service', 'de')
            # Cache key uses relative path from current directory
            cache_key = 'services/de/test-service/meta-service.yaml'
            assert cache_key in adapter._config_cache
            
            # Verify cached value
            cached_value = adapter._config_cache[cache_key]
            assert cached_value == service_config
            
            # Second load should use cache
            adapter.set_service_type('test-service', 'de')
            assert adapter._config_cache[cache_key] == cached_value
        finally:
            os.chdir(original_dir)
    
    def test_missing_config_files_handled_gracefully(self, sample_metadata_config, tmp_path):
        """Test that missing config files don't cause errors."""
        import os
        
        # Use a temporary directory with no service configs
        original_dir = os.getcwd()
        try:
            os.chdir(tmp_path)
            
            adapter = MetaAdapter(sample_metadata_config)
            adapter.connect()
            
            # Set service type with non-existent configs
            adapter.set_service_type('non-existent-service', 'de')
            
            # Should not raise error, configs should be None
            assert adapter._service_config is None
            assert adapter._global_service_config is None
            
            # Field resolution should return None
            assert adapter.get_field('service.id') is None
        finally:
            os.chdir(original_dir)
    
    def test_service_and_process_types_independent(self, sample_metadata_config, tmp_path):
        """Test that service and process types can be set independently."""
        import yaml
        import os
        
        # Create both service and process configs
        service_dir = tmp_path / 'services' / 'de' / 'test-service'
        service_dir.mkdir(parents=True)
        process_dir = tmp_path / 'processes' / 'de' / 'test-process'
        process_dir.mkdir(parents=True)
        
        service_config = {'service': {'id': 'SVC-001'}}
        with open(service_dir / 'meta-service.yaml', 'w') as f:
            yaml.dump(service_config, f)
        
        process_config = {'process': {'id': 'PROC-001'}}
        with open(process_dir / 'meta-process.yaml', 'w') as f:
            yaml.dump(process_config, f)
        
        original_dir = os.getcwd()
        try:
            os.chdir(tmp_path)
            
            adapter = MetaAdapter(sample_metadata_config)
            adapter.connect()
            
            # Set service type
            adapter.set_service_type('test-service', 'de')
            assert adapter.get_field('service.id') == 'SVC-001'
            assert adapter.get_field('process.id') is None
            
            # Set process type
            adapter.set_process_type('test-process', 'de')
            assert adapter.get_field('process.id') == 'PROC-001'
            # Service should still work
            assert adapter.get_field('service.id') == 'SVC-001'
        finally:
            os.chdir(original_dir)
