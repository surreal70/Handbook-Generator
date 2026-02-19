"""
Integration tests for process documentation generation.

Tests the complete workflow of generating process documentation including
template discovery, metadata loading, placeholder resolution, and output generation.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

import pytest
from pathlib import Path
import tempfile
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


class TestProcessDiscovery:
    """Tests for process template discovery."""
    
    def test_discover_processes_basic(self):
        """Test basic process discovery."""
        manager = TemplateManager(Path('processes'))
        processes = manager.discover_processes()
        
        # Verify structure
        assert isinstance(processes, dict)
        
        # Verify German processes exist
        if Path('processes/de').exists():
            assert 'de' in processes
            assert isinstance(processes['de'], dict)
    
    def test_discover_processes_german(self):
        """Test discovering German process templates."""
        manager = TemplateManager(Path('processes'))
        processes = manager.discover_processes()
        
        # Verify German generic process template exists
        if Path('processes/de/generic-process-template').exists():
            assert 'de' in processes
            assert 'generic-process-template' in processes['de']
            assert len(processes['de']['generic-process-template']) > 0
    
    def test_discover_processes_english(self):
        """Test discovering English process templates."""
        manager = TemplateManager(Path('processes'))
        processes = manager.discover_processes()
        
        # Verify English generic process template exists
        if Path('processes/en/generic-process-template').exists():
            assert 'en' in processes
            assert 'generic-process-template' in processes['en']
            assert len(processes['en']['generic-process-template']) > 0
    
    def test_get_processes_german(self):
        """Test getting specific German process templates."""
        if not Path('processes/de/generic-process-template').exists():
            pytest.skip("German process templates not found")
        
        manager = TemplateManager(Path('processes'))
        templates = manager.get_processes('de', 'generic-process-template')
        
        assert len(templates) > 0
        assert all(t.language == 'de' for t in templates)
        assert all(t.category == 'generic-process-template' for t in templates)
    
    def test_get_processes_english(self):
        """Test getting specific English process templates."""
        if not Path('processes/en/generic-process-template').exists():
            pytest.skip("English process templates not found")
        
        manager = TemplateManager(Path('processes'))
        templates = manager.get_processes('en', 'generic-process-template')
        
        assert len(templates) > 0
        assert all(t.language == 'en' for t in templates)
        assert all(t.category == 'generic-process-template' for t in templates)
    
    def test_get_processes_nonexistent_language(self):
        """Test error handling for non-existent language."""
        manager = TemplateManager(Path('processes'))
        
        with pytest.raises(ValueError, match="No processes found"):
            manager.get_processes('xx', 'generic-process-template')
    
    def test_get_processes_nonexistent_process(self):
        """Test error handling for non-existent process."""
        manager = TemplateManager(Path('processes'))
        
        with pytest.raises(ValueError, match="Process .* not found"):
            manager.get_processes('de', 'nonexistent-process')
    
    def test_diagrams_directory_excluded(self):
        """Test that diagrams directory is excluded from process discovery."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create process directory with diagrams subdirectory
            process_dir = Path(tmpdir) / 'processes' / 'de'
            process_dir.mkdir(parents=True)
            
            # Create regular process directory
            (process_dir / 'test-process').mkdir()
            (process_dir / 'test-process' / 'process-template.md').write_text('content')
            
            # Create diagrams directory (should be excluded)
            (process_dir / 'diagrams').mkdir()
            (process_dir / 'diagrams' / 'flow.bpmn').write_text('diagram')
            
            manager = TemplateManager(Path(tmpdir) / 'processes')
            processes = manager.discover_processes()
            
            # Verify diagrams is not discovered as a process
            assert 'de' in processes
            assert 'diagrams' not in processes['de']
            assert 'test-process' in processes['de']


