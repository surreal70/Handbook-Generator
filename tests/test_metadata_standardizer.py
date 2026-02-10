"""
Unit tests for MetadataStandardizer.

Tests framework scanning, missing metadata detection, metadata file creation,
metadata enhancement, and validation logic.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

import pytest
from pathlib import Path
import tempfile
import shutil
from src.metadata_standardizer import (
    MetadataStandardizer,
    FrameworkStatus,
    MissingMetadata,
    ValidationResult,
    StandardizationReport
)


class TestMetadataStandardizer:
    """Unit tests for MetadataStandardizer class."""
    
    @pytest.fixture
    def temp_templates_dir(self):
        """Create a temporary templates directory for testing."""
        temp_dir = tempfile.mkdtemp()
        templates_dir = Path(temp_dir) / "templates"
        templates_dir.mkdir()
        
        # Create language directories
        (templates_dir / "de").mkdir()
        (templates_dir / "en").mkdir()
        
        yield templates_dir
        
        # Cleanup
        shutil.rmtree(temp_dir)
    
    @pytest.fixture
    def standardizer(self, temp_templates_dir):
        """Create a MetadataStandardizer instance with temp directory."""
        return MetadataStandardizer(str(temp_templates_dir))
    
    def test_init(self, temp_templates_dir):
        """Test MetadataStandardizer initialization."""
        standardizer = MetadataStandardizer(str(temp_templates_dir))
        
        assert standardizer.templates_dir == temp_templates_dir
        assert standardizer._frameworks_cache is None
    
    def test_discover_frameworks_empty(self, standardizer):
        """Test framework discovery with empty templates directory."""
        frameworks = standardizer._discover_frameworks()
        
        assert isinstance(frameworks, set)
        assert len(frameworks) == 0
    
    def test_discover_frameworks_with_frameworks(self, standardizer, temp_templates_dir):
        """Test framework discovery with multiple frameworks."""
        # Create framework directories
        (temp_templates_dir / "de" / "gdpr").mkdir()
        (temp_templates_dir / "de" / "iso-9001").mkdir()
        (temp_templates_dir / "en" / "gdpr").mkdir()
        (temp_templates_dir / "en" / "pci-dss").mkdir()
        
        frameworks = standardizer._discover_frameworks()
        
        assert isinstance(frameworks, set)
        assert "gdpr" in frameworks
        assert "iso-9001" in frameworks
        assert "pci-dss" in frameworks
        assert len(frameworks) == 3
    
    def test_discover_frameworks_excludes_service_directory(self, standardizer, temp_templates_dir):
        """Test that service-directory is excluded from framework discovery."""
        # Create framework and service directories
        (temp_templates_dir / "de" / "gdpr").mkdir()
        (temp_templates_dir / "de" / "service-directory").mkdir()
        (temp_templates_dir / "en" / "service-directory").mkdir()
        
        frameworks = standardizer._discover_frameworks()
        
        assert "gdpr" in frameworks
        assert "service-directory" not in frameworks
    
    def test_discover_frameworks_caching(self, standardizer, temp_templates_dir):
        """Test that framework discovery results are cached."""
        # Create a framework
        (temp_templates_dir / "de" / "gdpr").mkdir()
        
        # First call
        frameworks1 = standardizer._discover_frameworks()
        
        # Add another framework
        (temp_templates_dir / "de" / "iso-9001").mkdir()
        
        # Second call should return cached result
        frameworks2 = standardizer._discover_frameworks()
        
        assert frameworks1 == frameworks2
        assert "iso-9001" not in frameworks2  # Not in cache
    
    def test_get_metadata_path(self, standardizer, temp_templates_dir):
        """Test metadata file path generation."""
        path = standardizer._get_metadata_path("gdpr", "de")
        
        expected = temp_templates_dir / "de" / "gdpr" / "0000_metadata_de_gdpr.md"
        assert path == expected
    
    def test_detect_missing_metadata_empty(self, standardizer):
        """Test missing metadata detection with no frameworks."""
        missing = standardizer.detect_missing_metadata()
        
        assert isinstance(missing, list)
        assert len(missing) == 0
    
    def test_detect_missing_metadata_all_missing(self, standardizer, temp_templates_dir):
        """Test missing metadata detection when all metadata files are missing."""
        # Create framework directories without metadata files
        (temp_templates_dir / "de" / "gdpr").mkdir()
        (temp_templates_dir / "en" / "gdpr").mkdir()
        
        missing = standardizer.detect_missing_metadata()
        
        assert len(missing) == 2
        assert any(m.framework == "gdpr" and m.language == "de" for m in missing)
        assert any(m.framework == "gdpr" and m.language == "en" for m in missing)
    
    def test_detect_missing_metadata_partial(self, standardizer, temp_templates_dir):
        """Test missing metadata detection when some metadata files exist."""
        # Create framework directory
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir()
        
        # Create only German metadata
        metadata_file = gdpr_de_dir / "0000_metadata_de_gdpr.md"
        metadata_file.write_text("# Test Metadata", encoding='utf-8')
        
        (temp_templates_dir / "en" / "gdpr").mkdir()
        
        missing = standardizer.detect_missing_metadata()
        
        assert len(missing) == 1
        assert missing[0].framework == "gdpr"
        assert missing[0].language == "en"
    
    def test_validate_metadata_structure_missing_file(self, standardizer):
        """Test validation of non-existent metadata file."""
        result = standardizer.validate_metadata_structure("/nonexistent/file.md")
        
        assert isinstance(result, ValidationResult)
        assert not result.is_valid
        assert len(result.missing_fields) == len(standardizer.REQUIRED_FIELDS)
        assert len(result.warnings) > 0
    
    def test_validate_metadata_structure_complete(self, standardizer, temp_templates_dir):
        """Test validation of complete metadata file."""
        # Create a complete metadata file
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir()
        
        metadata_file = gdpr_de_dir / "0000_metadata_de_gdpr.md"
        metadata_content = """# GDPR Handbuch - Metadaten

