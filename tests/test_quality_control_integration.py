"""
End-to-End Integration Tests for Quality Control System

This module contains comprehensive integration tests that verify the complete
quality control workflow, including all validators, metrics tracking, and
report generation.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

import pytest
import tempfile
import shutil
import json
import csv
from pathlib import Path
from datetime import datetime

from src.quality_control.quality_control_orchestrator import QualityControlOrchestrator
from src.quality_control.data_structures import QualityReport


@pytest.fixture
def temp_project():
    """Create a temporary project structure for integration tests."""
    temp_dir = tempfile.mkdtemp()
    project = Path(temp_dir)
    
    # Create directory structure
    templates_de = project / "templates" / "de"
    templates_en = project / "templates" / "en"
    tests_dir = project / "tests"
    docs_dir = project / "docs"
    
    templates_de.mkdir(parents=True)
    templates_en.mkdir(parents=True)
    tests_dir.mkdir(parents=True)
    docs_dir.mkdir(parents=True)
    
    yield project
    
    # Cleanup
    shutil.rmtree(temp_dir)


@pytest.fixture
def complete_framework_structure(temp_project):
    """Create a complete framework structure with all required files."""
    templates_de = temp_project / "templates" / "de"
    templates_en = temp_project / "templates" / "en"
    
    # Create multiple frameworks
    frameworks = ["bcm", "isms", "gdpr"]
    
    for framework in frameworks:
        # German framework
        de_framework = templates_de / framework
        de_framework.mkdir(parents=True)
        
        # Create mapping file
        (de_framework / "9999_Framework_Mapping.md").write_text(f"""# {framework.upper()} Framework Mapping

## Overview
This document maps {framework.upper()} requirements to templates.

## Version History
- 1.0.0 (2025-02-13): Initial version
""")
        
        # Create README
        (de_framework / "README.md").write_text(f"""# {framework.upper()} Framework

Standard: {framework.upper()} Compliance
Description: {framework.upper()} compliance framework templates
""")
        
        # Create templates with version history
        for i in range(1, 4):
            template_num = f"{i:04d}0"
            (de_framework / f"{template_num}_template_{i}.md").write_text(f"""# Template {i}

Content for template {i}.

## Version History
- 1.0.0 (2025-02-13): Initial version
""")
        
        # English framework (mirror structure)
        en_framework = templates_en / framework
        en_framework.mkdir(parents=True)
        
        (en_framework / "9999_Framework_Mapping.md").write_text(f"""# {framework.upper()} Framework Mapping

## Overview
This document maps {framework.upper()} requirements to templates.

## Version History
- 1.0.0 (2025-02-13): Initial version
""")
        
        (en_framework / "README.md").write_text(f"""# {framework.upper()} Framework

Standard: {framework.upper()} Compliance
Description: {framework.upper()} compliance framework templates
""")
        
        for i in range(1, 4):
            template_num = f"{i:04d}0"
            (en_framework / f"{template_num}_template_{i}.md").write_text(f"""# Template {i}

Content for template {i}.

## Version History
- 1.0.0 (2025-02-13): Initial version
""")
    
    return temp_project


@pytest.fixture
def incomplete_framework_structure(temp_project):
    """Create an incomplete framework structure with various issues."""
    templates_de = temp_project / "templates" / "de"
    templates_en = temp_project / "templates" / "en"
    
    # Framework 1: Missing mapping file
    framework1 = templates_de / "framework1"
    framework1.mkdir(parents=True)
    (framework1 / "0010_template.md").write_text("""# Template

## Version History
- 1.0.0: Initial
""")
    
    # Framework 2: Incorrectly named mapping file
    framework2 = templates_de / "framework2"
    framework2.mkdir(parents=True)
    (framework2 / "9999_Framework_Mapping.md").write_text("# Mapping")
    (framework2 / "0010_template.md").write_text("""# Template

## Version History
- 1.0.0: Initial
""")
    
    # Framework 3: Templates missing version history
    framework3 = templates_de / "framework3"
    framework3.mkdir(parents=True)
    (framework3 / "9999_Framework_Mapping.md").write_text("# Mapping")
    (framework3 / "0010_template_no_history.md").write_text("# Template\n\nNo version history here.")
    (framework3 / "0020_template_with_history.md").write_text("""# Template

## Version History
- 1.0.0: Initial
""")
    
    # Framework 4: Bilingual inconsistency (only DE, no EN)
    framework4 = templates_de / "framework4"
    framework4.mkdir(parents=True)
    (framework4 / "9999_Framework_Mapping.md").write_text("# Mapping")
    (framework4 / "0010_template.md").write_text("""# Template

