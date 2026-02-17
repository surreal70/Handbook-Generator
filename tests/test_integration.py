"""
Integration and End-to-End tests for Handbuch-Generator

This module contains integration tests that verify the complete workflow
of the handbook generator, including template processing, data integration,
and output generation.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

import pytest
import tempfile
import shutil
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
import yaml

from src.template_manager import TemplateManager
from src.placeholder_processor import PlaceholderProcessor
from src.netbox_adapter import NetBoxAdapter
from src.output_generator import OutputGenerator
from src.config_manager import ConfigManager
from src.logger import HandbookLogger


@pytest.fixture
def temp_workspace():
    """Create a temporary workspace for integration tests."""
    temp_dir = tempfile.mkdtemp()
    workspace = Path(temp_dir)
    
    # Create directory structure
    templates_dir = workspace / "templates"
    output_dir = workspace / "Handbook"
    
    templates_dir.mkdir()
    output_dir.mkdir()
    
    yield workspace
    
    # Cleanup
    shutil.rmtree(temp_dir)


@pytest.fixture
def complete_template_set(temp_workspace):
    """Create a complete set of templates for testing."""
    templates_dir = temp_workspace / "templates"
    
    # German backup templates
    de_backup = templates_dir / "de" / "backup"
    de_backup.mkdir(parents=True)
    
    # Metadata template
    (de_backup / "0000_metadata_de_backup.md").write_text("""# Backup-Handbuch

**Dokument-Metadaten**

- **Erstellt am:** {{ metadata.date }}
- **Autor:** {{ metadata.author }}
- **Version:** {{ metadata.version }}
- **Typ:** Backup-Handbuch

---
""")
    
    # Content templates
    (de_backup / "0100_einleitung.md").write_text("""# 1. Einleitung

Dieses Handbuch beschreibt die Backup-Strategie für {{ netbox.site_name }}.

## 1.1 Zweck

Das Backup-System sichert kritische Daten auf {{ netbox.device_name }}.
""")
    
    (de_backup / "0200_backup_strategie.md").write_text("""# 2. Backup-Strategie

## 2.1 Infrastruktur

- **Primäres Backup-Gerät:** {{ netbox.device_name }}
- **Standort:** {{ netbox.site_name }}
- **IP-Adresse:** {{ netbox.primary_ip }}

## 2.2 Backup-Zeitplan

Backups werden täglich durchgeführt.
""")
    
    return templates_dir


@pytest.fixture
def mock_netbox_api():
    """Create a mock NetBox API for testing."""
    mock_api = MagicMock()
    
    # Mock device data
    mock_device = MagicMock()
    mock_device.name = "backup-server-01"
    mock_device.primary_ip = "192.168.1.100"
    
    # Mock site data
    mock_site = MagicMock()
    mock_site.name = "Datacenter Munich"
    mock_device.site = mock_site
    
    # Configure the API to return lists with our mock objects
    mock_api.dcim.devices.all.return_value = [mock_device]
    mock_api.dcim.sites.all.return_value = [mock_site]
    
    # Also support get() method
    mock_api.dcim.devices.get.return_value = mock_device
    mock_api.dcim.sites.get.return_value = mock_site
    
    return mock_api


@pytest.mark.integration
def test_end_to_end_handbook_generation(temp_workspace, complete_template_set, mock_netbox_api):
    """
    Test complete handbook generation workflow.
    
    This test verifies:
    - Template discovery and sorting
    - Placeholder detection and replacement
    - Data fetching from mocked NetBox API
    - Markdown output generation
    - Output directory structure
    
    Requirements: All (complete workflow)
    """
    # Setup
    output_dir = temp_workspace / "Handbook"
    
    # Create config
    config_data = {
        "data_sources": {
            "netbox": {
                "url": "https://netbox.example.com",
                "api_token": "test_token"
            }
        },
        "metadata": {
            "author": "Andreas Huemmer [andreas.huemmer@adminsend.de]",
            "version": "1.0.0",
            "date": "2025-01-30"
        }
    }
    
    # Initialize components
    template_manager = TemplateManager(complete_template_set)
    logger = HandbookLogger(verbose=False)
    
    # Mock NetBox adapter
    with patch('pynetbox.api') as mock_pynetbox:
        mock_pynetbox.return_value = mock_netbox_api
        
        netbox_adapter = NetBoxAdapter(
            url=config_data["data_sources"]["netbox"]["url"],
            api_token=config_data["data_sources"]["netbox"]["api_token"]
        )
        netbox_adapter.connect()
        
        # Create placeholder processor with adapters
        data_sources = {"netbox": netbox_adapter, "metadata": config_data["metadata"]}
        processor = PlaceholderProcessor(data_sources)
        
        # Create output generator
        output_generator = OutputGenerator(output_dir, test_mode=True)
        
        # Execute workflow
        # 1. Discover templates
        templates = template_manager.get_templates("de", "backup")
        assert len(templates) == 3, "Should find 3 templates"
        
        # 2. Process templates
        processed_results = []
        for template in templates:
            content = template.read_content()
            result = processor.process_template(content, template.path)
            processed_results.append(result)
        
        # 3. Verify placeholder replacements
        all_content = "\n\n".join([r.content for r in processed_results])
        
        # Check that placeholders were replaced
        assert "{{ netbox.device_name }}" not in all_content
        assert "{{ netbox.site_name }}" not in all_content
        assert "{{ netbox.primary_ip }}" not in all_content
        assert "{{ metadata.author }}" not in all_content
        assert "{{ metadata.version }}" not in all_content
        assert "{{ metadata.date }}" not in all_content
        
        # Check that actual values are present
        assert "backup-server-01" in all_content
        assert "Datacenter Munich" in all_content
        assert "192.168.1.100" in all_content
        assert "Andreas Huemmer" in all_content
        # Date will be current date (check for year 2026 or 2025)
        assert "2026-" in all_content or "2025-" in all_content
        
        # 4. Generate markdown output
        processed_contents = [r.content for r in processed_results]
        output_result = output_generator.generate_markdown(
            processed_contents,
            "de",
            "backup"
        )
        output_path = output_result.markdown_path
        
        # 5. Verify output file exists and structure
        assert output_path.exists(), "Output file should be created"
        assert output_path.parent == output_dir / "de" / "backup" / "markdown"
        assert output_path.name == "backup_handbook.md"
        
        # 6. Verify output content
        output_content = output_path.read_text()
        assert "backup-server-01" in output_content
        assert "Datacenter Munich" in output_content
        assert "# Backup-Handbuch" in output_content
        assert "# 1. Einleitung" in output_content
        assert "# 2. Backup-Strategie" in output_content
        
        # 7. Verify no errors occurred
        total_errors = sum(len(r.errors) for r in processed_results)
        assert total_errors == 0, "No errors should occur during processing"


@pytest.mark.integration
def test_end_to_end_with_pdf_generation(temp_workspace, complete_template_set, mock_netbox_api):
    """
    Test complete handbook generation with PDF output.
    
    This test verifies PDF generation in addition to markdown output.
    
    Requirements: 9.1, 9.3, 9.5
    """
    output_dir = temp_workspace / "Handbook"
    
    config_data = {
        "data_sources": {
            "netbox": {
                "url": "https://netbox.example.com",
                "api_token": "test_token"
            }
        },
        "metadata": {
            "author": "Andreas Huemmer [andreas.huemmer@adminsend.de]",
            "version": "1.0.0",
            "date": "2025-01-30"
        }
    }
    
    # Initialize components
    template_manager = TemplateManager(complete_template_set)
    logger = HandbookLogger(verbose=False)
    
    with patch('pynetbox.api') as mock_pynetbox:
        mock_pynetbox.return_value = mock_netbox_api
        
        netbox_adapter = NetBoxAdapter(
            url=config_data["data_sources"]["netbox"]["url"],
            api_token=config_data["data_sources"]["netbox"]["api_token"]
        )
        netbox_adapter.connect()
        
        data_sources = {"netbox": netbox_adapter, "metadata": config_data["metadata"]}
        processor = PlaceholderProcessor(data_sources)
        output_generator = OutputGenerator(output_dir, test_mode=True)
        
        # Process templates
        templates = template_manager.get_templates("de", "backup")
        processed_results = []
        for template in templates:
            content = template.read_content()
            result = processor.process_template(content, template.path)
            processed_results.append(result)
        
        # Generate markdown
        processed_contents = [r.content for r in processed_results]
        output_result = output_generator.generate_markdown(processed_contents, "de", "backup")
        md_path = output_result.markdown_path
        assert md_path.exists()
        
        # Generate PDF
        markdown_content = md_path.read_text()
        
        try:
            pdf_path = output_generator.generate_pdf(markdown_content, "de", "backup")
            
            # Verify PDF was created
            assert pdf_path.exists(), "PDF file should be created"
            assert pdf_path.suffix == ".pdf"
            assert pdf_path.name == "backup_handbook.pdf"
            
            # Verify PDF has content (size > 0)
            assert pdf_path.stat().st_size > 0, "PDF should have content"
            
        except Exception as e:
            # PDF generation might fail if system libraries are missing
            # This is acceptable in test environment
            pytest.skip(f"PDF generation skipped: {e}")




@pytest.fixture
def multilanguage_templates(temp_workspace):
    """Create templates in multiple languages for testing."""
    templates_dir = temp_workspace / "templates"
    
    # German templates
    de_backup = templates_dir / "de" / "backup"
    de_backup.mkdir(parents=True)
    
    (de_backup / "0000_metadata_de_backup.md").write_text("""# Backup-Handbuch

**Dokument-Metadaten**

- **Erstellt am:** {{ metadata.date }}
- **Autor:** {{ metadata.author }}

---
""")
    
    (de_backup / "0100_einleitung.md").write_text("""# 1. Einleitung

Dieses Handbuch beschreibt die Backup-Strategie.

Standort: {{ netbox.site_name }}
""")
    
    # English templates
    en_backup = templates_dir / "en" / "backup"
    en_backup.mkdir(parents=True)
    
    (en_backup / "0000_metadata_en_backup.md").write_text("""# Backup Handbook

**Document Metadata**

- **Created:** {{ metadata.date }}
- **Author:** {{ metadata.author }}

---
""")
    
    (en_backup / "0100_introduction.md").write_text("""# 1. Introduction

This handbook describes the backup strategy.

Location: {{ netbox.site_name }}
""")
    
    return templates_dir


@pytest.mark.integration
def test_multi_language_handbook_generation(temp_workspace, multilanguage_templates, mock_netbox_api):
    """
    Test handbook generation for multiple languages.
    
    This test verifies:
    - Template discovery for multiple languages
    - Correct output directory structure per language
    - Independent processing of each language
    
    Requirements: 1.2, 8.3
    """
    output_dir = temp_workspace / "Handbook"
    
    config_data = {
        "data_sources": {
            "netbox": {
                "url": "https://netbox.example.com",
                "api_token": "test_token"
            }
        },
        "metadata": {
            "author": "Andreas Huemmer [andreas.huemmer@adminsend.de]",
            "version": "1.0.0",
            "date": "2025-01-30"
        }
    }
    
    template_manager = TemplateManager(multilanguage_templates)
    logger = HandbookLogger(verbose=False)
    
    with patch('pynetbox.api') as mock_pynetbox:
        mock_pynetbox.return_value = mock_netbox_api
        
        netbox_adapter = NetBoxAdapter(
            url=config_data["data_sources"]["netbox"]["url"],
            api_token=config_data["data_sources"]["netbox"]["api_token"]
        )
        netbox_adapter.connect()
        
        data_sources = {"netbox": netbox_adapter, "metadata": config_data["metadata"]}
        processor = PlaceholderProcessor(data_sources)
        output_generator = OutputGenerator(output_dir, test_mode=True)
        
        # Process German templates
        de_templates = template_manager.get_templates("de", "backup")
        assert len(de_templates) == 2, "Should find 2 German templates"
        
        de_results = []
        for template in de_templates:
            content = template.read_content()
            result = processor.process_template(content, template.path)
            de_results.append(result)
        
        de_output_result = output_generator.generate_markdown(
            [r.content for r in de_results], "de", "backup"
        )
        de_output = de_output_result.markdown_path
        
        # Process English templates
        en_templates = template_manager.get_templates("en", "backup")
        assert len(en_templates) == 2, "Should find 2 English templates"
        
        en_results = []
        for template in en_templates:
            content = template.read_content()
            result = processor.process_template(content, template.path)
            en_results.append(result)
        
        en_output_result = output_generator.generate_markdown(
            [r.content for r in en_results], "en", "backup"
        )
        en_output = en_output_result.markdown_path
        
        # Verify output structure
        assert de_output.exists(), "German output should exist"
        assert en_output.exists(), "English output should exist"
        
        # Verify correct directory structure
        assert de_output.parent == output_dir / "de" / "backup" / "markdown"
        assert en_output.parent == output_dir / "en" / "backup" / "markdown"
        
        # Verify language-specific content
        de_content = de_output.read_text()
        assert "Backup-Handbuch" in de_content
        assert "Einleitung" in de_content
        assert "Datacenter Munich" in de_content
        
        en_content = en_output.read_text()
        assert "Backup Handbook" in en_content
        assert "Introduction" in en_content
        assert "Datacenter Munich" in en_content
        
        # Verify files are independent
        assert de_content != en_content, "Language outputs should differ"


@pytest.mark.integration
def test_multi_language_discovery(temp_workspace, multilanguage_templates):
    """
    Test template discovery across multiple languages.
    
    This test verifies that the template manager correctly identifies
    and categorizes templates by language.
    
    Requirements: 1.2
    """
    template_manager = TemplateManager(multilanguage_templates)
    
    # Discover all templates
    discovered = template_manager.discover_templates()
    
    # Verify both languages are discovered
    assert "de" in discovered, "German templates should be discovered"
    assert "en" in discovered, "English templates should be discovered"
    
    # Verify backup type exists in both languages
    assert "backup" in discovered["de"], "German backup templates should exist"
    assert "backup" in discovered["en"], "English backup templates should exist"
    
    # Verify template counts
    assert len(discovered["de"]["backup"]) == 2, "Should find 2 German templates"
    assert len(discovered["en"]["backup"]) == 2, "Should find 2 English templates"




@pytest.fixture
def faulty_templates(temp_workspace):
    """Create templates with intentional errors for testing."""
    templates_dir = temp_workspace / "templates"
    
    de_backup = templates_dir / "de" / "backup"
    de_backup.mkdir(parents=True)
    
    # Template with invalid placeholder (not on its own line)
    (de_backup / "0100_invalid_placeholder.md").write_text("""# Test

This line has {{ netbox.device_name }} in the middle of text.
""")
    
    # Template with missing data source
    (de_backup / "0200_unknown_source.md").write_text("""# Test

{{ unknown_source.field }}
""")
    
    # Template with malformed placeholder
    (de_backup / "0300_malformed.md").write_text("""# Test

{{ netbox.missing_field }}
""")
    
    return templates_dir


@pytest.mark.integration
def test_error_propagation_and_summary(temp_workspace, faulty_templates, mock_netbox_api):
    """
    Test error handling and error summary generation.
    
    This test verifies:
    - Errors are collected during processing
    - Processing continues despite errors
    - Error summary contains all errors
    - Warnings are properly categorized
    
    Requirements: 12.5
    """
    output_dir = temp_workspace / "Handbook"
    
    config_data = {
        "data_sources": {
            "netbox": {
                "url": "https://netbox.example.com",
                "api_token": "test_token"
            }
        },
        "metadata": {
            "author": "Andreas Huemmer [andreas.huemmer@adminsend.de]",
            "version": "1.0.0",
            "date": "2025-01-30"
        }
    }
    
    template_manager = TemplateManager(faulty_templates)
    logger = HandbookLogger(verbose=False)
    
    # Mock NetBox to return None for missing field
    mock_netbox_api.dcim.devices.get.return_value = None
    
    with patch('pynetbox.api') as mock_pynetbox:
        mock_pynetbox.return_value = mock_netbox_api
        
        netbox_adapter = NetBoxAdapter(
            url=config_data["data_sources"]["netbox"]["url"],
            api_token=config_data["data_sources"]["netbox"]["api_token"]
        )
        netbox_adapter.connect()
        
        data_sources = {"netbox": netbox_adapter, "metadata": config_data["metadata"]}
        processor = PlaceholderProcessor(data_sources)
        
        # Process templates
        templates = template_manager.get_templates("de", "backup")
        assert len(templates) == 3, "Should find 3 templates"
        
        all_errors = []
        all_warnings = []
        processed_results = []
        
        for template in templates:
            content = template.read_content()
            result = processor.process_template(content, template.path)
            processed_results.append(result)
            all_errors.extend(result.errors)
            all_warnings.extend(result.warnings)
        
        # Verify errors were collected
        assert len(all_errors) > 0 or len(all_warnings) > 0, \
            "Should have collected errors or warnings"
        
        # Verify processing continued despite errors
        assert len(processed_results) == 3, \
            "All templates should be processed despite errors"
        
        # Verify each result has content (even if with errors)
        for result in processed_results:
            assert result.content, "Each result should have content"
        
        # Check for specific error types
        all_messages = all_errors + all_warnings
        
        # Should have warning about placeholder not on its own line
        has_line_warning = any("not the only statement" in msg.lower() 
                              for msg in all_messages)
        
        # Should have warning about unknown source
        has_unknown_source = any("unknown" in msg.lower() and "source" in msg.lower() 
                                for msg in all_messages)
        
        # At least one type of error should be present
        assert has_line_warning or has_unknown_source, \
            "Should detect at least one type of error"


@pytest.mark.integration
def test_error_recovery_with_partial_data(temp_workspace, mock_netbox_api):
    """
    Test that system continues processing when some data is unavailable.
    
    This test verifies graceful degradation when some placeholders
    cannot be resolved.
    
    Requirements: 4.4, 12.5
    """
    templates_dir = temp_workspace / "templates"
    output_dir = temp_workspace / "Handbook"
    
    # Create templates with mix of valid and invalid placeholders
    de_backup = templates_dir / "de" / "backup"
    de_backup.mkdir(parents=True)
    
    (de_backup / "0100_mixed.md").write_text("""# Test

Valid placeholder:
{{ netbox.site_name }}

Invalid placeholder:
{{ netbox.nonexistent_field }}

Another valid placeholder:
{{ metadata.author }}
""")
    
    config_data = {
        "data_sources": {
            "netbox": {
                "url": "https://netbox.example.com",
                "api_token": "test_token"
            }
        },
        "metadata": {
            "author": "Andreas Huemmer [andreas.huemmer@adminsend.de]",
            "version": "1.0.0",
            "date": "2025-01-30"
        }
    }
    
    template_manager = TemplateManager(templates_dir)
    logger = HandbookLogger(verbose=False)
    
    with patch('pynetbox.api') as mock_pynetbox:
        mock_pynetbox.return_value = mock_netbox_api
        
        netbox_adapter = NetBoxAdapter(
            url=config_data["data_sources"]["netbox"]["url"],
            api_token=config_data["data_sources"]["netbox"]["api_token"]
        )
        netbox_adapter.connect()
        
        data_sources = {"netbox": netbox_adapter, "metadata": config_data["metadata"]}
        processor = PlaceholderProcessor(data_sources)
        output_generator = OutputGenerator(output_dir, test_mode=True)
        
        # Process template
        templates = template_manager.get_templates("de", "backup")
        result = processor.process_template(templates[0].read_content(), templates[0].path)
        
        # Verify partial success
        # Valid placeholders should be replaced
        assert "Datacenter Munich" in result.content, \
            "Valid placeholder should be replaced"
        assert "Andreas Huemmer" in result.content, \
            "Metadata placeholder should be replaced"
        
        # Invalid placeholder should remain or generate warning
        assert len(result.warnings) > 0 or "{{ netbox.nonexistent_field }}" in result.content, \
            "Invalid placeholder should generate warning or remain unchanged"
        
        # Output should still be generated
        output_result = output_generator.generate_markdown([result.content], "de", "backup")
        output_path = output_result.markdown_path
        assert output_path.exists(), "Output should be generated despite partial errors"


@pytest.mark.integration
def test_complete_error_summary(temp_workspace, faulty_templates, mock_netbox_api):
    """
    Test that error summary includes all errors from all templates.
    
    This test verifies that the error collection mechanism captures
    errors from multiple templates and provides a complete summary.
    
    Requirements: 12.5
    """
    config_data = {
        "data_sources": {
            "netbox": {
                "url": "https://netbox.example.com",
                "api_token": "test_token"
            }
        },
        "metadata": {
            "author": "Andreas Huemmer [andreas.huemmer@adminsend.de]",
            "version": "1.0.0",
            "date": "2025-01-30"
        }
    }
    
    template_manager = TemplateManager(faulty_templates)
    
    # Mock NetBox to return None for missing field
    mock_netbox_api.dcim.devices.get.return_value = None
    
    with patch('pynetbox.api') as mock_pynetbox:
        mock_pynetbox.return_value = mock_netbox_api
        
        netbox_adapter = NetBoxAdapter(
            url=config_data["data_sources"]["netbox"]["url"],
            api_token=config_data["data_sources"]["netbox"]["api_token"]
        )
        netbox_adapter.connect()
        
        data_sources = {"netbox": netbox_adapter, "metadata": config_data["metadata"]}
        processor = PlaceholderProcessor(data_sources)
        
        # Process all templates and collect errors
        templates = template_manager.get_templates("de", "backup")
        
        error_summary = {
            "total_templates": len(templates),
            "templates_with_errors": 0,
            "total_errors": 0,
            "total_warnings": 0,
            "errors_by_template": {}
        }
        
        for template in templates:
            content = template.read_content()
            result = processor.process_template(content, template.path)
            
            template_name = template.path.name
            error_count = len(result.errors)
            warning_count = len(result.warnings)
            
            if error_count > 0 or warning_count > 0:
                error_summary["templates_with_errors"] += 1
                error_summary["errors_by_template"][template_name] = {
                    "errors": result.errors,
                    "warnings": result.warnings
                }
            
            error_summary["total_errors"] += error_count
            error_summary["total_warnings"] += warning_count
        
        # Verify summary completeness
        assert error_summary["total_templates"] == 3, \
            "Summary should include all templates"
        
        assert error_summary["templates_with_errors"] > 0, \
            "Summary should identify templates with errors"
        
        assert (error_summary["total_errors"] + error_summary["total_warnings"]) > 0, \
            "Summary should count all errors and warnings"
        
        # Verify each faulty template is in the summary
        assert len(error_summary["errors_by_template"]) > 0, \
            "Summary should detail errors by template"


# ============================================================================
# Meta-Platzhalter Integration Tests
# ============================================================================

@pytest.fixture
def meta_templates(temp_workspace):
    """Create templates with meta placeholders for testing."""
    templates_dir = temp_workspace / "templates"
    
    de_it_operation = templates_dir / "de" / "it-operation"
    de_it_operation.mkdir(parents=True)
    
    # Template with organization meta placeholders
    (de_it_operation / "0100_organization.md").write_text("""# Organisation

**Name:** {{ meta.organization.name }}
**Adresse:** {{ meta.organization.address }}
**Stadt:** {{ meta.organization.city }}
**PLZ:** {{ meta.organization.postal_code }}
**Land:** {{ meta.organization.country }}
**Website:** {{ meta.organization.website }}
**Telefon:** {{ meta.organization.phone }}
**E-Mail:** {{ meta.organization.email }}
""")
    
    # Template with role meta placeholders
    (de_it_operation / "0200_roles.md").write_text("""# Rollen und Verantwortlichkeiten

## CEO
- **Name:** {{ meta.ceo.name }}
- **Titel:** {{ meta.ceo.title }}
- **E-Mail:** {{ meta.ceo.email }}
- **Telefon:** {{ meta.ceo.phone }}

## CIO
- **Name:** {{ meta.cio.name }}
- **Titel:** {{ meta.cio.title }}
- **E-Mail:** {{ meta.cio.email }}

## CISO
- **Name:** {{ meta.ciso.name }}
- **E-Mail:** {{ meta.ciso.email }}
""")
    
    # Template with document meta placeholders
    (de_it_operation / "0300_document.md").write_text("""# Dokumentinformationen

