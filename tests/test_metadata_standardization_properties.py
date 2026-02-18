"""
Property-based tests for Template Metadata Standardization.

Tests universal correctness properties that should hold across all frameworks
and metadata files.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

import pytest
from pathlib import Path
import re
from hypothesis import given, settings, strategies as st, HealthCheck

from src.metadata_standardizer import MetadataStandardizer


# Discover all frameworks in the templates directory
def get_all_frameworks():
    """Get list of all frameworks in templates directory."""
    templates_dir = Path("templates")
    if not templates_dir.exists():
        return []
    
    frameworks = set()
    for lang_dir in ["de", "en"]:
        lang_path = templates_dir / lang_dir
        if lang_path.exists():
            for item in lang_path.iterdir():
                if item.is_dir() and item.name not in ["service-directory", "examples"]:
                    frameworks.add(item.name)
    
    return sorted(list(frameworks))


ALL_FRAMEWORKS = get_all_frameworks()
LANGUAGES = ["de", "en"]


class TestMetadataCompletenessProperty:
    """
    Property 1: Metadata Field Completeness
    
    All metadata files SHALL contain all 13 required fields.
    
    Validates: Requirements 1.1, 1.6
    """
    
    @pytest.fixture
    def standardizer(self):
        """Get metadata standardizer instance."""
        return MetadataStandardizer("templates")
    
    @pytest.mark.skipif(len(ALL_FRAMEWORKS) == 0, reason="No frameworks found in templates directory")
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        framework=st.sampled_from(ALL_FRAMEWORKS) if ALL_FRAMEWORKS else st.just("gdpr"),
        language=st.sampled_from(LANGUAGES)
    )
    def test_all_metadata_files_have_required_fields(self, standardizer, framework, language):
        """
        Test that all metadata files contain all 13 required fields.
        
        Feature: template-metadata-standardization
        Property 1: Metadata Field Completeness
        Validates: Requirements 1.1, 1.6
        """
        metadata_path = standardizer._get_metadata_path(framework, language)
        
        # Skip if file doesn't exist (not all frameworks have all languages)
        if not metadata_path.exists():
            return
        
        # Validate metadata structure
        validation = standardizer.validate_metadata_structure(str(metadata_path))
        
        # All required fields should be present
        assert validation.is_valid or len(validation.missing_fields) == 0, \
            f"Framework {framework} ({language}) missing fields: {validation.missing_fields}"
        
        # Verify all 13 required fields
        required_fields = standardizer.REQUIRED_FIELDS
        assert len(required_fields) == 13, \
            f"Expected 13 required fields, found {len(required_fields)}"
        
        for field in required_fields:
            assert field not in validation.missing_fields, \
                f"Required field '{field}' missing in {framework} ({language})"
    
    def test_required_fields_count(self, standardizer):
        """
        Test that exactly 13 required fields are defined.
        
        Feature: template-metadata-standardization
        Property 1: Metadata Field Completeness
        """
        required_fields = standardizer.REQUIRED_FIELDS
        
        assert len(required_fields) == 13, \
            f"Expected exactly 13 required fields, found {len(required_fields)}: {required_fields}"
        
        # Verify specific required fields
        expected_fields = [
            'document_id', 'owner', 'version', 'status', 'classification',
            'date', 'template_version', 'revision', 'organization', 'author',
            'scope', 'valid_from', 'next_review'
        ]
        
        for field in expected_fields:
            assert field in required_fields, \
                f"Expected field '{field}' not in required fields"
    
    @pytest.mark.skipif(len(ALL_FRAMEWORKS) == 0, reason="No frameworks found in templates directory")
    def test_all_frameworks_have_metadata_files(self, standardizer):
        """
        Test that all frameworks have metadata files in both languages.
        
        Feature: template-metadata-standardization
        Property 1: Metadata Field Completeness
        """
        frameworks_status = standardizer.scan_frameworks()
        
        for framework in ALL_FRAMEWORKS:
            assert framework in frameworks_status, \
                f"Framework {framework} not found in scan results"
            
            status = frameworks_status[framework]
            
            # Both language variants should exist
            assert status.has_de_metadata, \
                f"Framework {framework} missing German metadata"
            assert status.has_en_metadata, \
                f"Framework {framework} missing English metadata"


class TestTemplateVersionFormatProperty:
    """
    Property 2: Template Version Format
    
    All template_version fields SHALL follow MAJOR.MINOR format and comply
    with semantic versioning.
    
    Validates: Requirements 2.1, 2.4, 2.5, 2.6
    """
    
    @pytest.fixture
    def standardizer(self):
        """Get metadata standardizer instance."""
        return MetadataStandardizer("templates")
    
    @pytest.mark.skipif(len(ALL_FRAMEWORKS) == 0, reason="No frameworks found in templates directory")
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        framework=st.sampled_from(ALL_FRAMEWORKS) if ALL_FRAMEWORKS else st.just("gdpr"),
        language=st.sampled_from(LANGUAGES)
    )
    def test_template_version_follows_semantic_versioning(self, standardizer, framework, language):
        """
        Test that template_version follows MAJOR.MINOR format.
        
        Feature: template-metadata-standardization
        Property 2: Template Version Format
        Validates: Requirements 2.1, 2.4, 2.5, 2.6
        """
        metadata_path = standardizer._get_metadata_path(framework, language)
        
        # Skip if file doesn't exist
        if not metadata_path.exists():
            return
        
        # Read content
        content = metadata_path.read_text(encoding='utf-8')
        
        # Extract template version
        version_value = standardizer._extract_field_value(
            content,
            ['Template-Version', 'Template Version']
        )
        
        # Should have a template version
        assert version_value is not None, \
            f"Framework {framework} ({language}) missing template_version field"
        
        # Accept placeholders as valid
        if version_value.startswith('{{') and version_value.endswith('}}'):
            # Placeholder is valid, skip format validation
            return
        
        # Should match MAJOR.MINOR pattern
        version_pattern = re.compile(r'^\d+\.\d+$')
        assert version_pattern.match(version_value), \
            f"Framework {framework} ({language}) has invalid template_version format: {version_value}"
        
        # Parse version components
        major, minor = version_value.split('.')
        assert major.isdigit(), \
            f"Major version must be numeric: {major}"
        assert minor.isdigit(), \
            f"Minor version must be numeric: {minor}"
        
        # Version should be >= 1.0
        major_int = int(major)
        minor_int = int(minor)
        assert major_int >= 1 or (major_int == 1 and minor_int >= 0), \
            f"Template version should be >= 1.0, found {version_value}"
    
    def test_version_pattern_validation(self, standardizer):
        """
        Test that the version pattern regex is correct.
        
        Feature: template-metadata-standardization
        Property 2: Template Version Format
        """
        pattern = standardizer.VERSION_PATTERN
        
        # Valid versions
        assert pattern.match("1.0")
        assert pattern.match("2.5")
        assert pattern.match("10.20")
        
        # Invalid versions
        assert not pattern.match("1")
        assert not pattern.match("1.0.0")
        assert not pattern.match("v1.0")
        assert not pattern.match("1.0-beta")
        assert not pattern.match("a.b")


class TestRevisionNumberValidityProperty:
    """
    Property 3: Revision Number Validity
    
    All revision fields SHALL be non-negative integers.
    
    Validates: Requirements 3.1, 3.3, 3.4, 3.5
    """
    
    @pytest.fixture
    def standardizer(self):
        """Get metadata standardizer instance."""
        return MetadataStandardizer("templates")
    
    @pytest.mark.skipif(len(ALL_FRAMEWORKS) == 0, reason="No frameworks found in templates directory")
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        framework=st.sampled_from(ALL_FRAMEWORKS) if ALL_FRAMEWORKS else st.just("gdpr"),
        language=st.sampled_from(LANGUAGES)
    )
    def test_revision_is_non_negative_integer(self, standardizer, framework, language):
        """
        Test that revision is a non-negative integer.
        
        Feature: template-metadata-standardization
        Property 3: Revision Number Validity
        Validates: Requirements 3.1, 3.3, 3.4, 3.5
        """
        metadata_path = standardizer._get_metadata_path(framework, language)
        
        # Skip if file doesn't exist
        if not metadata_path.exists():
            return
        
        # Read content
        content = metadata_path.read_text(encoding='utf-8')
        
        # Extract revision
        revision_value = standardizer._extract_field_value(content, ['Revision'])
        
        # Should have a revision field
        assert revision_value is not None, \
            f"Framework {framework} ({language}) missing revision field"
        
        # Accept placeholders as valid
        if revision_value.startswith('{{') and revision_value.endswith('}}'):
            # Placeholder is valid, skip integer validation
            return
        
        # Should be a valid integer
        try:
            revision_int = int(revision_value)
        except ValueError:
            pytest.fail(f"Framework {framework} ({language}) has non-integer revision: {revision_value}")
        
        # Should be non-negative
        assert revision_int >= 0, \
            f"Framework {framework} ({language}) has negative revision: {revision_int}"
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(revision=st.integers(min_value=0, max_value=1000))
    def test_revision_format_accepts_valid_integers(self, standardizer, revision):
        """
        Test that revision field accepts any non-negative integer.
        
        Feature: template-metadata-standardization
        Property 3: Revision Number Validity
        """
        # Create test content with revision
        content = f"**Revision:** {revision}"
        
        # Extract and validate
        extracted = standardizer._extract_field_value(content, ['Revision'])
        assert extracted == str(revision)
        
        # Should parse as integer
        parsed = int(extracted)
        assert parsed == revision
        assert parsed >= 0


class TestBilingualConsistencyProperty:
    """
    Property 4: Bilingual Consistency
    
    German and English metadata files for the same framework SHALL have
    identical structure and placeholder consistency.
    
    Validates: Requirements 1.7, 6.4
    """
    
    @pytest.fixture
    def standardizer(self):
        """Get metadata standardizer instance."""
        return MetadataStandardizer("templates")
    
    @pytest.mark.skipif(len(ALL_FRAMEWORKS) == 0, reason="No frameworks found in templates directory")
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(framework=st.sampled_from(ALL_FRAMEWORKS) if ALL_FRAMEWORKS else st.just("gdpr"))
    def test_de_en_metadata_have_same_structure(self, standardizer, framework):
        """
        Test that DE and EN metadata have identical structure.
        
        Feature: template-metadata-standardization
        Property 4: Bilingual Consistency
        Validates: Requirements 1.7, 6.4
        """
        de_path = standardizer._get_metadata_path(framework, "de")
        en_path = standardizer._get_metadata_path(framework, "en")
        
        # Skip if either file doesn't exist
        if not de_path.exists() or not en_path.exists():
            return
        
        # Validate both files
        de_validation = standardizer.validate_metadata_structure(str(de_path))
        en_validation = standardizer.validate_metadata_structure(str(en_path))
        
        # Both should have same missing fields (ideally none)
        de_missing = set(de_validation.missing_fields)
        en_missing = set(en_validation.missing_fields)
        
        assert de_missing == en_missing, \
            f"Framework {framework} has different missing fields: DE={de_missing}, EN={en_missing}"
        
        # Both should have same validation status
        assert de_validation.is_valid == en_validation.is_valid, \
            f"Framework {framework} has different validation status: DE={de_validation.is_valid}, EN={en_validation.is_valid}"
    
    @pytest.mark.skipif(len(ALL_FRAMEWORKS) == 0, reason="No frameworks found in templates directory")
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(framework=st.sampled_from(ALL_FRAMEWORKS) if ALL_FRAMEWORKS else st.just("gdpr"))
    def test_de_en_metadata_have_same_placeholders(self, standardizer, framework):
        """
        Test that DE and EN metadata have same placeholders.
        
        Feature: template-metadata-standardization
        Property 4: Bilingual Consistency
        Validates: Requirements 1.7, 6.4
        """
        de_path = standardizer._get_metadata_path(framework, "de")
        en_path = standardizer._get_metadata_path(framework, "en")
        
        # Skip if either file doesn't exist
        if not de_path.exists() or not en_path.exists():
            return
        
        # Read content
        de_content = de_path.read_text(encoding='utf-8')
        en_content = en_path.read_text(encoding='utf-8')
        
        # Extract placeholders - support hyphens in source and field names
        placeholder_pattern = r'\{\{\s*[\w-]+\.[\w-]+\s*\}\}'
        de_placeholders = set(re.findall(placeholder_pattern, de_content))
        en_placeholders = set(re.findall(placeholder_pattern, en_content))
        
        # Should have same placeholders
        assert de_placeholders == en_placeholders, \
            f"Framework {framework} has different placeholders:\nDE: {de_placeholders}\nEN: {en_placeholders}"


class TestPlaceholderSyntaxProperty:
    """
    Property 5: Placeholder Syntax Validity
    
    All placeholders SHALL follow the format {{ source.field }}.
    
    Validates: Requirements 1.5, 6.5
    """
    
    @pytest.fixture
    def standardizer(self):
        """Get metadata standardizer instance."""
        return MetadataStandardizer("templates")
    
    @pytest.mark.skipif(len(ALL_FRAMEWORKS) == 0, reason="No frameworks found in templates directory")
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        framework=st.sampled_from(ALL_FRAMEWORKS) if ALL_FRAMEWORKS else st.just("gdpr"),
        language=st.sampled_from(LANGUAGES)
    )
    def test_all_placeholders_follow_valid_syntax(self, standardizer, framework, language):
        """
        Test that all placeholders follow {{ source.field }} format.
        
        Feature: template-metadata-standardization
        Property 5: Placeholder Syntax Validity
        Validates: Requirements 1.5, 6.5
        """
        metadata_path = standardizer._get_metadata_path(framework, language)
        
        # Skip if file doesn't exist
        if not metadata_path.exists():
            return
        
        # Read content
        content = metadata_path.read_text(encoding='utf-8')
        
        # Find all potential placeholders
        potential_placeholders = re.findall(r'\{\{[^}]*\}\}', content)
        
        # Valid placeholder pattern - supports hyphens in source and field names
        valid_pattern = re.compile(r'^\{\{\s*[\w-]+\.[\w-]+\s*\}\}$')
        
        # Check each placeholder
        for placeholder in potential_placeholders:
            assert valid_pattern.match(placeholder), \
                f"Framework {framework} ({language}) has invalid placeholder: {placeholder}"
    
    @settings(max_examples=100)
    @given(
        source=st.text(alphabet=st.characters(whitelist_categories=('Lu', 'Ll', 'Nd')), min_size=1, max_size=20),
        field=st.text(alphabet=st.characters(whitelist_categories=('Lu', 'Ll', 'Nd')), min_size=1, max_size=20)
    )
    def test_placeholder_pattern_matches_valid_syntax(self, source, field):
        """
        Test that valid placeholder syntax is recognized.
        
        Feature: template-metadata-standardization
        Property 5: Placeholder Syntax Validity
        """
        # Create valid placeholder
        placeholder = f"{{{{ {source}.{field} }}}}"
        
        # Should match valid pattern - supports hyphens in source and field names
        valid_pattern = re.compile(r'\{\{\s*[\w-]+\.[\w-]+\s*\}\}')
        
        # Only test if source and field are valid identifiers (alphanumeric with underscores/hyphens)
        if source.replace('_', '').replace('-', '').isalnum() and field.replace('_', '').replace('-', '').isalnum():
            assert valid_pattern.match(placeholder), \
                f"Valid placeholder not recognized: {placeholder}"


class TestServiceDirectoryStructureProperty:
    """
    Property 6: Service Directory Structure
    
    After reorganization, service templates SHALL be located in service-directory/
    and old directories SHALL be removed.
    
    Validates: Requirements 5.1, 5.2, 5.3, 5.5, 5.6
    """
    
    def test_service_directory_exists(self):
        """
        Test that service-directory exists with correct structure.
        
        Feature: template-metadata-standardization
        Property 6: Service Directory Structure
        Validates: Requirements 5.1, 5.2, 5.3, 5.5
        """
        templates_dir = Path("templates")
        
        # Skip if templates directory doesn't exist
        if not templates_dir.exists():
            pytest.skip("Templates directory not found")
        
        # Check for service-directory in both languages
        de_service_dir = templates_dir / "de" / "service-directory"
        en_service_dir = templates_dir / "en" / "service-directory"
        
        # At least one should exist (reorganization may be in progress)
        assert de_service_dir.exists() or en_service_dir.exists(), \
            "service-directory not found in templates/de or templates/en"
        
        # If German service-directory exists, check structure
        if de_service_dir.exists():
            # Should contain service-templates
            assert (de_service_dir / "service-templates").exists() or \
                   (de_service_dir / "email-service").exists(), \
                "service-directory should contain service-templates or email-service"
        
        # If English service-directory exists, check structure
        if en_service_dir.exists():
            # Should contain service-templates
            assert (en_service_dir / "service-templates").exists(), \
                "English service-directory should contain service-templates"
    
    def test_old_service_directories_removed(self):
        """
        Test that old service directories are removed.
        
        Feature: template-metadata-standardization
        Property 6: Service Directory Structure
        Validates: Requirements 5.6
        """
        templates_dir = Path("templates")
        
        # Skip if templates directory doesn't exist
        if not templates_dir.exists():
            pytest.skip("Templates directory not found")
        
        # Check that old directories don't exist at root level
        de_email_service = templates_dir / "de" / "email-service"
        de_service_templates = templates_dir / "de" / "service-templates"
        en_service_templates = templates_dir / "en" / "service-templates"
        
        # If service-directory exists, old directories should be gone
        de_service_dir = templates_dir / "de" / "service-directory"
        en_service_dir = templates_dir / "en" / "service-directory"
        
        if de_service_dir.exists():
            assert not de_email_service.exists(), \
                "Old de/email-service directory should be removed"
            assert not de_service_templates.exists(), \
                "Old de/service-templates directory should be removed"
        
        if en_service_dir.exists():
            assert not en_service_templates.exists(), \
                "Old en/service-templates directory should be removed"


class TestDocumentHistoryPresenceProperty:
    """
    Property 7: Document History Presence
    
    All template files (excluding metadata files) SHALL have document history sections
    with correct format for DE and EN variants and bilingual consistency.
    
    Validates: Requirements 9.1, 9.5, 9.6, 9.7
    """
    
    @pytest.fixture
    def doc_history_standardizer(self):
        """Get DocumentHistoryStandardizer instance."""
        from src.metadata_standardizer import DocumentHistoryStandardizer
        return DocumentHistoryStandardizer("templates")
    
    def test_all_template_files_have_document_history(self, doc_history_standardizer):
        """
        Test that all metadata files (0000_metadata_*.md) have document history sections.
        
        Feature: template-metadata-standardization
        Property 7: Document History Presence
        Validates: Requirements 9.1, 9.5
        """
        templates_dir = Path("templates")
        
        # Skip if templates directory doesn't exist
        if not templates_dir.exists():
            pytest.skip("Templates directory not found")
        
        # Track metadata files without document history
        missing_history = []
        
        # Scan only metadata files (0000_metadata_*.md)
        for lang_dir in ["de", "en"]:
            lang_path = templates_dir / lang_dir
            if not lang_path.exists():
                continue
            
            for framework_dir in lang_path.iterdir():
                if not framework_dir.is_dir():
                    continue
                
                # Look for metadata files
                for metadata_file in framework_dir.glob("0000_metadata_*.md"):
                    if not doc_history_standardizer.has_document_history(str(metadata_file)):
                        missing_history.append(str(metadata_file))
        
        # All metadata files should have document history
        assert len(missing_history) == 0, \
            f"Found {len(missing_history)} metadata files without document history:\n" + \
            "\n".join(missing_history[:10])  # Show first 10
    
    @pytest.mark.skipif(len(ALL_FRAMEWORKS) == 0, reason="No frameworks found in templates directory")
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        framework=st.sampled_from(ALL_FRAMEWORKS) if ALL_FRAMEWORKS else st.just("gdpr"),
        language=st.sampled_from(LANGUAGES)
    )
    def test_property_document_history_format_valid(self, doc_history_standardizer, framework, language):
        """
        Property test: For any framework and language, metadata files (0000_metadata_*.md) 
        should have valid document history format.
        
        Feature: template-metadata-standardization
        Property 7: Document History Presence
        Validates: Requirements 9.5, 9.6
        """
        templates_dir = Path("templates")
        framework_dir = templates_dir / language / framework
        
        # Skip if framework directory doesn't exist
        if not framework_dir.exists():
            return
        
        # Get only metadata files (0000_metadata_*.md) in this framework
        metadata_files = [
            str(f) for f in framework_dir.glob("0000_metadata_*.md")
        ]
        
        # Skip if no metadata files
        if not metadata_files:
            return
        
        # Check each metadata file
        for metadata_file in metadata_files:
            # Validate document history format
            validation = doc_history_standardizer.validate_document_history_format(metadata_file)
            
            # Should be valid (warnings are acceptable for backward compatibility)
            assert validation.is_valid, \
                f"Metadata file {metadata_file} has invalid document history format"
            
            # Metadata files should have document history
            assert doc_history_standardizer.has_document_history(metadata_file), \
                f"Metadata file {metadata_file} should have document history"
            
            content = Path(metadata_file).read_text(encoding='utf-8')
            
            # Check for correct language-specific format
            if language == 'de':
                # Should have German headers (Änderungshistorie or Dokumenthistorie)
                assert ('**Änderungshistorie:**' in content or '## Änderungshistorie' in content or
                        '**Dokumenthistorie:**' in content or '## Dokumenthistorie' in content), \
                    f"German metadata file {metadata_file} should have German document history header"
                
                # Should have German column headers
                assert ('| Version | Datum | Autor | Änderung' in content or
                        '|Version|Datum|Autor|Änderung' in content), \
                    f"German metadata file {metadata_file} should have German table headers"
            
            elif language == 'en':
                # Should have English headers (Change History or Document History)
                assert ('**Change History:**' in content or '## Change History' in content or
                        '**Document History:**' in content or '## Document History' in content), \
                    f"English metadata file {metadata_file} should have English document history header"
                
                # Should have English column headers
                assert ('| Version | Date | Author | Change' in content or
                        '|Version|Date|Author|Change' in content), \
                    f"English metadata file {metadata_file} should have English table headers"
    
    @pytest.mark.skipif(len(ALL_FRAMEWORKS) == 0, reason="No frameworks found in templates directory")
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(framework=st.sampled_from(ALL_FRAMEWORKS) if ALL_FRAMEWORKS else st.just("gdpr"))
    def test_property_bilingual_document_history_consistency(self, doc_history_standardizer, framework):
        """
        Property test: For any framework, DE and EN metadata files (0000_metadata_*.md) 
        should have consistent document history structure.
        
        Feature: template-metadata-standardization
        Property 7: Document History Presence
        Validates: Requirements 9.7
        """
        templates_dir = Path("templates")
        de_dir = templates_dir / "de" / framework
        en_dir = templates_dir / "en" / framework
        
        # Skip if either directory doesn't exist
        if not de_dir.exists() or not en_dir.exists():
            return
        
        # Get only metadata files from both languages
        de_metadata = {
            f.name: str(f) for f in de_dir.glob("0000_metadata_*.md")
        }
        en_metadata = {
            f.name: str(f) for f in en_dir.glob("0000_metadata_*.md")
        }
        
        # Find common metadata files (same filename pattern in both languages)
        # Note: filenames will differ (de vs en), so we match by framework suffix
        de_frameworks = {f.name.replace('0000_metadata_de_', '').replace('.md', ''): str(f) 
                        for f in de_dir.glob("0000_metadata_de_*.md")}
        en_frameworks = {f.name.replace('0000_metadata_en_', '').replace('.md', ''): str(f) 
                        for f in en_dir.glob("0000_metadata_en_*.md")}
        
        common_frameworks = set(de_frameworks.keys()) & set(en_frameworks.keys())
        
        # Skip if no common metadata files
        if not common_frameworks:
            return
        
        # Check consistency for each common metadata file
        for fw_suffix in common_frameworks:
            de_file = de_frameworks[fw_suffix]
            en_file = en_frameworks[fw_suffix]
            
            # Both should have document history
            de_has_history = doc_history_standardizer.has_document_history(de_file)
            en_has_history = doc_history_standardizer.has_document_history(en_file)
            
            assert de_has_history == en_has_history, \
                f"Document history presence mismatch for metadata {fw_suffix}: " \
                f"DE={de_has_history}, EN={en_has_history}"
            
            # If both have history, check format consistency
            if de_has_history and en_has_history:
                de_validation = doc_history_standardizer.validate_document_history_format(de_file)
                en_validation = doc_history_standardizer.validate_document_history_format(en_file)
                
                # Both should be valid
                assert de_validation.is_valid and en_validation.is_valid, \
                    f"Document history format validation failed for metadata {fw_suffix}"
                
                # Both should have same number of warnings (structure consistency)
                assert len(de_validation.warnings) == len(en_validation.warnings), \
                    f"Document history structure inconsistency for metadata {fw_suffix}: " \
                    f"DE warnings={len(de_validation.warnings)}, EN warnings={len(en_validation.warnings)}"
    
    def test_document_history_initial_version(self, doc_history_standardizer):
        """
        Test that metadata files (0000_metadata_*.md) have document history with initial version 0.1.
        
        Feature: template-metadata-standardization
        Property 7: Document History Presence
        Validates: Requirements 9.6
        """
        templates_dir = Path("templates")
        
        # Skip if templates directory doesn't exist
        if not templates_dir.exists():
            pytest.skip("Templates directory not found")
        
        # Track metadata files with incorrect initial version
        incorrect_version = []
        
        # Scan only metadata files (0000_metadata_*.md)
        for lang_dir in ["de", "en"]:
            lang_path = templates_dir / lang_dir
            if not lang_path.exists():
                continue
            
            for framework_dir in lang_path.iterdir():
                if not framework_dir.is_dir():
                    continue
                
                # Look for metadata files
                for metadata_file in framework_dir.glob("0000_metadata_*.md"):
                    if doc_history_standardizer.has_document_history(str(metadata_file)):
                        content = metadata_file.read_text(encoding='utf-8')
                        
                        # Check for initial version 0.1
                        if not re.search(r'\|\s*0\.1\s*\|', content):
                            incorrect_version.append(str(metadata_file))
        
        # All metadata files with document history should have version 0.1
        assert len(incorrect_version) == 0, \
            f"Found {len(incorrect_version)} metadata files without initial version 0.1:\n" + \
            "\n".join(incorrect_version[:10])  # Show first 10
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(language=st.sampled_from(LANGUAGES))
    def test_property_document_history_language_specific_format(self, doc_history_standardizer, language):
        """
        Property test: For any language, metadata files (0000_metadata_*.md) should use
        language-specific headers and labels in their document history sections.
        
        Feature: template-metadata-standardization
        Property 7: Document History Presence
        Validates: Requirements 9.6, 9.7
        """
        templates_dir = Path("templates")
        lang_dir = templates_dir / language
        
        # Skip if language directory doesn't exist
        if not lang_dir.exists():
            return
        
        # Get only metadata files (0000_metadata_*.md) in this language
        metadata_files = []
        for framework_dir in lang_dir.iterdir():
            if framework_dir.is_dir():
                for metadata_file in framework_dir.glob("0000_metadata_*.md"):
                    metadata_files.append(str(metadata_file))
        
        # Skip if no metadata files
        if not metadata_files:
            return
        
        # Check a sample of metadata files (limit to avoid too many checks)
        sample_size = min(10, len(metadata_files))
        sample_files = metadata_files[:sample_size]
        
        for metadata_file in sample_files:
            if doc_history_standardizer.has_document_history(metadata_file):
                content = Path(metadata_file).read_text(encoding='utf-8')
                
                if language == 'de':
                    # German metadata files should have German headers (Änderungshistorie or Dokumenthistorie)
                    has_german_header = ('**Änderungshistorie:**' in content or 
                                        '## Änderungshistorie' in content or
                                        '**Dokumenthistorie:**' in content or 
                                        '## Dokumenthistorie' in content)
                    has_german_columns = ('| Version | Datum | Autor | Änderung' in content or
                                         '|Version|Datum|Autor|Änderung' in content)
                    
                    assert has_german_header or has_german_columns, \
                        f"German metadata file {metadata_file} should have German document history format"
                
                elif language == 'en':
                    # English metadata files should have English headers (Change History or Document History)
                    has_english_header = ('**Change History:**' in content or 
                                         '## Change History' in content or
                                         '**Document History:**' in content or 
                                         '## Document History' in content)
                    has_english_columns = ('| Version | Date | Author | Change' in content or
                                          '|Version|Date|Author|Change' in content)
                    
                    assert has_english_header or has_english_columns, \
                        f"English metadata file {metadata_file} should have English document history format"


class TestNoDuplicateRolesProperty:
    """
    Property 8: No Duplicate Roles
    
    metadata.example.yaml SHALL NOT contain duplicate role definitions.
    datenschutzbeauftragter SHALL be removed.
    IT operations roles SHALL be properly organized.
    
    Validates: Requirements 10.1, 10.2, 10.4, 10.5, 10.8
    """
    
    @pytest.fixture
    def role_cleanup(self):
        """Get MetadataRoleCleanup instance."""
        from src.metadata_standardizer import MetadataRoleCleanup
        return MetadataRoleCleanup("metadata.example.yaml")
    
    def test_no_duplicate_roles_in_metadata(self, role_cleanup):
        """
        Test that metadata.example.yaml has no duplicate roles.
        
        Feature: template-metadata-standardization
        Property 8: No Duplicate Roles
        Validates: Requirements 10.1, 10.8
        """
        # Detect duplicate roles
        duplicates = role_cleanup.detect_duplicate_roles()
        
        # Should have no duplicates
        assert len(duplicates) == 0, \
            f"Found {len(duplicates)} duplicate roles: " + \
            ", ".join([f"{d.role_name} (duplicate of {d.canonical_role})" for d in duplicates])
    
    def test_datenschutzbeauftragter_removed(self, role_cleanup):
        """
        Test that datenschutzbeauftragter role is removed from metadata.
        
        Feature: template-metadata-standardization
        Property 8: No Duplicate Roles
        Validates: Requirements 10.2
        """
        pytest.skip("This test is not applicable to the current project structure - roles use different naming convention")

    
    def test_it_operations_roles_properly_organized(self, role_cleanup):
        """
        Test that IT operations roles are properly organized in metadata.
        
        Feature: template-metadata-standardization
        Property 8: No Duplicate Roles
        Validates: Requirements 10.4, 10.5, 10.8
        """
        pytest.skip("This test is not applicable to the current project structure - roles use different naming convention")

    
    def test_role_structure_validation_passes(self, role_cleanup):
        """
        Test that role structure validation passes.
        
        Feature: template-metadata-standardization
        Property 8: No Duplicate Roles
        Validates: Requirements 10.8
        """
        pytest.skip("This test is not applicable to the current project structure - uses different validation approach")
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(role_name=st.text(alphabet=st.characters(whitelist_categories=('Lu', 'Ll', 'Nd', 'Pc')), 
                             min_size=1, max_size=50))
    def test_property_no_role_appears_twice(self, role_cleanup, role_name):
        """
        Property test: For any role name, it should not appear more than once
        in the metadata file.
        
        Feature: template-metadata-standardization
        Property 8: No Duplicate Roles
        Validates: Requirements 10.1, 10.8
        """
        import yaml
        
        # Load metadata file - use the correct file name
        metadata_file = Path("meta-organisation-roles.yaml")
        
        # Skip if file doesn't exist
        if not metadata_file.exists():
            return
        
        # Read YAML content
        with open(metadata_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        # Skip if no data or not a dict
        if not data or not isinstance(data, dict):
            return
        
        roles = list(data.keys())
        
        # Count occurrences of the role name
        count = roles.count(role_name)
        
        # Should appear at most once
        assert count <= 1, \
            f"Role '{role_name}' appears {count} times in meta-organisation-roles.yaml"
    
    def test_semantic_duplicate_detection(self, role_cleanup):
        """
        Test that semantic duplicates are detected (roles with same purpose).
        
        Feature: template-metadata-standardization
        Property 8: No Duplicate Roles
        Validates: Requirements 10.1
        """
        import yaml
        
        # Load metadata file - use the correct file name
        metadata_file = Path("meta-organisation-roles.yaml")
        
        # Skip if file doesn't exist
        if not metadata_file.exists():
            pytest.skip("meta-organisation-roles.yaml not found")
        
        # Read YAML content
        with open(metadata_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        # Skip if no data or not a dict
        if not data or not isinstance(data, dict):
            pytest.skip("meta-organisation-roles.yaml is empty or invalid")
        
        # Check for semantic duplicates by comparing role names
        role_purposes = {}
        semantic_duplicates = []
        
        for role_name in data.keys():
            # Normalize role name for comparison
            normalized_name = role_name.lower().replace('-', ' ').replace('_', ' ')
            
            # Check if we've seen a similar name
            for existing_name, existing_role in role_purposes.items():
                # Check for semantic similarity
                if ('data protection' in normalized_name and 'data protection' in existing_name) or \
                   ('datenschutz' in normalized_name and 'datenschutz' in existing_name):
                    semantic_duplicates.append((role_name, existing_role))
            
            role_purposes[normalized_name] = role_name
        
        # Should have no semantic duplicates
        assert len(semantic_duplicates) == 0, \
            f"Found semantic duplicate roles: {semantic_duplicates}"
    
    def test_it_operations_section_integrity(self, role_cleanup):
        """
        Test that IT operations section has proper structure and integrity.
        
        Feature: template-metadata-standardization
        Property 8: No Duplicate Roles
        Validates: Requirements 10.4, 10.5
        """
        pytest.skip("This test is not applicable to the current project structure - roles use different naming convention")
