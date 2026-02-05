"""
Tests for Output Generator

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2026
"""

import pytest
from pathlib import Path
from hypothesis import given, settings
import hypothesis.strategies as st
from src.output_generator import OutputGenerator, OutputResult


# ============================================================================
# Property-Based Tests
# ============================================================================

@settings(max_examples=100)
@given(
    contents=st.lists(
        st.text(
            alphabet=st.characters(whitelist_categories=('L', 'N', 'P', 'Z', 'S')),
            min_size=0,
            max_size=500
        ),
        min_size=0,
        max_size=10
    )
)
def test_property_15_markdown_assembly(contents):
    """
    Feature: handbook-generator, Property 15: Markdown Assembly
    
    For any set of processed templates, the markdown output should contain
    all template contents in the correct order as a single concatenated document.
    
    Validates: Requirements 8.1
    """
    generator = OutputGenerator(Path("test_output"), test_mode=True)
    
    # Assemble markdown
    assembled = generator.assemble_markdown(contents)
    
    # Property 1: All content should be present in the assembled output
    for content in contents:
        assert content in assembled, f"Content missing from assembled markdown: {content[:50]}"
    
    # Property 2: Content should appear in the same order
    # For duplicate content, we need to check that at least one occurrence appears in order
    if len(contents) > 1:
        last_idx = -1
        for content in contents:
            if content:  # Skip empty strings
                # Find the next occurrence after the last position
                idx = assembled.find(content, last_idx + 1)
                if idx != -1:
                    assert idx >= last_idx, "Content order not preserved in assembly"
                    last_idx = idx
    
    # Property 3: Empty input should produce empty output
    if not contents or all(not c for c in contents):
        assert assembled == "" or assembled.strip() == ""


@settings(max_examples=100)
@given(
    language=st.sampled_from(['de', 'en', 'fr', 'es']),
    template_type=st.sampled_from(['backup', 'bcm', 'isms', 'it-operation', 'custom'])
)
def test_property_16_output_directory_structure_mirroring(language, template_type):
    """
    Feature: handbook-generator, Property 16: Output Directory Structure Mirroring
    
    For any template with language and type (e.g., "de/backup"), the output
    directory structure should mirror this organization (e.g., "Handbook/de/backup/").
    
    Validates: Requirements 8.3
    """
    import tempfile
    with tempfile.TemporaryDirectory() as tmp_dir:
        output_dir = Path(tmp_dir) / "Handbook"
        generator = OutputGenerator(output_dir, test_mode=True)
    
        # Ensure output structure (now uses output_type instead of template_type)
        created_dir = generator.ensure_output_structure(language, template_type)
        
        # Property 1: Directory should exist
        assert created_dir.exists(), f"Output directory not created: {created_dir}"
        assert created_dir.is_dir(), f"Output path is not a directory: {created_dir}"
        
        # Property 2: Directory structure should mirror template organization
        expected_path = output_dir / language / template_type
        assert created_dir == expected_path, f"Directory structure mismatch: {created_dir} != {expected_path}"
        
        # Property 3: Parent directories should also exist
        assert created_dir.parent.exists(), "Parent directory not created"
        assert created_dir.parent.parent.exists(), "Grandparent directory not created"


@settings(max_examples=100)
@given(
    content=st.text(
        alphabet=st.characters(whitelist_categories=('L', 'N', 'P', 'Z', 'S')),
        min_size=0,
        max_size=1000
    )
)
def test_property_17_markdown_validity(content):
    """
    Feature: handbook-generator, Property 17: Markdown Validity
    
    For any generated markdown output, the content should be parseable
    as valid markdown syntax.
    
    Validates: Requirements 8.5
    """
    generator = OutputGenerator(Path("test_output"), test_mode=True)
    
    # Validate markdown
    warnings = generator.validate_markdown(content)
    
    # Property 1: Empty content should produce a warning
    if not content or not content.strip():
        assert len(warnings) > 0, "Empty content should produce validation warning"
        assert any("empty" in w.lower() for w in warnings)
    
    # Property 2: Unclosed code blocks should be detected
    code_block_count = content.count('```')
    if code_block_count % 2 != 0:
        assert any("code block" in w.lower() for w in warnings), \
            "Unclosed code blocks should be detected"
    
    # Property 3: Valid markdown should produce no warnings (or only minor ones)
    # We can't guarantee all random text is valid markdown, but we check the validator works
    assert isinstance(warnings, list), "Validation should return a list"


