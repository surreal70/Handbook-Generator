"""
Tests for CLI Interface

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2026
"""

import pytest
from hypothesis import given, settings, strategies as st
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
import argparse
import sys

from src.cli import parse_arguments, validate_arguments, interactive_selection, main


class TestCLIParameterValidation:
    """Tests for CLI parameter validation."""
    
    @settings(max_examples=100)
    @given(
        language=st.sampled_from(['de', 'en']),
        template=st.sampled_from(['backup', 'bcm', 'isms', 'it-operation'])
    )
    def test_property_2_valid_parameter_combinations(self, language, template):
        """
        Feature: handbook-generator, Property 2: CLI Parameter Validation
        
        For any valid combination of language and template type parameters,
        the system should accept them without error.
        
        Validates: Requirements 2.1, 2.2, 2.3, 2.5
        """
        # Create mock args with valid combination
        args = argparse.Namespace(
            language=language,
            template=template,
            output='both',
            verbose=False,
            config='config.yaml',
            create_config=False,
            template_dir='templates',
            output_dir='Handbook'
        )
        
        # Validation should pass (return None)
        error = validate_arguments(args)
        assert error is None, f"Valid combination {language}/{template} should not produce validation error"
    
    @settings(max_examples=100)
    @given(
        language=st.sampled_from(['de', 'en', None]),
        template=st.sampled_from(['backup', 'bcm', 'isms', 'it-operation', None])
    )
    def test_property_2_parameter_consistency(self, language, template):
        """
        Feature: handbook-generator, Property 2: CLI Parameter Validation
        
        For any combination of language and template parameters, if one is provided
        without the other (and not in create-config mode), validation should fail.
        
        Validates: Requirements 2.1, 2.2, 2.3, 2.5
        """
        # Skip if both are None (valid for interactive mode) or both are set (valid)
        if (language is None and template is None) or (language is not None and template is not None):
            return
        
        # Create mock args with inconsistent combination
        args = argparse.Namespace(
            language=language,
            template=template,
            output='both',
            verbose=False,
            config='config.yaml',
            create_config=False,
            template_dir='templates',
            output_dir='Handbook'
        )
        
        # Validation should fail (return error message)
        error = validate_arguments(args)
        assert error is not None, \
            f"Inconsistent combination (language={language}, template={template}) should produce validation error"
        assert "must be provided together" in error.lower(), \
            "Error message should indicate parameters must be provided together"
    
    @settings(max_examples=50)
    @given(
        output_format=st.sampled_from(['markdown', 'pdf', 'both'])
    )
    def test_property_2_output_format_validation(self, output_format):
        """
        Feature: handbook-generator, Property 2: CLI Parameter Validation
        
        For any valid output format, the system should accept it.
        
        Validates: Requirements 2.1, 2.2, 2.3, 2.5
        """
        args = argparse.Namespace(
            language='de',
            template='backup',
            output=output_format,
            verbose=False,
            config='config.yaml',
            create_config=False,
            template_dir='templates',
            output_dir='Handbook'
        )
        
        error = validate_arguments(args)
        assert error is None, f"Valid output format '{output_format}' should not produce validation error"
    
    def test_create_config_bypasses_validation(self):
        """
        Test that --create-config flag bypasses other parameter validation.
        
        Validates: Requirements 2.1, 2.2, 2.3, 2.5
        """
        # Even with inconsistent parameters, create_config should bypass validation
        args = argparse.Namespace(
            language='de',
            template=None,  # Inconsistent
            output='both',
            verbose=False,
            config='config.yaml',
            create_config=True,  # This should bypass validation
            template_dir='templates',
            output_dir='Handbook'
        )
        
        error = validate_arguments(args)
        assert error is None, "--create-config should bypass parameter validation"