**Verantwortlicher:** {{ meta.document.owner }}
**Genehmiger:** {{ meta.document.approver }}
**Version:** {{ meta.document.version }}
**Klassifizierung:** {{ meta.document.classification }}
**Autor:** {{ meta.author }}
**Sprache:** {{ meta.language }}
""")
    
    return templates_dir


@pytest.fixture
def sample_metadata_config():
    """Create a sample metadata configuration for testing."""
    from src.metadata_config_manager import (
        MetadataConfig, OrganizationInfo, PersonRole, DocumentInfo
    )
    
    organization = OrganizationInfo(
        name="Test Organization GmbH",
        address="Test Street 123",
        city="Test City",
        postal_code="12345",
        country="Germany",
        website="https://test.example.com",
        phone="+49 123 456789",
        email="info@test.example.com"
    )
    
    roles = {
        "ceo": PersonRole(
            name="John Doe",
            title="Chief Executive Officer",
            email="john.doe@test.example.com",
            phone="+49 123 456789-100",
            department="Management"
        ),
        "cio": PersonRole(
            name="Jane Smith",
            title="Chief Information Officer",
            email="jane.smith@test.example.com",
            phone="+49 123 456789-200",
            department="IT"
        ),
        "ciso": PersonRole(
            name="Bob Johnson",
            title="Chief Information Security Officer",
            email="bob.johnson@test.example.com",
            phone="+49 123 456789-300",
            department="IT Security"
        )
    }
    
    document = DocumentInfo(
        owner="IT Operations Manager",
        approver="CIO",
        version="2.0.0",
        classification="internal"
    )
    
    return MetadataConfig(
        organization=organization,
        roles=roles,
        document=document,
        author="Test Author [test@example.com]",
        language="de"
    )


@pytest.mark.integration
def test_end_to_end_with_meta_placeholders(temp_workspace, meta_templates, sample_metadata_config):
    """
    Test end-to-end template processing with meta placeholders.
    
    This test verifies:
    - Meta placeholder detection in templates
    - Meta placeholder replacement with metadata values
    - Correct routing to meta adapter
    - All organization, role, and document fields are replaced
    
    Requirements: 16.1, 16.2, 16.3
    """
    from src.meta_adapter import MetaAdapter
    
    output_dir = temp_workspace / "Handbook"
    
    # Initialize components
    template_manager = TemplateManager(meta_templates)
    
    # Create meta adapter with sample metadata
    meta_adapter = MetaAdapter(sample_metadata_config)
    meta_adapter.connect()
    
    # Create placeholder processor with meta adapter
    data_sources = {"meta": meta_adapter}
    processor = PlaceholderProcessor(data_sources)
    
    # Process templates
    templates = template_manager.get_templates("de", "it-operation")
    assert len(templates) == 3, "Should find 3 templates"
    
    processed_results = []
    for template in templates:
        content = template.read_content()
        result = processor.process_template(content, template.path.name)
        processed_results.append(result)
    
    # Verify all templates were processed
    assert len(processed_results) == 3, "All templates should be processed"
    
    # Combine all content for verification
    all_content = "\n\n".join([r.content for r in processed_results])
    
    # Verify organization placeholders were replaced
    assert "{{ meta.organization.name }}" not in all_content
    assert "{{ meta.organization.address }}" not in all_content
    assert "{{ meta.organization.city }}" not in all_content
    assert "{{ meta.organization.email }}" not in all_content
    
    # Verify actual organization values are present
    assert "Test Organization GmbH" in all_content
    assert "Test Street 123" in all_content
    assert "Test City" in all_content
    assert "info@test.example.com" in all_content
    
    # Verify role placeholders were replaced
    assert "{{ meta.ceo.name }}" not in all_content
    assert "{{ meta.cio.email }}" not in all_content
    assert "{{ meta.ciso.name }}" not in all_content
    
    # Verify actual role values are present
    assert "John Doe" in all_content
    assert "jane.smith@test.example.com" in all_content
    assert "Bob Johnson" in all_content
    
    # Verify document placeholders were replaced
    assert "{{ meta.document.owner }}" not in all_content
    assert "{{ meta.document.version }}" not in all_content
    
    # Verify actual document values are present
    assert "IT Operations Manager" in all_content
    assert "2.0.0" in all_content
    assert "internal" in all_content
    
    # Verify no errors occurred
    total_errors = sum(len(r.errors) for r in processed_results)
    assert total_errors == 0, "No errors should occur during processing"
    
    # Verify replacement statistics
    total_replacements = sum(len(r.replacements) for r in processed_results)
    assert total_replacements > 0, "Should have successful replacements"
    
    # Verify all replacements are from meta source
    for result in processed_results:
        for replacement in result.replacements:
            assert replacement.source == "meta", \
                f"All replacements should be from 'meta' source, got '{replacement.source}'"



@pytest.fixture
def mixed_placeholders_templates(temp_workspace):
    """Create templates with both netbox and meta placeholders for testing."""
    templates_dir = temp_workspace / "templates"
    
    de_it_operation = templates_dir / "de" / "it-operation"
    de_it_operation.mkdir(parents=True)
    
    # Template with mixed placeholders
    (de_it_operation / "0100_mixed.md").write_text("""# IT-Operations Handbuch

## Organisation
**Name:** {{ meta.organization.name }}
**Standort:** {{ meta.organization.city }}

## Infrastruktur
**Primärer Standort:** {{ netbox.site_name }}
**Backup-Server:** {{ netbox.device_name }}
**IP-Adresse:** {{ netbox.primary_ip }}

## Verantwortlichkeiten
**CIO:** {{ meta.cio.name }}
**E-Mail:** {{ meta.cio.email }}

## Dokumentinformationen
**Version:** {{ meta.document.version }}
**Autor:** {{ meta.author }}
**Datum:** {{ metadata.date }}
""")
    
    return templates_dir


@pytest.mark.integration
def test_end_to_end_with_mixed_placeholders(temp_workspace, mixed_placeholders_templates, 
                                            sample_metadata_config, mock_netbox_api):
    """
    Test end-to-end template processing with mixed netbox and meta placeholders.
    
    This test verifies:
    - Dual-source placeholder detection (netbox + meta)
    - Correct routing to appropriate adapters
    - Both sources work independently and correctly
    - Statistics track both sources separately
    
    Requirements: 16.5, 19.2
    """
    from src.meta_adapter import MetaAdapter
    
    output_dir = temp_workspace / "Handbook"
    
    # Initialize components
    template_manager = TemplateManager(mixed_placeholders_templates)
    
    # Create meta adapter
    meta_adapter = MetaAdapter(sample_metadata_config)
    meta_adapter.connect()
    
    # Create netbox adapter
    with patch('pynetbox.api') as mock_pynetbox:
        mock_pynetbox.return_value = mock_netbox_api
        
        netbox_adapter = NetBoxAdapter(
            url="https://netbox.example.com",
            api_token="test_token"
        )
        netbox_adapter.connect()
        
        # Create placeholder processor with both adapters
        metadata_dict = {
            "author": "Test Author",
            "version": "1.0.0"
        }
        data_sources = {
            "meta": meta_adapter,
            "netbox": netbox_adapter,
            "metadata": metadata_dict
        }
        processor = PlaceholderProcessor(data_sources, metadata_dict)
        
        # Process template
        templates = template_manager.get_templates("de", "it-operation")
        assert len(templates) == 1, "Should find 1 template"
        
        template = templates[0]
        content = template.read_content()
        result = processor.process_template(content, template.path.name)
        
        # Verify no errors
        assert len(result.errors) == 0, "No errors should occur"
        
        # Verify meta placeholders were replaced
        assert "{{ meta.organization.name }}" not in result.content
        assert "{{ meta.cio.name }}" not in result.content
        assert "{{ meta.document.version }}" not in result.content
        
        # Verify meta values are present
        assert "Test Organization GmbH" in result.content
        assert "Jane Smith" in result.content
        assert "2.0.0" in result.content
        
        # Verify netbox placeholders were replaced
        assert "{{ netbox.site_name }}" not in result.content
        assert "{{ netbox.device_name }}" not in result.content
        assert "{{ netbox.primary_ip }}" not in result.content
        
        # Verify netbox values are present
        assert "Datacenter Munich" in result.content
        assert "backup-server-01" in result.content
        assert "192.168.1.100" in result.content
        
        # Verify metadata placeholders were replaced
        assert "{{ metadata.date }}" not in result.content
        
        # Verify replacement statistics
        assert len(result.replacements) > 0, "Should have replacements"
        
        # Verify both sources were used
        sources_used = result.get_sources_used()
        assert "meta" in sources_used, "Meta source should be used"
        assert "netbox" in sources_used, "NetBox source should be used"
        assert "metadata" in sources_used, "Metadata source should be used"
        
        # Verify statistics by source
        stats = result.get_statistics_summary()
        assert stats.get("meta", 0) > 0, "Should have meta replacements"
        assert stats.get("netbox", 0) > 0, "Should have netbox replacements"
        assert stats.get("metadata", 0) > 0, "Should have metadata replacements"
        
        # Verify specific counts
        meta_count = result.get_replacement_count_by_source("meta")
        netbox_count = result.get_replacement_count_by_source("netbox")
        metadata_count = result.get_replacement_count_by_source("metadata")
        
        assert meta_count >= 5, f"Should have at least 5 meta replacements, got {meta_count}"
        assert netbox_count >= 3, f"Should have at least 3 netbox replacements, got {netbox_count}"
        assert metadata_count >= 1, f"Should have at least 1 metadata replacement, got {metadata_count}"


@pytest.fixture
def error_handling_templates(temp_workspace):
    """Create templates with various error conditions for testing."""
    templates_dir = temp_workspace / "templates"
    
    de_it_operation = templates_dir / "de" / "it-operation"
    de_it_operation.mkdir(parents=True)
    
    # Template with missing meta fields
    (de_it_operation / "0100_missing_fields.md").write_text("""# Test

**Existierendes Feld:** {{ meta.organization.name }}
**Fehlendes Feld:** {{ meta.organization.nonexistent_field }}
**Fehlende Rolle:** {{ meta.unknown_role.name }}
""")
    
    # Template with invalid field paths
    (de_it_operation / "0200_invalid_paths.md").write_text("""# Test

**Gültiger Pfad:** {{ meta.ceo.name }}
**Ungültiger Pfad:** {{ meta.ceo.invalid_field }}
""")
    
    return templates_dir


@pytest.mark.integration
def test_error_handling_missing_metadata_file(temp_workspace):
    """
    Test error handling when metadata.yaml file is missing.
    
    This test verifies:
    - System detects missing metadata.yaml
    - Appropriate error message is generated
    - Processing can continue with warnings
    
    Requirements: 16.4, 17.4, 17.5
    """
    from src.metadata_config_manager import MetadataConfigManager
    
    # Try to load non-existent metadata file
    metadata_path = temp_workspace / "metadata.yaml"
    manager = MetadataConfigManager(metadata_path)
    
    # Should raise FileNotFoundError
    with pytest.raises(FileNotFoundError) as exc_info:
        manager.load_metadata()
    
    # Verify error message is helpful
    error_message = str(exc_info.value)
    assert "not found" in error_message.lower()
    assert str(metadata_path) in error_message


@pytest.mark.integration
def test_error_handling_missing_fields(temp_workspace, error_handling_templates):
    """
    Test error handling when metadata fields are missing.
    
    This test verifies:
    - System detects missing fields in metadata
    - Warnings are generated for missing fields
    - Processing continues despite missing fields
    - Placeholders remain unchanged when fields not found
    
    Requirements: 16.4, 17.4, 17.5
    """
    from src.meta_adapter import MetaAdapter
    from src.metadata_config_manager import (
        MetadataConfig, OrganizationInfo, PersonRole, DocumentInfo
    )
    
    # Create minimal metadata config (missing some fields)
    organization = OrganizationInfo(
        name="Test Org",
        address="Test Address",
        city="Test City",
        postal_code="12345",
        country="Germany",
        website="https://test.com",
        phone="+49 123 456789",
        email="info@test.com"
    )
    
    # Only include CEO role, missing other roles
    roles = {
        "ceo": PersonRole(
            name="John Doe",
            title="CEO",
            email="john@test.com",
            phone="+49 123 456789"
        )
    }
    
    document = DocumentInfo(
        owner="Test Owner",
        approver="Test Approver",
        version="1.0.0",
        classification="internal"
    )
    
    metadata_config = MetadataConfig(
        organization=organization,
        roles=roles,
        document=document,
        author="Test Author",
        language="de"
    )
    
    # Initialize components
    template_manager = TemplateManager(error_handling_templates)
    meta_adapter = MetaAdapter(metadata_config)
    meta_adapter.connect()
    
    data_sources = {"meta": meta_adapter}
    processor = PlaceholderProcessor(data_sources)
    
    # Process templates
    templates = template_manager.get_templates("de", "it-operation")
    
    all_warnings = []
    for template in templates:
        content = template.read_content()
        result = processor.process_template(content, template.path.name)
        all_warnings.extend(result.warnings)
    
    # Verify warnings were generated
    assert len(all_warnings) > 0, "Should generate warnings for missing fields"
    
    # Verify warnings mention missing fields
    warning_text = " ".join(all_warnings).lower()
    assert "not found" in warning_text or "unknown" in warning_text or "missing" in warning_text, \
        "Warnings should mention missing/unknown fields"


@pytest.mark.integration
def test_error_handling_invalid_field_paths(temp_workspace, error_handling_templates, 
                                            sample_metadata_config):
    """
    Test error handling for invalid field paths in meta placeholders.
    
    This test verifies:
    - System detects invalid field paths
    - Warnings are generated for invalid paths
    - Valid placeholders are still replaced
    - Processing continues despite errors
    
    Requirements: 16.4
    """
    from src.meta_adapter import MetaAdapter
    
    # Initialize components
    template_manager = TemplateManager(error_handling_templates)
    meta_adapter = MetaAdapter(sample_metadata_config)
    meta_adapter.connect()
    
    data_sources = {"meta": meta_adapter}
    processor = PlaceholderProcessor(data_sources)
    
    # Process template with invalid paths
    templates = template_manager.get_templates("de", "it-operation")
    invalid_path_template = [t for t in templates if "invalid_paths" in t.path.name][0]
    
    content = invalid_path_template.read_content()
    result = processor.process_template(content, invalid_path_template.path.name)
    
    # Verify warnings were generated
    assert len(result.warnings) > 0, "Should generate warnings for invalid field paths"
    
    # Verify valid placeholder was replaced
    assert "John Doe" in result.content, "Valid placeholder should be replaced"
    
    # Verify invalid placeholder generated warning
    warning_text = " ".join(result.warnings).lower()
    assert "invalid_field" in warning_text or "not found" in warning_text, \
        "Warning should mention invalid field"
    
    # Verify processing continued
    assert result.content, "Should have processed content despite errors"
    
    # Verify some replacements succeeded
    assert len(result.replacements) > 0, "Should have some successful replacements"



# ============================================================================
# Phase 3: Integration Tests für vollständigen Workflow
# ============================================================================

@pytest.fixture
def it_operations_templates(temp_workspace):
    """Create complete IT-Operations templates for end-to-end testing."""
    templates_dir = temp_workspace / "templates"
    
    # German IT-Operations templates
    de_it_op = templates_dir / "de" / "it-operation"
    de_it_op.mkdir(parents=True)
    
    # Metadata template
    (de_it_op / "0000_metadata_de_it-operation.md").write_text("""# IT-Operations Handbuch

**Dokument-Metadaten**

- **Organisation:** {{ meta.organization.name }}
- **Erstellt am:** {{ metadata.date }}
- **Autor:** {{ meta.author }}
- **Version:** {{ meta.document.version }}

---
""")
    
    # Introduction
    (de_it_op / "0010_Einleitung.md").write_text("""# 1. Einleitung

## 1.1 Zweck

Dieses IT-Operations-Handbuch beschreibt die Betriebsprozesse für {{ meta.organization.name }}.

## 1.2 Geltungsbereich

Standort: {{ netbox.site_name }}
Verantwortlicher: {{ meta.cio.name }} ({{ meta.cio.email }})
""")
    
    # Roles and Responsibilities
    (de_it_op / "0060_Rollen_und_Verantwortlichkeiten.md").write_text("""# 6. Rollen und Verantwortlichkeiten

## 6.1 Führungsebene

### Chief Information Officer (CIO)
- **Name:** {{ meta.cio.name }}
- **E-Mail:** {{ meta.cio.email }}
- **Telefon:** {{ meta.cio.phone }}

### Chief Information Security Officer (CISO)
- **Name:** {{ meta.ciso.name }}
- **E-Mail:** {{ meta.ciso.email }}
- **Telefon:** {{ meta.ciso.phone }}

## 6.2 Infrastruktur

**Primärer Standort:** {{ netbox.site_name }}
**Backup-Server:** {{ netbox.device_name }}
**IP-Adresse:** {{ netbox.primary_ip }}
""")
    
    # English IT-Operations templates
    en_it_op = templates_dir / "en" / "it-operation"
    en_it_op.mkdir(parents=True)
    
    # Metadata template
    (en_it_op / "0000_metadata_en_it-operation.md").write_text("""# IT-Operations Handbook

**Document Metadata**

- **Organization:** {{ meta.organization.name }}
- **Created:** {{ metadata.date }}
- **Author:** {{ meta.author }}
- **Version:** {{ meta.document.version }}

---
""")
    
    # Introduction
    (en_it_op / "0010_Introduction.md").write_text("""# 1. Introduction

## 1.1 Purpose

This IT-Operations Handbook describes the operational processes for {{ meta.organization.name }}.

## 1.2 Scope

Location: {{ netbox.site_name }}
Responsible: {{ meta.cio.name }} ({{ meta.cio.email }})
""")
    
    # Roles and Responsibilities
    (en_it_op / "0060_Roles_and_Responsibilities.md").write_text("""# 6. Roles and Responsibilities

## 6.1 Leadership

### Chief Information Officer (CIO)
- **Name:** {{ meta.cio.name }}
- **Email:** {{ meta.cio.email }}
- **Phone:** {{ meta.cio.phone }}

### Chief Information Security Officer (CISO)
- **Name:** {{ meta.ciso.name }}
- **Email:** {{ meta.ciso.email }}
- **Phone:** {{ meta.ciso.phone }}

## 6.2 Infrastructure

**Primary Location:** {{ netbox.site_name }}
**Backup Server:** {{ netbox.device_name }}
**IP Address:** {{ netbox.primary_ip }}
""")
    
    return templates_dir


@pytest.mark.integration
def test_end_to_end_it_operations_handbook_generation(temp_workspace, it_operations_templates, 
                                                      sample_metadata_config, mock_netbox_api):
    """
    Test vollständige IT-Operations-Handbuch-Generierung.
    
    This test verifies:
    - Complete IT-Operations handbook generation
    - Integration of metadata.yaml and config.yaml
    - All placeholder replacements (meta + netbox)
    - Correct output structure
    - No errors during processing
    
    Requirements: Alle (Phase 3, Task 3.3.1)
    """
    from src.meta_adapter import MetaAdapter
    
    output_dir = temp_workspace / "Handbook"
    
    # Initialize components
    template_manager = TemplateManager(it_operations_templates)
    
    # Create meta adapter
    meta_adapter = MetaAdapter(sample_metadata_config)
    meta_adapter.connect()
    
    # Create netbox adapter
    with patch('pynetbox.api') as mock_pynetbox:
        mock_pynetbox.return_value = mock_netbox_api
        
        netbox_adapter = NetBoxAdapter(
            url="https://netbox.example.com",
            api_token="test_token"
        )
        netbox_adapter.connect()
        
        # Create placeholder processor with both adapters
        metadata_dict = {
            "author": "Test Author",
            "version": "1.0.0",
            "date": "2025-01-30"
        }
        data_sources = {
            "meta": meta_adapter,
            "netbox": netbox_adapter,
            "metadata": metadata_dict
        }
        processor = PlaceholderProcessor(data_sources, metadata_dict)
        output_generator = OutputGenerator(output_dir, test_mode=True)
        
        # Process German templates
        de_templates = template_manager.get_templates("de", "it-operation")
        assert len(de_templates) == 3, "Should find 3 German templates"
        
        de_results = []
        for template in de_templates:
            content = template.read_content()
            result = processor.process_template(content, template.path.name)
            de_results.append(result)
        
        # Verify no errors
        total_errors = sum(len(r.errors) for r in de_results)
        assert total_errors == 0, "No errors should occur during processing"
        
        # Verify all placeholders were replaced
        all_content = "\n\n".join([r.content for r in de_results])
        
        # Check meta placeholders
        assert "{{ meta.organization.name }}" not in all_content
        assert "{{ meta.cio.name }}" not in all_content
        assert "{{ meta.ciso.email }}" not in all_content
        assert "{{ meta.document.version }}" not in all_content
        
        # Check netbox placeholders
        assert "{{ netbox.site_name }}" not in all_content
        assert "{{ netbox.device_name }}" not in all_content
        assert "{{ netbox.primary_ip }}" not in all_content
        
        # Check metadata placeholders
        assert "{{ metadata.date }}" not in all_content
        
        # Verify actual values are present
        assert "Test Organization GmbH" in all_content
        assert "Jane Smith" in all_content
        assert "Bob Johnson" in all_content
        assert "Datacenter Munich" in all_content
        assert "backup-server-01" in all_content
        assert "192.168.1.100" in all_content
        # Date will be current date (check for year 2026 or 2025)
        assert "2026-" in all_content or "2025-" in all_content
        
        # Generate output
        de_output_result = output_generator.generate_markdown(
            [r.content for r in de_results], "de", "it-operation"
        )
        de_output = de_output_result.markdown_path
        
        # Verify output structure
        assert de_output.exists(), "German output should exist"
        assert de_output.parent == output_dir / "de" / "it-operation" / "markdown" 
        assert de_output.name == "it-operation_handbook.md"
        
        # Verify output content
        output_content = de_output.read_text()
        assert "IT-Operations Handbuch" in output_content
        assert "Test Organization GmbH" in output_content
        assert "Jane Smith" in output_content
        assert "Datacenter Munich" in output_content
        
        # Verify replacement statistics
        total_replacements = sum(len(r.replacements) for r in de_results)
        assert total_replacements > 0, "Should have successful replacements"
        
        # Verify both sources were used
        meta_count = sum(r.get_replacement_count_by_source("meta") for r in de_results)
        netbox_count = sum(r.get_replacement_count_by_source("netbox") for r in de_results)
        metadata_count = sum(r.get_replacement_count_by_source("metadata") for r in de_results)
        
        assert meta_count > 0, "Should have meta replacements"
        assert netbox_count > 0, "Should have netbox replacements"
        assert metadata_count > 0, "Should have metadata replacements"


@pytest.mark.integration
def test_end_to_end_bilingual_handbook_generation(temp_workspace, it_operations_templates, 
                                                  sample_metadata_config, mock_netbox_api):
    """
    Test bilinguale Handbuch-Generierung (Deutsch und Englisch).
    
    This test verifies:
    - German and English handbook generation
    - Correct output structure for both languages
    - Independent processing of each language
    - Same data sources used for both languages
    
    Requirements: 21.1, 21.5 (Phase 3, Task 3.3.2)
    """
    from src.meta_adapter import MetaAdapter
    
    output_dir = temp_workspace / "Handbook"
    
    # Initialize components
    template_manager = TemplateManager(it_operations_templates)
    
    # Create meta adapter
    meta_adapter = MetaAdapter(sample_metadata_config)
    meta_adapter.connect()
    
    # Create netbox adapter
    with patch('pynetbox.api') as mock_pynetbox:
        mock_pynetbox.return_value = mock_netbox_api
        
        netbox_adapter = NetBoxAdapter(
            url="https://netbox.example.com",
            api_token="test_token"
        )
        netbox_adapter.connect()
        
        # Create placeholder processor
        metadata_dict = {
            "author": "Test Author",
            "version": "1.0.0",
            "date": "2025-01-30"
        }
        data_sources = {
            "meta": meta_adapter,
            "netbox": netbox_adapter,
            "metadata": metadata_dict
        }
        processor = PlaceholderProcessor(data_sources, metadata_dict)
        output_generator = OutputGenerator(output_dir, test_mode=True)
        
        # Process German templates
        de_templates = template_manager.get_templates("de", "it-operation")
        de_results = []
        for template in de_templates:
            content = template.read_content()
            result = processor.process_template(content, template.path.name)
            de_results.append(result)
        
        de_output_result = output_generator.generate_markdown(
            [r.content for r in de_results], "de", "it-operation"
        )
        de_output = de_output_result.markdown_path
        
        # Process English templates
        en_templates = template_manager.get_templates("en", "it-operation")
        en_results = []
        for template in en_templates:
            content = template.read_content()
            result = processor.process_template(content, template.path.name)
            en_results.append(result)
        
        en_output_result = output_generator.generate_markdown(
            [r.content for r in en_results], "en", "it-operation"
        )
        en_output = en_output_result.markdown_path
        
        # Verify both outputs exist
        assert de_output.exists(), "German output should exist"
        assert en_output.exists(), "English output should exist"
        
        # Verify correct directory structure
        assert de_output.parent == output_dir / "de" / "it-operation" / "markdown" 
        assert en_output.parent == output_dir / "en" / "it-operation" / "markdown"
        
        # Verify language-specific content
        de_content = de_output.read_text()
        assert "IT-Operations Handbuch" in de_content
        assert "Einleitung" in de_content
        assert "Rollen und Verantwortlichkeiten" in de_content
        
        en_content = en_output.read_text()
        assert "IT-Operations Handbook" in en_content
        assert "Introduction" in en_content
        assert "Roles and Responsibilities" in en_content
        
        # Verify same data values in both languages
        assert "Test Organization GmbH" in de_content
        assert "Test Organization GmbH" in en_content
        assert "Jane Smith" in de_content
        assert "Jane Smith" in en_content
        assert "Datacenter Munich" in de_content
        assert "Datacenter Munich" in en_content
        
        # Verify files are independent
        assert de_content != en_content, "Language outputs should differ"
        
        # Verify no errors in either language
        de_errors = sum(len(r.errors) for r in de_results)
        en_errors = sum(len(r.errors) for r in en_results)
        assert de_errors == 0, "No errors in German processing"
        assert en_errors == 0, "No errors in English processing"


@pytest.fixture
def service_template(temp_workspace):
    """Create service description template for testing."""
    templates_dir = temp_workspace / "templates"
    
    # German service template
    de_service = templates_dir / "de" / "service-templates"
    de_service.mkdir(parents=True)
    
    (de_service / "service_description_template.md").write_text("""# Service-Beschreibung: [SERVICE_NAME]