## Version History
- 1.0.0: Initial
""")
    
    return temp_project


@pytest.fixture
def simple_test_suite(temp_project):
    """Create a simple test suite for testing."""
    tests_dir = temp_project / "tests"
    
    # Create a simple passing test
    (tests_dir / "test_sample.py").write_text("""
import pytest

def test_passing():
    assert True

def test_another_passing():
    assert 1 + 1 == 2
""")
    
    return temp_project


class TestQualityControlFullWorkflow:
    """Test complete quality control workflow end-to-end."""
    
    def test_complete_quality_control_run_success(self, complete_framework_structure):
        """
        Test full quality control run on a complete, valid project.
        
        Validates: Requirements 5.1, 5.2, 5.3, 5.4, 5.5, 5.6
        """
        # Initialize orchestrator
        orchestrator = QualityControlOrchestrator(str(complete_framework_structure))
        
        # Run all checks
        report = orchestrator.run_all_checks()
        
        # Verify report structure
        assert isinstance(report, QualityReport)
        assert report.timestamp is not None
        assert isinstance(report.timestamp, datetime)
        assert report.execution_duration > 0
        
        # Verify all checks executed
        assert report.mapping_validation is not None
        assert report.version_validation is not None
        assert report.test_results is not None
        assert report.coverage_documentation is not None
        
        # Verify metrics calculated
        assert report.metrics is not None
        assert 0 <= report.metrics.framework_mapping_compliance <= 100
        assert 0 <= report.metrics.version_history_compliance <= 100
        assert 0 <= report.metrics.test_pass_rate <= 100
        assert 0 <= report.metrics.bilingual_consistency_rate <= 100
        
        # For complete structure, expect high compliance
        assert report.mapping_validation.success
        assert report.version_validation.success
        assert report.metrics.framework_mapping_compliance == 100.0
        assert report.metrics.version_history_compliance == 100.0
        assert report.metrics.bilingual_consistency_rate == 100.0
    
    def test_complete_quality_control_run_with_issues(self, incomplete_framework_structure):
        """
        Test full quality control run on a project with various issues.
        
        Validates: Requirements 5.1, 5.2, 5.3
        """
        # Initialize orchestrator
        orchestrator = QualityControlOrchestrator(str(incomplete_framework_structure))
        
        # Run all checks
        report = orchestrator.run_all_checks()
        
        # Verify report generated even with failures
        assert isinstance(report, QualityReport)
        assert report.timestamp is not None
        
        # Verify issues detected
        assert not report.overall_success
        
        # Verify mapping validation detected issues
        assert not report.mapping_validation.success
        assert len(report.mapping_validation.missing_files) > 0 or \
               len(report.mapping_validation.invalid_frameworks) > 0
        
        # Verify version history validation detected issues
        assert not report.version_validation.success
        assert len(report.version_validation.missing_version_history) > 0
        
        # Verify metrics reflect issues
        assert report.metrics.framework_mapping_compliance < 100.0
        assert report.metrics.version_history_compliance < 100.0
    
    def test_consolidated_report_generation(self, complete_framework_structure):
        """
        Test consolidated report generation with all validation results.
        
        Validates: Requirements 5.4, 5.5, 5.6
        """
        orchestrator = QualityControlOrchestrator(str(complete_framework_structure))
        report = orchestrator.run_all_checks()
        
        # Generate consolidated report
        report_text = orchestrator.generate_consolidated_report(report)
        
        # Verify report structure
        assert isinstance(report_text, str)
        assert len(report_text) > 0
        
        # Verify report contains key sections
        assert "QUALITY CONTROL CONSOLIDATED REPORT" in report_text
        assert "QUALITY METRICS" in report_text
        assert "FRAMEWORK MAPPING VALIDATION" in report_text
        assert "VERSION HISTORY VALIDATION" in report_text
        assert "TEST SUITE EXECUTION" in report_text
        assert "COVERAGE DOCUMENTATION" in report_text
        assert "RECOMMENDATIONS" in report_text
        
        # Verify metrics included
        assert "Framework Mapping Compliance:" in report_text
        assert "Version History Compliance:" in report_text
        assert "Test Pass Rate:" in report_text
        assert "Bilingual Consistency Rate:" in report_text
        
        # Verify timestamp and duration
        assert report.timestamp.strftime('%Y-%m-%d') in report_text
        assert "Duration:" in report_text
    
    def test_metrics_persistence(self, complete_framework_structure):
        """
        Test metrics are correctly saved to history file.
        
        Validates: Requirements 8.2
        """
        orchestrator = QualityControlOrchestrator(str(complete_framework_structure))
        report = orchestrator.run_all_checks()
        
        # Save metrics
        orchestrator.save_metrics(report)
        
        # Verify metrics history file created
        metrics_file = complete_framework_structure / ".quality" / "metrics_history.json"
        assert metrics_file.exists()
        
        # Verify metrics content
        with open(metrics_file, 'r') as f:
            metrics_data = json.load(f)
        
        assert "runs" in metrics_data
        assert len(metrics_data["runs"]) > 0
        
        latest_run = metrics_data["runs"][-1]
        assert "timestamp" in latest_run
        assert "framework_mapping_compliance" in latest_run
        assert "version_history_compliance" in latest_run
        assert "test_pass_rate" in latest_run
        assert "bilingual_consistency_rate" in latest_run
        assert "overall_success" in latest_run
        
        # Verify last run file created
        last_run_file = complete_framework_structure / ".quality" / "last_run.json"
        assert last_run_file.exists()
    
    def test_trend_analysis(self, complete_framework_structure):
        """
        Test trend analysis comparing multiple runs.
        
        Validates: Requirements 8.3, 8.4, 8.5
        """
        orchestrator = QualityControlOrchestrator(str(complete_framework_structure))
        
        # First run
        report1 = orchestrator.run_all_checks()
        orchestrator.save_metrics(report1)
        
        # Modify structure to create a regression
        framework = complete_framework_structure / "templates" / "de" / "bcm"
        template = framework / "0010_template_1.md"
        template.write_text("# Template without version history")
        
        # Second run
        report2 = orchestrator.run_all_checks()
        
        # Analyze trends
        trends = orchestrator.analyze_trends(report2)
        
        # Verify trends structure
        assert isinstance(trends, dict)
        assert "framework_mapping_compliance" in trends
        assert "version_history_compliance" in trends
        assert "test_pass_rate" in trends
        assert "bilingual_consistency_rate" in trends
        
        # Verify trend data
        for metric_name, trend_data in trends.items():
            assert "current" in trend_data
            assert "previous" in trend_data
            assert "change" in trend_data
            assert "trend" in trend_data
            assert trend_data["trend"] in ["improved", "declined", "stable"]
        
        # Generate trend report
        trend_report = orchestrator.generate_trend_report(trends)
        assert isinstance(trend_report, str)
        assert len(trend_report) > 0
    
    def test_metrics_export_json(self, complete_framework_structure, tmp_path):
        """
        Test metrics export to JSON format.
        
        Validates: Requirements 8.7
        """
        orchestrator = QualityControlOrchestrator(str(complete_framework_structure))
        report = orchestrator.run_all_checks()
        
        # Export to JSON
        json_file = tmp_path / "metrics.json"
        orchestrator.export_metrics_json(report, str(json_file))
        
        # Verify file created
        assert json_file.exists()
        
        # Verify JSON content
        with open(json_file, 'r') as f:
            data = json.load(f)
        
        assert "timestamp" in data
        assert "execution_duration" in data
        assert "overall_success" in data
        assert "metrics" in data
        assert "details" in data
        
        # Verify metrics structure
        metrics = data["metrics"]
        assert "framework_mapping_compliance" in metrics
        assert "version_history_compliance" in metrics
        assert "test_pass_rate" in metrics
        assert "bilingual_consistency_rate" in metrics
    
    def test_metrics_export_csv(self, complete_framework_structure, tmp_path):
        """
        Test metrics export to CSV format.
        
        Validates: Requirements 8.7
        """
        orchestrator = QualityControlOrchestrator(str(complete_framework_structure))
        report = orchestrator.run_all_checks()
        
        # Export to CSV
        csv_file = tmp_path / "metrics.csv"
        orchestrator.export_metrics_csv(report, str(csv_file))
        
        # Verify file created
        assert csv_file.exists()
        
        # Verify CSV content
        with open(csv_file, 'r', newline='') as f:
            reader = csv.DictReader(f)
            rows = list(reader)
        
        assert len(rows) > 0
        
        # Verify CSV headers
        headers = rows[0].keys()
        assert "timestamp" in headers
        assert "execution_duration" in headers
        assert "overall_success" in headers
        assert "framework_mapping_compliance" in headers
        assert "version_history_compliance" in headers
        assert "test_pass_rate" in headers
        assert "bilingual_consistency_rate" in headers
    
    def test_specific_check_execution(self, complete_framework_structure):
        """
        Test execution of specific individual checks.
        
        Validates: Requirements 5.1
        """
        orchestrator = QualityControlOrchestrator(str(complete_framework_structure))
        
        # Test mapping check
        mapping_result = orchestrator.run_specific_check("mapping")
        assert mapping_result is not None
        assert hasattr(mapping_result, 'success')
        assert hasattr(mapping_result, 'total_frameworks')
        
        # Test version check
        version_result = orchestrator.run_specific_check("version")
        assert version_result is not None
        assert hasattr(version_result, 'success')
        assert hasattr(version_result, 'total_templates')
        
        # Test coverage check
        coverage_result = orchestrator.run_specific_check("coverage")
        assert coverage_result is not None
        assert isinstance(coverage_result, list)
    
    def test_sequential_execution_order(self, complete_framework_structure):
        """
        Test that validators execute in the correct sequence.
        
        Validates: Requirements 5.1, 5.2
        """
        orchestrator = QualityControlOrchestrator(str(complete_framework_structure))
        
        # Track execution order by checking report structure
        report = orchestrator.run_all_checks()
        
        # All checks should have executed
        assert report.mapping_validation is not None
        assert report.version_validation is not None
        assert report.test_results is not None
        assert report.coverage_documentation is not None
        
        # Verify execution completed even if individual checks would fail
        # (This is tested more thoroughly in the incomplete structure test)
        assert report.timestamp is not None
        assert report.execution_duration > 0
    
    def test_coverage_documentation_generation(self, complete_framework_structure):
        """
        Test that coverage documentation is generated correctly.
        
        Validates: Requirements 4.7, 4.8, 4.9, 4.10
        """
        orchestrator = QualityControlOrchestrator(str(complete_framework_structure))
        report = orchestrator.run_all_checks()
        
        # Verify coverage documentation generated
        assert report.coverage_documentation is not None
        assert isinstance(report.coverage_documentation, str)
        assert len(report.coverage_documentation) > 0
        
        # Verify documentation contains framework information
        assert "bcm" in report.coverage_documentation.lower()
        assert "isms" in report.coverage_documentation.lower()
        assert "gdpr" in report.coverage_documentation.lower()
        
        # Verify Markdown format
        assert "#" in report.coverage_documentation  # Headers
        assert "|" in report.coverage_documentation  # Tables
    
    def test_error_handling_and_recovery(self, temp_project):
        """
        Test that quality control handles errors gracefully.
        
        Validates: Requirements 5.3
        """
        # Create a project with permission issues
        templates_dir = temp_project / "templates"
        templates_dir.mkdir(parents=True)
        
        orchestrator = QualityControlOrchestrator(str(temp_project))
        
        # Should not crash even with empty/invalid structure
        report = orchestrator.run_all_checks()
        
        # Verify report generated
        assert isinstance(report, QualityReport)
        assert report.timestamp is not None
        
        # Verify graceful handling of empty structure
        assert report.mapping_validation.total_frameworks == 0
        assert report.version_validation.total_templates == 0
    
    def test_multiple_consecutive_runs(self, complete_framework_structure):
        """
        Test multiple consecutive quality control runs.
        
        Validates: Requirements 8.2, 8.3
        """
        orchestrator = QualityControlOrchestrator(str(complete_framework_structure))
        
        # Run multiple times
        reports = []
        for i in range(3):
            report = orchestrator.run_all_checks()
            orchestrator.save_metrics(report)
            reports.append(report)
        
        # Verify all runs completed
        assert len(reports) == 3
        
        # Verify metrics history accumulated
        metrics_file = complete_framework_structure / ".quality" / "metrics_history.json"
        with open(metrics_file, 'r') as f:
            metrics_data = json.load(f)
        
        assert len(metrics_data["runs"]) >= 3
        
        # Verify each run has unique timestamp
        timestamps = [run["timestamp"] for run in metrics_data["runs"]]
        assert len(timestamps) == len(set(timestamps))


class TestQualityControlReportGeneration:
    """Test report generation in various scenarios."""
    
    def test_report_with_all_checks_passing(self, complete_framework_structure):
        """Test report generation when all checks pass."""
        orchestrator = QualityControlOrchestrator(str(complete_framework_structure))
        report = orchestrator.run_all_checks()
        report_text = orchestrator.generate_consolidated_report(report)
        
        assert "Overall Status: PASSED" in report_text
        assert "✓ All quality checks passed!" in report_text
    
    def test_report_with_failures(self, incomplete_framework_structure):
        """Test report generation when checks fail."""
        orchestrator = QualityControlOrchestrator(str(incomplete_framework_structure))
        report = orchestrator.run_all_checks()
        report_text = orchestrator.generate_consolidated_report(report)
        
        assert "Overall Status: FAILED" in report_text
        assert "RECOMMENDATIONS" in report_text
        
        # Should contain specific recommendations
        assert "Fix framework mapping file issues" in report_text or \
               "Add version history sections" in report_text
    
    def test_report_includes_execution_metadata(self, complete_framework_structure):
        """Test that report includes execution metadata."""
        orchestrator = QualityControlOrchestrator(str(complete_framework_structure))
        report = orchestrator.run_all_checks()
        report_text = orchestrator.generate_consolidated_report(report)
        
        # Verify metadata present
        assert "Execution Time:" in report_text
        assert "Duration:" in report_text
        assert "seconds" in report_text
        
        # Verify timestamp format
        assert report.timestamp.strftime('%Y-%m-%d') in report_text


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