**Dokument-ID:** 0000  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** {{ meta.status }}  
**Klassifizierung:** {{ meta.classification }}  
**Letzte Aktualisierung:** {{ meta.date }}  
**Template-Version:** 1.0  
**Revision:** 0  

---

## Handbuch-Informationen

**Handbuch-Titel:** GDPR Datenschutz-Handbuch  
**Organisation:** {{ meta.organization }}  
**Autor:** {{ meta.author }}  
**Geltungsbereich:** {{ meta.scope }}  
**Gültig ab:** {{ meta.valid_from }}  
**Nächste Überprüfung:** {{ meta.next_review }}  

---

## Dokumentenzweck

Test purpose

## Geltungsbereich

Test scope

## Normative Verweise

- GDPR

## Änderungshistorie

| Version | Datum | Autor | Änderung |
|---------|-------|-------|----------|
| 1.0 | 2025-01-01 | Test | Initial |
"""
        metadata_file.write_text(metadata_content, encoding='utf-8')
        
        result = standardizer.validate_metadata_structure(str(metadata_file))
        
        assert isinstance(result, ValidationResult)
        assert result.is_valid
        assert len(result.missing_fields) == 0
        assert len(result.invalid_fields) == 0
    
    def test_validate_metadata_structure_missing_fields(self, standardizer, temp_templates_dir):
        """Test validation of metadata file with missing fields."""
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir()
        
        metadata_file = gdpr_de_dir / "0000_metadata_de_gdpr.md"
        metadata_content = """# GDPR Handbuch - Metadaten

**Dokument-ID:** 0000  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
"""
        metadata_file.write_text(metadata_content, encoding='utf-8')
        
        result = standardizer.validate_metadata_structure(str(metadata_file))
        
        assert not result.is_valid
        assert "status" in result.missing_fields
        assert "template_version" in result.missing_fields
        assert "revision" in result.missing_fields
    
    def test_validate_metadata_structure_invalid_version_format(self, standardizer, temp_templates_dir):
        """Test validation of metadata file with invalid template_version format."""
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir()
        
        metadata_file = gdpr_de_dir / "0000_metadata_de_gdpr.md"
        metadata_content = """# GDPR Handbuch - Metadaten