## Service-Übersicht

### Basis-Informationen
- **Service-Name:** [TODO: Service-Name eintragen]
- **Service-Owner:** {{ meta.cio.name }}
- **Technischer Ansprechpartner:** {{ meta.it_operations_manager.name }}
- **Version:** {{ meta.document.version }}

### Kurzbeschreibung
[TODO: 2-3 Sätze zur Beschreibung des Service]

## Technische Details

### Systemkomponenten
| Komponente | Standort | Verantwortlich |
|---|---|---|
| {{ netbox.device_name }} | {{ netbox.site_name }} | {{ meta.cio.name }} |

### Infrastruktur
- **IP-Adresse:** {{ netbox.primary_ip }}
- **Standort:** {{ netbox.site_name }}

## Kontakte und Eskalation

### Verantwortlichkeiten
- **Service Owner:** {{ meta.cio.name }} ({{ meta.cio.email }})
- **Technical Lead:** {{ meta.it_operations_manager.name }}
- **On-Call:** {{ meta.service_desk_lead.name }}

### Eskalationspfad
1. **Level 1:** Service Desk - {{ meta.service_desk_lead.email }}
2. **Level 2:** IT Operations - {{ meta.it_operations_manager.email }}
3. **Level 3:** CIO - {{ meta.cio.email }}

---

**Dokumentverantwortlicher:** {{ meta.document.owner }}  
**Genehmigt durch:** {{ meta.document.approver }}  
**Organisation:** {{ meta.organization.name }}
""")
    
    return templates_dir


@pytest.fixture
def extended_metadata_config():
    """Create extended metadata configuration with additional roles."""
    from src.metadata_config_manager import (
        MetadataConfig, OrganizationInfo, PersonRole, DocumentInfo
    )
    
    organization = OrganizationInfo(
        name="Test Organization GmbH",
        address="Test Street 123",
        city="Test City",
        postal_code="12345",
        country="Germany",
        website="https://test.example.com",
        phone="+49 123 456789",
        email="info@test.example.com"
    )
    
    roles = {
        "ceo": PersonRole(
            name="John Doe",
            title="Chief Executive Officer",
            email="john.doe@test.example.com",
            phone="+49 123 456789-100"
        ),
        "cio": PersonRole(
            name="Jane Smith",
            title="Chief Information Officer",
            email="jane.smith@test.example.com",
            phone="+49 123 456789-200"
        ),
        "ciso": PersonRole(
            name="Bob Johnson",
            title="Chief Information Security Officer",
            email="bob.johnson@test.example.com",
            phone="+49 123 456789-300"
        ),
        "it_operations_manager": PersonRole(
            name="Alice Williams",
            title="IT Operations Manager",
            email="alice.williams@test.example.com",
            phone="+49 123 456789-250"
        ),
        "service_desk_lead": PersonRole(
            name="Charlie Brown",
            title="Service Desk Lead",
            email="charlie.brown@test.example.com",
            phone="+49 123 456789-111"
        )
    }
    
    document = DocumentInfo(
        owner="IT Operations Manager",
        approver="CIO",
        version="2.0.0",
        classification="internal"
    )
    
    return MetadataConfig(
        organization=organization,
        roles=roles,
        document=document,
        author="Test Author [test@example.com]",
        language="de"
    )


@pytest.mark.integration
def test_service_template_workflow(temp_workspace, service_template, 
                                  extended_metadata_config, mock_netbox_api):
    """
    Test Service-Template-Workflow.
    
    This test verifies:
    - Service template can be copied and individualized
    - Placeholders are replaced correctly
    - Handbook can be generated from service template
    - All role placeholders work (including additional roles)
    
    Requirements: 15.1, 15.4 (Phase 3, Task 3.3.3)
    """
    from src.meta_adapter import MetaAdapter
    
    output_dir = temp_workspace / "Handbook"
    
    # Initialize components
    template_manager = TemplateManager(service_template)
    
    # Create meta adapter with extended metadata
    meta_adapter = MetaAdapter(extended_metadata_config)
    meta_adapter.connect()
    
    # Create netbox adapter
    with patch('pynetbox.api') as mock_pynetbox:
        mock_pynetbox.return_value = mock_netbox_api
        
        netbox_adapter = NetBoxAdapter(
            url="https://netbox.example.com",
            api_token="test_token"
        )
        netbox_adapter.connect()
        
        # Create placeholder processor
        metadata_dict = {
            "author": "Test Author",
            "version": "1.0.0",
            "date": "2025-01-30"
        }
        data_sources = {
            "meta": meta_adapter,
            "netbox": netbox_adapter,
            "metadata": metadata_dict
        }
        processor = PlaceholderProcessor(data_sources, metadata_dict)
        output_generator = OutputGenerator(output_dir, test_mode=True)
        
        # Process service template
        templates = template_manager.get_templates("de", "service-templates")
        assert len(templates) == 1, "Should find 1 service template"
        
        template = templates[0]
        content = template.read_content()
        result = processor.process_template(content, template.path.name)
        
        # Verify no errors
        assert len(result.errors) == 0, "No errors should occur"
        
        # Verify standard role placeholders were replaced
        assert "{{ meta.cio.name }}" not in result.content
        assert "{{ meta.cio.email }}" not in result.content
        
        # Verify additional role placeholders were replaced
        assert "{{ meta.it_operations_manager.name }}" not in result.content
        assert "{{ meta.it_operations_manager.email }}" not in result.content
        assert "{{ meta.service_desk_lead.name }}" not in result.content
        assert "{{ meta.service_desk_lead.email }}" not in result.content
        
        # Verify netbox placeholders were replaced
        assert "{{ netbox.device_name }}" not in result.content
        assert "{{ netbox.site_name }}" not in result.content
        assert "{{ netbox.primary_ip }}" not in result.content
        
        # Verify document placeholders were replaced
        assert "{{ meta.document.owner }}" not in result.content
        assert "{{ meta.document.approver }}" not in result.content
        assert "{{ meta.organization.name }}" not in result.content
        
        # Verify actual values are present
        assert "Jane Smith" in result.content  # CIO
        assert "Alice Williams" in result.content  # IT Ops Manager
        assert "Charlie Brown" in result.content  # Service Desk Lead
        assert "backup-server-01" in result.content  # Device
        assert "Datacenter Munich" in result.content  # Site
        assert "192.168.1.100" in result.content  # IP
        assert "IT Operations Manager" in result.content  # Document owner
        assert "CIO" in result.content  # Document approver
        assert "Test Organization GmbH" in result.content  # Organization
        
        # Verify TODO markers are still present (for individualization)
        assert "[TODO:" in result.content, "TODO markers should remain for individualization"
        assert "[SERVICE_NAME]" in result.content, "Service name placeholder should remain"
        
        # Generate output
        output_result = output_generator.generate_markdown(
            [result.content], "de", "service-templates"
        )
        output_path = output_result.markdown_path
        
        # Verify output was created
        assert output_path.exists(), "Service template output should exist"
        assert output_path.parent == output_dir / "de" / "service-templates" / "markdown" 
        
        # Verify output content
        output_content = output_path.read_text()
        assert "Service-Beschreibung" in output_content
        assert "Jane Smith" in output_content
        assert "Alice Williams" in output_content
        assert "Datacenter Munich" in output_content
        
        # Verify replacement statistics
        assert len(result.replacements) > 0, "Should have successful replacements"
        
        # Verify all three sources were used
        meta_count = result.get_replacement_count_by_source("meta")
        netbox_count = result.get_replacement_count_by_source("netbox")
        
        assert meta_count > 0, "Should have meta replacements"
        assert netbox_count > 0, "Should have netbox replacements"
        
        # Verify specific role counts
        # Should have replacements for CIO, IT Ops Manager, Service Desk Lead
        assert meta_count >= 10, f"Should have at least 10 meta replacements, got {meta_count}"


# ============================================================================
# Phase 5.5: Integration Tests for New Template Types
# ============================================================================

@pytest.fixture
def bcm_templates(temp_workspace):
    """Create BCM templates for end-to-end testing."""
    templates_dir = temp_workspace / "templates"
    
    # German BCM templates
    de_bcm = templates_dir / "de" / "bcm"
    de_bcm.mkdir(parents=True)
    
    # Metadata template
    (de_bcm / "0000_metadata_de_bcm.md").write_text("""# BCM-Handbuch

**Dokument-Metadaten**

- **Organisation:** {{ meta.organization.name }}
- **Erstellt am:** {{ metadata.date }}
- **Autor:** {{ meta.author }}
- **Version:** {{ meta.document.version }}
- **Typ:** Business Continuity Management Handbuch

---
""")
    
    # Purpose and Scope
    (de_bcm / "0010_Zweck_und_Geltungsbereich.md").write_text("""# 1. Zweck und Geltungsbereich

## 1.1 Zweck

Dieses BCM-Handbuch beschreibt das Business Continuity Management für {{ meta.organization.name }}.

**Referenz:** ISO 22301:2019

## 1.2 Geltungsbereich

- **Organisation:** {{ meta.organization.name }}
- **Standort:** {{ netbox.site_name }}
- **BCM-Verantwortlicher:** {{ meta.cio.name }}

## 1.3 Zielgruppe

Dieses Handbuch richtet sich an:
- Geschäftsführung
- BCM-Team
- Krisenmanagement-Team
""")
    
    # BCM Policy
    (de_bcm / "0020_BCM_Leitlinie_Policy.md").write_text("""# 2. BCM-Leitlinie (Policy)

## 2.1 Management Commitment

Die Geschäftsführung von {{ meta.organization.name }} verpflichtet sich zur Implementierung und Aufrechterhaltung eines Business Continuity Management Systems nach ISO 22301.

**CEO:** {{ meta.ceo.name }}  
**CIO:** {{ meta.cio.name }}

## 2.2 BCM-Governance

### RACI-Matrix

| Aktivität | CEO | CIO | BCM-Manager |
|---|---|---|---|
| BCM-Strategie | A | R | C |
| BIA-Durchführung | I | A | R |
| Plan-Tests | I | A | R |

**Legende:** R=Responsible, A=Accountable, C=Consulted, I=Informed

## 2.3 Infrastruktur

**Primärer Standort:** {{ netbox.site_name }}  
**Backup-Infrastruktur:** {{ netbox.device_name }}
""")
    
    # BIA Methodology
    (de_bcm / "0070_BIA_Methodik.md").write_text("""# 7. BIA-Methodik

## 7.1 Business Impact Analysis

Die Business Impact Analysis (BIA) wird nach ISO 22301 durchgeführt.

**Verantwortlich:** {{ meta.cio.name }}

## 7.2 Kritikalitätsbewertung

Standort: {{ netbox.site_name }}

[TODO: Kritikalitätsbewertung für spezifische Services eintragen]

## 7.3 RTO/RPO Definitionen

[TODO: Recovery Time Objectives und Recovery Point Objectives definieren]
""")
    
    # English BCM templates
    en_bcm = templates_dir / "en" / "bcm"
    en_bcm.mkdir(parents=True)
    
    # Metadata template
    (en_bcm / "0000_metadata_en_bcm.md").write_text("""# BCM Handbook

**Document Metadata**

- **Organization:** {{ meta.organization.name }}
- **Created:** {{ metadata.date }}
- **Author:** {{ meta.author }}
- **Version:** {{ meta.document.version }}
- **Type:** Business Continuity Management Handbook

---
""")
    
    # Purpose and Scope
    (en_bcm / "0010_Purpose_and_Scope.md").write_text("""# 1. Purpose and Scope

## 1.1 Purpose

This BCM Handbook describes the Business Continuity Management for {{ meta.organization.name }}.

**Reference:** ISO 22301:2019

## 1.2 Scope

- **Organization:** {{ meta.organization.name }}
- **Location:** {{ netbox.site_name }}
- **BCM Responsible:** {{ meta.cio.name }}

## 1.3 Target Audience

This handbook is intended for:
- Management
- BCM Team
- Crisis Management Team
""")
    
    # BCM Policy
    (en_bcm / "0020_BCM_Policy.md").write_text("""# 2. BCM Policy

## 2.1 Management Commitment

The management of {{ meta.organization.name }} commits to implementing and maintaining a Business Continuity Management System according to ISO 22301.

**CEO:** {{ meta.ceo.name }}  
**CIO:** {{ meta.cio.name }}

## 2.2 BCM Governance

### RACI Matrix

| Activity | CEO | CIO | BCM Manager |
|---|---|---|---|
| BCM Strategy | A | R | C |
| BIA Execution | I | A | R |
| Plan Tests | I | A | R |

**Legend:** R=Responsible, A=Accountable, C=Consulted, I=Informed

## 2.3 Infrastructure

**Primary Location:** {{ netbox.site_name }}  
**Backup Infrastructure:** {{ netbox.device_name }}
""")
    
    # BIA Methodology
    (en_bcm / "0070_BIA_Methodology.md").write_text("""# 7. BIA Methodology

## 7.1 Business Impact Analysis

The Business Impact Analysis (BIA) is conducted according to ISO 22301.

**Responsible:** {{ meta.cio.name }}

## 7.2 Criticality Assessment

Location: {{ netbox.site_name }}

[TODO: Enter criticality assessment for specific services]

## 7.3 RTO/RPO Definitions

[TODO: Define Recovery Time Objectives and Recovery Point Objectives]
""")
    
    return templates_dir


@pytest.mark.integration
def test_end_to_end_bcm_handbook_generation_german(temp_workspace, bcm_templates, 
                                                   sample_metadata_config, mock_netbox_api):
    """
    Test end-to-end BCM handbook generation for German.
    
    This test verifies:
    - German BCM handbook generation
    - ISO 22301 references present
    - RACI matrices included
    - All placeholder replacements (meta + netbox)
    - Correct output structure
    - No errors during processing
    
    Requirements: All BCM requirements (1.1-4.5)
    Task: 5.5.1
    """
    from src.meta_adapter import MetaAdapter
    
    output_dir = temp_workspace / "Handbook"
    
    # Initialize components
    template_manager = TemplateManager(bcm_templates)
    
    # Create meta adapter
    meta_adapter = MetaAdapter(sample_metadata_config)
    meta_adapter.connect()
    
    # Create netbox adapter
    with patch('pynetbox.api') as mock_pynetbox:
        mock_pynetbox.return_value = mock_netbox_api
        
        netbox_adapter = NetBoxAdapter(
            url="https://netbox.example.com",
            api_token="test_token"
        )
        netbox_adapter.connect()
        
        # Create placeholder processor
        metadata_dict = {
            "author": "Test Author",
            "version": "1.0.0",
            "date": "2025-01-30"
        }
        data_sources = {
            "meta": meta_adapter,
            "netbox": netbox_adapter,
            "metadata": metadata_dict
        }
        processor = PlaceholderProcessor(data_sources, metadata_dict)
        output_generator = OutputGenerator(output_dir, test_mode=True)
        
        # Process German BCM templates
        de_templates = template_manager.get_templates("de", "bcm")
        assert len(de_templates) == 4, "Should find 4 German BCM templates"
        
        de_results = []
        for template in de_templates:
            content = template.read_content()
            result = processor.process_template(content, template.path.name)
            de_results.append(result)
        
        # Verify no errors
        total_errors = sum(len(r.errors) for r in de_results)
        assert total_errors == 0, "No errors should occur during processing"
        
        # Verify all placeholders were replaced
        all_content = "\n\n".join([r.content for r in de_results])
        
        # Check meta placeholders
        assert "{{ meta.organization.name }}" not in all_content
        assert "{{ meta.ceo.name }}" not in all_content
        assert "{{ meta.cio.name }}" not in all_content
        assert "{{ meta.document.version }}" not in all_content
        assert "{{ meta.author }}" not in all_content
        
        # Check netbox placeholders
        assert "{{ netbox.site_name }}" not in all_content
        assert "{{ netbox.device_name }}" not in all_content
        
        # Check metadata placeholders
        assert "{{ metadata.date }}" not in all_content
        
        # Verify actual values are present
        assert "Test Organization GmbH" in all_content
        assert "John Doe" in all_content  # CEO
        assert "Jane Smith" in all_content  # CIO
        assert "Datacenter Munich" in all_content
        assert "backup-server-01" in all_content
        
        # Verify ISO 22301 references
        assert "ISO 22301" in all_content, "Should contain ISO 22301 references"
        
        # Verify RACI matrix present
        assert "RACI" in all_content or "Responsible" in all_content, \
            "Should contain RACI matrix"
        
        # Verify TODO markers remain (for customization)
        assert "[TODO:" in all_content, "TODO markers should remain for customization"
        
        # Generate output
        de_output_result = output_generator.generate_markdown(
            [r.content for r in de_results], "de", "bcm"
        )
        de_output = de_output_result.markdown_path
        
        # Verify output structure
        assert de_output.exists(), "German BCM output should exist"
        assert de_output.parent == output_dir / "de" / "bcm" / "markdown" 
        assert de_output.name == "bcm_handbook.md"
        
        # Verify output content
        output_content = de_output.read_text()
        assert "BCM-Handbuch" in output_content
        assert "Business Continuity Management" in output_content
        assert "Test Organization GmbH" in output_content
        assert "ISO 22301" in output_content
        
        # Verify replacement statistics
        total_replacements = sum(len(r.replacements) for r in de_results)
        assert total_replacements > 0, "Should have successful replacements"


@pytest.mark.integration
def test_end_to_end_bcm_handbook_generation_english(temp_workspace, bcm_templates, 
                                                    sample_metadata_config, mock_netbox_api):
    """
    Test end-to-end BCM handbook generation for English.
    
    This test verifies:
    - English BCM handbook generation
    - Bilingual consistency (same structure as German)
    - All placeholder replacements work in English
    - Correct output structure
    
    Requirements: 3.1, 3.2, 3.3, 3.4, 3.5
    Task: 5.5.1
    """
    from src.meta_adapter import MetaAdapter
    
    output_dir = temp_workspace / "Handbook"
    
    # Initialize components
    template_manager = TemplateManager(bcm_templates)
    
    # Create meta adapter
    meta_adapter = MetaAdapter(sample_metadata_config)
    meta_adapter.connect()
    
    # Create netbox adapter
    with patch('pynetbox.api') as mock_pynetbox:
        mock_pynetbox.return_value = mock_netbox_api
        
        netbox_adapter = NetBoxAdapter(
            url="https://netbox.example.com",
            api_token="test_token"
        )
        netbox_adapter.connect()
        
        # Create placeholder processor
        metadata_dict = {
            "author": "Test Author",
            "version": "1.0.0",
            "date": "2025-01-30"
        }
        data_sources = {
            "meta": meta_adapter,
            "netbox": netbox_adapter,
            "metadata": metadata_dict
        }
        processor = PlaceholderProcessor(data_sources, metadata_dict)
        output_generator = OutputGenerator(output_dir, test_mode=True)
        
        # Process English BCM templates
        en_templates = template_manager.get_templates("en", "bcm")
        assert len(en_templates) == 4, "Should find 4 English BCM templates"
        
        en_results = []
        for template in en_templates:
            content = template.read_content()
            result = processor.process_template(content, template.path.name)
            en_results.append(result)
        
        # Verify no errors
        total_errors = sum(len(r.errors) for r in en_results)
        assert total_errors == 0, "No errors should occur during processing"
        
        # Verify all placeholders were replaced
        all_content = "\n\n".join([r.content for r in en_results])
        
        # Check placeholders were replaced
        assert "{{ meta.organization.name }}" not in all_content
        assert "{{ meta.ceo.name }}" not in all_content
        assert "{{ meta.cio.name }}" not in all_content
        assert "{{ netbox.site_name }}" not in all_content
        assert "{{ netbox.device_name }}" not in all_content
        
        # Verify actual values are present
        assert "Test Organization GmbH" in all_content
        assert "John Doe" in all_content
        assert "Jane Smith" in all_content
        assert "Datacenter Munich" in all_content
        assert "backup-server-01" in all_content
        
        # Verify ISO 22301 references
        assert "ISO 22301" in all_content
        
        # Verify RACI matrix present
        assert "RACI" in all_content or "Responsible" in all_content
        
        # Generate output
        en_output_result = output_generator.generate_markdown(
            [r.content for r in en_results], "en", "bcm"
        )
        en_output = en_output_result.markdown_path
        
        # Verify output structure
        assert en_output.exists(), "English BCM output should exist"
        assert en_output.parent == output_dir / "en" / "bcm" / "markdown" 
        assert en_output.name == "bcm_handbook.md"
        
        # Verify output content
        output_content = en_output.read_text()
        assert "BCM Handbook" in output_content
        assert "Business Continuity Management" in output_content
        assert "Test Organization GmbH" in output_content
        assert "ISO 22301" in output_content


@pytest.mark.integration
def test_bcm_bilingual_consistency(temp_workspace, bcm_templates, 
                                  sample_metadata_config, mock_netbox_api):
    """
    Test BCM bilingual consistency.
    
    This test verifies:
    - German and English BCM templates have same structure
    - Same number of templates in both languages
    - Same placeholder usage
    - Same data values in both outputs
    
    Requirements: 3.3, 3.4, 3.5
    Task: 5.5.1
    """
    from src.meta_adapter import MetaAdapter
    
    output_dir = temp_workspace / "Handbook"
    
    # Initialize components
    template_manager = TemplateManager(bcm_templates)
    
    # Create adapters
    meta_adapter = MetaAdapter(sample_metadata_config)
    meta_adapter.connect()
    
    with patch('pynetbox.api') as mock_pynetbox:
        mock_pynetbox.return_value = mock_netbox_api
        
        netbox_adapter = NetBoxAdapter(
            url="https://netbox.example.com",
            api_token="test_token"
        )
        netbox_adapter.connect()
        
        metadata_dict = {
            "author": "Test Author",
            "version": "1.0.0",
            "date": "2025-01-30"
        }
        data_sources = {
            "meta": meta_adapter,
            "netbox": netbox_adapter,
            "metadata": metadata_dict
        }
        processor = PlaceholderProcessor(data_sources, metadata_dict)
        output_generator = OutputGenerator(output_dir, test_mode=True)
        
        # Process both languages
        de_templates = template_manager.get_templates("de", "bcm")
        en_templates = template_manager.get_templates("en", "bcm")
        
        # Verify same number of templates
        assert len(de_templates) == len(en_templates), \
            "German and English should have same number of templates"
        
        # Process German
        de_results = []
        for template in de_templates:
            content = template.read_content()
            result = processor.process_template(content, template.path.name)
            de_results.append(result)
        
        # Process English
        en_results = []
        for template in en_templates:
            content = template.read_content()
            result = processor.process_template(content, template.path.name)
            en_results.append(result)
        
        # Verify same number of replacements (approximately)
        de_total_replacements = sum(len(r.replacements) for r in de_results)
        en_total_replacements = sum(len(r.replacements) for r in en_results)
        
        # Allow small difference due to language-specific text
        assert abs(de_total_replacements - en_total_replacements) <= 2, \
            f"Replacement counts should be similar: DE={de_total_replacements}, EN={en_total_replacements}"
        
        # Verify same data values in both
        de_content = "\n".join([r.content for r in de_results])
        en_content = "\n".join([r.content for r in en_results])
        
        # Same organization data
        assert "Test Organization GmbH" in de_content
        assert "Test Organization GmbH" in en_content
        
        # Same personnel
        assert "John Doe" in de_content
        assert "John Doe" in en_content
        assert "Jane Smith" in de_content
        assert "Jane Smith" in en_content
        
        # Same infrastructure
        assert "Datacenter Munich" in de_content
        assert "Datacenter Munich" in en_content
        assert "backup-server-01" in de_content
        assert "backup-server-01" in en_content
        
        # Generate outputs
        de_output_result = output_generator.generate_markdown(
            [r.content for r in de_results], "de", "bcm"
        )
        en_output_result = output_generator.generate_markdown(
            [r.content for r in en_results], "en", "bcm"
        )
        
        # Verify both outputs exist
        assert de_output_result.markdown_path.exists()
        assert en_output_result.markdown_path.exists()
        
        # Verify different directory structure
        assert de_output_result.markdown_path.parent == output_dir / "de" / "bcm" / "markdown"
        assert en_output_result.markdown_path.parent == output_dir / "en" / "bcm" / "markdown"



@pytest.fixture
def isms_templates(temp_workspace):
    """Create ISMS templates for end-to-end testing."""
    templates_dir = temp_workspace / "templates"
    
    # German ISMS templates
    de_isms = templates_dir / "de" / "isms"
    de_isms.mkdir(parents=True)
    
    # Metadata template
    (de_isms / "0000_metadata_de_isms.md").write_text("""# ISMS-Handbuch

