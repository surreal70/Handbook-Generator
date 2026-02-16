# Design Document: Quality Control and Framework Documentation

## Overview

This design specifies a comprehensive quality control system for the Handbook Generator project. The system validates framework structure, ensures metadata consistency, executes test suites, and maintains framework coverage documentation.

The quality control system consists of four main components:
1. Framework Mapping Validator - ensures 9999_Framework_Mapping.md files exist
2. Version History Validator - verifies all templates contain version history
3. Test Suite Runner - executes pytest and analyzes failures
4. Coverage Documentation Generator - creates comprehensive framework documentation

The system is designed to be run as a standalone quality check or integrated into CI/CD pipelines.

## Architecture

### System Components

```
Quality Control System
├── Framework Mapping Validator
│   ├── Directory Scanner
│   ├── File Name Checker
│   └── Report Generator
├── Version History Validator
│   ├── Template Scanner
│   ├── Metadata Parser
│   └── Compliance Checker
├── Test Suite Runner
│   ├── Pytest Executor
│   ├── Output Parser
│   ├── Failure Analyzer
│   └── Task Generator
├── Coverage Documentation Generator
│   ├── Framework Discovery
│   ├── Template Counter
│   ├── Bilingual Consistency Checker
│   └── Markdown Report Generator
└── Quality Control Orchestrator
    ├── Execution Coordinator
    ├── Report Consolidator
    └── Metrics Tracker
```

### Component Interactions

1. User invokes Quality Control Orchestrator
2. Orchestrator executes validators in sequence
3. Each validator reports results to Orchestrator
4. Orchestrator consolidates results and generates final report
5. User reviews report and takes action on identified issues

## Components and Interfaces

### 1. Framework Mapping Validator

**Purpose**: Ensures all framework directories contain properly named mapping files (9999_Framework_Mapping.md)

**Interface**:
```python
class FrameworkMappingValidator:
    def scan_frameworks(self, base_path: str) -> List[FrameworkInfo]
    def validate_mapping_files(self, frameworks: List[FrameworkInfo]) -> ValidationResult
    def generate_report(self, result: ValidationResult) -> str
```

**Data Structures**:
```python
@dataclass
class FrameworkInfo:
    name: str
    language: str  # 'de' or 'en'
    path: Path
    has_mapping_file: bool
    mapping_file_name: Optional[str]

@dataclass
class ValidationResult:
    total_frameworks: int
    valid_frameworks: int
    invalid_frameworks: List[FrameworkInfo]
    missing_files: List[FrameworkInfo]
    success: bool
```

**Algorithm**:
1. Scan templates/de/ and templates/en/ directories
2. For each subdirectory, check for 9999_Framework_Mapping.md
3. Record frameworks with missing or incorrectly named files
4. Generate validation report with pass/fail status

### 2. Version History Validator

**Purpose**: Verifies all template files contain version history metadata

**Interface**:
```python
class VersionHistoryValidator:
    def scan_templates(self, framework_path: str) -> List[TemplateFile]
    def validate_version_history(self, templates: List[TemplateFile]) -> ValidationResult
    def generate_report(self, result: ValidationResult) -> str
```

**Data Structures**:
```python
@dataclass
class TemplateFile:
    path: Path
    framework: str
    language: str
    has_version_history: bool
    version_history_format_valid: bool
    version_entries: int

@dataclass
class VersionHistoryValidationResult:
    total_templates: int
    valid_templates: int
    missing_version_history: List[TemplateFile]
    invalid_format: List[TemplateFile]
    success: bool
```

**Algorithm**:
1. Scan all .md files in framework directories
2. Parse each file for "## Version History" or "## Versionshistorie" section
3. Validate section contains at least one version entry
4. Record templates with missing or invalid version history
5. Generate validation report

### 3. Test Suite Runner

**Purpose**: Executes pytest test suite and analyzes failures

**Interface**:
```python
class TestSuiteRunner:
    def execute_tests(self, test_path: str = "tests/") -> TestResult
    def parse_output(self, output: str) -> TestResult
    def analyze_failures(self, result: TestResult) -> List[FailedTest]
    def create_tasks(self, failures: List[FailedTest]) -> List[Task]
    def generate_report(self, result: TestResult) -> str
```