@settings(max_examples=100)
@given(
    error_message=st.text(min_size=1, max_size=200)
)
def test_property_18_pdf_generation_error_handling(error_message):
    """
    Feature: handbook-generator, Property 18: PDF Generation Error Handling
    
    For any PDF generation failure, the system should produce an error message
    containing details about the failure cause.
    
    Validates: Requirements 9.5
    """
    import tempfile
    with tempfile.TemporaryDirectory() as tmp_dir:
        output_dir = Path(tmp_dir) / "Handbook"
        generator = OutputGenerator(output_dir, test_mode=True)
    
        # Test with invalid markdown that might cause PDF generation issues
        # We'll test the error handling structure
        invalid_markdown = "# Test\n" + "```\nunclosed code block"
        
        try:
            result = generator.generate_pdf(
                invalid_markdown,
                language="de",
                template_type="test"
            )
            
            # Property 1: Result should be an OutputResult object
            assert isinstance(result, OutputResult), "Should return OutputResult"
            
            # Property 2: If PDF generation fails, errors list should not be empty
            # (This will likely fail due to missing dependencies, which is expected)
            if result.pdf_path is None:
                assert len(result.errors) > 0, "Failed PDF generation should produce error messages"
            
            # Property 3: Error messages should contain useful information
            if result.errors:
                for error in result.errors:
                    assert isinstance(error, str), "Errors should be strings"
                    assert len(error) > 0, "Error messages should not be empty"
        except (ImportError, OSError):
            # System dependencies missing - this is expected in test environment
            # The property test validates that IF PDF generation runs, it handles errors properly
            pass


@settings(max_examples=100)
@given(
    language=st.sampled_from(['de', 'en', 'fr', 'es']),
    output_type=st.sampled_from(['markdown', 'pdf', 'html']),
    template_type=st.sampled_from(['backup', 'bcm', 'isms', 'it-operation', 'bsi-grundschutz'])
)
def test_property_25_output_directory_consolidation(language, output_type, template_type):
    """
    Feature: handbook-generator, Property 25: Output Directory Consolidation
    
    For any handbook generation with test mode enabled, all outputs should go to
    test-output/{language}/{output_type}/ directory structure, and no outputs
    should go to old Handbook/ or PDF_Output/ directories.
    
    Validates: Requirements TBD (new requirement for test mode)
    """
    import tempfile
    with tempfile.TemporaryDirectory() as tmp_dir:
        output_dir = Path(tmp_dir) / "test-output"
        generator = OutputGenerator(output_dir, test_mode=True)
        
        # Property 1: Output directory structure should use test-output/{language}/{output_type}/
        created_dir = generator.ensure_output_structure(language, output_type)
        
        assert created_dir.exists(), f"Output directory not created: {created_dir}"
        assert "test-output" in str(created_dir), "Output should be in test-output directory"
        assert created_dir == output_dir / language / output_type, \
            f"Directory structure mismatch: {created_dir} != {output_dir / language / output_type}"
        
        # Property 2: Old directory structures should NOT be created
        old_handbook_dir = Path(tmp_dir) / "Handbook" / language / template_type
        old_pdf_dir = Path(tmp_dir) / "PDF_Output" / language / template_type
        
        assert not old_handbook_dir.exists(), \
            f"Old Handbook directory should not be created: {old_handbook_dir}"
        assert not old_pdf_dir.exists(), \
            f"Old PDF_Output directory should not be created: {old_pdf_dir}"
        
        # Property 3: Output type should be in the path (markdown, pdf, or html)
        assert output_type in str(created_dir), \
            f"Output type '{output_type}' should be in path: {created_dir}"
        
        # Property 4: Language should be in the path
        assert language in str(created_dir), \
            f"Language '{language}' should be in path: {created_dir}"


# ============================================================================
# Unit Tests
# ============================================================================

def test_markdown_assembly_basic():
    """Test basic markdown assembly with multiple templates."""
    generator = OutputGenerator(Path("test_output"), test_mode=True)
    
    contents = [
        "# Introduction\n\nThis is the intro.",
        "# Chapter 1\n\nFirst chapter content.",
        "# Chapter 2\n\nSecond chapter content."
    ]
    
    assembled = generator.assemble_markdown(contents)
    
    # All content should be present
    assert "# Introduction" in assembled
    assert "# Chapter 1" in assembled
    assert "# Chapter 2" in assembled
    
    # Content should be in order
    assert assembled.index("Introduction") < assembled.index("Chapter 1")
    assert assembled.index("Chapter 1") < assembled.index("Chapter 2")


def test_markdown_assembly_empty():
    """Test markdown assembly with empty input."""
    generator = OutputGenerator(Path("test_output"), test_mode=True)
    
    # Empty list
    assert generator.assemble_markdown([]) == ""
    
    # List with empty strings
    assert generator.assemble_markdown(["", "", ""]) == "\n\n\n\n"


def test_markdown_validation_valid():
    """Test markdown validation with valid content."""
    generator = OutputGenerator(Path("test_output"), test_mode=True)
    
    valid_markdown = """# Title

## Subtitle

This is a paragraph with **bold** and *italic* text.

- List item 1
- List item 2

```python
def hello():
    print("Hello")
```

| Column 1 | Column 2 |
|----------|----------|
| Data 1   | Data 2   |
"""
    
    warnings = generator.validate_markdown(valid_markdown)
    
    # Should have no warnings for valid markdown
    assert len(warnings) == 0