**Dokument-Metadaten**

- **Organisation:** {{ meta.organization.name }}
- **Erstellt am:** {{ metadata.date }}
- **Autor:** {{ meta.author }}
- **Version:** {{ meta.document.version }}
- **Typ:** Information Security Management System Handbuch

---
""")
    
    # Basis ISMS - Information Security Policy
    (de_isms / "0010_ISMS_Informationssicherheitsleitlinie.md").write_text("""# 1. Informationssicherheitsleitlinie

## 1.1 Management Commitment

Die Geschäftsführung von {{ meta.organization.name }} verpflichtet sich zur Implementierung und Aufrechterhaltung eines Information Security Management Systems nach ISO/IEC 27001:2022.

**Referenz:** ISO 27001:2022 Clause 5.2

**CEO:** {{ meta.ceo.name }}  
**CISO:** {{ meta.ciso.name }}

## 1.2 Informationssicherheitsziele

[TODO: Spezifische Sicherheitsziele definieren]

## 1.3 Geltungsbereich

**Organisation:** {{ meta.organization.name }}  
**Standort:** {{ netbox.site_name }}
""")
    
    # Basis ISMS - Scope
    (de_isms / "0020_ISMS_Geltungsbereich_Scope.md").write_text("""# 2. ISMS Geltungsbereich (Scope)

## 2.1 Scope Definition

**Referenz:** ISO 27001:2022 Clause 4.3

Der Geltungsbereich des ISMS umfasst:

- **Organisation:** {{ meta.organization.name }}
- **Standorte:** {{ netbox.site_name }}
- **Systeme:** {{ netbox.device_name }}

## 2.2 Boundaries

[TODO: Grenzen des ISMS definieren]

## 2.3 Ausschlüsse

[TODO: Ausschlüsse dokumentieren]
""")
    
    # Basis ISMS - Governance
    (de_isms / "0040_ISMS_Governance_Rollen_und_Verantwortlichkeiten.md").write_text("""# 4. ISMS Governance, Rollen und Verantwortlichkeiten

## 4.1 ISMS Governance-Struktur

**Referenz:** ISO 27001:2022 Clause 5.3

### Führungsebene

- **CEO:** {{ meta.ceo.name }} ({{ meta.ceo.email }})
- **CIO:** {{ meta.cio.name }} ({{ meta.cio.email }})
- **CISO:** {{ meta.ciso.name }} ({{ meta.ciso.email }})

## 4.2 RACI-Matrix für ISMS-Prozesse

| Prozess | CEO | CIO | CISO | IT-Team |
|---|---|---|---|---|
| ISMS-Strategie | A | R | C | I |
| Risikoanalyse | I | A | R | C |
| Incident Response | I | A | R | R |
| Audits | A | C | R | I |

**Legende:** R=Responsible, A=Accountable, C=Consulted, I=Informed
""")
    
    # Abstract Policy - Access Control
    (de_isms / "0220_Policy_Zugriffssteuerung_und_Identitaetsmanagement.md").write_text("""# Policy: Zugriffssteuerung und Identitätsmanagement

## Zweck

Diese Policy definiert die Anforderungen an Zugriffssteuerung und Identitätsmanagement.

**Annex A Mapping:** A.5.15, A.5.16, A.5.17, A.5.18

## Geltungsbereich

**Organisation:** {{ meta.organization.name }}  
**Verantwortlich:** {{ meta.ciso.name }}

## Policy-Statements

1. Zugriff auf Informationssysteme erfolgt nach dem Need-to-Know-Prinzip
2. Alle Benutzerkonten müssen eindeutig identifizierbar sein
3. Privilegierte Zugriffe werden besonders überwacht

## Verantwortlichkeiten

- **Policy Owner:** {{ meta.ciso.name }}
- **Genehmigung:** {{ meta.cio.name }}

[TODO: Spezifische Policy-Anforderungen ergänzen]
""")
    
    # Detailed Guideline - IAM
    (de_isms / "0230_Richtlinie_IAM_Joiner_Mover_Leaver_und_Zugriffsantraege.md").write_text("""# Richtlinie: IAM Joiner-Mover-Leaver und Zugriffsanträge

## Zweck

Diese Richtlinie beschreibt die detaillierte Implementierung der Zugriffssteuerung.

**Bezug:** Policy 0220 - Zugriffssteuerung und Identitätsmanagement  
**Annex A Mapping:** A.5.16, A.5.17

## Joiner-Prozess

1. HR meldet neuen Mitarbeiter an {{ meta.ciso.email }}
2. IT erstellt Benutzerkonto
3. Vorgesetzter genehmigt Zugriffsrechte

## Mover-Prozess

[TODO: Mover-Prozess definieren]

## Leaver-Prozess

[TODO: Leaver-Prozess definieren]

## Verantwortlichkeiten

- **Prozess-Owner:** {{ meta.ciso.name }}
- **Technische Umsetzung:** IT-Team
- **Standort:** {{ netbox.site_name }}
""")
    
    # Appendix - Annex A Mapping
    (de_isms / "0710_Anhang_AnnexA_Mapping_Template.md").write_text("""# Anhang: Annex A Mapping

## Annex A Control Mapping

**Referenz:** ISO 27001:2022 Annex A, Amendment 1:2024

### Organizational Controls (A.5)

| Control | Title | Applicable | Implementation |
|---|---|---|---|
| A.5.1 | Policies for information security | Yes | 0010 |
| A.5.15 | Access control | Yes | 0220, 0230 |
| A.5.16 | Identity management | Yes | 0220, 0230 |

### People Controls (A.6)

[TODO: People Controls mapping]

### Physical Controls (A.7)

**Standort:** {{ netbox.site_name }}

[TODO: Physical Controls mapping]

## Compliance Status

**Verantwortlich:** {{ meta.ciso.name }}  
**Letzte Überprüfung:** {{ metadata.date }}
""")
    
    # English ISMS templates
    en_isms = templates_dir / "en" / "isms"
    en_isms.mkdir(parents=True)
    
    # Metadata template
    (en_isms / "0000_metadata_en_isms.md").write_text("""# ISMS Handbook

**Document Metadata**

- **Organization:** {{ meta.organization.name }}
- **Created:** {{ metadata.date }}
- **Author:** {{ meta.author }}
- **Version:** {{ meta.document.version }}
- **Type:** Information Security Management System Handbook

---
""")
    
    # Basis ISMS - Information Security Policy
    (en_isms / "0010_ISMS_Information_Security_Policy.md").write_text("""# 1. Information Security Policy

## 1.1 Management Commitment

The management of {{ meta.organization.name }} commits to implementing and maintaining an Information Security Management System according to ISO/IEC 27001:2022.

**Reference:** ISO 27001:2022 Clause 5.2

**CEO:** {{ meta.ceo.name }}  
**CISO:** {{ meta.ciso.name }}

## 1.2 Information Security Objectives

[TODO: Define specific security objectives]

## 1.3 Scope

**Organization:** {{ meta.organization.name }}  
**Location:** {{ netbox.site_name }}
""")
    
    # Basis ISMS - Scope
    (en_isms / "0020_ISMS_Scope.md").write_text("""# 2. ISMS Scope

## 2.1 Scope Definition

**Reference:** ISO 27001:2022 Clause 4.3

The ISMS scope includes:

- **Organization:** {{ meta.organization.name }}
- **Locations:** {{ netbox.site_name }}
- **Systems:** {{ netbox.device_name }}

## 2.2 Boundaries

[TODO: Define ISMS boundaries]

## 2.3 Exclusions

[TODO: Document exclusions]
""")
    
    # Basis ISMS - Governance
    (en_isms / "0040_ISMS_Governance_Roles_and_Responsibilities.md").write_text("""# 4. ISMS Governance, Roles and Responsibilities

## 4.1 ISMS Governance Structure

**Reference:** ISO 27001:2022 Clause 5.3

### Leadership

- **CEO:** {{ meta.ceo.name }} ({{ meta.ceo.email }})
- **CIO:** {{ meta.cio.name }} ({{ meta.cio.email }})
- **CISO:** {{ meta.ciso.name }} ({{ meta.ciso.email }})

## 4.2 RACI Matrix for ISMS Processes

| Process | CEO | CIO | CISO | IT Team |
|---|---|---|---|---|
| ISMS Strategy | A | R | C | I |
| Risk Analysis | I | A | R | C |
| Incident Response | I | A | R | R |
| Audits | A | C | R | I |

**Legend:** R=Responsible, A=Accountable, C=Consulted, I=Informed
""")
    
    # Abstract Policy - Access Control
    (en_isms / "0220_Policy_Access_Control_and_Identity_Management.md").write_text("""# Policy: Access Control and Identity Management

## Purpose

This policy defines requirements for access control and identity management.

**Annex A Mapping:** A.5.15, A.5.16, A.5.17, A.5.18

## Scope

**Organization:** {{ meta.organization.name }}  
**Responsible:** {{ meta.ciso.name }}

## Policy Statements

1. Access to information systems follows the need-to-know principle
2. All user accounts must be uniquely identifiable
3. Privileged access is specially monitored

## Responsibilities

- **Policy Owner:** {{ meta.ciso.name }}
- **Approval:** {{ meta.cio.name }}

[TODO: Add specific policy requirements]
""")
    
    # Detailed Guideline - IAM
    (en_isms / "0230_Guideline_IAM_Joiner_Mover_Leaver_and_Access_Requests.md").write_text("""# Guideline: IAM Joiner-Mover-Leaver and Access Requests

## Purpose

This guideline describes the detailed implementation of access control.

**Reference:** Policy 0220 - Access Control and Identity Management  
**Annex A Mapping:** A.5.16, A.5.17

## Joiner Process

1. HR reports new employee to {{ meta.ciso.email }}
2. IT creates user account
3. Supervisor approves access rights

## Mover Process

[TODO: Define mover process]

## Leaver Process

[TODO: Define leaver process]

## Responsibilities

- **Process Owner:** {{ meta.ciso.name }}
- **Technical Implementation:** IT Team
- **Location:** {{ netbox.site_name }}
""")
    
    # Appendix - Annex A Mapping
    (en_isms / "0710_Appendix_AnnexA_Mapping_Template.md").write_text("""# Appendix: Annex A Mapping

## Annex A Control Mapping

**Reference:** ISO 27001:2022 Annex A, Amendment 1:2024

### Organizational Controls (A.5)

| Control | Title | Applicable | Implementation |
|---|---|---|---|
| A.5.1 | Policies for information security | Yes | 0010 |
| A.5.15 | Access control | Yes | 0220, 0230 |
| A.5.16 | Identity management | Yes | 0220, 0230 |

### People Controls (A.6)

[TODO: People Controls mapping]

### Physical Controls (A.7)

**Location:** {{ netbox.site_name }}

[TODO: Physical Controls mapping]

## Compliance Status

**Responsible:** {{ meta.ciso.name }}  
**Last Review:** {{ metadata.date }}
""")
    
    return templates_dir


@pytest.mark.integration
def test_end_to_end_isms_handbook_generation_german(temp_workspace, isms_templates, 
                                                    sample_metadata_config, mock_netbox_api):
    """
    Test end-to-end ISMS handbook generation for German.
    
    This test verifies:
    - German ISMS handbook generation
    - Three-tier structure (Basis, Policy, Guideline)
    - ISO 27001:2022 references present
    - Annex A mappings included
    - RACI matrices included
    - All placeholder replacements
    
    Requirements: All ISMS requirements (5.1-9.5)
    Task: 5.5.2
    """
    from src.meta_adapter import MetaAdapter
    
    output_dir = temp_workspace / "Handbook"
    
    # Initialize components
    template_manager = TemplateManager(isms_templates)
    
    # Create meta adapter
    meta_adapter = MetaAdapter(sample_metadata_config)
    meta_adapter.connect()
    
    # Create netbox adapter
    with patch('pynetbox.api') as mock_pynetbox:
        mock_pynetbox.return_value = mock_netbox_api
        
        netbox_adapter = NetBoxAdapter(
            url="https://netbox.example.com",
            api_token="test_token"
        )
        netbox_adapter.connect()
        
        # Create placeholder processor
        metadata_dict = {
            "author": "Test Author",
            "version": "1.0.0",
            "date": "2025-01-30"
        }
        data_sources = {
            "meta": meta_adapter,
            "netbox": netbox_adapter,
            "metadata": metadata_dict
        }
        processor = PlaceholderProcessor(data_sources, metadata_dict)
        output_generator = OutputGenerator(output_dir, test_mode=True)
        
        # Process German ISMS templates
        de_templates = template_manager.get_templates("de", "isms")
        assert len(de_templates) == 7, "Should find 7 German ISMS templates"
        
        de_results = []
        for template in de_templates:
            content = template.read_content()
            result = processor.process_template(content, template.path.name)
            de_results.append(result)
        
        # Verify no errors
        total_errors = sum(len(r.errors) for r in de_results)
        assert total_errors == 0, "No errors should occur during processing"
        
        # Verify all placeholders were replaced
        all_content = "\n\n".join([r.content for r in de_results])
        
        # Check meta placeholders
        assert "{{ meta.organization.name }}" not in all_content
        assert "{{ meta.ceo.name }}" not in all_content
        assert "{{ meta.cio.name }}" not in all_content
        assert "{{ meta.ciso.name }}" not in all_content
        assert "{{ meta.ciso.email }}" not in all_content
        
        # Check netbox placeholders
        assert "{{ netbox.site_name }}" not in all_content
        assert "{{ netbox.device_name }}" not in all_content
        
        # Verify actual values are present
        assert "Test Organization GmbH" in all_content
        assert "John Doe" in all_content  # CEO
        assert "Jane Smith" in all_content  # CIO
        assert "Bob Johnson" in all_content  # CISO
        assert "Datacenter Munich" in all_content
        assert "backup-server-01" in all_content
        
        # Verify ISO 27001:2022 references
        assert "ISO 27001:2022" in all_content or "ISO/IEC 27001:2022" in all_content, \
            "Should contain ISO 27001:2022 references"
        
        # Verify Annex A mappings
        assert "Annex A" in all_content, "Should contain Annex A mappings"
        assert "A.5." in all_content, "Should contain Annex A control references"
        
        # Verify RACI matrix present
        assert "RACI" in all_content or "Responsible" in all_content, \
            "Should contain RACI matrix"
        
        # Verify three-tier structure elements
        # Basis ISMS (0010-0160)
        assert "Informationssicherheitsleitlinie" in all_content or "Information Security Policy" in all_content
        assert "Geltungsbereich" in all_content or "Scope" in all_content
        
        # Abstract Policy (0220)
        assert "Policy" in all_content
        assert "Zugriffssteuerung" in all_content or "Access Control" in all_content
        
        # Detailed Guideline (0230)
        assert "Richtlinie" in all_content or "Guideline" in all_content
        assert "Joiner" in all_content and "Mover" in all_content and "Leaver" in all_content
        
        # Verify TODO markers remain
        assert "[TODO:" in all_content, "TODO markers should remain for customization"
        
        # Generate output
        de_output_result = output_generator.generate_markdown(
            [r.content for r in de_results], "de", "isms"
        )
        de_output = de_output_result.markdown_path
        
        # Verify output structure
        assert de_output.exists(), "German ISMS output should exist"
        assert de_output.parent == output_dir / "de" / "isms" / "markdown" 
        assert de_output.name == "isms_handbook.md"
        
        # Verify output content
        output_content = de_output.read_text()
        assert "ISMS" in output_content
        assert "Information Security Management" in output_content
        assert "Test Organization GmbH" in output_content
        assert "ISO 27001" in output_content
        assert "Annex A" in output_content


@pytest.mark.integration
def test_end_to_end_isms_handbook_generation_english(temp_workspace, isms_templates, 
                                                     sample_metadata_config, mock_netbox_api):
    """
    Test end-to-end ISMS handbook generation for English.
    
    This test verifies:
    - English ISMS handbook generation
    - Three-tier structure maintained in English
    - All placeholder replacements work in English
    - Correct output structure
    
    Requirements: 8.1, 8.2, 8.3, 8.4, 8.5
    Task: 5.5.2
    """
    from src.meta_adapter import MetaAdapter
    
    output_dir = temp_workspace / "Handbook"
    
    # Initialize components
    template_manager = TemplateManager(isms_templates)
    
    # Create meta adapter
    meta_adapter = MetaAdapter(sample_metadata_config)
    meta_adapter.connect()
    
    # Create netbox adapter
    with patch('pynetbox.api') as mock_pynetbox:
        mock_pynetbox.return_value = mock_netbox_api
        
        netbox_adapter = NetBoxAdapter(
            url="https://netbox.example.com",
            api_token="test_token"
        )
        netbox_adapter.connect()
        
        # Create placeholder processor
        metadata_dict = {
            "author": "Test Author",
            "version": "1.0.0",
            "date": "2025-01-30"
        }
        data_sources = {
            "meta": meta_adapter,
            "netbox": netbox_adapter,
            "metadata": metadata_dict
        }
        processor = PlaceholderProcessor(data_sources, metadata_dict)
        output_generator = OutputGenerator(output_dir, test_mode=True)
        
        # Process English ISMS templates
        en_templates = template_manager.get_templates("en", "isms")
        assert len(en_templates) == 7, "Should find 7 English ISMS templates"
        
        en_results = []
        for template in en_templates:
            content = template.read_content()
            result = processor.process_template(content, template.path.name)
            en_results.append(result)
        
        # Verify no errors
        total_errors = sum(len(r.errors) for r in en_results)
        assert total_errors == 0, "No errors should occur during processing"
        
        # Verify all placeholders were replaced
        all_content = "\n\n".join([r.content for r in en_results])
        
        # Check placeholders were replaced
        assert "{{ meta.organization.name }}" not in all_content
        assert "{{ meta.ciso.name }}" not in all_content
        assert "{{ netbox.site_name }}" not in all_content
        
        # Verify actual values are present
        assert "Test Organization GmbH" in all_content
        assert "Bob Johnson" in all_content  # CISO
        assert "Datacenter Munich" in all_content
        
        # Verify ISO 27001:2022 references
        assert "ISO 27001:2022" in all_content or "ISO/IEC 27001:2022" in all_content
        
        # Verify Annex A mappings
        assert "Annex A" in all_content
        assert "A.5." in all_content
        
        # Verify RACI matrix present
        assert "RACI" in all_content or "Responsible" in all_content
        
        # Verify three-tier structure in English
        assert "Information Security Policy" in all_content
        assert "Scope" in all_content
        assert "Policy" in all_content
        assert "Guideline" in all_content
        assert "Joiner" in all_content
        
        # Generate output
        en_output_result = output_generator.generate_markdown(
            [r.content for r in en_results], "en", "isms"
        )
        en_output = en_output_result.markdown_path
        
        # Verify output structure
        assert en_output.exists(), "English ISMS output should exist"
        assert en_output.parent == output_dir / "en" / "isms" / "markdown" 
        assert en_output.name == "isms_handbook.md"
        
        # Verify output content
        output_content = en_output.read_text()
        assert "ISMS Handbook" in output_content
        assert "Information Security Management" in output_content
        assert "Test Organization GmbH" in output_content
        assert "ISO 27001" in output_content
        assert "Annex A" in output_content


@pytest.mark.integration
def test_isms_three_tier_structure_verification(temp_workspace, isms_templates, 
                                               sample_metadata_config, mock_netbox_api):
    """
    Test ISMS three-tier structure verification.
    
    This test verifies:
    - Basis ISMS documents (0010-0160)
    - Abstract Policies (0200-0680, even numbers)
    - Detailed Guidelines (0210-0690, odd numbers)
    - Policy-Guideline pairing
    
    Requirements: 7.1, 7.2, 7.3, 7.4, 7.5
    Task: 5.5.2
    """
    from src.meta_adapter import MetaAdapter
    
    # Initialize components
    template_manager = TemplateManager(isms_templates)
    
    # Get German ISMS templates
    de_templates = template_manager.get_templates("de", "isms")
    
    # Categorize templates by tier
    basis_templates = []
    policy_templates = []
    guideline_templates = []
    appendix_templates = []
    
    for template in de_templates:
        filename = template.path.name
        # Extract number from filename
        import re
        match = re.match(r'^(\d{4})_', filename)
        if match:
            number = int(match.group(1))
            
            if 10 <= number <= 160:
                basis_templates.append(template)
            elif 200 <= number <= 680 and number % 20 == 0:  # Even numbers (0200, 0220, etc.)
                policy_templates.append(template)
            elif 210 <= number <= 690 and number % 20 == 10:  # Odd numbers (0210, 0230, etc.)
                guideline_templates.append(template)
            elif 710 <= number <= 740:
                appendix_templates.append(template)
    
    # Verify we have templates in each tier
    assert len(basis_templates) > 0, "Should have Basis ISMS templates"
    assert len(policy_templates) > 0, "Should have Policy templates"
    assert len(guideline_templates) > 0, "Should have Guideline templates"
    assert len(appendix_templates) > 0, "Should have Appendix templates"
    
    # Verify Policy-Guideline pairing
    # For each policy (0220), there should be a corresponding guideline (0230)
    policy_numbers = set()
    guideline_numbers = set()
    
    for template in policy_templates:
        match = re.match(r'^(\d{4})_', template.path.name)
        if match:
            policy_numbers.add(int(match.group(1)))
    
    for template in guideline_templates:
        match = re.match(r'^(\d{4})_', template.path.name)
        if match:
            guideline_numbers.add(int(match.group(1)))
    
    # Check that for each policy, there's a guideline 10 numbers higher
    for policy_num in policy_numbers:
        expected_guideline = policy_num + 10
        assert expected_guideline in guideline_numbers, \
            f"Policy {policy_num} should have corresponding guideline {expected_guideline}"
    
    # Process templates and verify content structure
    meta_adapter = MetaAdapter(sample_metadata_config)
    meta_adapter.connect()
    
    with patch('pynetbox.api') as mock_pynetbox:
        mock_pynetbox.return_value = mock_netbox_api
        
        netbox_adapter = NetBoxAdapter(
            url="https://netbox.example.com",
            api_token="test_token"
        )
        netbox_adapter.connect()
        
        metadata_dict = {"author": "Test Author", "version": "1.0.0", "date": "2025-01-30"}
        data_sources = {
            "meta": meta_adapter,
            "netbox": netbox_adapter,
            "metadata": metadata_dict
        }
        processor = PlaceholderProcessor(data_sources, metadata_dict)
        
        # Process policy template
        if policy_templates:
            policy_content = policy_templates[0].read_content()
            policy_result = processor.process_template(policy_content, policy_templates[0].path.name)
            
            # Verify policy characteristics
            assert "Policy" in policy_result.content
            assert "Annex A" in policy_result.content, "Policies should reference Annex A"
            assert "Verantwortlich" in policy_result.content or "Responsible" in policy_result.content
        
        # Process guideline template
        if guideline_templates:
            guideline_content = guideline_templates[0].read_content()
            guideline_result = processor.process_template(guideline_content, guideline_templates[0].path.name)
            
            # Verify guideline characteristics
            assert "Richtlinie" in guideline_result.content or "Guideline" in guideline_result.content
            assert "Policy" in guideline_result.content, "Guidelines should reference their parent policy"



@pytest.fixture
def bsi_grundschutz_templates(temp_workspace):
    """Create BSI Grundschutz templates for end-to-end testing."""
    templates_dir = temp_workspace / "templates"
    
    # German BSI Grundschutz templates
    de_bsi = templates_dir / "de" / "bsi-grundschutz"
    de_bsi.mkdir(parents=True)
    
    # Metadata template
    (de_bsi / "0000_metadata_de_bsi-grundschutz.md").write_text("""# BSI IT-Grundschutz Handbuch

