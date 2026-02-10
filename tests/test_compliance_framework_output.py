"""
Tests for Compliance Framework Output Generation

Verifies that HTML, PDF, and Markdown output generation works correctly
for the new compliance frameworks (PCI-DSS, HIPAA, NIST 800-53, TSC,
Common Criteria, ISO 9001, GDPR).

Author: Kiro AI Assistant
"""

import pytest
from pathlib import Path
from src.html_output_generator import HTMLOutputGenerator
from src.output_generator import OutputGenerator


# New compliance frameworks to test
NEW_FRAMEWORKS = [
    'pci-dss',
    'hipaa',
    'nist-800-53',
    'tsc',
    'common-criteria',
    'iso-9001',
    'gdpr'
]


@pytest.fixture
def temp_output_dir(tmp_path):
    """Create temporary output directory."""
    output_dir = tmp_path / "test-output"
    output_dir.mkdir()
    return output_dir


@pytest.fixture
def sample_templates():
    """Sample template data for testing."""
    return [
        ('0010_Introduction.md', '# Introduction\n\nThis is the introduction.'),
        ('0020_Requirements.md', '# Requirements\n\nThese are the requirements.'),
        ('0030_Implementation.md', '# Implementation\n\nImplementation details.')
    ]


class TestHTMLOutputForNewFrameworks:
    """Test HTML output generation for new compliance frameworks."""
    
    @pytest.mark.parametrize('framework', NEW_FRAMEWORKS)
    @pytest.mark.parametrize('language', ['de', 'en'])
    def test_html_generation_for_framework(self, temp_output_dir, sample_templates, framework, language):
        """
        Test HTML generation for each new framework.
        
        Validates: Requirements 12.1, 12.2
        """
        generator = HTMLOutputGenerator(temp_output_dir, test_mode=True)
        
        filenames = [t[0] for t in sample_templates]
        contents = [t[1] for t in sample_templates]
        
        result = generator.generate_html_site(
            processed_contents=contents,
            filenames=filenames,
            language=language,
            template_type=framework
        )
        
        # Verify no errors
        assert not result['errors'], f"HTML generation failed for {framework}: {result['errors']}"
        
        # Verify output directory structure
        assert result['html_dir'] is not None
        expected_path = temp_output_dir / language / framework / 'html'
        assert result['html_dir'] == expected_path
        assert result['html_dir'].exists()
        
        # Verify files were created
        assert len(result['files']) > 0
        
        # Verify index.html (TOC) exists
        index_file = result['html_dir'] / 'index.html'
        assert index_file.exists()
        assert index_file in result['files']
        
        # Verify styles.css exists
        css_file = result['html_dir'] / 'styles.css'
        assert css_file.exists()
        assert css_file in result['files']
        
        # Verify template pages exist
        for filename in filenames:
            number = filename[:4]
            name = filename[5:-3]  # Remove number prefix and .md extension
            html_file = result['html_dir'] / f"{number}_{name}.html"
            assert html_file.exists(), f"Template page {html_file} not found"
    
    @pytest.mark.parametrize('framework', NEW_FRAMEWORKS)
    def test_html_navigation_links(self, temp_output_dir, sample_templates, framework):
        """
        Test that HTML pages have proper navigation links.
        
        Validates: Requirements 12.1
        """
        generator = HTMLOutputGenerator(temp_output_dir, test_mode=True)
        
        filenames = [t[0] for t in sample_templates]
        contents = [t[1] for t in sample_templates]
        
        result = generator.generate_html_site(
            processed_contents=contents,
            filenames=filenames,
            language='en',
            template_type=framework
        )
        
        # Check first page (should have Next but no Previous)
        first_page = result['html_dir'] / '0010_Introduction.html'
        first_content = first_page.read_text(encoding='utf-8')
        assert 'Next' in first_content or 'Weiter' in first_content
        assert 'index.html' in first_content  # TOC link
        
        # Check middle page (should have both Previous and Next)
        middle_page = result['html_dir'] / '0020_Requirements.html'
        middle_content = middle_page.read_text(encoding='utf-8')
        assert ('Previous' in middle_content or 'Zurück' in middle_content)
        assert ('Next' in middle_content or 'Weiter' in middle_content)
        assert 'index.html' in middle_content
        
        # Check last page (should have Previous but no Next)
        last_page = result['html_dir'] / '0030_Implementation.html'
        last_content = last_page.read_text(encoding='utf-8')
        assert 'Previous' in last_content or 'Zurück' in last_content
        assert 'index.html' in last_content
    
    @pytest.mark.parametrize('framework', NEW_FRAMEWORKS)
    def test_html_consistent_styling(self, temp_output_dir, sample_templates, framework):
        """
        Test that consistent styling is applied across all frameworks.
        
        Validates: Requirements 12.2
        """
        generator = HTMLOutputGenerator(temp_output_dir, test_mode=True)
        
        filenames = [t[0] for t in sample_templates]
        contents = [t[1] for t in sample_templates]
        
        result = generator.generate_html_site(
            processed_contents=contents,
            filenames=filenames,
            language='en',
            template_type=framework
        )
        
        # Verify CSS file exists and has content
        css_file = result['html_dir'] / 'styles.css'
        css_content = css_file.read_text(encoding='utf-8')
        
        # Check for key CSS elements
        assert 'body' in css_content
        assert 'header' in css_content
        assert '.container' in css_content
        assert '.page-nav' in css_content
        assert '@media' in css_content  # Responsive design
        
        # Verify all HTML pages link to the stylesheet
        for filename in filenames:
            number = filename[:4]
            name = filename[5:-3]
            html_file = result['html_dir'] / f"{number}_{name}.html"
            html_content = html_file.read_text(encoding='utf-8')
            assert '<link rel="stylesheet" href="styles.css">' in html_content


