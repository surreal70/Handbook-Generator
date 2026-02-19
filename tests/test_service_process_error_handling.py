"""
Tests for error handling in service and process documentation generation.

Tests various error scenarios including missing files, invalid YAML,
permission errors, and graceful degradation.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

import pytest
from pathlib import Path
import tempfile
import yaml
import os

from src.template_manager import TemplateManager
from src.meta_adapter import MetaAdapter
from src.placeholder_processor import PlaceholderProcessor
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


class TestMissingFileHandling:
    """Tests for handling missing files."""
    
    def test_missing_service_directory(self):
        """Test handling of missing service directory."""
        manager = TemplateManager(Path('nonexistent/services'))
        services = manager.discover_services()
        
        # Should return empty dict, not raise error
        assert services == {}
        assert isinstance(services, dict)
    
    def test_missing_process_directory(self):
        """Test handling of missing process directory."""
        manager = TemplateManager(Path('nonexistent/processes'))
        processes = manager.discover_processes()
        
        # Should return empty dict, not raise error
        assert processes == {}
        assert isinstance(processes, dict)
    
    def test_missing_service_metadata_file(self):
        """Test handling of missing service metadata file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create service directory without metadata
            service_dir = Path(tmpdir) / 'services' / 'de' / 'test-service'
            service_dir.mkdir(parents=True)
            (service_dir / 'service-template.md').write_text('# Test Service')
            
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
            
            # Should handle missing metadata gracefully
            adapter.set_service_type('test-service', 'de')
            
            # Service config should be None
            assert adapter._service_config is None
    
    def test_missing_process_metadata_file(self):
        """Test handling of missing process metadata file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create process directory without metadata
            process_dir = Path(tmpdir) / 'processes' / 'de' / 'test-process'
            process_dir.mkdir(parents=True)
            (process_dir / 'process-template.md').write_text('# Test Process')
            
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
            
            # Should handle missing metadata gracefully
            adapter.set_process_type('test-process', 'de')
            
            # Process config should be None
            assert adapter._process_config is None
    
    def test_missing_global_service_config(self):
        """Test handling of missing global service config."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create service directory without global config
            service_dir = Path(tmpdir) / 'services' / 'de' / 'test-service'
            service_dir.mkdir(parents=True)
            
            # Create service-specific config only
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
            
            adapter = MetaAdapter(metadata_config, language='de')
            adapter.connect()
            
            # Should handle missing global config gracefully
            adapter.set_service_type('test-service', 'de')
            
            # Service config should be loaded
            assert adapter._service_config is not None
            # Global config should be None
            assert adapter._global_service_config is None
    
    def test_missing_template_file(self):
        """Test handling of missing template file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create service directory
            service_dir = Path(tmpdir) / 'services' / 'de' / 'test-service'
            service_dir.mkdir(parents=True)
            
            # Create metadata but no template
            service_config = {
                'service': {
                    'id': 'SVC-001'
                }
            }
            service_config_path = service_dir / 'meta-service.yaml'
            with open(service_config_path, 'w') as f:
                yaml.dump(service_config, f)
            
            manager = TemplateManager(Path(tmpdir) / 'services')
            
            # Should discover service even without template
            services = manager.discover_services()
            assert 'de' in services
            # But should have no templates
            assert len(services['de'].get('test-service', [])) == 0


class TestInvalidYAMLHandling:
    """Tests for handling invalid YAML files."""
    
    def test_invalid_service_yaml_syntax(self):
        """Test handling of invalid YAML syntax in service metadata."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create service directory with invalid YAML
            service_dir = Path(tmpdir) / 'services' / 'de' / 'test-service'
            service_dir.mkdir(parents=True)
            (service_dir / 'meta-service.yaml').write_text('invalid: yaml: content: [')
            
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
            
            # Should handle invalid YAML gracefully
            adapter.set_service_type('test-service', 'de')
            
            # Service config should be None due to YAML error
            assert adapter._service_config is None
    
    def test_invalid_process_yaml_syntax(self):
        """Test handling of invalid YAML syntax in process metadata."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create process directory with invalid YAML
            process_dir = Path(tmpdir) / 'processes' / 'de' / 'test-process'
            process_dir.mkdir(parents=True)
            (process_dir / 'meta-process.yaml').write_text('invalid: yaml: content: {')
            
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
            
            # Should handle invalid YAML gracefully
            adapter.set_process_type('test-process', 'de')
            
            # Process config should be None due to YAML error
            assert adapter._process_config is None
    
    def test_invalid_global_service_yaml(self):
        """Test handling of invalid YAML in global service config."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create service directory
            service_dir = Path(tmpdir) / 'services' / 'de' / 'test-service'
            service_dir.mkdir(parents=True)
            
            # Create invalid global config
            global_config_path = Path(tmpdir) / 'services' / 'de' / 'meta-global-service.yaml'
            global_config_path.write_text('invalid: yaml: [[[')
            
            # Create valid service config
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
            
            adapter = MetaAdapter(metadata_config, language='de')
            adapter.connect()
            
            # Should handle invalid global YAML gracefully
            adapter.set_service_type('test-service', 'de')
            
            # Service config should be loaded
            assert adapter._service_config is not None
            # Global config should be None due to YAML error
            assert adapter._global_service_config is None