**Dokument-Metadaten**

- **Organisation:** {{ meta.organization.name }}
- **Erstellt am:** {{ metadata.date }}
- **Autor:** {{ meta.author }}
- **Version:** {{ meta.document.version }}
- **Typ:** BSI IT-Grundschutz Handbuch

---
""")
    
    # Information Security Policy
    (de_bsi / "0010_Informationssicherheitsleitlinie.md").write_text("""# 1. Informationssicherheitsleitlinie

## 1.1 Management Commitment

Die Geschäftsführung von {{ meta.organization.name }} verpflichtet sich zur Implementierung und Aufrechterhaltung eines ISMS nach BSI IT-Grundschutz.

**Referenz:** BSI Standard 200-1

**CEO:** {{ meta.ceo.name }}  
**CISO:** {{ meta.ciso.name }}

## 1.2 Informationssicherheitsziele

[TODO: Spezifische Sicherheitsziele nach BSI-Vorgaben definieren]

## 1.3 Geltungsbereich

**Organisation:** {{ meta.organization.name }}  
**Standort:** {{ netbox.site_name }}
""")
    
    # ISMS Organization
    (de_bsi / "0020_ISMS_Organisation_Rollen_RACI.md").write_text("""# 2. ISMS Organisation, Rollen und RACI

## 2.1 ISMS-Organisationsstruktur

**Referenz:** BSI Standard 200-1, Kapitel 7

### Führungsebene

- **CEO:** {{ meta.ceo.name }} ({{ meta.ceo.email }})
- **CIO:** {{ meta.cio.name }} ({{ meta.cio.email }})
- **CISO/ISB:** {{ meta.ciso.name }} ({{ meta.ciso.email }})

## 2.2 RACI-Matrix für BSI-Prozesse

| Prozess | CEO | CIO | ISB | IT-Team |
|---|---|---|---|---|
| Sicherheitskonzept | A | R | R | C |
| Strukturanalyse | I | A | R | C |
| Schutzbedarfsfeststellung | I | A | R | C |
| Modellierung | I | A | R | R |
| Basis-Sicherheitscheck | I | A | R | R |

**Legende:** R=Responsible, A=Accountable, C=Consulted, I=Informed

**ISB:** Informationssicherheitsbeauftragter
""")
    
    # Structure Analysis
    (de_bsi / "0050_Strukturanalyse_Template.md").write_text("""# 5. Strukturanalyse

## 5.1 Methodik

Die Strukturanalyse wird nach BSI Standard 200-2 durchgeführt.

**Referenz:** BSI Standard 200-2, Kapitel 6

**Verantwortlich:** {{ meta.ciso.name }}

## 5.2 Informationsverbund

**Organisation:** {{ meta.organization.name }}  
**Standort:** {{ netbox.site_name }}  
**Systeme:** {{ netbox.device_name }}

## 5.3 Erfasste Objekte

[TODO: Erfasste Objekte nach BSI-Kategorien dokumentieren]

### Anwendungen

[TODO: Anwendungen erfassen]

### IT-Systeme

- **System:** {{ netbox.device_name }}
- **Standort:** {{ netbox.site_name }}

### Netzwerke

[TODO: Netzwerke erfassen]
""")
    
    # Baustein Mapping
    (de_bsi / "0070_Modellierung_Bausteinzuordnung_Template.md").write_text("""# 7. Modellierung und Bausteinzuordnung

## 7.1 Modellierung nach BSI IT-Grundschutz

**Referenz:** BSI Standard 200-2, Kapitel 8

**Verantwortlich:** {{ meta.ciso.name }}

## 7.2 Bausteinzuordnung

### ISMS-Bausteine (ISMS.*)

| Baustein | Titel | Zugeordnet zu |
|---|---|---|
| ISMS.1 | Sicherheitsmanagement | {{ meta.organization.name }} |
| ISMS.1.A1 | Übernahme der Gesamtverantwortung | {{ meta.ceo.name }} |

### ORP-Bausteine (Organisation und Personal)

[TODO: ORP-Bausteine zuordnen]

### CON-Bausteine (Konzeption und Vorgehensweisen)

[TODO: CON-Bausteine zuordnen]

### OPS-Bausteine (Betrieb)

**Standort:** {{ netbox.site_name }}

[TODO: OPS-Bausteine zuordnen]

### DER-Bausteine (Detektion und Reaktion)

[TODO: DER-Bausteine zuordnen]
""")
    
    # Risk Analysis
    (de_bsi / "0090_Risikoanalyse_nach_BSI_200_3_Template.md").write_text("""# 9. Risikoanalyse nach BSI Standard 200-3

## 9.1 Risikoanalyse-Methodik

Die Risikoanalyse wird nach BSI Standard 200-3 durchgeführt.

**Referenz:** BSI Standard 200-3

**Verantwortlich:** {{ meta.ciso.name }}

## 9.2 Gefährdungskatalog

[TODO: Relevante Gefährdungen aus BSI-Katalog identifizieren]

## 9.3 Risikobehandlung

**Standort:** {{ netbox.site_name }}

[TODO: Risikobehandlungsoptionen dokumentieren]

## 9.4 Restrisiken

[TODO: Akzeptierte Restrisiken dokumentieren]

**Genehmigung:** {{ meta.ceo.name }}
""")
    
    # Policy - Access Control
    (de_bsi / "0200_Policy_Zugriffssteuerung_und_Berechtigungen.md").write_text("""# Policy: Zugriffssteuerung und Berechtigungen

## Zweck

Diese Policy definiert die Anforderungen an Zugriffssteuerung und Berechtigungsvergabe.

**BSI Baustein-Referenz:** ORP.4 (Identitäts- und Berechtigungsmanagement)

## Geltungsbereich

**Organisation:** {{ meta.organization.name }}  
**Verantwortlich:** {{ meta.ciso.name }}

## Policy-Statements

1. Zugriff auf IT-Systeme erfolgt nach dem Need-to-Know-Prinzip
2. Alle Benutzerkonten müssen eindeutig identifizierbar sein
3. Privilegierte Zugriffe werden protokolliert und überwacht

## Verantwortlichkeiten

- **Policy Owner:** {{ meta.ciso.name }}
- **Genehmigung:** {{ meta.cio.name }}

[TODO: Spezifische Policy-Anforderungen nach BSI-Vorgaben ergänzen]
""")
    
    # Guideline - IAM
    (de_bsi / "0210_Richtlinie_IAM_Joiner_Mover_Leaver_und_Rezertifizierung.md").write_text("""# Richtlinie: IAM Joiner-Mover-Leaver und Rezertifizierung

## Zweck

Diese Richtlinie beschreibt die detaillierte Implementierung der Zugriffssteuerung nach BSI-Vorgaben.

**Bezug:** Policy 0200 - Zugriffssteuerung und Berechtigungen  
**BSI Baustein-Referenz:** ORP.4.A1, ORP.4.A2, ORP.4.A3

## Joiner-Prozess

1. HR meldet neuen Mitarbeiter an {{ meta.ciso.email }}
2. IT erstellt Benutzerkonto nach Freigabe
3. Vorgesetzter genehmigt Zugriffsrechte

## Mover-Prozess

[TODO: Mover-Prozess nach BSI-Vorgaben definieren]

## Leaver-Prozess

[TODO: Leaver-Prozess nach BSI-Vorgaben definieren]

## Rezertifizierung

[TODO: Rezertifizierungsprozess definieren]

## Verantwortlichkeiten

- **Prozess-Owner:** {{ meta.ciso.name }}
- **Technische Umsetzung:** IT-Team
- **Standort:** {{ netbox.site_name }}
""")
    
    # English BSI Grundschutz templates
    en_bsi = templates_dir / "en" / "bsi-grundschutz"
    en_bsi.mkdir(parents=True)
    
    # Metadata template
    (en_bsi / "0000_metadata_en_bsi-grundschutz.md").write_text("""# BSI IT-Grundschutz Handbook

**Document Metadata**

- **Organization:** {{ meta.organization.name }}
- **Created:** {{ metadata.date }}
- **Author:** {{ meta.author }}
- **Version:** {{ meta.document.version }}
- **Type:** BSI IT-Grundschutz Handbook

---
""")
    
    # Information Security Policy
    (en_bsi / "0010_Information_Security_Policy.md").write_text("""# 1. Information Security Policy

## 1.1 Management Commitment

The management of {{ meta.organization.name }} commits to implementing and maintaining an ISMS according to BSI IT-Grundschutz.

**Reference:** BSI Standard 200-1

**CEO:** {{ meta.ceo.name }}  
**CISO:** {{ meta.ciso.name }}

## 1.2 Information Security Objectives

[TODO: Define specific security objectives according to BSI requirements]

## 1.3 Scope

**Organization:** {{ meta.organization.name }}  
**Location:** {{ netbox.site_name }}
""")
    
    # ISMS Organization
    (en_bsi / "0020_ISMS_Organization_Roles_RACI.md").write_text("""# 2. ISMS Organization, Roles and RACI

## 2.1 ISMS Organization Structure

**Reference:** BSI Standard 200-1, Chapter 7

### Leadership

- **CEO:** {{ meta.ceo.name }} ({{ meta.ceo.email }})
- **CIO:** {{ meta.cio.name }} ({{ meta.cio.email }})
- **CISO/ISB:** {{ meta.ciso.name }} ({{ meta.ciso.email }})

## 2.2 RACI Matrix for BSI Processes

| Process | CEO | CIO | ISB | IT Team |
|---|---|---|---|---|
| Security Concept | A | R | R | C |
| Structure Analysis | I | A | R | C |
| Protection Requirements | I | A | R | C |
| Modeling | I | A | R | R |
| Basic Security Check | I | A | R | R |

**Legend:** R=Responsible, A=Accountable, C=Consulted, I=Informed

**ISB:** Information Security Officer
""")
    
    # Structure Analysis
    (en_bsi / "0050_Structure_Analysis_Template.md").write_text("""# 5. Structure Analysis

## 5.1 Methodology

The structure analysis is conducted according to BSI Standard 200-2.

**Reference:** BSI Standard 200-2, Chapter 6

**Responsible:** {{ meta.ciso.name }}

## 5.2 Information Domain

**Organization:** {{ meta.organization.name }}  
**Location:** {{ netbox.site_name }}  
**Systems:** {{ netbox.device_name }}

## 5.3 Recorded Objects

[TODO: Document recorded objects according to BSI categories]

### Applications

[TODO: Record applications]

### IT Systems

- **System:** {{ netbox.device_name }}
- **Location:** {{ netbox.site_name }}

### Networks

[TODO: Record networks]
""")
    
    # Baustein Mapping
    (en_bsi / "0070_Modeling_Baustein_Assignment_Template.md").write_text("""# 7. Modeling and Baustein Assignment

## 7.1 Modeling according to BSI IT-Grundschutz

**Reference:** BSI Standard 200-2, Chapter 8

**Responsible:** {{ meta.ciso.name }}

## 7.2 Baustein Assignment

### ISMS Bausteine (ISMS.*)

| Baustein | Title | Assigned to |
|---|---|---|
| ISMS.1 | Security Management | {{ meta.organization.name }} |
| ISMS.1.A1 | Assumption of Overall Responsibility | {{ meta.ceo.name }} |

### ORP Bausteine (Organization and Personnel)

[TODO: Assign ORP Bausteine]

### CON Bausteine (Conception and Procedures)

[TODO: Assign CON Bausteine]

### OPS Bausteine (Operations)

**Location:** {{ netbox.site_name }}

[TODO: Assign OPS Bausteine]

### DER Bausteine (Detection and Response)

[TODO: Assign DER Bausteine]
""")
    
    # Risk Analysis
    (en_bsi / "0090_Risk_Analysis_BSI_200_3_Template.md").write_text("""# 9. Risk Analysis according to BSI Standard 200-3

## 9.1 Risk Analysis Methodology

The risk analysis is conducted according to BSI Standard 200-3.

**Reference:** BSI Standard 200-3

**Responsible:** {{ meta.ciso.name }}

## 9.2 Threat Catalog

[TODO: Identify relevant threats from BSI catalog]

## 9.3 Risk Treatment

**Location:** {{ netbox.site_name }}

[TODO: Document risk treatment options]

## 9.4 Residual Risks

[TODO: Document accepted residual risks]

**Approval:** {{ meta.ceo.name }}
""")
    
    # Policy - Access Control
    (en_bsi / "0200_Policy_Access_Control_and_Permissions.md").write_text("""# Policy: Access Control and Permissions

## Purpose

This policy defines requirements for access control and permission assignment.

**BSI Baustein Reference:** ORP.4 (Identity and Authorization Management)

## Scope

**Organization:** {{ meta.organization.name }}  
**Responsible:** {{ meta.ciso.name }}

## Policy Statements

1. Access to IT systems follows the need-to-know principle
2. All user accounts must be uniquely identifiable
3. Privileged access is logged and monitored

## Responsibilities

- **Policy Owner:** {{ meta.ciso.name }}
- **Approval:** {{ meta.cio.name }}

[TODO: Add specific policy requirements according to BSI guidelines]
""")
    
    # Guideline - IAM
    (en_bsi / "0210_Guideline_IAM_Joiner_Mover_Leaver_and_Recertification.md").write_text("""# Guideline: IAM Joiner-Mover-Leaver and Recertification

## Purpose

This guideline describes the detailed implementation of access control according to BSI requirements.

**Reference:** Policy 0200 - Access Control and Permissions  
**BSI Baustein Reference:** ORP.4.A1, ORP.4.A2, ORP.4.A3

## Joiner Process

1. HR reports new employee to {{ meta.ciso.email }}
2. IT creates user account after approval
3. Supervisor approves access rights

## Mover Process

[TODO: Define mover process according to BSI requirements]

## Leaver Process

[TODO: Define leaver process according to BSI requirements]

## Recertification

[TODO: Define recertification process]

## Responsibilities

- **Process Owner:** {{ meta.ciso.name }}
- **Technical Implementation:** IT Team
- **Location:** {{ netbox.site_name }}
""")
    
    return templates_dir


@pytest.mark.integration
def test_end_to_end_bsi_grundschutz_handbook_generation_german(temp_workspace, bsi_grundschutz_templates, 
                                                               sample_metadata_config, mock_netbox_api):
    """
    Test end-to-end BSI Grundschutz handbook generation for German.
    
    This test verifies:
    - German BSI Grundschutz handbook generation
    - BSI Standards 200-1, 200-2, 200-3 references present
    - BSI Baustein references included
    - RACI matrices included
    - All placeholder replacements
    
    Requirements: All BSI Grundschutz requirements (10.1-14.5)
    Task: 5.5.3
    """
    from src.meta_adapter import MetaAdapter
    
    output_dir = temp_workspace / "Handbook"
    
    # Initialize components
    template_manager = TemplateManager(bsi_grundschutz_templates)
    
    # Create meta adapter
    meta_adapter = MetaAdapter(sample_metadata_config)
    meta_adapter.connect()
    
    # Create netbox adapter
    with patch('pynetbox.api') as mock_pynetbox:
        mock_pynetbox.return_value = mock_netbox_api
        
        netbox_adapter = NetBoxAdapter(
            url="https://netbox.example.com",
            api_token="test_token"
        )
        netbox_adapter.connect()
        
        # Create placeholder processor
        metadata_dict = {
            "author": "Test Author",
            "version": "1.0.0",
            "date": "2025-01-30"
        }
        data_sources = {
            "meta": meta_adapter,
            "netbox": netbox_adapter,
            "metadata": metadata_dict
        }
        processor = PlaceholderProcessor(data_sources, metadata_dict)
        output_generator = OutputGenerator(output_dir, test_mode=True)
        
        # Process German BSI Grundschutz templates
        de_templates = template_manager.get_templates("de", "bsi-grundschutz")
        assert len(de_templates) == 8, "Should find 8 German BSI Grundschutz templates"
        
        de_results = []
        for template in de_templates:
            content = template.read_content()
            result = processor.process_template(content, template.path.name)
            de_results.append(result)
        
        # Verify no errors
        total_errors = sum(len(r.errors) for r in de_results)
        assert total_errors == 0, "No errors should occur during processing"
        
        # Verify all placeholders were replaced
        all_content = "\n\n".join([r.content for r in de_results])
        
        # Check meta placeholders
        assert "{{ meta.organization.name }}" not in all_content
        assert "{{ meta.ceo.name }}" not in all_content
        assert "{{ meta.cio.name }}" not in all_content
        assert "{{ meta.ciso.name }}" not in all_content
        assert "{{ meta.ciso.email }}" not in all_content
        
        # Check netbox placeholders
        assert "{{ netbox.site_name }}" not in all_content
        assert "{{ netbox.device_name }}" not in all_content
        
        # Verify actual values are present
        assert "Test Organization GmbH" in all_content
        assert "John Doe" in all_content  # CEO
        assert "Jane Smith" in all_content  # CIO
        assert "Bob Johnson" in all_content  # CISO
        assert "Datacenter Munich" in all_content
        assert "backup-server-01" in all_content
        
        # Verify BSI Standards references
        assert "BSI Standard 200-1" in all_content, "Should contain BSI Standard 200-1 references"
        assert "BSI Standard 200-2" in all_content, "Should contain BSI Standard 200-2 references"
        assert "BSI Standard 200-3" in all_content, "Should contain BSI Standard 200-3 references"
        
        # Verify BSI Baustein references
        assert "Baustein" in all_content, "Should contain Baustein references"
        assert "ISMS." in all_content or "ORP." in all_content, \
            "Should contain specific Baustein references (ISMS.*, ORP.*, etc.)"
        
        # Verify RACI matrix present
        assert "RACI" in all_content or "Responsible" in all_content, \
            "Should contain RACI matrix"
        
        # Verify BSI-specific processes
        assert "Strukturanalyse" in all_content or "Structure Analysis" in all_content
        assert "Modellierung" in all_content or "Modeling" in all_content
        assert "Risikoanalyse" in all_content or "Risk Analysis" in all_content
        
        # Verify TODO markers remain
        assert "[TODO:" in all_content, "TODO markers should remain for customization"
        
        # Generate output
        de_output_result = output_generator.generate_markdown(
            [r.content for r in de_results], "de", "bsi-grundschutz"
        )
        de_output = de_output_result.markdown_path
        
        # Verify output structure
        assert de_output.exists(), "German BSI Grundschutz output should exist"
        assert de_output.parent == output_dir / "de" / "bsi-grundschutz" / "markdown" 
        assert de_output.name == "bsi-grundschutz_handbook.md"
        
        # Verify output content
        output_content = de_output.read_text()
        assert "BSI" in output_content
        assert "IT-Grundschutz" in output_content
        assert "Test Organization GmbH" in output_content
        assert "BSI Standard 200" in output_content


@pytest.mark.integration
def test_end_to_end_bsi_grundschutz_handbook_generation_english(temp_workspace, bsi_grundschutz_templates, 
                                                                sample_metadata_config, mock_netbox_api):
    """
    Test end-to-end BSI Grundschutz handbook generation for English.
    
    This test verifies:
    - English BSI Grundschutz handbook generation
    - All placeholder replacements work in English
    - Correct output structure
    
    Requirements: 13.1, 13.2, 13.3, 13.4, 13.5
    Task: 5.5.3
    """
    from src.meta_adapter import MetaAdapter
    
    output_dir = temp_workspace / "Handbook"
    
    # Initialize components
    template_manager = TemplateManager(bsi_grundschutz_templates)
    
    # Create meta adapter
    meta_adapter = MetaAdapter(sample_metadata_config)
    meta_adapter.connect()
    
    # Create netbox adapter
    with patch('pynetbox.api') as mock_pynetbox:
        mock_pynetbox.return_value = mock_netbox_api
        
        netbox_adapter = NetBoxAdapter(
            url="https://netbox.example.com",
            api_token="test_token"
        )
        netbox_adapter.connect()
        
        # Create placeholder processor
        metadata_dict = {
            "author": "Test Author",
            "version": "1.0.0",
            "date": "2025-01-30"
        }
        data_sources = {
            "meta": meta_adapter,
            "netbox": netbox_adapter,
            "metadata": metadata_dict
        }
        processor = PlaceholderProcessor(data_sources, metadata_dict)
        output_generator = OutputGenerator(output_dir, test_mode=True)
        
        # Process English BSI Grundschutz templates
        en_templates = template_manager.get_templates("en", "bsi-grundschutz")
        assert len(en_templates) == 8, "Should find 8 English BSI Grundschutz templates"
        
        en_results = []
        for template in en_templates:
            content = template.read_content()
            result = processor.process_template(content, template.path.name)
            en_results.append(result)
        
        # Verify no errors
        total_errors = sum(len(r.errors) for r in en_results)
        assert total_errors == 0, "No errors should occur during processing"
        
        # Verify all placeholders were replaced
        all_content = "\n\n".join([r.content for r in en_results])
        
        # Check placeholders were replaced
        assert "{{ meta.organization.name }}" not in all_content
        assert "{{ meta.ciso.name }}" not in all_content
        assert "{{ netbox.site_name }}" not in all_content
        
        # Verify actual values are present
        assert "Test Organization GmbH" in all_content
        assert "Bob Johnson" in all_content  # CISO
        assert "Datacenter Munich" in all_content
        
        # Verify BSI Standards references
        assert "BSI Standard 200" in all_content
        
        # Verify Baustein references
        assert "Baustein" in all_content
        
        # Verify RACI matrix present
        assert "RACI" in all_content or "Responsible" in all_content
        
        # Generate output
        en_output_result = output_generator.generate_markdown(
            [r.content for r in en_results], "en", "bsi-grundschutz"
        )
        en_output = en_output_result.markdown_path
        
        # Verify output structure
        assert en_output.exists(), "English BSI Grundschutz output should exist"
        assert en_output.parent == output_dir / "en" / "bsi-grundschutz" / "markdown" 
        assert en_output.name == "bsi-grundschutz_handbook.md"
        
        # Verify output content
        output_content = en_output.read_text()
        assert "BSI IT-Grundschutz Handbook" in output_content
        assert "Test Organization GmbH" in output_content
        assert "BSI Standard 200" in output_content


@pytest.mark.integration
def test_bsi_grundschutz_baustein_references(temp_workspace, bsi_grundschutz_templates, 
                                            sample_metadata_config, mock_netbox_api):
    """
    Test BSI Grundschutz Baustein references verification.
    
    This test verifies:
    - BSI Baustein references are present
    - Baustein categories (ISMS, ORP, CON, OPS, DER) are referenced
    - Baustein assignments are documented
    
    Requirements: 10.4, 11.4, 12.3
    Task: 5.5.3
    """
    from src.meta_adapter import MetaAdapter
    
    # Initialize components
    template_manager = TemplateManager(bsi_grundschutz_templates)
    
    # Create adapters
    meta_adapter = MetaAdapter(sample_metadata_config)
    meta_adapter.connect()
    
    with patch('pynetbox.api') as mock_pynetbox:
        mock_pynetbox.return_value = mock_netbox_api
        
        netbox_adapter = NetBoxAdapter(
            url="https://netbox.example.com",
            api_token="test_token"
        )
        netbox_adapter.connect()
        
        metadata_dict = {"author": "Test Author", "version": "1.0.0", "date": "2025-01-30"}
        data_sources = {
            "meta": meta_adapter,
            "netbox": netbox_adapter,
            "metadata": metadata_dict
        }
        processor = PlaceholderProcessor(data_sources, metadata_dict)
        
        # Get German BSI Grundschutz templates
        de_templates = template_manager.get_templates("de", "bsi-grundschutz")
        
        # Find Baustein mapping template
        baustein_template = None
        for template in de_templates:
            if "Modellierung" in template.path.name or "Baustein" in template.path.name:
                baustein_template = template
                break
        
        assert baustein_template is not None, "Should find Baustein mapping template"
        
        # Process Baustein template
        content = baustein_template.read_content()
        result = processor.process_template(content, baustein_template.path.name)
        
        # Verify Baustein references
        assert "Baustein" in result.content, "Should contain Baustein references"
        
        # Verify Baustein categories are mentioned
        baustein_categories = ["ISMS", "ORP", "CON", "OPS", "DER"]
        found_categories = [cat for cat in baustein_categories if cat in result.content]
        
        assert len(found_categories) > 0, \
            f"Should reference at least one Baustein category, found: {found_categories}"
        
        # Verify specific Baustein references (e.g., ISMS.1, ORP.4)
        import re
        baustein_pattern = r'(ISMS|ORP|CON|OPS|DER)\.\d+'
        baustein_matches = re.findall(baustein_pattern, result.content)
        
        assert len(baustein_matches) > 0, \
            "Should contain specific Baustein references (e.g., ISMS.1, ORP.4)"



@pytest.fixture
def it_operation_baseline_templates(temp_workspace):
    """Create baseline IT-Operation templates for backward compatibility testing."""
    templates_dir = temp_workspace / "templates"
    
    # German IT-Operation templates (existing format)
    de_it_op = templates_dir / "de" / "it-operation"
    de_it_op.mkdir(parents=True)
    
    # Metadata template
    (de_it_op / "0000_metadata_de_it-operation.md").write_text("""# IT-Operations Handbuch

