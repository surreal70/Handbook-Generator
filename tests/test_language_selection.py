"""
Unit tests for language selection functionality in CIS Controls integration.

This module contains unit tests for verifying that language selection works
correctly for CIS Controls handbooks, ensuring that the --language flag
controls which language's templates are used.

Feature: cis-controls-integration
Task: 11.2 Write unit tests for language selection
Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright (c) 2026
"""

import sys
import tempfile
from pathlib import Path
from unittest.mock import patch
import pytest

from src.template_manager import TemplateManager
from src.output_generator import OutputGenerator


class TestGermanCISControlsHandbookGeneration:
    """
    Test German CIS Controls handbook generation.
    
    Validates: Requirements 7.2, 7.5
    """
    
    @pytest.fixture
    def template_manager(self):
        """Get template manager instance."""
        return TemplateManager(Path("templates"))
    
    def test_german_cis_controls_templates_exist(self, template_manager):
        """
        Test that German CIS Controls templates exist and can be loaded.
        
        Feature: cis-controls-integration, Task 11.2
        Validates: Requirements 7.2
        """
        templates = template_manager.get_templates('de', 'cis-controls')
        
        assert len(templates) > 0, "Should have German CIS Controls templates"
        assert len(templates) >= 27, f"Should have at least 27 templates, got {len(templates)}"
    
    def test_german_cis_controls_metadata_template(self, template_manager):
        """
        Test that German CIS Controls metadata template exists.
        
        Feature: cis-controls-integration, Task 11.2
        Validates: Requirements 7.2
        """
        templates = template_manager.get_templates('de', 'cis-controls')
        
        # First template should be metadata
        assert templates[0].is_metadata(), \
            "First template should be metadata template"
        
        # Metadata template should be in German directory
        assert 'templates/de/cis-controls' in str(templates[0].path), \
            f"Metadata template should be in German directory: {templates[0].path}"
        
        # Metadata template should follow naming convention
        assert templates[0].path.name == '0000_metadata_de_cis-controls.md', \
            f"Metadata template should follow naming convention: {templates[0].path.name}"
    
    def test_german_cis_controls_content_templates(self, template_manager):
        """
        Test that German CIS Controls content templates are properly structured.
        
        Feature: cis-controls-integration, Task 11.2
        Validates: Requirements 7.2
        """
        templates = template_manager.get_templates('de', 'cis-controls')
        
        # Skip metadata template
        content_templates = [t for t in templates if not t.is_metadata()]
        
        assert len(content_templates) > 0, "Should have content templates"
        
        # All content templates should be in German directory
        for template in content_templates:
            assert 'templates/de/cis-controls' in str(template.path), \
                f"Content template should be in German directory: {template.path}"
            
            # Should have proper numbering
            assert template.sort_order > 0, \
                f"Content template should have sort_order > 0: {template.sort_order}"
    
    def test_german_cis_controls_markdown_generation(self, template_manager):
        """
        Test that German CIS Controls handbook can be generated as Markdown.
        
        Feature: cis-controls-integration, Task 11.2
        Validates: Requirements 7.2, 7.5
        """
        templates = template_manager.get_templates('de', 'cis-controls')
        
        # Process templates (simplified)
        processed_contents = [t.read_content() for t in templates]
        
        # Generate markdown
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / "test-output"
            generator = OutputGenerator(output_dir, test_mode=True)
            
            result = generator.generate_markdown(
                processed_contents,
                'de',
                'cis-controls'
            )
            
            # Should succeed
            assert result.markdown_path is not None, \
                "German CIS Controls markdown generation should succeed"
            assert result.markdown_path.exists(), \
                "German CIS Controls markdown file should exist"
            assert len(result.errors) == 0, \
                f"Should have no errors: {result.errors}"
            
            # Should be in German directory
            assert '/de/' in str(result.markdown_path), \
                f"Output should be in German directory: {result.markdown_path}"
            assert '/cis-controls/' in str(result.markdown_path), \
                f"Output should be in cis-controls directory: {result.markdown_path}"
    
    def test_german_cis_controls_template_content_language(self, template_manager):
        """
        Test that German CIS Controls templates contain German content.
        
        Feature: cis-controls-integration, Task 11.2
        Validates: Requirements 7.2
        """
        templates = template_manager.get_templates('de', 'cis-controls')
        
        # Check a few content templates for German content
        content_templates = [t for t in templates if not t.is_metadata()][:5]
        
        for template in content_templates:
            content = template.read_content()
            
            # Should have substantial content
            assert len(content) > 50, \
                f"Template {template.path.name} should have substantial content"
            
            # German content indicators (common German words)
            german_indicators = ['und', 'der', 'die', 'das', 'für', 'mit', 'von', 'auf']
            has_german = any(indicator in content.lower() for indicator in german_indicators)
            
            assert has_german, \
                f"German template {template.path.name} should contain German content"