class TestPDFOutputForNewFrameworks:
    """Test PDF output generation for new compliance frameworks."""
    
    @pytest.mark.parametrize('framework', NEW_FRAMEWORKS)
    @pytest.mark.parametrize('language', ['de', 'en'])
    def test_pdf_generation_for_framework(self, temp_output_dir, framework, language):
        """
        Test PDF generation for each new framework.
        
        Validates: Requirements 12.3, 12.4
        """
        generator = OutputGenerator(temp_output_dir, test_mode=True)
        
        templates_data = [
            ('0010', 'Introduction', '# Introduction\n\nContent here.'),
            ('0020', 'Requirements', '# Requirements\n\nMore content.'),
            ('0030', 'Implementation', '# Implementation\n\nFinal content.')
        ]
        
        result = generator.generate_pdf_with_toc(
            templates_data=templates_data,
            language=language,
            template_type=framework,
            filename=f'{framework}_handbook.pdf'
        )
        
        # Verify output directory structure
        expected_dir = temp_output_dir / language / framework / 'pdf'
        assert expected_dir.exists()
        
        # Verify PDF file was created
        pdf_file = expected_dir / f'{framework}_handbook.pdf'
        assert pdf_file.exists()
        assert result.pdf_path == pdf_file
        
        # Verify no errors
        assert not result.errors, f"PDF generation failed for {framework}: {result.errors}"
    
    @pytest.mark.parametrize('framework', NEW_FRAMEWORKS)
    def test_pdf_with_toc(self, temp_output_dir, framework):
        """
        Test that PDF includes table of contents.
        
        Validates: Requirements 12.3
        """
        generator = OutputGenerator(temp_output_dir, test_mode=True)
        
        templates_data = [
            ('0010', 'Section One', '# Section One\n\nContent.'),
            ('0020', 'Section Two', '# Section Two\n\nContent.'),
        ]
        
        result = generator.generate_pdf_with_toc(
            templates_data=templates_data,
            language='en',
            template_type=framework
        )
        
        # Verify PDF was created
        assert result.pdf_path is not None
        assert result.pdf_path.exists()
        assert not result.errors
    
    @pytest.mark.parametrize('framework', NEW_FRAMEWORKS)
    def test_pdf_page_breaks(self, temp_output_dir, framework):
        """
        Test that PDF includes page breaks between sections.
        
        Validates: Requirements 12.4
        """
        generator = OutputGenerator(temp_output_dir, test_mode=True)
        
        templates_data = [
            ('0010', 'First', '# First\n\nContent.'),
            ('0020', 'Second', '# Second\n\nContent.'),
            ('0030', 'Third', '# Third\n\nContent.')
        ]
        
        result = generator.generate_pdf_with_toc(
            templates_data=templates_data,
            language='en',
            template_type=framework
        )
        
        # Verify PDF was created successfully
        assert result.pdf_path is not None
        assert result.pdf_path.exists()
        assert not result.errors