class TestInteractiveSelection:
    """Tests for interactive template selection."""
    
    def test_interactive_selection_with_available_templates(self):
        """
        Test interactive selection when templates are available.
        
        Validates: Requirements 2.4
        """
        # Create mock template manager
        mock_manager = Mock()
        mock_manager.discover_templates.return_value = {
            'de': {
                'backup': [Path('templates/de/backup/0100_intro.md')],
                'bcm': [Path('templates/de/bcm/0100_intro.md')]
            },
            'en': {
                'backup': [Path('templates/en/backup/0100_intro.md')]
            }
        }
        
        # Mock user input
        with patch('builtins.input', side_effect=['de', 'backup']):
            language, template_type = interactive_selection(mock_manager)
        
        assert language == 'de'
        assert template_type == 'backup'
    
    def test_interactive_selection_no_templates(self):
        """
        Test interactive selection when no templates are available.
        
        Validates: Requirements 2.4
        """
        # Create mock template manager with no templates
        mock_manager = Mock()
        mock_manager.discover_templates.return_value = {}
        mock_manager.template_root = Path('templates')
        
        # Should exit with error
        with pytest.raises(SystemExit) as exc_info:
            interactive_selection(mock_manager)
        
        assert exc_info.value.code == 1
    
    def test_interactive_selection_invalid_then_valid_input(self):
        """
        Test interactive selection with invalid input followed by valid input.
        
        Validates: Requirements 2.4
        """
        mock_manager = Mock()
        mock_manager.discover_templates.return_value = {
            'de': {
                'backup': [Path('templates/de/backup/0100_intro.md')]
            }
        }
        
        # Mock user input: invalid language, then valid, invalid template, then valid
        with patch('builtins.input', side_effect=['fr', 'de', 'invalid', 'backup']):
            language, template_type = interactive_selection(mock_manager)
        
        assert language == 'de'
        assert template_type == 'backup'
    
    def test_interactive_selection_keyboard_interrupt(self):
        """
        Test that KeyboardInterrupt during interactive selection is handled.
        
        Validates: Requirements 2.4
        """
        mock_manager = Mock()
        mock_manager.discover_templates.return_value = {
            'de': {'backup': [Path('templates/de/backup/0100_intro.md')]}
        }
        
        # Mock user pressing Ctrl+C
        with patch('builtins.input', side_effect=KeyboardInterrupt()):
            with pytest.raises(KeyboardInterrupt):
                interactive_selection(mock_manager)