class TestEnglishCISControlsHandbookGeneration:
    """
    Test English CIS Controls handbook generation.
    
    Validates: Requirements 7.2, 7.5
    """
    
    @pytest.fixture
    def template_manager(self):
        """Get template manager instance."""
        return TemplateManager(Path("templates"))
    
    def test_english_cis_controls_templates_exist(self, template_manager):
        """
        Test that English CIS Controls templates exist and can be loaded.
        
        Feature: cis-controls-integration, Task 11.2
        Validates: Requirements 7.2
        """
        templates = template_manager.get_templates('en', 'cis-controls')
        
        assert len(templates) > 0, "Should have English CIS Controls templates"
        assert len(templates) >= 27, f"Should have at least 27 templates, got {len(templates)}"
    
    def test_english_cis_controls_metadata_template(self, template_manager):
        """
        Test that English CIS Controls metadata template exists.
        
        Feature: cis-controls-integration, Task 11.2
        Validates: Requirements 7.2
        """
        templates = template_manager.get_templates('en', 'cis-controls')
        
        # First template should be metadata
        assert templates[0].is_metadata(), \
            "First template should be metadata template"
        
        # Metadata template should be in English directory
        assert 'templates/en/cis-controls' in str(templates[0].path), \
            f"Metadata template should be in English directory: {templates[0].path}"
        
        # Metadata template should follow naming convention
        assert templates[0].path.name == '0000_metadata_en_cis-controls.md', \
            f"Metadata template should follow naming convention: {templates[0].path.name}"
    
    def test_english_cis_controls_content_templates(self, template_manager):
        """
        Test that English CIS Controls content templates are properly structured.
        
        Feature: cis-controls-integration, Task 11.2
        Validates: Requirements 7.2
        """
        templates = template_manager.get_templates('en', 'cis-controls')
        
        # Skip metadata template
        content_templates = [t for t in templates if not t.is_metadata()]
        
        assert len(content_templates) > 0, "Should have content templates"
        
        # All content templates should be in English directory
        for template in content_templates:
            assert 'templates/en/cis-controls' in str(template.path), \
                f"Content template should be in English directory: {template.path}"
            
            # Should have proper numbering
            assert template.sort_order > 0, \
                f"Content template should have sort_order > 0: {template.sort_order}"
    
    def test_english_cis_controls_markdown_generation(self, template_manager):
        """
        Test that English CIS Controls handbook can be generated as Markdown.
        
        Feature: cis-controls-integration, Task 11.2
        Validates: Requirements 7.2, 7.5
        """
        templates = template_manager.get_templates('en', 'cis-controls')
        
        # Process templates (simplified)
        processed_contents = [t.read_content() for t in templates]
        
        # Generate markdown
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / "test-output"
            generator = OutputGenerator(output_dir, test_mode=True)
            
            result = generator.generate_markdown(
                processed_contents,
                'en',
                'cis-controls'
            )
            
            # Should succeed
            assert result.markdown_path is not None, \
                "English CIS Controls markdown generation should succeed"
            assert result.markdown_path.exists(), \
                "English CIS Controls markdown file should exist"
            assert len(result.errors) == 0, \
                f"Should have no errors: {result.errors}"
            
            # Should be in English directory
            assert '/en/' in str(result.markdown_path), \
                f"Output should be in English directory: {result.markdown_path}"
            assert '/cis-controls/' in str(result.markdown_path), \
                f"Output should be in cis-controls directory: {result.markdown_path}"
    
    def test_english_cis_controls_template_content_language(self, template_manager):
        """
        Test that English CIS Controls templates contain English content.
        
        Feature: cis-controls-integration, Task 11.2
        Validates: Requirements 7.2
        """
        templates = template_manager.get_templates('en', 'cis-controls')
        
        # Check a few content templates for English content
        content_templates = [t for t in templates if not t.is_metadata()][:5]
        
        for template in content_templates:
            content = template.read_content()
            
            # Should have substantial content
            assert len(content) > 50, \
                f"Template {template.path.name} should have substantial content"
            
            # English content indicators (common English words)
            english_indicators = ['and', 'the', 'for', 'with', 'from', 'this', 'that', 'are']
            has_english = any(indicator in content.lower() for indicator in english_indicators)
            
            assert has_english, \
                f"English template {template.path.name} should contain English content"