**Data Structures**:
```python
@dataclass
class TestResult:
    total_tests: int
    passed: int
    failed: int
    skipped: int
    duration: float
    failed_tests: List[FailedTest]
    success: bool

@dataclass
class FailedTest:
    name: str
    file_path: str
    line_number: int
    failure_reason: str
    error_traceback: str
    
@dataclass
class Task:
    test_name: str
    description: str
    error_details: str
    priority: str  # 'high', 'medium', 'low'
    suggested_fix: Optional[str]
```

**Algorithm**:
1. Execute "python -m pytest tests/ -v" command
2. Capture stdout and stderr
3. Parse pytest output to extract test results
4. For each failed test, extract name, file, line, and error
5. Create task entries for each failure
6. Generate summary report with statistics

### 4. Coverage Documentation Generator

**Purpose**: Creates comprehensive documentation of all supported frameworks

**Interface**:
```python
class CoverageDocumentationGenerator:
    def discover_frameworks(self, base_path: str) -> List[Framework]
    def count_templates(self, framework: Framework) -> TemplateCounts
    def check_bilingual_consistency(self, frameworks: List[Framework]) -> ConsistencyReport
    def generate_documentation(self, frameworks: List[Framework]) -> str
    def save_documentation(self, content: str, output_path: str) -> None
```

**Data Structures**:
```python
@dataclass
class Framework:
    name: str
    standard: str  # e.g., "ISO 27001:2022"
    description: str
    template_count_de: int
    template_count_en: int
    path_de: Path
    path_en: Path
    bilingual_consistent: bool

@dataclass
class TemplateCounts:
    total: int
    content_templates: int
    metadata_templates: int
    mapping_files: int

@dataclass
class ConsistencyReport:
    consistent_frameworks: List[Framework]
    inconsistent_frameworks: List[Framework]
    missing_translations: List[Tuple[Framework, str]]  # (framework, language)
```

**Algorithm**:
1. Scan templates/de/ and templates/en/ directories
2. For each framework, count template files
3. Extract framework metadata (standard, description) from README.md
4. Compare German and English template counts
5. Flag inconsistencies
6. Generate Markdown table with all framework information
7. Save to docs/FRAMEWORK_COVERAGE.md

### 5. Quality Control Orchestrator

**Purpose**: Coordinates execution of all validators and consolidates results

**Interface**:
```python
class QualityControlOrchestrator:
    def __init__(self):
        self.mapping_validator = FrameworkMappingValidator()
        self.version_validator = VersionHistoryValidator()
        self.test_runner = TestSuiteRunner()
        self.coverage_generator = CoverageDocumentationGenerator()
        
    def run_all_checks(self) -> QualityReport
    def run_specific_check(self, check_name: str) -> ValidationResult
    def generate_consolidated_report(self, results: Dict[str, ValidationResult]) -> str
    def track_metrics(self, report: QualityReport) -> None
```

**Data Structures**:
```python
@dataclass
class QualityReport:
    timestamp: datetime
    mapping_validation: ValidationResult
    version_validation: VersionHistoryValidationResult
    test_results: TestResult
    coverage_documentation: str
    overall_success: bool
    metrics: QualityMetrics
    
@dataclass
class QualityMetrics:
    framework_mapping_compliance: float  # percentage
    version_history_compliance: float  # percentage
    test_pass_rate: float  # percentage
    bilingual_consistency_rate: float  # percentage
```

**Algorithm**:
1. Execute Framework Mapping Validator
2. Execute Version History Validator
3. Execute Test Suite Runner
4. Execute Coverage Documentation Generator
5. Consolidate all results into QualityReport
6. Calculate quality metrics
7. Generate consolidated report
8. Save metrics to history file

## Data Models

### File System Structure

```
templates/
├── de/
│   ├── bcm/
│   │   ├── 9999_Framework_Mapping.md
│   │   ├── 0010_Template.md
│   │   └── ...
│   ├── isms/
│   └── ...
└── en/
    ├── bcm/
    └── ...

docs/
└── FRAMEWORK_COVERAGE.md  # Generated documentation

.quality/
├── metrics_history.json
└── last_run.json
```

