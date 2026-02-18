"""
Property-based tests for Output Generator with new compliance frameworks.

Tests universal properties for multi-format output generation and directory structure
for IDW PS 951, NIST CSF 2.0, and TOGAF.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

import pytest
from hypothesis import given, strategies as st, settings, HealthCheck
from pathlib import Path
import shutil
import tempfile
from src.output_generator import OutputGenerator
from src.html_output_generator import HTMLOutputGenerator


# Strategy for generating framework names
framework_strategy = st.sampled_from(['idw-ps-951', 'nist-csf', 'togaf'])

# Strategy for generating language codes
language_strategy = st.sampled_from(['de', 'en'])

# Strategy for generating output types
output_type_strategy = st.sampled_from(['markdown', 'pdf', 'html'])


class TestMultiFormatOutputGeneration:
    """
    Property 13: Multi-Format Output Generation
    
    For any new framework template set, the Output_Generator must successfully generate
    output in all three formats (HTML with navigation, PDF with table of contents, and
    Markdown in both combined and separate file modes).
    
    Validates: Requirements 6.6, 8.1, 8.2, 8.3, 8.4, 8.5, 8.6
    """
    
    @settings(max_examples=100, deadline=None, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        framework=framework_strategy,
        language=language_strategy,
        num_templates=st.integers(min_value=1, max_value=5)
    )
    def test_html_generation_succeeds_for_all_frameworks(
        self,
        framework,
        language,
        num_templates
    ):
        """
        Property 13: Multi-Format Output Generation (HTML)
        
        Test that HTML generation succeeds for any framework, language, and template count.
        
        Feature: additional-compliance-frameworks
        Property 13: Multi-Format Output Generation
        """
        # Create temporary output directory
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / "test-output"
            output_dir.mkdir()
            
            generator = HTMLOutputGenerator(output_dir, test_mode=True)
            
            # Generate sample templates
            filenames = [f"{(i+1)*10:04d}_template_{i}.md" for i in range(num_templates)]
            contents = [f"# Template {i}\n\nContent for template {i}" for i in range(num_templates)]
            
            result = generator.generate_html_site(
                processed_contents=contents,
                filenames=filenames,
                language=language,
                template_type=framework
            )
            
            # Property: HTML generation should not produce errors
            assert len(result['errors']) == 0, \
                f"HTML generation should succeed for {framework}/{language}"
            
            # Property: HTML directory should be created
            assert result['html_dir'] is not None, \
                f"HTML directory should be created for {framework}/{language}"
            assert result['html_dir'].exists(), \
                f"HTML directory should exist for {framework}/{language}"
            
            # Property: Files should be generated
            assert len(result['files']) > 0, \
                f"HTML files should be generated for {framework}/{language}"
            
            # Property: index.html should exist
            index_path = result['html_dir'] / 'index.html'
            assert index_path.exists(), \
                f"index.html should exist for {framework}/{language}"
            
            # Property: styles.css should exist
            css_path = result['html_dir'] / 'styles.css'
            assert css_path.exists(), \
                f"styles.css should exist for {framework}/{language}"
    
    @settings(max_examples=100, deadline=None, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        framework=framework_strategy,
        language=language_strategy,
        num_templates=st.integers(min_value=1, max_value=5)
    )
    def test_markdown_combined_generation_succeeds(
        self,
        framework,
        language,
        num_templates
    ):
        """
        Property 13: Multi-Format Output Generation (Markdown Combined)
        
        Test that combined Markdown generation succeeds for any framework and language.
        
        Feature: additional-compliance-frameworks
        Property 13: Multi-Format Output Generation
        """
        # Create temporary output directory
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / "test-output"
            output_dir.mkdir()
            
            generator = OutputGenerator(output_dir, test_mode=True)
            
            # Generate sample templates
            contents = [f"# Template {i}\n\nContent for template {i}" for i in range(num_templates)]
            
            result = generator.generate_markdown(
                processed_contents=contents,
                language=language,
                template_type=framework
            )
            
            # Property: Markdown generation should not produce errors
            assert len(result.errors) == 0, \
                f"Markdown generation should succeed for {framework}/{language}"
            
            # Property: Markdown file should be created
            assert result.markdown_path is not None, \
                f"Markdown file should be created for {framework}/{language}"
            assert result.markdown_path.exists(), \
                f"Markdown file should exist for {framework}/{language}"
            
            # Property: Output should be a markdown file
            assert result.markdown_path.suffix == '.md', \
                f"Output should be a markdown file for {framework}/{language}"
    
    @settings(max_examples=100, deadline=None, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        framework=framework_strategy,
        language=language_strategy,
        num_templates=st.integers(min_value=1, max_value=5)
    )
    def test_markdown_separate_generation_succeeds(
        self,
        framework,
        language,
        num_templates
    ):
        """
        Property 13: Multi-Format Output Generation (Markdown Separate)
        
        Test that separate Markdown file generation succeeds for any framework and language.
        
        Feature: additional-compliance-frameworks
        Property 13: Multi-Format Output Generation
        """
        # Create temporary output directory
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / "test-output"
            output_dir.mkdir()
            
            generator = OutputGenerator(output_dir, test_mode=True)
            
            # Generate sample templates
            templates_data = [
                (f"{(i+1)*10:04d}_template_{i}.md", f"# Template {i}\n\nContent for template {i}")
                for i in range(num_templates)
            ]
            
            result = generator.generate_separate_markdown_files(
                templates_data=templates_data,
                language=language,
                template_type=framework
            )
            
            # Property: Markdown generation should not produce errors
            assert len(result.errors) == 0, \
                f"Separate Markdown generation should succeed for {framework}/{language}"
            
            # Property: Output directory should exist
            expected_dir = output_dir / language / framework / 'markdown'
            assert expected_dir.exists(), \
                f"Markdown directory should exist for {framework}/{language}"
            
            # Property: All template files should be created
            for filename, _ in templates_data:
                template_path = expected_dir / filename
                assert template_path.exists(), \
                    f"Template file {filename} should exist for {framework}/{language}"
    
    @settings(max_examples=100, deadline=None, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        framework=framework_strategy,
        language=language_strategy,
        num_templates=st.integers(min_value=1, max_value=5)
    )
    def test_markdown_toc_generation_succeeds(
        self,
        framework,
        language,
        num_templates
    ):
        """
        Property 13: Multi-Format Output Generation (Markdown TOC)
        
        Test that TOC.md generation succeeds for any framework and language.
        
        Feature: additional-compliance-frameworks
        Property 13: Multi-Format Output Generation
        """
        # Create temporary output directory
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / "test-output"
            output_dir.mkdir()
            
            generator = OutputGenerator(output_dir, test_mode=True)
            
            # Generate sample templates info
            templates_info = [
                (f"{(i+1)*10:04d}", f"Template {i}", f"{(i+1)*10:04d}_template_{i}.md")
                for i in range(num_templates)
            ]
            
            result = generator.generate_markdown_toc(
                templates_info=templates_info,
                language=language,
                template_type=framework
            )
            
            # Property: TOC generation should not produce errors
            assert len(result.errors) == 0, \
                f"TOC generation should succeed for {framework}/{language}"
            
            # Property: TOC.md should be created
            expected_dir = output_dir / language / framework / 'markdown'
            toc_path = expected_dir / 'TOC.md'
            assert toc_path.exists(), \
                f"TOC.md should exist for {framework}/{language}"
            
            # Property: TOC should contain all template references
            toc_content = toc_path.read_text(encoding='utf-8')
            for template_num, template_title, _ in templates_info:
                assert template_num in toc_content, \
                    f"TOC should contain template number {template_num}"
                assert template_title in toc_content, \
                    f"TOC should contain template title {template_title}"


class TestOutputDirectoryStructure:
    """
    Property 14: Output Directory Structure
    
    For any generated handbook output, files must be placed in the directory structure
    test-output/{language}/{framework}/ where language is (de, en) and framework is
    the framework identifier.
    
    Validates: Requirements 8.7
    """
    
    @settings(max_examples=100, deadline=None, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        framework=framework_strategy,
        language=language_strategy,
        output_type=output_type_strategy
    )
    def test_directory_structure_follows_pattern(
        self,
        framework,
        language,
        output_type
    ):
        """
        Property 14: Output Directory Structure
        
        Test that output directory structure follows the required pattern for any
        framework, language, and output type combination.
        
        Feature: additional-compliance-frameworks
        Property 14: Output Directory Structure
        """
        # Create temporary output directory
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / "test-output"
            output_dir.mkdir()
            
            if output_type == 'html':
                generator = HTMLOutputGenerator(output_dir, test_mode=True)
                result_dir = generator.ensure_output_structure(language, framework)
                expected_path = output_dir / language / framework / 'html'
            else:
                generator = OutputGenerator(output_dir, test_mode=True)
                result_dir = generator.ensure_output_structure(language, output_type, framework)
                expected_path = output_dir / language / framework / output_type
            
            # Property: Directory should be created
            assert result_dir.exists(), \
                f"Directory should exist for {framework}/{language}/{output_type}"
            
            # Property: Directory path should match expected pattern
            assert result_dir == expected_path, \
                f"Directory structure should match pattern: {result_dir} == {expected_path}"
            
            # Property: Directory should be under output_dir
            assert output_dir in result_dir.parents, \
                f"Directory should be under output_dir: {result_dir}"
            
            # Property: Directory should contain language code
            assert language in result_dir.parts, \
                f"Directory should contain language code: {language} in {result_dir}"
            
            # Property: Directory should contain framework identifier
            assert framework in result_dir.parts, \
                f"Directory should contain framework identifier: {framework} in {result_dir}"
    
    @settings(max_examples=100, deadline=None, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        framework=framework_strategy,
        language=language_strategy
    )
    def test_html_output_directory_structure(
        self,
        framework,
        language
    ):
        """
        Property 14: Output Directory Structure (HTML)
        
        Test that HTML output directory structure is correct for any framework and language.
        
        Feature: additional-compliance-frameworks
        Property 14: Output Directory Structure
        """
        # Create temporary output directory
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / "test-output"
            output_dir.mkdir()
            
            generator = HTMLOutputGenerator(output_dir, test_mode=True)
            
            # Generate minimal HTML site
            result = generator.generate_html_site(
                processed_contents=["# Test"],
                filenames=["0010_test.md"],
                language=language,
                template_type=framework
            )
            
            # Property: HTML directory should follow pattern
            expected_dir = output_dir / language / framework / 'html'
            assert result['html_dir'] == expected_dir, \
                f"HTML directory should follow pattern: {result['html_dir']} == {expected_dir}"
            
            # Property: Generated files should be in correct directory
            for file_path in result['files']:
                assert expected_dir in file_path.parents or file_path.parent == expected_dir, \
                    f"Generated file should be in HTML directory: {file_path}"
    
    @settings(max_examples=100, deadline=None, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        framework=framework_strategy,
        language=language_strategy
    )
    def test_markdown_output_directory_structure(
        self,
        framework,
        language
    ):
        """
        Property 14: Output Directory Structure (Markdown)
        
        Test that Markdown output directory structure is correct for any framework and language.
        
        Feature: additional-compliance-frameworks
        Property 14: Output Directory Structure
        """
        # Create temporary output directory
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / "test-output"
            output_dir.mkdir()
            
            generator = OutputGenerator(output_dir, test_mode=True)
            
            # Generate combined markdown
            result = generator.generate_markdown(
                processed_contents=["# Test"],
                language=language,
                template_type=framework
            )
            
            # Property: Markdown file should be in correct directory
            expected_dir = output_dir / language / framework
            assert result.markdown_path.parent == expected_dir, \
                f"Markdown file should be in correct directory: {result.markdown_path.parent} == {expected_dir}"
    
    @settings(max_examples=100, deadline=None, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        framework=framework_strategy,
        language=language_strategy
    )
    def test_directory_creation_is_idempotent(
        self,
        framework,
        language
    ):
        """
        Property 14: Output Directory Structure (Idempotency)
        
        Test that directory creation is idempotent - calling it multiple times
        should not cause errors.
        
        Feature: additional-compliance-frameworks
        Property 14: Output Directory Structure
        """
        # Create temporary output directory
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / "test-output"
            output_dir.mkdir()
            
            generator = OutputGenerator(output_dir, test_mode=True)
            
            # Create directory multiple times
            dir1 = generator.ensure_output_structure(language, 'markdown', framework)
            dir2 = generator.ensure_output_structure(language, 'markdown', framework)
            dir3 = generator.ensure_output_structure(language, 'markdown', framework)
            
            # Property: All calls should return the same directory
            assert dir1 == dir2 == dir3, \
                f"Directory creation should be idempotent: {dir1} == {dir2} == {dir3}"
            
            # Property: Directory should still exist
            assert dir1.exists(), \
                f"Directory should exist after multiple creations: {dir1}"
