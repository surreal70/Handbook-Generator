"""
Integration tests for service documentation generation.

Tests the complete workflow of generating service documentation including
template discovery, metadata loading, placeholder resolution, and output generation.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

import pytest
from pathlib import Path
import tempfile
import shutil
from hypothesis import given, settings, strategies as st

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


class TestServiceDiscovery:
    """Tests for service template discovery."""
    
    def test_discover_services_basic(self):
        """Test basic service discovery."""
        manager = TemplateManager(Path('services'))
        services = manager.discover_services()
        
        # Verify structure
        assert isinstance(services, dict)
        
        # Verify German services exist
        if Path('services/de').exists():
            assert 'de' in services
            assert isinstance(services['de'], dict)
    
    def test_discover_services_german(self):
        """Test discovering German service templates."""
        manager = TemplateManager(Path('services'))
        services = manager.discover_services()
        
        # Verify German generic service template exists
        if Path('services/de/generic-service-template').exists():
            assert 'de' in services
            assert 'generic-service-template' in services['de']
            assert len(services['de']['generic-service-template']) > 0
    
    def test_discover_services_english(self):
        """Test discovering English service templates."""
        manager = TemplateManager(Path('services'))
        services = manager.discover_services()
        
        # Verify English generic service template exists
        if Path('services/en/generic-service-template').exists():
            assert 'en' in services
            assert 'generic-service-template' in services['en']
            assert len(services['en']['generic-service-template']) > 0
    
    def test_get_services_german(self):
        """Test getting specific German service templates."""
        if not Path('services/de/generic-service-template').exists():
            pytest.skip("German service templates not found")
        
        manager = TemplateManager(Path('services'))
        templates = manager.get_services('de', 'generic-service-template')
        
        assert len(templates) > 0
        assert all(t.language == 'de' for t in templates)
        assert all(t.category == 'generic-service-template' for t in templates)
    
    def test_get_services_english(self):
        """Test getting specific English service templates."""
        if not Path('services/en/generic-service-template').exists():
            pytest.skip("English service templates not found")
        
        manager = TemplateManager(Path('services'))
        templates = manager.get_services('en', 'generic-service-template')
        
        assert len(templates) > 0
        assert all(t.language == 'en' for t in templates)
        assert all(t.category == 'generic-service-template' for t in templates)
    
    def test_get_services_nonexistent_language(self):
        """Test error handling for non-existent language."""
        manager = TemplateManager(Path('services'))
        
        with pytest.raises(ValueError, match="No services found"):
            manager.get_services('xx', 'generic-service-template')
    
    def test_get_services_nonexistent_service(self):
        """Test error handling for non-existent service."""
        manager = TemplateManager(Path('services'))
        
        with pytest.raises(ValueError, match="Service .* not found"):
            manager.get_services('de', 'nonexistent-service')


class TestServiceMetadataLoading:
    """Tests for service metadata loading."""
    
    def test_set_service_type_german(self):
        """Test setting service type for German service."""
        if not Path('services/de/generic-service-template/meta-service.yaml').exists():
            pytest.skip("German service metadata not found")
        
        metadata_config = create_test_metadata_config()
        
        adapter = MetaAdapter(metadata_config, language='de')
        adapter.connect()
        
        # Set service type
        adapter.set_service_type('generic-service-template', 'de')
        
        # Verify service type was set
        assert adapter._current_service_type == 'generic-service-template'
        assert adapter._service_config is not None
    
    def test_set_service_type_english(self):
        """Test setting service type for English service."""
        if not Path('services/en/generic-service-template/meta-service.yaml').exists():
            pytest.skip("English service metadata not found")
        
        metadata_config = create_test_metadata_config()
        
        adapter = MetaAdapter(metadata_config, language='en')
        adapter.connect()
        
        # Set service type
        adapter.set_service_type('generic-service-template', 'en')
        
        # Verify service type was set
        assert adapter._current_service_type == 'generic-service-template'
        assert adapter._service_config is not None


class TestServicePlaceholderResolution:
    """Tests for service placeholder resolution."""
    
    def test_service_placeholder_resolution_basic(self):
        """Test basic service placeholder resolution."""
        if not Path('services/de/generic-service-template/meta-service.yaml').exists():
            pytest.skip("German service metadata not found")
        
        # Create metadata config
        org_info = OrganizationInfo(
            name="Test Organization",
            address="Test Address",
            phone="+49 123 456789",
            email="test@example.com",
            web="https://example.com"
        )
        metadata_config = create_test_metadata_config()
        
        adapter = MetaAdapter(metadata_config, language='de')
        adapter.connect()
        adapter.set_service_type('generic-service-template', 'de')
        
        # Test service field resolution
        service_id = adapter.get_field('service.id')
        assert service_id is not None
        assert service_id != "[TODO]"
    
    def test_service_hierarchical_resolution(self):
        """Test hierarchical placeholder resolution for services."""
        if not Path('services/de/generic-service-template/meta-service.yaml').exists():
            pytest.skip("German service metadata not found")
        
        # Create metadata config
        org_info = OrganizationInfo(
            name="Test Organization",
            address="Test Address",
            phone="+49 123 456789",
            email="test@example.com",
            web="https://example.com"
        )
        metadata_config = create_test_metadata_config()
        
        adapter = MetaAdapter(metadata_config, language='de')
        adapter.connect()
        adapter.set_service_type('generic-service-template', 'de')
        
        # Test service-specific field (highest priority)
        service_value = adapter.get_field('service.id')
        assert service_value is not None
        
        # Test organization field (lower priority)
        org_value = adapter.get_field('organization.name')
        assert org_value == "Test Organization"


class TestServiceEndToEndGeneration:
    """End-to-end integration tests for service generation."""
    
    def test_service_generation_workflow_german(self):
        """Test complete service generation workflow for German."""
        if not Path('services/de/generic-service-template').exists():
            pytest.skip("German service templates not found")
        
        # Setup
        org_info = OrganizationInfo(
            name="Test Organization",
            address="Test Address",
            phone="+49 123 456789",
            email="test@example.com",
            web="https://example.com"
        )
        metadata_config = create_test_metadata_config()
        
        template_manager = TemplateManager(Path('services'))
        meta_adapter = MetaAdapter(metadata_config, language='de')
        meta_adapter.connect()
        
        # Get service templates
        templates = template_manager.get_services('de', 'generic-service-template')
        assert len(templates) > 0
        
        # Set service type
        meta_adapter.set_service_type('generic-service-template', 'de')
        
        # Process template
        processor = PlaceholderProcessor({'meta': meta_adapter})
        result = processor.process_template(
            templates[0].read_content(),
            templates[0].path.name
        )
        
        # Verify placeholders were processed
        assert result.content is not None
        assert len(result.content) > 0
        
        # Verify some placeholders were resolved (not all will be [TODO])
        assert '{{ service.' not in result.content or result.warnings
    
    def test_service_generation_workflow_english(self):
        """Test complete service generation workflow for English."""
        if not Path('services/en/generic-service-template').exists():
            pytest.skip("English service templates not found")
        
        # Setup
        org_info = OrganizationInfo(
            name="Test Organization",
            address="Test Address",
            phone="+49 123 456789",
            email="test@example.com",
            web="https://example.com"
        )
        metadata_config = create_test_metadata_config()
        
        template_manager = TemplateManager(Path('services'))
        meta_adapter = MetaAdapter(metadata_config, language='en')
        meta_adapter.connect()
        
        # Get service templates
        templates = template_manager.get_services('en', 'generic-service-template')
        assert len(templates) > 0
        
        # Set service type
        meta_adapter.set_service_type('generic-service-template', 'en')
        
        # Process template
        processor = PlaceholderProcessor({'meta': meta_adapter})
        result = processor.process_template(
            templates[0].read_content(),
            templates[0].path.name
        )
        
        # Verify placeholders were processed
        assert result.content is not None
        assert len(result.content) > 0
        
        # Verify some placeholders were resolved
        assert '{{ service.' not in result.content or result.warnings
    
    def test_service_template_content_structure(self):
        """Test that service templates have expected structure."""
        if not Path('services/de/generic-service-template').exists():
            pytest.skip("German service templates not found")
        
        manager = TemplateManager(Path('services'))
        templates = manager.get_services('de', 'generic-service-template')
        
        # Read first template
        content = templates[0].read_content()
        
        # Verify expected sections exist
        assert '# Service:' in content or '# Dienst:' in content
        assert 'Dokument-ID' in content or 'Document-ID' in content
        assert 'Organisation' in content or 'Organization' in content
    
    def test_service_bilingual_consistency(self):
        """Test that German and English service templates are consistent."""
        if not (Path('services/de/generic-service-template').exists() and 
                Path('services/en/generic-service-template').exists()):
            pytest.skip("Both German and English service templates required")
        
        manager = TemplateManager(Path('services'))
        
        de_templates = manager.get_services('de', 'generic-service-template')
        en_templates = manager.get_services('en', 'generic-service-template')
        
        # Verify same number of templates
        assert len(de_templates) == len(en_templates), \
            "German and English should have same number of service templates"
        
        # Verify similar structure (both should have service-template.md)
        de_names = {t.path.name for t in de_templates}
        en_names = {t.path.name for t in en_templates}
        
        assert de_names == en_names, \
            "German and English service templates should have matching filenames"


class TestServiceErrorHandling:
    """Tests for error handling in service generation."""
    
    def test_missing_service_directory(self):
        """Test handling of missing service directory."""
        manager = TemplateManager(Path('nonexistent'))
        services = manager.discover_services()
        
        # Should return empty dict, not raise error
        assert services == {}
    
    def test_missing_service_metadata(self):
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
            metadata_config = create_test_metadata_config()
            
            adapter = MetaAdapter(metadata_config, language='de')
            adapter.connect()
            
            # Set service type (should handle missing metadata gracefully)
            adapter.set_service_type('test-service', 'de')
            
            # Service config should be None
            assert adapter._service_config is None
    
    def test_invalid_service_yaml(self):
        """Test handling of invalid YAML in service metadata."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create service directory with invalid YAML
            service_dir = Path(tmpdir) / 'services' / 'de' / 'test-service'
            service_dir.mkdir(parents=True)
            (service_dir / 'meta-service.yaml').write_text('invalid: yaml: content:')
            
            # Create metadata config
            org_info = OrganizationInfo(
                name="Test Organization",
                address="Test Address",
                phone="+49 123 456789",
                email="test@example.com",
                web="https://example.com"
            )
            metadata_config = create_test_metadata_config()
            
            adapter = MetaAdapter(metadata_config, language='de')
            adapter.connect()
            
            # Set service type (should handle invalid YAML gracefully)
            adapter.set_service_type('test-service', 'de')
            
            # Service config should be None due to YAML error
            assert adapter._service_config is None