class TestLanguageFlagControlsTemplateSelection:
    """
    Test that language flag controls template selection.
    
    Validates: Requirements 7.5
    """
    
    @pytest.fixture
    def template_manager(self):
        """Get template manager instance."""
        return TemplateManager(Path("templates"))
    
    def test_language_flag_selects_german_templates(self, template_manager):
        """
        Test that specifying German language selects German templates.
        
        Feature: cis-controls-integration, Task 11.2
        Validates: Requirements 7.5
        """
        # Get German templates
        de_templates = template_manager.get_templates('de', 'cis-controls')
        
        # All should be German
        for template in de_templates:
            assert template.language == 'de', \
                f"Template should be German: {template.path}"
            assert '/de/' in str(template.path), \
                f"Template path should contain /de/: {template.path}"
    
    def test_language_flag_selects_english_templates(self, template_manager):
        """
        Test that specifying English language selects English templates.
        
        Feature: cis-controls-integration, Task 11.2
        Validates: Requirements 7.5
        """
        # Get English templates
        en_templates = template_manager.get_templates('en', 'cis-controls')
        
        # All should be English
        for template in en_templates:
            assert template.language == 'en', \
                f"Template should be English: {template.path}"
            assert '/en/' in str(template.path), \
                f"Template path should contain /en/: {template.path}"
    
    def test_language_flag_prevents_cross_language_contamination(self, template_manager):
        """
        Test that language flag prevents mixing templates from different languages.
        
        Feature: cis-controls-integration, Task 11.2
        Validates: Requirements 7.5
        """
        # Get German templates
        de_templates = template_manager.get_templates('de', 'cis-controls')
        de_paths = {str(t.path) for t in de_templates}
        
        # Get English templates
        en_templates = template_manager.get_templates('en', 'cis-controls')
        en_paths = {str(t.path) for t in en_templates}
        
        # No overlap
        assert len(de_paths & en_paths) == 0, \
            "German and English templates should not overlap"
        
        # All German templates in German directory
        for path in de_paths:
            assert '/de/' in path, \
                f"German template should be in /de/ directory: {path}"
            assert '/en/' not in path, \
                f"German template should not be in /en/ directory: {path}"
        
        # All English templates in English directory
        for path in en_paths:
            assert '/en/' in path, \
                f"English template should be in /en/ directory: {path}"
            assert '/de/' not in path, \
                f"English template should not be in /de/ directory: {path}"
    
    def test_language_flag_controls_output_directory(self, template_manager):
        """
        Test that language flag controls output directory structure.
        
        Feature: cis-controls-integration, Task 11.2
        Validates: Requirements 7.5
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / "test-output"
            generator = OutputGenerator(output_dir, test_mode=True)
            
            # Generate German handbook
            de_templates = template_manager.get_templates('de', 'cis-controls')
            de_contents = [t.read_content() for t in de_templates]
            
            de_result = generator.generate_markdown(
                de_contents,
                'de',
                'cis-controls'
            )
            
            # German output should be in German directory
            assert de_result.markdown_path is not None
            assert '/de/' in str(de_result.markdown_path), \
                f"German output should be in /de/ directory: {de_result.markdown_path}"
            
            # Generate English handbook
            en_templates = template_manager.get_templates('en', 'cis-controls')
            en_contents = [t.read_content() for t in en_templates]
            
            en_result = generator.generate_markdown(
                en_contents,
                'en',
                'cis-controls'
            )
            
            # English output should be in English directory
            assert en_result.markdown_path is not None
            assert '/en/' in str(en_result.markdown_path), \
                f"English output should be in /en/ directory: {en_result.markdown_path}"
            
            # Outputs should be in different directories
            assert str(de_result.markdown_path) != str(en_result.markdown_path), \
                "German and English outputs should be in different locations"
    
    def test_cli_language_flag_acceptance(self):
        """
        Test that CLI accepts language flag for CIS Controls.
        
        Feature: cis-controls-integration, Task 11.2
        Validates: Requirements 7.5
        """
        from src.cli import parse_arguments
        
        # Test German language flag
        test_args = [
            'cli.py',
            '--language', 'de',
            '--template', 'cis-controls'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.language == 'de', "Should accept German language flag"
        assert args.template == 'cis-controls', "Should accept cis-controls template"
        
        # Test English language flag
        test_args = [
            'cli.py',
            '--language', 'en',
            '--template', 'cis-controls'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.language == 'en', "Should accept English language flag"
        assert args.template == 'cis-controls', "Should accept cis-controls template"
    
    def test_cli_short_language_flag(self):
        """
        Test that CLI accepts short language flag (-l) for CIS Controls.
        
        Feature: cis-controls-integration, Task 11.2
        Validates: Requirements 7.5
        """
        from src.cli import parse_arguments
        
        # Test short German language flag
        test_args = [
            'cli.py',
            '-l', 'de',
            '-t', 'cis-controls'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.language == 'de', "Should accept short German language flag"
        assert args.template == 'cis-controls', "Should accept cis-controls template"
        
        # Test short English language flag
        test_args = [
            'cli.py',
            '-l', 'en',
            '-t', 'cis-controls'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.language == 'en', "Should accept short English language flag"
        assert args.template == 'cis-controls', "Should accept cis-controls template"
    
    def test_language_flag_with_all_output_formats(self, template_manager):
        """
        Test that language flag works with all output formats.
        
        Feature: cis-controls-integration, Task 11.2
        Validates: Requirements 7.5
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            output_dir = Path(tmpdir) / "test-output"
            
            # Test with German
            de_templates = template_manager.get_templates('de', 'cis-controls')
            de_contents = [t.read_content() for t in de_templates]
            
            generator = OutputGenerator(output_dir, test_mode=True)
            
            # Markdown
            md_result = generator.generate_markdown(de_contents, 'de', 'cis-controls')
            assert md_result.markdown_path is not None
            assert '/de/' in str(md_result.markdown_path)
            
            # PDF (if dependencies available)
            try:
                assembled = generator.assemble_markdown(de_contents)
                pdf_result = generator.generate_pdf(assembled, 'de', 'cis-controls')
                if pdf_result.pdf_path:
                    assert '/de/' in str(pdf_result.pdf_path)
            except (ImportError, OSError):
                pass  # PDF dependencies not available
            
            # Test with English
            en_templates = template_manager.get_templates('en', 'cis-controls')
            en_contents = [t.read_content() for t in en_templates]
            
            # Markdown
            md_result = generator.generate_markdown(en_contents, 'en', 'cis-controls')
            assert md_result.markdown_path is not None
            assert '/en/' in str(md_result.markdown_path)
            
            # PDF (if dependencies available)
            try:
                assembled = generator.assemble_markdown(en_contents)
                pdf_result = generator.generate_pdf(assembled, 'en', 'cis-controls')
                if pdf_result.pdf_path:
                    assert '/en/' in str(pdf_result.pdf_path)
            except (ImportError, OSError):
                pass  # PDF dependencies not available