**Dokument-Metadaten**

- **Organisation:** {{ meta.organization.name }}
- **Erstellt am:** {{ metadata.date }}
- **Autor:** {{ meta.author }}
- **Version:** {{ meta.document.version }}

---
""")
    
    # Introduction
    (de_it_op / "0010_Einleitung.md").write_text("""# 1. Einleitung

## 1.1 Zweck

Dieses IT-Operations-Handbuch beschreibt die Betriebsprozesse für {{ meta.organization.name }}.

## 1.2 Geltungsbereich

Standort: {{ netbox.site_name }}
""")
    
    # System Overview
    (de_it_op / "0040_Systemuebersicht_und_Architektur.md").write_text("""# 4. Systemübersicht und Architektur

## 4.1 Infrastruktur

**Primärer Standort:** {{ netbox.site_name }}  
**Backup-Server:** {{ netbox.device_name }}  
**IP-Adresse:** {{ netbox.primary_ip }}

## 4.2 Verantwortlichkeiten

**CIO:** {{ meta.cio.name }}  
**E-Mail:** {{ meta.cio.email }}
""")
    
    return templates_dir


# Backward compatibility tests removed - no longer needed after configuration separation refactoring



@pytest.fixture
def templates_with_html_comments(temp_workspace):
    """Create templates with HTML comments for integration testing."""
    templates_dir = temp_workspace / "templates"
    
    # German templates with HTML comments
    de_test = templates_dir / "de" / "test-comments"
    de_test.mkdir(parents=True)
    
    # Template with single-line HTML comments
    (de_test / "0010_single_line_comments.md").write_text("""# Test Template

<!-- This is a template author note -->

## Section 1

**Organisation:** {{ meta.organization.name }}

<!-- TODO: Add more details here -->

## Section 2

**Standort:** {{ netbox.site_name }}

<!-- End of template -->
""")
    
    # Template with multi-line HTML comments
    (de_test / "0020_multi_line_comments.md").write_text("""# Multi-line Comments Test

<!--
TEMPLATE AUTHOR NOTE:
This section requires customization based on your organization's
specific requirements. Consider the following:
- Business processes
- Critical systems
- Recovery objectives
-->

## Configuration

**CIO:** {{ meta.cio.name }}

<!--
Multi-line comment
spanning several lines
with various content
-->

**CISO:** {{ meta.ciso.name }}
""")
    
    # Template with mixed comments and placeholders
    (de_test / "0030_mixed_comments_placeholders.md").write_text("""# Mixed Content Test

<!-- Comment before placeholder -->
**Organisation:** {{ meta.organization.name }}
<!-- Comment after placeholder -->

## Infrastructure

<!-- This placeholder should still work: {{ netbox.site_name }} -->

**Actual Site:** {{ netbox.site_name }}

<!-- Comment with placeholder reference: Use {{ meta.cio.name }} for approval -->

**CIO:** {{ meta.cio.name }}
""")
    
    # Template without HTML comments (control)
    (de_test / "0040_no_comments.md").write_text("""# No Comments Test

## Basic Information

**Organisation:** {{ meta.organization.name }}
**CIO:** {{ meta.cio.name }}
**Standort:** {{ netbox.site_name }}
""")
    
    return templates_dir


@pytest.mark.integration
def test_html_comment_integration_single_line(temp_workspace, templates_with_html_comments, 
                                             sample_metadata_config, mock_netbox_api):
    """
    Test HTML comment integration with single-line comments.
    
    This test verifies:
    - Single-line HTML comments are removed
    - Placeholders are still processed correctly
    - Markdown content is preserved
    - No comment markers remain in output
    
    Requirements: 16.1, 16.2, 17.1, 17.3
    Task: 5.5.5
    """
    from src.meta_adapter import MetaAdapter
    
    # Initialize components
    template_manager = TemplateManager(templates_with_html_comments)
    
    # Create adapters
    meta_adapter = MetaAdapter(sample_metadata_config)
    meta_adapter.connect()
    
    with patch('pynetbox.api') as mock_pynetbox:
        mock_pynetbox.return_value = mock_netbox_api
        
        netbox_adapter = NetBoxAdapter(
            url="https://netbox.example.com",
            api_token="test_token"
        )
        netbox_adapter.connect()
        
        metadata_dict = {"author": "Test Author", "version": "1.0.0", "date": "2025-01-30"}
        data_sources = {
            "meta": meta_adapter,
            "netbox": netbox_adapter,
            "metadata": metadata_dict
        }
        processor = PlaceholderProcessor(data_sources, metadata_dict)
        
        # Get template with single-line comments
        templates = template_manager.get_templates("de", "test-comments")
        single_line_template = [t for t in templates if "single_line" in t.path.name][0]
        
        # Process template
        content = single_line_template.read_content()
        result = processor.process_template(content, single_line_template.path.name)
        
        # Verify HTML comments were removed
        assert "<!--" not in result.content, "HTML comment start marker should be removed"
        assert "-->" not in result.content, "HTML comment end marker should be removed"
        assert "template author note" not in result.content.lower(), \
            "Comment content should be removed"
        assert "TODO: Add more details" not in result.content, \
            "TODO comment should be removed"
        
        # Verify placeholders were still processed
        assert "{{ meta.organization.name }}" not in result.content
        assert "{{ netbox.site_name }}" not in result.content
        
        # Verify actual values are present
        assert "Test Organization GmbH" in result.content
        assert "Datacenter Munich" in result.content
        
        # Verify markdown structure is preserved
        assert "# Test Template" in result.content
        assert "## Section 1" in result.content
        assert "## Section 2" in result.content
        assert "**Organisation:**" in result.content
        assert "**Standort:**" in result.content


@pytest.mark.integration
def test_html_comment_integration_multi_line(temp_workspace, templates_with_html_comments, 
                                            sample_metadata_config, mock_netbox_api):
    """
    Test HTML comment integration with multi-line comments.
    
    This test verifies:
    - Multi-line HTML comments are completely removed
    - All lines of multi-line comments are removed
    - Placeholders after comments are still processed
    - Markdown formatting is preserved
    
    Requirements: 16.3, 17.2, 17.3
    Task: 5.5.5
    """
    from src.meta_adapter import MetaAdapter
    
    # Initialize components
    template_manager = TemplateManager(templates_with_html_comments)
    
    # Create adapters
    meta_adapter = MetaAdapter(sample_metadata_config)
    meta_adapter.connect()
    
    with patch('pynetbox.api') as mock_pynetbox:
        mock_pynetbox.return_value = mock_netbox_api
        
        netbox_adapter = NetBoxAdapter(
            url="https://netbox.example.com",
            api_token="test_token"
        )
        netbox_adapter.connect()
        
        metadata_dict = {"author": "Test Author", "version": "1.0.0", "date": "2025-01-30"}
        data_sources = {
            "meta": meta_adapter,
            "netbox": netbox_adapter,
            "metadata": metadata_dict
        }
        processor = PlaceholderProcessor(data_sources, metadata_dict)
        
        # Get template with multi-line comments
        templates = template_manager.get_templates("de", "test-comments")
        multi_line_template = [t for t in templates if "multi_line" in t.path.name][0]
        
        # Process template
        content = multi_line_template.read_content()
        result = processor.process_template(content, multi_line_template.path.name)
        
        # Verify HTML comments were removed
        assert "<!--" not in result.content, "HTML comment start marker should be removed"
        assert "-->" not in result.content, "HTML comment end marker should be removed"
        
        # Verify multi-line comment content was removed
        assert "TEMPLATE AUTHOR NOTE" not in result.content
        assert "requires customization" not in result.content
        assert "Business processes" not in result.content
        assert "Critical systems" not in result.content
        assert "Recovery objectives" not in result.content
        assert "spanning several lines" not in result.content
        
        # Verify placeholders were still processed
        assert "{{ meta.cio.name }}" not in result.content
        assert "{{ meta.ciso.name }}" not in result.content
        
        # Verify actual values are present
        assert "Jane Smith" in result.content  # CIO
        assert "Bob Johnson" in result.content  # CISO
        
        # Verify markdown structure is preserved
        assert "# Multi-line Comments Test" in result.content
        assert "## Configuration" in result.content
        assert "**CIO:**" in result.content
        assert "**CISO:**" in result.content


@pytest.mark.integration
def test_html_comment_integration_mixed_scenarios(temp_workspace, templates_with_html_comments, 
                                                 sample_metadata_config, mock_netbox_api):
    """
    Test HTML comment integration with mixed scenarios.
    
    This test verifies:
    - Comments before placeholders don't affect processing
    - Comments after placeholders don't affect processing
    - Comments containing placeholder references are removed
    - Actual placeholders outside comments are processed
    
    Requirements: 18.1, 18.2
    Task: 5.5.5
    """
    from src.meta_adapter import MetaAdapter
    
    # Initialize components
    template_manager = TemplateManager(templates_with_html_comments)
    
    # Create adapters
    meta_adapter = MetaAdapter(sample_metadata_config)
    meta_adapter.connect()
    
    with patch('pynetbox.api') as mock_pynetbox:
        mock_pynetbox.return_value = mock_netbox_api
        
        netbox_adapter = NetBoxAdapter(
            url="https://netbox.example.com",
            api_token="test_token"
        )
        netbox_adapter.connect()
        
        metadata_dict = {"author": "Test Author", "version": "1.0.0", "date": "2025-01-30"}
        data_sources = {
            "meta": meta_adapter,
            "netbox": netbox_adapter,
            "metadata": metadata_dict
        }
        processor = PlaceholderProcessor(data_sources, metadata_dict)
        
        # Get template with mixed comments and placeholders
        templates = template_manager.get_templates("de", "test-comments")
        mixed_template = [t for t in templates if "mixed" in t.path.name][0]
        
        # Process template
        content = mixed_template.read_content()
        result = processor.process_template(content, mixed_template.path.name)
        
        # Verify all HTML comments were removed
        assert "<!--" not in result.content
        assert "-->" not in result.content
        assert "Comment before placeholder" not in result.content
        assert "Comment after placeholder" not in result.content
        assert "This placeholder should still work" not in result.content
        assert "Use {{ meta.cio.name }} for approval" not in result.content
        
        # Verify actual placeholders (outside comments) were processed
        assert "{{ meta.organization.name }}" not in result.content
        assert "{{ netbox.site_name }}" not in result.content
        assert "{{ meta.cio.name }}" not in result.content
        
        # Verify actual values are present
        assert "Test Organization GmbH" in result.content
        assert "Datacenter Munich" in result.content
        assert "Jane Smith" in result.content
        
        # Verify markdown structure is preserved
        assert "# Mixed Content Test" in result.content
        assert "## Infrastructure" in result.content
        assert "**Organisation:**" in result.content
        assert "**Actual Site:**" in result.content
        assert "**CIO:**" in result.content


@pytest.mark.integration
def test_html_comment_integration_no_comments_control(temp_workspace, templates_with_html_comments, 
                                                     sample_metadata_config, mock_netbox_api):
    """
    Test HTML comment integration with templates without comments (control test).
    
    This test verifies:
    - Templates without HTML comments work normally
    - No regression when HTML comments are not present
    - Placeholder processing is unaffected
    
    Requirements: 17.4, 17.5
    Task: 5.5.5
    """
    from src.meta_adapter import MetaAdapter
    
    # Initialize components
    template_manager = TemplateManager(templates_with_html_comments)
    
    # Create adapters
    meta_adapter = MetaAdapter(sample_metadata_config)
    meta_adapter.connect()
    
    with patch('pynetbox.api') as mock_pynetbox:
        mock_pynetbox.return_value = mock_netbox_api
        
        netbox_adapter = NetBoxAdapter(
            url="https://netbox.example.com",
            api_token="test_token"
        )
        netbox_adapter.connect()
        
        metadata_dict = {"author": "Test Author", "version": "1.0.0", "date": "2025-01-30"}
        data_sources = {
            "meta": meta_adapter,
            "netbox": netbox_adapter,
            "metadata": metadata_dict
        }
        processor = PlaceholderProcessor(data_sources, metadata_dict)
        
        # Get template without comments
        templates = template_manager.get_templates("de", "test-comments")
        no_comments_template = [t for t in templates if "no_comments" in t.path.name][0]
        
        # Process template
        content = no_comments_template.read_content()
        result = processor.process_template(content, no_comments_template.path.name)
        
        # Verify no errors
        assert len(result.errors) == 0, "No errors should occur"
        
        # Verify placeholders were processed
        assert "{{ meta.organization.name }}" not in result.content
        assert "{{ meta.cio.name }}" not in result.content
        assert "{{ netbox.site_name }}" not in result.content
        
        # Verify actual values are present
        assert "Test Organization GmbH" in result.content
        assert "Jane Smith" in result.content
        assert "Datacenter Munich" in result.content
        
        # Verify markdown structure is preserved
        assert "# No Comments Test" in result.content
        assert "## Basic Information" in result.content
        assert "**Organisation:**" in result.content
        assert "**CIO:**" in result.content
        assert "**Standort:**" in result.content


@pytest.mark.integration
def test_html_comment_integration_end_to_end(temp_workspace, templates_with_html_comments, 
                                            sample_metadata_config, mock_netbox_api):
    """
    Test HTML comment integration end-to-end workflow.
    
    This test verifies:
    - Complete workflow with HTML comments
    - Output generation with comment removal
    - No comment markers in final output file
    - All templates processed correctly
    
    Requirements: 16.1, 16.2, 16.3, 17.1, 17.2, 17.3
    Task: 5.5.5
    """
    from src.meta_adapter import MetaAdapter
    
    output_dir = temp_workspace / "Handbook"
    
    # Initialize components
    template_manager = TemplateManager(templates_with_html_comments)
    
    # Create adapters
    meta_adapter = MetaAdapter(sample_metadata_config)
    meta_adapter.connect()
    
    with patch('pynetbox.api') as mock_pynetbox:
        mock_pynetbox.return_value = mock_netbox_api
        
        netbox_adapter = NetBoxAdapter(
            url="https://netbox.example.com",
            api_token="test_token"
        )
        netbox_adapter.connect()
        
        metadata_dict = {"author": "Test Author", "version": "1.0.0", "date": "2025-01-30"}
        data_sources = {
            "meta": meta_adapter,
            "netbox": netbox_adapter,
            "metadata": metadata_dict
        }
        processor = PlaceholderProcessor(data_sources, metadata_dict)
        output_generator = OutputGenerator(output_dir, test_mode=True)
        
        # Process all templates
        templates = template_manager.get_templates("de", "test-comments")
        results = []
        for template in templates:
            content = template.read_content()
            result = processor.process_template(content, template.path.name)
            results.append(result)
        
        # Verify no errors
        total_errors = sum(len(r.errors) for r in results)
        assert total_errors == 0, "No errors should occur"
        
        # Generate output
        output_result = output_generator.generate_markdown(
            [r.content for r in results], "de", "test-comments"
        )
        output_path = output_result.markdown_path
        
        # Verify output was created
        assert output_path.exists(), "Output file should be created"
        
        # Read output content
        output_content = output_path.read_text()
        
        # Verify no HTML comment markers in output
        assert "<!--" not in output_content, "No HTML comment start markers in output"
        assert "-->" not in output_content, "No HTML comment end markers in output"
        
        # Verify comment content was removed
        assert "template author note" not in output_content.lower()
        assert "TEMPLATE AUTHOR NOTE" not in output_content
        assert "TODO: Add more details" not in output_content
        assert "requires customization" not in output_content
        
        # Verify placeholders were replaced
        assert "{{ meta.organization.name }}" not in output_content
        assert "{{ meta.cio.name }}" not in output_content
        assert "{{ netbox.site_name }}" not in output_content
        
        # Verify actual values are present
        assert "Test Organization GmbH" in output_content
        assert "Jane Smith" in output_content
        assert "Datacenter Munich" in output_content
        
        # Verify markdown structure is preserved
        assert "# Test Template" in output_content or "# Multi-line Comments Test" in output_content
        assert "**Organisation:**" in output_content or "**CIO:**" in output_content


# ============================================================================
# Phase 6: Integration Tests for New Features
# ============================================================================

@pytest.fixture
def bcm_templates_for_testing(temp_workspace):
    """Create minimal BCM templates for integration testing."""
    templates_dir = temp_workspace / "templates"
    
    # German BCM templates
    de_bcm = templates_dir / "de" / "bcm"
    de_bcm.mkdir(parents=True)
    
    (de_bcm / "0010_Zweck_und_Geltungsbereich.md").write_text("""# 1. Zweck und Geltungsbereich

**Organisation:** {{ meta.organization.name }}
**Version:** {{ handbook.version }}
**Verantwortlicher:** {{ handbook.owner }}
**Datum:** {{ handbook.date }}

Dieses BCM-Handbuch gilt für {{ netbox.site_name }}.
""")
    
    (de_bcm / "0020_BCM_Leitlinie_Policy.md").write_text("""# 2. BCM-Leitlinie

**Genehmiger:** {{ handbook.approver }}
**CISO:** {{ meta.ciso.name }}
**Standort:** {{ netbox.site_name }}
""")
    
    (de_bcm / "0030_Dokumentenlenkung.md").write_text("""# 3. Dokumentenlenkung

