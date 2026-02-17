"""
Test suite for diagrams directory structure validation.

This module ensures that every handbook template has a diagrams subdirectory
with a README.md file explaining its purpose and usage.
"""

import os
import pytest
from pathlib import Path


# Get the project root directory
PROJECT_ROOT = Path(__file__).parent.parent
TEMPLATES_DIR = PROJECT_ROOT / "templates"


def get_all_handbook_directories():
    """
    Get all handbook directories from both English and German templates.
    
    Returns:
        list: List of tuples (language, framework_name, path)
    """
    handbooks = []
    
    for language in ["en", "de"]:
        lang_dir = TEMPLATES_DIR / language
        if not lang_dir.exists():
            continue
            
        for framework_dir in lang_dir.iterdir():
            if framework_dir.is_dir() and not framework_dir.name.startswith('.'):
                handbooks.append((language, framework_dir.name, framework_dir))
    
    return handbooks


def get_all_diagrams_directories():
    """
    Get all diagrams directories from both English and German templates.
    
    Returns:
        list: List of tuples (language, framework_name, diagrams_path)
    """
    diagrams_dirs = []
    
    for language, framework_name, framework_path in get_all_handbook_directories():
        diagrams_path = framework_path / "diagrams"
        diagrams_dirs.append((language, framework_name, diagrams_path))
    
    return diagrams_dirs