class TestInvalidDataHandling:
    """Tests for handling invalid data structures."""
    
    def test_service_yaml_wrong_structure(self):
        """Test handling of YAML with wrong structure."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create service directory with wrong structure
            service_dir = Path(tmpdir) / 'services' / 'de' / 'test-service'
            service_dir.mkdir(parents=True)
            
            # Create YAML with unexpected structure
            service_config = {
                'wrong_key': {
                    'nested': 'value'
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
            
            adapter = MetaAdapter(metadata_config, language='de')
            adapter.connect()
            adapter.set_service_type('test-service', 'de')
            
            # Should load config but return None for missing fields
            value = adapter.get_field('service.id')
            assert value is None
    
    def test_empty_service_yaml(self):
        """Test handling of empty YAML file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create service directory with empty YAML
            service_dir = Path(tmpdir) / 'services' / 'de' / 'test-service'
            service_dir.mkdir(parents=True)
            (service_dir / 'meta-service.yaml').write_text('')
            
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
            
            # Should handle empty YAML gracefully
            adapter.set_service_type('test-service', 'de')
            
            # Config should be None or empty
            assert adapter._service_config is None or adapter._service_config == {}


class TestNonexistentResourceHandling:
    """Tests for handling non-existent resources."""
    
    def test_get_nonexistent_service(self):
        """Test error when getting non-existent service."""
        manager = TemplateManager(Path('services'))
        
        with pytest.raises(ValueError, match="Service .* not found"):
            manager.get_services('de', 'nonexistent-service')
    
    def test_get_nonexistent_process(self):
        """Test error when getting non-existent process."""
        manager = TemplateManager(Path('processes'))
        
        with pytest.raises(ValueError, match="Process .* not found"):
            manager.get_processes('de', 'nonexistent-process')
    
    def test_get_service_nonexistent_language(self):
        """Test error when getting service for non-existent language."""
        manager = TemplateManager(Path('services'))
        
        with pytest.raises(ValueError, match="No services found"):
            manager.get_services('xx', 'generic-service-template')
    
    def test_get_process_nonexistent_language(self):
        """Test error when getting process for non-existent language."""
        manager = TemplateManager(Path('processes'))
        
        with pytest.raises(ValueError, match="No processes found"):
            manager.get_processes('xx', 'generic-process-template')


class TestGracefulDegradation:
    """Tests for graceful degradation when data is missing."""
    
    def test_service_generation_with_missing_metadata(self):
        """Test that service generation works even with missing metadata."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create service directory with template but no metadata
            service_dir = Path(tmpdir) / 'services' / 'de' / 'test-service'
            service_dir.mkdir(parents=True)
            
            # Create template with placeholders
            template_content = """# Service: {{ service.name }}