class TestMainFunction:
    """Tests for main function orchestration."""
    
    def test_main_with_create_config_success(self, tmp_path):
        """
        Test main function with --create-config flag.
        
        Validates: Requirements 2.1, 2.2, 2.3, 2.5
        """
        config_file = tmp_path / "test_config.yaml"
        
        test_args = [
            'cli.py',
            '--create-config',
            '--config', str(config_file)
        ]
        
        with patch.object(sys, 'argv', test_args):
            exit_code = main()
        
        assert exit_code == 0
        assert config_file.exists()
    
    def test_main_with_create_config_already_exists(self, tmp_path):
        """
        Test main function with --create-config when file already exists.
        
        Validates: Requirements 2.1, 2.2, 2.3, 2.5
        """
        config_file = tmp_path / "test_config.yaml"
        config_file.write_text("existing config")
        
        test_args = [
            'cli.py',
            '--create-config',
            '--config', str(config_file)
        ]
        
        with patch.object(sys, 'argv', test_args):
            exit_code = main()
        
        assert exit_code == 1  # Should fail because file exists
    
    def test_main_missing_config_file(self):
        """
        Test main function when config file is missing.
        
        Validates: Requirements 2.1, 2.2, 2.3, 2.5
        """
        test_args = [
            'cli.py',
            '--language', 'de',
            '--template', 'backup',
            '--config', 'nonexistent_config.yaml'
        ]
        
        with patch.object(sys, 'argv', test_args):
            exit_code = main()
        
        assert exit_code == 1  # Should fail due to missing config
    
    def test_main_invalid_template_combination(self, tmp_path):
        """
        Test main function with invalid language/template combination.
        
        Validates: Requirements 2.1, 2.2, 2.3, 2.5
        """
        # Create a valid config file
        config_file = tmp_path / "config.yaml"
        config_file.write_text("""
data_sources:
  netbox:
    url: "https://netbox.example.com"
    api_token: "test-token"
defaults:
  language: "de"
  output_format: "both"
metadata:
  author: "Test Author"
  version: "1.0.0"
""")
        
        # Create template directory but without the requested combination
        template_dir = tmp_path / "templates"
        template_dir.mkdir()
        (template_dir / "de").mkdir()
        (template_dir / "de" / "backup").mkdir()
        # Don't create bcm directory
        
        test_args = [
            'cli.py',
            '--language', 'de',
            '--template', 'bcm',  # This doesn't exist
            '--config', str(config_file),
            '--template-dir', str(template_dir)
        ]
        
        with patch.object(sys, 'argv', test_args):
            exit_code = main()
        
        assert exit_code == 1  # Should fail due to missing templates
    
    @patch('src.cli.TemplateManager')
    @patch('src.cli.ConfigManager')
    @patch('src.cli.PlaceholderProcessor')
    @patch('src.cli.OutputGenerator')
    @patch('src.cli.NetBoxAdapter')
    def test_main_successful_execution(
        self,
        mock_netbox,
        mock_output_gen,
        mock_processor,
        mock_config_mgr,
        mock_template_mgr
    ):
        """
        Test successful execution of main function with all components.
        
        Validates: Requirements 2.1, 2.2, 2.3, 2.5
        """
        # Setup mocks
        mock_config_instance = Mock()
        mock_config_instance.netbox_url = "https://netbox.example.com"
        mock_config_instance.netbox_api_token = "test-token"
        mock_config_mgr.return_value.load_config.return_value = mock_config_instance
        mock_config_mgr.return_value.validate_template_structure.return_value = []
        
        mock_template_instance = Mock()
        mock_template = Mock()
        mock_template.path = Mock()
        mock_template.path.name = "test_template.md"
        mock_template.read_content.return_value = "# Test Content"
        mock_template_mgr.return_value.get_templates.return_value = [mock_template]
        mock_template_mgr.return_value.validate_template_structure.return_value = []
        
        mock_netbox_instance = Mock()
        mock_netbox_instance.connect.return_value = True
        mock_netbox.return_value = mock_netbox_instance
        
        mock_proc_result = Mock()
        mock_proc_result.content = "# Processed Content"
        mock_proc_result.replacements = []
        mock_proc_result.warnings = []
        mock_proc_result.errors = []
        mock_processor.return_value.process_template.return_value = mock_proc_result
        
        mock_output_result = Mock()
        mock_output_result.markdown_path = Path("output.md")
        mock_output_result.warnings = []
        mock_output_result.errors = []
        mock_output_gen.return_value.generate_markdown.return_value = mock_output_result
        mock_output_gen.return_value.assemble_markdown.return_value = "# Assembled"
        
        test_args = [
            'cli.py',
            '--language', 'de',
            '--template', 'backup',
            '--output', 'markdown'
        ]
        
        with patch.object(sys, 'argv', test_args):
            exit_code = main()
        
        assert exit_code == 0  # Should succeed


class TestArgumentParsing:
    """Tests for argument parsing functionality."""
    
    def test_parse_arguments_all_parameters(self):
        """
        Test parsing all command-line parameters.
        
        Validates: Requirements 2.1, 2.2, 2.3, 2.5
        """
        test_args = [
            'cli.py',
            '--language', 'de',
            '--template', 'backup',
            '--output', 'pdf',
            '--verbose',
            '--config', 'custom.yaml',
            '--template-dir', 'my_templates',
            '--output-dir', 'my_output'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.language == 'de'
        assert args.template == 'backup'
        assert args.output == 'pdf'
        assert args.verbose is True
        assert args.config == 'custom.yaml'
        assert args.template_dir == 'my_templates'
        assert args.output_dir == 'my_output'
    
    def test_parse_arguments_short_options(self):
        """
        Test parsing short command-line options.
        
        Validates: Requirements 2.1, 2.2, 2.3, 2.5
        """
        test_args = [
            'cli.py',
            '-l', 'en',
            '-t', 'isms',
            '-o', 'both',
            '-v',
            '-c', 'test.yaml'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.language == 'en'
        assert args.template == 'isms'
        assert args.output == 'both'
        assert args.verbose is True
        assert args.config == 'test.yaml'
    
    def test_parse_arguments_defaults(self):
        """
        Test default values for optional parameters.
        
        Validates: Requirements 2.1, 2.2, 2.3, 2.5
        """
        test_args = ['cli.py']
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.output == 'both'
        assert args.verbose is False
        assert args.config == 'config.yaml'
        assert args.template_dir == 'templates'
        assert args.output_dir == 'Handbook'
        assert args.create_config is False