**Dokument-ID:** 0000  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** {{ meta.status }}  
**Klassifizierung:** {{ meta.classification }}  
**Letzte Aktualisierung:** {{ meta.date }}  
**Template-Version:** invalid  
**Revision:** 0  

## Handbuch-Informationen

**Organisation:** {{ meta.organization }}  
**Autor:** {{ meta.author }}  
**Geltungsbereich:** {{ meta.scope }}  
**Gültig ab:** {{ meta.valid_from }}  
**Nächste Überprüfung:** {{ meta.next_review }}  
"""
        metadata_file.write_text(metadata_content, encoding='utf-8')
        
        result = standardizer.validate_metadata_structure(str(metadata_file))
        
        assert not result.is_valid
        assert any("template_version" in field for field in result.invalid_fields)
    
    def test_validate_metadata_structure_invalid_revision(self, standardizer, temp_templates_dir):
        """Test validation of metadata file with invalid revision number."""
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir()
        
        metadata_file = gdpr_de_dir / "0000_metadata_de_gdpr.md"
        metadata_content = """# GDPR Handbuch - Metadaten

**Dokument-ID:** 0000  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** {{ meta.status }}  
**Klassifizierung:** {{ meta.classification }}  
**Letzte Aktualisierung:** {{ meta.date }}  
**Template-Version:** 1.0  
**Revision:** not_a_number  

## Handbuch-Informationen

**Organisation:** {{ meta.organization }}  
**Autor:** {{ meta.author }}  
**Geltungsbereich:** {{ meta.scope }}  
**Gültig ab:** {{ meta.valid_from }}  
**Nächste Überprüfung:** {{ meta.next_review }}  
"""
        metadata_file.write_text(metadata_content, encoding='utf-8')
        
        result = standardizer.validate_metadata_structure(str(metadata_file))
        
        assert not result.is_valid
        assert any("revision" in field for field in result.invalid_fields)
    
    def test_scan_frameworks(self, standardizer, temp_templates_dir):
        """Test complete framework scanning."""
        # Create framework with complete metadata
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir()
        
        metadata_file = gdpr_de_dir / "0000_metadata_de_gdpr.md"
        complete_metadata = """# GDPR Handbuch - Metadaten

**Dokument-ID:** 0000  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** {{ meta.status }}  
**Klassifizierung:** {{ meta.classification }}  
**Letzte Aktualisierung:** {{ meta.date }}  
**Template-Version:** 1.0  
**Revision:** 0  

## Handbuch-Informationen

**Organisation:** {{ meta.organization }}  
**Autor:** {{ meta.author }}  
**Geltungsbereich:** {{ meta.scope }}  
**Gültig ab:** {{ meta.valid_from }}  
**Nächste Überprüfung:** {{ meta.next_review }}  
"""
        metadata_file.write_text(complete_metadata, encoding='utf-8')
        
        # Create English directory without metadata
        (temp_templates_dir / "en" / "gdpr").mkdir()
        
        status = standardizer.scan_frameworks()
        
        assert "gdpr" in status
        assert status["gdpr"].has_de_metadata
        assert status["gdpr"].de_metadata_complete
        assert not status["gdpr"].has_en_metadata
        assert not status["gdpr"].en_metadata_complete
    
    def test_generate_report(self, standardizer, temp_templates_dir):
        """Test report generation."""
        # Create a framework with metadata
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir()
        
        metadata_file = gdpr_de_dir / "0000_metadata_de_gdpr.md"
        metadata_file.write_text("# Test", encoding='utf-8')
        
        report = standardizer.generate_report()
        
        assert isinstance(report, StandardizationReport)
        assert report.total_frameworks >= 0
        assert isinstance(report.summary, str)
        assert len(report.summary) > 0
    
    def test_create_metadata_file_success(self, standardizer, temp_templates_dir):
        """Test successful metadata file creation."""
        # Create framework directory
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir()
        
        result = standardizer.create_metadata_file("gdpr", "de")
        
        assert result is True
        
        # Verify file was created
        metadata_path = standardizer._get_metadata_path("gdpr", "de")
        assert metadata_path.exists()
        
        # Verify content
        content = metadata_path.read_text(encoding='utf-8')
        assert "Template-Version: 1.0" in content or "Template Version: 1.0" in content
        assert "Revision: 0" in content or "**Revision:** 0" in content
    
    def test_create_metadata_file_already_exists(self, standardizer, temp_templates_dir):
        """Test metadata file creation when file already exists."""
        # Create framework directory and metadata file
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir()
        
        metadata_path = standardizer._get_metadata_path("gdpr", "de")
        metadata_path.write_text("# Existing", encoding='utf-8')
        
        with pytest.raises(FileExistsError):
            standardizer.create_metadata_file("gdpr", "de")
    
    def test_create_metadata_file_invalid_language(self, standardizer):
        """Test metadata file creation with invalid language."""
        with pytest.raises(ValueError):
            standardizer.create_metadata_file("gdpr", "fr")
    
    def test_enhance_existing_metadata_success(self, standardizer, temp_templates_dir):
        """Test successful metadata enhancement."""
        # Create framework directory with incomplete metadata
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir()
        
        metadata_file = gdpr_de_dir / "0000_metadata_de_gdpr.md"
        incomplete_metadata = """# GDPR Handbuch - Metadaten

