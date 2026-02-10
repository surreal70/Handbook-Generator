"""
Unit tests for MetadataValidator (validation script).

Tests required fields check, template_version format validation, revision number
validation, placeholder syntax validation, and bilingual consistency check.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

import pytest
from pathlib import Path
import tempfile
import shutil
import sys

# Add helpers directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'helpers'))

from validate_metadata import MetadataValidator, ValidationError, ValidationReport


class TestMetadataValidator:
    """Unit tests for MetadataValidator class."""
    
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
    def validator(self, temp_templates_dir):
        """Create a MetadataValidator instance with temp directory."""
        return MetadataValidator(str(temp_templates_dir))
    
    def test_init(self, temp_templates_dir):
        """Test MetadataValidator initialization."""
        validator = MetadataValidator(str(temp_templates_dir))
        
        assert validator.templates_dir == temp_templates_dir
        assert validator.standardizer is not None
    
    def test_validate_all_empty(self, validator):
        """Test validate_all with no frameworks."""
        report = validator.validate_all()
        
        assert isinstance(report, ValidationReport)
        assert report.total_frameworks == 0
        assert report.total_files == 0
        assert report.valid_files == 0
        assert report.invalid_files == 0
    
    def test_validate_all_with_valid_metadata(self, validator, temp_templates_dir):
        """Test validate_all with valid metadata files."""
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

---

## Handbuch-Informationen

**Organisation:** {{ meta.organization }}  
**Autor:** {{ meta.author }}  
**Geltungsbereich:** {{ meta.scope }}  
**Gültig ab:** {{ meta.valid_from }}  
**Nächste Überprüfung:** {{ meta.next_review }}  
"""
        metadata_file.write_text(complete_metadata, encoding='utf-8')
        
        # Create English version
        gdpr_en_dir = temp_templates_dir / "en" / "gdpr"
        gdpr_en_dir.mkdir()
        
        en_metadata_file = gdpr_en_dir / "0000_metadata_en_gdpr.md"
        en_complete_metadata = """# GDPR Handbook - Metadata

**Document-ID:** 0000  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Status:** {{ meta.status }}  
**Classification:** {{ meta.classification }}  
**Last Updated:** {{ meta.date }}  
**Template Version:** 1.0  
**Revision:** 0  

---

## Handbook Information

**Organization:** {{ meta.organization }}  
**Author:** {{ meta.author }}  
**Scope:** {{ meta.scope }}  
**Valid from:** {{ meta.valid_from }}  
**Next Review:** {{ meta.next_review }}  
"""
        en_metadata_file.write_text(en_complete_metadata, encoding='utf-8')
        
        report = validator.validate_all()
        
        assert report.total_frameworks == 1
        assert report.total_files == 2
        assert report.valid_files == 2
        assert report.invalid_files == 0
        assert report.success_rate == 100.0
    
    def test_validate_all_with_invalid_metadata(self, validator, temp_templates_dir):
        """Test validate_all with invalid metadata files."""
        # Create framework with incomplete metadata
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir()
        
        metadata_file = gdpr_de_dir / "0000_metadata_de_gdpr.md"
        incomplete_metadata = """# GDPR Handbuch - Metadaten

**Dokument-ID:** 0000  
**Owner:** {{ meta.owner }}  
"""
        metadata_file.write_text(incomplete_metadata, encoding='utf-8')
        
        (temp_templates_dir / "en" / "gdpr").mkdir()
        
        report = validator.validate_all()
        
        assert report.total_frameworks == 1
        assert report.invalid_files > 0
        assert len(report.errors) > 0
    
    def test_validate_framework(self, validator, temp_templates_dir):
        """Test validate_framework for specific framework."""
        # Create framework
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir()
        
        metadata_file = gdpr_de_dir / "0000_metadata_de_gdpr.md"
        metadata_file.write_text("# Test", encoding='utf-8')
        
        (temp_templates_dir / "en" / "gdpr").mkdir()
        
        report = validator.validate_framework("gdpr")
        
        assert isinstance(report, ValidationReport)
        assert report.total_frameworks == 1
    
    def test_validate_language(self, validator, temp_templates_dir):
        """Test validate_language for specific language."""
        # Create framework
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir()
        
        metadata_file = gdpr_de_dir / "0000_metadata_de_gdpr.md"
        metadata_file.write_text("# Test", encoding='utf-8')
        
        report = validator.validate_language("de")
        
        assert isinstance(report, ValidationReport)
        assert report.total_files >= 1
    
    def test_validate_placeholder_syntax_valid(self, validator):
        """Test placeholder syntax validation with valid placeholders."""
        content = """
**Owner:** {{ meta.owner }}
**Version:** {{ meta.version }}
**Organization:** {{ meta.organization }}
"""
        
        malformed = validator.validate_placeholder_syntax(content)
        
        assert len(malformed) == 0
    
    def test_validate_placeholder_syntax_malformed(self, validator):
        """Test placeholder syntax validation with malformed placeholders."""
        content = """
**Owner:** {{ meta.owner }}
**Invalid1:** {{meta.field}}
**Invalid2:** {{ meta }}
**Invalid3:** {{ field }}
**Valid:** {{ meta.valid }}
"""
        
        malformed = validator.validate_placeholder_syntax(content)
        
        # Should find malformed placeholders (no space, missing parts)
        assert len(malformed) > 0
    
    def test_check_bilingual_consistency_both_missing(self, validator, temp_templates_dir):
        """Test bilingual consistency check when both files are missing."""
        (temp_templates_dir / "de" / "gdpr").mkdir()
        (temp_templates_dir / "en" / "gdpr").mkdir()
        
        inconsistencies = validator.check_bilingual_consistency("gdpr")
        
        assert len(inconsistencies) > 0
        assert any("missing" in inc.lower() for inc in inconsistencies)
    
    def test_check_bilingual_consistency_one_missing(self, validator, temp_templates_dir):
        """Test bilingual consistency check when one file is missing."""
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir()
        
        metadata_file = gdpr_de_dir / "0000_metadata_de_gdpr.md"
        metadata_file.write_text("# Test", encoding='utf-8')
        
        (temp_templates_dir / "en" / "gdpr").mkdir()
        
        inconsistencies = validator.check_bilingual_consistency("gdpr")
        
        assert len(inconsistencies) > 0
        assert any("English metadata file missing" in inc for inc in inconsistencies)
    
    def test_check_bilingual_consistency_matching(self, validator, temp_templates_dir):
        """Test bilingual consistency check with matching files."""
        # Create German metadata
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir()
        
        de_metadata = """# GDPR Handbuch - Metadaten

**Dokument-ID:** 0000  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Template-Version:** 1.0  
**Revision:** 0  

## Handbuch-Informationen

**Organisation:** {{ meta.organization }}  
"""
        (gdpr_de_dir / "0000_metadata_de_gdpr.md").write_text(de_metadata, encoding='utf-8')
        
        # Create English metadata with same structure
        gdpr_en_dir = temp_templates_dir / "en" / "gdpr"
        gdpr_en_dir.mkdir()
        
        en_metadata = """# GDPR Handbook - Metadata

**Document-ID:** 0000  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Template Version:** 1.0  
**Revision:** 0  

## Handbook Information

**Organization:** {{ meta.organization }}  
"""
        (gdpr_en_dir / "0000_metadata_en_gdpr.md").write_text(en_metadata, encoding='utf-8')
        
        inconsistencies = validator.check_bilingual_consistency("gdpr")
        
        # Should have no or minimal inconsistencies
        assert len(inconsistencies) == 0 or all("section" not in inc.lower() for inc in inconsistencies)
    
    def test_check_bilingual_consistency_different_fields(self, validator, temp_templates_dir):
        """Test bilingual consistency check with different fields."""
        # Create German metadata
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir()
        
        de_metadata = """# GDPR Handbuch - Metadaten

**Dokument-ID:** 0000  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
**Extra-Field:** {{ meta.extra }}  
"""
        (gdpr_de_dir / "0000_metadata_de_gdpr.md").write_text(de_metadata, encoding='utf-8')
        
        # Create English metadata without extra field
        gdpr_en_dir = temp_templates_dir / "en" / "gdpr"
        gdpr_en_dir.mkdir()
        
        en_metadata = """# GDPR Handbook - Metadata

**Document-ID:** 0000  
**Owner:** {{ meta.owner }}  
**Version:** {{ meta.version }}  
"""
        (gdpr_en_dir / "0000_metadata_en_gdpr.md").write_text(en_metadata, encoding='utf-8')
        
        inconsistencies = validator.check_bilingual_consistency("gdpr")
        
        assert len(inconsistencies) > 0
        assert any("Fields in DE but not in EN" in inc for inc in inconsistencies)
    
    def test_check_bilingual_consistency_different_placeholders(self, validator, temp_templates_dir):
        """Test bilingual consistency check with different placeholders."""
        # Create German metadata
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir()
        
        de_metadata = """# GDPR Handbuch - Metadaten

**Owner:** {{ meta.owner }}  
**Extra:** {{ meta.extra }}  
"""
        (gdpr_de_dir / "0000_metadata_de_gdpr.md").write_text(de_metadata, encoding='utf-8')
        
        # Create English metadata without extra placeholder
        gdpr_en_dir = temp_templates_dir / "en" / "gdpr"
        gdpr_en_dir.mkdir()
        
        en_metadata = """# GDPR Handbook - Metadata

**Owner:** {{ meta.owner }}  
"""
        (gdpr_en_dir / "0000_metadata_en_gdpr.md").write_text(en_metadata, encoding='utf-8')
        
        inconsistencies = validator.check_bilingual_consistency("gdpr")
        
        assert len(inconsistencies) > 0
        assert any("Placeholders in DE but not in EN" in inc for inc in inconsistencies)
    
    def test_extract_fields(self, validator):
        """Test field extraction from metadata content."""
        content = """
**Dokument-ID:** 0000
**Owner:** {{ meta.owner }}
**Version:** 1.0
**Template-Version:** 1.0
"""
        
        fields = validator._extract_fields(content)
        
        assert "document_id" in fields
        assert "owner" in fields
        assert "version" in fields
        assert "template_version" in fields
    
    def test_normalize_field_name(self, validator):
        """Test field name normalization."""
        assert validator._normalize_field_name("Dokument-ID") == "document_id"
        assert validator._normalize_field_name("Document-ID") == "document_id"
        assert validator._normalize_field_name("Organisation") == "organization"
        assert validator._normalize_field_name("Organization") == "organization"
        assert validator._normalize_field_name("Template-Version") == "template_version"
        assert validator._normalize_field_name("Template Version") == "template_version"
    
    def test_extract_sections(self, validator):
        """Test section extraction from metadata content."""
        content = """# Title

## Section 1

Content 1

## Section 2

Content 2

## Section 3

Content 3
"""
        
        sections = validator._extract_sections(content)
        
        assert len(sections) == 3
        assert "Section 1" in sections
        assert "Section 2" in sections
        assert "Section 3" in sections
    
    def test_validation_report_success_rate(self, validator, temp_templates_dir):
        """Test success rate calculation in validation report."""
        # Create one valid and one invalid framework
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir()
        
        valid_metadata = """# GDPR Handbuch - Metadaten

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
        (gdpr_de_dir / "0000_metadata_de_gdpr.md").write_text(valid_metadata, encoding='utf-8')
        
        iso_de_dir = temp_templates_dir / "de" / "iso-9001"
        iso_de_dir.mkdir()
        
        invalid_metadata = """# ISO 9001 Handbuch - Metadaten