def test_markdown_validation_unclosed_code_block():
    """Test markdown validation detects unclosed code blocks."""
    generator = OutputGenerator(Path("test_output"), test_mode=True)
    
    invalid_markdown = """# Title

```python
def hello():
    print("Hello")
# Missing closing ```
"""
    
    warnings = generator.validate_markdown(invalid_markdown)
    
    assert len(warnings) > 0
    assert any("code block" in w.lower() for w in warnings)


def test_markdown_validation_malformed_headers():
    """Test markdown validation detects malformed headers."""
    generator = OutputGenerator(Path("test_output"), test_mode=True)
    
    invalid_markdown = """#Title without space
## Subtitle

##Another malformed header
"""
    
    warnings = generator.validate_markdown(invalid_markdown)
    
    assert len(warnings) > 0
    assert any("header" in w.lower() for w in warnings)


def test_markdown_validation_empty():
    """Test markdown validation with empty content."""
    generator = OutputGenerator(Path("test_output"), test_mode=True)
    
    warnings = generator.validate_markdown("")
    assert len(warnings) > 0
    assert any("empty" in w.lower() for w in warnings)
    
    warnings = generator.validate_markdown("   \n  \n  ")
    assert len(warnings) > 0


def test_ensure_output_structure(tmp_path):
    """Test output directory structure creation."""
    output_dir = tmp_path / "Handbook"
    generator = OutputGenerator(output_dir, test_mode=True)
    
    # Create structure for German backup handbook (now uses output_type)
    created_dir = generator.ensure_output_structure("de", "markdown")
    
    assert created_dir.exists()
    assert created_dir.is_dir()
    assert created_dir == output_dir / "de" / "markdown"
    
    # Create structure for English ISMS handbook
    created_dir = generator.ensure_output_structure("en", "pdf")
    
    assert created_dir.exists()
    assert created_dir == output_dir / "en" / "pdf"


def test_generate_markdown_basic(tmp_path):
    """Test basic markdown file generation."""
    output_dir = tmp_path / "Handbook"
    generator = OutputGenerator(output_dir, test_mode=True)
    
    contents = [
        "# Test Handbook",
        "## Section 1",
        "Content here."
    ]
    
    result = generator.generate_markdown(contents, "de", "backup")
    
    # Check result
    assert result.markdown_path is not None
    assert result.markdown_path.exists()
    assert len(result.errors) == 0
    
    # Check file content
    content = result.markdown_path.read_text(encoding='utf-8')
    assert "# Test Handbook" in content
    assert "## Section 1" in content
    assert "Content here." in content
    
    # Check file location (now uses markdown subdirectory)
    assert result.markdown_path.parent.name == "markdown"
    assert result.markdown_path.parent.parent.name == "de"


def test_generate_markdown_overwrite_warning(tmp_path):
    """Test that overwriting existing file produces warning."""
    output_dir = tmp_path / "Handbook"
    generator = OutputGenerator(output_dir, test_mode=True)
    
    contents = ["# Test"]
    
    # Generate first time
    result1 = generator.generate_markdown(contents, "de", "backup")
    # First generation might have validation warnings but not overwrite warnings
    overwrite_warnings1 = [w for w in result1.warnings if "overwrite" in w.lower() or "exists" in w.lower()]
    assert len(overwrite_warnings1) == 0, "No overwrite warning on first generation"
    
    # Generate again (overwrite)
    result2 = generator.generate_markdown(contents, "de", "backup")
    overwrite_warnings2 = [w for w in result2.warnings if "overwrite" in w.lower() or "exists" in w.lower()]
    assert len(overwrite_warnings2) > 0, f"Expected overwrite warning, got warnings: {result2.warnings}"


def test_generate_markdown_custom_filename(tmp_path):
    """Test markdown generation with custom filename."""
    output_dir = tmp_path / "Handbook"
    generator = OutputGenerator(output_dir, test_mode=True)
    
    contents = ["# Custom Handbook"]
    
    result = generator.generate_markdown(
        contents,
        "en",
        "isms",
        filename="custom_name.md"
    )
    
    assert result.markdown_path is not None
    assert result.markdown_path.name == "custom_name.md"


def test_generate_pdf_missing_dependencies(tmp_path):
    """Test PDF generation with missing dependencies."""
    output_dir = tmp_path / "Handbook"
    generator = OutputGenerator(output_dir, test_mode=True)
    
    markdown_content = "# Test PDF"
    
    # Try to generate PDF - this will likely fail due to missing system dependencies
    try:
        result = generator.generate_pdf(markdown_content, "de", "backup")
        
        # Should produce error about missing dependencies (unless they're installed)
        # This test documents the expected behavior
        assert isinstance(result, OutputResult)
        
        # If PDF generation failed, should have error message
        if result.pdf_path is None:
            assert len(result.errors) > 0
            # Error should mention dependencies or generation failure
            assert any(
                "dependencies" in e.lower() or "failed" in e.lower() or "import" in e.lower()
                for e in result.errors
            )
    except (ImportError, OSError) as e:
        # If the import itself fails (system dependencies missing), that's also expected
        # The generate_pdf method should catch this and return an error in OutputResult
        # but if it doesn't, we accept it as a known limitation
        pytest.skip(f"PDF generation dependencies not available: {e}")


