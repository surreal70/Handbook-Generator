"""
Core data structures for the Quality Control System.

This module defines all data classes used throughout the quality control system
for representing frameworks, validation results, test results, and quality metrics.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Dict


@dataclass
class FrameworkInfo:
    """Information about a framework directory."""
    name: str
    language: str  # 'de' or 'en'
    path: Path
    has_mapping_file: bool
    mapping_file_name: Optional[str] = None


@dataclass
class ValidationResult:
    """Result of framework mapping validation."""
    total_frameworks: int
    valid_frameworks: int
    invalid_frameworks: List[FrameworkInfo]
    missing_files: List[FrameworkInfo]
    success: bool
    error: Optional[str] = None


@dataclass
class TemplateFile:
    """Information about a template file."""
    path: Path
    framework: str
    language: str
    has_version_history: bool
    version_history_format_valid: bool
    version_entries: int


@dataclass
class VersionHistoryValidationResult:
    """Result of version history validation."""
    total_templates: int
    valid_templates: int
    missing_version_history: List[TemplateFile]
    invalid_format: List[TemplateFile]
    success: bool
    error: Optional[str] = None


@dataclass
class FailedTest:
    """Information about a failed test."""
    name: str
    file_path: str
    line_number: int
    failure_reason: str
    error_traceback: str


@dataclass
class TestResult:
    """Result of test suite execution."""
    total_tests: int
    passed: int
    failed: int
    skipped: int
    duration: float
    failed_tests: List[FailedTest]
    success: bool
    error: Optional[str] = None


@dataclass
class Task:
    """Task for fixing a failed test."""
    test_name: str
    description: str
    error_details: str
    priority: str  # 'high', 'medium', 'low'
    suggested_fix: Optional[str] = None


@dataclass
class TemplateCounts:
    """Template counts for a framework."""
    total: int
    content_templates: int
    metadata_templates: int
    mapping_files: int


@dataclass
class Framework:
    """Information about a compliance framework."""
    name: str
    standard: str  # e.g., "ISO 27001:2022"
    description: str
    template_count_de: int
    template_count_en: int
    path_de: Path
    path_en: Path
    bilingual_consistent: bool


@dataclass
class ConsistencyReport:
    """Report on bilingual consistency."""
    consistent_frameworks: List[Framework]
    inconsistent_frameworks: List[Framework]
    missing_translations: List[tuple]  # (framework, language)


@dataclass
class QualityMetrics:
    """Quality metrics for a quality control run."""
    framework_mapping_compliance: float  # percentage
    version_history_compliance: float  # percentage
    test_pass_rate: float  # percentage
    bilingual_consistency_rate: float  # percentage


@dataclass
class QualityReport:
    """Consolidated quality control report."""
    timestamp: datetime
    mapping_validation: ValidationResult
    version_validation: VersionHistoryValidationResult
    test_results: TestResult
    coverage_documentation: str
    overall_success: bool
    metrics: QualityMetrics
    execution_duration: float = 0.0
