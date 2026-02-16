"""
Tests for Coverage Documentation Generator.

This module contains unit tests and property-based tests for the
CoverageDocumentationGenerator class.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

import os
import tempfile
from pathlib import Path
import pytest
from hypothesis import given, strategies as st

from src.quality_control.coverage_documentation_generator import CoverageDocumentationGenerator
from src.quality_control.data_structures import Framework


class TestCoverageDocumentationGenerator:
    """Unit tests for CoverageDocumentationGenerator."""
    
    def test_discover_frameworks_empty_directory(self):
        """Test framework discovery with empty directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create empty templates directory
            templates_dir = Path(tmpdir) / "templates"
            templates_dir.mkdir()
            (templates_dir / "de").mkdir()
            (templates_dir / "en").mkdir()
            
            generator = CoverageDocumentationGenerator(tmpdir)
            frameworks = generator.discover_frameworks()
            
            assert len(frameworks) == 0
    
    def test_discover_frameworks_single_framework(self):
        """Test framework discovery with single framework."""
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create framework directories
            templates_dir = Path(tmpdir) / "templates"
            de_dir = templates_dir / "de" / "isms"
            en_dir = templates_dir / "en" / "isms"
            de_dir.mkdir(parents=True)
            en_dir.mkdir(parents=True)
            
            # Create template files
            (de_dir / "0010_Template.md").write_text("# Template")
            (en_dir / "0010_Template.md").write_text("# Template")
            
            generator = CoverageDocumentationGenerator(tmpdir)
            frameworks = generator.discover_frameworks()
            
            assert len(frameworks) == 1
            assert frameworks[0].name == "isms"
            assert frameworks[0].template_count_de == 1
            assert frameworks[0].template_count_en == 1
            assert frameworks[0].bilingual_consistent is True
    
    def test_count_templates_excludes_metadata(self):
        """Test that template counting excludes metadata files."""
        with tempfile.TemporaryDirectory() as tmpdir:
            framework_dir = Path(tmpdir)
            
            # Create various files
            (framework_dir / "0010_Template.md").write_text("# Template")
            (framework_dir / "0020_Template.md").write_text("# Template")
            (framework_dir / "metadata.yaml").write_text("key: value")
            (framework_dir / "9999_Framework_Mapping.md").write_text("# Mapping")
            (framework_dir / "README.md").write_text("# README")
            
            generator = CoverageDocumentationGenerator()
            count = generator._count_templates(framework_dir)
            
            assert count == 2  # Only the two template files
    
    def test_extract_metadata_missing_readme(self):
        """Test metadata extraction with missing README."""
        with tempfile.TemporaryDirectory() as tmpdir:
            framework_dir = Path(tmpdir)
            
            generator = CoverageDocumentationGenerator()
            metadata = generator._extract_metadata(framework_dir)
            
            assert metadata['standard'] == ''
            assert metadata['description'] == ''
    
    def test_extract_metadata_with_readme(self):
        """Test metadata extraction with README file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            framework_dir = Path(tmpdir)
            readme_path = framework_dir / "README.md"
            
            readme_content = """# ISO 27001:2022
            
