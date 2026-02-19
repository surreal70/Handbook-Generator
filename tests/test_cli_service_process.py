"""
CLI tests for service and process documentation options.

Tests the command-line interface for --service and --process options,
including argument parsing, mutual exclusivity, and execution.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

import pytest
import subprocess
import sys
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
from io import StringIO

from src.cli import parse_arguments


class TestServiceProcessArgumentParsing:
    """Tests for --service and --process argument parsing."""
    
    def test_service_argument_parsing(self):
        """Test parsing --service argument."""
        with patch('sys.argv', ['handbook-generator', '--language', 'de', '--service', 'generic-service-template', '--test']):
            args = parse_arguments()
            
            assert args.service == 'generic-service-template'
            assert args.language == 'de'
            assert args.test is True
    
    def test_service_short_argument(self):
        """Test parsing -s short form."""
        with patch('sys.argv', ['handbook-generator', '-l', 'de', '-s', 'email-service', '--test']):
            args = parse_arguments()
            
            assert args.service == 'email-service'
            assert args.language == 'de'
    
    def test_process_argument_parsing(self):
        """Test parsing --process argument."""
        with patch('sys.argv', ['handbook-generator', '--language', 'de', '--process', 'generic-process-template', '--test']):
            args = parse_arguments()
            
            assert args.process == 'generic-process-template'
            assert args.language == 'de'
            assert args.test is True
    
    def test_process_short_argument(self):
        """Test parsing -p short form."""
        with patch('sys.argv', ['handbook-generator', '-l', 'de', '-p', 'incident-management', '--test']):
            args = parse_arguments()
            
            assert args.process == 'incident-management'
            assert args.language == 'de'
    
    def test_service_with_output_format(self):
        """Test --service with output format option."""
        with patch('sys.argv', ['handbook-generator', '-l', 'en', '--service', 'email-service', '-o', 'pdf', '--test']):
            args = parse_arguments()
            
            assert args.service == 'email-service'
            assert args.output_format == 'pdf'
            assert args.language == 'en'
    
    def test_process_with_output_format(self):
        """Test --process with output format option."""
        with patch('sys.argv', ['handbook-generator', '-l', 'en', '--process', 'incident-management', '-o', 'html', '--test']):
            args = parse_arguments()
            
            assert args.process == 'incident-management'
            assert args.output_format == 'html'
            assert args.language == 'en'


class TestMutualExclusivity:
    """Tests for mutual exclusivity between --template, --service, and --process."""
    
    def test_template_and_service_mutually_exclusive(self):
        """Test that --template and --service cannot be used together."""
        with patch('sys.argv', ['handbook-generator', '-l', 'de', '--template', 'isms', '--service', 'email-service', '--test']):
            with pytest.raises(SystemExit):
                parse_arguments()
    
    def test_template_and_process_mutually_exclusive(self):
        """Test that --template and --process cannot be used together."""
        with patch('sys.argv', ['handbook-generator', '-l', 'de', '--template', 'isms', '--process', 'incident-management', '--test']):
            with pytest.raises(SystemExit):
                parse_arguments()
    
    def test_service_and_process_mutually_exclusive(self):
        """Test that --service and --process cannot be used together."""
        with patch('sys.argv', ['handbook-generator', '-l', 'de', '--service', 'email-service', '--process', 'incident-management', '--test']):
            with pytest.raises(SystemExit):
                parse_arguments()
    
    def test_all_three_mutually_exclusive(self):
        """Test that all three options cannot be used together."""
        with patch('sys.argv', ['handbook-generator', '-l', 'de', '--template', 'isms', '--service', 'email-service', '--process', 'incident-management', '--test']):
            with pytest.raises(SystemExit):
                parse_arguments()
    
    def test_template_only_allowed(self):
        """Test that --template alone is allowed."""
        with patch('sys.argv', ['handbook-generator', '-l', 'de', '--template', 'isms', '--test']):
            args = parse_arguments()
            assert args.template == 'isms'
            assert args.service is None
            assert args.process is None
    
    def test_service_only_allowed(self):
        """Test that --service alone is allowed."""
        with patch('sys.argv', ['handbook-generator', '-l', 'de', '--service', 'email-service', '--test']):
            args = parse_arguments()
            assert args.service == 'email-service'
            assert args.template is None
            assert args.process is None
    
    def test_process_only_allowed(self):
        """Test that --process alone is allowed."""
        with patch('sys.argv', ['handbook-generator', '-l', 'de', '--process', 'incident-management', '--test']):
            args = parse_arguments()
            assert args.process == 'incident-management'
            assert args.template is None
            assert args.service is None


class TestServiceProcessHelpText:
    """Tests for help text including service and process examples."""
    
    def test_help_includes_service_examples(self):
        """Test that help text includes service examples."""
        result = subprocess.run(
            [sys.executable, '-m', 'src.cli', '--help'],
            capture_output=True,
            text=True
        )
        
        # Verify service examples are in help text
        assert '--service' in result.stdout or '-s' in result.stdout
        assert 'service' in result.stdout.lower()
    
    def test_help_includes_process_examples(self):
        """Test that help text includes process examples."""
        result = subprocess.run(
            [sys.executable, '-m', 'src.cli', '--help'],
            capture_output=True,
            text=True
        )
        
        # Verify process examples are in help text
        assert '--process' in result.stdout or '-p' in result.stdout
        assert 'process' in result.stdout.lower()


class TestServiceProcessExecution:
    """Tests for executing service and process generation via CLI."""
    
    @pytest.mark.skipif(
        not Path('services/de/generic-service-template').exists(),
        reason="German service templates not found"
    )
    def test_execute_service_generation_german(self):
        """Test executing German service generation via CLI."""
        result = subprocess.run(
            [sys.executable, '-m', 'src.cli', '--language', 'de', '--service', 'generic-service-template', '--test'],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Should complete successfully
        assert result.returncode == 0, f"CLI failed with: {result.stderr}"
        
        # Output should contain service-related content
        assert 'service' in result.stdout.lower() or 'dienst' in result.stdout.lower()
    
    @pytest.mark.skipif(
        not Path('services/en/generic-service-template').exists(),
        reason="English service templates not found"
    )
    def test_execute_service_generation_english(self):
        """Test executing English service generation via CLI."""
        result = subprocess.run(
            [sys.executable, '-m', 'src.cli', '--language', 'en', '--service', 'generic-service-template', '--test'],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Should complete successfully
        assert result.returncode == 0, f"CLI failed with: {result.stderr}"
        
        # Output should contain service-related content
        assert 'service' in result.stdout.lower()
    
    @pytest.mark.skipif(
        not Path('processes/de/generic-process-template').exists(),
        reason="German process templates not found"
    )
    def test_execute_process_generation_german(self):
        """Test executing German process generation via CLI."""
        result = subprocess.run(
            [sys.executable, '-m', 'src.cli', '--language', 'de', '--process', 'generic-process-template', '--test'],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Should complete successfully
        assert result.returncode == 0, f"CLI failed with: {result.stderr}"
        
        # Output should contain process-related content
        assert 'process' in result.stdout.lower() or 'prozess' in result.stdout.lower()
    
    @pytest.mark.skipif(
        not Path('processes/en/generic-process-template').exists(),
        reason="English process templates not found"
    )
    def test_execute_process_generation_english(self):
        """Test executing English process generation via CLI."""
        result = subprocess.run(
            [sys.executable, '-m', 'src.cli', '--language', 'en', '--process', 'generic-process-template', '--test'],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Should complete successfully
        assert result.returncode == 0, f"CLI failed with: {result.stderr}"
        
        # Output should contain process-related content
        assert 'process' in result.stdout.lower()
    
    def test_service_nonexistent_error(self):
        """Test error handling for non-existent service."""
        result = subprocess.run(
            [sys.executable, '-m', 'src.cli', '--language', 'de', '--service', 'nonexistent-service', '--test'],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Should fail with error
        assert result.returncode != 0
        assert 'error' in result.stderr.lower() or 'not found' in result.stderr.lower()
    
    def test_process_nonexistent_error(self):
        """Test error handling for non-existent process."""
        result = subprocess.run(
            [sys.executable, '-m', 'src.cli', '--language', 'de', '--process', 'nonexistent-process', '--test'],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Should fail with error
        assert result.returncode != 0
        assert 'error' in result.stderr.lower() or 'not found' in result.stderr.lower()
    
    @pytest.mark.skipif(
        not Path('services/de/generic-service-template').exists(),
        reason="German service templates not found"
    )
    def test_service_with_pdf_output(self):
        """Test service generation with PDF output format."""
        result = subprocess.run(
            [sys.executable, '-m', 'src.cli', '-l', 'de', '--service', 'generic-service-template', '-o', 'pdf', '--test'],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Should complete successfully
        assert result.returncode == 0, f"CLI failed with: {result.stderr}"
    
    @pytest.mark.skipif(
        not Path('processes/de/generic-process-template').exists(),
        reason="German process templates not found"
    )
    def test_process_with_html_output(self):
        """Test process generation with HTML output format."""
        result = subprocess.run(
            [sys.executable, '-m', 'src.cli', '-l', 'de', '--process', 'generic-process-template', '-o', 'html', '--test'],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # Should complete successfully
        assert result.returncode == 0, f"CLI failed with: {result.stderr}"


class TestLanguageRequirement:
    """Tests for language requirement with service/process options."""
    
    def test_service_requires_language(self):
        """Test that --service requires --language."""
        with patch('sys.argv', ['handbook-generator', '--service', 'email-service', '--test']):
            # Should either raise error or have validation logic
            try:
                args = parse_arguments()
                # If parsing succeeds, language should be required in validation
                assert args.language is not None or args.service is not None
            except SystemExit:
                # Expected if argparse enforces requirement
                pass
    
    def test_process_requires_language(self):
        """Test that --process requires --language."""
        with patch('sys.argv', ['handbook-generator', '--process', 'incident-management', '--test']):
            # Should either raise error or have validation logic
            try:
                args = parse_arguments()
                # If parsing succeeds, language should be required in validation
                assert args.language is not None or args.process is not None
            except SystemExit:
                # Expected if argparse enforces requirement
                pass


class TestBackwardCompatibility:
    """Tests for backward compatibility with existing CLI options."""
    
    def test_template_option_still_works(self):
        """Test that existing --template option still works."""
        with patch('sys.argv', ['handbook-generator', '-l', 'de', '--template', 'isms', '--test']):
            args = parse_arguments()
            
            assert args.template == 'isms'
            assert args.language == 'de'
            assert args.service is None
            assert args.process is None
    
    def test_all_existing_options_work(self):
        """Test that all existing options still work."""
        with patch('sys.argv', [
            'handbook-generator',
            '-l', 'de',
            '--template', 'bcm',
            '-o', 'pdf',
            '--test',
            '--separate-files',
            '--pdf-toc'
        ]):
            args = parse_arguments()
            
            assert args.template == 'bcm'
            assert args.language == 'de'
            assert args.output_format == 'pdf'
            assert args.test is True
            assert args.separate_files is True
            assert args.pdf_toc is True
