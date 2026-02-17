"""
Tests for CLI interface.

This module contains unit tests for the command-line interface,
including argument parsing, execution modes, and error handling.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

import pytest
import sys
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
from io import StringIO

from src.quality_control.cli import (
    create_parser,
    run_quality_control,
    main
)
from src.quality_control.data_structures import (
    QualityReport,
    QualityMetrics,
    ValidationResult,
    VersionHistoryValidationResult,
    TestResult,
    FrameworkInfo,
    TemplateFile,
    FailedTest
)


class TestArgumentParsing:
    """Tests for command-line argument parsing."""
    
    def test_parser_creation(self):
        """Test that parser is created successfully."""
        parser = create_parser()
        assert parser is not None
        assert parser.prog == 'quality-control'
    
    def test_default_arguments(self):
        """Test default argument values."""
        parser = create_parser()
        args = parser.parse_args([])
        
        assert args.check == 'all'
        assert args.output is None
        assert args.verbose is False
        assert args.export_json is None
        assert args.export_csv is None
        assert args.base_path == '.'
        assert args.no_save_metrics is False
        assert args.interactive is False
        assert args.save_tasks is None
        assert args.show_remediation is False
        assert args.generate_remediation_script is None
    
    def test_check_argument_all(self):
        """Test --check argument with 'all' value."""
        parser = create_parser()
        args = parser.parse_args(['--check', 'all'])
        assert args.check == 'all'
    
    def test_check_argument_mapping(self):
        """Test --check argument with 'mapping' value."""
        parser = create_parser()
        args = parser.parse_args(['--check', 'mapping'])
        assert args.check == 'mapping'
    
    def test_check_argument_version(self):
        """Test --check argument with 'version' value."""
        parser = create_parser()
        args = parser.parse_args(['--check', 'version'])
        assert args.check == 'version'
    
    def test_check_argument_tests(self):
        """Test --check argument with 'tests' value."""
        parser = create_parser()
        args = parser.parse_args(['--check', 'tests'])
        assert args.check == 'tests'
    
    def test_check_argument_coverage(self):
        """Test --check argument with 'coverage' value."""
        parser = create_parser()
        args = parser.parse_args(['--check', 'coverage'])
        assert args.check == 'coverage'
    
    def test_output_argument(self):
        """Test --output argument."""
        parser = create_parser()
        args = parser.parse_args(['--output', 'report.txt'])
        assert args.output == 'report.txt'
    
    def test_verbose_argument(self):
        """Test --verbose argument."""
        parser = create_parser()
        args = parser.parse_args(['--verbose'])
        assert args.verbose is True
    
    def test_verbose_short_argument(self):
        """Test -v short form of verbose argument."""
        parser = create_parser()
        args = parser.parse_args(['-v'])
        assert args.verbose is True
    
    def test_export_json_argument(self):
        """Test --export-json argument."""
        parser = create_parser()
        args = parser.parse_args(['--export-json', 'metrics.json'])
        assert args.export_json == 'metrics.json'
    
    def test_export_csv_argument(self):
        """Test --export-csv argument."""
        parser = create_parser()
        args = parser.parse_args(['--export-csv', 'metrics.csv'])
        assert args.export_csv == 'metrics.csv'
    
    def test_base_path_argument(self):
        """Test --base-path argument."""
        parser = create_parser()
        args = parser.parse_args(['--base-path', '/custom/path'])
        assert args.base_path == '/custom/path'
    
    def test_no_save_metrics_argument(self):
        """Test --no-save-metrics argument."""
        parser = create_parser()
        args = parser.parse_args(['--no-save-metrics'])
        assert args.no_save_metrics is True
    
    def test_interactive_argument(self):
        """Test --interactive argument."""
        parser = create_parser()
        args = parser.parse_args(['--interactive'])
        assert args.interactive is True
    
    def test_interactive_short_argument(self):
        """Test -i short form of interactive argument."""
        parser = create_parser()
        args = parser.parse_args(['-i'])
        assert args.interactive is True
    
    def test_save_tasks_argument(self):
        """Test --save-tasks argument."""
        parser = create_parser()
        args = parser.parse_args(['--save-tasks', 'tasks.md'])
        assert args.save_tasks == 'tasks.md'
    
    def test_show_remediation_argument(self):
        """Test --show-remediation argument."""
        parser = create_parser()
        args = parser.parse_args(['--show-remediation'])
        assert args.show_remediation is True
    
    def test_generate_remediation_script_argument(self):
        """Test --generate-remediation-script argument."""
        parser = create_parser()
        args = parser.parse_args(['--generate-remediation-script', 'fix.sh'])
        assert args.generate_remediation_script == 'fix.sh'
    
    def test_multiple_arguments(self):
        """Test multiple arguments together."""
        parser = create_parser()
        args = parser.parse_args([
            '--check', 'mapping',
            '--output', 'report.txt',
            '--verbose',
            '--export-json', 'metrics.json'
        ])
        
        assert args.check == 'mapping'
        assert args.output == 'report.txt'
        assert args.verbose is True
        assert args.export_json == 'metrics.json'
    
    def test_invalid_check_value(self):
        """Test that invalid check value raises error."""
        parser = create_parser()
        
        with pytest.raises(SystemExit):
            parser.parse_args(['--check', 'invalid'])


class TestExecutionModes:
    """Tests for different execution modes."""
    
    @patch('src.quality_control.cli.QualityControlOrchestrator')
    @patch('src.quality_control.cli.setup_logging')
    def test_run_all_checks_mode(self, mock_logging, mock_orchestrator):
        """Test running all checks mode."""
        # Setup mock
        mock_instance = Mock()
        mock_orchestrator.return_value = mock_instance
        
        # Create mock report
        mock_report = Mock(spec=QualityReport)
        mock_report.overall_success = True
        mock_report.mapping_validation = Mock(spec=ValidationResult)
        mock_report.version_validation = Mock(spec=VersionHistoryValidationResult)
        mock_report.test_results = Mock(spec=TestResult)
        mock_report.test_results.failed_tests = []
        mock_report.metrics = Mock(spec=QualityMetrics)
        
        mock_instance.run_all_checks.return_value = mock_report
        mock_instance.generate_consolidated_report.return_value = "Test Report"
        
        # Execute
        exit_code = run_quality_control(
            check='all',
            base_path='.',
            output=None,
            verbose=False,
            export_json=None,
            export_csv=None,
            save_metrics=True,
            interactive=False,
            save_tasks=None,
            show_remediation=False,
            generate_remediation_script=None
        )
        
        # Verify
        assert exit_code == 0
        mock_instance.run_all_checks.assert_called_once()
        mock_instance.generate_consolidated_report.assert_called_once()
    
    @patch('src.quality_control.cli.QualityControlOrchestrator')
    @patch('src.quality_control.cli.setup_logging')
    def test_run_specific_check_mode(self, mock_logging, mock_orchestrator):
        """Test running specific check mode."""
        # Setup mock
        mock_instance = Mock()
        mock_orchestrator.return_value = mock_instance
        
        # Create mock result
        mock_result = Mock(spec=ValidationResult)
        mock_result.success = True
        mock_result.total_frameworks = 10
        mock_result.valid_frameworks = 10
        
        mock_instance.run_specific_check.return_value = mock_result
        
        # Execute
        exit_code = run_quality_control(
            check='mapping',
            base_path='.',
            output=None,
            verbose=False,
            export_json=None,
            export_csv=None,
            save_metrics=True,
            interactive=False,
            save_tasks=None,
            show_remediation=False,
            generate_remediation_script=None
        )
        
        # Verify
        assert exit_code == 0
        mock_instance.run_specific_check.assert_called_once_with('mapping')
    
    @patch('src.quality_control.cli.QualityControlOrchestrator')
    @patch('src.quality_control.cli.setup_logging')
    def test_save_metrics_mode(self, mock_logging, mock_orchestrator):
        """Test that metrics are saved when requested."""
        # Setup mock
        mock_instance = Mock()
        mock_orchestrator.return_value = mock_instance
        
        mock_report = Mock(spec=QualityReport)
        mock_report.overall_success = True
        mock_report.test_results = Mock(spec=TestResult)
        mock_report.test_results.failed_tests = []
        
        mock_instance.run_all_checks.return_value = mock_report
        mock_instance.generate_consolidated_report.return_value = "Test Report"
        
        # Execute with save_metrics=True
        run_quality_control(
            check='all',
            base_path='.',
            output=None,
            verbose=False,
            export_json=None,
            export_csv=None,
            save_metrics=True,
            interactive=False,
            save_tasks=None,
            show_remediation=False,
            generate_remediation_script=None
        )
        
        # Verify save_metrics was called
        mock_instance.save_metrics.assert_called_once_with(mock_report)
    
    @patch('src.quality_control.cli.QualityControlOrchestrator')
    @patch('src.quality_control.cli.setup_logging')
    def test_no_save_metrics_mode(self, mock_logging, mock_orchestrator):
        """Test that metrics are not saved when disabled."""
        # Setup mock
        mock_instance = Mock()
        mock_orchestrator.return_value = mock_instance
        
        mock_report = Mock(spec=QualityReport)
        mock_report.overall_success = True
        mock_report.test_results = Mock(spec=TestResult)
        mock_report.test_results.failed_tests = []
        
        mock_instance.run_all_checks.return_value = mock_report
        mock_instance.generate_consolidated_report.return_value = "Test Report"
        
        # Execute with save_metrics=False
        run_quality_control(
            check='all',
            base_path='.',
            output=None,
            verbose=False,
            export_json=None,
            export_csv=None,
            save_metrics=False,
            interactive=False,
            save_tasks=None,
            show_remediation=False,
            generate_remediation_script=None
        )
        
        # Verify save_metrics was NOT called
        mock_instance.save_metrics.assert_not_called()
    
    @patch('src.quality_control.cli.QualityControlOrchestrator')
    @patch('src.quality_control.cli.setup_logging')
    def test_export_json_mode(self, mock_logging, mock_orchestrator):
        """Test exporting metrics to JSON."""
        # Setup mock
        mock_instance = Mock()
        mock_orchestrator.return_value = mock_instance
        
        mock_report = Mock(spec=QualityReport)
        mock_report.overall_success = True
        mock_report.test_results = Mock(spec=TestResult)
        mock_report.test_results.failed_tests = []
        
        mock_instance.run_all_checks.return_value = mock_report
        mock_instance.generate_consolidated_report.return_value = "Test Report"
        
        # Execute with export_json
        run_quality_control(
            check='all',
            base_path='.',
            output=None,
            verbose=False,
            export_json='metrics.json',
            export_csv=None,
            save_metrics=True,
            interactive=False,
            save_tasks=None,
            show_remediation=False,
            generate_remediation_script=None
        )
        
        # Verify export was called
        mock_instance.export_metrics_json.assert_called_once_with(mock_report, 'metrics.json')
    
    @patch('src.quality_control.cli.QualityControlOrchestrator')
    @patch('src.quality_control.cli.setup_logging')
    def test_export_csv_mode(self, mock_logging, mock_orchestrator):
        """Test exporting metrics to CSV."""
        # Setup mock
        mock_instance = Mock()
        mock_orchestrator.return_value = mock_instance
        
        mock_report = Mock(spec=QualityReport)
        mock_report.overall_success = True
        mock_report.test_results = Mock(spec=TestResult)
        mock_report.test_results.failed_tests = []
        
        mock_instance.run_all_checks.return_value = mock_report
        mock_instance.generate_consolidated_report.return_value = "Test Report"
        
        # Execute with export_csv
        run_quality_control(
            check='all',
            base_path='.',
            output=None,
            verbose=False,
            export_json=None,
            export_csv='metrics.csv',
            save_metrics=True,
            interactive=False,
            save_tasks=None,
            show_remediation=False,
            generate_remediation_script=None
        )
        
        # Verify export was called
        mock_instance.export_metrics_csv.assert_called_once_with(mock_report, 'metrics.csv')


class TestErrorHandling:
    """Tests for error handling in CLI."""
    
    @patch('src.quality_control.cli.QualityControlOrchestrator')
    @patch('src.quality_control.cli.setup_logging')
    def test_exception_handling(self, mock_logging, mock_orchestrator):
        """Test that exceptions are handled gracefully."""
        # Setup mock to raise exception
        mock_instance = Mock()
        mock_orchestrator.return_value = mock_instance
        mock_instance.run_all_checks.side_effect = Exception("Test error")
        
        # Execute
        exit_code = run_quality_control(
            check='all',
            base_path='.',
            output=None,
            verbose=False,
            export_json=None,
            export_csv=None,
            save_metrics=True,
            interactive=False,
            save_tasks=None,
            show_remediation=False,
            generate_remediation_script=None
        )
        
        # Verify error exit code
        assert exit_code == 1
    
    @patch('src.quality_control.cli.QualityControlOrchestrator')
    @patch('src.quality_control.cli.setup_logging')
    def test_failed_checks_return_error_code(self, mock_logging, mock_orchestrator):
        """Test that failed checks return error exit code."""
        # Setup mock
        mock_instance = Mock()
        mock_orchestrator.return_value = mock_instance
        
        mock_report = Mock(spec=QualityReport)
        mock_report.overall_success = False  # Failed
        mock_report.test_results = Mock(spec=TestResult)
        mock_report.test_results.failed_tests = []
        
        mock_instance.run_all_checks.return_value = mock_report
        mock_instance.generate_consolidated_report.return_value = "Test Report"
        
        # Execute
        exit_code = run_quality_control(
            check='all',
            base_path='.',
            output=None,
            verbose=False,
            export_json=None,
            export_csv=None,
            save_metrics=True,
            interactive=False,
            save_tasks=None,
            show_remediation=False,
            generate_remediation_script=None
        )
        
        # Verify error exit code
        assert exit_code == 1
    
    @patch('src.quality_control.cli.QualityControlOrchestrator')
    @patch('src.quality_control.cli.setup_logging')
    def test_output_file_creation(self, mock_logging, mock_orchestrator):
        """Test that output file is created correctly."""
        # Setup mock
        mock_instance = Mock()
        mock_orchestrator.return_value = mock_instance
        
        mock_report = Mock(spec=QualityReport)
        mock_report.overall_success = True
        mock_report.test_results = Mock(spec=TestResult)
        mock_report.test_results.failed_tests = []
        
        mock_instance.run_all_checks.return_value = mock_report
        mock_instance.generate_consolidated_report.return_value = "Test Report Content"
        
        # Execute with temporary output file
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "report.txt"
            
            run_quality_control(
                check='all',
                base_path='.',
                output=str(output_path),
                verbose=False,
                export_json=None,
                export_csv=None,
                save_metrics=False,
                interactive=False,
                save_tasks=None,
                show_remediation=False,
                generate_remediation_script=None
            )
            
            # Verify file was created
            assert output_path.exists()
            
            # Verify content
            with open(output_path, 'r') as f:
                content = f.read()
            assert content == "Test Report Content"


class TestMainFunction:
    """Tests for main entry point function."""
    
    @patch('src.quality_control.cli.run_quality_control')
    @patch('sys.argv', ['quality-control', '--check', 'all'])
    def test_main_calls_run_quality_control(self, mock_run):
        """Test that main function calls run_quality_control."""
        mock_run.return_value = 0
        
        with pytest.raises(SystemExit) as exc_info:
            main()
        
        assert exc_info.value.code == 0
        mock_run.assert_called_once()
    
    @patch('src.quality_control.cli.run_quality_control')
    @patch('sys.argv', ['quality-control', '--check', 'mapping', '--verbose'])
    def test_main_with_arguments(self, mock_run):
        """Test main function with command-line arguments."""
        mock_run.return_value = 0
        
        with pytest.raises(SystemExit) as exc_info:
            main()
        
        assert exc_info.value.code == 0
        
        # Verify arguments were passed correctly
        call_args = mock_run.call_args
        assert call_args.kwargs['check'] == 'mapping'
        assert call_args.kwargs['verbose'] is True
    
    @patch('src.quality_control.cli.run_quality_control')
    @patch('sys.argv', ['quality-control'])
    def test_main_with_error_exit_code(self, mock_run):
        """Test main function with error exit code."""
        mock_run.return_value = 1
        
        with pytest.raises(SystemExit) as exc_info:
            main()
        
        assert exc_info.value.code == 1