### Metrics History Format

```json
{
  "runs": [
    {
      "timestamp": "2025-02-10T14:30:00Z",
      "framework_mapping_compliance": 95.5,
      "version_history_compliance": 88.2,
      "test_pass_rate": 99.3,
      "bilingual_consistency_rate": 100.0,
      "total_frameworks": 22,
      "total_templates": 1732,
      "total_tests": 765
    }
  ]
}
```

## Correctness Properties

*A property is a characteristic or behavior that should hold true across all valid executions of a system—essentially, a formal statement about what the system should do. Properties serve as the bridge between human-readable specifications and machine-verifiable correctness guarantees.*

### Property 1: Complete Framework Discovery

*For any* directory structure containing framework directories, the Quality_Control_System should discover all framework directories under both templates/de/ and templates/en/ without omission.

**Validates: Requirements 1.1, 2.1, 4.1**

### Property 2: Universal File Validation

*For any* framework directory, the Quality_Control_System should correctly identify whether the 9999_Framework_Mapping.md file exists and is correctly named.

**Validates: Requirements 1.2, 1.4**

### Property 3: Complete Error Reporting

*For any* set of validation errors (missing files, incorrect names, missing version history, invalid formats), the Quality_Control_System should report all errors without omission.

**Validates: Requirements 1.3, 1.4, 2.3, 2.5, 4.6**

### Property 4: Report Completeness

*For any* set of frameworks, templates, or test results, generated reports should include information about all items in the input set.

**Validates: Requirements 1.5, 2.6, 3.7, 4.7, 5.4**

### Property 5: Accurate Counting

*For any* directory containing template files, the count reported by the system should equal the actual number of files matching the criteria.

**Validates: Requirements 2.6, 3.7, 4.4, 4.9**

### Property 6: Version History Detection

*For any* template file, the Template_Validator should correctly identify whether it contains a "## Version History" or "## Versionshistorie" section.

**Validates: Requirements 2.2, 2.4**

### Property 7: Test Output Parsing Completeness

*For any* pytest output containing failed tests, the Test_Runner should identify and extract information for all failed tests without omission.

**Validates: Requirements 3.2, 3.3, 3.4**

### Property 8: Task Creation Mapping

*For any* set of failed tests, the Test_Runner should create exactly one task per failed test, maintaining a one-to-one correspondence.

**Validates: Requirements 3.5**

### Property 9: Framework Metadata Extraction

*For any* framework directory containing a README.md file, the Documentation_Generator should extract the framework name, standard, and description.

**Validates: Requirements 4.2, 4.3**

### Property 10: Bilingual Consistency Detection

*For any* pair of German and English framework directories, the Documentation_Generator should correctly identify whether template counts match.

**Validates: Requirements 4.5, 4.6**

### Property 11: Markdown Format Validity

*For any* set of frameworks, the generated coverage documentation should be valid Markdown with a properly formatted table containing all required columns.

**Validates: Requirements 4.8**

### Property 12: Sequential Execution

*For any* quality control run, all validation checks should execute in the specified order (Framework Mapping → Version History → Test Suite → Coverage Documentation) regardless of individual check failures.

**Validates: Requirements 5.1, 5.3**

### Property 13: Metrics Calculation Completeness

*For any* quality control run, all four quality metrics (framework mapping compliance, version history compliance, test pass rate, bilingual consistency rate) should be calculated and included in the report.

**Validates: Requirements 8.1**

### Property 14: Metrics Persistence

*For any* calculated quality metrics, the system should persist them to the metrics history file with a timestamp.

**Validates: Requirements 8.2**

### Property 15: Trend Detection

*For any* two consecutive quality control runs, the system should correctly identify whether each metric has improved, declined, or remained stable.

**Validates: Requirements 8.3, 8.4, 8.5**

### Property 16: Metrics Export Format

*For any* quality metrics, the system should be able to export them in both JSON and CSV formats with all required fields present.

**Validates: Requirements 8.7**

## Error Handling

### Error Categories

1. **File System Errors**
   - Directory not found
   - Permission denied
   - File read/write failures

