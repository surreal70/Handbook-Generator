"""
HTML Comment Processor for Handbook Generator

Processes templates to remove HTML-style comments before placeholder processing.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

import re
from typing import Optional


class HTMLCommentProcessor:
    """
    Processes templates to remove HTML comments.
    
    HTML comments follow the format: <!-- comment -->
    Comments can span single or multiple lines.
    """
    
    # Regex pattern for HTML comment detection
    # Matches: <!-- ... --> with DOTALL flag for multiline support
    # Non-greedy match (.*?) to handle multiple comments correctly
    COMMENT_PATTERN = re.compile(r'<!--.*?-->', re.DOTALL)
    
    # Pattern for detecting unclosed comments
    UNCLOSED_COMMENT_PATTERN = re.compile(r'<!--(?!.*?-->)', re.DOTALL)
    
    def remove_comments(self, content: str) -> str:
        """
        Remove all HTML comments from content.
        
        Handles:
        - Single-line comments: <!-- comment -->
        - Multi-line comments: <!-- 
                                  comment
                                  -->
        - Empty comments: <!-- -->
        - Comments with special characters
        
        Preserves:
        - Surrounding markdown content
        - Whitespace and formatting
        
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
        cleaned_content = self.COMMENT_PATTERN.sub('', content)
        
        return cleaned_content
    
    def validate_comments(self, content: str) -> list[str]:
        """
        Validate HTML comments for common issues.
        
        Checks for:
        - Unclosed comments (<!-- without -->)
        - Nested comments (warning only, as HTML doesn't support nesting)
        
        Args:
            content: Template content to validate
            
        Returns:
            List of validation warnings
        """
        warnings = []
        
        if not content:
            return warnings
        
        # Check for unclosed comments
        # Look for <!-- that doesn't have a corresponding -->
        lines = content.split('\n')
        open_comment_line = None
        
        for line_num, line in enumerate(lines, start=1):
            # Count opening and closing markers in this line
            opens = line.count('<!--')
            closes = line.count('-->')
            
            # Track if we're in an open comment
            if open_comment_line is None:
                if opens > closes:
                    open_comment_line = line_num
            else:
                if closes > 0:
                    open_comment_line = None
        
        # If we still have an open comment at the end, it's unclosed
        if open_comment_line is not None:
            warnings.append(
                f"Unclosed HTML comment detected starting at line {open_comment_line}. "
                f"Ensure all comments have closing -->"
            )
        
        # Check for nested comments (warning only)
        # Nested comments are when we have <!-- inside a comment
        # This is a simplified check - looks for multiple <!-- before a -->
        nested_pattern = re.compile(r'<!--[^>]*<!--', re.DOTALL)
        if nested_pattern.search(content):
            warnings.append(
                "Nested HTML comments detected. HTML comments cannot be nested. "
                "Only the outermost comment markers will be processed."
            )
        
        return warnings