This is a framework for information security management.
It provides comprehensive controls for security.
"""
            readme_path.write_text(readme_content)
            
            generator = CoverageDocumentationGenerator()
            metadata = generator._extract_metadata(framework_dir)
            
            assert 'ISO 27001:2022' in metadata['standard']
            assert len(metadata['description']) > 0
    
    def test_discover_frameworks_missing_templates_directory(self):
        """Test framework discovery when templates directory doesn't exist."""
        with tempfile.TemporaryDirectory() as tmpdir:
            generator = CoverageDocumentationGenerator(tmpdir)
            frameworks = generator.discover_frameworks()
            
            assert len(frameworks) == 0
    
    def test_count_templates_empty_framework_directory(self):
        """Test template counting with empty framework directory."""
        with tempfile.TemporaryDirectory() as tmpdir:
            framework_dir = Path(tmpdir)
            
            generator = CoverageDocumentationGenerator()
            count = generator._count_templates(framework_dir)
            
            assert count == 0
    
    def test_extract_metadata_malformed_readme(self):
        """Test metadata extraction with malformed README content."""
        with tempfile.TemporaryDirectory() as tmpdir:
            framework_dir = Path(tmpdir)
            readme_path = framework_dir / "README.md"
            
            # Create malformed README
            readme_content = "This is not a proper markdown file\nNo headers\nJust text"
            readme_path.write_text(readme_content)
            
            generator = CoverageDocumentationGenerator()
            metadata = generator._extract_metadata(framework_dir)
            
            # Should handle gracefully
            assert 'standard' in metadata
            assert 'description' in metadata
    
    def test_save_documentation_creates_directory(self):
        """Test that save_documentation creates output directory if needed."""
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "new_dir" / "output.md"
            
            generator = CoverageDocumentationGenerator()
            content = "# Test Documentation"
            generator.save_documentation(content, str(output_path))
            
            assert output_path.exists()
            assert output_path.read_text() == content
    
    def test_bilingual_consistency_with_missing_language(self):
        """Test bilingual consistency check when one language is missing."""
        framework = Framework(
            name="test",
            standard="Test",
            description="Test",
            template_count_de=5,
            template_count_en=0,
            path_de=Path("/test/de/test"),
            path_en=Path(),
            bilingual_consistent=False
        )
        
        generator = CoverageDocumentationGenerator()
        report = generator.check_bilingual_consistency([framework])
        
        assert len(report.inconsistent_frameworks) == 1
        assert len(report.missing_translations) == 1
        assert report.missing_translations[0] == (framework, 'en')