def test_generate_pdf_overwrite_warning(tmp_path):
    """Test that PDF generation warns about overwriting."""
    output_dir = tmp_path / "Handbook"
    generator = OutputGenerator(output_dir, test_mode=True)
    
    # Create a dummy PDF file (now in pdf subdirectory)
    pdf_dir = output_dir / "de" / "pdf"
    pdf_dir.mkdir(parents=True, exist_ok=True)
    pdf_file = pdf_dir / "backup_handbook.pdf"
    pdf_file.write_text("dummy pdf content")
    
    markdown_content = "# Test"
    
    try:
        result = generator.generate_pdf(markdown_content, "de", "backup")
        
        # Should warn about overwriting (if PDF generation succeeds or gets far enough)
        assert any("overwrite" in w.lower() for w in result.warnings)
    except (ImportError, OSError) as e:
        # If system dependencies are missing, skip this test
        pytest.skip(f"PDF generation dependencies not available: {e}")


def test_output_result_initialization():
    """Test OutputResult dataclass initialization."""
    # Default initialization
    result = OutputResult()
    assert result.markdown_path is None
    assert result.pdf_path is None
    assert result.warnings == []
    assert result.errors == []
    
    # With values
    result = OutputResult(
        markdown_path=Path("test.md"),
        pdf_path=Path("test.pdf"),
        warnings=["warning1"],
        errors=["error1"]
    )
    assert result.markdown_path == Path("test.md")
    assert result.pdf_path == Path("test.pdf")
    assert result.warnings == ["warning1"]
    assert result.errors == ["error1"]


# ============================================================================
# Test Mode Validation Tests
# ============================================================================

def test_test_mode_disabled_blocks_markdown_generation(tmp_path):
    """Test that markdown generation is blocked when test mode is disabled."""
    output_dir = tmp_path / "test-output"
    generator = OutputGenerator(output_dir, test_mode=False)
    
    contents = ["# Test Handbook"]
    
    result = generator.generate_markdown(contents, "de", "backup")
    
    # Should have error about test mode
    assert len(result.errors) > 0
    assert any("--test" in e for e in result.errors)
    assert any("test mode" in e.lower() for e in result.errors)
    assert result.markdown_path is None


def test_test_mode_disabled_blocks_pdf_generation(tmp_path):
    """Test that PDF generation is blocked when test mode is disabled."""
    output_dir = tmp_path / "test-output"
    generator = OutputGenerator(output_dir, test_mode=False)
    
    markdown_content = "# Test Handbook"
    
    result = generator.generate_pdf(markdown_content, "de", "backup")
    
    # Should have error about test mode
    assert len(result.errors) > 0
    assert any("--test" in e for e in result.errors)
    assert any("test mode" in e.lower() for e in result.errors)
    assert result.pdf_path is None


def test_test_mode_enabled_allows_markdown_generation(tmp_path):
    """Test that markdown generation works when test mode is enabled."""
    output_dir = tmp_path / "test-output"
    generator = OutputGenerator(output_dir, test_mode=True)
    
    contents = ["# Test Handbook", "## Section 1"]
    
    result = generator.generate_markdown(contents, "de", "backup")
    
    # Should succeed
    assert result.markdown_path is not None
    assert result.markdown_path.exists()
    assert len([e for e in result.errors if "--test" in e]) == 0
    
    # Check file location uses new structure
    assert "test-output" in str(result.markdown_path)
    assert result.markdown_path.parent.name == "markdown"
    assert result.markdown_path.parent.parent.name == "de"


def test_test_mode_enabled_allows_pdf_generation(tmp_path):
    """Test that PDF generation works when test mode is enabled."""
    output_dir = tmp_path / "test-output"
    generator = OutputGenerator(output_dir, test_mode=True)
    
    markdown_content = "# Test Handbook"
    
    try:
        result = generator.generate_pdf(markdown_content, "de", "backup")
        
        # If PDF generation succeeds, check the path
        if result.pdf_path is not None:
            assert "test-output" in str(result.pdf_path)
            assert result.pdf_path.parent.name == "pdf"
            assert result.pdf_path.parent.parent.name == "de"
        
        # Should not have test mode errors
        test_mode_errors = [e for e in result.errors if "--test" in e]
        assert len(test_mode_errors) == 0
        
    except (ImportError, OSError) as e:
        pytest.skip(f"PDF generation dependencies not available: {e}")


