"""
Tests for placeholder resolution hierarchy in service and process documentation.

Tests the hierarchical resolution of placeholders across multiple configuration levels:
1. Service/Process-specific metadata (meta-service.yaml / meta-process.yaml)
2. Global service/process config (meta-global-service.yaml / meta-global-process.yaml)
3. Organization roles (meta-organisation-roles.yaml)
4. Organization metadata (meta-organisation.yaml)
5. Global metadata (meta-global.yaml)

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

import pytest
from pathlib import Path
import tempfile
import yaml

from src.meta_adapter import MetaAdapter
from src.metadata_config_manager import MetadataConfig, OrganizationInfo, PersonRole, DocumentInfo


def create_test_metadata_config():
    """Helper function to create test metadata configuration."""
    org_info = OrganizationInfo(
        name="Test Organization",
        address="Test Address",
        city="Test City",
        postal_code="12345",
        country="Germany",
        website="https://example.com",
        phone="+49 123 456789",
        email="test@example.com"
    )
    doc_info = DocumentInfo(
        owner="Test Owner",
        approver="Test Approver",
        version="1.0.0",
        classification="internal"
    )
    return MetadataConfig(
        organization=org_info,
        roles={},
        document=doc_info,
        author="Test Author",
        language="de"
    )


class TestServicePlaceholderHierarchy:
    """Tests for service placeholder resolution hierarchy."""
    
    def test_service_specific_overrides_global(self):
        """Test that service-specific metadata overrides global service config."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create service directory structure
            service_dir = Path(tmpdir) / 'services' / 'de' / 'test-service'
            service_dir.mkdir(parents=True)
            
            # Create global service config
            global_config = {
                'sla': {
                    'availability_target': '99.5%'
                }
            }
            global_config_path = Path(tmpdir) / 'services' / 'de' / 'meta-global-service.yaml'
            with open(global_config_path, 'w') as f:
                yaml.dump(global_config, f)
            
            # Create service-specific config (overrides global)
            service_config = {
                'service': {
                    'id': 'SVC-001',
                    'sla': {
                        'availability_target': '99.9%'  # Override
                    }
                }
            }
            service_config_path = service_dir / 'meta-service.yaml'
            with open(service_config_path, 'w') as f:
                yaml.dump(service_config, f)
            
            # Create metadata config
            org_info = OrganizationInfo(
                name="Test Organization",
                address="Test Address",
                phone="+49 123 456789",
                email="test@example.com",
                web="https://example.com"
            )
            metadata_config = MetadataConfig(organization=org_config)
            
            # Test resolution
            adapter = MetaAdapter(metadata_config, language='de')
            adapter.connect()
            adapter.set_service_type('test-service', 'de')
            
            # Should get service-specific value, not global
            value = adapter.get_field('service.sla.availability_target')
            assert value == '99.9%', "Service-specific value should override global"
    
    def test_global_service_fallback(self):
        """Test that global service config is used when service-specific is missing."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create service directory structure
            service_dir = Path(tmpdir) / 'services' / 'de' / 'test-service'
            service_dir.mkdir(parents=True)
            
            # Create global service config
            global_config = {
                'support': {
                    'business_hours': 'Mo-Fr 08:00-18:00 CET'
                }
            }
            global_config_path = Path(tmpdir) / 'services' / 'de' / 'meta-global-service.yaml'
            with open(global_config_path, 'w') as f:
                yaml.dump(global_config, f)
            
            # Create service-specific config (without support section)
            service_config = {
                'service': {
                    'id': 'SVC-001',
                    'name': 'Test Service'
                }
            }
            service_config_path = service_dir / 'meta-service.yaml'
            with open(service_config_path, 'w') as f:
                yaml.dump(service_config, f)
            
            # Create metadata config
            org_info = OrganizationInfo(
                name="Test Organization",
                address="Test Address",
                phone="+49 123 456789",
                email="test@example.com",
                web="https://example.com"
            )
            metadata_config = MetadataConfig(organization=org_config)
            
            # Test resolution
            adapter = MetaAdapter(metadata_config, language='de')
            adapter.connect()
            adapter.set_service_type('test-service', 'de')
            
            # Should fall back to global value
            value = adapter.get_field('support.business_hours')
            assert value == 'Mo-Fr 08:00-18:00 CET', "Should fall back to global config"
    
    def test_organization_metadata_fallback(self):
        """Test that organization metadata is accessible from service context."""
        # Create metadata config
        org_info = OrganizationInfo(
            name="Test Organization",
            address="Test Address",
            phone="+49 123 456789",
            email="test@example.com",
            web="https://example.com"
        )
        metadata_config = MetadataConfig(organization=org_config)
        
        adapter = MetaAdapter(metadata_config, language='de')
        adapter.connect()
        
        # Even without setting service type, org data should be accessible
        org_name = adapter.get_field('organization.name')
        assert org_name == "Test Organization"


class TestProcessPlaceholderHierarchy:
    """Tests for process placeholder resolution hierarchy."""
    
    def test_process_specific_overrides_global(self):
        """Test that process-specific metadata overrides global process config."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create process directory structure
            process_dir = Path(tmpdir) / 'processes' / 'de' / 'test-process'
            process_dir.mkdir(parents=True)
            
            # Create global process config
            global_config = {
                'kpis': {
                    'process_efficiency': 'Cycle time reduction'
                }
            }
            global_config_path = Path(tmpdir) / 'processes' / 'de' / 'meta-global-process.yaml'
            with open(global_config_path, 'w') as f:
                yaml.dump(global_config, f)
            
            # Create process-specific config (overrides global)
            process_config = {
                'process': {
                    'id': 'PROC-001',
                    'kpis': {
                        'process_efficiency': 'Custom efficiency metric'  # Override
                    }
                }
            }
            process_config_path = process_dir / 'meta-process.yaml'
            with open(process_config_path, 'w') as f:
                yaml.dump(process_config, f)
            
            # Create metadata config
            org_info = OrganizationInfo(
                name="Test Organization",
                address="Test Address",
                phone="+49 123 456789",
                email="test@example.com",
                web="https://example.com"
            )
            metadata_config = MetadataConfig(organization=org_config)
            
            # Test resolution
            adapter = MetaAdapter(metadata_config, language='de')
            adapter.connect()
            adapter.set_process_type('test-process', 'de')
            
            # Should get process-specific value, not global
            value = adapter.get_field('process.kpis.process_efficiency')
            assert value == 'Custom efficiency metric', "Process-specific value should override global"
    
    def test_global_process_fallback(self):
        """Test that global process config is used when process-specific is missing."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create process directory structure
            process_dir = Path(tmpdir) / 'processes' / 'de' / 'test-process'
            process_dir.mkdir(parents=True)
            
            # Create global process config
            global_config = {
                'escalation': {
                    'level_1': 'IT Manager',
                    'level_2': 'Risk Manager'
                }
            }
            global_config_path = Path(tmpdir) / 'processes' / 'de' / 'meta-global-process.yaml'
            with open(global_config_path, 'w') as f:
                yaml.dump(global_config, f)
            
            # Create process-specific config (without escalation section)
            process_config = {
                'process': {
                    'id': 'PROC-001',
                    'name': 'Test Process'
                }
            }
            process_config_path = process_dir / 'meta-process.yaml'
            with open(process_config_path, 'w') as f:
                yaml.dump(process_config, f)
            
            # Create metadata config
            org_info = OrganizationInfo(
                name="Test Organization",
                address="Test Address",
                phone="+49 123 456789",
                email="test@example.com",
                web="https://example.com"
            )
            metadata_config = MetadataConfig(organization=org_config)
            
            # Test resolution
            adapter = MetaAdapter(metadata_config, language='de')
            adapter.connect()
            adapter.set_process_type('test-process', 'de')
            
            # Should fall back to global value
            value = adapter.get_field('escalation.level_1')
            assert value == 'IT Manager', "Should fall back to global config"


class TestNestedPlaceholderResolution:
    """Tests for nested placeholder resolution."""
    
    def test_deeply_nested_service_placeholder(self):
        """Test resolution of deeply nested service placeholders."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create service directory structure
            service_dir = Path(tmpdir) / 'services' / 'de' / 'test-service'
            service_dir.mkdir(parents=True)
            
            # Create service config with nested structure
            service_config = {
                'service': {
                    'technology': {
                        'platform': {
                            'name': 'Microsoft Exchange',
                            'version': '2019'
                        }
                    }
                }
            }
            service_config_path = service_dir / 'meta-service.yaml'
            with open(service_config_path, 'w') as f:
                yaml.dump(service_config, f)
            
            # Create metadata config
            org_info = OrganizationInfo(
                name="Test Organization",
                address="Test Address",
                phone="+49 123 456789",
                email="test@example.com",
                web="https://example.com"
            )
            metadata_config = MetadataConfig(organization=org_config)
            
            # Test resolution
            adapter = MetaAdapter(metadata_config, language='de')
            adapter.connect()
            adapter.set_service_type('test-service', 'de')
            
            # Should resolve deeply nested value
            value = adapter.get_field('service.technology.platform.name')
            assert value == 'Microsoft Exchange'
            
            version = adapter.get_field('service.technology.platform.version')
            assert version == '2019'
    
    def test_deeply_nested_process_placeholder(self):
        """Test resolution of deeply nested process placeholders."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create process directory structure
            process_dir = Path(tmpdir) / 'processes' / 'de' / 'test-process'
            process_dir.mkdir(parents=True)
            
            # Create process config with nested structure
            process_config = {
                'process': {
                    'raci': {
                        'incident_detection': {
                            'responsible': 'System Administrator',
                            'accountable': 'IT Manager',
                            'consulted': 'CISO',
                            'informed': 'CIO'
                        }
                    }
                }
            }
            process_config_path = process_dir / 'meta-process.yaml'
            with open(process_config_path, 'w') as f:
                yaml.dump(process_config, f)
            
            # Create metadata config
            org_info = OrganizationInfo(
                name="Test Organization",
                address="Test Address",
                phone="+49 123 456789",
                email="test@example.com",
                web="https://example.com"
            )
            metadata_config = MetadataConfig(organization=org_config)
            
            # Test resolution
            adapter = MetaAdapter(metadata_config, language='de')
            adapter.connect()
            adapter.set_process_type('test-process', 'de')
            
            # Should resolve deeply nested values
            responsible = adapter.get_field('process.raci.incident_detection.responsible')
            assert responsible == 'System Administrator'
            
            accountable = adapter.get_field('process.raci.incident_detection.accountable')
            assert accountable == 'IT Manager'


class TestMissingPlaceholderHandling:
    """Tests for handling missing placeholders in hierarchy."""
    
    def test_missing_service_placeholder_returns_none(self):
        """Test that missing service placeholder returns None."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create service directory structure
            service_dir = Path(tmpdir) / 'services' / 'de' / 'test-service'
            service_dir.mkdir(parents=True)
            
            # Create minimal service config
            service_config = {
                'service': {
                    'id': 'SVC-001'
                }
            }
            service_config_path = service_dir / 'meta-service.yaml'
            with open(service_config_path, 'w') as f:
                yaml.dump(service_config, f)
            
            # Create metadata config
            org_info = OrganizationInfo(
                name="Test Organization",
                address="Test Address",
                phone="+49 123 456789",
                email="test@example.com",
                web="https://example.com"
            )
            metadata_config = MetadataConfig(organization=org_config)
            
            # Test resolution
            adapter = MetaAdapter(metadata_config, language='de')
            adapter.connect()
            adapter.set_service_type('test-service', 'de')
            
            # Should return None for missing field
            value = adapter.get_field('service.nonexistent.field')
            assert value is None
    
    def test_missing_process_placeholder_returns_none(self):
        """Test that missing process placeholder returns None."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create process directory structure
            process_dir = Path(tmpdir) / 'processes' / 'de' / 'test-process'
            process_dir.mkdir(parents=True)
            
            # Create minimal process config
            process_config = {
                'process': {
                    'id': 'PROC-001'
                }
            }
            process_config_path = process_dir / 'meta-process.yaml'
            with open(process_config_path, 'w') as f:
                yaml.dump(process_config, f)
            
            # Create metadata config
            org_info = OrganizationInfo(
                name="Test Organization",
                address="Test Address",
                phone="+49 123 456789",
                email="test@example.com",
                web="https://example.com"
            )
            metadata_config = MetadataConfig(organization=org_config)
            
            # Test resolution
            adapter = MetaAdapter(metadata_config, language='de')
            adapter.connect()
            adapter.set_process_type('test-process', 'de')
            
            # Should return None for missing field
            value = adapter.get_field('process.nonexistent.field')
            assert value is None


class TestConfigurationCaching:
    """Tests for configuration file caching."""
    
    def test_service_config_cached(self):
        """Test that service configuration is cached."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create service directory structure
            service_dir = Path(tmpdir) / 'services' / 'de' / 'test-service'
            service_dir.mkdir(parents=True)
            
            # Create service config
            service_config = {
                'service': {
                    'id': 'SVC-001',
                    'name': 'Test Service'
                }
            }
            service_config_path = service_dir / 'meta-service.yaml'
            with open(service_config_path, 'w') as f:
                yaml.dump(service_config, f)
            
            # Create metadata config
            org_info = OrganizationInfo(
                name="Test Organization",
                address="Test Address",
                phone="+49 123 456789",
                email="test@example.com",
                web="https://example.com"
            )
            metadata_config = MetadataConfig(organization=org_config)
            
            # Test caching
            adapter = MetaAdapter(metadata_config, language='de')
            adapter.connect()
            adapter.set_service_type('test-service', 'de')
            
            # First access
            value1 = adapter.get_field('service.id')
            
            # Modify file (should not affect cached value)
            service_config['service']['id'] = 'SVC-999'
            with open(service_config_path, 'w') as f:
                yaml.dump(service_config, f)
            
            # Second access (should use cached value)
            value2 = adapter.get_field('service.id')
            
            # Both should return original cached value
            assert value1 == 'SVC-001'
            assert value2 == 'SVC-001'
    
    def test_process_config_cached(self):
        """Test that process configuration is cached."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create process directory structure
            process_dir = Path(tmpdir) / 'processes' / 'de' / 'test-process'
            process_dir.mkdir(parents=True)
            
            # Create process config
            process_config = {
                'process': {
                    'id': 'PROC-001',
                    'name': 'Test Process'
                }
            }
            process_config_path = process_dir / 'meta-process.yaml'
            with open(process_config_path, 'w') as f:
                yaml.dump(process_config, f)
            
            # Create metadata config
            org_info = OrganizationInfo(
                name="Test Organization",
                address="Test Address",
                phone="+49 123 456789",
                email="test@example.com",
                web="https://example.com"
            )
            metadata_config = MetadataConfig(organization=org_config)
            
            # Test caching
            adapter = MetaAdapter(metadata_config, language='de')
            adapter.connect()
            adapter.set_process_type('test-process', 'de')
            
            # First access
            value1 = adapter.get_field('process.id')
            
            # Modify file (should not affect cached value)
            process_config['process']['id'] = 'PROC-999'
            with open(process_config_path, 'w') as f:
                yaml.dump(process_config, f)
            
            # Second access (should use cached value)
            value2 = adapter.get_field('process.id')
            
            # Both should return original cached value
            assert value1 == 'PROC-001'
            assert value2 == 'PROC-001'
