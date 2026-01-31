"""
Logger for Handbook Generator

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

from dataclasses import dataclass, field
from typing import Optional
import sys
import time


@dataclass
class Statistics:
    """
    Processing statistics for handbook generation.
    
    Attributes:
        documents_processed: Number of templates processed
        placeholders_replaced: Number of successful placeholder replacements
        placeholders_failed: Number of failed placeholder replacements
        total_words: Total word count in output
        output_size_bytes: Size of output file(s) in bytes
        processing_time_seconds: Total processing time in seconds
    """
    documents_processed: int = 0
    placeholders_replaced: int = 0
    placeholders_failed: int = 0
    total_words: int = 0
    output_size_bytes: int = 0
    processing_time_seconds: float = 0.0


class StatisticsCalculator:
    """
    Helper class to calculate statistics from processing results.
    """
    
    @staticmethod
    def calculate_word_count(content: str) -> int:
        """
        Calculate word count in content.
        
        Args:
            content: Text content to count words in
            
        Returns:
            Number of words
        """
        if not content:
            return 0
        # Split on whitespace and count non-empty strings
        return len([word for word in content.split() if word.strip()])
    
    @staticmethod
    def calculate_statistics(
        processed_results: list,
        output_content: str,
        output_size_bytes: int,
        processing_time: float
    ) -> Statistics:
        """
        Calculate comprehensive statistics from processing results.
        
        Args:
            processed_results: List of ProcessingResult objects
            output_content: Final assembled output content
            output_size_bytes: Size of output file(s) in bytes
            processing_time: Processing time in seconds
            
        Returns:
            Statistics object with all metrics
        """
        stats = Statistics()
        
        # Count documents processed
        stats.documents_processed = len(processed_results)
        
        # Count replacements and failures
        for result in processed_results:
            stats.placeholders_replaced += len(result.replacements)
            # Count warnings related to placeholder failures
            # (warnings about missing fields or unknown sources)
            for warning in result.warnings:
                if 'not found' in warning.lower() or 'unknown data source' in warning.lower():
                    stats.placeholders_failed += 1
        
        # Calculate word count
        stats.total_words = StatisticsCalculator.calculate_word_count(output_content)
        
        # Set output size and processing time
        stats.output_size_bytes = output_size_bytes
        stats.processing_time_seconds = processing_time
        
        return stats


class HandbookLogger:
    """
    Structured logger for handbook generation with normal and verbose modes.
    
    Provides consistent logging output with support for:
    - Normal mode: High-level progress and statistics
    - Verbose mode: Detailed placeholder replacements and extended error information
    """
    
    def __init__(self, verbose: bool = False):
        """
        Initialize logger with verbosity level.
        
        Args:
            verbose: Enable verbose logging mode
        """
        self.verbose = verbose
        self._start_time: Optional[float] = None
    
    def start_processing(self) -> None:
        """Start processing timer."""
        self._start_time = time.time()
    
    def get_elapsed_time(self) -> float:
        """
        Get elapsed processing time.
        
        Returns:
            Elapsed time in seconds, or 0.0 if not started
        """
        if self._start_time is None:
            return 0.0
        return time.time() - self._start_time
    
    def log_processing(self, template_name: str) -> None:
        """
        Log template processing (normal level).
        
        Args:
            template_name: Name of template being processed
        """
        print(f"Processing: {template_name}")
    
    def log_replacement(self, replacement) -> None:
        """
        Log placeholder replacement (verbose level only).
        
        Args:
            replacement: Replacement object with placeholder, value, source, line_number
        """
        if self.verbose:
            print(
                f"  [Line {replacement.line_number}] "
                f"Replaced '{replacement.placeholder}' "
                f"with '{replacement.value}' "
                f"from source '{replacement.source}'"
            )
    
    def log_replacements_summary(self, replacements: list, template_name: str) -> None:
        """
        Log summary of all replacements for a template (verbose level only).
        
        Args:
            replacements: List of Replacement objects
            template_name: Name of the template
        """
        if self.verbose and replacements:
            print(f"  → {len(replacements)} placeholder(s) replaced in {template_name}")
    
    def log_statistics(self, stats: Statistics) -> None:
        """
        Log processing statistics (normal level).
        
        Args:
            stats: Statistics object with processing metrics
        """
        print("\n" + "=" * 60)
        print("Processing Statistics")
        print("=" * 60)
        print(f"Documents processed:      {stats.documents_processed}")
        print(f"Placeholders replaced:    {stats.placeholders_replaced}")
        print(f"Placeholders failed:      {stats.placeholders_failed}")
        print(f"Total words:              {stats.total_words:,}")
        print(f"Output size:              {stats.output_size_bytes:,} bytes "
              f"({stats.output_size_bytes / 1024:.2f} KB)")
        print(f"Processing time:          {stats.processing_time_seconds:.2f} seconds")
        print("=" * 60)
    
    def log_warning(self, message: str, verbose_details: Optional[str] = None) -> None:
        """
        Log warning message with optional verbose details.
        
        In normal mode: Shows only the main warning message
        In verbose mode: Shows warning message plus additional details
        
        Args:
            message: Warning message
            verbose_details: Additional details shown only in verbose mode
        """
        print(f"WARNING: {message}", file=sys.stderr)
        if self.verbose and verbose_details:
            print(f"  Details: {verbose_details}", file=sys.stderr)
    
    def log_error(self, message: str, verbose_details: Optional[str] = None) -> None:
        """
        Log error message with optional verbose details.
        
        In normal mode: Shows only the main error message
        In verbose mode: Shows error message plus additional details (e.g., stack traces)
        
        Args:
            message: Error message
            verbose_details: Additional details shown only in verbose mode
        """
        print(f"ERROR: {message}", file=sys.stderr)
        if self.verbose and verbose_details:
            print(f"  Details: {verbose_details}", file=sys.stderr)
    
    def log_info(self, message: str) -> None:
        """
        Log informational message (normal level).
        
        Args:
            message: Info message
        """
        print(message)
    
    def log_verbose(self, message: str) -> None:
        """
        Log message only in verbose mode.
        
        Args:
            message: Verbose message
        """
        if self.verbose:
            print(message)
    
    def log_summary(self, warnings: list[str], errors: list[str]) -> None:
        """
        Log summary of all warnings and errors.
        
        Args:
            warnings: List of warning messages
            errors: List of error messages
        """
        if not warnings and not errors:
            print("\n✓ Processing completed successfully with no warnings or errors.")
            return
        
        print("\n" + "=" * 60)
        print("Processing Summary")
        print("=" * 60)
        
        if errors:
            print(f"\nErrors ({len(errors)}):")
            for i, error in enumerate(errors, start=1):
                print(f"  {i}. {error}")
        
        if warnings:
            print(f"\nWarnings ({len(warnings)}):")
            for i, warning in enumerate(warnings, start=1):
                print(f"  {i}. {warning}")
        
        print("=" * 60)