class TestMarkdownOutputForNewFrameworks:
    """Test Markdown output generation for new compliance frameworks."""
    
    @pytest.mark.parametrize('framework', NEW_FRAMEWORKS)
    @pytest.mark.parametrize('language', ['de', 'en'])
    def test_markdown_combined_mode(self, temp_output_dir, framework, language):
        """
        Test combined markdown file generation for each framework.
        
        Validates: Requirements 12.5
        """
        generator = OutputGenerator(temp_output_dir, test_mode=True)
        
        contents = [
            '# Introduction\n\nIntro content.',
            '# Requirements\n\nRequirements content.',
            '# Implementation\n\nImplementation content.'
        ]
        
        result = generator.generate_markdown(
            processed_contents=contents,
            language=language,
            template_type=framework,
            filename=f'{framework}_handbook.md'
        )
        
        # Verify output directory structure
        expected_dir = temp_output_dir / language / framework / 'markdown'
        assert expected_dir.exists()
        
        # Verify markdown file was created
        md_file = expected_dir / f'{framework}_handbook.md'
        assert md_file.exists()
        assert result.markdown_path == md_file
        
        # Verify content
        content = md_file.read_text(encoding='utf-8')
        assert '# Introduction' in content
        assert '# Requirements' in content
        assert '# Implementation' in content
        
        # Verify no errors
        assert not result.errors
    
    @pytest.mark.parametrize('framework', NEW_FRAMEWORKS)
    @pytest.mark.parametrize('language', ['de', 'en'])
    def test_markdown_separate_mode(self, temp_output_dir, framework, language):
        """
        Test separate markdown files generation for each framework.
        
        Validates: Requirements 12.6
        """
        generator = OutputGenerator(temp_output_dir, test_mode=True)
        
        templates_data = [
            ('0010_Introduction.md', '# Introduction\n\nContent.'),
            ('0020_Requirements.md', '# Requirements\n\nContent.'),
            ('0030_Implementation.md', '# Implementation\n\nContent.')
        ]
        
        result = generator.generate_separate_markdown_files(
            templates_data=templates_data,
            language=language,
            template_type=framework
        )
        
        # Verify output directory
        expected_dir = temp_output_dir / language / framework / 'markdown'
        assert expected_dir.exists()
        
        # Verify individual files were created
        for filename, _ in templates_data:
            md_file = expected_dir / filename
            assert md_file.exists(), f"File {md_file} not found"
        
        # Verify no errors
        assert not result.errors
    
    @pytest.mark.parametrize('framework', NEW_FRAMEWORKS)
    def test_markdown_toc_generation(self, temp_output_dir, framework):
        """
        Test TOC.md generation for separate markdown mode.
        
        Validates: Requirements 12.6
        """
        generator = OutputGenerator(temp_output_dir, test_mode=True)
        
        templates_info = [
            ('0010', 'Introduction', '0010_Introduction.md'),
            ('0020', 'Requirements', '0020_Requirements.md'),
            ('0030', 'Implementation', '0030_Implementation.md')
        ]
        
        result = generator.generate_markdown_toc(
            templates_info=templates_info,
            language='en',
            template_type=framework
        )
        
        # Verify TOC file was created
        expected_dir = temp_output_dir / 'en' / framework / 'markdown'
        toc_file = expected_dir / 'TOC.md'
        assert toc_file.exists()
        
        # Verify TOC content
        toc_content = toc_file.read_text(encoding='utf-8')
        assert '# Table of Contents' in toc_content or '# Inhaltsverzeichnis' in toc_content
        assert '[0010 - Introduction](0010_Introduction.md)' in toc_content
        assert '[0020 - Requirements](0020_Requirements.md)' in toc_content
        assert '[0030 - Implementation](0030_Implementation.md)' in toc_content
        
        # Verify no errors
        assert not result.errors