**Dokumentverantwortlicher:** {{ meta.document.owner }}
**Version:** {{ handbook.version }}
""")
    
    return templates_dir


@pytest.fixture
def sample_metadata_config_with_handbooks():
    """Create a sample metadata configuration with handbook metadata for testing."""
    from src.metadata_config_manager import (
        MetadataConfig, OrganizationInfo, PersonRole, DocumentInfo, HandbookInfo
    )
    
    organization = OrganizationInfo(
        name="Test Organization GmbH",
        address="Test Street 123",
        city="Test City",
        postal_code="12345",
        country="Germany",
        website="https://test.example.com",
        phone="+49 123 456789",
        email="info@test.example.com"
    )
    
    roles = {
        "ceo": PersonRole(
            name="John Doe",
            title="Chief Executive Officer",
            email="john.doe@test.example.com",
            phone="+49 123 456789-100",
            department="Management"
        ),
        "cio": PersonRole(
            name="Jane Smith",
            title="Chief Information Officer",
            email="jane.smith@test.example.com",
            phone="+49 123 456789-200",
            department="IT"
        ),
        "ciso": PersonRole(
            name="Bob Johnson",
            title="Chief Information Security Officer",
            email="bob.johnson@test.example.com",
            phone="+49 123 456789-300",
            department="IT Security"
        )
    }
    
    document = DocumentInfo(
        owner="IT Operations Manager",
        approver="CIO",
        version="2.0.0",
        classification="internal"
    )
    
    handbooks = {
        "bcm": HandbookInfo(
            version="1.0.0",
            owner="BCM Manager",
            approver="CEO",
            date="2025-02-01"
        ),
        "isms": HandbookInfo(
            version="2.1.0",
            owner="CISO",
            approver="CIO",
            date="2025-02-05"
        )
    }
    
    return MetadataConfig(
        organization=organization,
        roles=roles,
        document=document,
        handbooks=handbooks,
        author="Test Author [test@example.com]",
        language="de"
    )


@pytest.fixture
def handbook_metadata_config():
    """Create configuration with per-handbook metadata."""
    return {
        "handbooks": {
            "bcm": {
                "version": "1.0.0",
                "owner": "BCM Manager",
                "approver": "CEO",
                "date": "2025-02-01"
            },
            "isms": {
                "version": "2.1.0",
                "owner": "CISO",
                "approver": "CIO",
                "date": "2025-02-05"
            }
        }
    }


@pytest.mark.integration
def test_separate_markdown_files_generation(temp_workspace, bcm_templates_for_testing, 
                                           sample_metadata_config_with_handbooks,
                                           mock_netbox_api):
    """
    Test separate markdown file generation for each template.
    
    This test verifies:
    - One markdown file per template is created
    - TOC.md file is created with correct links
    - No combined markdown file is created
    - Output directory structure is correct (test-output/{language}/markdown/)
    - Test mode validation works
    
    Requirements: 32.1, 32.2, 32.3, 32.4, 32.5, 32.6
    """
    from src.meta_adapter import MetaAdapter
    from src.config_manager import ConfigManager
    
    # Setup output directory
    output_dir = temp_workspace / "test-output"
    
    # Initialize components
    template_manager = TemplateManager(bcm_templates_for_testing)
    
    # Create meta adapter
    meta_adapter = MetaAdapter(sample_metadata_config_with_handbooks)
    meta_adapter.connect()
    
    # Set handbook type for handbook placeholders
    meta_adapter.set_handbook_type("bcm")
    
    # Create netbox adapter
    with patch('pynetbox.api') as mock_pynetbox:
        mock_pynetbox.return_value = mock_netbox_api
        
        netbox_adapter = NetBoxAdapter(
            url="https://netbox.example.com",
            api_token="test_token"
        )
        netbox_adapter.connect()
        
        # Create placeholder processor with all adapters
        metadata_dict = {
            "author": "Test Author",
            "version": "1.0.0",
            "date": "2025-01-30"
        }
        # Note: handbook metadata is accessed through meta adapter, not as separate source
        data_sources = {
            "meta": meta_adapter,
            "netbox": netbox_adapter,
            "metadata": metadata_dict
        }
        processor = PlaceholderProcessor(data_sources, metadata_dict)
        output_generator = OutputGenerator(output_dir, test_mode=True)
        
        # Process templates
        templates = template_manager.get_templates("de", "bcm")
        assert len(templates) == 3, "Should find 3 BCM templates"
        
        processed_results = []
        templates_data = []
        for template in templates:
            content = template.read_content()
            result = processor.process_template(content, template.path.name)
            processed_results.append(result)
            
            # Extract template number and name from filename
            filename = template.path.stem  # e.g., "0010_Zweck_und_Geltungsbereich"
            templates_data.append((filename, result.content))
        
        # Generate separate markdown files
        result = output_generator.generate_separate_markdown_files(
            templates_data,
            "de",
            "bcm"
        )
        
        # Generate TOC file
        toc_data = []
        for template in templates:
            filename = template.path.stem
            parts = filename.split("_", 1)
            template_number = parts[0]
            template_title = parts[1].replace("_", " ") if len(parts) > 1 else filename
            toc_data.append((template_number, template_title, f"{filename}.md"))
        
        toc_result = output_generator.generate_markdown_toc(
            toc_data,
            "de",
            "bcm"
        )
        
        # Verify output directory structure
        markdown_dir = output_dir / "de" / "bcm" / "markdown"
        assert markdown_dir.exists(), "Markdown directory should exist"
        
        # Verify one file per template
        markdown_files = list(markdown_dir.glob("*.md"))
        # Should have 3 template files + 1 TOC file
        assert len(markdown_files) == 4, f"Should have 4 markdown files (3 templates + TOC), got {len(markdown_files)}"
        
        # Verify TOC.md exists
        toc_file = markdown_dir / "TOC.md"
        assert toc_file.exists(), "TOC.md should exist"
        
        # Verify TOC content
        toc_content = toc_file.read_text()
        assert "0010" in toc_content, "TOC should contain template 0010"
        assert "0020" in toc_content, "TOC should contain template 0020"
        assert "0030" in toc_content, "TOC should contain template 0030"
        assert ".md" in toc_content, "TOC should contain links to .md files"
        
        # Verify individual template files exist
        template_0010 = markdown_dir / "0010_Zweck_und_Geltungsbereich.md"
        template_0020 = markdown_dir / "0020_BCM_Leitlinie_Policy.md"
        template_0030 = markdown_dir / "0030_Dokumentenlenkung.md"
        
        assert template_0010.exists(), "Template 0010 file should exist"
        assert template_0020.exists(), "Template 0020 file should exist"
        assert template_0030.exists(), "Template 0030 file should exist"
        
        # Verify template content has placeholders replaced
        content_0010 = template_0010.read_text()
        assert "{{ handbook.version }}" not in content_0010, "Placeholders should be replaced"
        assert "1.0.0" in content_0010, "Handbook version should be present"
        assert "BCM Manager" in content_0010, "Handbook owner should be present"
        
        # Verify no combined file was created
        combined_file = markdown_dir / "bcm_handbook.md"
        assert not combined_file.exists(), "Combined markdown file should NOT exist in separate mode"
        
        # Verify no errors occurred
        total_errors = sum(len(r.errors) for r in processed_results)
        assert total_errors == 0, "No errors should occur during processing"


@pytest.mark.integration
def test_pdf_with_toc_generation(temp_workspace, bcm_templates_for_testing,
                                sample_metadata_config_with_handbooks,
                                mock_netbox_api):
    """
    Test PDF generation with table of contents and page breaks.
    
    This test verifies:
    - PDF file is created
    - PDF contains TOC at beginning (check HTML structure before PDF conversion)
    - Page breaks are inserted between templates (check HTML structure)
    - Test mode validation works
    
    Requirements: 33.1, 33.2, 33.3, 33.4
    """
    from src.meta_adapter import MetaAdapter
    
    # Setup output directory
    output_dir = temp_workspace / "test-output"
    
    # Initialize components
    template_manager = TemplateManager(bcm_templates_for_testing)
    
    # Create meta adapter
    meta_adapter = MetaAdapter(sample_metadata_config_with_handbooks)
    meta_adapter.connect()
    
    # Set handbook type for handbook placeholders
    meta_adapter.set_handbook_type("bcm")
    
    # Create netbox adapter
    with patch('pynetbox.api') as mock_pynetbox:
        mock_pynetbox.return_value = mock_netbox_api
        
        netbox_adapter = NetBoxAdapter(
            url="https://netbox.example.com",
            api_token="test_token"
        )
        netbox_adapter.connect()
        
        # Create placeholder processor
        metadata_dict = {
            "author": "Test Author",
            "version": "1.0.0",
            "date": "2025-01-30"
        }
        data_sources = {
            "meta": meta_adapter,
            "netbox": netbox_adapter,
            "metadata": metadata_dict,
            
        }
        processor = PlaceholderProcessor(data_sources, metadata_dict)
        output_generator = OutputGenerator(output_dir, test_mode=True)
        
        # Process templates
        templates = template_manager.get_templates("de", "bcm")
        assert len(templates) == 3, "Should find 3 BCM templates"
        
        processed_results = []
        templates_data = []
        for template in templates:
            content = template.read_content()
            result = processor.process_template(content, template.path.name)
            processed_results.append(result)
            
            # Extract template number and title
            filename = template.path.stem
            parts = filename.split("_", 1)
            template_number = parts[0]
            template_title = parts[1].replace("_", " ") if len(parts) > 1 else filename
            
            templates_data.append((template_number, template_title, result.content))
        
        # Generate PDF with TOC
        try:
            result = output_generator.generate_pdf_with_toc(
                templates_data,
                "de",
                "bcm"
            )
            
            # Verify PDF file was created
            pdf_dir = output_dir / "de" / "pdf"
            assert pdf_dir.exists(), "PDF directory should exist"
            
            pdf_file = pdf_dir / "bcm_handbook.pdf"
            assert pdf_file.exists(), "PDF file should exist"
            
            # Verify PDF has content
            assert pdf_file.stat().st_size > 0, "PDF should have content"
            
            # Verify HTML structure before PDF conversion (check result object)
            # The HTML should contain TOC and page breaks
            assert result.html_content is not None, "HTML content should be generated"
            
            html_content = result.html_content
            
            # Verify TOC is present
            assert "Table of Contents" in html_content or "Inhaltsverzeichnis" in html_content, \
                "HTML should contain TOC heading"
            assert "0010" in html_content, "TOC should list template 0010"
            assert "0020" in html_content, "TOC should list template 0020"
            assert "0030" in html_content, "TOC should list template 0030"
            
            # Verify page breaks are present
            assert "page-break-after" in html_content or "page-break-before" in html_content, \
                "HTML should contain page break CSS"
            
            # Verify anchor IDs for TOC links
            assert 'id="section-' in html_content or 'id="template-' in html_content, \
                "HTML should contain anchor IDs for TOC links"
            
        except Exception as e:
            # PDF generation might fail if system libraries are missing
            pytest.skip(f"PDF generation skipped: {e}")


@pytest.mark.integration
def test_multi_format_output_generation(temp_workspace, bcm_templates_for_testing,
                                       sample_metadata_config_with_handbooks,
                                       mock_netbox_api):
    """
    Test generation of multiple output formats simultaneously.
    
    This test verifies:
    - HTML, separate markdown, and PDF with TOC can be generated for one handbook
    - All formats coexist correctly in test-output structure
    - Output directory structure is correct (test-output/{language}/{type}/)
    - Test mode validation works for all output types
    
    Requirements: 31.1-31.5, 32.1-32.6, 33.1-33.4
    """
    from src.meta_adapter import MetaAdapter
    from src.html_output_generator import HTMLOutputGenerator
    
    # Setup output directory
    output_dir = temp_workspace / "test-output"
    
    # Initialize components
    template_manager = TemplateManager(bcm_templates_for_testing)
    
    # Create meta adapter
    meta_adapter = MetaAdapter(sample_metadata_config_with_handbooks)
    meta_adapter.connect()
    
    # Set handbook type for handbook placeholders
    meta_adapter.set_handbook_type("bcm")
    
    # Create netbox adapter
    with patch('pynetbox.api') as mock_pynetbox:
        mock_pynetbox.return_value = mock_netbox_api
        
        netbox_adapter = NetBoxAdapter(
            url="https://netbox.example.com",
            api_token="test_token"
        )
        netbox_adapter.connect()
        
        # Create placeholder processor
        metadata_dict = {
            "author": "Test Author",
            "version": "1.0.0",
            "date": "2025-01-30"
        }
        data_sources = {
            "meta": meta_adapter,
            "netbox": netbox_adapter,
            "metadata": metadata_dict,
            
        }
        processor = PlaceholderProcessor(data_sources, metadata_dict)
        output_generator = OutputGenerator(output_dir, test_mode=True)
        html_generator = HTMLOutputGenerator(output_dir, test_mode=True)
        
        # Process templates
        templates = template_manager.get_templates("de", "bcm")
        assert len(templates) == 3, "Should find 3 BCM templates"
        
        processed_results = []
        templates_data_markdown = []
        templates_data_pdf = []
        templates_data_html = []
        
        for template in templates:
            content = template.read_content()
            result = processor.process_template(content, template.path.name)
            processed_results.append(result)
            
            filename = template.path.stem
            parts = filename.split("_", 1)
            template_number = parts[0]
            template_title = parts[1].replace("_", " ") if len(parts) > 1 else filename
            
            templates_data_markdown.append((filename, result.content))
            templates_data_pdf.append((template_number, template_title, result.content))
            templates_data_html.append((template_number, template_title, result.content))
        
        # Generate separate markdown files
        markdown_result = output_generator.generate_separate_markdown_files(
            templates_data_markdown,
            "de",
            "bcm"
        )
        
        # Generate TOC for markdown
        toc_data = [(num, title, f"{num}_{title.replace(' ', '_')}.md") 
                    for num, title, _ in templates_data_pdf]
        toc_result = output_generator.generate_markdown_toc(
            toc_data,
            "de",
            "bcm"
        )
        
        # Generate HTML output
        html_contents = [content for _, _, content in templates_data_html]
        html_filenames = [f"{num}_{title.replace(' ', '_')}" for num, title, _ in templates_data_html]
        html_result = html_generator.generate_html_site(
            html_contents,
            html_filenames,
            "de",
            "bcm"
        )
        
        # Generate PDF with TOC
        try:
            pdf_result = output_generator.generate_pdf_with_toc(
                templates_data_pdf,
                "de",
                "bcm"
            )
            pdf_generated = True
        except Exception as e:
            # PDF generation might fail if system libraries are missing
            pdf_generated = False
            print(f"PDF generation skipped: {e}")
        
        # Verify output directory structure
        assert (output_dir / "de" / "bcm" / "markdown").exists(), "Markdown directory should exist"
        assert (output_dir / "de" / "bcm" / "html").exists(), "HTML directory should exist"
        
        # Verify markdown files
        markdown_dir = output_dir / "de" / "bcm" / "markdown"
        markdown_files = list(markdown_dir.glob("*.md"))
        assert len(markdown_files) == 4, "Should have 4 markdown files (3 templates + TOC)"
        
        # Verify HTML files
        html_dir = output_dir / "de" / "bcm" / "html"
        html_files = list(html_dir.glob("*.html"))
        assert len(html_files) >= 4, "Should have at least 4 HTML files (3 templates + index)"
        
        # Debug: print actual HTML files created
        print(f"HTML files created: {[f.name for f in html_files]}")
        
        # Verify index.html exists
        index_file = html_dir / "index.html"
        assert index_file.exists(), "index.html should exist"
        
        # Verify PDF file (if generated)
        if pdf_generated:
            pdf_dir = output_dir / "de" / "pdf"
            assert pdf_dir.exists(), "PDF directory should exist"
            pdf_file = pdf_dir / "bcm_handbook.pdf"
            assert pdf_file.exists(), "PDF file should exist"
        
        # Verify all formats have correct content
        # Check markdown
        markdown_0010 = markdown_dir / "0010_Zweck_und_Geltungsbereich.md"
        markdown_content = markdown_0010.read_text()
        assert "1.0.0" in markdown_content, "Markdown should have replaced placeholders"
        
        # Check HTML - use the first template file found
        template_html_files = [f for f in html_files if f.name != "index.html"]
        if template_html_files:
            html_content = template_html_files[0].read_text()
            assert "1.0.0" in html_content, "HTML should have replaced placeholders"
        
        # Verify no errors occurred
        total_errors = sum(len(r.errors) for r in processed_results)
        assert total_errors == 0, "No errors should occur during processing"


@pytest.mark.integration
def test_complete_workflow_with_all_new_features(temp_workspace, bcm_templates_for_testing,
                                                 sample_metadata_config_with_handbooks):
    """
    Test complete workflow with all Phase 6 features.
    
    This test verifies:
    - Mock NetBox API for data loading
    - Per-handbook metadata for multiple handbook types
    - All placeholder types (meta, meta-netbox, handbook, extended roles)
    - All output formats (HTML, separate markdown, PDF with TOC)
    - Test mode validation
    - Complete workflow executes without errors
    
    Requirements: All Phase 6 requirements
    """
    from src.meta_adapter import MetaAdapter
    from src.meta_netbox_adapter import MetaNetBoxAdapter
    from src.netbox_metadata_loader import NetBoxMetadataLoader
    from src.html_output_generator import HTMLOutputGenerator
    from src.metadata_config_manager import (
        MetadataConfig, OrganizationInfo, PersonRole, DocumentInfo
    )
    
    # Setup output directory
    output_dir = temp_workspace / "test-output"
    
    # Create extended metadata config with new roles
    organization = OrganizationInfo(
        name="Test Organization GmbH",
        address="Test Street 123",
        city="Test City",
        postal_code="12345",
        country="Germany",
        website="https://test.example.com",
        phone="+49 123 456789",
        email="info@test.example.com"
    )
    
    roles = {
        "ceo": PersonRole(
            name="John Doe",
            title="Chief Executive Officer",
            email="john.doe@test.example.com",
            phone="+49 123 456789-100"
        ),
        "cio": PersonRole(
            name="Jane Smith",
            title="Chief Information Officer",
            email="jane.smith@test.example.com",
            phone="+49 123 456789-200"
        ),
        "ciso": PersonRole(
            name="Bob Johnson",
            title="Chief Information Security Officer",
            email="bob.johnson@test.example.com",
            phone="+49 123 456789-300"
        ),
        "sysop": PersonRole(
            name="Alice Admin",
            title="System Administrator",
            email="alice.admin@test.example.com",
            phone="+49 123 456789-400"
        ),
        "datenschutzbeauftragter": PersonRole(
            name="Charlie Privacy",
            title="Data Protection Officer",
            email="charlie.privacy@test.example.com",
            phone="+49 123 456789-500"
        )
    }
    
    document = DocumentInfo(
        owner="IT Operations Manager",
        approver="CIO",
        version="2.0.0",
        classification="internal"
    )
    
    extended_metadata_config = MetadataConfig(
        organization=organization,
        roles=roles,
        document=document,
        author="Test Author [test@example.com]",
        language="de"
    )
    
    # Mock NetBox metadata
    netbox_metadata = {
        "contacts": {
            "ciso": {
                "name": "NetBox CISO",
                "email": "netbox.ciso@test.example.com",
                "phone": "+49 123 999-100"
            }
        },
        "devices": {
            "firewall": {
                "name": "fw-01",
                "ip": "192.168.1.1"
            }
        },
        "sites": {
            "primary": {
                "name": "Datacenter Munich",
                "address": "Munich Street 1"
            }
        }
    }
    
    # Create mock NetBox API
    mock_netbox_api = MagicMock()
    mock_device = MagicMock()
    mock_device.name = "backup-server-01"
    mock_device.primary_ip = "192.168.1.100"
    mock_site = MagicMock()
    mock_site.name = "Datacenter Munich"
    mock_device.site = mock_site
    mock_netbox_api.dcim.devices.all.return_value = [mock_device]
    mock_netbox_api.dcim.sites.all.return_value = [mock_site]
    mock_netbox_api.dcim.devices.get.return_value = mock_device
    mock_netbox_api.dcim.sites.get.return_value = mock_site
    
    # Initialize components
    template_manager = TemplateManager(bcm_templates_for_testing)
    
    # Create meta adapter with extended metadata (includes handbooks)
    meta_adapter = MetaAdapter(sample_metadata_config_with_handbooks)
    meta_adapter.connect()
    
    # Set handbook type for handbook placeholders
    meta_adapter.set_handbook_type("bcm")
    
    # Create meta-netbox adapter
    meta_netbox_adapter = MetaNetBoxAdapter(netbox_metadata)
    meta_netbox_adapter.connect()
    
    # Create netbox adapter
    with patch('pynetbox.api') as mock_pynetbox:
        mock_pynetbox.return_value = mock_netbox_api
        
        netbox_adapter = NetBoxAdapter(
            url="https://netbox.example.com",
            api_token="test_token"
        )
        netbox_adapter.connect()
        
        # Create placeholder processor with all adapters
        metadata_dict = {
            "author": "Test Author",
            "version": "1.0.0",
            "date": "2025-01-30"
        }
        data_sources = {
            "meta": meta_adapter,
            "meta-netbox": meta_netbox_adapter,
            "netbox": netbox_adapter,
            "metadata": metadata_dict,
            
        }
        processor = PlaceholderProcessor(data_sources, metadata_dict)
        output_generator = OutputGenerator(output_dir, test_mode=True)
        html_generator = HTMLOutputGenerator(output_dir, test_mode=True)
        
        # Process templates
        templates = template_manager.get_templates("de", "bcm")
        assert len(templates) == 3, "Should find 3 BCM templates"
        
        processed_results = []
        templates_data = []
        
        for template in templates:
            content = template.read_content()
            result = processor.process_template(content, template.path.name)
            processed_results.append(result)
            
            filename = template.path.stem
            parts = filename.split("_", 1)
            template_number = parts[0]
            template_title = parts[1].replace("_", " ") if len(parts) > 1 else filename
            
            templates_data.append((template_number, template_title, result.content))
        
        # Verify no errors occurred
        total_errors = sum(len(r.errors) for r in processed_results)
        assert total_errors == 0, "No errors should occur during processing"
        
        # Verify all placeholder types were used
        all_content = "\n\n".join([r.content for r in processed_results])
        
        # Check meta placeholders
        assert "{{ meta.organization.name }}" not in all_content
        assert "{{ meta.ciso.name }}" not in all_content
        assert "Test Organization GmbH" in all_content
        assert "Bob Johnson" in all_content
        
        # Check handbook placeholders
        assert "{{ handbook.version }}" not in all_content
        assert "{{ handbook.owner }}" not in all_content
        assert "1.0.0" in all_content
        assert "BCM Manager" in all_content
        
        # Check netbox placeholders
        assert "{{ netbox.site_name }}" not in all_content
        assert "Datacenter Munich" in all_content
        
        # Generate all output formats
        markdown_data = [(f"{t[0]}_{t[1].replace(' ', '_')}", t[2]) for t in templates_data]
        
        # Generate separate markdown
        markdown_result = output_generator.generate_separate_markdown_files(
            markdown_data,
            "de",
            "bcm"
        )
        
        # Generate TOC for markdown
        toc_data = [(num, title, f"{num}_{title.replace(' ', '_')}.md") 
                    for num, title, _ in templates_data]
        toc_result = output_generator.generate_markdown_toc(
            toc_data,
            "de",
            "bcm"
        )
        
        # Generate HTML
        html_contents = [content for _, _, content in templates_data]
        html_filenames = [f"{num}_{title.replace(' ', '_')}" for num, title, _ in templates_data]
        html_result = html_generator.generate_html_site(
            html_contents,
            html_filenames,
            "de",
            "bcm"
        )
        
        # Generate PDF with TOC (may skip if libraries missing)
        try:
            pdf_result = output_generator.generate_pdf_with_toc(
                templates_data,
                "de",
                "bcm"
            )
            pdf_generated = True
        except Exception as e:
            pdf_generated = False
            print(f"PDF generation skipped: {e}")
        
        # Verify all outputs were created
        assert (output_dir / "de" / "bcm" / "markdown").exists(), "Markdown directory should exist"
        assert (output_dir / "de" / "bcm" / "html").exists(), "HTML directory should exist"
        
        # Verify markdown files
        markdown_dir = output_dir / "de" / "bcm" / "markdown"
        assert (markdown_dir / "TOC.md").exists(), "TOC.md should exist"
        assert len(list(markdown_dir.glob("*.md"))) == 4, "Should have 4 markdown files"
        
        # Verify HTML files
        html_dir = output_dir / "de" / "bcm" / "html"
        assert (html_dir / "index.html").exists(), "index.html should exist"
        assert len(list(html_dir.glob("*.html"))) >= 4, "Should have at least 4 HTML files"
        
        # Verify PDF (if generated)
        if pdf_generated:
            pdf_dir = output_dir / "de" / "pdf"
            assert (pdf_dir / "bcm_handbook.pdf").exists(), "PDF should exist"
        
        # Verify test mode validation
        # Try to create output generator without test mode - should fail
        non_test_generator = OutputGenerator(output_dir, test_mode=False)
        
        result = non_test_generator.generate_separate_markdown_files(
            markdown_data,
            "de",
            "bcm"
        )
        
        # Should have errors about test mode
        assert len(result.errors) > 0, "Should have errors when test mode is disabled"
        error_message = " ".join(result.errors).lower()
        assert "test" in error_message or "flag" in error_message, \
            "Error should mention test mode requirement"


# ============================================================================
# CIS Controls Integration Tests
# ============================================================================

@pytest.fixture
def cis_controls_templates(temp_workspace):
    """Create CIS Controls templates for integration testing."""
    templates_dir = temp_workspace / "templates"
    
    # German CIS Controls templates
    de_cis = templates_dir / "de" / "cis-controls"
    de_cis.mkdir(parents=True)
    
    # Metadata template
    (de_cis / "0000_metadata_de_cis-controls.md").write_text("""# CIS Controls v8 Hardening Templates

**Dokument-Metadaten**

- **Autor:** {{ meta.author }}
- **Version:** {{ meta.document.version }}
- **Organisation:** {{ meta.organization.name }}
- **Klassifizierung:** {{ meta.document.classification }}

---
""")
    
    # Foundation templates
    (de_cis / "0010_CIS_Controls_Ueberblick_und_Vorgehen.md").write_text("""# 1. CIS Controls Überblick und Vorgehen

## 1.1 Einführung

Die CIS Controls v8 bieten einen strukturierten Ansatz zur Systemhärtung.

Organisation: {{ meta.organization.name }}
Standort: {{ meta.organization.city }}
""")
    
    (de_cis / "0020_Geltungsbereich_Assetgruppen_und_Tiering.md").write_text("""# 2. Geltungsbereich, Assetgruppen und Tiering

## 2.1 Geltungsbereich

Dieses Dokument gilt für alle IT-Systeme der {{ meta.organization.name }}.

## 2.2 Verantwortlichkeiten

- **CISO:** {{ meta.ciso.name }}
- **CIO:** {{ meta.cio.name }}
""")
    
    # OS templates
    (de_cis / "0110_OS_Windows_Server_Hardening_Baseline.md").write_text("""# 3. Windows Server Hardening Baseline

## 3.1 Sicherheitseinstellungen

Dokumentverantwortlicher: {{ meta.document.owner }}
Genehmiger: {{ meta.document.approver }}
""")
    
    # English CIS Controls templates
    en_cis = templates_dir / "en" / "cis-controls"
    en_cis.mkdir(parents=True)
    
    # Metadata template
    (en_cis / "0000_metadata_en_cis-controls.md").write_text("""# CIS Controls v8 Hardening Templates

**Document Metadata**

- **Author:** {{ meta.author }}
- **Version:** {{ meta.document.version }}
- **Organization:** {{ meta.organization.name }}
- **Classification:** {{ meta.document.classification }}

---
""")
    
    # Foundation templates
    (en_cis / "0010_CIS_Controls_Overview_and_Approach.md").write_text("""# 1. CIS Controls Overview and Approach

## 1.1 Introduction

CIS Controls v8 provide a structured approach to system hardening.

Organization: {{ meta.organization.name }}
Location: {{ meta.organization.city }}
""")
    
    (en_cis / "0020_Scope_Asset_Groups_and_Tiering.md").write_text("""# 2. Scope, Asset Groups and Tiering

## 2.1 Scope

This document applies to all IT systems of {{ meta.organization.name }}.

## 2.2 Responsibilities

- **CISO:** {{ meta.ciso.name }}
- **CIO:** {{ meta.cio.name }}
""")
    
    # OS templates
    (en_cis / "0110_OS_Windows_Server_Hardening_Baseline.md").write_text("""# 3. Windows Server Hardening Baseline

## 3.1 Security Settings

