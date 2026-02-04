"""
Tests for HTML Comment Processor

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

import pytest
from hypothesis import given, settings, strategies as st

from src.html_comment_processor import HTMLCommentProcessor


class TestHTMLCommentRemoval:
    """Unit tests for HTML comment removal functionality."""
    
    def test_remove_single_line_comment(self):
        """Test removal of single-line HTML comment."""
        processor = HTMLCommentProcessor()
        content = "# Header\n<!-- This is a comment -->\nSome text"
        
        result = processor.remove_comments(content)
        
        assert "<!--" not in result
        assert "-->" not in result
        assert "# Header" in result
        assert "Some text" in result
    
    def test_remove_multi_line_comment(self):
        """Test removal of multi-line HTML comment."""
        processor = HTMLCommentProcessor()
        content = """# Header
<!-- This is a
multi-line
comment -->
Some text"""
        
        result = processor.remove_comments(content)
        
        assert "<!--" not in result
        assert "-->" not in result
        assert "# Header" in result
        assert "Some text" in result
        assert "multi-line" not in result
    
    def test_remove_empty_comment(self):
        """Test removal of empty HTML comment."""
        processor = HTMLCommentProcessor()
        content = "Text before<!-- -->Text after"
        
        result = processor.remove_comments(content)
        
        assert "<!--" not in result
        assert "-->" not in result
        assert "Text before" in result
        assert "Text after" in result
    
    def test_remove_comment_with_special_characters(self):
        """Test removal of comment with special characters."""
        processor = HTMLCommentProcessor()
        content = "# Header\n<!-- TODO: Fix {{ meta.org }} -->\nContent"
        
        result = processor.remove_comments(content)
        
        assert "<!--" not in result
        assert "-->" not in result
        assert "TODO" not in result
        assert "{{ meta.org }}" not in result
        assert "# Header" in result
        assert "Content" in result
    
    def test_preserve_markdown_formatting(self):
        """Test that markdown formatting is preserved."""
        processor = HTMLCommentProcessor()
        content = """# Header 1
## Header 2
<!-- Comment -->
- List item 1
- List item 2

**Bold text**

```python
code block
```"""
        
        result = processor.remove_comments(content)
        
        assert "<!--" not in result
        assert "-->" not in result
        assert "# Header 1" in result
        assert "## Header 2" in result
        assert "- List item 1" in result
        assert "**Bold text**" in result
        assert "```python" in result
        assert "code block" in result
    
    def test_remove_multiple_comments(self):
        """Test removal of multiple HTML comments."""
        processor = HTMLCommentProcessor()
        content = """<!-- Comment 1 -->
Text 1
<!-- Comment 2 -->
Text 2
<!-- Comment 3 -->"""
        
        result = processor.remove_comments(content)
        
        assert "<!--" not in result
        assert "-->" not in result
        assert "Comment 1" not in result
        assert "Comment 2" not in result
        assert "Comment 3" not in result
        assert "Text 1" in result
        assert "Text 2" in result
    
    def test_comment_adjacent_to_markdown(self):
        """Test comment adjacent to markdown syntax."""
        processor = HTMLCommentProcessor()
        content = "<!-- comment -->## Header"
        
        result = processor.remove_comments(content)
        
        assert "<!--" not in result
        assert "-->" not in result
        assert "## Header" in result
    
    def test_empty_content(self):
        """Test with empty content."""
        processor = HTMLCommentProcessor()
        content = ""
        
        result = processor.remove_comments(content)
        
        assert result == ""
    
    def test_none_content(self):
        """Test with None content."""
        processor = HTMLCommentProcessor()
        content = None
        
        result = processor.remove_comments(content)
        
        assert result is None
    
    def test_content_without_comments(self):
        """Test content without any comments."""
        processor = HTMLCommentProcessor()
        content = """# Header
Some text
More text"""
        
        result = processor.remove_comments(content)
        
        assert result == content
    
    def test_comment_with_newlines_inside(self):
        """Test comment with multiple newlines inside."""
        processor = HTMLCommentProcessor()
        content = """Text before
<!--

Multiple blank lines


inside comment