**Dokument-ID:** 0000  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
"""
        metadata_file.write_text(incomplete_metadata, encoding='utf-8')
        
        result = standardizer.enhance_existing_metadata(str(metadata_file))
        
        assert result is True
        
        # Verify enhanced content
        content = metadata_file.read_text(encoding='utf-8')
        assert "Template-Version" in content or "Template Version" in content
        assert "Revision" in content
    
    def test_enhance_existing_metadata_already_complete(self, standardizer, temp_templates_dir):
        """Test metadata enhancement when file is already complete."""
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir()
        
        metadata_file = gdpr_de_dir / "0000_metadata_de_gdpr.md"
        complete_metadata = """# GDPR Handbuch - Metadaten

**Dokument-ID:** 0000  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** {{ meta.status }}  
**Klassifizierung:** {{ meta.classification }}  
**Letzte Aktualisierung:** {{ meta.date }}  
**Template-Version:** 1.0  
**Revision:** 0  

## Handbuch-Informationen

**Organisation:** {{ meta.organization }}  
**Autor:** {{ meta.author }}  
**Geltungsbereich:** {{ meta.scope }}  
**Gültig ab:** {{ meta.valid_from }}  
**Nächste Überprüfung:** {{ meta.next_review }}  
"""
        metadata_file.write_text(complete_metadata, encoding='utf-8')
        
        result = standardizer.enhance_existing_metadata(str(metadata_file))
        
        assert result is True
    
    def test_enhance_existing_metadata_file_not_found(self, standardizer):
        """Test metadata enhancement with non-existent file."""
        with pytest.raises(FileNotFoundError):
            standardizer.enhance_existing_metadata("/nonexistent/file.md")
    
    def test_field_exists(self, standardizer):
        """Test field existence checking."""
        content = """
**Dokument-ID:** 0000
**Owner:** {{ meta.owner }}
Template-Version: 1.0
"""
        
        assert standardizer._field_exists(content, "document_id", ["Dokument-ID"])
        assert standardizer._field_exists(content, "owner", ["Owner"])
        assert standardizer._field_exists(content, "template_version", ["Template-Version"])
        assert not standardizer._field_exists(content, "status", ["Status"])
    
    def test_extract_field_value(self, standardizer):
        """Test field value extraction."""
        content = """
