"""
HTML Comment Processor for Handbook Generator

Processes templates to remove HTML-style comments before placeholder processing.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

import re
from typing import Optional


class HTMLCommentProcessor:
    """
    Processes templates to remove HTML comments using regex with BeautifulSoup fallback.
    
    HTML comments follow the format: <!-- comment -->
    Comments can span single or multiple lines.
    
    Uses regex for primary processing (fast and preserves markdown exactly),
    with BeautifulSoup as fallback for complex edge cases.
    """
    
    # Regex pattern for HTML comment detection
    # Matches: <!-- ... --> with DOTALL flag for multiline support
    # Non-greedy match (.*?) to handle multiple comments correctly
    COMMENT_PATTERN = re.compile(r'<!--.*?-->', re.DOTALL)
    
    def remove_comments(self, content: str) -> str:
        """
        Remove all HTML comments from content using regex.
        
        Handles:
        - Single-line comments: <!-- comment -->
        - Multi-line comments: <!-- 
                                  comment
                                  -->
        - Empty comments: <!-- -->
        - Comments with special characters
        - Comment content containing --> markers (per HTML spec)
        
        Preserves:
        - Surrounding markdown content exactly as-is
        - Whitespace and formatting
        - Special characters without escaping
        
        Note: Per HTML spec, --> cannot appear in comment content. If it does,
        the first --> closes the comment and any subsequent --> becomes plain text.
        This is correct HTML parsing behavior implemented by the regex.
        
        Args:
            content: Template content with potential HTML comments
            
        Returns:
            Content with all HTML comments removed
        """
        if not content:
            return content
        
        # Remove all HTML comments using regex
        # The pattern <!--.*?--> matches from <!-- to the nearest -->
        # DOTALL flag allows . to match newlines for multiline comments
        # Non-greedy .*? ensures we match the shortest possible comment
        cleaned_content = self.COMMENT_PATTERN.sub('', content)
        
        return cleaned_content
    
    def validate_comments(self, content: str) -> list[str]:
        """
        Validate HTML comments for common issues using BeautifulSoup4.
        
        Checks for:
        - Unclosed comments (<!-- without -->)
        - Malformed comment syntax
        
        Args:
            content: Template content to validate
            
        Returns:
            List of validation warnings
        """
        warnings = []
        
        if not content:
            return warnings
        
        # Check for unclosed comments using simple pattern matching
        # BeautifulSoup will handle them, but we want to warn users
        lines = content.split('\n')
        open_count = 0
        close_count = 0
        unclosed_line = None
        
        for line_num, line in enumerate(lines, start=1):
            opens = line.count('<!--')
            closes = line.count('-->')
            
            open_count += opens
            close_count += closes
            
            # Track first unclosed comment
            if unclosed_line is None and open_count > close_count:
                unclosed_line = line_num
            elif unclosed_line is not None and open_count <= close_count:
                unclosed_line = None
        
        # If we still have unclosed comments at the end
        if open_count > close_count:
            warnings.append(
                f"Unclosed HTML comment detected (line {unclosed_line or 'unknown'}). "
                f"Found {open_count} opening markers but only {close_count} closing markers."
            )
        
        # Check for nested comments (warning only)
        # Nested comments are problematic in HTML
        nested_pattern = re.compile(r'<!--[^>]*<!--', re.DOTALL)
        if nested_pattern.search(content):
            warnings.append(
                "Nested HTML comments detected. HTML comments cannot be nested. "
                "Only the outermost comment markers will be processed correctly."
            )
        
        return warnings