-->
Text after"""
        
        result = processor.remove_comments(content)
        
        assert "<!--" not in result
        assert "-->" not in result
        assert "Text before" in result
        assert "Text after" in result
        assert "inside comment" not in result


class TestHTMLCommentValidation:
    """Unit tests for HTML comment validation functionality."""
    
    def test_validate_valid_comment(self):
        """Test validation of valid HTML comment."""
        processor = HTMLCommentProcessor()
        content = "<!-- Valid comment -->"
        
        warnings = processor.validate_comments(content)
        
        assert len(warnings) == 0
    
    def test_validate_unclosed_comment(self):
        """Test detection of unclosed HTML comment."""
        processor = HTMLCommentProcessor()
        content = "<!-- Unclosed comment"
        
        warnings = processor.validate_comments(content)
        
        assert len(warnings) >= 1
        assert any("unclosed" in w.lower() for w in warnings)
    
    def test_validate_nested_comments(self):
        """Test warning about nested HTML comments."""
        processor = HTMLCommentProcessor()
        content = "<!-- Outer <!-- Inner --> -->"
        
        warnings = processor.validate_comments(content)
        
        assert len(warnings) >= 1
        assert any("nested" in w.lower() for w in warnings)
    
    def test_validate_empty_content(self):
        """Test validation of empty content."""
        processor = HTMLCommentProcessor()
        content = ""
        
        warnings = processor.validate_comments(content)
        
        assert len(warnings) == 0
    
    def test_validate_none_content(self):
        """Test validation of None content."""
        processor = HTMLCommentProcessor()
        content = None
        
        warnings = processor.validate_comments(content)
        
        assert len(warnings) == 0
    
    def test_validate_multiple_valid_comments(self):
        """Test validation of multiple valid comments."""
        processor = HTMLCommentProcessor()
        content = """<!-- Comment 1 -->
Text
<!-- Comment 2 -->"""
        
        warnings = processor.validate_comments(content)
        
        assert len(warnings) == 0
    
    def test_validate_unclosed_comment_line_number(self):
        """Test that unclosed comment warning includes line number."""
        processor = HTMLCommentProcessor()
        content = """Line 1
Line 2
<!-- Unclosed comment on line 3"""
        
        warnings = processor.validate_comments(content)
        
        assert len(warnings) >= 1
        assert any("line 3" in w.lower() for w in warnings)
    
    def test_validate_content_without_comments(self):
        """Test validation of content without comments."""
        processor = HTMLCommentProcessor()
        content = """# Header
Regular text
No comments here"""
        
        warnings = processor.validate_comments(content)
        
        assert len(warnings) == 0


class TestHTMLCommentEdgeCases:
    """Tests for edge cases in HTML comment processing."""
    
    def test_comment_with_dashes_inside(self):
        """Test comment containing dashes inside."""
        processor = HTMLCommentProcessor()
        content = "<!-- Comment with -- dashes -->"
        
        result = processor.remove_comments(content)
        
        # Should remove the entire comment
        assert "<!--" not in result
        assert "-->" not in result
    
    def test_comment_at_start_of_file(self):
        """Test comment at the very start of file."""
        processor = HTMLCommentProcessor()
        content = "<!-- First line comment -->\nText"
        
        result = processor.remove_comments(content)
        
        assert "<!--" not in result
        assert "Text" in result
    
    def test_comment_at_end_of_file(self):
        """Test comment at the very end of file."""
        processor = HTMLCommentProcessor()
        content = "Text\n<!-- Last line comment -->"
        
        result = processor.remove_comments(content)
        
        assert "<!--" not in result
        assert "Text" in result
    
    def test_comment_only_content(self):
        """Test content that is only a comment."""
        processor = HTMLCommentProcessor()
        content = "<!-- Only comment -->"
        
        result = processor.remove_comments(content)
        
        assert "<!--" not in result
        assert "-->" not in result
        # Result should be empty or whitespace only
        assert result.strip() == ""
    
    def test_multiple_comments_on_same_line(self):
        """Test multiple comments on the same line."""
        processor = HTMLCommentProcessor()
        content = "<!-- Comment 1 --> Text <!-- Comment 2 -->"
        
        result = processor.remove_comments(content)
        
        assert "<!--" not in result
        assert "-->" not in result
        assert "Text" in result
        assert "Comment 1" not in result
        assert "Comment 2" not in result
    
    def test_comment_with_markdown_inside(self):
        """Test comment containing markdown syntax."""
        processor = HTMLCommentProcessor()
        content = """Text before