class TestCoverageDocumentationGeneratorProperties:
    """Property-based tests for CoverageDocumentationGenerator."""
    
    @given(st.lists(st.text(min_size=1, max_size=20, alphabet=st.characters(
        whitelist_categories=('Ll', 'Lu', 'Nd'), whitelist_characters='_-'
    )), min_size=0, max_size=20))
    def test_property_accurate_counting(self, template_names):
        """
        Feature: quality-control-and-framework-documentation
        Property 5: Accurate Counting
        
        For any directory containing template files, the count reported by
        the system should equal the actual number of files matching the criteria.
        
        Validates: Requirements 2.6, 3.7, 4.4, 4.9
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            framework_dir = Path(tmpdir)
            
            # Create template files (deduplicate names to avoid file overwrites)
            created_files = set()
            for name in template_names:
                if name and not name.startswith('metadata') and \
                   not name.endswith('Framework_Mapping') and \
                   name.lower() != 'readme':
                    filename = f"{name}.md"
                    (framework_dir / filename).write_text(f"# {name}")
                    created_files.add(filename)
            
            expected_count = len(created_files)
            
            # Create some excluded files
            (framework_dir / "metadata.yaml").write_text("key: value")
            (framework_dir / "9999_Framework_Mapping.md").write_text("# Mapping")
            (framework_dir / "README.md").write_text("# README")
            
            generator = CoverageDocumentationGenerator()
            actual_count = generator._count_templates(framework_dir)
            
            assert actual_count == expected_count, \
                f"Expected {expected_count} templates, but counted {actual_count}"
    
    @given(
        st.text(min_size=1, max_size=100, alphabet=st.characters(
            whitelist_categories=('Lu', 'Ll', 'Nd', 'Zs'), whitelist_characters=':-.'
        )),
        st.text(min_size=1, max_size=200, alphabet=st.characters(
            whitelist_categories=('Lu', 'Ll', 'Nd', 'Zs', 'Po')
        ))
    )
    def test_property_framework_metadata_extraction(self, standard, description):
        """
        Feature: quality-control-and-framework-documentation
        Property 9: Framework Metadata Extraction
        
        For any framework directory containing a README.md file, the
        Documentation_Generator should extract the framework name, standard,
        and description.
        
        Validates: Requirements 4.2, 4.3
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            framework_dir = Path(tmpdir)
            readme_path = framework_dir / "README.md"
            
            # Create README with standard and description
            readme_content = f"# {standard}\n\n{description}\n"
            readme_path.write_text(readme_content)
            
            generator = CoverageDocumentationGenerator()
            metadata = generator._extract_metadata(framework_dir)
            
            # Verify metadata was extracted
            assert 'standard' in metadata
            assert 'description' in metadata
            
            # Verify standard contains the input standard
            assert standard in metadata['standard'] or metadata['standard'] == ''
            
            # Verify description is not empty if input description was not empty
            if description.strip():
                assert len(metadata['description']) > 0
    
    @given(st.lists(st.tuples(
        st.text(min_size=1, max_size=20, alphabet=st.characters(
            whitelist_categories=('Ll', 'Lu', 'Nd'), whitelist_characters='_-'
        )),
        st.integers(min_value=0, max_value=100),
        st.integers(min_value=0, max_value=100)
    ), min_size=0, max_size=20))
    def test_property_bilingual_consistency_detection(self, framework_data):
        """
        Feature: quality-control-and-framework-documentation
        Property 10: Bilingual Consistency Detection
        
        For any pair of German and English framework directories, the
        Documentation_Generator should correctly identify whether template
        counts match.
        
        Validates: Requirements 4.5, 4.6
        """
        frameworks = []
        
        for name, count_de, count_en in framework_data:
            if not name:
                continue
                
            framework = Framework(
                name=name,
                standard="Test Standard",
                description="Test Description",
                template_count_de=count_de,
                template_count_en=count_en,
                path_de=Path("/test/de") / name,
                path_en=Path("/test/en") / name,
                bilingual_consistent=(count_de == count_en)
            )
            frameworks.append(framework)
        
        generator = CoverageDocumentationGenerator()
        report = generator.check_bilingual_consistency(frameworks)
        
        # Verify all frameworks are categorized
        total_categorized = len(report.consistent_frameworks) + len(report.inconsistent_frameworks)
        assert total_categorized == len(frameworks)
        
        # Verify consistent frameworks have matching counts
        for framework in report.consistent_frameworks:
            assert framework.template_count_de == framework.template_count_en
        
        # Verify inconsistent frameworks have different counts
        for framework in report.inconsistent_frameworks:
            assert framework.template_count_de != framework.template_count_en
        
        # Verify missing translations are correctly identified
        for framework, language in report.missing_translations:
            if language == 'de':
                assert framework.template_count_en > framework.template_count_de
            elif language == 'en':
                assert framework.template_count_de > framework.template_count_en
    
    @given(st.lists(st.tuples(
        st.text(min_size=1, max_size=20, alphabet=st.characters(
            whitelist_categories=('Ll', 'Lu', 'Nd'), whitelist_characters='_-'
        )),
        st.text(min_size=1, max_size=50, alphabet=st.characters(
            whitelist_categories=('Lu', 'Ll', 'Nd', 'Zs'), whitelist_characters=':-.'
        )),
        st.integers(min_value=0, max_value=50),
        st.integers(min_value=0, max_value=50)
    ), min_size=0, max_size=10))
    def test_property_markdown_format_validity(self, framework_data):
        """
        Feature: quality-control-and-framework-documentation
        Property 11: Markdown Format Validity
        
        For any set of frameworks, the generated coverage documentation should
        be valid Markdown with a properly formatted table containing all
        required columns.
        
        Validates: Requirements 4.8
        """
        frameworks = []
        
        for name, standard, count_de, count_en in framework_data:
            if not name:
                continue
                
            framework = Framework(
                name=name,
                standard=standard,
                description="Test description",
                template_count_de=count_de,
                template_count_en=count_en,
                path_de=Path("/test/de") / name,
                path_en=Path("/test/en") / name,
                bilingual_consistent=(count_de == count_en)
            )
            frameworks.append(framework)
        
        generator = CoverageDocumentationGenerator()
        markdown = generator.generate_markdown_documentation(frameworks)
        
        # Verify Markdown structure
        assert "# Framework Coverage Documentation" in markdown
        assert "## Summary" in markdown
        assert "## Frameworks" in markdown
        
        # Verify table header exists
        assert "| Framework | Standard | Templates (DE) | Templates (EN) | Consistent | Description |" in markdown
        assert "|-----------|----------|----------------|----------------|------------|-------------|" in markdown
        
        # Verify summary statistics
        assert f"**Total Frameworks**: {len(frameworks)}" in markdown
        
        # Verify each framework appears in the table
        for framework in frameworks:
            assert framework.name in markdown