**Dokument-ID:** 0000
**Template-Version:** 1.0
Revision: 5
"""
        
        value1 = standardizer._extract_field_value(content, ["Dokument-ID"])
        assert value1 == "0000"
        
        value2 = standardizer._extract_field_value(content, ["Template-Version"])
        assert value2 == "1.0"
        
        value3 = standardizer._extract_field_value(content, ["Revision"])
        assert value3 == "5"
        
        value4 = standardizer._extract_field_value(content, ["Nonexistent"])
        assert value4 is None
    
    def test_get_field_labels(self, standardizer):
        """Test field label retrieval."""
        labels = standardizer._get_field_labels("document_id")
        assert "Dokument-ID" in labels
        assert "Document-ID" in labels
        
        labels = standardizer._get_field_labels("organization")
        assert "Organisation" in labels
        assert "Organization" in labels
    
    def test_get_field_label(self, standardizer):
        """Test field label generation for specific language."""
        label_de = standardizer._get_field_label("document_id", "de")
        assert label_de == "Dokument-ID"
        
        label_en = standardizer._get_field_label("document_id", "en")
        assert label_en == "Document-ID"
        
        label_de = standardizer._get_field_label("organization", "de")
        assert label_de == "Organisation"
        
        label_en = standardizer._get_field_label("organization", "en")
        assert label_en == "Organization"
    
    def test_get_field_placeholder(self, standardizer):
        """Test field placeholder generation."""
        placeholder = standardizer._get_field_placeholder("owner")
        assert placeholder == "{{ meta.owner }}"
        
        placeholder = standardizer._get_field_placeholder("template_version")
        assert placeholder == "1.0"
        
        placeholder = standardizer._get_field_placeholder("revision")
        assert placeholder == "0"


class TestDocumentHistoryStandardizer:
    """Unit tests for DocumentHistoryStandardizer class."""
    
    @pytest.fixture
    def temp_templates_dir(self):
        """Create a temporary templates directory for testing."""
        temp_dir = tempfile.mkdtemp()
        templates_dir = Path(temp_dir) / "templates"
        templates_dir.mkdir()
        
        # Create language directories
        (templates_dir / "de").mkdir()
        (templates_dir / "en").mkdir()
        
        yield templates_dir
        
        # Cleanup
        shutil.rmtree(temp_dir)
    
    @pytest.fixture
    def doc_history_standardizer(self, temp_templates_dir):
        """Create a DocumentHistoryStandardizer instance with temp directory."""
        from src.metadata_standardizer import DocumentHistoryStandardizer
        return DocumentHistoryStandardizer(str(temp_templates_dir))
    
    def test_init(self, temp_templates_dir):
        """Test DocumentHistoryStandardizer initialization."""
        from src.metadata_standardizer import DocumentHistoryStandardizer
        standardizer = DocumentHistoryStandardizer(str(temp_templates_dir))
        
        assert standardizer.templates_dir == temp_templates_dir
    
    def test_scan_template_files_empty(self, doc_history_standardizer):
        """Test scanning template files with empty directory."""
        files = doc_history_standardizer.scan_template_files()
        
        assert isinstance(files, list)
        assert len(files) == 0
    
    def test_scan_template_files_with_templates(self, doc_history_standardizer, temp_templates_dir):
        """Test scanning template files with multiple templates."""
        # Create framework directories and template files
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir(parents=True)
        
        # Create template files
        (gdpr_de_dir / "0001_introduction.md").write_text("# Introduction", encoding='utf-8')
        (gdpr_de_dir / "0002_scope.md").write_text("# Scope", encoding='utf-8')
        
        # Create metadata file (should be excluded)
        (gdpr_de_dir / "0000_metadata_de_gdpr.md").write_text("# Metadata", encoding='utf-8')
        
        iso_en_dir = temp_templates_dir / "en" / "iso-9001"
        iso_en_dir.mkdir(parents=True)
        (iso_en_dir / "0001_quality.md").write_text("# Quality", encoding='utf-8')
        
        files = doc_history_standardizer.scan_template_files()
        
        assert len(files) == 3
        assert any("0001_introduction.md" in f for f in files)
        assert any("0002_scope.md" in f for f in files)
        assert any("0001_quality.md" in f for f in files)
        # Metadata file should be excluded
        assert not any("0000_metadata_de_gdpr.md" in f for f in files)
    
    def test_scan_template_files_excludes_metadata(self, doc_history_standardizer, temp_templates_dir):
        """Test that metadata files are excluded from scanning."""
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir(parents=True)
        
        # Create metadata file
        (gdpr_de_dir / "0000_metadata_de_gdpr.md").write_text("# Metadata", encoding='utf-8')
        
        # Create regular template
        (gdpr_de_dir / "0001_template.md").write_text("# Template", encoding='utf-8')
        
        files = doc_history_standardizer.scan_template_files()
        
        assert len(files) == 1
        assert "0001_template.md" in files[0]
        assert not any("0000_metadata" in f for f in files)
    
    def test_has_document_history_missing_file(self, doc_history_standardizer):
        """Test document history detection with non-existent file."""
        result = doc_history_standardizer.has_document_history("/nonexistent/file.md")
        
        assert result is False
    
    def test_has_document_history_no_history(self, doc_history_standardizer, temp_templates_dir):
        """Test document history detection when no history section exists."""
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir(parents=True)
        
        template_file = gdpr_de_dir / "0001_template.md"
        template_file.write_text("# Template\n\nSome content", encoding='utf-8')
        
        result = doc_history_standardizer.has_document_history(str(template_file))
        
        assert result is False
    
    def test_has_document_history_with_german_history(self, doc_history_standardizer, temp_templates_dir):
        """Test document history detection with German history section."""
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir(parents=True)
        
        template_file = gdpr_de_dir / "0001_template.md"
        content = """# Template