class TestProcessMetadataLoading:
    """Tests for process metadata loading."""
    
    def test_set_process_type_german(self):
        """Test setting process type for German process."""
        if not Path('processes/de/generic-process-template/meta-process.yaml').exists():
            pytest.skip("German process metadata not found")
        
        # Create minimal metadata config
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
        
        # Set process type
        adapter.set_process_type('generic-process-template', 'de')
        
        # Verify process type was set
        assert adapter._current_process_type == 'generic-process-template'
        assert adapter._process_config is not None
    
    def test_set_process_type_english(self):
        """Test setting process type for English process."""
        if not Path('processes/en/generic-process-template/meta-process.yaml').exists():
            pytest.skip("English process metadata not found")
        
        # Create minimal metadata config
        org_info = OrganizationInfo(
            name="Test Organization",
            address="Test Address",
            phone="+49 123 456789",
            email="test@example.com",
            web="https://example.com"
        )
        metadata_config = create_test_metadata_config()
        
        adapter = MetaAdapter(metadata_config, language='en')
        adapter.connect()
        
        # Set process type
        adapter.set_process_type('generic-process-template', 'en')
        
        # Verify process type was set
        assert adapter._current_process_type == 'generic-process-template'
        assert adapter._process_config is not None


class TestProcessPlaceholderResolution:
    """Tests for process placeholder resolution."""
    
    def test_process_placeholder_resolution_basic(self):
        """Test basic process placeholder resolution."""
        if not Path('processes/de/generic-process-template/meta-process.yaml').exists():
            pytest.skip("German process metadata not found")
        
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
        adapter.set_process_type('generic-process-template', 'de')
        
        # Test process field resolution
        process_id = adapter.get_field('process.id')
        assert process_id is not None
        assert process_id != "[TODO]"
    
    def test_process_hierarchical_resolution(self):
        """Test hierarchical placeholder resolution for processes."""
        if not Path('processes/de/generic-process-template/meta-process.yaml').exists():
            pytest.skip("German process metadata not found")
        
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
        adapter.set_process_type('generic-process-template', 'de')
        
        # Test process-specific field (highest priority)
        process_value = adapter.get_field('process.id')
        assert process_value is not None
        
        # Test organization field (lower priority)
        org_value = adapter.get_field('organization.name')
        assert org_value == "Test Organization"