class TestDiagramsStructure:
    """Test suite for diagrams directory structure."""
    
    def test_templates_directory_exists(self):
        """Test that the templates directory exists."""
        assert TEMPLATES_DIR.exists(), f"Templates directory not found: {TEMPLATES_DIR}"
        assert TEMPLATES_DIR.is_dir(), f"Templates path is not a directory: {TEMPLATES_DIR}"
    
    def test_language_directories_exist(self):
        """Test that both English and German template directories exist."""
        en_dir = TEMPLATES_DIR / "en"
        de_dir = TEMPLATES_DIR / "de"
        
        assert en_dir.exists(), "English templates directory (templates/en) not found"
        assert en_dir.is_dir(), "templates/en is not a directory"
        
        assert de_dir.exists(), "German templates directory (templates/de) not found"
        assert de_dir.is_dir(), "templates/de is not a directory"
    
    def test_handbooks_discovered(self):
        """Test that handbooks are discovered in both languages."""
        handbooks = get_all_handbook_directories()
        
        assert len(handbooks) > 0, "No handbooks found in templates directory"
        
        # Check that we have handbooks in both languages
        languages = set(lang for lang, _, _ in handbooks)
        assert "en" in languages, "No English handbooks found"
        assert "de" in languages, "No German handbooks found"
        
        # Check that we have a reasonable number of handbooks
        en_count = sum(1 for lang, _, _ in handbooks if lang == "en")
        de_count = sum(1 for lang, _, _ in handbooks if lang == "de")
        
        assert en_count >= 20, f"Expected at least 20 English handbooks, found {en_count}"
        assert de_count >= 20, f"Expected at least 20 German handbooks, found {de_count}"
        assert en_count == de_count, f"Mismatch: {en_count} EN handbooks vs {de_count} DE handbooks"
    
    @pytest.mark.parametrize("language,framework_name,framework_path", get_all_handbook_directories())
    def test_diagrams_directory_exists(self, language, framework_name, framework_path):
        """Test that each handbook has a diagrams subdirectory."""
        diagrams_path = framework_path / "diagrams"
        
        assert diagrams_path.exists(), (
            f"Diagrams directory missing for {language}/{framework_name}\n"
            f"Expected: {diagrams_path}\n"
            f"Please create the directory: mkdir -p {diagrams_path}"
        )
        
        assert diagrams_path.is_dir(), (
            f"Diagrams path exists but is not a directory: {diagrams_path}"
        )
    
    @pytest.mark.parametrize("language,framework_name,diagrams_path", get_all_diagrams_directories())
    def test_diagrams_readme_exists(self, language, framework_name, diagrams_path):
        """Test that each diagrams directory has a README.md file."""
        readme_path = diagrams_path / "README.md"
        
        assert readme_path.exists(), (
            f"README.md missing in diagrams directory for {language}/{framework_name}\n"
            f"Expected: {readme_path}\n"
            f"Please create the README file with diagram usage instructions"
        )
        
        assert readme_path.is_file(), (
            f"README.md exists but is not a file: {readme_path}"
        )
    
    @pytest.mark.parametrize("language,framework_name,diagrams_path", get_all_diagrams_directories())
    def test_diagrams_readme_not_empty(self, language, framework_name, diagrams_path):
        """Test that each diagrams README.md file is not empty."""
        readme_path = diagrams_path / "README.md"
        
        if not readme_path.exists():
            pytest.skip(f"README.md does not exist: {readme_path}")
        
        content = readme_path.read_text(encoding='utf-8')
        
        assert len(content.strip()) > 0, (
            f"README.md is empty for {language}/{framework_name}\n"
            f"File: {readme_path}\n"
            f"Please add content explaining diagram usage"
        )
        
        # Check minimum content length (should have at least some documentation)
        assert len(content) >= 100, (
            f"README.md is too short for {language}/{framework_name}\n"
            f"File: {readme_path}\n"
            f"Current length: {len(content)} characters\n"
            f"Expected at least 100 characters of documentation"
        )
    
    @pytest.mark.parametrize("language,framework_name,diagrams_path", get_all_diagrams_directories())
    def test_diagrams_readme_has_title(self, language, framework_name, diagrams_path):
        """Test that each diagrams README.md has a title."""
        readme_path = diagrams_path / "README.md"
        
        if not readme_path.exists():
            pytest.skip(f"README.md does not exist: {readme_path}")
        
        content = readme_path.read_text(encoding='utf-8')
        lines = content.split('\n')
        
        # Check that first non-empty line is a markdown header
        first_line = next((line for line in lines if line.strip()), None)
        
        assert first_line is not None, (
            f"README.md has no content for {language}/{framework_name}: {readme_path}"
        )
        
        assert first_line.startswith('#'), (
            f"README.md should start with a markdown header for {language}/{framework_name}\n"
            f"File: {readme_path}\n"
            f"First line: {first_line}"
        )
    
    @pytest.mark.parametrize("language,framework_name,diagrams_path", get_all_diagrams_directories())
    def test_diagrams_readme_has_key_sections(self, language, framework_name, diagrams_path):
        """Test that each diagrams README.md has key documentation sections."""
        readme_path = diagrams_path / "README.md"
        
        if not readme_path.exists():
            pytest.skip(f"README.md does not exist: {readme_path}")
        
        content = readme_path.read_text(encoding='utf-8').lower()
        
        # Check for key sections that should be in diagram documentation
        expected_keywords = [
            'diagram',  # Should mention diagrams
            'purpose',  # Should explain purpose
            'format',   # Should mention supported formats
            'usage',    # Should explain how to use
        ]
        
        missing_keywords = [kw for kw in expected_keywords if kw not in content]
        
        assert len(missing_keywords) == 0, (
            f"README.md missing key sections for {language}/{framework_name}\n"
            f"File: {readme_path}\n"
            f"Missing keywords: {', '.join(missing_keywords)}\n"
            f"Expected sections: Purpose, Supported Formats, Usage"
        )
    
    def test_diagrams_structure_summary(self):
        """Test summary: verify overall diagrams structure completeness."""
        handbooks = get_all_handbook_directories()
        diagrams_dirs = get_all_diagrams_directories()
        
        # Count handbooks with complete diagrams structure
        complete_count = 0
        incomplete = []
        
        for language, framework_name, diagrams_path in diagrams_dirs:
            readme_path = diagrams_path / "README.md"
            
            if diagrams_path.exists() and readme_path.exists():
                complete_count += 1
            else:
                incomplete.append(f"{language}/{framework_name}")
        
        total_handbooks = len(handbooks)
        completion_rate = (complete_count / total_handbooks * 100) if total_handbooks > 0 else 0
        
        # Generate summary message
        summary = (
            f"\n{'='*60}\n"
            f"Diagrams Structure Summary\n"
            f"{'='*60}\n"
            f"Total handbooks: {total_handbooks}\n"
            f"Complete (with diagrams/README.md): {complete_count}\n"
            f"Completion rate: {completion_rate:.1f}%\n"
        )
        
        if incomplete:
            summary += f"\nIncomplete handbooks:\n"
            for item in incomplete:
                summary += f"  - {item}\n"
        
        summary += f"{'='*60}\n"
        
        # Assert 100% completion
        assert completion_rate == 100.0, (
            f"{summary}\n"
            f"Not all handbooks have complete diagrams structure.\n"
            f"Expected: 100% completion\n"
            f"Actual: {completion_rate:.1f}%"
        )
        
        # Print summary for successful test
        print(summary)
    
    def test_symmetric_structure_en_de(self):
        """Test that English and German handbooks have symmetric structure."""
        handbooks = get_all_handbook_directories()
        
        # Group by framework name
        en_frameworks = set(name for lang, name, _ in handbooks if lang == "en")
        de_frameworks = set(name for lang, name, _ in handbooks if lang == "de")
        
        # Check for frameworks only in one language
        only_en = en_frameworks - de_frameworks
        only_de = de_frameworks - en_frameworks
        
        assert len(only_en) == 0, (
            f"Frameworks only in English: {', '.join(sorted(only_en))}\n"
            f"These frameworks need German translations"
        )
        
        assert len(only_de) == 0, (
            f"Frameworks only in German: {', '.join(sorted(only_de))}\n"
            f"These frameworks need English translations"
        )
        
        # Verify diagrams structure is symmetric
        for framework_name in en_frameworks:
            en_diagrams = TEMPLATES_DIR / "en" / framework_name / "diagrams"
            de_diagrams = TEMPLATES_DIR / "de" / framework_name / "diagrams"
            
            en_has_diagrams = en_diagrams.exists()
            de_has_diagrams = de_diagrams.exists()
            
            assert en_has_diagrams == de_has_diagrams, (
                f"Asymmetric diagrams structure for {framework_name}\n"
                f"EN has diagrams: {en_has_diagrams}\n"
                f"DE has diagrams: {de_has_diagrams}"
            )
            
            if en_has_diagrams:
                en_readme = en_diagrams / "README.md"
                de_readme = de_diagrams / "README.md"
                
                assert en_readme.exists() == de_readme.exists(), (
                    f"Asymmetric README.md for {framework_name}\n"
                    f"EN has README: {en_readme.exists()}\n"
                    f"DE has README: {de_readme.exists()}"
                )


