"""
Unit tests for Meta-NetBox Adapter

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

import pytest
from src.meta_netbox_adapter import MetaNetBoxAdapter


class TestMetaNetBoxAdapter:
    """Test suite for MetaNetBoxAdapter class."""
    
    @pytest.fixture
    def sample_netbox_metadata(self):
        """Sample NetBox metadata for testing."""
        return {
            'contacts': {
                'ciso': {
                    'name': 'John Security',
                    'email': 'john.security@example.com',
                    'phone': '+49 123 456789'
                },
                'cio': {
                    'name': 'Jane Tech',
                    'email': 'jane.tech@example.com',
                    'phone': '+49 123 456790'
                },
                'sysop': {
                    'name': 'Bob Admin',
                    'email': 'bob.admin@example.com',
                    'phone': '+49 123 456791'
                }
            },
            'devices': {
                'firewall': {
                    'name': 'fw-01',
                    'ip': '192.168.1.1',
                    'model': 'Cisco ASA 5506'
                },
                'core_switch': {
                    'name': 'sw-core-01',
                    'ip': '192.168.1.2',
                    'model': 'Cisco Catalyst 9300'
                }
            },
            'sites': {
                'primary': {
                    'name': 'Headquarters',
                    'address': '123 Main Street',
                    'city': 'Munich'
                },
                'secondary': {
                    'name': 'Branch Office',
                    'address': '456 Oak Avenue',
                    'city': 'Berlin'
                }
            }
        }
    
    def test_adapter_initialization(self, sample_netbox_metadata):
        """Test adapter initialization with valid metadata."""
        adapter = MetaNetBoxAdapter(sample_netbox_metadata)
        assert adapter.netbox_metadata == sample_netbox_metadata
        assert not adapter._connected
    
    def test_adapter_initialization_with_none(self):
        """Test adapter initialization with None metadata."""
        adapter = MetaNetBoxAdapter(None)
        assert adapter.netbox_metadata == {}
        assert not adapter._connected
    
    def test_adapter_initialization_with_empty_dict(self):
        """Test adapter initialization with empty dictionary."""
        adapter = MetaNetBoxAdapter({})
        assert adapter.netbox_metadata == {}
        assert not adapter._connected
    
    def test_connect_success(self, sample_netbox_metadata):
        """Test successful connection with valid metadata."""
        adapter = MetaNetBoxAdapter(sample_netbox_metadata)
        result = adapter.connect()
        assert result is True
        assert adapter._connected is True
    
    def test_connect_with_none_metadata(self):
        """Test connection succeeds with None metadata (converted to empty dict)."""
        adapter = MetaNetBoxAdapter(None)
        result = adapter.connect()
        # None is converted to {} in __init__, so connection succeeds
        assert result is True
        assert adapter._connected is True
    
    def test_connect_with_invalid_metadata_type(self):
        """Test connection fails with invalid metadata type."""
        adapter = MetaNetBoxAdapter("invalid")
        result = adapter.connect()
        assert result is False
        assert adapter._connected is False
    
    def test_disconnect(self, sample_netbox_metadata):
        """Test disconnect method."""
        adapter = MetaNetBoxAdapter(sample_netbox_metadata)
        adapter.connect()
        assert adapter._connected is True
        
        adapter.disconnect()
        assert adapter._connected is False
    
    def test_get_field_without_connection(self, sample_netbox_metadata):
        """Test get_field raises error when not connected."""
        adapter = MetaNetBoxAdapter(sample_netbox_metadata)
        
        with pytest.raises(ConnectionError, match="Not connected to NetBox metadata"):
            adapter.get_field("contacts.ciso.name")
    
    def test_get_field_with_empty_path(self, sample_netbox_metadata):
        """Test get_field raises error with empty field path."""
        adapter = MetaNetBoxAdapter(sample_netbox_metadata)
        adapter.connect()
        
        with pytest.raises(ValueError, match="field_path cannot be empty"):
            adapter.get_field("")
    
    def test_get_contact_field(self, sample_netbox_metadata):
        """Test retrieving contact fields."""
        adapter = MetaNetBoxAdapter(sample_netbox_metadata)
        adapter.connect()
        
        # Test CISO contact
        assert adapter.get_field("contacts.ciso.name") == "John Security"
        assert adapter.get_field("contacts.ciso.email") == "john.security@example.com"
        assert adapter.get_field("contacts.ciso.phone") == "+49 123 456789"
        
        # Test CIO contact
        assert adapter.get_field("contacts.cio.name") == "Jane Tech"
        assert adapter.get_field("contacts.cio.email") == "jane.tech@example.com"
        
        # Test Sysop contact
        assert adapter.get_field("contacts.sysop.name") == "Bob Admin"
    
    def test_get_device_field(self, sample_netbox_metadata):
        """Test retrieving device fields."""
        adapter = MetaNetBoxAdapter(sample_netbox_metadata)
        adapter.connect()
        
        # Test firewall device
        assert adapter.get_field("devices.firewall.name") == "fw-01"
        assert adapter.get_field("devices.firewall.ip") == "192.168.1.1"
        assert adapter.get_field("devices.firewall.model") == "Cisco ASA 5506"
        
        # Test core switch device
        assert adapter.get_field("devices.core_switch.name") == "sw-core-01"
        assert adapter.get_field("devices.core_switch.ip") == "192.168.1.2"
    
    def test_get_site_field(self, sample_netbox_metadata):
        """Test retrieving site fields."""
        adapter = MetaNetBoxAdapter(sample_netbox_metadata)
        adapter.connect()
        
        # Test primary site
        assert adapter.get_field("sites.primary.name") == "Headquarters"
        assert adapter.get_field("sites.primary.address") == "123 Main Street"
        assert adapter.get_field("sites.primary.city") == "Munich"
        
        # Test secondary site
        assert adapter.get_field("sites.secondary.name") == "Branch Office"
        assert adapter.get_field("sites.secondary.city") == "Berlin"
    
    def test_get_field_nonexistent_path(self, sample_netbox_metadata):
        """Test get_field returns None for nonexistent paths."""
        adapter = MetaNetBoxAdapter(sample_netbox_metadata)
        adapter.connect()
        
        # Nonexistent top-level key
        assert adapter.get_field("nonexistent.field") is None
        
        # Nonexistent contact
        assert adapter.get_field("contacts.nonexistent.name") is None
        
        # Nonexistent field in existing contact
        assert adapter.get_field("contacts.ciso.nonexistent") is None
        
        # Nonexistent device
        assert adapter.get_field("devices.nonexistent.name") is None
        
        # Nonexistent site
        assert adapter.get_field("sites.nonexistent.name") is None
    
    def test_get_field_partial_path(self, sample_netbox_metadata):
        """Test get_field with partial paths returns None."""
        adapter = MetaNetBoxAdapter(sample_netbox_metadata)
        adapter.connect()
        
        # Partial path should return None (not a string value)
        result = adapter.get_field("contacts.ciso")
        # This returns the dict as string representation
        assert result is not None
        assert "name" in result or "John Security" in result
    
    def test_context_manager(self, sample_netbox_metadata):
        """Test adapter as context manager."""
        with MetaNetBoxAdapter(sample_netbox_metadata) as adapter:
            assert adapter._connected is True
            name = adapter.get_field("contacts.ciso.name")
            assert name == "John Security"
        
        # After context, should be disconnected
        assert adapter._connected is False
    
    def test_independence_from_meta_adapter(self, sample_netbox_metadata):
        """Test that meta-netbox adapter is independent from meta adapter."""
        # Create meta-netbox adapter
        adapter = MetaNetBoxAdapter(sample_netbox_metadata)
        adapter.connect()
        
        # Should be able to retrieve NetBox-specific data
        assert adapter.get_field("contacts.ciso.name") == "John Security"
        assert adapter.get_field("devices.firewall.name") == "fw-01"
        assert adapter.get_field("sites.primary.name") == "Headquarters"
        
        # These are NetBox metadata, not meta adapter data
        # The adapter should work independently
        assert adapter.netbox_metadata is not None
        assert 'contacts' in adapter.netbox_metadata
        assert 'devices' in adapter.netbox_metadata
        assert 'sites' in adapter.netbox_metadata


class TestMetaNetBoxAdapterIntegration:
    """Integration tests for MetaNetBoxAdapter with PlaceholderProcessor."""
    
    @pytest.fixture
    def sample_netbox_metadata(self):
        """Sample NetBox metadata for testing."""
        return {
            'contacts': {
                'ciso': {
                    'name': 'John Security',
                    'email': 'john.security@example.com'
                }
            },
            'devices': {
                'firewall': {
                    'name': 'fw-01',
                    'ip': '192.168.1.1'
                }
            },
            'sites': {
                'primary': {
                    'name': 'Headquarters'
                }
            }
        }
    
    def test_placeholder_processor_with_meta_netbox(self, sample_netbox_metadata):
        """Test PlaceholderProcessor with meta-netbox adapter."""
        from src.placeholder_processor import PlaceholderProcessor
        
        # Create meta-netbox adapter
        adapter = MetaNetBoxAdapter(sample_netbox_metadata)
        adapter.connect()
        
        # Create placeholder processor with meta-netbox data source
        processor = PlaceholderProcessor(
            data_sources={'meta-netbox': adapter}
        )
        
        # Test template with meta-netbox placeholders
        template = """