class TestProcessEndToEndGeneration:
    """End-to-end integration tests for process generation."""
    
    def test_process_generation_workflow_german(self):
        """Test complete process generation workflow for German."""
        if not Path('processes/de/generic-process-template').exists():
            pytest.skip("German process templates not found")
        
        # Setup
        org_info = OrganizationInfo(
            name="Test Organization",
            address="Test Address",
            phone="+49 123 456789",
            email="test@example.com",
            web="https://example.com"
        )
        metadata_config = create_test_metadata_config()
        
        template_manager = TemplateManager(Path('processes'))
        meta_adapter = MetaAdapter(metadata_config, language='de')
        meta_adapter.connect()
        
        # Get process templates
        templates = template_manager.get_processes('de', 'generic-process-template')
        assert len(templates) > 0
        
        # Set process type
        meta_adapter.set_process_type('generic-process-template', 'de')
        
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
        assert '{{ process.' not in result.content or result.warnings
    
    def test_process_generation_workflow_english(self):
        """Test complete process generation workflow for English."""
        if not Path('processes/en/generic-process-template').exists():
            pytest.skip("English process templates not found")
        
        # Setup
        org_info = OrganizationInfo(
            name="Test Organization",
            address="Test Address",
            phone="+49 123 456789",
            email="test@example.com",
            web="https://example.com"
        )
        metadata_config = create_test_metadata_config()
        
        template_manager = TemplateManager(Path('processes'))
        meta_adapter = MetaAdapter(metadata_config, language='en')
        meta_adapter.connect()
        
        # Get process templates
        templates = template_manager.get_processes('en', 'generic-process-template')
        assert len(templates) > 0
        
        # Set process type
        meta_adapter.set_process_type('generic-process-template', 'en')
        
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
        assert '{{ process.' not in result.content or result.warnings
    
    def test_process_template_content_structure(self):
        """Test that process templates have expected structure."""
        if not Path('processes/de/generic-process-template').exists():
            pytest.skip("German process templates not found")
        
        manager = TemplateManager(Path('processes'))
        templates = manager.get_processes('de', 'generic-process-template')
        
        # Read first template
        content = templates[0].read_content()
        
        # Verify expected sections exist
        assert '# Prozess:' in content or '# Process:' in content
        assert 'Dokument-ID' in content or 'Document-ID' in content
        assert 'Organisation' in content or 'Organization' in content
    
    def test_process_raci_matrix_structure(self):
        """Test that process templates include RACI matrix."""
        if not Path('processes/de/generic-process-template').exists():
            pytest.skip("German process templates not found")
        
        manager = TemplateManager(Path('processes'))
        templates = manager.get_processes('de', 'generic-process-template')
        
        # Read first template
        content = templates[0].read_content()
        
        # Verify RACI matrix section exists
        assert 'RACI' in content
    
    def test_process_bilingual_consistency(self):
        """Test that German and English process templates are consistent."""
        if not (Path('processes/de/generic-process-template').exists() and 
                Path('processes/en/generic-process-template').exists()):
            pytest.skip("Both German and English process templates required")
        
        manager = TemplateManager(Path('processes'))
        
        de_templates = manager.get_processes('de', 'generic-process-template')
        en_templates = manager.get_processes('en', 'generic-process-template')
        
        # Verify same number of templates
        assert len(de_templates) == len(en_templates), \
            "German and English should have same number of process templates"
        
        # Verify similar structure (both should have process-template.md)
        de_names = {t.path.name for t in de_templates}
        en_names = {t.path.name for t in en_templates}
        
        assert de_names == en_names, \
            "German and English process templates should have matching filenames"
    
    def test_process_diagrams_directory_exists(self):
        """Test that process templates have diagrams directory."""
        if not Path('processes/de/generic-process-template').exists():
            pytest.skip("German process templates not found")
        
        diagrams_dir = Path('processes/de/generic-process-template/diagrams')
        
        # Diagrams directory should exist
        assert diagrams_dir.exists(), \
            "Process templates should have a diagrams directory"
        assert diagrams_dir.is_dir(), \
            "diagrams should be a directory"


class TestProcessErrorHandling:
    """Tests for error handling in process generation."""
    
    def test_missing_process_directory(self):
        """Test handling of missing process directory."""
        manager = TemplateManager(Path('nonexistent'))
        processes = manager.discover_processes()
        
        # Should return empty dict, not raise error
        assert processes == {}
    
    def test_missing_process_metadata(self):
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
            metadata_config = create_test_metadata_config()
            
            adapter = MetaAdapter(metadata_config, language='de')
            adapter.connect()
            
            # Set process type (should handle missing metadata gracefully)
            adapter.set_process_type('test-process', 'de')
            
            # Process config should be None
            assert adapter._process_config is None
    
    def test_invalid_process_yaml(self):
        """Test handling of invalid YAML in process metadata."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create process directory with invalid YAML
            process_dir = Path(tmpdir) / 'processes' / 'de' / 'test-process'
            process_dir.mkdir(parents=True)
            (process_dir / 'meta-process.yaml').write_text('invalid: yaml: content:')
            
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
            
            # Set process type (should handle invalid YAML gracefully)
            adapter.set_process_type('test-process', 'de')
            
            # Process config should be None due to YAML error
            assert adapter._process_config is None
    
    def test_missing_diagrams_directory(self):
        """Test handling of missing diagrams directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create process directory without diagrams
            process_dir = Path(tmpdir) / 'processes' / 'de' / 'test-process'
            process_dir.mkdir(parents=True)
            (process_dir / 'process-template.md').write_text('# Test Process')
            
            manager = TemplateManager(Path(tmpdir) / 'processes')
            
            # Should still discover the process
            processes = manager.discover_processes()
            assert 'de' in processes
            assert 'test-process' in processes['de']
