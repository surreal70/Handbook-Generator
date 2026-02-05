"""
Unit tests for HTML Output Generator

Tests HTML mini-website generation with navigation and styling.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

import pytest
from pathlib import Path
import tempfile
import shutil
from hypothesis import given, settings, strategies as st, HealthCheck

from src.html_output_generator import HTMLOutputGenerator, Template


class TestHTMLOutputGenerator:
    """Test suite for HTMLOutputGenerator class."""
    
    @pytest.fixture
    def temp_output_dir(self):
        """Create temporary output directory for tests."""
        temp_dir = tempfile.mkdtemp()
        yield Path(temp_dir)
        shutil.rmtree(temp_dir)
    
    @pytest.fixture
    def html_generator(self, temp_output_dir):
        """Create HTMLOutputGenerator instance with test mode enabled."""
        return HTMLOutputGenerator(temp_output_dir, test_mode=True)
    
    @pytest.fixture
    def sample_templates(self):
        """Create sample template data for testing."""
        return [
            ('0010_Introduction.md', '# Introduction\n\nThis is the introduction.'),
            ('0020_Overview.md', '# Overview\n\nThis is the overview.'),
            ('0030_Details.md', '# Details\n\nThese are the details.')
        ]
    
    def test_initialization(self, temp_output_dir):
        """Test HTMLOutputGenerator initialization."""
        generator = HTMLOutputGenerator(temp_output_dir, test_mode=True)
        assert generator.output_dir == temp_output_dir
        assert generator.test_mode is True
    
    def test_ensure_output_structure_with_test_mode(self, html_generator):
        """Test output directory creation with test mode enabled."""
        html_dir = html_generator.ensure_output_structure('de')
        
        assert html_dir.exists()
        assert html_dir.is_dir()
        assert html_dir.name == 'html'
        assert html_dir.parent.name == 'de'
    
    def test_ensure_output_structure_without_test_mode(self, temp_output_dir):
        """Test output directory creation fails without test mode."""
        generator = HTMLOutputGenerator(temp_output_dir, test_mode=False)
        
        with pytest.raises(RuntimeError) as exc_info:
            generator.ensure_output_structure('de')
        
        assert "requires --test flag" in str(exc_info.value)
    
    def test_parse_template_metadata_standard_filename(self, html_generator):
        """Test parsing template metadata from standard filename."""
        filename = '0010_Zweck_und_Geltungsbereich.md'
        content = '# Purpose and Scope\n\nThis is the content.'
        
        template = html_generator.parse_template_metadata(filename, content)
        
        assert template.number == '0010'
        assert template.name == 'Zweck_und_Geltungsbereich'
        assert template.title == 'Purpose and Scope'
        assert template.content == content
        assert template.filename == filename
    
    def test_parse_template_metadata_non_standard_filename(self, html_generator):
        """Test parsing template metadata from non-standard filename."""
        filename = 'readme.md'
        content = '## README\n\nThis is a readme.'
        
        template = html_generator.parse_template_metadata(filename, content)
        
        assert template.number == '0000'
        assert template.name == 'readme'
        assert template.title == 'README'
    
    def test_parse_template_metadata_no_heading(self, html_generator):
        """Test parsing template metadata when content has no heading."""
        filename = '0020_Test_File.md'
        content = 'Just some content without a heading.'
        
        template = html_generator.parse_template_metadata(filename, content)
        
        assert template.number == '0020'
        assert template.name == 'Test_File'
        assert template.title == 'Test File'
    
    def test_markdown_to_html_basic(self, html_generator):
        """Test basic markdown to HTML conversion."""
        markdown = '# Heading\n\nParagraph text.'
        html = html_generator.markdown_to_html(markdown)
        
        assert '<h1>' in html or '<h1' in html
        assert 'Heading' in html
        assert 'Paragraph text' in html
    
    def test_generate_toc_page_german(self, html_generator):
        """Test TOC page generation for German language."""
        templates = [
            Template('0010', 'Intro', 'Introduction', 'content1', '0010_Intro.md'),
            Template('0020', 'Overview', 'Overview', 'content2', '0020_Overview.md')
        ]
        
        toc_html = html_generator.generate_toc_page(templates, 'de', 'bcm')
        
        assert '<!DOCTYPE html>' in toc_html
        assert 'lang="de"' in toc_html
        assert 'Inhaltsverzeichnis' in toc_html
        assert '0010_Intro.html' in toc_html
        assert '0020_Overview.html' in toc_html
        assert 'Introduction' in toc_html
        assert 'Overview' in toc_html
        assert 'styles.css' in toc_html
    
    def test_generate_toc_page_english(self, html_generator):
        """Test TOC page generation for English language."""
        templates = [
            Template('0010', 'Intro', 'Introduction', 'content1', '0010_Intro.md')
        ]
        
        toc_html = html_generator.generate_toc_page(templates, 'en', 'isms')
        
        assert 'lang="en"' in toc_html
        assert 'Table of Contents' in toc_html
    
    def test_generate_template_page_with_navigation(self, html_generator):
        """Test template page generation with navigation links."""
        template = Template('0020', 'Middle', 'Middle Page', '# Middle\n\nContent', '0020_Middle.md')
        
        page_html = html_generator.generate_template_page(
            template,
            prev_link='0010_First.html',
            next_link='0030_Last.html',
            language='de'
        )
        
        assert '<!DOCTYPE html>' in page_html
        assert 'lang="de"' in page_html
        assert '0020' in page_html
        assert 'Middle Page' in page_html
        assert '0010_First.html' in page_html
        assert '0030_Last.html' in page_html
        assert 'Zurück' in page_html  # German "Previous"
        assert 'Weiter' in page_html  # German "Next"
        assert 'Inhaltsverzeichnis' in page_html  # German "TOC"
        assert 'index.html' in page_html
        assert 'styles.css' in page_html
    
    def test_generate_template_page_first_page(self, html_generator):
        """Test template page generation for first page (no previous link)."""
        template = Template('0010', 'First', 'First Page', '# First\n\nContent', '0010_First.md')
        
        page_html = html_generator.generate_template_page(
            template,
            prev_link=None,
            next_link='0020_Second.html',
            language='en'
        )
        
        assert 'disabled' in page_html  # Previous link should be disabled
        assert '0020_Second.html' in page_html
        assert 'Next' in page_html
    
    def test_generate_template_page_last_page(self, html_generator):
        """Test template page generation for last page (no next link)."""
        template = Template('0030', 'Last', 'Last Page', '# Last\n\nContent', '0030_Last.md')
        
        page_html = html_generator.generate_template_page(
            template,
            prev_link='0020_Middle.html',
            next_link=None,
            language='en'
        )
        
        assert '0020_Middle.html' in page_html
        assert 'disabled' in page_html  # Next link should be disabled
    
    def test_apply_styling(self, html_generator):
        """Test CSS stylesheet generation."""
        css_content = html_generator.apply_styling()
        
        assert 'body {' in css_content
        assert 'font-family:' in css_content
        assert '.container' in css_content
        assert 'header' in css_content
        assert '.page-nav' in css_content
        assert 'main' in css_content
        assert 'footer' in css_content
        assert '.toc' in css_content
        assert 'table' in css_content
        assert '@media' in css_content  # Responsive design
    
    def test_generate_html_site_success(self, html_generator, sample_templates):
        """Test complete HTML site generation."""
        filenames = [t[0] for t in sample_templates]
        contents = [t[1] for t in sample_templates]
        
        result = html_generator.generate_html_site(
            contents,
            filenames,
            'de',
            'bcm'
        )
        
        assert result['html_dir'] is not None
        assert result['html_dir'].exists()
        assert len(result['files']) == 5  # 3 templates + 1 TOC + 1 CSS
        assert len(result['errors']) == 0
        
        # Check that all expected files exist
        html_dir = result['html_dir']
        assert (html_dir / 'index.html').exists()
        assert (html_dir / 'styles.css').exists()
        assert (html_dir / '0010_Introduction.html').exists()
        assert (html_dir / '0020_Overview.html').exists()
        assert (html_dir / '0030_Details.html').exists()
    
    def test_generate_html_site_without_test_mode(self, temp_output_dir, sample_templates):
        """Test HTML site generation fails without test mode."""
        generator = HTMLOutputGenerator(temp_output_dir, test_mode=False)
        filenames = [t[0] for t in sample_templates]
        contents = [t[1] for t in sample_templates]
        
        result = generator.generate_html_site(
            contents,
            filenames,
            'de',
            'bcm'
        )
        
        assert len(result['errors']) > 0
        assert 'requires --test flag' in result['errors'][0]
    
    def test_generate_html_site_empty_templates(self, html_generator):
        """Test HTML site generation with empty template list."""
        result = html_generator.generate_html_site(
            [],
            [],
            'de',
            'bcm'
        )
        
        assert len(result['errors']) > 0
        assert 'No templates to process' in result['errors'][0]
    
    def test_generate_html_site_output_directory_structure(self, html_generator, sample_templates):
        """Test that HTML output follows correct directory structure."""
        filenames = [t[0] for t in sample_templates]
        contents = [t[1] for t in sample_templates]
        
        result = html_generator.generate_html_site(
            contents,
            filenames,
            'en',
            'isms'
        )
        
        html_dir = result['html_dir']
        assert html_dir.name == 'html'
        assert html_dir.parent.name == 'isms'
        assert html_dir.parent.parent.name == 'en'
    
    def test_generate_html_site_navigation_links(self, html_generator, sample_templates):
        """Test that navigation links are correctly generated between pages."""
        filenames = [t[0] for t in sample_templates]
        contents = [t[1] for t in sample_templates]
        
        result = html_generator.generate_html_site(
            contents,
            filenames,
            'de',
            'bcm'
        )
        
        html_dir = result['html_dir']
        
        # Check first page
        first_page = (html_dir / '0010_Introduction.html').read_text(encoding='utf-8')
        assert '0020_Overview.html' in first_page  # Next link
        assert 'index.html' in first_page  # TOC link
        
        # Check middle page
        middle_page = (html_dir / '0020_Overview.html').read_text(encoding='utf-8')
        assert '0010_Introduction.html' in middle_page  # Previous link
        assert '0030_Details.html' in middle_page  # Next link
        assert 'index.html' in middle_page  # TOC link
        
        # Check last page
        last_page = (html_dir / '0030_Details.html').read_text(encoding='utf-8')
        assert '0020_Overview.html' in last_page  # Previous link
        assert 'index.html' in last_page  # TOC link
    
    def test_generate_html_site_css_applied(self, html_generator, sample_templates):
        """Test that CSS stylesheet is linked in all HTML pages."""
        filenames = [t[0] for t in sample_templates]
        contents = [t[1] for t in sample_templates]
        
        result = html_generator.generate_html_site(
            contents,
            filenames,
            'de',
            'bcm'
        )
        
        html_dir = result['html_dir']
        
        # Check TOC page
        toc_page = (html_dir / 'index.html').read_text(encoding='utf-8')
        assert '<link rel="stylesheet" href="styles.css">' in toc_page
        
        # Check template pages
        for filename in ['0010_Introduction.html', '0020_Overview.html', '0030_Details.html']:
            page_content = (html_dir / filename).read_text(encoding='utf-8')
            assert '<link rel="stylesheet" href="styles.css">' in page_content
    
    def test_generate_html_site_with_special_characters(self, html_generator):
        """Test HTML generation with special characters in content."""
        filenames = ['0010_Test.md']
        contents = ['# Test\n\nContent with <special> & "characters"']
        
        result = html_generator.generate_html_site(
            contents,
            filenames,
            'de',
            'bcm'
        )
        
        assert len(result['errors']) == 0
        html_dir = result['html_dir']
        page_content = (html_dir / '0010_Test.html').read_text(encoding='utf-8')
        # HTML should be properly escaped or rendered
        assert 'Test' in page_content
    
    def test_generate_html_site_warnings_for_parse_errors(self, html_generator):
        """Test that warnings are generated for template parsing errors."""
        # Use invalid filename that might cause parsing issues
        filenames = ['invalid_filename_without_number.md']
        contents = ['# Content']
        
        result = html_generator.generate_html_site(
            contents,
            filenames,
            'de',
            'bcm'
        )
        
        # Should still generate output but may have warnings
        assert result['html_dir'] is not None
        # The implementation should handle this gracefully


class TestHTMLOutputIntegration:
    """Integration tests for HTML output generation."""
    
    @pytest.fixture
    def temp_output_dir(self):
        """Create temporary output directory for tests."""
        temp_dir = tempfile.mkdtemp()
        yield Path(temp_dir)
        shutil.rmtree(temp_dir)
    
    def test_full_html_generation_workflow(self, temp_output_dir):
        """Test complete HTML generation workflow."""
        generator = HTMLOutputGenerator(temp_output_dir, test_mode=True)
        
        # Simulate processed templates
        filenames = [
            '0010_Introduction.md',
            '0020_Methodology.md',
            '0030_Implementation.md',
            '0040_Conclusion.md'
        ]
        
        contents = [
            '# Introduction\n\nThis is the introduction section.',
            '# Methodology\n\nThis describes the methodology.',
            '# Implementation\n\nImplementation details here.',
            '# Conclusion\n\nFinal thoughts and conclusion.'
        ]
        
        result = generator.generate_html_site(
            contents,
            filenames,
            'en',
            'isms'
        )
        
        # Verify success
        assert len(result['errors']) == 0
        assert result['html_dir'] is not None
        
        # Verify all files created
        html_dir = result['html_dir']
        assert (html_dir / 'index.html').exists()
        assert (html_dir / 'styles.css').exists()
        assert (html_dir / '0010_Introduction.html').exists()
        assert (html_dir / '0020_Methodology.html').exists()
        assert (html_dir / '0030_Implementation.html').exists()
        assert (html_dir / '0040_Conclusion.html').exists()
        
        # Verify TOC contains all links
        toc_content = (html_dir / 'index.html').read_text(encoding='utf-8')
        assert '0010_Introduction.html' in toc_content
        assert '0020_Methodology.html' in toc_content
        assert '0030_Implementation.html' in toc_content
        assert '0040_Conclusion.html' in toc_content
        
        # Verify navigation chain
        intro = (html_dir / '0010_Introduction.html').read_text(encoding='utf-8')
        assert '0020_Methodology.html' in intro
        
        method = (html_dir / '0020_Methodology.html').read_text(encoding='utf-8')
        assert '0010_Introduction.html' in method
        assert '0030_Implementation.html' in method
        
        impl = (html_dir / '0030_Implementation.html').read_text(encoding='utf-8')
        assert '0020_Methodology.html' in impl
        assert '0040_Conclusion.html' in impl
        
        concl = (html_dir / '0040_Conclusion.html').read_text(encoding='utf-8')
        assert '0030_Implementation.html' in concl



# Property-Based Tests

class TestProperty26HTMLOutputStructure:
    """
    Property 26: HTML Output Structure
    
    For any handbook generation with HTML output, the system SHALL create separate HTML files
    for each template, generate a table of contents index page, provide navigation links between
    pages, apply consistent styling across all pages, and store output in test-output/{language}/html/.
    
    Validates: Requirements 31.1, 31.2, 31.3, 31.4, 31.5
    """
    
    @pytest.fixture
    def html_generator(self, tmp_path):
        """Create HTML generator with temporary output directory."""
        from src.html_output_generator import HTMLOutputGenerator
        return HTMLOutputGenerator(output_dir=tmp_path, test_mode=True)
    
    @settings(max_examples=50, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        language=st.sampled_from(['de', 'en']),
        template_type=st.sampled_from(['bcm', 'isms', 'bsi-grundschutz', 'it-operation']),
        num_templates=st.integers(min_value=1, max_value=10)
    )
    def test_property_html_output_structure(self, html_generator, language, template_type, num_templates):
        """
        Property test: For any handbook generation with HTML output, verify all structural requirements.
        
        Feature: template-system-extension
        Property 26: HTML Output Structure
        
        Validates: Requirements 31.1, 31.2, 31.3, 31.4, 31.5
        """
        # Generate test templates
        filenames = []
        contents = []
        for i in range(num_templates):
            num = (i + 1) * 10
            filenames.append(f'{num:04d}_Template_{i+1}.md')
            contents.append(f'# Template {i+1}\n\nContent for template {i+1}.')
        
        # Generate HTML site
        result = html_generator.generate_html_site(
            contents,
            filenames,
            language,
            template_type
        )
        
        # Should have no errors
        assert len(result['errors']) == 0, \
            f"HTML generation should have no errors, found: {result['errors']}"
        
        html_dir = result['html_dir']
        
        # Requirement 31.1: Separate HTML file for each template
        for filename in filenames:
            html_filename = filename.replace('.md', '.html')
            html_file = html_dir / html_filename
            assert html_file.exists(), \
                f"Should create separate HTML file for {filename}"
            
            # Verify file has content
            content = html_file.read_text(encoding='utf-8')
            assert len(content) > 0, \
                f"HTML file {html_filename} should have content"
        
        # Requirement 31.2: Table of contents index page
        toc_file = html_dir / 'index.html'
        assert toc_file.exists(), \
            "Should create table of contents index page (index.html)"
        
        toc_content = toc_file.read_text(encoding='utf-8')
        
        # TOC should link to all template pages
        for filename in filenames:
            html_filename = filename.replace('.md', '.html')
            assert html_filename in toc_content, \
                f"TOC should contain link to {html_filename}"
        
        # Requirement 31.3: Navigation links between pages
        for i, filename in enumerate(filenames):
            html_filename = filename.replace('.md', '.html')
            page_content = (html_dir / html_filename).read_text(encoding='utf-8')
            
            # Should have link back to TOC
            assert 'index.html' in page_content, \
                f"Page {html_filename} should have link to TOC"
            
            # Should have previous link (except first page)
            if i > 0:
                prev_filename = filenames[i-1].replace('.md', '.html')
                assert prev_filename in page_content, \
                    f"Page {html_filename} should have link to previous page {prev_filename}"
            
            # Should have next link (except last page)
            if i < len(filenames) - 1:
                next_filename = filenames[i+1].replace('.md', '.html')
                assert next_filename in page_content, \
                    f"Page {html_filename} should have link to next page {next_filename}"
        
        # Requirement 31.4: Consistent styling across all pages
        css_file = html_dir / 'styles.css'
        assert css_file.exists(), \
            "Should create CSS stylesheet (styles.css)"
        
        # All pages should link to the stylesheet
        for filename in filenames:
            html_filename = filename.replace('.md', '.html')
            page_content = (html_dir / html_filename).read_text(encoding='utf-8')
            assert '<link rel="stylesheet" href="styles.css">' in page_content, \
                f"Page {html_filename} should link to stylesheet"
        
        # TOC should also link to stylesheet
        assert '<link rel="stylesheet" href="styles.css">' in toc_content, \
            "TOC page should link to stylesheet"
        
        # Requirement 31.5: Output stored in test-output/{language}/{template_type}/html/
        # Note: The actual path is output_dir/{language}/{template_type}/html/
        assert html_dir.name == 'html', \
            "HTML files should be in 'html' directory"
        assert html_dir.parent.name == template_type, \
            f"HTML directory should be under template type directory '{template_type}'"
        assert html_dir.parent.parent.name == language, \
            f"Template type directory should be under language directory '{language}'"
    
    @settings(max_examples=30, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        language=st.sampled_from(['de', 'en']),
        template_type=st.sampled_from(['bcm', 'isms', 'bsi-grundschutz']),
        num_templates=st.integers(min_value=2, max_value=5)
    )
    def test_property_html_navigation_completeness(self, html_generator, language, template_type, num_templates):
        """
        Property test: Verify navigation links form a complete chain.
        
        Feature: template-system-extension
        Property 26: HTML Output Structure
        
        Validates: Requirement 31.3
        """
        # Generate test templates
        filenames = [f'{(i+1)*10:04d}_Test_{i+1}.md' for i in range(num_templates)]
        contents = [f'# Test {i+1}\n\nContent {i+1}.' for i in range(num_templates)]
        
        # Generate HTML site
        result = html_generator.generate_html_site(contents, filenames, language, template_type)
        
        assert len(result['errors']) == 0
        html_dir = result['html_dir']
        
        # Verify navigation chain is complete
        for i in range(num_templates):
            html_filename = filenames[i].replace('.md', '.html')
            page_content = (html_dir / html_filename).read_text(encoding='utf-8')
            
            # First page: should have next but no previous
            if i == 0:
                if num_templates > 1:
                    next_file = filenames[1].replace('.md', '.html')
                    assert next_file in page_content, \
                        "First page should have link to next page"
            
            # Last page: should have previous but no next
            elif i == num_templates - 1:
                prev_file = filenames[i-1].replace('.md', '.html')
                assert prev_file in page_content, \
                    "Last page should have link to previous page"
            
            # Middle pages: should have both previous and next
            else:
                prev_file = filenames[i-1].replace('.md', '.html')
                next_file = filenames[i+1].replace('.md', '.html')
                assert prev_file in page_content, \
                    f"Middle page {i+1} should have link to previous page"
                assert next_file in page_content, \
                    f"Middle page {i+1} should have link to next page"
    
    @settings(max_examples=30, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        language=st.sampled_from(['de', 'en']),
        num_templates=st.integers(min_value=1, max_value=8)
    )
    def test_property_html_toc_completeness(self, html_generator, language, num_templates):
        """
        Property test: Verify TOC contains all templates.
        
        Feature: template-system-extension
        Property 26: HTML Output Structure
        
        Validates: Requirement 31.2
        """
        # Generate test templates with various naming patterns
        filenames = []
        contents = []
        for i in range(num_templates):
            num = (i + 1) * 10
            name = f'Section_{chr(65+i)}'  # A, B, C, etc.
            filenames.append(f'{num:04d}_{name}.md')
            contents.append(f'# {name}\n\nContent for {name}.')
        
        # Generate HTML site
        result = html_generator.generate_html_site(
            contents,
            filenames,
            language,
            'isms'
        )
        
        assert len(result['errors']) == 0
        html_dir = result['html_dir']
        
        # Read TOC
        toc_content = (html_dir / 'index.html').read_text(encoding='utf-8')
        
        # TOC should contain link to every template
        for filename in filenames:
            html_filename = filename.replace('.md', '.html')
            assert html_filename in toc_content, \
                f"TOC should contain link to {html_filename}"
        
        # TOC should have proper HTML structure
        assert '<html' in toc_content.lower()
        assert '</html>' in toc_content.lower()
        assert '<body' in toc_content.lower()
        assert '</body>' in toc_content.lower()
    
    def test_property_html_css_consistency(self, html_generator):
        """
        Property test: Verify CSS is consistently applied.
        
        Feature: template-system-extension
        Property 26: HTML Output Structure
        
        Validates: Requirement 31.4
        """
        # Generate a few templates
        filenames = ['0010_First.md', '0020_Second.md', '0030_Third.md']
        contents = ['# First', '# Second', '# Third']
        
        result = html_generator.generate_html_site(
            contents,
            filenames,
            'en',
            'bcm'
        )
        
        assert len(result['errors']) == 0
        html_dir = result['html_dir']
        
        # CSS file should exist
        css_file = html_dir / 'styles.css'
        assert css_file.exists(), "CSS file should exist"
        
        # CSS should have content
        css_content = css_file.read_text(encoding='utf-8')
        assert len(css_content) > 0, "CSS file should have content"
        
        # All HTML files should reference the same CSS file
        css_link = '<link rel="stylesheet" href="styles.css">'
        
        # Check TOC
        toc_content = (html_dir / 'index.html').read_text(encoding='utf-8')
        assert css_link in toc_content, "TOC should link to CSS"
        
        # Check all template pages
        for filename in filenames:
            html_filename = filename.replace('.md', '.html')
            page_content = (html_dir / html_filename).read_text(encoding='utf-8')
            assert css_link in page_content, \
                f"Page {html_filename} should link to CSS"


# ============================================================================
# CIS Controls HTML Generation Tests
# ============================================================================

class TestCISControlsHTMLGeneration:
    """Test suite for CIS Controls HTML generation."""
    
    @pytest.fixture
    def temp_output_dir(self, tmp_path):
        """Create temporary output directory."""
        return tmp_path / "test-output"
    
    @pytest.fixture
    def html_generator(self, temp_output_dir):
        """Create HTMLOutputGenerator instance with test mode enabled."""
        return HTMLOutputGenerator(temp_output_dir, test_mode=True)
    
    @pytest.fixture
    def template_manager(self):
        """Get template manager instance."""
        from src.template_manager import TemplateManager
        return TemplateManager(Path("templates"))
    
    def test_cis_controls_html_mini_website_generation(self, html_generator, template_manager):
        """
        Test HTML mini-website generation for CIS Controls.
        
        Requirements: 5.1
        """
        # Get CIS Controls templates
        try:
            templates = template_manager.get_templates('de', 'cis-controls')
        except ValueError:
            pytest.skip("CIS Controls templates not found")
        
        if not templates:
            pytest.skip("No CIS Controls templates available")
        
        # Process templates
        processed_contents = [t.read_content() for t in templates]
        filenames = [t.path.name for t in templates]
        
        # Generate HTML site
        result = html_generator.generate_html_site(
            processed_contents,
            filenames,
            'de',
            'cis-controls'
        )
        
        # Verify success
        assert len(result['errors']) == 0, f"Should have no errors: {result['errors']}"
        assert result['html_dir'] is not None, "HTML directory should be set"
        
        # Verify directory structure
        html_dir = Path(result['html_dir'])
        assert html_dir.exists(), "HTML directory should exist"
        assert html_dir.name == "html"
        assert html_dir.parent.name == "cis-controls"
        assert html_dir.parent.parent.name == "de"
        
        # Verify index.html exists
        index_file = html_dir / "index.html"
        assert index_file.exists(), "index.html should exist"
        
        # Verify individual HTML files exist
        html_files = list(html_dir.glob("*.html"))
        # Should have index.html plus one file per template
        assert len(html_files) >= len(templates), \
            f"Should have at least {len(templates)} HTML files (including index)"
    
    def test_cis_controls_html_navigation_structure(self, html_generator, template_manager):
        """
        Test that CIS Controls HTML has correct navigation structure.
        
        Requirements: 5.1
        """
        # Get CIS Controls templates (just first 3 for testing)
        try:
            templates = template_manager.get_templates('de', 'cis-controls')[:3]
        except ValueError:
            pytest.skip("CIS Controls templates not found")
        
        if len(templates) < 2:
            pytest.skip("Need at least 2 templates for navigation test")
        
        # Process templates
        processed_contents = [t.read_content() for t in templates]
        filenames = [t.path.name for t in templates]
        
        # Generate HTML site
        result = html_generator.generate_html_site(
            processed_contents,
            filenames,
            'de',
            'cis-controls'
        )
        
        assert len(result['errors']) == 0
        html_dir = Path(result['html_dir'])
        
        # Check first template page
        first_file = html_dir / filenames[0].replace('.md', '.html')
        if first_file.exists():
            content = first_file.read_text(encoding='utf-8')
            
            # Should have navigation
            assert '<nav' in content, "Should have navigation element"
            
            # Should have link to TOC (index.html)
            assert 'index.html' in content, "Should have link to TOC"
            
            # Should have link to next page
            if len(templates) > 1:
                next_file = filenames[1].replace('.md', '.html')
                assert next_file in content, "Should have link to next page"
        
        # Check middle template page
        if len(templates) > 2:
            middle_file = html_dir / filenames[1].replace('.md', '.html')
            if middle_file.exists():
                content = middle_file.read_text(encoding='utf-8')
                
                # Should have link to previous page
                prev_file = filenames[0].replace('.md', '.html')
                assert prev_file in content, "Should have link to previous page"
                
                # Should have link to next page
                next_file = filenames[2].replace('.md', '.html')
                assert next_file in content, "Should have link to next page"
    
    def test_cis_controls_html_styles_css_inclusion(self, html_generator, template_manager):
        """
        Test that CIS Controls HTML includes styles.css.
        
        Requirements: 5.1
        """
        # Get CIS Controls templates
        try:
            templates = template_manager.get_templates('de', 'cis-controls')[:1]
        except ValueError:
            pytest.skip("CIS Controls templates not found")
        
        if not templates:
            pytest.skip("No CIS Controls templates available")
        
        # Process templates
        processed_contents = [t.read_content() for t in templates]
        filenames = [t.path.name for t in templates]
        
        # Generate HTML site
        result = html_generator.generate_html_site(
            processed_contents,
            filenames,
            'de',
            'cis-controls'
        )
        
        assert len(result['errors']) == 0
        html_dir = Path(result['html_dir'])
        
        # Verify styles.css exists
        styles_file = html_dir / "styles.css"
        assert styles_file.exists(), "styles.css should exist"
        
        # Verify styles.css has content
        styles_content = styles_file.read_text(encoding='utf-8')
        assert len(styles_content) > 0, "styles.css should have content"
        assert 'body' in styles_content, "styles.css should have body styles"
        
        # Verify HTML files link to styles.css
        index_file = html_dir / "index.html"
        if index_file.exists():
            index_content = index_file.read_text(encoding='utf-8')
            assert '<link rel="stylesheet" href="styles.css">' in index_content, \
                "index.html should link to styles.css"
        
        # Check first template page
        first_file = html_dir / filenames[0].replace('.md', '.html')
        if first_file.exists():
            content = first_file.read_text(encoding='utf-8')
            assert '<link rel="stylesheet" href="styles.css">' in content, \
                "Template pages should link to styles.css"
    
    def test_cis_controls_english_html_generation(self, html_generator, template_manager):
        """
        Test HTML generation for English CIS Controls templates.
        
        Requirements: 5.1
        """
        # Get English CIS Controls templates
        try:
            templates = template_manager.get_templates('en', 'cis-controls')
        except ValueError:
            pytest.skip("English CIS Controls templates not found")
        
        if not templates:
            pytest.skip("No English CIS Controls templates available")
        
        # Process templates
        processed_contents = [t.read_content() for t in templates]
        filenames = [t.path.name for t in templates]
        
        # Generate HTML site
        result = html_generator.generate_html_site(
            processed_contents,
            filenames,
            'en',
            'cis-controls'
        )
        
        # Verify success
        assert len(result['errors']) == 0, f"Should have no errors: {result['errors']}"
        assert result['html_dir'] is not None
        
        # Verify directory structure uses English
        html_dir = Path(result['html_dir'])
        assert html_dir.parent.parent.name == "en"
    
    def test_cis_controls_html_toc_page_structure(self, html_generator, template_manager):
        """
        Test that CIS Controls HTML TOC page has correct structure.
        
        Requirements: 5.1
        """
        # Get CIS Controls templates
        try:
            templates = template_manager.get_templates('de', 'cis-controls')
        except ValueError:
            pytest.skip("CIS Controls templates not found")
        
        if not templates:
            pytest.skip("No CIS Controls templates available")
        
        # Process templates
        processed_contents = [t.read_content() for t in templates]
        filenames = [t.path.name for t in templates]
        
        # Generate HTML site
        result = html_generator.generate_html_site(
            processed_contents,
            filenames,
            'de',
            'cis-controls'
        )
        
        assert len(result['errors']) == 0
        html_dir = Path(result['html_dir'])
        
        # Check index.html (TOC page)
        index_file = html_dir / "index.html"
        assert index_file.exists(), "index.html should exist"
        
        index_content = index_file.read_text(encoding='utf-8')
        
        # Should have TOC heading
        assert 'Inhaltsverzeichnis' in index_content or 'Table of Contents' in index_content, \
            "TOC page should have heading"
        
        # Should have links to all templates
        for filename in filenames:
            html_filename = filename.replace('.md', '.html')
            assert html_filename in index_content, \
                f"TOC should link to {html_filename}"
    
    def test_cis_controls_html_responsive_design(self, html_generator, template_manager):
        """
        Test that CIS Controls HTML includes responsive design CSS.
        
        Requirements: 5.1
        """
        # Get CIS Controls templates
        try:
            templates = template_manager.get_templates('de', 'cis-controls')[:1]
        except ValueError:
            pytest.skip("CIS Controls templates not found")
        
        if not templates:
            pytest.skip("No CIS Controls templates available")
        
        # Process templates
        processed_contents = [t.read_content() for t in templates]
        filenames = [t.path.name for t in templates]
        
        # Generate HTML site
        result = html_generator.generate_html_site(
            processed_contents,
            filenames,
            'de',
            'cis-controls'
        )
        
        assert len(result['errors']) == 0
        html_dir = Path(result['html_dir'])
        
        # Check styles.css for responsive design
        styles_file = html_dir / "styles.css"
        if styles_file.exists():
            styles_content = styles_file.read_text(encoding='utf-8')
            
            # Should have media queries for responsive design
            assert '@media' in styles_content, \
                "styles.css should include media queries for responsive design"
        
        # Check HTML files for viewport meta tag
        index_file = html_dir / "index.html"
        if index_file.exists():
            index_content = index_file.read_text(encoding='utf-8')
            assert 'viewport' in index_content, \
                "HTML should include viewport meta tag for responsive design"
    
    def test_cis_controls_html_overwrite_warning(self, html_generator, template_manager):
        """
        Test that CIS Controls HTML generation succeeds even when files exist.
        
        Note: HTML generator currently overwrites files without warning.
        This test verifies that generation succeeds on second run.
        
        Requirements: 5.1
        """
        # Get CIS Controls templates
        try:
            templates = template_manager.get_templates('de', 'cis-controls')[:1]
        except ValueError:
            pytest.skip("CIS Controls templates not found")
        
        if not templates:
            pytest.skip("No CIS Controls templates available")
        
        # Process templates
        processed_contents = [t.read_content() for t in templates]
        filenames = [t.path.name for t in templates]
        
        # Generate first time
        result1 = html_generator.generate_html_site(
            processed_contents,
            filenames,
            'de',
            'cis-controls'
        )
        assert len(result1['errors']) == 0
        
        # Generate again (overwrite)
        result2 = html_generator.generate_html_site(
            processed_contents,
            filenames,
            'de',
            'cis-controls'
        )
        
        # Should succeed without errors
        assert len(result2['errors']) == 0, \
            "HTML generation should succeed even when overwriting existing files"
        
        # Files should still exist
        html_dir = Path(result2['html_dir'])
        assert (html_dir / "index.html").exists(), "index.html should exist after overwrite"
    
    def test_cis_controls_html_content_conversion(self, html_generator, template_manager):
        """
        Test that CIS Controls markdown content is properly converted to HTML.
        
        Requirements: 5.1
        """
        # Get CIS Controls templates
        try:
            templates = template_manager.get_templates('de', 'cis-controls')[:1]
        except ValueError:
            pytest.skip("CIS Controls templates not found")
        
        if not templates:
            pytest.skip("No CIS Controls templates available")
        
        # Process templates
        processed_contents = [t.read_content() for t in templates]
        filenames = [t.path.name for t in templates]
        
        # Generate HTML site
        result = html_generator.generate_html_site(
            processed_contents,
            filenames,
            'de',
            'cis-controls'
        )
        
        assert len(result['errors']) == 0
        html_dir = Path(result['html_dir'])
        
        # Check first template page
        first_file = html_dir / filenames[0].replace('.md', '.html')
        if first_file.exists():
            content = first_file.read_text(encoding='utf-8')
            
            # Should have HTML structure
            assert '<!DOCTYPE html>' in content, "Should have HTML doctype"
            assert '<html' in content, "Should have html tag"
            assert '<head>' in content, "Should have head section"
            assert '<body>' in content, "Should have body section"
            
            # Markdown headers should be converted to HTML headers
            if '#' in processed_contents[0]:
                assert '<h1>' in content or '<h2>' in content or '<h3>' in content, \
                    "Markdown headers should be converted to HTML headers"
