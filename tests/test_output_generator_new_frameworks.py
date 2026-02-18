"""
Unit tests for Output Generator with new compliance frameworks.

Tests HTML, PDF, and Markdown output generation for IDW PS 951, NIST CSF 2.0, and TOGAF.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

import pytest
from pathlib import Path
import shutil
from src.output_generator import OutputGenerator
from src.html_output_generator import HTMLOutputGenerator


class TestHTMLOutputGenerationNewFrameworks:
    """Test HTML output generation for new frameworks"""
    
    @pytest.fixture
    def output_dir(self, tmp_path):
        """Create temporary output directory"""
        output_dir = tmp_path / "test-output"
        output_dir.mkdir()
        yield output_dir
        # Cleanup
        if output_dir.exists():
            shutil.rmtree(output_dir)
    
    @pytest.fixture
    def sample_templates(self):
        """Sample template data for testing"""
        return [
            ("0010_audit_planning.md", "# Audit Planning\n\nThis is the audit planning template."),
            ("0020_risk_assessment.md", "# Risk Assessment\n\nThis is the risk assessment template."),
            ("0030_control_evaluation.md", "# Control Evaluation\n\nThis is the control evaluation template.")
        ]
    
    def test_html_generation_idw_ps_951_german(self, output_dir, sample_templates):
        """
        Test HTML generation for IDW PS 951 German templates.
        
        Validates: Requirements 8.1, 8.2
        """
        generator = HTMLOutputGenerator(output_dir, test_mode=True)
        
        filenames = [t[0] for t in sample_templates]
        contents = [t[1] for t in sample_templates]
        
        result = generator.generate_html_site(
            processed_contents=contents,
            filenames=filenames,
            language='de',
            template_type='idw-ps-951'
        )
        
        # Verify no errors
        assert len(result['errors']) == 0, f"HTML generation should not have errors: {result['errors']}"
        
        # Verify output directory structure
        expected_dir = output_dir / 'de' / 'idw-ps-951' / 'html'
        assert expected_dir.exists(), "HTML output directory should exist"
        assert result['html_dir'] == expected_dir
        
        # Verify generated files
        assert len(result['files']) > 0, "Should generate HTML files"
        
        # Verify index.html exists
        index_path = expected_dir / 'index.html'
        assert index_path.exists(), "index.html should exist"
        assert index_path in result['files']
        
        # Verify styles.css exists
        css_path = expected_dir / 'styles.css'
        assert css_path.exists(), "styles.css should exist"
        assert css_path in result['files']
        
        # Verify template pages exist
        for filename in filenames:
            template_name = filename.replace('.md', '.html')
            template_path = expected_dir / template_name
            assert template_path.exists(), f"{template_name} should exist"
    
    def test_html_generation_nist_csf_english(self, output_dir, sample_templates):
        """
        Test HTML generation for NIST CSF 2.0 English templates.
        
        Validates: Requirements 8.1, 8.2
        """
        generator = HTMLOutputGenerator(output_dir, test_mode=True)
        
        filenames = [t[0] for t in sample_templates]
        contents = [t[1] for t in sample_templates]
        
        result = generator.generate_html_site(
            processed_contents=contents,
            filenames=filenames,
            language='en',
            template_type='nist-csf'
        )
        
        # Verify no errors
        assert len(result['errors']) == 0, f"HTML generation should not have errors: {result['errors']}"
        
        # Verify output directory structure
        expected_dir = output_dir / 'en' / 'nist-csf' / 'html'
        assert expected_dir.exists(), "HTML output directory should exist"
        
        # Verify generated files
        assert len(result['files']) > 0, "Should generate HTML files"
        
        # Verify index.html exists
        index_path = expected_dir / 'index.html'
        assert index_path.exists(), "index.html should exist"
    
    def test_html_generation_togaf_german(self, output_dir, sample_templates):
        """
        Test HTML generation for TOGAF German templates.
        
        Validates: Requirements 8.1, 8.2
        """
        generator = HTMLOutputGenerator(output_dir, test_mode=True)
        
        filenames = [t[0] for t in sample_templates]
        contents = [t[1] for t in sample_templates]
        
        result = generator.generate_html_site(
            processed_contents=contents,
            filenames=filenames,
            language='de',
            template_type='togaf'
        )
        
        # Verify no errors
        assert len(result['errors']) == 0, f"HTML generation should not have errors: {result['errors']}"
        
        # Verify output directory structure
        expected_dir = output_dir / 'de' / 'togaf' / 'html'
        assert expected_dir.exists(), "HTML output directory should exist"
        
        # Verify generated files
        assert len(result['files']) > 0, "Should generate HTML files"
    
    def test_html_styling_consistency(self, output_dir, sample_templates):
        """
        Test that HTML styling is consistent across all frameworks.
        
        Validates: Requirements 8.2
        """
        generator = HTMLOutputGenerator(output_dir, test_mode=True)
        
        filenames = [t[0] for t in sample_templates]
        contents = [t[1] for t in sample_templates]
        
        frameworks = ['idw-ps-951', 'nist-csf', 'togaf']
        css_contents = []
        
        for framework in frameworks:
            result = generator.generate_html_site(
                processed_contents=contents,
                filenames=filenames,
                language='de',
                template_type=framework
            )
            
            # Read CSS content
            css_path = output_dir / 'de' / framework / 'html' / 'styles.css'
            assert css_path.exists(), f"CSS file should exist for {framework}"
            css_content = css_path.read_text(encoding='utf-8')
            css_contents.append(css_content)
        
        # Verify all CSS files are identical (consistent styling)
        assert all(css == css_contents[0] for css in css_contents), \
            "CSS styling should be consistent across all frameworks"


class TestPDFOutputGenerationNewFrameworks:
    """Test PDF output generation for new frameworks"""
    
    @pytest.fixture
    def output_dir(self, tmp_path):
        """Create temporary output directory"""
        output_dir = tmp_path / "test-output"
        output_dir.mkdir()
        yield output_dir
        # Cleanup
        if output_dir.exists():
            shutil.rmtree(output_dir)
    
    @pytest.fixture
    def sample_templates_with_toc(self):
        """Sample template data with TOC information"""
        return [
            ("0010", "Audit Planning", "# Audit Planning\n\nThis is the audit planning template."),
            ("0020", "Risk Assessment", "# Risk Assessment\n\nThis is the risk assessment template."),
            ("0030", "Control Evaluation", "# Control Evaluation\n\nThis is the control evaluation template.")
        ]
    
    def test_pdf_generation_idw_ps_951(self, output_dir, sample_templates_with_toc):
        """
        Test PDF generation with TOC for IDW PS 951.
        
        Validates: Requirements 8.3, 8.4
        """
        # Check if PDF dependencies are available
        try:
            import markdown
            from weasyprint import HTML
        except (ImportError, OSError) as e:
            pytest.skip(f"PDF generation dependencies not available: {e}")
        
        generator = OutputGenerator(output_dir, test_mode=True)
        
        result = generator.generate_pdf_with_toc(
            templates_data=sample_templates_with_toc,
            language='de',
            template_type='idw-ps-951'
        )
        
        # Verify output directory structure
        expected_dir = output_dir / 'de' / 'idw-ps-951' / 'pdf'
        assert expected_dir.exists(), "PDF output directory should exist"
        
        # Verify PDF file was created
        if result.pdf_path:
            assert result.pdf_path.exists(), "PDF file should exist"
            assert result.pdf_path.suffix == '.pdf', "Output should be a PDF file"
    
    def test_pdf_generation_nist_csf(self, output_dir, sample_templates_with_toc):
        """
        Test PDF generation with TOC for NIST CSF 2.0.
        
        Validates: Requirements 8.3, 8.4
        """
        # Check if PDF dependencies are available
        try:
            import markdown
            from weasyprint import HTML
        except (ImportError, OSError) as e:
            pytest.skip(f"PDF generation dependencies not available: {e}")
        
        generator = OutputGenerator(output_dir, test_mode=True)
        
        result = generator.generate_pdf_with_toc(
            templates_data=sample_templates_with_toc,
            language='en',
            template_type='nist-csf'
        )
        
        # Verify output directory structure
        expected_dir = output_dir / 'en' / 'nist-csf' / 'pdf'
        assert expected_dir.exists(), "PDF output directory should exist"
    
    def test_pdf_generation_togaf(self, output_dir, sample_templates_with_toc):
        """
        Test PDF generation with TOC for TOGAF.
        
        Validates: Requirements 8.3, 8.4
        """
        # Check if PDF dependencies are available
        try:
            import markdown
            from weasyprint import HTML
        except (ImportError, OSError) as e:
            pytest.skip(f"PDF generation dependencies not available: {e}")
        
        generator = OutputGenerator(output_dir, test_mode=True)
        
        result = generator.generate_pdf_with_toc(
            templates_data=sample_templates_with_toc,
            language='de',
            template_type='togaf'
        )
        
        # Verify output directory structure
        expected_dir = output_dir / 'de' / 'togaf' / 'pdf'
        assert expected_dir.exists(), "PDF output directory should exist"


class TestMarkdownOutputGenerationNewFrameworks:
    """Test Markdown output generation for new frameworks"""
    
    @pytest.fixture
    def output_dir(self, tmp_path):
        """Create temporary output directory"""
        output_dir = tmp_path / "test-output"
        output_dir.mkdir()
        yield output_dir
        # Cleanup
        if output_dir.exists():
            shutil.rmtree(output_dir)
    
    @pytest.fixture
    def sample_templates(self):
        """Sample template data for testing"""
        return [
            ("0010_audit_planning.md", "# Audit Planning\n\nThis is the audit planning template."),
            ("0020_risk_assessment.md", "# Risk Assessment\n\nThis is the risk assessment template."),
            ("0030_control_evaluation.md", "# Control Evaluation\n\nThis is the control evaluation template.")
        ]
    
    def test_markdown_combined_mode_idw_ps_951(self, output_dir, sample_templates):
        """
        Test combined Markdown generation for IDW PS 951.
        
        Validates: Requirements 8.5
        """
        generator = OutputGenerator(output_dir, test_mode=True)
        
        contents = [t[1] for t in sample_templates]
        
        result = generator.generate_markdown(
            processed_contents=contents,
            language='de',
            template_type='idw-ps-951'
        )
        
        # Verify no errors
        assert len(result.errors) == 0, f"Markdown generation should not have errors: {result.errors}"
        
        # Verify output directory structure
        expected_dir = output_dir / 'de' / 'idw-ps-951'
        assert expected_dir.exists(), "Markdown output directory should exist"
        
        # Verify markdown file was created
        assert result.markdown_path is not None, "Markdown file should be created"
        assert result.markdown_path.exists(), "Markdown file should exist"
        assert result.markdown_path.suffix == '.md', "Output should be a markdown file"
    
    def test_markdown_separate_mode_nist_csf(self, output_dir, sample_templates):
        """
        Test separate Markdown file generation for NIST CSF 2.0.
        
        Validates: Requirements 8.5, 8.6
        """
        generator = OutputGenerator(output_dir, test_mode=True)
        
        result = generator.generate_separate_markdown_files(
            templates_data=sample_templates,
            language='en',
            template_type='nist-csf'
        )
        
        # Verify no errors
        assert len(result.errors) == 0, f"Markdown generation should not have errors: {result.errors}"
        
        # Verify output directory structure
        expected_dir = output_dir / 'en' / 'nist-csf' / 'markdown'
        assert expected_dir.exists(), "Markdown output directory should exist"
        
        # Verify separate markdown files were created
        for filename, _ in sample_templates:
            template_path = expected_dir / filename
            assert template_path.exists(), f"{filename} should exist"
    
    def test_markdown_toc_generation_togaf(self, output_dir):
        """
        Test TOC.md generation for TOGAF.
        
        Validates: Requirements 8.6
        """
        generator = OutputGenerator(output_dir, test_mode=True)
        
        templates_info = [
            ("0010", "Preliminary Phase", "0010_preliminary_phase.md"),
            ("0020", "Architecture Vision", "0020_architecture_vision.md"),
            ("0030", "Business Architecture", "0030_business_architecture.md")
        ]
        
        result = generator.generate_markdown_toc(
            templates_info=templates_info,
            language='de',
            template_type='togaf'
        )
        
        # Verify no errors
        assert len(result.errors) == 0, f"TOC generation should not have errors: {result.errors}"
        
        # Verify output directory structure
        expected_dir = output_dir / 'de' / 'togaf' / 'markdown'
        assert expected_dir.exists(), "Markdown output directory should exist"
        
        # Verify TOC.md was created
        toc_path = expected_dir / 'TOC.md'
        assert toc_path.exists(), "TOC.md should exist"
        assert result.markdown_path == toc_path
        
        # Verify TOC content
        toc_content = toc_path.read_text(encoding='utf-8')
        assert 'Table of Contents' in toc_content
        assert '0010 - Preliminary Phase' in toc_content
        assert '0020 - Architecture Vision' in toc_content
        assert '0030 - Business Architecture' in toc_content


class TestOutputDirectoryStructure:
    """Test output directory structure for new frameworks"""
    
    @pytest.fixture
    def output_dir(self, tmp_path):
        """Create temporary output directory"""
        output_dir = tmp_path / "test-output"
        output_dir.mkdir()
        yield output_dir
        # Cleanup
        if output_dir.exists():
            shutil.rmtree(output_dir)
    
    def test_directory_structure_creation(self, output_dir):
        """
        Test that output directories are created automatically.
        
        Validates: Requirements 8.7
        """
        generator = OutputGenerator(output_dir, test_mode=True)
        
        frameworks = ['idw-ps-951', 'nist-csf', 'togaf']
        languages = ['de', 'en']
        output_types = ['markdown', 'pdf', 'html']
        
        for framework in frameworks:
            for language in languages:
                for output_type in output_types:
                    # Ensure directory structure
                    if output_type == 'html':
                        html_gen = HTMLOutputGenerator(output_dir, test_mode=True)
                        result_dir = html_gen.ensure_output_structure(language, framework)
                    else:
                        result_dir = generator.ensure_output_structure(language, output_type, framework)
                    
                    # Verify directory was created
                    assert result_dir.exists(), f"Directory should exist: {result_dir}"
                    
                    # Verify directory structure matches expected pattern
                    if output_type == 'html':
                        expected_path = output_dir / language / framework / 'html'
                    else:
                        expected_path = output_dir / language / framework / output_type
                    
                    assert result_dir == expected_path, \
                        f"Directory structure should match: {result_dir} == {expected_path}"
    
    def test_directory_structure_pattern(self, output_dir):
        """
        Test that directory structure follows test-output/{language}/{framework}/ pattern.
        
        Validates: Requirements 8.7
        """
        generator = OutputGenerator(output_dir, test_mode=True)
        
        # Test IDW PS 951
        dir_path = generator.ensure_output_structure('de', 'markdown', 'idw-ps-951')
        assert str(dir_path) == str(output_dir / 'de' / 'idw-ps-951' / 'markdown')
        
        # Test NIST CSF
        dir_path = generator.ensure_output_structure('en', 'pdf', 'nist-csf')
        assert str(dir_path) == str(output_dir / 'en' / 'nist-csf' / 'pdf')
        
        # Test TOGAF
        html_gen = HTMLOutputGenerator(output_dir, test_mode=True)
        dir_path = html_gen.ensure_output_structure('de', 'togaf')
        assert str(dir_path) == str(output_dir / 'de' / 'togaf' / 'html')