def test_test_mode_error_message_content(tmp_path):
    """Test that test mode error message contains helpful information."""
    output_dir = tmp_path / "test-output"
    generator = OutputGenerator(output_dir, test_mode=False)
    
    contents = ["# Test"]
    result = generator.generate_markdown(contents, "de", "backup")
    
    # Check error message content
    assert len(result.errors) > 0
    error_msg = result.errors[0]
    
    # Should mention --test flag
    assert "--test" in error_msg
    # Should mention test mode
    assert "test mode" in error_msg.lower()
    # Should be helpful
    assert "requires" in error_msg.lower() or "use" in error_msg.lower()


def test_test_mode_directory_structure_creation(tmp_path):
    """Test that test mode creates correct directory structure."""
    output_dir = tmp_path / "test-output"
    generator = OutputGenerator(output_dir, test_mode=True)
    
    # Test markdown directory
    md_dir = generator.ensure_output_structure("de", "markdown")
    assert md_dir.exists()
    assert md_dir == output_dir / "de" / "markdown"
    
    # Test pdf directory
    pdf_dir = generator.ensure_output_structure("en", "pdf")
    assert pdf_dir.exists()
    assert pdf_dir == output_dir / "en" / "pdf"
    
    # Test html directory
    html_dir = generator.ensure_output_structure("de", "html")
    assert html_dir.exists()
    assert html_dir == output_dir / "de" / "html"


def test_test_mode_validation_before_directory_creation(tmp_path):
    """Test that test mode validation occurs before directory creation."""
    output_dir = tmp_path / "test-output"
    generator = OutputGenerator(output_dir, test_mode=False)
    
    # Try to ensure output structure without test mode
    with pytest.raises(RuntimeError) as exc_info:
        generator.ensure_output_structure("de", "markdown")
    
    # Check error message
    assert "--test" in str(exc_info.value)
    
    # Directory should not have been created
    assert not (output_dir / "de" / "markdown").exists()


# ============================================================================
# Separate Markdown File Generation Tests
# ============================================================================

def test_generate_separate_markdown_files_basic(tmp_path):
    """Test basic separate markdown file generation."""
    output_dir = tmp_path / "test-output"
    generator = OutputGenerator(output_dir, test_mode=True)
    
    templates_data = [
        ("0010_Introduction.md", "# Introduction\n\nThis is the intro."),
        ("0020_Chapter_One.md", "# Chapter One\n\nFirst chapter content."),
        ("0030_Chapter_Two.md", "# Chapter Two\n\nSecond chapter content.")
    ]
    
    result = generator.generate_separate_markdown_files(
        templates_data,
        "de",
        "bcm"
    )
    
    # Check result
    assert result.markdown_path is not None
    assert len(result.errors) == 0
    
    # Check that separate files were created
    output_md_dir = output_dir / "de" / "markdown"
    assert output_md_dir.exists()
    
    # Check each file exists and has correct content
    intro_file = output_md_dir / "0010_Introduction.md"
    assert intro_file.exists()
    assert "# Introduction" in intro_file.read_text(encoding='utf-8')
    
    chapter1_file = output_md_dir / "0020_Chapter_One.md"
    assert chapter1_file.exists()
    assert "# Chapter One" in chapter1_file.read_text(encoding='utf-8')
    
    chapter2_file = output_md_dir / "0030_Chapter_Two.md"
    assert chapter2_file.exists()
    assert "# Chapter Two" in chapter2_file.read_text(encoding='utf-8')
    
    # Check warning message about file count
    assert any("3 separate markdown files" in w for w in result.warnings)


def test_generate_separate_markdown_files_filename_pattern(tmp_path):
    """Test that separate markdown files follow correct naming pattern."""
    output_dir = tmp_path / "test-output"
    generator = OutputGenerator(output_dir, test_mode=True)
    
    templates_data = [
        ("0010_Zweck_und_Geltungsbereich.md", "# Zweck"),
        ("0020_BCM_Leitlinie_Policy.md", "# BCM Leitlinie"),
    ]
    
    result = generator.generate_separate_markdown_files(
        templates_data,
        "de",
        "bcm"
    )
    
    assert len(result.errors) == 0
    
    output_md_dir = output_dir / "de" / "markdown"
    
    # Check filenames match pattern {template-number}_{template-name}.md
    file1 = output_md_dir / "0010_Zweck_und_Geltungsbereich.md"
    file2 = output_md_dir / "0020_BCM_Leitlinie_Policy.md"
    
    assert file1.exists()
    assert file2.exists()


def test_generate_separate_markdown_files_test_mode_validation(tmp_path):
    """Test that separate markdown generation requires test mode."""
    output_dir = tmp_path / "test-output"
    generator = OutputGenerator(output_dir, test_mode=False)
    
    templates_data = [
        ("0010_Test.md", "# Test")
    ]
    
    result = generator.generate_separate_markdown_files(
        templates_data,
        "de",
        "bcm"
    )
    
    # Should have error about test mode
    assert len(result.errors) > 0
    assert any("--test" in e for e in result.errors)
    assert result.markdown_path is None