**Dokument-ID:** 0000  
"""
        (iso_de_dir / "0000_metadata_de_iso-9001.md").write_text(invalid_metadata, encoding='utf-8')
        
        (temp_templates_dir / "en" / "gdpr").mkdir()
        (temp_templates_dir / "en" / "iso-9001").mkdir()
        
        report = validator.validate_language("de")
        
        assert report.total_files == 2
        assert report.valid_files == 1
        assert report.invalid_files == 1
        assert report.success_rate == 50.0
    
    def test_validation_error_types(self, validator, temp_templates_dir):
        """Test different validation error types."""
        # Create framework with various errors
        gdpr_de_dir = temp_templates_dir / "de" / "gdpr"
        gdpr_de_dir.mkdir()
        
        metadata_with_errors = """# GDPR Handbuch - Metadaten

**Dokument-ID:** 0000  
**Owner:** {{ meta.owner }}  
**Template-Version:** invalid_format  
**Revision:** not_a_number  
**Invalid-Placeholder:** {{bad.placeholder}}
"""
        (gdpr_de_dir / "0000_metadata_de_gdpr.md").write_text(metadata_with_errors, encoding='utf-8')
        
        (temp_templates_dir / "en" / "gdpr").mkdir()
        
        report = validator.validate_all()
        
        # Should have multiple error types
        error_types = set(error.error_type for error in report.errors)
        assert "missing_field" in error_types
        assert "invalid_field" in error_types or "invalid_placeholder" in error_types
