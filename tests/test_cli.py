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
        template=st.sampled_from(['bcm', 'bsi-grundschutz', 'cis-controls', 'isms', 'it-operation'])
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
        template=st.sampled_from(['bcm', 'bsi-grundschutz', 'cis-controls', 'isms', 'it-operation', None])
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
            template='bcm',
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
                'bcm': [Path('templates/de/bcm/0100_intro.md')],
                'isms': [Path('templates/de/isms/0100_intro.md')]
            },
            'en': {
                'bcm': [Path('templates/en/bcm/0100_intro.md')]
            }
        }
        
        # Mock user input
        with patch('builtins.input', side_effect=['de', 'bcm']):
            language, template_type = interactive_selection(mock_manager)
        
        assert language == 'de'
        assert template_type == 'bcm'
    
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
                'bcm': [Path('templates/de/bcm/0100_intro.md')]
            }
        }
        
        # Mock user input: invalid language, then valid, invalid template, then valid
        with patch('builtins.input', side_effect=['fr', 'de', 'invalid', 'bcm']):
            language, template_type = interactive_selection(mock_manager)
        
        assert language == 'de'
        assert template_type == 'bcm'
    
    def test_interactive_selection_keyboard_interrupt(self):
        """
        Test that KeyboardInterrupt during interactive selection is handled.
        
        Validates: Requirements 2.4
        """
        mock_manager = Mock()
        mock_manager.discover_templates.return_value = {
            'de': {'bcm': [Path('templates/de/bcm/0100_intro.md')]}
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
            '--template', 'bcm',
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
        (template_dir / "de" / "isms").mkdir()
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
            '--template', 'bcm',
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
            '--template', 'bcm',
            '--output', 'pdf',
            '--verbose',
            '--config', 'custom.yaml',
            '--template-dir', 'my_templates',
            '--output-dir', 'my_output'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.language == 'de'
        assert args.template == 'bcm'
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


class TestTemplateTypeValidation:
    """Tests for template type validation in CLI."""
    
    def test_valid_template_type_bcm(self):
        """
        Test that 'bcm' template type is accepted.
        
        Validates: Requirements 21.1, 21.5
        """
        test_args = [
            'cli.py',
            '--language', 'de',
            '--template', 'bcm'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'bcm'
    
    def test_valid_template_type_isms(self):
        """
        Test that 'isms' template type is accepted.
        
        Validates: Requirements 21.2, 21.5
        """
        test_args = [
            'cli.py',
            '--language', 'en',
            '--template', 'isms'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'isms'
    
    def test_valid_template_type_bsi_grundschutz(self):
        """
        Test that 'bsi-grundschutz' template type is accepted.
        
        Validates: Requirements 21.3, 21.5
        """
        test_args = [
            'cli.py',
            '--language', 'de',
            '--template', 'bsi-grundschutz'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'bsi-grundschutz'
    
    def test_valid_template_type_it_operation(self):
        """
        Test that 'it-operation' template type is accepted.
        
        Validates: Requirements 21.1, 21.5
        """
        test_args = [
            'cli.py',
            '--language', 'en',
            '--template', 'it-operation'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'it-operation'
    
    def test_valid_template_type_cis_controls(self):
        """
        Test that 'cis-controls' template type is accepted.
        
        Validates: Requirements 3.1, 3.2
        """
        test_args = [
            'cli.py',
            '--language', 'de',
            '--template', 'cis-controls'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'cis-controls'
    
    def test_valid_template_type_cis_controls_short_flag(self):
        """
        Test that 'cis-controls' template type is accepted with short flag.
        
        Validates: Requirements 3.1, 3.2
        """
        test_args = [
            'cli.py',
            '-l', 'en',
            '-t', 'cis-controls'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'cis-controls'
    
    def test_valid_template_type_pci_dss(self):
        """
        Test that 'pci-dss' template type is accepted.
        
        Validates: Requirements 10.7, 15.1
        """
        test_args = [
            'cli.py',
            '--language', 'de',
            '--template', 'pci-dss'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'pci-dss'
    
    def test_valid_template_type_hipaa(self):
        """
        Test that 'hipaa' template type is accepted.
        
        Validates: Requirements 10.7, 15.1
        """
        test_args = [
            'cli.py',
            '--language', 'en',
            '--template', 'hipaa'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'hipaa'
    
    def test_valid_template_type_nist_800_53(self):
        """
        Test that 'nist-800-53' template type is accepted.
        
        Validates: Requirements 10.7, 15.1
        """
        test_args = [
            'cli.py',
            '--language', 'de',
            '--template', 'nist-800-53'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'nist-800-53'
    
    def test_valid_template_type_tsc(self):
        """
        Test that 'tsc' template type is accepted.
        
        Validates: Requirements 10.7, 15.1
        """
        test_args = [
            'cli.py',
            '--language', 'en',
            '--template', 'tsc'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'tsc'
    
    def test_valid_template_type_common_criteria(self):
        """
        Test that 'common-criteria' template type is accepted.
        
        Validates: Requirements 10.7, 15.1
        """
        test_args = [
            'cli.py',
            '--language', 'de',
            '--template', 'common-criteria'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'common-criteria'
    
    def test_valid_template_type_iso_9001(self):
        """
        Test that 'iso-9001' template type is accepted.
        
        Validates: Requirements 10.7, 15.1
        """
        test_args = [
            'cli.py',
            '--language', 'en',
            '--template', 'iso-9001'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'iso-9001'
    
    def test_valid_template_type_gdpr(self):
        """
        Test that 'gdpr' template type is accepted.
        
        Validates: Requirements 10.7, 15.1
        """
        test_args = [
            'cli.py',
            '--language', 'de',
            '--template', 'gdpr'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'gdpr'
    
    def test_valid_template_type_idw_ps_951(self):
        """
        Test that 'idw-ps-951' template type is accepted.
        
        Validates: Requirements 6.7
        """
        test_args = [
            'cli.py',
            '--language', 'de',
            '--template', 'idw-ps-951'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'idw-ps-951'
    
    def test_valid_template_type_nist_csf(self):
        """
        Test that 'nist-csf' template type is accepted.
        
        Validates: Requirements 6.7
        """
        test_args = [
            'cli.py',
            '--language', 'en',
            '--template', 'nist-csf'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'nist-csf'
    
    def test_valid_template_type_togaf(self):
        """
        Test that 'togaf' template type is accepted.
        
        Validates: Requirements 6.7
        """
        test_args = [
            'cli.py',
            '--language', 'de',
            '--template', 'togaf'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'togaf'
    
    def test_new_frameworks_with_short_flags(self):
        """
        Test that new framework names work with short flags.
        
        Validates: Requirements 10.7, 15.1, 6.7
        """
        new_frameworks = ['pci-dss', 'hipaa', 'nist-800-53', 'tsc', 'common-criteria', 'iso-9001', 'gdpr', 'idw-ps-951', 'nist-csf', 'togaf']
        
        for framework in new_frameworks:
            test_args = [
                'cli.py',
                '-l', 'en',
                '-t', framework
            ]
            
            with patch.object(sys, 'argv', test_args):
                args = parse_arguments()
            
            assert args.template == framework, \
                f"New framework '{framework}' should be accepted with short flags"
    
    def test_cis_controls_appears_in_help_text(self, capsys):
        """
        Test that 'cis-controls' and new frameworks appear in help text.
        
        Validates: Requirements 3.1, 3.2, 6.7
        """
        test_args = [
            'cli.py',
            '--help'
        ]
        
        with patch.object(sys, 'argv', test_args):
            with pytest.raises(SystemExit) as exc_info:
                parse_arguments()
        
        # Help exits with code 0
        assert exc_info.value.code == 0
        
        captured = capsys.readouterr()
        help_output = captured.out
        
        # Verify cis-controls appears in help text
        assert 'cis-controls' in help_output.lower()
        
        # Verify new frameworks appear in help text
        assert 'idw-ps-951' in help_output.lower()
        assert 'nist-csf' in help_output.lower()
        assert 'togaf' in help_output.lower()
    
    def test_invalid_template_type_rejected(self):
        """
        Test that invalid template type is rejected with error message.
        
        Validates: Requirements 21.5
        """
        test_args = [
            'cli.py',
            '--language', 'de',
            '--template', 'invalid-type'
        ]
        
        with patch.object(sys, 'argv', test_args):
            with pytest.raises(SystemExit) as exc_info:
                parse_arguments()
        
        # argparse exits with code 2 for invalid arguments
        assert exc_info.value.code == 2
    
    def test_invalid_template_type_shows_valid_choices(self, capsys):
        """
        Test that invalid template type shows available choices in error message.
        
        Validates: Requirements 21.5, 15.1, 6.7
        """
        test_args = [
            'cli.py',
            '--language', 'de',
            '--template', 'nonexistent'
        ]
        
        with patch.object(sys, 'argv', test_args):
            with pytest.raises(SystemExit):
                parse_arguments()
        
        captured = capsys.readouterr()
        error_output = captured.err
        
        # Verify error message contains valid choices
        assert 'invalid choice' in error_output.lower()
        assert 'bcm' in error_output
        assert 'bsi-grundschutz' in error_output
        assert 'cis-controls' in error_output
        assert 'isms' in error_output
        assert 'it-operation' in error_output
        # Verify existing new frameworks appear in error message
        assert 'pci-dss' in error_output
        assert 'hipaa' in error_output
        assert 'nist-800-53' in error_output
        assert 'tsc' in error_output
        assert 'common-criteria' in error_output
        assert 'iso-9001' in error_output
        assert 'gdpr' in error_output
        # Verify Phase 1 frameworks appear in error message
        assert 'idw-ps-951' in error_output
        assert 'nist-csf' in error_output
        assert 'togaf' in error_output
        # Verify Phase 2 frameworks appear in error message
        assert 'iso-38500' in error_output
        assert 'iso-31000' in error_output
        assert 'csa-ccm' in error_output
        assert 'tisax' in error_output
        assert 'soc1' in error_output
        assert 'coso' in error_output
        assert 'dora' in error_output
    
    def test_all_valid_template_types_accepted(self):
        """
        Test that all valid template types are accepted.
        
        Validates: Requirements 21.1, 21.2, 21.3, 21.5, 3.1, 10.7, 6.7
        """
        valid_types = ['bcm', 'bsi-grundschutz', 'cis-controls', 'common-criteria', 
                       'coso', 'csa-ccm', 'dora', 'email-service', 'gdpr', 'hipaa', 
                       'idw-ps-951', 'isms', 'iso-31000', 'iso-38500', 'iso-9001', 
                       'it-operation', 'nist-800-53', 'nist-csf', 'pci-dss', 
                       'service-templates', 'soc1', 'tisax', 'togaf', 'tsc']
        
        for template_type in valid_types:
            test_args = [
                'cli.py',
                '--language', 'de',
                '--template', template_type
            ]
            
            with patch.object(sys, 'argv', test_args):
                args = parse_arguments()
            
            assert args.template == template_type, \
                f"Template type '{template_type}' should be accepted"
    
    @settings(max_examples=100)
    @given(
        template_type=st.sampled_from(['bcm', 'bsi-grundschutz', 'cis-controls', 'common-criteria', 
                                       'coso', 'csa-ccm', 'dora', 'email-service', 'gdpr', 'hipaa', 
                                       'idw-ps-951', 'isms', 'iso-31000', 'iso-38500', 'iso-9001', 
                                       'it-operation', 'nist-800-53', 'nist-csf', 'pci-dss', 
                                       'service-templates', 'soc1', 'tisax', 'togaf', 'tsc']),
        language=st.sampled_from(['de', 'en'])
    )
    def test_property_14_cli_template_type_validation(self, template_type, language):
        """
        Feature: template-system-extension, compliance-framework-templates, additional-compliance-frameworks
        Property 14: CLI Template Type Validation
        
        For any CLI invocation with --template parameter, if the template type
        is in the valid set (all supported frameworks), the system SHALL accept 
        the input without error.
        
        Validates: Requirements 21.5, 3.1, 10.7, 6.7
        """
        test_args = [
            'cli.py',
            '--language', language,
            '--template', template_type
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        # Verify the template type was accepted
        assert args.template == template_type, \
            f"Valid template type '{template_type}' should be accepted"
        assert args.language == language, \
            f"Language '{language}' should be accepted"
    
    @settings(max_examples=100)
    @given(
        invalid_template=st.text(
            alphabet=st.characters(blacklist_categories=('Cs',)),
            min_size=1,
            max_size=50
        ).filter(lambda x: x not in ['bcm', 'bsi-grundschutz', 'cis-controls', 'common-criteria', 
                                      'coso', 'csa-ccm', 'dora', 'email-service', 'gdpr', 'hipaa', 
                                      'idw-ps-951', 'isms', 'iso-31000', 'iso-38500', 'iso-9001', 
                                      'it-operation', 'nist-800-53', 'nist-csf', 'pci-dss', 
                                      'service-templates', 'soc1', 'tisax', 'togaf', 'tsc'])
    )
    def test_property_14_cli_invalid_template_rejection(self, invalid_template):
        """
        Feature: template-system-extension, compliance-framework-templates, additional-compliance-frameworks
        Property 14: CLI Template Type Validation
        
        For any CLI invocation with --template parameter, if the template type
        is NOT in the valid set, the system SHALL reject the input with an
        error message listing valid options.
        
        Validates: Requirements 21.5, 10.7, 15.1, 6.7
        """
        test_args = [
            'cli.py',
            '--language', 'de',
            '--template', invalid_template
        ]
        
        with patch.object(sys, 'argv', test_args):
            with pytest.raises(SystemExit) as exc_info:
                parse_arguments()
        
        # argparse exits with code 2 for invalid arguments
        assert exc_info.value.code == 2, \
            f"Invalid template type '{invalid_template}' should be rejected with exit code 2"


class TestPhase2FrameworkCLIIntegration:
    """Tests for Phase 2 framework CLI integration."""
    
    def test_valid_template_type_iso_38500(self):
        """
        Test that 'iso-38500' template type is accepted.
        
        Validates: Requirements 6.7
        """
        test_args = [
            'cli.py',
            '--language', 'en',
            '--template', 'iso-38500'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'iso-38500'
    
    def test_valid_template_type_iso_31000(self):
        """
        Test that 'iso-31000' template type is accepted.
        
        Validates: Requirements 6.7
        """
        test_args = [
            'cli.py',
            '--language', 'de',
            '--template', 'iso-31000'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'iso-31000'
    
    def test_valid_template_type_csa_ccm(self):
        """
        Test that 'csa-ccm' template type is accepted.
        
        Validates: Requirements 6.7
        """
        test_args = [
            'cli.py',
            '--language', 'en',
            '--template', 'csa-ccm'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'csa-ccm'
    
    def test_valid_template_type_tisax(self):
        """
        Test that 'tisax' template type is accepted.
        
        Validates: Requirements 6.7
        """
        test_args = [
            'cli.py',
            '--language', 'de',
            '--template', 'tisax'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'tisax'
    
    def test_valid_template_type_soc1(self):
        """
        Test that 'soc1' template type is accepted.
        
        Validates: Requirements 6.7
        """
        test_args = [
            'cli.py',
            '--language', 'en',
            '--template', 'soc1'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'soc1'
    
    def test_valid_template_type_coso(self):
        """
        Test that 'coso' template type is accepted.
        
        Validates: Requirements 6.7
        """
        test_args = [
            'cli.py',
            '--language', 'de',
            '--template', 'coso'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'coso'
    
    def test_valid_template_type_dora(self):
        """
        Test that 'dora' template type is accepted.
        
        Validates: Requirements 6.7
        """
        test_args = [
            'cli.py',
            '--language', 'en',
            '--template', 'dora'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'dora'
    
    def test_phase2_frameworks_with_short_flags(self):
        """
        Test that Phase 2 framework names work with short flags.
        
        Validates: Requirements 6.7
        """
        phase2_frameworks = ['iso-38500', 'iso-31000', 'csa-ccm', 'tisax', 'soc1', 'coso', 'dora']
        
        for framework in phase2_frameworks:
            test_args = [
                'cli.py',
                '-l', 'en',
                '-t', framework
            ]
            
            with patch.object(sys, 'argv', test_args):
                args = parse_arguments()
            
            assert args.template == framework, \
                f"Phase 2 framework '{framework}' should be accepted with short flags"
    
    def test_phase2_frameworks_appear_in_help_text(self, capsys):
        """
        Test that Phase 2 frameworks appear in help text.
        
        Validates: Requirements 6.7
        """
        test_args = [
            'cli.py',
            '--help'
        ]
        
        with patch.object(sys, 'argv', test_args):
            with pytest.raises(SystemExit) as exc_info:
                parse_arguments()
        
        # Help exits with code 0
        assert exc_info.value.code == 0
        
        captured = capsys.readouterr()
        help_output = captured.out.lower()
        
        # Verify Phase 2 frameworks appear in help text
        assert 'iso-38500' in help_output
        assert 'iso-31000' in help_output
        assert 'csa-ccm' in help_output
        assert 'tisax' in help_output
        assert 'soc1' in help_output
        assert 'coso' in help_output
        assert 'dora' in help_output
    
    def test_invalid_framework_shows_phase2_in_choices(self, capsys):
        """
        Test that invalid template type shows Phase 2 frameworks in error message.
        
        Validates: Requirements 6.7
        """
        test_args = [
            'cli.py',
            '--language', 'de',
            '--template', 'nonexistent-framework'
        ]
        
        with patch.object(sys, 'argv', test_args):
            with pytest.raises(SystemExit):
                parse_arguments()
        
        captured = capsys.readouterr()
        error_output = captured.err
        
        # Verify error message contains Phase 2 frameworks
        assert 'invalid choice' in error_output.lower()
        assert 'iso-38500' in error_output
        assert 'iso-31000' in error_output
        assert 'csa-ccm' in error_output
        assert 'tisax' in error_output
        assert 'soc1' in error_output
        assert 'coso' in error_output
        assert 'dora' in error_output
    
    def test_all_phase2_frameworks_accepted(self):
        """
        Test that all Phase 2 framework types are accepted.
        
        Validates: Requirements 6.7
        """
        phase2_frameworks = ['iso-38500', 'iso-31000', 'csa-ccm', 'tisax', 'soc1', 'coso', 'dora']
        
        for framework in phase2_frameworks:
            test_args = [
                'cli.py',
                '--language', 'de',
                '--template', framework
            ]
            
            with patch.object(sys, 'argv', test_args):
                args = parse_arguments()
            
            assert args.template == framework, \
                f"Phase 2 framework '{framework}' should be accepted"
    
    @settings(max_examples=100)
    @given(
        framework=st.sampled_from(['iso-38500', 'iso-31000', 'csa-ccm', 'tisax', 'soc1', 'coso', 'dora']),
        language=st.sampled_from(['de', 'en'])
    )
    def test_property_phase2_cli_framework_validation(self, framework, language):
        """
        Feature: additional-compliance-frameworks
        Property: Phase 2 CLI Framework Validation
        
        For any CLI invocation with --template parameter set to a Phase 2 framework,
        the system SHALL accept the input without error.
        
        Validates: Requirements 6.7
        """
        test_args = [
            'cli.py',
            '--language', language,
            '--template', framework
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        # Verify the framework was accepted
        assert args.template == framework, \
            f"Phase 2 framework '{framework}' should be accepted"
        assert args.language == language, \
            f"Language '{language}' should be accepted"
    
    def test_phase2_frameworks_with_all_output_formats(self):
        """
        Test that Phase 2 frameworks work with all output formats.
        
        Validates: Requirements 6.7
        """
        phase2_frameworks = ['iso-38500', 'iso-31000', 'csa-ccm', 'tisax', 'soc1', 'coso', 'dora']
        output_formats = ['markdown', 'pdf', 'html', 'both', 'all']
        
        for framework in phase2_frameworks:
            for output_format in output_formats:
                test_args = [
                    'cli.py',
                    '--language', 'en',
                    '--template', framework,
                    '--output', output_format
                ]
                
                with patch.object(sys, 'argv', test_args):
                    args = parse_arguments()
                
                assert args.template == framework
                assert args.output == output_format
    
    def test_phase2_frameworks_with_verbose_flag(self):
        """
        Test that Phase 2 frameworks work with verbose flag.
        
        Validates: Requirements 6.7
        """
        phase2_frameworks = ['iso-38500', 'iso-31000', 'csa-ccm', 'tisax', 'soc1', 'coso', 'dora']
        
        for framework in phase2_frameworks:
            test_args = [
                'cli.py',
                '--language', 'de',
                '--template', framework,
                '--verbose'
            ]
            
            with patch.object(sys, 'argv', test_args):
                args = parse_arguments()
            
            assert args.template == framework
            assert args.verbose is True
    
    def test_phase2_frameworks_with_custom_config(self):
        """
        Test that Phase 2 frameworks work with custom config file.
        
        Validates: Requirements 6.7
        """
        phase2_frameworks = ['iso-38500', 'iso-31000', 'csa-ccm', 'tisax', 'soc1', 'coso', 'dora']
        
        for framework in phase2_frameworks:
            test_args = [
                'cli.py',
                '--language', 'en',
                '--template', framework,
                '--config', 'custom_config.yaml'
            ]
            
            with patch.object(sys, 'argv', test_args):
                args = parse_arguments()
            
            assert args.template == framework
            assert args.config == 'custom_config.yaml'
    
    def test_phase2_frameworks_with_separate_files_flag(self):
        """
        Test that Phase 2 frameworks work with --separate-files flag.
        
        Validates: Requirements 6.7
        """
        phase2_frameworks = ['iso-38500', 'iso-31000', 'csa-ccm', 'tisax', 'soc1', 'coso', 'dora']
        
        for framework in phase2_frameworks:
            test_args = [
                'cli.py',
                '--language', 'de',
                '--template', framework,
                '--separate-files'
            ]
            
            with patch.object(sys, 'argv', test_args):
                args = parse_arguments()
            
            assert args.template == framework
            assert args.separate_files is True
    
    def test_phase2_frameworks_with_pdf_toc_flag(self):
        """
        Test that Phase 2 frameworks work with --pdf-toc flag.
        
        Validates: Requirements 6.7
        """
        phase2_frameworks = ['iso-38500', 'iso-31000', 'csa-ccm', 'tisax', 'soc1', 'coso', 'dora']
        
        for framework in phase2_frameworks:
            test_args = [
                'cli.py',
                '--language', 'en',
                '--template', framework,
                '--pdf-toc'
            ]
            
            with patch.object(sys, 'argv', test_args):
                args = parse_arguments()
            
            assert args.template == framework
            assert args.pdf_toc is True