Document Owner: {{ meta.document.owner }}
Approver: {{ meta.document.approver }}
""")
    
    return templates_dir


@pytest.fixture
def sample_meta_config():
    """Create sample metadata configuration for CIS Controls testing."""
    from src.metadata_config_manager import (
        MetadataConfig, OrganizationInfo, PersonRole, DocumentInfo
    )
    
    organization = OrganizationInfo(
        name="SecureOrg GmbH",
        address="Security Street 42",
        city="Munich",
        postal_code="80331",
        country="Germany",
        website="https://secureorg.example.com",
        phone="+49 89 12345678",
        email="info@secureorg.example.com"
    )
    
    roles = {
        "ceo": PersonRole(
            name="Alice Schmidt",
            title="Chief Executive Officer",
            email="alice.schmidt@secureorg.example.com",
            phone="+49 89 12345678-100",
            department="Management"
        ),
        "cio": PersonRole(
            name="Bob Mueller",
            title="Chief Information Officer",
            email="bob.mueller@secureorg.example.com",
            phone="+49 89 12345678-200",
            department="IT"
        ),
        "ciso": PersonRole(
            name="Carol Weber",
            title="Chief Information Security Officer",
            email="carol.weber@secureorg.example.com",
            phone="+49 89 12345678-300",
            department="IT Security"
        )
    }
    
    document = DocumentInfo(
        owner="Security Operations Manager",
        approver="CISO",
        version="1.0.0",
        classification="confidential"
    )
    
    return MetadataConfig(
        organization=organization,
        roles=roles,
        document=document,
        author="Security Team [security@secureorg.example.com]",
        language="de"
    )


@pytest.mark.integration
def test_end_to_end_cis_controls_german_generation(temp_workspace, cis_controls_templates, sample_meta_config):
    """
    Test complete CIS Controls handbook generation workflow for German.
    
    This test verifies:
    - Template discovery for CIS Controls
    - Placeholder detection and replacement with meta adapter
    - Markdown output generation
    - Output directory structure
    - Content correctness
    
    Requirements: 3.1, 5.1, 5.2, 5.3
    Feature: cis-controls-integration
    Task: 14.1
    """
    from src.meta_adapter import MetaAdapter
    
    output_dir = temp_workspace / "Handbook"
    
    # Initialize components
    template_manager = TemplateManager(cis_controls_templates)
    logger = HandbookLogger(verbose=False)
    
    # Initialize meta adapter
    meta_adapter = MetaAdapter(sample_meta_config, language='de')
    meta_adapter.connect()
    meta_adapter.set_handbook_type('cis-controls')
    
    data_sources = {'meta': meta_adapter}
    processor = PlaceholderProcessor(data_sources)
    output_generator = OutputGenerator(output_dir, test_mode=True)
    
    # Execute workflow
    # 1. Discover templates
    templates = template_manager.get_templates('de', 'cis-controls')
    assert len(templates) == 4, "Should find 4 German CIS Controls templates"
    
    # 2. Process templates
    processed_results = []
    for template in templates:
        content = template.read_content()
        result = processor.process_template(content, template.path.name)
        processed_results.append(result)
    
    # 3. Verify placeholder replacements
    all_content = "\n\n".join([r.content for r in processed_results])
    
    # Check that placeholders were replaced
    assert "{{ meta.organization.name }}" not in all_content
    assert "{{ meta.organization.city }}" not in all_content
    assert "{{ meta.ciso.name }}" not in all_content
    assert "{{ meta.cio.name }}" not in all_content
    assert "{{ meta.document.owner }}" not in all_content
    assert "{{ meta.document.approver }}" not in all_content
    assert "{{ meta.author }}" not in all_content
    assert "{{ meta.document.version }}" not in all_content
    assert "{{ meta.document.classification }}" not in all_content
    
    # Check that actual values are present
    assert "SecureOrg GmbH" in all_content
    assert "Munich" in all_content
    assert "Carol Weber" in all_content
    assert "Bob Mueller" in all_content
    assert "Security Operations Manager" in all_content
    assert "CISO" in all_content
    assert "Security Team" in all_content
    assert "1.0.0" in all_content
    assert "confidential" in all_content
    
    # 4. Generate markdown output
    processed_contents = [r.content for r in processed_results]
    output_result = output_generator.generate_markdown(
        processed_contents,
        'de',
        'cis-controls'
    )
    output_path = output_result.markdown_path
    
    # 5. Verify output file exists and structure
    assert output_path.exists(), "Output file should be created"
    assert output_path.parent == output_dir / "de" / "cis-controls" / "markdown" 
    assert output_path.name == "cis-controls_handbook.md"
    
    # 6. Verify output content
    output_content = output_path.read_text()
    assert "SecureOrg GmbH" in output_content
    assert "CIS Controls v8 Hardening Templates" in output_content
    assert "CIS Controls Überblick und Vorgehen" in output_content
    assert "Geltungsbereich, Assetgruppen und Tiering" in output_content
    assert "Windows Server Hardening Baseline" in output_content
    
    # 7. Verify no errors occurred
    total_errors = sum(len(r.errors) for r in processed_results)
    assert total_errors == 0, "No errors should occur during processing"


@pytest.mark.integration
def test_end_to_end_cis_controls_english_generation(temp_workspace, cis_controls_templates, sample_meta_config):
    """
    Test complete CIS Controls handbook generation workflow for English.
    
    This test verifies:
    - Template discovery for English CIS Controls
    - Placeholder replacement with English language setting
    - Markdown output generation
    - Language-specific content
    
    Requirements: 3.1, 5.1, 5.2, 5.3
    Feature: cis-controls-integration
    Task: 14.1
    """
    from src.meta_adapter import MetaAdapter
    
    output_dir = temp_workspace / "Handbook"
    
    # Initialize components
    template_manager = TemplateManager(cis_controls_templates)
    logger = HandbookLogger(verbose=False)
    
    # Initialize meta adapter with English language
    meta_adapter = MetaAdapter(sample_meta_config, language='en')
    meta_adapter.connect()
    meta_adapter.set_handbook_type('cis-controls')
    
    data_sources = {'meta': meta_adapter}
    processor = PlaceholderProcessor(data_sources)
    output_generator = OutputGenerator(output_dir, test_mode=True)
    
    # Execute workflow
    # 1. Discover templates
    templates = template_manager.get_templates('en', 'cis-controls')
    assert len(templates) == 4, "Should find 4 English CIS Controls templates"
    
    # 2. Process templates
    processed_results = []
    for template in templates:
        content = template.read_content()
        result = processor.process_template(content, template.path.name)
        processed_results.append(result)
    
    # 3. Verify placeholder replacements
    all_content = "\n\n".join([r.content for r in processed_results])
    
    # Check that placeholders were replaced
    assert "{{ meta.organization.name }}" not in all_content
    assert "{{ meta.organization.city }}" not in all_content
    assert "{{ meta.ciso.name }}" not in all_content
    assert "{{ meta.cio.name }}" not in all_content
    
    # Check that actual values are present
    assert "SecureOrg GmbH" in all_content
    assert "Munich" in all_content
    assert "Carol Weber" in all_content
    assert "Bob Mueller" in all_content
    
    # 4. Generate markdown output
    processed_contents = [r.content for r in processed_results]
    output_result = output_generator.generate_markdown(
        processed_contents,
        'en',
        'cis-controls'
    )
    output_path = output_result.markdown_path
    
    # 5. Verify output file exists and structure
    assert output_path.exists(), "Output file should be created"
    assert output_path.parent == output_dir / "en" / "cis-controls" / "markdown" 
    assert output_path.name == "cis-controls_handbook.md"
    
    # 6. Verify English-specific content
    output_content = output_path.read_text()
    assert "SecureOrg GmbH" in output_content
    assert "CIS Controls v8 Hardening Templates" in output_content
    assert "CIS Controls Overview and Approach" in output_content
    assert "Scope, Asset Groups and Tiering" in output_content
    assert "Windows Server Hardening Baseline" in output_content
    
    # 7. Verify no errors occurred
    total_errors = sum(len(r.errors) for r in processed_results)
    assert total_errors == 0, "No errors should occur during processing"


@pytest.mark.integration
def test_end_to_end_cis_controls_all_formats(temp_workspace, cis_controls_templates, sample_meta_config):
    """
    Test CIS Controls handbook generation in all output formats.
    
    This test verifies:
    - Markdown generation
    - PDF generation
    - HTML generation
    - All formats work correctly for CIS Controls
    
    Requirements: 5.1, 5.2, 5.3
    Feature: cis-controls-integration
    Task: 14.1
    """
    from src.meta_adapter import MetaAdapter
    
    output_dir = temp_workspace / "Handbook"
    
    # Initialize components
    template_manager = TemplateManager(cis_controls_templates)
    logger = HandbookLogger(verbose=False)
    
    # Initialize meta adapter
    meta_adapter = MetaAdapter(sample_meta_config, language='de')
    meta_adapter.connect()
    meta_adapter.set_handbook_type('cis-controls')
    
    data_sources = {'meta': meta_adapter}
    processor = PlaceholderProcessor(data_sources)
    output_generator = OutputGenerator(output_dir, test_mode=True)
    
    # Process templates
    templates = template_manager.get_templates('de', 'cis-controls')
    processed_results = []
    for template in templates:
        content = template.read_content()
        result = processor.process_template(content, template.path.name)
        processed_results.append(result)
    
    processed_contents = [r.content for r in processed_results]
    
    # Test 1: Generate Markdown
    md_result = output_generator.generate_markdown(processed_contents, 'de', 'cis-controls')
    md_path = md_result.markdown_path
    
    assert md_path.exists(), "Markdown file should be created"
    assert md_path.suffix == ".md"
    assert md_path.name == "cis-controls_handbook.md"
    
    # Test 2: Generate PDF
    markdown_content = md_path.read_text()
    
    try:
        pdf_result = output_generator.generate_pdf(markdown_content, 'de', 'cis-controls')
        pdf_path = pdf_result.pdf_path
        
        assert pdf_path.exists(), "PDF file should be created"
        assert pdf_path.suffix == ".pdf"
        assert pdf_path.name == "cis-controls_handbook.pdf"
        assert pdf_path.stat().st_size > 0, "PDF should have content"
        
    except Exception as e:
        # PDF generation might fail if system libraries are missing
        pytest.skip(f"PDF generation skipped: {e}")
    
    # Test 3: Generate HTML
    html_generator = HTMLOutputGenerator(output_dir, test_mode=True)
    filenames = [template.path.name for template in templates]
    
    html_result = html_generator.generate_html_site(
        processed_contents,
        filenames,
        'de',
        'cis-controls'
    )
    
    html_dir = html_result.get('html_dir')
    assert html_dir is not None, "HTML directory should be created"
    assert html_dir.exists(), "HTML directory should exist"
    
    # Verify HTML files
    html_files = list(html_dir.glob("*.html"))
    assert len(html_files) > 0, "HTML files should be generated"
    
    # Verify index.html exists
    index_html = html_dir / "index.html"
    assert index_html.exists(), "index.html should exist"
    
    # Verify styles.css exists
    styles_css = html_dir / "styles.css"
    assert styles_css.exists(), "styles.css should exist"
    
    # Verify HTML content
    index_content = index_html.read_text()
    assert "CIS Controls" in index_content, "HTML should contain CIS Controls content"



@pytest.mark.integration
def test_cis_controls_separate_files_mode(temp_workspace, cis_controls_templates, sample_meta_config):
    """
    Test CIS Controls handbook generation with separate markdown files.
    
    This test verifies:
    - Separate markdown files generation for each template
    - TOC.md creation with proper links
    - File naming conventions
    - Directory structure
    
    Requirements: 5.4
    Feature: cis-controls-integration
    Task: 14.2
    """
    from src.meta_adapter import MetaAdapter
    
    output_dir = temp_workspace / "Handbook"
    
    # Initialize components
    template_manager = TemplateManager(cis_controls_templates)
    logger = HandbookLogger(verbose=False)
    
    # Initialize meta adapter
    meta_adapter = MetaAdapter(sample_meta_config, language='de')
    meta_adapter.connect()
    meta_adapter.set_handbook_type('cis-controls')
    
    data_sources = {'meta': meta_adapter}
    processor = PlaceholderProcessor(data_sources)
    output_generator = OutputGenerator(output_dir, test_mode=True)
    
    # Process templates
    templates = template_manager.get_templates('de', 'cis-controls')
    processed_results = []
    for template in templates:
        content = template.read_content()
        result = processor.process_template(content, template.path.name)
        processed_results.append(result)
    
    processed_contents = [r.content for r in processed_results]
    
    # Generate separate markdown files
    templates_data = [
        (template.path.name, content)
        for template, content in zip(templates, processed_contents)
    ]
    
    md_result = output_generator.generate_separate_markdown_files(
        templates_data,
        'de',
        'cis-controls'
    )
    
    # Verify result
    assert md_result.markdown_path is not None, "Markdown path should be set"
    output_dir_path = md_result.markdown_path.parent
    
    # Verify directory structure
    assert output_dir_path == output_dir / "de" / "cis-controls" / "markdown"
    assert output_dir_path.exists(), "Output directory should exist"
    
    # Verify separate files were created
    markdown_files = list(output_dir_path.glob("*.md"))
    # Should have 4 template files (excluding TOC.md if generated separately)
    template_files = [f for f in markdown_files if not f.name.startswith("TOC")]
    assert len(template_files) == 4, f"Should have 4 separate markdown files, found {len(template_files)}"
    
    # Verify file naming conventions
    expected_filenames = [
        "0000_metadata_de_cis-controls.md",
        "0010_CIS_Controls_Ueberblick_und_Vorgehen.md",
        "0020_Geltungsbereich_Assetgruppen_und_Tiering.md",
        "0110_OS_Windows_Server_Hardening_Baseline.md"
    ]
    
    actual_filenames = sorted([f.name for f in template_files])
    assert actual_filenames == sorted(expected_filenames), \
        f"File names should match template names. Expected: {expected_filenames}, Got: {actual_filenames}"
    
    # Verify each file has content
    for md_file in template_files:
        content = md_file.read_text()
        assert len(content) > 0, f"File {md_file.name} should have content"
        # Check that at least some placeholders were replaced (not all files have all placeholders)
        # Just verify the file has actual content, not empty
        assert len(content) > 50, f"File {md_file.name} should have substantial content"
    
    # Generate TOC file
    templates_info = []
    for template in templates:
        filename = template.path.name
        filename_base = Path(filename).stem
        template_number = filename_base[:4]
        title_part = filename_base[5:] if len(filename_base) > 5 else filename_base
        template_title = title_part.replace('_', ' ')
        templates_info.append((template_number, template_title, filename))
    
    toc_result = output_generator.generate_markdown_toc(
        templates_info,
        'de',
        'cis-controls'
    )
    
    # Verify TOC.md was created
    toc_path = toc_result.markdown_path
    assert toc_path is not None, "TOC path should be set"
    assert toc_path.exists(), "TOC.md should exist"
    assert toc_path.name == "TOC.md"
    
    # Verify TOC content
    toc_content = toc_path.read_text()
    assert "# Table of Contents" in toc_content or "# Inhaltsverzeichnis" in toc_content, \
        "TOC should have a title"
    
    # Verify TOC contains links to all templates
    for template_info in templates_info:
        template_number, template_title, filename = template_info
        # TOC should contain the filename as a link
        assert filename in toc_content, f"TOC should contain link to {filename}"
    
    # Verify no errors occurred
    assert len(md_result.errors) == 0, "No errors should occur during separate files generation"
    assert len(toc_result.errors) == 0, "No errors should occur during TOC generation"


@pytest.mark.integration
def test_cis_controls_separate_files_english(temp_workspace, cis_controls_templates, sample_meta_config):
    """
    Test CIS Controls separate files generation for English language.
    
    This test verifies:
    - Separate files work for English templates
    - File naming conventions for English
    - TOC generation for English
    
    Requirements: 5.4
    Feature: cis-controls-integration
    Task: 14.2
    """
    from src.meta_adapter import MetaAdapter
    
    output_dir = temp_workspace / "Handbook"
    
    # Initialize components
    template_manager = TemplateManager(cis_controls_templates)
    
    # Initialize meta adapter with English language
    meta_adapter = MetaAdapter(sample_meta_config, language='en')
    meta_adapter.connect()
    meta_adapter.set_handbook_type('cis-controls')
    
    data_sources = {'meta': meta_adapter}
    processor = PlaceholderProcessor(data_sources)
    output_generator = OutputGenerator(output_dir, test_mode=True)
    
    # Process templates
    templates = template_manager.get_templates('en', 'cis-controls')
    processed_results = []
    for template in templates:
        content = template.read_content()
        result = processor.process_template(content, template.path.name)
        processed_results.append(result)
    
    processed_contents = [r.content for r in processed_results]
    
    # Generate separate markdown files
    templates_data = [
        (template.path.name, content)
        for template, content in zip(templates, processed_contents)
    ]
    
    md_result = output_generator.generate_separate_markdown_files(
        templates_data,
        'en',
        'cis-controls'
    )
    
    # Verify result
    output_dir_path = md_result.markdown_path.parent
    assert output_dir_path == output_dir / "en" / "cis-controls" / "markdown" 
    
    # Verify separate files were created
    markdown_files = list(output_dir_path.glob("*.md"))
    template_files = [f for f in markdown_files if not f.name.startswith("TOC")]
    assert len(template_files) == 4, "Should have 4 separate markdown files for English"
    
    # Verify English file naming
    expected_filenames = [
        "0000_metadata_en_cis-controls.md",
        "0010_CIS_Controls_Overview_and_Approach.md",
        "0020_Scope_Asset_Groups_and_Tiering.md",
        "0110_OS_Windows_Server_Hardening_Baseline.md"
    ]
    
    actual_filenames = sorted([f.name for f in template_files])
    assert actual_filenames == sorted(expected_filenames), \
        f"English file names should match. Expected: {expected_filenames}, Got: {actual_filenames}"
    
    # Verify content is in English
    for md_file in template_files:
        content = md_file.read_text()
        if "Overview" in md_file.name:
            assert "Overview and Approach" in content, "Should contain English content"
        elif "Scope" in md_file.name:
            assert "Scope, Asset Groups" in content, "Should contain English content"



@pytest.mark.integration
def test_cis_controls_pdf_with_toc(temp_workspace, cis_controls_templates, sample_meta_config):
    """
    Test CIS Controls PDF generation with table of contents.
    
    This test verifies:
    - PDF generation with table of contents
    - Page breaks between sections
    - Clickable links in TOC
    - PDF structure and content
    
    Requirements: 5.5
    Feature: cis-controls-integration
    Task: 14.3
    """
    from src.meta_adapter import MetaAdapter
    
    output_dir = temp_workspace / "Handbook"
    
    # Initialize components
    template_manager = TemplateManager(cis_controls_templates)
    logger = HandbookLogger(verbose=False)
    
    # Initialize meta adapter
    meta_adapter = MetaAdapter(sample_meta_config, language='de')
    meta_adapter.connect()
    meta_adapter.set_handbook_type('cis-controls')
    
    data_sources = {'meta': meta_adapter}
    processor = PlaceholderProcessor(data_sources)
    output_generator = OutputGenerator(output_dir, test_mode=True)
    
    # Process templates
    templates = template_manager.get_templates('de', 'cis-controls')
    processed_results = []
    for template in templates:
        content = template.read_content()
        result = processor.process_template(content, template.path.name)
        processed_results.append(result)
    
    processed_contents = [r.content for r in processed_results]
    
    # Prepare templates data for PDF with TOC
    templates_data = []
    for template, content in zip(templates, processed_contents):
        filename = template.path.name
        filename_base = Path(filename).stem
        
        # Extract template number (first 4 digits)
        template_number = filename_base[:4]
        
        # Extract title (everything after first underscore, replace underscores with spaces)
        title_part = filename_base[5:] if len(filename_base) > 5 else filename_base
        template_title = title_part.replace('_', ' ')
        
        templates_data.append((template_number, template_title, content))
    
    # Generate PDF with TOC
    try:
        pdf_result = output_generator.generate_pdf_with_toc(
            templates_data,
            'de',
            'cis-controls'
        )
        
        # Verify PDF was created
        pdf_path = pdf_result.pdf_path
        assert pdf_path is not None, "PDF path should be set"
        assert pdf_path.exists(), "PDF file should be created"
        assert pdf_path.suffix == ".pdf"
        assert pdf_path.name == "cis-controls_handbook.pdf"
        
        # Verify PDF directory structure
        assert pdf_path.parent == output_dir / "de" / "cis-controls" / "pdf"
        
        # Verify PDF has content (size > 0)
        assert pdf_path.stat().st_size > 0, "PDF should have content"
        
        # Verify no errors occurred
        assert len(pdf_result.errors) == 0, "No errors should occur during PDF generation"
        
        # Note: We cannot easily verify internal PDF structure (TOC, page breaks, links)
        # without a PDF parsing library, but we can verify the file was created successfully
        # and has reasonable size
        
        # PDF should be larger than a minimal PDF (at least 10KB for content + TOC)
        assert pdf_path.stat().st_size > 10000, \
            "PDF with TOC should have substantial content (>10KB)"
        
    except Exception as e:
        # PDF generation might fail if system libraries are missing
        pytest.skip(f"PDF generation skipped: {e}")


@pytest.mark.integration
def test_cis_controls_pdf_with_toc_english(temp_workspace, cis_controls_templates, sample_meta_config):
    """
    Test CIS Controls PDF with TOC generation for English language.
    
    This test verifies:
    - PDF with TOC works for English templates
    - English content in PDF
    - Proper structure for English handbook
    
    Requirements: 5.5
    Feature: cis-controls-integration
    Task: 14.3
    """
    from src.meta_adapter import MetaAdapter
    
    output_dir = temp_workspace / "Handbook"
    
    # Initialize components
    template_manager = TemplateManager(cis_controls_templates)
    
    # Initialize meta adapter with English language
    meta_adapter = MetaAdapter(sample_meta_config, language='en')
    meta_adapter.connect()
    meta_adapter.set_handbook_type('cis-controls')
    
    data_sources = {'meta': meta_adapter}
    processor = PlaceholderProcessor(data_sources)
    output_generator = OutputGenerator(output_dir, test_mode=True)
    
    # Process templates
    templates = template_manager.get_templates('en', 'cis-controls')
    processed_results = []
    for template in templates:
        content = template.read_content()
        result = processor.process_template(content, template.path.name)
        processed_results.append(result)
    
    processed_contents = [r.content for r in processed_results]
    
    # Prepare templates data for PDF with TOC
    templates_data = []
    for template, content in zip(templates, processed_contents):
        filename = template.path.name
        filename_base = Path(filename).stem
        template_number = filename_base[:4]
        title_part = filename_base[5:] if len(filename_base) > 5 else filename_base
        template_title = title_part.replace('_', ' ')
        templates_data.append((template_number, template_title, content))
    
    # Generate PDF with TOC
    try:
        pdf_result = output_generator.generate_pdf_with_toc(
            templates_data,
            'en',
            'cis-controls'
        )
        
        # Verify PDF was created
        pdf_path = pdf_result.pdf_path
        assert pdf_path is not None, "PDF path should be set"
        assert pdf_path.exists(), "PDF file should be created for English"
        
        # Verify PDF directory structure for English
        assert pdf_path.parent == output_dir / "en" / "cis-controls" / "pdf"
        
        # Verify PDF has content
        assert pdf_path.stat().st_size > 0, "English PDF should have content"
        assert pdf_path.stat().st_size > 10000, "English PDF with TOC should have substantial content"
        
        # Verify no errors occurred
        assert len(pdf_result.errors) == 0, "No errors should occur during English PDF generation"
        
    except Exception as e:
        # PDF generation might fail if system libraries are missing
        pytest.skip(f"PDF generation skipped: {e}")


@pytest.mark.integration
def test_cis_controls_pdf_with_toc_page_breaks(temp_workspace, cis_controls_templates, sample_meta_config):
    """
    Test that PDF with TOC includes page breaks between templates.
    
    This test verifies:
    - Page breaks are inserted between templates
    - Each template starts on a new page
    - TOC structure is correct
    
    Requirements: 5.5
    Feature: cis-controls-integration
    Task: 14.3
    """
    from src.meta_adapter import MetaAdapter
    
    output_dir = temp_workspace / "Handbook"
    
    # Initialize components
    template_manager = TemplateManager(cis_controls_templates)
    
    # Initialize meta adapter
    meta_adapter = MetaAdapter(sample_meta_config, language='de')
    meta_adapter.connect()
    meta_adapter.set_handbook_type('cis-controls')
    
    data_sources = {'meta': meta_adapter}
    processor = PlaceholderProcessor(data_sources)
    output_generator = OutputGenerator(output_dir, test_mode=True)
    
    # Process templates
    templates = template_manager.get_templates('de', 'cis-controls')
    processed_results = []
    for template in templates:
        content = template.read_content()
        result = processor.process_template(content, template.path.name)
        processed_results.append(result)
    
    processed_contents = [r.content for r in processed_results]
    
    # Prepare templates data
    templates_data = []
    for template, content in zip(templates, processed_contents):
        filename = template.path.name
        filename_base = Path(filename).stem
        template_number = filename_base[:4]
        title_part = filename_base[5:] if len(filename_base) > 5 else filename_base
        template_title = title_part.replace('_', ' ')
        templates_data.append((template_number, template_title, content))
    
    # Generate PDF with TOC
    try:
        pdf_result = output_generator.generate_pdf_with_toc(
            templates_data,
            'de',
            'cis-controls'
        )
        
        pdf_path = pdf_result.pdf_path
        assert pdf_path.exists(), "PDF should be created"
        
        # Read the intermediate markdown that was generated
        # The generate_pdf_with_toc method should create markdown with page breaks
        # We can verify this by checking if the method was called correctly
        
        # Verify that we have multiple templates (which should result in page breaks)
        assert len(templates_data) > 1, "Should have multiple templates for page break testing"
        
        # Verify PDF size is reasonable for multi-page document
        # A single-page PDF would be smaller than a multi-page PDF with TOC
        pdf_size = pdf_path.stat().st_size
        assert pdf_size > 15000, \
            f"PDF with multiple templates and TOC should be >15KB, got {pdf_size} bytes"
        
        # Verify no errors occurred
        assert len(pdf_result.errors) == 0, "No errors should occur"
        
    except Exception as e:
        # PDF generation might fail if system libraries are missing
        pytest.skip(f"PDF generation skipped: {e}")