class TestDiagramsContentQuality:
    """Test suite for diagrams README content quality."""
    
    @pytest.mark.parametrize("language,framework_name,diagrams_path", get_all_diagrams_directories())
    def test_readme_mentions_supported_formats(self, language, framework_name, diagrams_path):
        """Test that README mentions common diagram formats."""
        readme_path = diagrams_path / "README.md"
        
        if not readme_path.exists():
            pytest.skip(f"README.md does not exist: {readme_path}")
        
        content = readme_path.read_text(encoding='utf-8').lower()
        
        # Check for common diagram formats
        common_formats = ['plantuml', 'mermaid', 'svg', 'png']
        mentioned_formats = [fmt for fmt in common_formats if fmt in content]
        
        assert len(mentioned_formats) >= 2, (
            f"README.md should mention common diagram formats for {language}/{framework_name}\n"
            f"File: {readme_path}\n"
            f"Found: {', '.join(mentioned_formats) if mentioned_formats else 'none'}\n"
            f"Expected at least 2 of: {', '.join(common_formats)}"
        )
    
    @pytest.mark.parametrize("language,framework_name,diagrams_path", get_all_diagrams_directories())
    def test_readme_has_usage_example(self, language, framework_name, diagrams_path):
        """Test that README includes usage examples."""
        readme_path = diagrams_path / "README.md"
        
        if not readme_path.exists():
            pytest.skip(f"README.md does not exist: {readme_path}")
        
        content = readme_path.read_text(encoding='utf-8')
        
        # Check for markdown code blocks (usage examples)
        has_code_block = '```' in content or '    ' in content
        
        assert has_code_block, (
            f"README.md should include usage examples for {language}/{framework_name}\n"
            f"File: {readme_path}\n"
            f"Expected markdown code blocks with usage examples"
        )


if __name__ == "__main__":
    # Run tests with pytest
    pytest.main([__file__, "-v", "--tb=short"])