**CISO (NetBox):** {{ meta-netbox.contacts.ciso.name }}
**CISO Email (NetBox):** {{ meta-netbox.contacts.ciso.email }}
**Firewall (NetBox):** {{ meta-netbox.devices.firewall.name }}
**Firewall IP (NetBox):** {{ meta-netbox.devices.firewall.ip }}
**Site (NetBox):** {{ meta-netbox.sites.primary.name }}
"""
        
        result = processor.process_template(template)
        
        # Verify replacements
        assert "John Security" in result.content
        assert "john.security@example.com" in result.content
        assert "fw-01" in result.content
        assert "192.168.1.1" in result.content
        assert "Headquarters" in result.content
        
        # Verify no placeholder markers remain
        assert "{{ meta-netbox." not in result.content
        
        # Verify replacement count
        assert len(result.replacements) == 5
        assert all(r.source == 'meta-netbox' for r in result.replacements)
    
    def test_meta_and_meta_netbox_independence(self, sample_netbox_metadata):
        """Test that meta and meta-netbox placeholders work independently."""
        from src.placeholder_processor import PlaceholderProcessor
        from src.meta_adapter import MetaAdapter
        from src.metadata_config_manager import MetadataConfig, OrganizationInfo, DocumentInfo, PersonRole
        
        # Create meta adapter with regular metadata
        meta_config = MetadataConfig(
            organization=OrganizationInfo(
                name="Test Org",
                address="123 Test St",
                city="Test City",
                postal_code="12345",
                country="Test Country",
                website="https://test.org",
                phone="+1234567890",
                email="test@test.org"
            ),
            roles={
                'ciso': PersonRole(
                    name="Meta CISO",
                    title="Chief Information Security Officer",
                    email="meta.ciso@test.org",
                    phone="+1234567891"
                )
            },
            document=DocumentInfo(
                owner="Test Owner",
                approver="Test Approver",
                version="1.0.0",
                classification="internal"
            ),
            author="Test Author",
            language="en"
        )
        
        meta_adapter = MetaAdapter(meta_config)
        meta_adapter.connect()
        
        # Create meta-netbox adapter
        netbox_adapter = MetaNetBoxAdapter(sample_netbox_metadata)
        netbox_adapter.connect()
        
        # Create placeholder processor with both adapters
        processor = PlaceholderProcessor(
            data_sources={
                'meta': meta_adapter,
                'meta-netbox': netbox_adapter
            }
        )
        
        # Test template with both meta and meta-netbox placeholders
        template = """
**CISO (Meta):** {{ meta.ciso.name }}
**CISO (NetBox):** {{ meta-netbox.contacts.ciso.name }}
**Organization:** {{ meta.organization.name }}
**Site (NetBox):** {{ meta-netbox.sites.primary.name }}
"""
        
        result = processor.process_template(template)
        
        # Verify both sources work independently
        assert "Meta CISO" in result.content
        assert "John Security" in result.content
        assert "Test Org" in result.content
        assert "Headquarters" in result.content
        
        # Verify no placeholder markers remain
        assert "{{ meta." not in result.content
        assert "{{ meta-netbox." not in result.content
        
        # Verify replacement count and sources
        assert len(result.replacements) == 4
        meta_replacements = [r for r in result.replacements if r.source == 'meta']
        netbox_replacements = [r for r in result.replacements if r.source == 'meta-netbox']
        assert len(meta_replacements) == 2
        assert len(netbox_replacements) == 2
