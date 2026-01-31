"""
Error Handler for Handbook Generator

Provides structured error messages with context and resolution suggestions.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

from dataclasses import dataclass
from typing import Optional
from pathlib import Path


@dataclass
class ErrorContext:
    """
    Context information for an error.
    
    Attributes:
        file_path: Path to the file where error occurred
        line_number: Line number where error occurred (1-indexed)
        placeholder: Placeholder that caused the error (if applicable)
        additional_info: Any additional context information
    """
    file_path: Optional[Path] = None
    line_number: Optional[int] = None
    placeholder: Optional[str] = None
    additional_info: Optional[str] = None


class ErrorHandler:
    """
    Provides structured error messages with context and resolution suggestions.
    
    Follows requirements 12.1-12.4 for clear, actionable error messages.
    """
    
    @staticmethod
    def template_not_found_error(
        language: str,
        template_type: str,
        expected_path: Path,
        available_languages: list[str],
        available_types: dict[str, list[str]]
    ) -> str:
        """
        Generate error message for missing template directory.
        
        Args:
            language: Requested language
            template_type: Requested template type
            expected_path: Expected path where templates should be
            available_languages: List of available languages
            available_types: Dictionary of available types per language
            
        Returns:
            Formatted error message with suggestions
        """
        message = f"Template directory not found: {expected_path}\n"
        message += f"\nRequested: language='{language}', type='{template_type}'\n"
        
        if available_languages:
            message += f"\nAvailable languages: {', '.join(available_languages)}"
            
            if language in available_types and available_types[language]:
                message += f"\nAvailable types for '{language}': {', '.join(available_types[language])}"
            elif language not in available_languages:
                message += f"\n\nSuggestion: Language '{language}' is not available. "
                message += f"Try one of: {', '.join(available_languages)}"
        else:
            message += "\nNo templates found in the templates directory."
            message += f"\n\nExpected structure: templates/{language}/{template_type}/"
        
        return message
    
    @staticmethod
    def api_connection_error(
        source_name: str,
        url: str,
        status_code: Optional[int] = None,
        error_message: Optional[str] = None
    ) -> str:
        """
        Generate error message for API connection failures.
        
        Args:
            source_name: Name of the data source (e.g., "netbox")
            url: API URL that failed
            status_code: HTTP status code (if applicable)
            error_message: Detailed error message
            
        Returns:
            Formatted error message with troubleshooting suggestions
        """
        message = f"Failed to connect to {source_name} API\n"
        message += f"URL: {url}\n"
        
        if status_code:
            message += f"Status Code: {status_code}\n"
            
            # Provide specific suggestions based on status code
            if status_code == 401:
                message += "\nCause: Authentication failed"
                message += "\nSuggestion: Check your API token in the configuration file"
                message += "\n  - Verify the token is correct and not expired"
                message += "\n  - Ensure the token has appropriate permissions"
            elif status_code == 403:
                message += "\nCause: Access forbidden"
                message += "\nSuggestion: Your API token does not have sufficient permissions"
                message += "\n  - Contact your administrator to grant necessary permissions"
            elif status_code == 404:
                message += "\nCause: API endpoint not found"
                message += "\nSuggestion: Check the API URL in your configuration"
                message += "\n  - Verify the URL is correct and includes the API path"
                message += f"\n  - Example: https://netbox.example.com/api/"
            elif status_code >= 500:
                message += "\nCause: Server error"
                message += "\nSuggestion: The API server is experiencing issues"
                message += "\n  - Try again later"
                message += "\n  - Contact your administrator if the problem persists"
            else:
                message += f"\nHTTP Error: {status_code}"
        
        if error_message:
            message += f"\nDetails: {error_message}"
        
        message += "\n\nTroubleshooting steps:"
        message += "\n  1. Verify the API URL is correct and accessible"
        message += "\n  2. Check your API token is valid"
        message += "\n  3. Ensure network connectivity to the API server"
        message += "\n  4. Check firewall rules and proxy settings"
        
        return message
    
    @staticmethod
    def placeholder_error(
        context: ErrorContext,
        error_type: str,
        suggestion: Optional[str] = None
    ) -> str:
        """
        Generate error message for placeholder-related errors.
        
        Args:
            context: Error context with file, line, and placeholder info
            error_type: Type of error (e.g., "field_not_found", "invalid_format")
            suggestion: Optional suggestion for resolution
            
        Returns:
            Formatted error message with context and suggestions
        """
        message = f"Placeholder error: {error_type}\n"
        
        if context.file_path:
            message += f"File: {context.file_path}\n"
        
        if context.line_number:
            message += f"Line: {context.line_number}\n"
        
        if context.placeholder:
            message += f"Placeholder: {context.placeholder}\n"
        
        if context.additional_info:
            message += f"Details: {context.additional_info}\n"
        
        if suggestion:
            message += f"\nSuggestion: {suggestion}"
        else:
            # Provide default suggestions based on error type
            if error_type == "field_not_found":
                message += "\nSuggestion: Verify the field name is correct"
                message += "\n  - Check the data source documentation for available fields"
                message += "\n  - Ensure the field exists in the data source"
            elif error_type == "invalid_format":
                message += "\nSuggestion: Check placeholder format"
                message += "\n  - Correct format: {{ source.field }}"
                message += "\n  - Example: {{ netbox.device_name }}"
            elif error_type == "not_alone_in_line":
                message += "\nSuggestion: Place placeholder on its own line"
                message += "\n  - Placeholders must be the only content on their line"
                message += "\n  - Remove any text before or after the placeholder"
        
        return message
    
    @staticmethod
    def configuration_error(
        config_path: Path,
        missing_fields: list[str],
        invalid_fields: dict[str, str]
    ) -> str:
        """
        Generate error message for configuration errors.
        
        Args:
            config_path: Path to configuration file
            missing_fields: List of required fields that are missing
            invalid_fields: Dictionary of invalid fields and their issues
            
        Returns:
            Formatted error message with resolution steps
        """
        message = f"Configuration error in: {config_path}\n"
        
        if missing_fields:
            message += f"\nMissing required fields:"
            for field in missing_fields:
                message += f"\n  - {field}"
        
        if invalid_fields:
            message += f"\nInvalid fields:"
            for field, issue in invalid_fields.items():
                message += f"\n  - {field}: {issue}"
        
        message += "\n\nSuggestion: Update your configuration file"
        message += "\n  1. Open the configuration file"
        message += f"\n  2. Add or correct the fields listed above"
        message += "\n  3. Refer to config.example.yaml for the correct format"
        
        if missing_fields:
            message += "\n\nExample configuration:"
            message += "\ndata_sources:"
            if "netbox_url" in missing_fields or "netbox_api_token" in missing_fields:
                message += "\n  netbox:"
                message += "\n    url: \"https://netbox.example.com/api/\""
                message += "\n    api_token: \"your-api-token-here\""
        
        return message
    
    @staticmethod
    def empty_template_directory_error(template_path: Path) -> str:
        """
        Generate error message for empty template directories.
        
        Args:
            template_path: Path to the empty template directory
            
        Returns:
            Formatted error message with suggestions
        """
        message = f"Template directory is empty: {template_path}\n"
        message += "\nNo template files (*.md) found in the directory."
        message += "\n\nSuggestion: Add template files to the directory"
        message += "\n  1. Create markdown files with .md extension"
        message += "\n  2. Use 4-digit prefixes for ordering (e.g., 0100_introduction.md)"
        message += "\n  3. Add a metadata template: 0000_metadata_[language]_[type].md"
        message += "\n\nExample structure:"
        message += f"\n  {template_path}/"
        message += "\n    0000_metadata_de_backup.md"
        message += "\n    0100_einleitung.md"
        message += "\n    0200_backup_strategie.md"
        
        return message
    
    @staticmethod
    def invalid_filename_warning(file_path: Path, reason: str) -> str:
        """
        Generate warning message for invalid template filenames.
        
        Args:
            file_path: Path to the file with invalid name
            reason: Reason why the filename is invalid
            
        Returns:
            Formatted warning message
        """
        message = f"Invalid template filename: {file_path.name}\n"
        message += f"Reason: {reason}\n"
        message += "\nSuggestion: Rename the file to follow naming conventions"
        message += "\n  - Content templates: NNNN_name.md (e.g., 0100_introduction.md)"
        message += "\n  - Metadata templates: 0000_metadata_[language]_[type].md"
        message += "\n\nNote: This template will be processed last in the order."
        
        return message