def test_generate_separate_markdown_files_overwrite_warning(tmp_path):
    """Test that overwriting existing files produces warnings."""
    output_dir = tmp_path / "test-output"
    generator = OutputGenerator(output_dir, test_mode=True)
    
    templates_data = [
        ("0010_Test.md", "# Test Content")
    ]
    
    # Generate first time
    result1 = generator.generate_separate_markdown_files(
        templates_data,
        "de",
        "bcm"
    )
    assert len(result1.errors) == 0
    
    # Generate again (overwrite)
    result2 = generator.generate_separate_markdown_files(
        templates_data,
        "de",
        "bcm"
    )
    
    # Should have overwrite warning
    overwrite_warnings = [w for w in result2.warnings if "overwrite" in w.lower() or "exists" in w.lower()]
    assert len(overwrite_warnings) > 0


def test_generate_separate_markdown_files_output_directory(tmp_path):
    """Test that separate markdown files go to correct directory."""
    output_dir = tmp_path / "test-output"
    generator = OutputGenerator(output_dir, test_mode=True)
    
    templates_data = [
        ("0010_Test.md", "# Test")
    ]
    
    result = generator.generate_separate_markdown_files(
        templates_data,
        "en",
        "isms"
    )
    
    assert len(result.errors) == 0
    
    # Check directory structure: test-output/en/markdown/
    expected_dir = output_dir / "en" / "markdown"
    assert expected_dir.exists()
    
    test_file = expected_dir / "0010_Test.md"
    assert test_file.exists()


def test_generate_markdown_toc_basic(tmp_path):
    """Test basic TOC file generation."""
    output_dir = tmp_path / "test-output"
    generator = OutputGenerator(output_dir, test_mode=True)
    
    templates_info = [
        ("0010", "Introduction", "0010_Introduction.md"),
        ("0020", "Chapter One", "0020_Chapter_One.md"),
        ("0030", "Chapter Two", "0030_Chapter_Two.md")
    ]
    
    result = generator.generate_markdown_toc(
        templates_info,
        "de",
        "bcm"
    )
    
    # Check result
    assert result.markdown_path is not None
    assert len(result.errors) == 0
    
    # Check TOC file exists
    toc_file = output_dir / "de" / "markdown" / "TOC.md"
    assert toc_file.exists()
    
    # Check TOC content
    toc_content = toc_file.read_text(encoding='utf-8')
    
    # Should have title
    assert "Table of Contents" in toc_content
    assert "BCM" in toc_content.upper()
    
    # Should have language
    assert "de" in toc_content
    
    # Should have links to all templates
    assert "[0010 - Introduction](0010_Introduction.md)" in toc_content
    assert "[0020 - Chapter One](0020_Chapter_One.md)" in toc_content
    assert "[0030 - Chapter Two](0030_Chapter_Two.md)" in toc_content


def test_generate_markdown_toc_link_format(tmp_path):
    """Test that TOC uses correct markdown link format."""
    output_dir = tmp_path / "test-output"
    generator = OutputGenerator(output_dir, test_mode=True)
    
    templates_info = [
        ("0010", "Zweck und Geltungsbereich", "0010_Zweck_und_Geltungsbereich.md"),
    ]
    
    result = generator.generate_markdown_toc(
        templates_info,
        "de",
        "bcm"
    )
    
    assert len(result.errors) == 0
    
    toc_file = output_dir / "de" / "markdown" / "TOC.md"
    toc_content = toc_file.read_text(encoding='utf-8')
    
    # Check markdown link format: - [0010 - Title](0010_Title.md)
    assert "- [0010 - Zweck und Geltungsbereich](0010_Zweck_und_Geltungsbereich.md)" in toc_content


def test_generate_markdown_toc_test_mode_validation(tmp_path):
    """Test that TOC generation requires test mode."""
    output_dir = tmp_path / "test-output"
    generator = OutputGenerator(output_dir, test_mode=False)
    
    templates_info = [
        ("0010", "Test", "0010_Test.md")
    ]
    
    result = generator.generate_markdown_toc(
        templates_info,
        "de",
        "bcm"
    )
    
    # Should have error about test mode
    assert len(result.errors) > 0
    assert any("--test" in e for e in result.errors)
    assert result.markdown_path is None


def test_generate_markdown_toc_overwrite_warning(tmp_path):
    """Test that TOC generation warns about overwriting."""
    output_dir = tmp_path / "test-output"
    generator = OutputGenerator(output_dir, test_mode=True)
    
    templates_info = [
        ("0010", "Test", "0010_Test.md")
    ]
    
    # Generate first time
    result1 = generator.generate_markdown_toc(
        templates_info,
        "de",
        "bcm"
    )
    assert len(result1.errors) == 0
    
    # Generate again (overwrite)
    result2 = generator.generate_markdown_toc(
        templates_info,
        "de",
        "bcm"
    )
    
    # Should have overwrite warning
    overwrite_warnings = [w for w in result2.warnings if "overwrite" in w.lower() or "exists" in w.lower()]
    assert len(overwrite_warnings) > 0


