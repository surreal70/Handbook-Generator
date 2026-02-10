"""
Property-based tests for Template Metadata Standardization.

Tests universal correctness properties that should hold across all frameworks
and metadata files.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
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
        
        # Should be a valid integer
        try:
            revision_int = int(revision_value)
        except ValueError:
            pytest.fail(f"Framework {framework} ({language}) has non-integer revision: {revision_value}")
        
        # Should be non-negative
        assert revision_int >= 0, \
            f"Framework {framework} ({language}) has negative revision: {revision_int}"
        
        # For new templates, should be 0
        if "1.0" in content:  # New template with version 1.0
            assert revision_int == 0, \
                f"New template {framework} ({language}) should have revision 0, found {revision_int}"
    
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
        
        # Extract placeholders
        placeholder_pattern = r'\{\{\s*\w+\.\w+\s*\}\}'
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
        
        # Valid placeholder pattern
        valid_pattern = re.compile(r'^\{\{\s*\w+\.\w+\s*\}\}$')
        
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
        
        # Should match valid pattern
        valid_pattern = re.compile(r'\{\{\s*\w+\.\w+\s*\}\}')
        
        # Only test if source and field are valid identifiers
        if source.replace('_', '').isalnum() and field.replace('_', '').isalnum():
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
        Test that all template files have document history sections.
        
        Feature: template-metadata-standardization
        Property 7: Document History Presence
        Validates: Requirements 9.1, 9.5
        """
        # Scan all template files
        template_files = doc_history_standardizer.scan_template_files()
        
        # Skip if no templates found
        if not template_files:
            pytest.skip("No template files found")
        
        # Track files without document history
        missing_history = []
        
        for template_file in template_files:
            if not doc_history_standardizer.has_document_history(template_file):
                missing_history.append(template_file)
        
        # All template files should have document history
        assert len(missing_history) == 0, \
            f"Found {len(missing_history)} template files without document history:\n" + \
            "\n".join(missing_history[:10])  # Show first 10
    
    @pytest.mark.skipif(len(ALL_FRAMEWORKS) == 0, reason="No frameworks found in templates directory")
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        framework=st.sampled_from(ALL_FRAMEWORKS) if ALL_FRAMEWORKS else st.just("gdpr"),
        language=st.sampled_from(LANGUAGES)
    )
    def test_property_document_history_format_valid(self, doc_history_standardizer, framework, language):
        """
        Property test: For any framework and language, template files should have
        valid document history format.
        
        Feature: template-metadata-standardization
        Property 7: Document History Presence
        Validates: Requirements 9.5, 9.6
        """
        templates_dir = Path("templates")
        framework_dir = templates_dir / language / framework
        
        # Skip if framework directory doesn't exist
        if not framework_dir.exists():
            return
        
        # Get all template files in this framework (excluding metadata)
        template_files = [
            str(f) for f in framework_dir.glob("*.md")
            if not f.name.startswith("0000_metadata")
        ]
        
        # Skip if no templates
        if not template_files:
            return
        
        # Check each template file
        for template_file in template_files:
            # Validate document history format
            validation = doc_history_standardizer.validate_document_history_format(template_file)
            
            # Should be valid (warnings are acceptable for backward compatibility)
            assert validation.is_valid, \
                f"Template {template_file} has invalid document history format"
            
            # If document history exists, check format
            if doc_history_standardizer.has_document_history(template_file):
                content = Path(template_file).read_text(encoding='utf-8')
                
                # Check for correct language-specific format
                if language == 'de':
                    # Should have German headers
                    assert ('**Dokumenthistorie:**' in content or '## Dokumenthistorie' in content), \
                        f"German template {template_file} should have German document history header"
                    
                    # Should have German column headers
                    assert ('| Version | Datum | Autor | Änderungen |' in content or
                            '|Version|Datum|Autor|Änderungen|' in content), \
                        f"German template {template_file} should have German table headers"
                
                elif language == 'en':
                    # Should have English headers
                    assert ('**Document History:**' in content or '## Document History' in content), \
                        f"English template {template_file} should have English document history header"
                    
                    # Should have English column headers
                    assert ('| Version | Date | Author | Changes |' in content or
                            '|Version|Date|Author|Changes|' in content), \
                        f"English template {template_file} should have English table headers"
    
    @pytest.mark.skipif(len(ALL_FRAMEWORKS) == 0, reason="No frameworks found in templates directory")
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(framework=st.sampled_from(ALL_FRAMEWORKS) if ALL_FRAMEWORKS else st.just("gdpr"))
    def test_property_bilingual_document_history_consistency(self, doc_history_standardizer, framework):
        """
        Property test: For any framework, DE and EN templates should have consistent
        document history structure.
        
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
        
        # Get template files from both languages (excluding metadata)
        de_templates = {
            f.name: str(f) for f in de_dir.glob("*.md")
            if not f.name.startswith("0000_metadata")
        }
        en_templates = {
            f.name: str(f) for f in en_dir.glob("*.md")
            if not f.name.startswith("0000_metadata")
        }
        
        # Find common template files (same filename in both languages)
        common_templates = set(de_templates.keys()) & set(en_templates.keys())
        
        # Skip if no common templates
        if not common_templates:
            return
        
        # Check consistency for each common template
        for template_name in common_templates:
            de_file = de_templates[template_name]
            en_file = en_templates[template_name]
            
            # Both should have document history or both should not
            de_has_history = doc_history_standardizer.has_document_history(de_file)
            en_has_history = doc_history_standardizer.has_document_history(en_file)
            
            assert de_has_history == en_has_history, \
                f"Document history presence mismatch for {template_name}: " \
                f"DE={de_has_history}, EN={en_has_history}"
            
            # If both have history, check format consistency
            if de_has_history and en_has_history:
                de_validation = doc_history_standardizer.validate_document_history_format(de_file)
                en_validation = doc_history_standardizer.validate_document_history_format(en_file)
                
                # Both should be valid
                assert de_validation.is_valid and en_validation.is_valid, \
                    f"Document history format validation failed for {template_name}"
                
                # Both should have same number of warnings (structure consistency)
                assert len(de_validation.warnings) == len(en_validation.warnings), \
                    f"Document history structure inconsistency for {template_name}: " \
                    f"DE warnings={len(de_validation.warnings)}, EN warnings={len(en_validation.warnings)}"
    
    def test_document_history_initial_version(self, doc_history_standardizer):
        """
        Test that document history sections have initial version 0.1.
        
        Feature: template-metadata-standardization
        Property 7: Document History Presence
        Validates: Requirements 9.6
        """
        # Scan all template files
        template_files = doc_history_standardizer.scan_template_files()
        
        # Skip if no templates found
        if not template_files:
            pytest.skip("No template files found")
        
        # Track files with incorrect initial version
        incorrect_version = []
        
        for template_file in template_files:
            if doc_history_standardizer.has_document_history(template_file):
                content = Path(template_file).read_text(encoding='utf-8')
                
                # Check for initial version 0.1
                if not re.search(r'\|\s*0\.1\s*\|', content):
                    incorrect_version.append(template_file)
        
        # All document histories should have version 0.1
        assert len(incorrect_version) == 0, \
            f"Found {len(incorrect_version)} template files without initial version 0.1:\n" + \
            "\n".join(incorrect_version[:10])  # Show first 10
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(language=st.sampled_from(LANGUAGES))
    def test_property_document_history_language_specific_format(self, doc_history_standardizer, language):
        """
        Property test: For any language, document history sections should use
        language-specific headers and labels.
        
        Feature: template-metadata-standardization
        Property 7: Document History Presence
        Validates: Requirements 9.6, 9.7
        """
        templates_dir = Path("templates")
        lang_dir = templates_dir / language
        
        # Skip if language directory doesn't exist
        if not lang_dir.exists():
            return
        
        # Get all template files in this language (excluding metadata)
        template_files = []
        for framework_dir in lang_dir.iterdir():
            if framework_dir.is_dir():
                for template_file in framework_dir.glob("*.md"):
                    if not template_file.name.startswith("0000_metadata"):
                        template_files.append(str(template_file))
        
        # Skip if no templates
        if not template_files:
            return
        
        # Check a sample of templates (limit to avoid too many checks)
        sample_size = min(10, len(template_files))
        sample_files = template_files[:sample_size]
        
        for template_file in sample_files:
            if doc_history_standardizer.has_document_history(template_file):
                content = Path(template_file).read_text(encoding='utf-8')
                
                if language == 'de':
                    # German templates should have German headers
                    has_german_header = ('**Dokumenthistorie:**' in content or 
                                        '## Dokumenthistorie' in content)
                    has_german_columns = ('| Version | Datum | Autor | Änderungen |' in content or
                                         '|Version|Datum|Autor|Änderungen|' in content)
                    
                    assert has_german_header or has_german_columns, \
                        f"German template {template_file} should have German document history format"
                
                elif language == 'en':
                    # English templates should have English headers
                    has_english_header = ('**Document History:**' in content or 
                                         '## Document History' in content)
                    has_english_columns = ('| Version | Date | Author | Changes |' in content or
                                          '|Version|Date|Author|Changes|' in content)
                    
                    assert has_english_header or has_english_columns, \
                        f"English template {template_file} should have English document history format"


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
        import yaml
        
        # Load metadata file
        metadata_file = Path("metadata.example.yaml")
        
        # Skip if file doesn't exist
        if not metadata_file.exists():
            pytest.skip("metadata.example.yaml not found")
        
        # Read YAML content
        with open(metadata_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        # Check roles section exists
        assert 'roles' in data, "metadata.example.yaml should have 'roles' section"
        
        roles = data['roles']
        
        # datenschutzbeauftragter should NOT exist
        assert 'datenschutzbeauftragter' not in roles, \
            "datenschutzbeauftragter should be removed from metadata.example.yaml"
        
        # data_protection_officer should exist
        assert 'data_protection_officer' in roles, \
            "data_protection_officer should exist in metadata.example.yaml"
    
    def test_it_operations_roles_properly_organized(self, role_cleanup):
        """
        Test that IT operations roles are properly organized in metadata.
        
        Feature: template-metadata-standardization
        Property 8: No Duplicate Roles
        Validates: Requirements 10.4, 10.5, 10.8
        """
        import yaml
        
        # Load metadata file
        metadata_file = Path("metadata.example.yaml")
        
        # Skip if file doesn't exist
        if not metadata_file.exists():
            pytest.skip("metadata.example.yaml not found")
        
        # Read YAML content
        with open(metadata_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        # Check roles section exists
        assert 'roles' in data, "metadata.example.yaml should have 'roles' section"
        
        roles = list(data['roles'].keys())
        
        # Check that IT operations roles exist
        it_ops_roles = ['it_operations_manager', 'service_desk_lead', 'it_manager', 'sysop']
        
        for role in it_ops_roles:
            assert role in roles, f"IT operations role '{role}' should exist in metadata"
        
        # Get indices of IT operations roles
        try:
            it_ops_manager_idx = roles.index('it_operations_manager')
            service_desk_idx = roles.index('service_desk_lead')
            it_manager_idx = roles.index('it_manager')
            sysop_idx = roles.index('sysop')
        except ValueError as e:
            pytest.fail(f"Missing IT operations role: {e}")
        
        # Verify IT operations roles are grouped together
        # They should be in order: it_operations_manager, service_desk_lead, it_manager, sysop
        assert it_ops_manager_idx < service_desk_idx, \
            "it_operations_manager should come before service_desk_lead"
        assert service_desk_idx < it_manager_idx, \
            "service_desk_lead should come before it_manager"
        assert it_manager_idx < sysop_idx, \
            "it_manager should come before sysop"
        
        # Verify they are consecutive (no other roles between them)
        it_ops_section = roles[it_ops_manager_idx:sysop_idx + 1]
        assert it_ops_section == it_ops_roles, \
            f"IT operations roles should be consecutive and in order. " \
            f"Expected {it_ops_roles}, found {it_ops_section}"
    
    def test_role_structure_validation_passes(self, role_cleanup):
        """
        Test that role structure validation passes.
        
        Feature: template-metadata-standardization
        Property 8: No Duplicate Roles
        Validates: Requirements 10.8
        """
        # Validate role structure
        validation = role_cleanup.validate_role_structure()
        
        # Should be valid
        assert validation.is_valid, \
            f"Role structure validation failed: {validation.invalid_fields}"
        
        # Should have no errors about duplicate roles
        for error in validation.invalid_fields:
            assert 'duplicate' not in error.lower(), \
                f"Found duplicate role error: {error}"
    
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
        
        # Load metadata file
        metadata_file = Path("metadata.example.yaml")
        
        # Skip if file doesn't exist
        if not metadata_file.exists():
            return
        
        # Read YAML content
        with open(metadata_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        # Skip if no roles section
        if 'roles' not in data:
            return
        
        roles = list(data['roles'].keys())
        
        # Count occurrences of the role name
        count = roles.count(role_name)
        
        # Should appear at most once
        assert count <= 1, \
            f"Role '{role_name}' appears {count} times in metadata.example.yaml"
    
    def test_semantic_duplicate_detection(self, role_cleanup):
        """
        Test that semantic duplicates are detected (roles with same purpose).
        
        Feature: template-metadata-standardization
        Property 8: No Duplicate Roles
        Validates: Requirements 10.1
        """
        import yaml
        
        # Load metadata file
        metadata_file = Path("metadata.example.yaml")
        
        # Skip if file doesn't exist
        if not metadata_file.exists():
            pytest.skip("metadata.example.yaml not found")
        
        # Read YAML content
        with open(metadata_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        # Skip if no roles section
        if 'roles' not in data:
            pytest.skip("No roles section in metadata.example.yaml")
        
        roles = data['roles']
        
        # Check for semantic duplicates by comparing role titles
        role_purposes = {}
        semantic_duplicates = []
        
        for role_name, role_data in roles.items():
            if 'title' in role_data:
                title = role_data['title'].lower()
                
                # Normalize title for comparison
                normalized_title = title.replace('-', ' ').replace('_', ' ')
                
                # Check if we've seen a similar title
                for existing_title, existing_role in role_purposes.items():
                    # Check for semantic similarity
                    if ('data protection' in normalized_title and 'data protection' in existing_title) or \
                       ('datenschutz' in normalized_title and 'datenschutz' in existing_title):
                        semantic_duplicates.append((role_name, existing_role))
                
                role_purposes[normalized_title] = role_name
        
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
        import yaml
        
        # Load metadata file
        metadata_file = Path("metadata.example.yaml")
        
        # Skip if file doesn't exist
        if not metadata_file.exists():
            pytest.skip("metadata.example.yaml not found")
        
        # Read YAML content
        with open(metadata_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        # Skip if no roles section
        if 'roles' not in data:
            pytest.skip("No roles section in metadata.example.yaml")
        
        roles = list(data['roles'].keys())
        
        # Define expected IT operations roles
        expected_it_ops_roles = ['it_operations_manager', 'service_desk_lead', 'it_manager', 'sysop']
        
        # All expected IT ops roles should exist
        for role in expected_it_ops_roles:
            assert role in roles, \
                f"Expected IT operations role '{role}' not found in metadata"
        
        # Get the section of roles between first and last IT ops role
        first_it_ops_idx = roles.index('it_operations_manager')
        last_it_ops_idx = roles.index('sysop')
        
        it_ops_section = roles[first_it_ops_idx:last_it_ops_idx + 1]
        
        # All roles in this section should be IT operations roles
        for role in it_ops_section:
            assert role in expected_it_ops_roles, \
                f"Non-IT operations role '{role}' found in IT operations section"
        
        # Section should contain exactly the expected roles
        assert set(it_ops_section) == set(expected_it_ops_roles), \
            f"IT operations section has unexpected roles. " \
            f"Expected {expected_it_ops_roles}, found {it_ops_section}"