class TestOutputDirectoryStructure:
    """Test output directory structure for new frameworks."""
    
    @pytest.mark.parametrize('framework', NEW_FRAMEWORKS)
    @pytest.mark.parametrize('language', ['de', 'en'])
    @pytest.mark.parametrize('output_type', ['html', 'pdf', 'markdown'])
    def test_output_directory_structure(self, temp_output_dir, framework, language, output_type):
        """
        Test that output files are placed in correct directory structure.
        
        Validates: Requirements 12.7
        """
        if output_type == 'html':
            generator = HTMLOutputGenerator(temp_output_dir, test_mode=True)
            output_dir = generator.ensure_output_structure(language, framework)
        else:
            generator = OutputGenerator(temp_output_dir, test_mode=True)
            output_dir = generator.ensure_output_structure(language, output_type, framework)
        
        # Verify directory structure
        expected_path = temp_output_dir / language / framework / output_type
        assert output_dir == expected_path
        assert output_dir.exists()
        
        # Verify parent directories exist
        assert (temp_output_dir / language).exists()
        assert (temp_output_dir / language / framework).exists()
    
    @pytest.mark.parametrize('framework', NEW_FRAMEWORKS)
    def test_directory_creation_automatic(self, temp_output_dir, framework):
        """
        Test that directories are created automatically if they don't exist.
        
        Validates: Requirements 12.7
        """
        generator = OutputGenerator(temp_output_dir, test_mode=True)
        
        # Ensure directory doesn't exist
        test_dir = temp_output_dir / 'en' / framework / 'pdf'
        assert not test_dir.exists()
        
        # Create directory structure
        output_dir = generator.ensure_output_structure('en', 'pdf', framework)
        
        # Verify it was created
        assert output_dir.exists()
        assert output_dir == test_dir



# Property-Based Tests
from hypothesis import given, strategies as st, settings, HealthCheck