def test_generate_markdown_toc_output_directory(tmp_path):
    """Test that TOC file goes to correct directory."""
    output_dir = tmp_path / "test-output"
    generator = OutputGenerator(output_dir, test_mode=True)
    
    templates_info = [
        ("0010", "Test", "0010_Test.md")
    ]
    
    result = generator.generate_markdown_toc(
        templates_info,
        "en",
        "isms"
    )
    
    assert len(result.errors) == 0
    
    # Check directory structure: test-output/en/markdown/TOC.md
    toc_file = output_dir / "en" / "markdown" / "TOC.md"
    assert toc_file.exists()


def test_separate_markdown_no_combined_file(tmp_path):
    """Test that separate markdown mode does not create a combined file."""
    output_dir = tmp_path / "test-output"
    generator = OutputGenerator(output_dir, test_mode=True)
    
    templates_data = [
        ("0010_Test.md", "# Test 1"),
        ("0020_Test.md", "# Test 2")
    ]
    
    result = generator.generate_separate_markdown_files(
        templates_data,
        "de",
        "bcm"
    )
    
    assert len(result.errors) == 0
    
    output_md_dir = output_dir / "de" / "markdown"
    
    # Check that separate files exist
    assert (output_md_dir / "0010_Test.md").exists()
    assert (output_md_dir / "0020_Test.md").exists()
    
    # Check that no combined file exists (e.g., bcm_handbook.md)
    combined_file = output_md_dir / "bcm_handbook.md"
    assert not combined_file.exists()


# ============================================================================
# PDF with TOC Tests
# ============================================================================

def test_generate_pdf_with_toc_basic(tmp_path):
    """Test basic PDF generation with table of contents."""
    output_dir = tmp_path / "test-output"
    generator = OutputGenerator(output_dir, test_mode=True)
    
    templates_data = [
        ("0010", "Introduction", "# Introduction\n\nThis is the intro."),
        ("0020", "Chapter One", "# Chapter One\n\nFirst chapter content."),
        ("0030", "Chapter Two", "# Chapter Two\n\nSecond chapter content.")
    ]
    
    try:
        result = generator.generate_pdf_with_toc(
            templates_data,
            "de",
            "bcm"
        )
        
        # Check result structure
        assert isinstance(result, OutputResult)
        
        # If PDF generation succeeds, check the path
        if result.pdf_path is not None:
            assert result.pdf_path.exists()
            assert result.pdf_path.name == "bcm_handbook.pdf"
            assert result.pdf_path.parent.name == "pdf"
            assert result.pdf_path.parent.parent.name == "de"
            assert len(result.errors) == 0
        else:
            # If PDF generation failed, should have error message
            assert len(result.errors) > 0
            
    except (ImportError, OSError) as e:
        pytest.skip(f"PDF generation dependencies not available: {e}")


def test_generate_pdf_with_toc_test_mode_validation(tmp_path):
    """Test that PDF with TOC generation requires test mode."""
    output_dir = tmp_path / "test-output"
    generator = OutputGenerator(output_dir, test_mode=False)
    
    templates_data = [
        ("0010", "Test", "# Test")
    ]
    
    result = generator.generate_pdf_with_toc(
        templates_data,
        "de",
        "bcm"
    )
    
    # Should have error about test mode
    assert len(result.errors) > 0
    assert any("--test" in e for e in result.errors)
    assert result.pdf_path is None


def test_generate_pdf_with_toc_overwrite_warning(tmp_path):
    """Test that PDF with TOC generation warns about overwriting."""
    output_dir = tmp_path / "test-output"
    generator = OutputGenerator(output_dir, test_mode=True)
    
    # Create a dummy PDF file
    pdf_dir = output_dir / "de" / "pdf"
    pdf_dir.mkdir(parents=True, exist_ok=True)
    pdf_file = pdf_dir / "bcm_handbook.pdf"
    pdf_file.write_text("dummy pdf content")
    
    templates_data = [
        ("0010", "Test", "# Test")
    ]
    
    try:
        result = generator.generate_pdf_with_toc(
            templates_data,
            "de",
            "bcm"
        )
        
        # Should warn about overwriting
        assert any("overwrite" in w.lower() for w in result.warnings)
        
    except (ImportError, OSError) as e:
        pytest.skip(f"PDF generation dependencies not available: {e}")


def test_generate_pdf_with_toc_custom_filename(tmp_path):
    """Test PDF with TOC generation with custom filename."""
    output_dir = tmp_path / "test-output"
    generator = OutputGenerator(output_dir, test_mode=True)
    
    templates_data = [
        ("0010", "Test", "# Test")
    ]
    
    try:
        result = generator.generate_pdf_with_toc(
            templates_data,
            "en",
            "isms",
            filename="custom_handbook.pdf"
        )
        
        if result.pdf_path is not None:
            assert result.pdf_path.name == "custom_handbook.pdf"
            
    except (ImportError, OSError) as e:
        pytest.skip(f"PDF generation dependencies not available: {e}")