2. **Validation Errors**
   - Missing framework mapping files
   - Missing version history
   - Invalid metadata format

3. **Test Execution Errors**
   - Pytest not installed
   - Test execution timeout
   - Invalid test output format

4. **Data Processing Errors**
   - Invalid Markdown parsing
   - Malformed JSON/CSV
   - Arithmetic overflow in metrics

### Error Handling Strategy

**Graceful Degradation**:
- Continue execution when individual checks fail
- Collect all errors and report at the end
- Provide partial results when possible

**Error Reporting**:
- Clear error messages with context
- File paths and line numbers for validation errors
- Suggested remediation steps

**Logging**:
- All errors logged to quality_control.log
- Different log levels: ERROR, WARNING, INFO, DEBUG
- Structured logging for machine parsing

### Error Recovery

```python
def run_validation_check(check_name: str, check_func: Callable) -> ValidationResult:
    try:
        result = check_func()
        return result
    except FileNotFoundError as e:
        logger.error(f"{check_name} failed: Directory not found - {e}")
        return ValidationResult(success=False, error=str(e))
    except PermissionError as e:
        logger.error(f"{check_name} failed: Permission denied - {e}")
        return ValidationResult(success=False, error=str(e))
    except Exception as e:
        logger.error(f"{check_name} failed: Unexpected error - {e}")
        return ValidationResult(success=False, error=str(e))
```

## Testing Strategy

### Dual Testing Approach

The quality control system will be validated using both unit tests and property-based tests:

**Unit Tests**: Focus on specific examples, edge cases, and error conditions
- Test with known directory structures
- Test with specific malformed files
- Test error handling paths
- Test report generation with fixed inputs

**Property Tests**: Verify universal properties across all inputs
- Generate random directory structures
- Generate random template files with/without version history
- Generate random test outputs
- Verify properties hold for all generated inputs

### Property-Based Testing Configuration

- Use Hypothesis library for Python property-based testing
- Minimum 100 iterations per property test
- Each property test references its design document property
- Tag format: **Feature: quality-control-and-framework-documentation, Property {number}: {property_text}**

### Test Organization

```
tests/
├── test_framework_mapping_validator.py
│   ├── Unit tests for specific cases
│   └── Property tests for universal behaviors
├── test_version_history_validator.py
│   ├── Unit tests for parsing edge cases
│   └── Property tests for detection completeness
├── test_test_suite_runner.py
│   ├── Unit tests for pytest output parsing
│   └── Property tests for failure extraction
├── test_coverage_documentation_generator.py
│   ├── Unit tests for markdown generation
│   └── Property tests for counting accuracy
└── test_quality_control_orchestrator.py
    ├── Unit tests for integration
    └── Property tests for execution order
```

### Example Property Test

```python
from hypothesis import given, strategies as st
import pytest

@given(st.lists(st.text(min_size=1, max_size=50), min_size=0, max_size=100))
def test_framework_discovery_completeness(framework_names):
    """
    Feature: quality-control-and-framework-documentation
    Property 1: Complete Framework Discovery
    
    For any directory structure containing framework directories,
    the system should discover all frameworks without omission.
    """
    # Setup: Create temporary directory structure
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create framework directories
        for name in framework_names:
            os.makedirs(os.path.join(tmpdir, "templates", "de", name))
            os.makedirs(os.path.join(tmpdir, "templates", "en", name))
        
        # Execute: Scan frameworks
        validator = FrameworkMappingValidator()
        discovered = validator.scan_frameworks(tmpdir)
        
        # Verify: All frameworks discovered
        discovered_names = {f.name for f in discovered}
        expected_names = set(framework_names)
        assert discovered_names == expected_names
```

### Unit Test Balance

- Focus unit tests on specific examples and edge cases
- Use property tests for comprehensive input coverage
- Unit tests should cover:
  - Empty directories
  - Single framework
  - Missing README files
  - Malformed version history sections
  - Invalid pytest output
  - File permission errors

### Test Coverage Goals

- Minimum 80% code coverage
- 100% coverage of error handling paths
- All correctness properties implemented as property tests
- All edge cases covered by unit tests

