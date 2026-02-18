"""
Placeholder Processor for Handbook Generator

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
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
        todo_warnings: List of TODO value warnings (tracked separately)
    """
    content: str
    replacements: list[Replacement] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    comments_removed: int = 0
    todo_warnings: list[str] = field(default_factory=list)
    
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
    where source is the data source name (e.g., "netbox", "meta-global", "meta-organisation")
    and field is the field path (e.g., "device_name" or "device.name")
    
    Supported sources:
    - netbox: NetBox data source for infrastructure data
    - meta: Meta data source for organization-wide metadata (legacy)
    - meta-global: Global metadata (Handbook Generator version and source)
    - meta-organisation: Organization-specific metadata
    - meta-organisation-roles: Personnel roles and contact information
    - meta-handbook: Individual handbook metadata
    - meta-netbox: NetBox metadata loaded from metadata-netbox.yaml
    - metadata: Legacy metadata source (date, author, version)
    """
    
    # Regex pattern for placeholder detection
    # Matches: {{ source.field }} where field can have dots for nested paths
    # Supports any source name (netbox, meta, metadata, meta-global, meta-organisation, etc.)
    # Source names can contain alphanumeric characters, hyphens, and underscores
    # Must have at least one character for source and field
    PLACEHOLDER_PATTERN = re.compile(r'\{\{\s*([\w-]+)\.(\w+(?:\.\w+)*)\s*\}\}')
    
    # Pattern to detect incomplete/malformed placeholders
    INCOMPLETE_PLACEHOLDER_PATTERN = re.compile(r'\{\{(?!\s*[\w-]+\.[\w.]+\s*\}\})')
    
    def __init__(self, data_sources: Optional[dict] = None, metadata: Optional[dict] = None, unified_metadata: Optional['UnifiedMetadata'] = None):
        """
        Initialize placeholder processor.
        
        Args:
            data_sources: Dictionary of data source adapters (source_name -> adapter) - legacy support
            metadata: Dictionary of metadata values (author, version, date) - legacy support
            unified_metadata: UnifiedMetadata object for new configuration structure
        """
        self.data_sources = data_sources or {}
        self.metadata = metadata or {}
        self.unified_metadata = unified_metadata
    
    def find_placeholders(self, content: str) -> list[Placeholder]:
        """
        Find all placeholders in template content.
        
        Only finds valid placeholders matching the pattern {{ source.field }}.
        Incomplete or malformed placeholders (e.g., just '{{') are ignored.
        
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
    
    def find_incomplete_placeholders(self, content: str) -> list[tuple[int, str]]:
        """
        Find incomplete or malformed placeholders in content.
        
        These are strings that start with '{{' but don't match the valid
        placeholder pattern (e.g., '{{', '{{ invalid', '{{ no.dot.field').
        
        Args:
            content: Template content to scan
            
        Returns:
            List of tuples (line_number, line_content) containing incomplete placeholders
        """
        incomplete = []
        lines = content.split('\n')
        
        for line_idx, line in enumerate(lines, start=1):
            # Check if line contains '{{' 
            if '{{' in line:
                # Find all valid placeholders in this line
                valid_matches = list(self.PLACEHOLDER_PATTERN.finditer(line))
                
                # Create a copy of the line and remove all valid placeholders
                line_copy = line
                for match in valid_matches:
                    line_copy = line_copy.replace(match.group(0), '', 1)
                
                # If there's still '{{' remaining, it's incomplete
                if '{{' in line_copy:
                    incomplete.append((line_idx, line))
        
        return incomplete
    
    def validate_placeholder_line(self, line: str, placeholder: Placeholder) -> Optional[str]:
        """
        Validate that placeholder is the only statement in its line.
        
        Args:
            line: The line containing the placeholder
            placeholder: The placeholder to validate
            
        Returns:
            Warning message if validation fails, None otherwise
        """
        # Remove the placeholder from the line (don't strip yet)
        line_without_placeholder = line.replace(placeholder.raw, '')
        
        # Check if there are any characters that aren't standard whitespace (space, tab) or comma
        # We need to check before stripping because .strip() removes all whitespace including
        # non-standard whitespace like \x85 (NEL - Next Line)
        for c in line_without_placeholder:
            # Allow only space, tab, and comma
            if c not in ' \t,':
                # Any other character (including non-standard whitespace) is content
                context = ErrorContext(
                    line_number=placeholder.line_number,
                    placeholder=placeholder.raw
                )
                return ErrorHandler.placeholder_error(
                    context,
                    "not_alone_in_line"
                )
        
        return None
    
    def replace_placeholder(self, placeholder: Placeholder) -> tuple[Optional[str], Optional[str], Optional[str]]:
        """
        Replace a single placeholder with data from its source.
        
        Routes placeholders to appropriate data source adapters:
        - "metadata" source: Legacy metadata (date, author, version)
        - "meta" source: Organization-wide metadata from metadata.yaml (legacy)
        - "meta-global" source: Global metadata (Handbook Generator version and source)
        - "meta-organisation" source: Organization-specific metadata
        - "meta-organisation-roles" source: Personnel roles and contact information
        - "meta-handbook" source: Individual handbook metadata
        - "netbox" source: NetBox infrastructure data
        - Other sources: Custom data source adapters
        
        Args:
            placeholder: The placeholder to replace
            
        Returns:
            Tuple of (replacement_value, warning_message, todo_warning)
            - replacement_value: The value to replace the placeholder with, or None if not found
            - warning_message: Warning message if replacement failed, or None if successful
            - todo_warning: Warning message if value is "[TODO]", or None otherwise
        """
        # Handle new unified metadata placeholders (meta-global, meta-organisation, meta-organisation-roles, meta-handbook)
        if placeholder.source in ('meta-global', 'meta-organisation', 'meta-organisation-roles', 'meta-handbook'):
            if self.unified_metadata is None:
                context = ErrorContext(
                    line_number=placeholder.line_number,
                    placeholder=placeholder.raw,
                    additional_info=f"Unified metadata placeholders require UnifiedMetadata configuration"
                )
                warning = ErrorHandler.placeholder_error(
                    context,
                    "unknown_data_source",
                    f"Configure unified metadata to use {placeholder.source} placeholders"
                )
                return None, warning, None
            
            # Build full field path for UnifiedMetadata.get_field()
            full_field_path = f"{placeholder.source}.{placeholder.field}"
            
            try:
                value = self.unified_metadata.get_field(full_field_path)
                
                if value is None:
                    context = ErrorContext(
                        line_number=placeholder.line_number,
                        placeholder=placeholder.raw,
                        additional_info=f"Field: {full_field_path}"
                    )
                    warning = ErrorHandler.placeholder_error(
                        context,
                        "field_not_found"
                    )
                    return None, warning, None
                
                # Check if value is [TODO]
                value_str = str(value)
                todo_warning = None
                if value_str == "[TODO]":
                    todo_warning = (
                        f"Line {placeholder.line_number}: Placeholder '{placeholder.raw}' "
                        f"has TODO value. Field '{full_field_path}' needs to be configured."
                    )
                
                return value_str, None, todo_warning
            except Exception as e:
                context = ErrorContext(
                    line_number=placeholder.line_number,
                    placeholder=placeholder.raw,
                    additional_info=str(e)
                )
                warning = ErrorHandler.placeholder_error(
                    context,
                    "adapter_error"
                )
                return None, warning, None
        
        # Handle legacy metadata placeholders (date, author, version)
        if placeholder.source == 'metadata':
            return self._replace_metadata_placeholder(placeholder)
        
        # Route handbook placeholders to meta adapter
        # {{ handbook.version }} should be handled by meta adapter as "handbook.version"
        if placeholder.source == 'handbook':
            if 'meta' not in self.data_sources:
                context = ErrorContext(
                    line_number=placeholder.line_number,
                    placeholder=placeholder.raw,
                    additional_info="Handbook placeholders require 'meta' data source"
                )
                warning = ErrorHandler.placeholder_error(
                    context,
                    "unknown_data_source",
                    "Configure 'meta' data source to use handbook placeholders"
                )
                return None, warning, None
            
            # Route to meta adapter with full field path
            adapter = self.data_sources['meta']
            full_field_path = f"handbook.{placeholder.field}"
            try:
                value = adapter.get_field(full_field_path)
                
                if value is None:
                    context = ErrorContext(
                        line_number=placeholder.line_number,
                        placeholder=placeholder.raw,
                        additional_info=f"Field: {full_field_path}"
                    )
                    warning = ErrorHandler.placeholder_error(
                        context,
                        "field_not_found"
                    )
                    return None, warning, None
                
                return str(value), None, None
            except Exception as e:
                context = ErrorContext(
                    line_number=placeholder.line_number,
                    placeholder=placeholder.raw,
                    additional_info=str(e)
                )
                warning = ErrorHandler.placeholder_error(
                    context,
                    "adapter_error"
                )
                return None, warning, None
        
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
            return None, warning, None
        
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
                return None, warning, None
            
            return str(value), None, None
            
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
            return None, warning, None
    
    def _replace_metadata_placeholder(self, placeholder: Placeholder) -> tuple[Optional[str], Optional[str], Optional[str]]:
        """
        Replace a metadata placeholder with appropriate value.
        
        Handles special metadata fields:
        - date: Current date in ISO format (YYYY-MM-DD)
        - author: Author information from metadata
        - version: Version number from metadata (fallback to "1.0.0")
        
        Args:
            placeholder: The metadata placeholder to replace
            
        Returns:
            Tuple of (replacement_value, warning_message, todo_warning)
        """
        field = placeholder.field
        
        # Handle date field - always use current date in ISO format
        if field == 'date':
            current_date = datetime.now().strftime('%Y-%m-%d')
            return current_date, None, None
        
        # Handle author field
        if field == 'author':
            author = self.metadata.get('author', 'Andreas Huemmer [andreas.huemmer@adminsend.de]')
            return author, None, None
        
        # Handle version field with fallback
        if field == 'version':
            # Import version from package
            from . import __version__
            version = self.metadata.get('version', __version__)
            return version, None, None
        
        # Unknown metadata field
        warning = (
            f"Line {placeholder.line_number}: Unknown metadata field '{field}' "
            f"in placeholder '{placeholder.raw}'. Available metadata fields: "
            f"date, author, version"
        )
        return None, warning, None
    
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
        
        # Edge case: After comment removal, check if content is empty or only whitespace
        if not template_content.strip():
            # Content was only comments, return early
            return result
        
        # Step 2: Find all placeholders
        placeholders = self.find_placeholders(template_content)
        
        # Check for incomplete/malformed placeholders
        incomplete = self.find_incomplete_placeholders(template_content)
        if incomplete:
            for line_num, line in incomplete:
                warning = (
                    f"Line {line_num}: Found incomplete or malformed placeholder. "
                    f"Valid format is: {{{{ source.field }}}}. "
                    f"Line content: {line.strip()[:50]}"
                )
                if template_name:
                    warning = f"{template_name}: {warning}"
                result.warnings.append(warning)
        
        # If no valid placeholders, return content with comments removed
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
            replacement_value, warning, todo_warning = self.replace_placeholder(placeholder)
            
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
                
                # Add TODO warning to separate list if present
                if todo_warning:
                    if template_name:
                        todo_warning = f"{template_name}: {todo_warning}"
                    result.todo_warnings.append(todo_warning)
            elif warning:
                if template_name:
                    warning = f"{template_name}: {warning}"
                result.warnings.append(warning)
        
        # Reconstruct content
        result.content = '\n'.join(lines)
        
        return result
