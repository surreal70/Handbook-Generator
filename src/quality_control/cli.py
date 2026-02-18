"""
Command-line interface for the Quality Control System.

This module provides a CLI for running quality control checks, viewing reports,
and managing quality metrics.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

import argparse
import sys
import logging
from pathlib import Path
from typing import Optional

from .quality_control_orchestrator import QualityControlOrchestrator
from .logging_config import setup_logging
from .interactive_mode import InteractiveMode
from .remediation_suggestions import RemediationSuggestions


def create_parser() -> argparse.ArgumentParser:
    """
    Create and configure the argument parser for the CLI.
    
    Returns:
        Configured ArgumentParser instance
    """
    parser = argparse.ArgumentParser(
        prog='quality-control',
        description='Quality Control System for Handbook Generator',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run all quality checks
  python -m src.quality_control.cli
  
  # Run specific check
  python -m src.quality_control.cli --check mapping
  
  # Run unit tests only (default)
  python -m src.quality_control.cli --check tests
  
  # Run property-based tests
  python -m src.quality_control.cli --check tests --test-category property
  
  # Run all tests (including slow tests)
  python -m src.quality_control.cli --check tests --test-category all
  
  # Run with verbose output
  python -m src.quality_control.cli --verbose
  
  # Save report to custom location
  python -m src.quality_control.cli --output reports/quality_report.txt
  
  # Export metrics to JSON
  python -m src.quality_control.cli --export-json metrics.json
  
  # Export metrics to CSV
  python -m src.quality_control.cli --export-csv metrics.csv

Available checks:
  all       - Run all quality checks (default)
  mapping   - Framework mapping file validation
  version   - Version history validation
  tests     - Test suite execution
  coverage  - Coverage documentation generation

Test categories (for --check tests):
  unit        - Unit tests only (fast, isolated tests) [default]
  integration - Integration tests (component interaction)
  property    - Property-based tests (Hypothesis)
  slow        - Slow tests (long-running)
  all         - All tests (unit, integration, property, slow)
        """
    )
    
    parser.add_argument(
        '--check',
        type=str,
        default='all',
        choices=['all', 'mapping', 'version', 'tests', 'coverage'],
        help='Specify which check to run (default: all)'
    )
    
    parser.add_argument(
        '--test-category',
        type=str,
        default='unit',
        choices=['unit', 'integration', 'property', 'slow', 'all'],
        help='Test category to run when --check tests is used (default: unit)'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        default=None,
        help='Path where to save the quality report (default: print to stdout)'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose logging output'
    )
    
    parser.add_argument(
        '--export-json',
        type=str,
        default=None,
        metavar='PATH',
        help='Export metrics to JSON file at specified path'
    )
    
    parser.add_argument(
        '--export-csv',
        type=str,
        default=None,
        metavar='PATH',
        help='Export metrics to CSV file at specified path'
    )
    
    parser.add_argument(
        '--base-path',
        type=str,
        default='.',
        help='Base path to the project root (default: current directory)'
    )
    
    parser.add_argument(
        '--no-save-metrics',
        action='store_true',
        help='Do not save metrics to history file'
    )
    
    parser.add_argument(
        '--interactive', '-i',
        action='store_true',
        help='Enable interactive mode for handling failed tests'
    )
    
    parser.add_argument(
        '--save-tasks',
        type=str,
        default=None,
        metavar='PATH',
        help='Save created tasks to file (used with --interactive)'
    )
    
    parser.add_argument(
        '--show-remediation',
        action='store_true',
        help='Show remediation suggestions for identified issues'
    )
    
    parser.add_argument(
        '--generate-remediation-script',
        type=str,
        default=None,
        metavar='PATH',
        help='Generate batch remediation script and save to specified path'
    )
    
    return parser


