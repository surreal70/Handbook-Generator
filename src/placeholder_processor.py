"""
Placeholder Processor for Handbook Generator

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime
from pathlib import Path
import re
from src.error_handler import ErrorHandler, ErrorContext
from src.html_comment_processor import HTMLCommentProcessor


@dataclass
class Placeholder:
    """
    Represents a placeholder found in a template.
    
    Attributes:
        raw: Original placeholder string (e.g., "{{ netbox.device_name }}")
        source: Data source name (e.g., "netbox")
        field: Field path (e.g., "device_name" or "device.name")
        line_number: Line number where placeholder was found (1-indexed)
    """
    raw: str
    source: str
    field: str
    line_number: int
    
    @classmethod
    def parse(cls, match: re.Match, line_number: int) -> 'Placeholder':
        """
        Parse placeholder from regex match.
        
        Args:
            match: Regex match object containing placeholder groups
            line_number: Line number where placeholder was found
            
        Returns:
            Placeholder object
        """
        raw = match.group(0)
        source = match.group(1)
        field = match.group(2)
        
        return cls(
            raw=raw,
            source=source,
            field=field,
            line_number=line_number
        )


@dataclass
class Replacement:
    """
    Represents a successful placeholder replacement.
    
    Attributes:
        placeholder: Original placeholder string
        value: Replacement value
        source: Data source name
        line_number: Line number where replacement occurred
    """
    placeholder: str
    value: str
    source: str
    line_number: int


@dataclass
class ProcessingResult:
    """
    Result of processing a template.
    
    Attributes:
        content: Processed template content with replacements applied
        replacements: List of successful replacements
        warnings: List of warning messages
        errors: List of error messages
        comments_removed: Number of HTML comments removed
    """
    content: str
    replacements: list[Replacement] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    comments_removed: int = 0
    
    def get_replacement_count_by_source(self, source: str) -> int:
        """
        Get count of replacements for a specific source.
        
        Args:
            source: Data source name (e.g., "netbox", "meta", "metadata")
            
        Returns:
            Number of replacements from that source
        """
        return sum(1 for r in self.replacements if r.source == source)
    
    def get_sources_used(self) -> set[str]:
        """
        Get set of all data sources that had successful replacements.
        
        Returns:
            Set of source names
        """
        return {r.source for r in self.replacements}
    
    def get_statistics_summary(self) -> dict[str, int]:
        """
        Get summary statistics of replacements by source.
        
        Returns:
            Dictionary mapping source names to replacement counts
        """
        stats = {}
        for source in self.get_sources_used():
            stats[source] = self.get_replacement_count_by_source(source)
        return stats


class PlaceholderProcessor:
    """
    Processes templates to detect and replace placeholders.
    
    Placeholders follow the format: {{ source.field }}
    where source is the data source name (e.g., "netbox", "meta")
    and field is the field path (e.g., "device_name" or "device.name")
    
    Supported sources:
    - netbox: NetBox data source for infrastructure data
    - meta: Meta data source for organization-wide metadata
    - metadata: Legacy metadata source (date, author, version)
    """
    
    # Regex pattern for placeholder detection
    # Matches: {{ source.field }} where field can have dots for nested paths
    # Supports any source name (netbox, meta, metadata, etc.)
    PLACEHOLDER_PATTERN = re.compile(r'\{\{\s*(\w+)\.(\w+(?:\.\w+)*)\s*\}\}')
    
    def __init__(self, data_sources: Optional[dict] = None, metadata: Optional[dict] = None):
        """
        Initialize placeholder processor.
        
        Args:
            data_sources: Dictionary of data source adapters (source_name -> adapter)
            metadata: Dictionary of metadata values (author, version, date)
        """
        self.data_sources = data_sources or {}
        self.metadata = metadata or {}
    
    def find_placeholders(self, content: str) -> list[Placeholder]:
        """
        Find all placeholders in template content.
        
        Args:
            content: Template content to scan
            
        Returns:
            List of Placeholder objects found in content
        """
        placeholders = []
        lines = content.split('\n')
        
        for line_idx, line in enumerate(lines, start=1):
            # Find all placeholder matches in this line
            for match in self.PLACEHOLDER_PATTERN.finditer(line):
                placeholder = Placeholder.parse(match, line_idx)
                placeholders.append(placeholder)
        
        return placeholders
    
    def validate_placeholder_line(self, line: str, placeholder: Placeholder) -> Optional[str]:
        """
        Validate that placeholder is the only statement in its line.
        
        Args:
            line: The line containing the placeholder
            placeholder: The placeholder to validate
            
        Returns:
            Warning message if validation fails, None otherwise
        """
        # Remove the placeholder from the line
        line_without_placeholder = line.replace(placeholder.raw, '').strip()
        
        # If there's any non-whitespace content left, the placeholder is not alone
        if line_without_placeholder:
            context = ErrorContext(
                line_number=placeholder.line_number,
                placeholder=placeholder.raw
            )
            return ErrorHandler.placeholder_error(
                context,
                "not_alone_in_line"
            )
        
        return None
    
    def replace_placeholder(self, placeholder: Placeholder) -> tuple[Optional[str], Optional[str]]:
        """
        Replace a single placeholder with data from its source.
        
        Routes placeholders to appropriate data source adapters:
        - "metadata" source: Legacy metadata (date, author, version)
        - "meta" source: Organization-wide metadata from metadata.yaml
        - "netbox" source: NetBox infrastructure data
        - Other sources: Custom data source adapters
        
        Args:
            placeholder: The placeholder to replace
            
        Returns:
            Tuple of (replacement_value, warning_message)
            - replacement_value: The value to replace the placeholder with, or None if not found
            - warning_message: Warning message if replacement failed, or None if successful
        """
        # Handle legacy metadata placeholders (date, author, version)
        if placeholder.source == 'metadata':
            return self._replace_metadata_placeholder(placeholder)
        
        # Check if data source is available (handles both "meta" and "netbox" sources)
        if placeholder.source not in self.data_sources:
            available_sources = ', '.join(self.data_sources.keys()) if self.data_sources else 'none'
            context = ErrorContext(
                line_number=placeholder.line_number,
                placeholder=placeholder.raw,
                additional_info=f"Available sources: {available_sources}"
            )
            warning = ErrorHandler.placeholder_error(
                context,
                "unknown_data_source",
                f"Check your configuration file and ensure '{placeholder.source}' is configured"
            )
            return None, warning
        
        # Get data from source adapter (unified handling for all sources)
        adapter = self.data_sources[placeholder.source]
        try:
            value = adapter.get_field(placeholder.field)
            
            if value is None:
                context = ErrorContext(
                    line_number=placeholder.line_number,
                    placeholder=placeholder.raw,
                    additional_info=f"Data source: {placeholder.source}, Field: {placeholder.field}"
                )
                warning = ErrorHandler.placeholder_error(
                    context,
                    "field_not_found"
                )
                return None, warning
            
            return str(value), None
            
        except Exception as e:
            context = ErrorContext(
                line_number=placeholder.line_number,
                placeholder=placeholder.raw,
                additional_info=str(e)
            )
            warning = ErrorHandler.placeholder_error(
                context,
                "data_retrieval_error",
                "Check the field name and data source connection"
            )
            return None, warning
    
    def _replace_metadata_placeholder(self, placeholder: Placeholder) -> tuple[Optional[str], Optional[str]]:
        """
        Replace a metadata placeholder with appropriate value.
        
        Handles special metadata fields:
        - date: Current date in ISO format (YYYY-MM-DD)
        - author: Author information from metadata
        - version: Version number from metadata (fallback to "1.0.0")
        
        Args:
            placeholder: The metadata placeholder to replace
            
        Returns:
            Tuple of (replacement_value, warning_message)
        """
        field = placeholder.field
        
        # Handle date field - always use current date in ISO format
        if field == 'date':
            current_date = datetime.now().strftime('%Y-%m-%d')
            return current_date, None
        
        # Handle author field
        if field == 'author':
            author = self.metadata.get('author', 'Andreas Huemmer [andreas.huemmer@adminsend.de]')
            return author, None
        
        # Handle version field with fallback
        if field == 'version':
            # Import version from package
            from . import __version__
            version = self.metadata.get('version', __version__)
            return version, None
        
        # Unknown metadata field
        warning = (
            f"Line {placeholder.line_number}: Unknown metadata field '{field}' "
            f"in placeholder '{placeholder.raw}'. Available metadata fields: "
            f"date, author, version"
        )
        return None, warning
    
    def process_template(self, template_content: str, template_name: str = "") -> ProcessingResult:
        """
        Process template and replace all placeholders.
        
        Processing steps:
        1. Remove HTML comments
        2. Find placeholders
        3. Validate and replace placeholders
        
        Args:
            template_content: Template content to process
            template_name: Optional template name for better error messages
            
        Returns:
            ProcessingResult with processed content and metadata
        """
        result = ProcessingResult(content=template_content)
        
        # Edge case: Empty template content
        if not template_content or not template_content.strip():
            if template_name:
                result.warnings.append(
                    f"{template_name}: Template is empty or contains only whitespace"
                )
            return result
        
        # Step 1: Remove HTML comments before placeholder processing
        comment_processor = HTMLCommentProcessor()
        
        # Count comments before removal
        comments_before = template_content.count('<!--')
        
        # Remove comments
        template_content = comment_processor.remove_comments(template_content)
        
        # Count comments after removal (should be 0)
        comments_after = template_content.count('<!--')
        
        # Update statistics
        result.comments_removed = comments_before - comments_after
        
        # Validate comments and add warnings
        comment_warnings = comment_processor.validate_comments(template_content)
        for warning in comment_warnings:
            if template_name:
                warning = f"{template_name}: {warning}"
            result.warnings.append(warning)
        
        # Update result content with comments removed
        result.content = template_content
        
        # Step 2: Find all placeholders
        placeholders = self.find_placeholders(template_content)
        
        # If no placeholders, return content with comments removed
        if not placeholders:
            return result
        
        # Step 3: Validate and replace placeholders
        lines = template_content.split('\n')
        
        for placeholder in placeholders:
            line_idx = placeholder.line_number - 1  # Convert to 0-indexed
            
            # Edge case: Line number out of range (shouldn't happen, but defensive)
            if line_idx < 0 or line_idx >= len(lines):
                warning = f"Internal error: Line number {placeholder.line_number} out of range"
                if template_name:
                    warning = f"{template_name}: {warning}"
                result.warnings.append(warning)
                continue
            
            line = lines[line_idx]
            
            # Validate placeholder placement
            validation_warning = self.validate_placeholder_line(line, placeholder)
            if validation_warning:
                if template_name:
                    validation_warning = f"{template_name}: {validation_warning}"
                result.warnings.append(validation_warning)
            
            # Attempt replacement
            replacement_value, warning = self.replace_placeholder(placeholder)
            
            if replacement_value is not None:
                # Replace placeholder in the line
                lines[line_idx] = line.replace(placeholder.raw, replacement_value)
                
                # Record successful replacement
                result.replacements.append(Replacement(
                    placeholder=placeholder.raw,
                    value=replacement_value,
                    source=placeholder.source,
                    line_number=placeholder.line_number
                ))
            elif warning:
                if template_name:
                    warning = f"{template_name}: {warning}"
                result.warnings.append(warning)
        
        # Reconstruct content
        result.content = '\n'.join(lines)
        
        return result
