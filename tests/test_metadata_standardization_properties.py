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