**ID:** {{ service.id }}
**Organization:** {{ organization.name }}
"""
            (service_dir / 'service-template.md').write_text(template_content)
            
            # Create metadata config
            org_info = OrganizationInfo(
                name="Test Organization",
                address="Test Address",
                phone="+49 123 456789",
                email="test@example.com",
                web="https://example.com"
            )
            metadata_config = MetadataConfig(organization=org_config)
            
            # Process template
            manager = TemplateManager(Path(tmpdir) / 'services')
            templates = manager.get_services('de', 'test-service')
            
            adapter = MetaAdapter(metadata_config, language='de')
            adapter.connect()
            adapter.set_service_type('test-service', 'de')
            
            processor = PlaceholderProcessor({'meta': adapter})
            result = processor.process_template(
                templates[0].read_content(),
                templates[0].path.name
            )
            
            # Should generate output even with missing service metadata
            assert result.content is not None
            assert 'Test Organization' in result.content
            # Service placeholders should be replaced with [TODO] or remain
            assert '[TODO]' in result.content or '{{ service.' in result.content
    
    def test_process_generation_with_partial_metadata(self):
        """Test that process generation works with partial metadata."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create process directory with partial metadata
            process_dir = Path(tmpdir) / 'processes' / 'de' / 'test-process'
            process_dir.mkdir(parents=True)
            
            # Create partial process config (only ID, no other fields)
            process_config = {
                'process': {
                    'id': 'PROC-001'
                }
            }
            process_config_path = process_dir / 'meta-process.yaml'
            with open(process_config_path, 'w') as f:
                yaml.dump(process_config, f)
            
            # Create template
            template_content = """# Process: {{ process.name }}

**ID:** {{ process.id }}
**Category:** {{ process.category }}
"""
            (process_dir / 'process-template.md').write_text(template_content)
            
            # Create metadata config
            org_info = OrganizationInfo(
                name="Test Organization",
                address="Test Address",
                phone="+49 123 456789",
                email="test@example.com",
                web="https://example.com"
            )
            metadata_config = MetadataConfig(organization=org_config)
            
            # Process template
            manager = TemplateManager(Path(tmpdir) / 'processes')
            templates = manager.get_processes('de', 'test-process')
            
            adapter = MetaAdapter(metadata_config, language='de')
            adapter.connect()
            adapter.set_process_type('test-process', 'de')
            
            processor = PlaceholderProcessor({'meta': adapter})
            result = processor.process_template(
                templates[0].read_content(),
                templates[0].path.name
            )
            
            # Should generate output with partial data
            assert result.content is not None
            assert 'PROC-001' in result.content
            # Missing fields should be replaced with [TODO] or remain
            assert '[TODO]' in result.content or '{{ process.' in result.content


class TestEdgeCases:
    """Tests for edge cases and boundary conditions."""
    
    def test_empty_service_directory(self):
        """Test handling of empty service directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create empty service directory
            service_dir = Path(tmpdir) / 'services' / 'de'
            service_dir.mkdir(parents=True)
            
            manager = TemplateManager(Path(tmpdir) / 'services')
            services = manager.discover_services()
            
            # Should discover language but no services
            assert 'de' in services
            assert services['de'] == {}
    
    def test_service_with_only_diagrams_directory(self):
        """Test that diagrams directory alone doesn't create a service."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create only diagrams directory
            diagrams_dir = Path(tmpdir) / 'services' / 'de' / 'diagrams'
            diagrams_dir.mkdir(parents=True)
            (diagrams_dir / 'diagram.png').write_text('fake image')
            
            manager = TemplateManager(Path(tmpdir) / 'services')
            services = manager.discover_services()
            
            # Diagrams should not be discovered as a service
            assert 'de' in services
            assert 'diagrams' not in services['de']
    
    def test_very_long_placeholder_path(self):
        """Test handling of very long placeholder paths."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create service with deeply nested structure
            service_dir = Path(tmpdir) / 'services' / 'de' / 'test-service'
            service_dir.mkdir(parents=True)
            
            # Create config with very deep nesting
            service_config = {
                'service': {
                    'level1': {
                        'level2': {
                            'level3': {
                                'level4': {
                                    'level5': 'deep value'
                                }
                            }
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
            
            adapter = MetaAdapter(metadata_config, language='de')
            adapter.connect()
            adapter.set_service_type('test-service', 'de')
            
            # Should handle very long path
            value = adapter.get_field('service.level1.level2.level3.level4.level5')
            assert value == 'deep value'
