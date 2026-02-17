"""
Quality Control Orchestrator for the Quality Control System.

This module coordinates the execution of all validators, consolidates results,
tracks quality metrics, and generates comprehensive reports.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

import json
import csv
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional, List
import logging
import time

from .framework_mapping_validator import FrameworkMappingValidator
from .version_history_validator import VersionHistoryValidator
from .test_suite_runner import TestSuiteRunner
from .coverage_documentation_generator import CoverageDocumentationGenerator
from .data_structures import (
    QualityReport,
    QualityMetrics,
    ValidationResult,
    VersionHistoryValidationResult,
    TestResult,
    Framework
)


class QualityControlOrchestrator:
    """
    Orchestrates execution of all quality control validators.
    
    This class coordinates the execution of all validation checks in sequence,
    consolidates results, calculates quality metrics, and generates comprehensive
    reports.
    """
    
    def __init__(self, base_path: str = ".", test_category: str = "unit"):
        """
        Initialize the Quality Control Orchestrator.
        
        Args:
            base_path: Base path to the project root (default: current directory)
            test_category: Test category to run ('unit', 'integration', 'property', 'slow', 'all')
        """
        self.base_path = Path(base_path)
        self.logger = logging.getLogger(__name__)
        self.test_category = test_category
        
        # Initialize all validator components
        self.mapping_validator = FrameworkMappingValidator(str(self.base_path))
        self.version_validator = VersionHistoryValidator(str(self.base_path))
        self.test_runner = TestSuiteRunner("tests/")
        self.coverage_generator = CoverageDocumentationGenerator(str(self.base_path))
        
        # Quality metrics directory
        self.quality_dir = self.base_path / ".quality"
        self.metrics_history_file = self.quality_dir / "metrics_history.json"
        self.last_run_file = self.quality_dir / "last_run.json"
    
    def run_all_checks(self) -> QualityReport:
        """
        Execute all quality control checks in sequence.
        
        Executes validators in the specified order:
        1. Framework Mapping validation
        2. Version History validation
        3. Test Suite execution
        4. Coverage Documentation generation
        
        Continues execution even if individual checks fail, collecting all results.
        
        Returns:
            QualityReport object with consolidated results from all checks
        """
        self.logger.info("Starting quality control execution")
        start_time = time.time()
        timestamp = datetime.now()
        
        # Execute validators in sequence
        # Continue even if individual checks fail
        
        # 1. Framework Mapping validation
        self.logger.info("Step 1/4: Validating framework mapping files")
        mapping_validation = self._run_check(
            "Framework Mapping Validation",
            self.mapping_validator.validate
        )
        
        # 2. Version History validation (DISABLED)
        self.logger.info("Step 2/4: Version History validation (DISABLED - will be re-enabled after defining new versioning scheme)")
        version_validation = VersionHistoryValidationResult(
            total_templates=0,
            valid_templates=0,
            missing_version_history=[],
            invalid_format=[],
            success=True,
            error="Version History validation is currently disabled. Will be re-enabled after defining new versioning scheme."
        )
        
        # 3. Test Suite execution
        self.logger.info(f"Step 3/4: Executing test suite (category: {self.test_category})")
        test_results = self._run_check(
            "Test Suite Execution",
            lambda: self.test_runner.execute_tests(category=self.test_category)
        )
        
        # 4. Coverage Documentation generation
        self.logger.info("Step 4/4: Generating coverage documentation")
        frameworks = self._run_check(
            "Coverage Documentation Generation",
            self.coverage_generator.discover_frameworks
        )
        
        # Generate coverage documentation
        if frameworks and isinstance(frameworks, list):
            coverage_documentation = self.coverage_generator.generate_markdown_documentation(frameworks)
        else:
            coverage_documentation = "Coverage documentation generation failed"
            frameworks = []
        
        # Calculate execution duration
        execution_duration = time.time() - start_time
        
        # Calculate quality metrics
        metrics = self._calculate_metrics(
            mapping_validation,
            version_validation,
            test_results,
            frameworks
        )
        
        # Determine overall success
        overall_success = (
            mapping_validation.success and
            version_validation.success and
            test_results.success
        )
        
        # Create quality report
        report = QualityReport(
            timestamp=timestamp,
            mapping_validation=mapping_validation,
            version_validation=version_validation,
            test_results=test_results,
            coverage_documentation=coverage_documentation,
            overall_success=overall_success,
            metrics=metrics,
            execution_duration=execution_duration
        )
        
        self.logger.info(f"Quality control completed in {execution_duration:.2f}s")
        
        return report
    
    def _run_check(self, check_name: str, check_func):
        """
        Execute a single validation check with error handling.
        
        Args:
            check_name: Name of the check for logging
            check_func: Function to execute
            
        Returns:
            Result from check_func, or error result if check fails
        """
        try:
            result = check_func()
            if hasattr(result, 'success'):
                status = "PASSED" if result.success else "FAILED"
                self.logger.info(f"{check_name}: {status}")
            return result
        except Exception as e:
            self.logger.error(f"{check_name} failed with exception: {e}")
            # Return appropriate error result based on expected type
            if "Mapping" in check_name:
                return ValidationResult(
                    total_frameworks=0,
                    valid_frameworks=0,
                    invalid_frameworks=[],
                    missing_files=[],
                    success=False,
                    error=str(e)
                )
            elif "Version" in check_name:
                return VersionHistoryValidationResult(
                    total_templates=0,
                    valid_templates=0,
                    missing_version_history=[],
                    invalid_format=[],
                    success=False,
                    error=str(e)
                )
            elif "Test" in check_name:
                return TestResult(
                    total_tests=0,
                    passed=0,
                    failed=0,
                    skipped=0,
                    duration=0.0,
                    failed_tests=[],
                    success=False,
                    error=str(e)
                )
            else:
                return []
    
    def _calculate_metrics(
        self,
        mapping_validation: ValidationResult,
        version_validation: VersionHistoryValidationResult,
        test_results: TestResult,
        frameworks: List[Framework]
    ) -> QualityMetrics:
        """
        Calculate quality metrics from validation results.
        
        Args:
            mapping_validation: Framework mapping validation result
            version_validation: Version history validation result
            test_results: Test suite execution result
            frameworks: List of discovered frameworks
            
        Returns:
            QualityMetrics object with calculated percentages
        """
        # Framework mapping compliance rate
        if mapping_validation.total_frameworks > 0:
            framework_mapping_compliance = (
                mapping_validation.valid_frameworks / mapping_validation.total_frameworks
            ) * 100
        else:
            framework_mapping_compliance = 0.0
        
        # Version history compliance rate
        if version_validation.total_templates > 0:
            version_history_compliance = (
                version_validation.valid_templates / version_validation.total_templates
            ) * 100
        else:
            version_history_compliance = 0.0
        
        # Test pass rate
        if test_results.total_tests > 0:
            test_pass_rate = (test_results.passed / test_results.total_tests) * 100
        else:
            test_pass_rate = 0.0
        
        # Bilingual consistency rate
        if frameworks:
            consistent_count = sum(1 for f in frameworks if f.bilingual_consistent)
            bilingual_consistency_rate = (consistent_count / len(frameworks)) * 100
        else:
            bilingual_consistency_rate = 0.0
        
        return QualityMetrics(
            framework_mapping_compliance=framework_mapping_compliance,
            version_history_compliance=version_history_compliance,
            test_pass_rate=test_pass_rate,
            bilingual_consistency_rate=bilingual_consistency_rate
        )
    
    def run_specific_check(self, check_name: str):
        """
        Execute a specific validation check by name.
        
        Args:
            check_name: Name of the check to run. Valid values:
                       'mapping', 'version', 'tests', 'coverage'
            
        Returns:
            Result from the specified check
            
        Raises:
            ValueError: If check_name is not recognized
        """
        check_name_lower = check_name.lower()
        
        if check_name_lower in ['mapping', 'framework_mapping']:
            self.logger.info("Running Framework Mapping validation")
            return self.mapping_validator.validate()
        
        elif check_name_lower in ['version', 'version_history']:
            self.logger.info("Version History validation is currently DISABLED")
            self.logger.info("This check will be re-enabled after defining a new versioning scheme")
            # Return a disabled result
            return VersionHistoryValidationResult(
                total_templates=0,
                valid_templates=0,
                missing_version_history=[],
                invalid_format=[],
                success=True,
                error="Version History validation is currently disabled. Will be re-enabled after defining new versioning scheme."
            )
        
        elif check_name_lower in ['tests', 'test_suite']:
            self.logger.info(f"Running Test Suite execution (category: {self.test_category})")
            return self.test_runner.execute_tests(category=self.test_category)
        
        elif check_name_lower in ['coverage', 'documentation']:
            self.logger.info("Running Coverage Documentation generation")
            return self.coverage_generator.discover_frameworks()
        
        else:
            raise ValueError(
                f"Unknown check name: {check_name}. "
                f"Valid options: mapping, version, tests, coverage"
            )
    
    def generate_consolidated_report(self, report: QualityReport) -> str:
        """
        Generate a comprehensive consolidated report from all validation results.
        
        Aggregates results from all validators, includes timestamps and execution
        duration, calculates overall success status, and formats a comprehensive
        human-readable report.
        
        Args:
            report: QualityReport object containing all validation results
            
        Returns:
            Formatted consolidated report as a string
        """
        lines = []
        
        # Header
        lines.append("=" * 80)
        lines.append("QUALITY CONTROL CONSOLIDATED REPORT")
        lines.append("=" * 80)
        lines.append("")
        
        # Timestamp and execution info
        lines.append(f"Execution Time: {report.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append(f"Duration: {report.execution_duration:.2f} seconds")
        lines.append(f"Overall Status: {'PASSED' if report.overall_success else 'FAILED'}")
        lines.append("")
        
        # Quality Metrics Summary
        lines.append("-" * 80)
        lines.append("QUALITY METRICS")
        lines.append("-" * 80)
        lines.append(f"Framework Mapping Compliance: {report.metrics.framework_mapping_compliance:.1f}%")
        lines.append(f"Version History Compliance: {report.metrics.version_history_compliance:.1f}%")
        lines.append(f"Test Pass Rate: {report.metrics.test_pass_rate:.1f}%")
        lines.append(f"Bilingual Consistency Rate: {report.metrics.bilingual_consistency_rate:.1f}%")
        lines.append("")
        
        # Framework Mapping Validation Results
        lines.append("-" * 80)
        lines.append("1. FRAMEWORK MAPPING VALIDATION")
        lines.append("-" * 80)
        
        if report.mapping_validation.error:
            lines.append(f"Status: ERROR")
            lines.append(f"Error: {report.mapping_validation.error}")
        else:
            lines.append(f"Status: {'PASSED' if report.mapping_validation.success else 'FAILED'}")
            lines.append(f"Total Frameworks: {report.mapping_validation.total_frameworks}")
            lines.append(f"Valid Frameworks: {report.mapping_validation.valid_frameworks}")
            lines.append(f"Invalid Frameworks: {len(report.mapping_validation.invalid_frameworks)}")
            lines.append(f"Missing Files: {len(report.mapping_validation.missing_files)}")
            
            if not report.mapping_validation.success:
                if report.mapping_validation.invalid_frameworks:
                    lines.append("\nFrameworks with Incorrectly Named Mapping Files:")
                    for fw in report.mapping_validation.invalid_frameworks[:5]:
                        lines.append(f"  - {fw.language}/{fw.name}: {fw.mapping_file_name}")
                    if len(report.mapping_validation.invalid_frameworks) > 5:
                        remaining = len(report.mapping_validation.invalid_frameworks) - 5
                        lines.append(f"  ... and {remaining} more")
                
                if report.mapping_validation.missing_files:
                    lines.append("\nFrameworks with Missing Mapping Files:")
                    for fw in report.mapping_validation.missing_files[:5]:
                        lines.append(f"  - {fw.language}/{fw.name}")
                    if len(report.mapping_validation.missing_files) > 5:
                        remaining = len(report.mapping_validation.missing_files) - 5
                        lines.append(f"  ... and {remaining} more")
        
        lines.append("")
        
        # Version History Validation Results
        lines.append("-" * 80)
        lines.append("2. VERSION HISTORY VALIDATION")
        lines.append("-" * 80)
        
        if report.version_validation.error:
            lines.append(f"Status: ERROR")
            lines.append(f"Error: {report.version_validation.error}")
        else:
            lines.append(f"Status: {'PASSED' if report.version_validation.success else 'FAILED'}")
            lines.append(f"Total Templates: {report.version_validation.total_templates}")
            lines.append(f"Valid Templates: {report.version_validation.valid_templates}")
            lines.append(f"Missing Version History: {len(report.version_validation.missing_version_history)}")
            lines.append(f"Invalid Format: {len(report.version_validation.invalid_format)}")
            
            if not report.version_validation.success:
                if report.version_validation.missing_version_history:
                    lines.append("\nTemplates Missing Version History (first 5):")
                    for tpl in report.version_validation.missing_version_history[:5]:
                        lines.append(f"  - {tpl.framework}/{tpl.path.name}")
                    if len(report.version_validation.missing_version_history) > 5:
                        remaining = len(report.version_validation.missing_version_history) - 5
                        lines.append(f"  ... and {remaining} more")
        
        lines.append("")
        
        # Test Suite Results
        lines.append("-" * 80)
        lines.append("3. TEST SUITE EXECUTION")
        lines.append("-" * 80)
        
        if report.test_results.error:
            lines.append(f"Status: ERROR")
            lines.append(f"Error: {report.test_results.error}")
        else:
            lines.append(f"Status: {'PASSED' if report.test_results.success else 'FAILED'}")
            lines.append(f"Total Tests: {report.test_results.total_tests}")
            lines.append(f"Passed: {report.test_results.passed}")
            lines.append(f"Failed: {report.test_results.failed}")
            lines.append(f"Skipped: {report.test_results.skipped}")
            lines.append(f"Duration: {report.test_results.duration:.2f}s")
            
            if report.test_results.failed_tests:
                lines.append(f"\nFailed Tests (first 5):")
                for test in report.test_results.failed_tests[:5]:
                    lines.append(f"  - {test.name}")
                    lines.append(f"    Reason: {test.failure_reason[:100]}")
                if len(report.test_results.failed_tests) > 5:
                    remaining = len(report.test_results.failed_tests) - 5
                    lines.append(f"  ... and {remaining} more")
        
        lines.append("")
        
        # Coverage Documentation Status
        lines.append("-" * 80)
        lines.append("4. COVERAGE DOCUMENTATION")
        lines.append("-" * 80)
        
        if "failed" in report.coverage_documentation.lower():
            lines.append("Status: FAILED")
            lines.append(report.coverage_documentation)
        else:
            lines.append("Status: GENERATED")
            lines.append("Documentation generated successfully")
            # Count lines to give an idea of size
            doc_lines = report.coverage_documentation.count('\n')
            lines.append(f"Documentation size: {doc_lines} lines")
        
        lines.append("")
        
        # Recommendations
        lines.append("-" * 80)
        lines.append("RECOMMENDATIONS")
        lines.append("-" * 80)
        
        recommendations = []
        
        if not report.mapping_validation.success:
            recommendations.append(
                "• Fix framework mapping file issues: Ensure all frameworks have "
                "9999_Framework_Mapping.md files"
            )
        
        if not report.version_validation.success:
            recommendations.append(
                "• Add version history sections to templates: Use '## Version History' "
                "or '## Versionshistorie'"
            )
        
        if not report.test_results.success:
            recommendations.append(
                f"• Fix {report.test_results.failed} failing test(s): Review test failures "
                "and update code or tests"
            )
        
        if report.metrics.bilingual_consistency_rate < 100.0:
            recommendations.append(
                "• Improve bilingual consistency: Ensure German and English templates "
                "are in sync"
            )
        
        if recommendations:
            for rec in recommendations:
                lines.append(rec)
        else:
            lines.append("✓ All quality checks passed! No action required.")
        
        lines.append("")
        lines.append("=" * 80)
        
        return "\n".join(lines)
    
    def save_metrics(self, report: QualityReport) -> None:
        """
        Persist quality metrics to metrics history file.
        
        Creates .quality/ directory if it doesn't exist, saves metrics to
        metrics_history.json with timestamps, and appends to existing history.
        
        Args:
            report: QualityReport object containing metrics to save
            
        Raises:
            IOError: If file write fails
        """
        # Create .quality directory if it doesn't exist
        self.quality_dir.mkdir(parents=True, exist_ok=True)
        
        # Load existing metrics history
        metrics_history = {"runs": []}
        if self.metrics_history_file.exists():
            try:
                with open(self.metrics_history_file, 'r', encoding='utf-8') as f:
                    metrics_history = json.load(f)
            except Exception as e:
                self.logger.warning(f"Could not load existing metrics history: {e}")
                metrics_history = {"runs": []}
        
        # Create new metrics entry
        metrics_entry = {
            "timestamp": report.timestamp.isoformat(),
            "framework_mapping_compliance": report.metrics.framework_mapping_compliance,
            "version_history_compliance": report.metrics.version_history_compliance,
            "test_pass_rate": report.metrics.test_pass_rate,
            "bilingual_consistency_rate": report.metrics.bilingual_consistency_rate,
            "total_frameworks": report.mapping_validation.total_frameworks,
            "total_templates": report.version_validation.total_templates,
            "total_tests": report.test_results.total_tests,
            "execution_duration": report.execution_duration,
            "overall_success": report.overall_success
        }
        
        # Append to history
        metrics_history["runs"].append(metrics_entry)
        
        # Save updated history
        try:
            with open(self.metrics_history_file, 'w', encoding='utf-8') as f:
                json.dump(metrics_history, f, indent=2)
            
            self.logger.info(f"Metrics saved to {self.metrics_history_file}")
        except Exception as e:
            self.logger.error(f"Failed to save metrics: {e}")
            raise IOError(f"Failed to save metrics: {e}")
        
        # Also save as last run for quick access
        try:
            with open(self.last_run_file, 'w', encoding='utf-8') as f:
                json.dump(metrics_entry, f, indent=2)
        except Exception as e:
            self.logger.warning(f"Failed to save last run metrics: {e}")
    

    def export_metrics_json(self, report: QualityReport, output_path: str) -> None:
        """
        Export quality metrics to JSON format.
        
        Args:
            report: QualityReport object containing metrics to export
            output_path: Path where to save the JSON file
            
        Raises:
            IOError: If file write fails
        """
        metrics_data = {
            "timestamp": report.timestamp.isoformat(),
            "execution_duration": report.execution_duration,
            "overall_success": report.overall_success,
            "metrics": {
                "framework_mapping_compliance": report.metrics.framework_mapping_compliance,
                "version_history_compliance": report.metrics.version_history_compliance,
                "test_pass_rate": report.metrics.test_pass_rate,
                "bilingual_consistency_rate": report.metrics.bilingual_consistency_rate
            },
            "details": {
                "framework_mapping": {
                    "total_frameworks": report.mapping_validation.total_frameworks,
                    "valid_frameworks": report.mapping_validation.valid_frameworks,
                    "invalid_frameworks": len(report.mapping_validation.invalid_frameworks),
                    "missing_files": len(report.mapping_validation.missing_files),
                    "success": report.mapping_validation.success
                },
                "version_history": {
                    "total_templates": report.version_validation.total_templates,
                    "valid_templates": report.version_validation.valid_templates,
                    "missing_version_history": len(report.version_validation.missing_version_history),
                    "invalid_format": len(report.version_validation.invalid_format),
                    "success": report.version_validation.success
                },
                "test_suite": {
                    "total_tests": report.test_results.total_tests,
                    "passed": report.test_results.passed,
                    "failed": report.test_results.failed,
                    "skipped": report.test_results.skipped,
                    "duration": report.test_results.duration,
                    "success": report.test_results.success
                }
            }
        }
        
        try:
            output_file = Path(output_path)
            output_file.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(metrics_data, f, indent=2)
            
            self.logger.info(f"Metrics exported to JSON: {output_file}")
        except Exception as e:
            self.logger.error(f"Failed to export metrics to JSON: {e}")
            raise IOError(f"Failed to export metrics to JSON: {e}")
    
    def export_metrics_csv(self, report: QualityReport, output_path: str) -> None:
        """
        Export quality metrics to CSV format.
        
        Args:
            report: QualityReport object containing metrics to export
            output_path: Path where to save the CSV file
            
        Raises:
            IOError: If file write fails
        """
        try:
            output_file = Path(output_path)
            output_file.parent.mkdir(parents=True, exist_ok=True)
            
            # Check if file exists to determine if we need to write headers
            file_exists = output_file.exists()
            
            with open(output_file, 'a', encoding='utf-8', newline='') as f:
                fieldnames = [
                    'timestamp',
                    'execution_duration',
                    'overall_success',
                    'framework_mapping_compliance',
                    'version_history_compliance',
                    'test_pass_rate',
                    'bilingual_consistency_rate',
                    'total_frameworks',
                    'valid_frameworks',
                    'total_templates',
                    'valid_templates',
                    'total_tests',
                    'passed_tests',
                    'failed_tests'
                ]
                
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                
                # Write header if file is new
                if not file_exists:
                    writer.writeheader()
                
                # Write metrics row
                writer.writerow({
                    'timestamp': report.timestamp.isoformat(),
                    'execution_duration': report.execution_duration,
                    'overall_success': report.overall_success,
                    'framework_mapping_compliance': report.metrics.framework_mapping_compliance,
                    'version_history_compliance': report.metrics.version_history_compliance,
                    'test_pass_rate': report.metrics.test_pass_rate,
                    'bilingual_consistency_rate': report.metrics.bilingual_consistency_rate,
                    'total_frameworks': report.mapping_validation.total_frameworks,
                    'valid_frameworks': report.mapping_validation.valid_frameworks,
                    'total_templates': report.version_validation.total_templates,
                    'valid_templates': report.version_validation.valid_templates,
                    'total_tests': report.test_results.total_tests,
                    'passed_tests': report.test_results.passed,
                    'failed_tests': report.test_results.failed
                })
            
            self.logger.info(f"Metrics exported to CSV: {output_file}")
        except Exception as e:
            self.logger.error(f"Failed to export metrics to CSV: {e}")
            raise IOError(f"Failed to export metrics to CSV: {e}")