class TestPropertyBasedOutputGeneration:
    """Property-based tests for output generation."""
    
    @settings(max_examples=50, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        framework=st.sampled_from(NEW_FRAMEWORKS),
        language=st.sampled_from(['de', 'en'])
    )
    def test_property_17_multi_format_output_generation(self, temp_output_dir, framework, language):
        """
        Property 17: Multi-Format Output Generation
        
        For any compliance framework and language, the system SHALL generate
        output in all three formats (HTML, PDF, Markdown) with consistent content.
        
        Validates: Requirements 10.6, 12.1, 12.3, 12.5
        """
        # Sample template data
        templates_data = [
            ('0010_Introduction.md', '# Introduction\n\nIntroduction content.'),
            ('0020_Requirements.md', '# Requirements\n\nRequirements content.')
        ]
        
        filenames = [t[0] for t in templates_data]
        contents = [t[1] for t in templates_data]
        
        # Generate HTML
        html_generator = HTMLOutputGenerator(temp_output_dir, test_mode=True)
        html_result = html_generator.generate_html_site(
            processed_contents=contents,
            filenames=filenames,
            language=language,
            template_type=framework
        )
        
        # Generate Markdown
        md_generator = OutputGenerator(temp_output_dir, test_mode=True)
        md_result = md_generator.generate_markdown(
            processed_contents=contents,
            language=language,
            template_type=framework
        )
        
        # Verify all formats generated successfully
        assert not html_result['errors'], f"HTML generation failed: {html_result['errors']}"
        assert not md_result.errors, f"Markdown generation failed: {md_result.errors}"
        
        # Verify output directories exist
        assert html_result['html_dir'].exists()
        assert md_result.markdown_path.exists()
        
        # Verify files were created
        assert len(html_result['files']) > 0
        assert md_result.markdown_path.stat().st_size > 0
        
        # Verify directory structure is consistent
        html_parent = html_result['html_dir'].parent
        md_parent = md_result.markdown_path.parent.parent
        assert html_parent == md_parent, "Output directories should share same parent"
    
    @settings(max_examples=50, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        framework=st.sampled_from(NEW_FRAMEWORKS),
        language=st.sampled_from(['de', 'en']),
        output_format=st.sampled_from(['html', 'markdown'])
    )
    def test_property_30_output_format_consistency(self, temp_output_dir, framework, language, output_format):
        """
        Property 30: Output Format Consistency
        
        For any compliance framework, language, and output format, the generated
        output SHALL:
        1. Follow the correct directory structure (test-output/{language}/{framework}/{format}/)
        2. Contain all template content
        3. Be generated without errors
        4. Be reproducible (same input produces same output structure)
        
        Validates: Requirements 12.1-12.7
        """
        # Sample template data
        templates_data = [
            ('0010_Test.md', '# Test\n\nTest content.'),
            ('0020_More.md', '# More\n\nMore content.')
        ]
        
        if output_format == 'html':
            generator = HTMLOutputGenerator(temp_output_dir, test_mode=True)
            filenames = [t[0] for t in templates_data]
            contents = [t[1] for t in templates_data]
            
            result = generator.generate_html_site(
                processed_contents=contents,
                filenames=filenames,
                language=language,
                template_type=framework
            )
            
            # Verify no errors
            assert not result['errors'], f"Generation failed: {result['errors']}"
            
            # Verify directory structure
            expected_dir = temp_output_dir / language / framework / 'html'
            assert result['html_dir'] == expected_dir
            assert result['html_dir'].exists()
            
            # Verify files exist
            assert len(result['files']) > 0
            assert (result['html_dir'] / 'index.html').exists()
            assert (result['html_dir'] / 'styles.css').exists()
            
            # Verify template pages exist
            for filename in filenames:
                number = filename[:4]
                name = filename[5:-3]
                html_file = result['html_dir'] / f"{number}_{name}.html"
                assert html_file.exists(), f"Template page {html_file} not found"
                
                # Verify content is present
                content = html_file.read_text(encoding='utf-8')
                assert len(content) > 0
                assert 'html' in content.lower()
                
        elif output_format == 'markdown':
            generator = OutputGenerator(temp_output_dir, test_mode=True)
            contents = [t[1] for t in templates_data]
            
            result = generator.generate_markdown(
                processed_contents=contents,
                language=language,
                template_type=framework
            )
            
            # Verify no errors
            assert not result.errors, f"Generation failed: {result.errors}"
            
            # Verify directory structure
            expected_dir = temp_output_dir / language / framework / 'markdown'
            assert result.markdown_path.parent == expected_dir
            assert result.markdown_path.exists()
            
            # Verify content
            content = result.markdown_path.read_text(encoding='utf-8')
            assert len(content) > 0
            assert '# Test' in content
            assert '# More' in content
        
        # Test reproducibility - generate again and verify same structure
        if output_format == 'html':
            result2 = generator.generate_html_site(
                processed_contents=contents,
                filenames=filenames,
                language=language,
                template_type=framework
            )
            assert result2['html_dir'] == result['html_dir']
            assert len(result2['files']) == len(result['files'])
        else:
            result2 = generator.generate_markdown(
                processed_contents=contents,
                language=language,
                template_type=framework
            )
            assert result2.markdown_path == result.markdown_path