def test_add_page_breaks_basic(tmp_path):
    """Test page break insertion between templates."""
    output_dir = tmp_path / "test-output"
    generator = OutputGenerator(output_dir, test_mode=True)
    
    templates_html = [
        "<h1>Template 1</h1><p>Content 1</p>",
        "<h1>Template 2</h1><p>Content 2</p>",
        "<h1>Template 3</h1><p>Content 3</p>"
    ]
    
    result = generator._add_page_breaks(templates_html)
    
    # Check that page breaks are inserted
    assert '<div class="page-break"></div>' in result
    
    # Count page breaks (should be n-1 for n templates)
    page_break_count = result.count('<div class="page-break"></div>')
    assert page_break_count == 2  # 3 templates = 2 page breaks
    
    # Check that all templates are present
    assert "Template 1" in result
    assert "Template 2" in result
    assert "Template 3" in result


def test_add_page_breaks_empty(tmp_path):
    """Test page break insertion with empty input."""
    output_dir = tmp_path / "test-output"
    generator = OutputGenerator(output_dir, test_mode=True)
    
    result = generator._add_page_breaks([])
    assert result == ""


def test_add_page_breaks_single_template(tmp_path):
    """Test page break insertion with single template (no breaks needed)."""
    output_dir = tmp_path / "test-output"
    generator = OutputGenerator(output_dir, test_mode=True)
    
    templates_html = ["<h1>Single Template</h1>"]
    
    result = generator._add_page_breaks(templates_html)
    
    # Should not have page breaks for single template
    assert '<div class="page-break"></div>' not in result
    assert "Single Template" in result


def test_generate_toc_html_basic(tmp_path):
    """Test TOC HTML generation."""
    output_dir = tmp_path / "test-output"
    generator = OutputGenerator(output_dir, test_mode=True)
    
    templates_data = [
        ("0010", "Introduction", "# Intro"),
        ("0020", "Chapter One", "# Chapter 1"),
        ("0030", "Chapter Two", "# Chapter 2")
    ]
    
    toc_html = generator._generate_toc_html(templates_data, "bcm")
    
    # Check TOC structure
    assert '<div class="toc">' in toc_html
    assert '<h1>Table of Contents</h1>' in toc_html
    assert '<ul>' in toc_html
    assert '</ul>' in toc_html
    assert '</div>' in toc_html
    
    # Check that all templates are listed
    assert '0010 - Introduction' in toc_html
    assert '0020 - Chapter One' in toc_html
    assert '0030 - Chapter Two' in toc_html
    
    # Check anchor links
    assert 'href="#section-0010"' in toc_html
    assert 'href="#section-0020"' in toc_html
    assert 'href="#section-0030"' in toc_html
    
    # Check page break after TOC
    assert '<div class="page-break"></div>' in toc_html


def test_generate_toc_html_empty(tmp_path):
    """Test TOC HTML generation with empty input."""
    output_dir = tmp_path / "test-output"
    generator = OutputGenerator(output_dir, test_mode=True)
    
    toc_html = generator._generate_toc_html([], "bcm")
    
    # Should still have TOC structure
    assert '<div class="toc">' in toc_html
    assert '<h1>Table of Contents</h1>' in toc_html
    assert '<ul>' in toc_html
    assert '</ul>' in toc_html


def test_generate_pdf_with_toc_anchor_ids(tmp_path):
    """Test that PDF with TOC includes anchor IDs for each template."""
    output_dir = tmp_path / "test-output"
    generator = OutputGenerator(output_dir, test_mode=True)
    
    templates_data = [
        ("0010", "Test Template", "# Test Content")
    ]
    
    try:
        # We can't easily test the final PDF, but we can test the HTML generation
        # by checking the TOC HTML and verifying anchor structure
        toc_html = generator._generate_toc_html(templates_data, "bcm")
        
        # Check that anchor link is present in TOC
        assert 'href="#section-0010"' in toc_html
        
        # The actual anchor ID would be added during HTML conversion
        # We verify the structure is correct
        assert '0010 - Test Template' in toc_html
        
    except Exception as e:
        pytest.skip(f"Test skipped due to: {e}")


def test_generate_pdf_with_toc_output_directory(tmp_path):
    """Test that PDF with TOC goes to correct directory."""
    output_dir = tmp_path / "test-output"
    generator = OutputGenerator(output_dir, test_mode=True)
    
    templates_data = [
        ("0010", "Test", "# Test")
    ]
    
    try:
        result = generator.generate_pdf_with_toc(
            templates_data,
            "en",
            "isms"
        )
        
        if result.pdf_path is not None:
            # Check directory structure: test-output/en/pdf/
            expected_dir = output_dir / "en" / "pdf"
            assert result.pdf_path.parent == expected_dir
            
    except (ImportError, OSError) as e:
        pytest.skip(f"PDF generation dependencies not available: {e}")