def run_quality_control(
    check: str,
    base_path: str,
    output: Optional[str],
    verbose: bool,
    export_json: Optional[str],
    export_csv: Optional[str],
    save_metrics: bool,
    interactive: bool,
    save_tasks: Optional[str],
    show_remediation: bool,
    generate_remediation_script: Optional[str],
    test_category: str = 'unit'
) -> int:
    """
    Execute quality control checks based on CLI arguments.
    
    Args:
        check: Which check to run ('all' or specific check name)
        base_path: Base path to the project root
        output: Path where to save the report (None for stdout)
        verbose: Enable verbose logging
        export_json: Path to export metrics as JSON (None to skip)
        export_csv: Path to export metrics as CSV (None to skip)
        save_metrics: Whether to save metrics to history file
        interactive: Enable interactive mode for failed tests
        save_tasks: Path to save created tasks (None to skip)
        show_remediation: Show remediation suggestions
        generate_remediation_script: Path to save remediation script (None to skip)
        test_category: Test category to run ('unit', 'integration', 'property', 'slow', 'all')
        
    Returns:
        Exit code (0 for success, 1 for failure)
    """
    # Setup logging
    log_level = "DEBUG" if verbose else "INFO"
    setup_logging(log_level)
    logger = logging.getLogger(__name__)
    
    try:
        # Initialize orchestrator
        logger.info(f"Initializing Quality Control System (base path: {base_path})")
        orchestrator = QualityControlOrchestrator(base_path, test_category=test_category)
        
        # Execute checks
        if check == 'all':
            logger.info("Running all quality checks...")
            report = orchestrator.run_all_checks()
        else:
            logger.info(f"Running {check} check...")
            
            if verbose:
                print(f"\n{'='*80}")
                print(f"QUALITY CONTROL: {check.upper()} CHECK")
                print(f"{'='*80}\n")
            
            result = orchestrator.run_specific_check(check)
            
            # For specific checks, we need to create a minimal report
            # This is a simplified report for single check execution
            print(f"\n{check.upper()} CHECK RESULTS")
            print("=" * 80)
            
            if hasattr(result, 'success'):
                print(f"Status: {'PASSED' if result.success else 'FAILED'}")
                
                # Print relevant details based on check type
                if check == 'mapping':
                    print(f"Total Frameworks: {result.total_frameworks}")
                    print(f"Valid Frameworks: {result.valid_frameworks}")
                    if not result.success:
                        print(f"Invalid Frameworks: {len(result.invalid_frameworks)}")
                        print(f"Missing Files: {len(result.missing_files)}")
                        
                        if verbose and result.invalid_frameworks:
                            print(f"\nInvalid Frameworks:")
                            for fw in result.invalid_frameworks:
                                print(f"  - {fw.name} ({fw.language}): {fw.path}")
                        
                        if verbose and result.missing_files:
                            print(f"\nMissing Mapping Files:")
                            for fw in result.missing_files:
                                print(f"  - {fw.name} ({fw.language}): {fw.path}")
                
                elif check == 'version':
                    print(f"Total Templates: {result.total_templates}")
                    print(f"Valid Templates: {result.valid_templates}")
                    
                    if result.error and "disabled" in result.error.lower():
                        print(f"\nNote: {result.error}")
                    elif not result.success:
                        print(f"Missing Version History: {len(result.missing_version_history)}")
                        print(f"Invalid Format: {len(result.invalid_format)}")
                        
                        if verbose and result.missing_version_history:
                            print(f"\nTemplates Missing Version History (showing first 10):")
                            for tmpl in result.missing_version_history[:10]:
                                print(f"  - {tmpl.path}")
                            if len(result.missing_version_history) > 10:
                                print(f"  ... and {len(result.missing_version_history) - 10} more")
                
                elif check == 'tests':
                    print(f"Total Tests: {result.total_tests}")
                    print(f"Passed: {result.passed}")
                    print(f"Failed: {result.failed}")
                    print(f"Skipped: {result.skipped}")
                    print(f"Duration: {result.duration:.2f}s")
                    
                    if result.failed > 0:
                        print(f"\nFailed Tests:")
                        for test in result.failed_tests[:10]:
                            print(f"  - {test.name}")
                            if verbose:
                                print(f"    Reason: {test.failure_reason}")
                        if len(result.failed_tests) > 10:
                            print(f"  ... and {len(result.failed_tests) - 10} more")
                        
                        if interactive:
                            print(f"\nEntering interactive mode to handle failed tests...")
                            interactive_handler = InteractiveMode()
                            tasks = interactive_handler.handle_failed_tests(result.failed_tests)
                            
                            if save_tasks and tasks:
                                logger.info(f"Saving {len(tasks)} tasks to {save_tasks}")
                                interactive_handler.save_tasks(tasks, save_tasks)
                
                elif check == 'coverage':
                    print(f"Frameworks discovered: {len(result)}")
                    if verbose:
                        for fw in result:
                            consistency = "✓" if fw.bilingual_consistent else "✗"
                            print(f"  {consistency} {fw.name}: DE={fw.template_count_de}, EN={fw.template_count_en}")
                    else:
                        for fw in result[:5]:
                            print(f"  - {fw.name}: DE={fw.template_count_de}, EN={fw.template_count_en}")
                        if len(result) > 5:
                            print(f"  ... and {len(result) - 5} more (use --verbose to see all)")
            
            print("=" * 80)
            
            return 0 if (hasattr(result, 'success') and result.success) or check == 'coverage' else 1
        
        # Generate consolidated report
        logger.info("Generating consolidated report...")
        report_text = orchestrator.generate_consolidated_report(report)
        
        # Handle interactive mode for failed tests
        if interactive and report.test_results.failed_tests:
            logger.info("Entering interactive mode for failed tests...")
            interactive_handler = InteractiveMode()
            result = interactive_handler.process_failed_tests(report.test_results.failed_tests)
            
            # Save tasks if requested
            if save_tasks and result['created_tasks']:
                interactive_handler.save_tasks_to_file(save_tasks)
            elif result['created_tasks'] and not save_tasks:
                # Default location if tasks were created but no path specified
                default_path = Path(base_path) / "failed_test_tasks.md"
                interactive_handler.save_tasks_to_file(str(default_path))
        
        # Output report
        if output:
            output_path = Path(output)
            output_path.parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(report_text)
            logger.info(f"Report saved to: {output_path}")
        else:
            print("\n" + report_text)
        
        # Save metrics to history
        if save_metrics:
            logger.info("Saving metrics to history...")
            orchestrator.save_metrics(report)
        
        # Export metrics if requested
        if export_json:
            logger.info(f"Exporting metrics to JSON: {export_json}")
            orchestrator.export_metrics_json(report, export_json)
        
        if export_csv:
            logger.info(f"Exporting metrics to CSV: {export_csv}")
            orchestrator.export_metrics_csv(report, export_csv)
        
        # Show remediation suggestions if requested
        if show_remediation and not report.overall_success:
            logger.info("Generating remediation suggestions...")
            remediation = RemediationSuggestions()
            
            # Get frameworks for translation suggestions
            frameworks = orchestrator.coverage_generator.discover_frameworks()
            
            remediation_report = remediation.generate_remediation_report(
                report.mapping_validation,
                report.version_validation,
                frameworks
            )
            print("\n" + remediation_report)
        
        # Generate remediation script if requested
        if generate_remediation_script:
            logger.info(f"Generating remediation script: {generate_remediation_script}")
            remediation = RemediationSuggestions()
            
            # Get frameworks for translation suggestions
            frameworks = orchestrator.coverage_generator.discover_frameworks()
            
            remediation.save_remediation_script(
                report.mapping_validation,
                report.version_validation,
                frameworks,
                generate_remediation_script
            )
        
        # Return exit code based on overall success
        return 0 if report.overall_success else 1
        
    except Exception as e:
        logger.error(f"Quality control execution failed: {e}", exc_info=True)
        return 1


def main():
    """Main entry point for the CLI."""
    parser = create_parser()
    args = parser.parse_args()
    
    exit_code = run_quality_control(
        check=args.check,
        base_path=args.base_path,
        output=args.output,
        verbose=args.verbose,
        export_json=args.export_json,
        export_csv=args.export_csv,
        save_metrics=not args.no_save_metrics,
        interactive=args.interactive,
        save_tasks=args.save_tasks,
        show_remediation=args.show_remediation,
        generate_remediation_script=args.generate_remediation_script,
        test_category=args.test_category
    )
    
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