Some content

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | 2025-01-01 | Test | Initiale Erstellung |
"""
        template_file.write_text(content, encoding='utf-8')
        
        result = doc_history_standardizer.has_document_history(str(template_file))
        
        assert result is True
    
    def test_has_document_history_with_english_history(self, doc_history_standardizer, temp_templates_dir):
        """Test document history detection with English history section."""
        iso_en_dir = temp_templates_dir / "en" / "iso-9001"
        iso_en_dir.mkdir(parents=True)
        
        template_file = iso_en_dir / "0001_template.md"
        content = """# Template

Some content

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2025-01-01 | Test | Initial Creation |
"""
        template_file.write_text(content, encoding='utf-8')
        
        result = doc_history_standardizer.has_document_history(str(template_file))
        
        assert result is True
    
    def test_has_document_history_with_header_format(self, doc_history_standardizer, temp_templates_dir):
        """Test document history detection with ## header format."""
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir(parents=True)
        
        template_file = gdpr_de_dir / "0001_template.md"
        content = """# Template

Some content

## Dokumenthistorie

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | 2025-01-01 | Test | Initiale Erstellung |
"""
        template_file.write_text(content, encoding='utf-8')
        
        result = doc_history_standardizer.has_document_history(str(template_file))
        
        assert result is True
    
    def test_generate_history_section_german(self, doc_history_standardizer):
        """Test document history section generation for German."""
        section = doc_history_standardizer.generate_history_section('de')
        
        assert '**Dokumenthistorie:**' in section
        assert '| Version | Datum | Autor | Änderungen |' in section
        assert '| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initiale Erstellung |' in section
    
    def test_generate_history_section_english(self, doc_history_standardizer):
        """Test document history section generation for English."""
        section = doc_history_standardizer.generate_history_section('en')
        
        assert '**Document History:**' in section
        assert '| Version | Date | Author | Changes |' in section
        assert '| 0.1 | {{ meta.document.last_updated }} | {{ meta.defaults.author }} | Initial Creation |' in section
    
    def test_add_document_history_success(self, doc_history_standardizer, temp_templates_dir):
        """Test successful document history addition."""
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir(parents=True)
        
        template_file = gdpr_de_dir / "0001_template.md"
        template_file.write_text("# Template\n\nSome content", encoding='utf-8')
        
        result = doc_history_standardizer.add_document_history(str(template_file), 'de')
        
        assert result is True
        
        # Verify content
        content = template_file.read_text(encoding='utf-8')
        assert '**Dokumenthistorie:**' in content
        assert '| Version | Datum | Autor | Änderungen |' in content
        assert '| 0.1 |' in content
    
    def test_add_document_history_with_end_marker(self, doc_history_standardizer, temp_templates_dir):
        """Test document history addition with end marker."""
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir(parents=True)
        
        template_file = gdpr_de_dir / "0001_template.md"
        content = """# Template

Some content

<!-- End of template -->
"""
        template_file.write_text(content, encoding='utf-8')
        
        result = doc_history_standardizer.add_document_history(str(template_file), 'de')
        
        assert result is True
        
        # Verify history is before end marker
        new_content = template_file.read_text(encoding='utf-8')
        assert '**Dokumenthistorie:**' in new_content
        
        # Check that history comes before end marker
        history_pos = new_content.find('**Dokumenthistorie:**')
        marker_pos = new_content.find('<!-- End of template -->')
        assert history_pos < marker_pos
    
    def test_add_document_history_skips_metadata_files(self, doc_history_standardizer, temp_templates_dir):
        """Test that document history addition skips metadata files."""
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir(parents=True)
        
        metadata_file = gdpr_de_dir / "0000_metadata_de_gdpr.md"
        metadata_file.write_text("# Metadata", encoding='utf-8')
        
        result = doc_history_standardizer.add_document_history(str(metadata_file), 'de')
        
        assert result is False
        
        # Verify content unchanged
        content = metadata_file.read_text(encoding='utf-8')
        assert '**Dokumenthistorie:**' not in content
    
    def test_add_document_history_preserves_existing_content(self, doc_history_standardizer, temp_templates_dir):
        """Test that document history addition preserves existing content."""
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir(parents=True)
        
        template_file = gdpr_de_dir / "0001_template.md"
        original_content = """# Template Title

## Section 1

Some important content here.

## Section 2

More content.
"""
        template_file.write_text(original_content, encoding='utf-8')
        
        result = doc_history_standardizer.add_document_history(str(template_file), 'de')
        
        assert result is True
        
        # Verify original content is preserved
        new_content = template_file.read_text(encoding='utf-8')
        assert '# Template Title' in new_content
        assert '## Section 1' in new_content
        assert 'Some important content here.' in new_content
        assert '## Section 2' in new_content
        assert 'More content.' in new_content
        assert '**Dokumenthistorie:**' in new_content
    
    def test_add_document_history_already_exists(self, doc_history_standardizer, temp_templates_dir):
        """Test document history addition when history already exists."""
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir(parents=True)
        
        template_file = gdpr_de_dir / "0001_template.md"
        content = """# Template

Some content

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | 2025-01-01 | Test | Initiale Erstellung |
"""
        template_file.write_text(content, encoding='utf-8')
        
        result = doc_history_standardizer.add_document_history(str(template_file), 'de')
        
        # Should return True (already has history)
        assert result is True
    
    def test_add_document_history_file_not_found(self, doc_history_standardizer):
        """Test document history addition with non-existent file."""
        result = doc_history_standardizer.add_document_history("/nonexistent/file.md", 'de')
        
        assert result is False
    
    def test_add_document_history_english(self, doc_history_standardizer, temp_templates_dir):
        """Test document history addition for English template."""
        iso_en_dir = temp_templates_dir / "en" / "iso-9001"
        iso_en_dir.mkdir(parents=True)
        
        template_file = iso_en_dir / "0001_template.md"
        template_file.write_text("# Template\n\nSome content", encoding='utf-8')
        
        result = doc_history_standardizer.add_document_history(str(template_file), 'en')
        
        assert result is True
        
        # Verify English content
        content = template_file.read_text(encoding='utf-8')
        assert '**Document History:**' in content
        assert '| Version | Date | Author | Changes |' in content
        assert '| 0.1 |' in content
        assert 'Initial Creation' in content
    
    def test_validate_document_history_format_missing_file(self, doc_history_standardizer):
        """Test document history format validation with non-existent file."""
        result = doc_history_standardizer.validate_document_history_format("/nonexistent/file.md")
        
        assert isinstance(result, ValidationResult)
        assert not result.is_valid
        assert len(result.warnings) > 0
    
    def test_validate_document_history_format_skips_metadata(self, doc_history_standardizer, temp_templates_dir):
        """Test that validation skips metadata files."""
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir(parents=True)
        
        metadata_file = gdpr_de_dir / "0000_metadata_de_gdpr.md"
        metadata_file.write_text("# Metadata", encoding='utf-8')
        
        result = doc_history_standardizer.validate_document_history_format(str(metadata_file))
        
        assert result.is_valid
        assert any("Skipped metadata file" in w for w in result.warnings)
    
    def test_validate_document_history_format_no_history(self, doc_history_standardizer, temp_templates_dir):
        """Test validation when no document history section exists."""
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir(parents=True)
        
        template_file = gdpr_de_dir / "0001_template.md"
        template_file.write_text("# Template\n\nSome content", encoding='utf-8')
        
        result = doc_history_standardizer.validate_document_history_format(str(template_file))
        
        # Should return True (warning, not error for backward compatibility)
        assert result.is_valid
        assert any("Missing document history section" in w for w in result.warnings)
    
    def test_validate_document_history_format_valid_german(self, doc_history_standardizer, temp_templates_dir):
        """Test validation of valid German document history."""
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir(parents=True)
        
        template_file = gdpr_de_dir / "0001_template.md"
        content = """# Template

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | 2025-01-01 | Test | Initiale Erstellung |
"""
        template_file.write_text(content, encoding='utf-8')
        
        result = doc_history_standardizer.validate_document_history_format(str(template_file))
        
        assert result.is_valid
        assert len(result.warnings) == 0
    
    def test_validate_document_history_format_valid_english(self, doc_history_standardizer, temp_templates_dir):
        """Test validation of valid English document history."""
        iso_en_dir = temp_templates_dir / "en" / "iso-9001"
        iso_en_dir.mkdir(parents=True)
        
        template_file = iso_en_dir / "0001_template.md"
        content = """# Template

**Document History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2025-01-01 | Test | Initial Creation |
"""
        template_file.write_text(content, encoding='utf-8')
        
        result = doc_history_standardizer.validate_document_history_format(str(template_file))
        
        assert result.is_valid
        assert len(result.warnings) == 0
    
    def test_validate_document_history_format_invalid_headers(self, doc_history_standardizer, temp_templates_dir):
        """Test validation with invalid table headers."""
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir(parents=True)
        
        template_file = gdpr_de_dir / "0001_template.md"
        content = """# Template

**Dokumenthistorie:**

| Ver | Date | Who | What |
|-----|------|-----|------|
| 0.1 | 2025-01-01 | Test | Initial |
"""
        template_file.write_text(content, encoding='utf-8')
        
        result = doc_history_standardizer.validate_document_history_format(str(template_file))
        
        # Should still be valid (warning only)
        assert result.is_valid
        assert any("table headers do not match" in w for w in result.warnings)
    
    def test_validate_document_history_format_missing_version(self, doc_history_standardizer, temp_templates_dir):
        """Test validation when initial version 0.1 is missing."""
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir(parents=True)
        
        template_file = gdpr_de_dir / "0001_template.md"
        content = """# Template

**Dokumenthistorie:**

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 1.0 | 2025-01-01 | Test | First release |
"""
        template_file.write_text(content, encoding='utf-8')
        
        result = doc_history_standardizer.validate_document_history_format(str(template_file))
        
        # Should still be valid (warning only)
        assert result.is_valid
        assert any("missing initial version 0.1" in w for w in result.warnings)
    
    def test_validate_document_history_format_header_format(self, doc_history_standardizer, temp_templates_dir):
        """Test validation with ## header format."""
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir(parents=True)
        
        template_file = gdpr_de_dir / "0001_template.md"
        content = """# Template

## Dokumenthistorie

| Version | Datum | Autor | Änderungen |
|---------|-------|-------|------------|
| 0.1 | 2025-01-01 | Test | Initiale Erstellung |
"""
        template_file.write_text(content, encoding='utf-8')
        
        result = doc_history_standardizer.validate_document_history_format(str(template_file))
        
        assert result.is_valid
        assert len(result.warnings) == 0