<!-- 
# This is a header inside comment
- List item
**Bold**
-->
Text after"""
        
        result = processor.remove_comments(content)
        
        assert "<!--" not in result
        assert "-->" not in result
        assert "Text before" in result
        assert "Text after" in result
        # Markdown inside comment should be removed
        assert "# This is a header inside comment" not in result
        assert "- List item" not in result
    
    def test_whitespace_preservation(self):
        """Test that whitespace around comments is handled correctly."""
        processor = HTMLCommentProcessor()
        content = "Line 1\n\n<!-- Comment -->\n\nLine 2"
        
        result = processor.remove_comments(content)
        
        assert "<!--" not in result
        assert "Line 1" in result
        assert "Line 2" in result



class TestHTMLCommentRemovalProperty:
    """Property-based tests for HTML comment removal."""
    
    @settings(max_examples=100)
    @given(
        content_before=st.text(
            alphabet=st.characters(blacklist_characters='<>-'),
            max_size=100
        ),
        comment_text=st.text(
            alphabet=st.characters(blacklist_characters='<>-'),
            max_size=100
        ),
        content_after=st.text(
            alphabet=st.characters(blacklist_characters='<>-'),
            max_size=100
        )
    )
    def test_property_1_html_comment_removal_completeness(
        self,
        content_before,
        comment_text,
        content_after
    ):
        """
        Feature: template-system-extension
        Property 1: HTML Comment Removal Completeness
        
        For any template content containing HTML comments, after processing,
        the output SHALL NOT contain any HTML comment markers (<!-- or -->).
        
        Validates: Requirements 16.1, 17.1, 17.2
        """
        processor = HTMLCommentProcessor()
        
        # Create content with HTML comment
        content_with_comment = f"{content_before}<!-- {comment_text} -->{content_after}"
        
        # Process content
        result = processor.remove_comments(content_with_comment)
        
        # Verify no comment markers remain
        assert "<!--" not in result, \
            "Opening comment marker should be removed"
        assert "-->" not in result, \
            "Closing comment marker should be removed"
        
        # Verify the surrounding content is preserved
        if content_before:
            assert content_before in result, \
                "Content before comment should be preserved"
        if content_after:
            assert content_after in result, \
                "Content after comment should be preserved"
    
    @settings(max_examples=100)
    @given(
        num_comments=st.integers(min_value=1, max_value=10),
        data=st.data()
    )
    def test_property_1_multiple_comments_removal(self, num_comments, data):
        """
        Feature: template-system-extension
        Property 1: HTML Comment Removal Completeness (Multiple Comments)
        
        For any template content containing multiple HTML comments, after processing,
        the output SHALL NOT contain any HTML comment markers.
        
        Validates: Requirements 16.1, 17.1, 17.2
        """
        processor = HTMLCommentProcessor()
        
        # Generate content with multiple comments
        parts = []
        for i in range(num_comments):
            # Add some content
            content = data.draw(st.text(
                alphabet=st.characters(blacklist_characters='<>-'),
                max_size=50
            ))
            parts.append(content)
            
            # Add a comment
            comment = data.draw(st.text(
                alphabet=st.characters(blacklist_characters='<>-'),
                max_size=50
            ))
            parts.append(f"<!-- {comment} -->")
        
        # Add final content
        final_content = data.draw(st.text(
            alphabet=st.characters(blacklist_characters='<>-'),
            max_size=50
        ))
        parts.append(final_content)
        
        content_with_comments = ''.join(parts)
        
        # Process content
        result = processor.remove_comments(content_with_comments)
        
        # Verify no comment markers remain
        assert "<!--" not in result, \
            f"Opening comment markers should be removed (found in: {result})"
        assert "-->" not in result, \
            f"Closing comment markers should be removed (found in: {result})"
    
    @settings(max_examples=100)
    @given(
        content=st.text(max_size=200),
        num_lines=st.integers(min_value=1, max_value=10),
        data=st.data()
    )
    def test_property_1_multiline_comment_removal(self, content, num_lines, data):
        """
        Feature: template-system-extension
        Property 1: HTML Comment Removal Completeness (Multiline)
        
        For any template content containing multiline HTML comments, after processing,
        the output SHALL NOT contain any HTML comment markers.
        
        Validates: Requirements 16.1, 16.3, 17.1, 17.2
        """
        processor = HTMLCommentProcessor()
        
        # Generate multiline comment
        comment_lines = []
        for i in range(num_lines):
            line = data.draw(st.text(
                alphabet=st.characters(blacklist_characters='<>-'),
                max_size=50
            ))
            comment_lines.append(line)
        
        multiline_comment = '\n'.join(comment_lines)
        
        # Create content with multiline comment
        content_with_comment = f"{content}\n<!--\n{multiline_comment}\n-->\n{content}"
        
        # Process content
        result = processor.remove_comments(content_with_comment)
        
        # Verify no comment markers remain
        assert "<!--" not in result, \
            "Opening comment marker should be removed from multiline comment"
        assert "-->" not in result, \
            "Closing comment marker should be removed from multiline comment"
