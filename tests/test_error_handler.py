"""
Tests for Error Handler

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2026
"""

import pytest
from pathlib import Path
from src.error_handler import ErrorHandler, ErrorContext


@pytest.mark.unit
def test_template_not_found_error():
    """
    Test für Template-nicht-gefunden-Fehler
    
    Requirements: 12.2
    """
    language = 'de'
    template_type = 'backup'
    expected_path = Path('templates/de/backup')
    available_languages = ['de', 'en']
    available_types = {'de': ['bcm', 'isms'], 'en': ['backup']}
    
    error_msg = ErrorHandler.template_not_found_error(
        language, template_type, expected_path,
        available_languages, available_types
    )
    
    # Verify error message contains key information
    assert 'Template directory not found' in error_msg
    assert str(expected_path) in error_msg
    assert language in error_msg
    assert template_type in error_msg
    
    # Verify available options are listed
    assert 'Available languages' in error_msg
    assert 'de' in error_msg
    assert 'en' in error_msg
    
    # Verify suggestion is provided
    assert 'Suggestion' in error_msg or 'Available types' in error_msg


@pytest.mark.unit
def test_template_not_found_error_no_templates():
    """
    Test für Template-nicht-gefunden-Fehler wenn keine Templates existieren
    
    Requirements: 12.2
    """
    language = 'de'
    template_type = 'backup'
    expected_path = Path('templates/de/backup')
    available_languages = []
    available_types = {}
    
    error_msg = ErrorHandler.template_not_found_error(
        language, template_type, expected_path,
        available_languages, available_types
    )
    
    # Verify error message indicates no templates found
    assert 'No templates found' in error_msg
    assert 'Expected structure' in error_msg


@pytest.mark.unit
def test_api_connection_error_401():
    """
    Test für API-Verbindungsfehler mit 401 (Authentication)
    
    Requirements: 12.3
    """
    source_name = 'netbox'
    url = 'https://netbox.example.com'
    status_code = 401
    error_message = 'Invalid token'
    
    error_msg = ErrorHandler.api_connection_error(
        source_name, url, status_code, error_message
    )
    
    # Verify error message contains key information
    assert 'Failed to connect' in error_msg
    assert source_name in error_msg
    assert url in error_msg
    assert '401' in error_msg
    
    # Verify specific suggestion for 401
    assert 'Authentication failed' in error_msg
    assert 'API token' in error_msg or 'token' in error_msg
    
    # Verify troubleshooting steps are provided
    assert 'Troubleshooting' in error_msg


@pytest.mark.unit
def test_api_connection_error_403():
    """
    Test für API-Verbindungsfehler mit 403 (Forbidden)
    
    Requirements: 12.3
    """
    error_msg = ErrorHandler.api_connection_error(
        'netbox', 'https://netbox.example.com', 403, 'Forbidden'
    )
    
    assert '403' in error_msg
    assert 'Access forbidden' in error_msg or 'forbidden' in error_msg.lower()
    assert 'permissions' in error_msg.lower()


@pytest.mark.unit
def test_api_connection_error_404():
    """
    Test für API-Verbindungsfehler mit 404 (Not Found)
    
    Requirements: 12.3
    """
    error_msg = ErrorHandler.api_connection_error(
        'netbox', 'https://netbox.example.com', 404, 'Not found'
    )
    
    assert '404' in error_msg
    assert 'not found' in error_msg.lower()
    assert 'URL' in error_msg or 'url' in error_msg


@pytest.mark.unit
def test_api_connection_error_500():
    """
    Test für API-Verbindungsfehler mit 500 (Server Error)
    
    Requirements: 12.3
    """
    error_msg = ErrorHandler.api_connection_error(
        'netbox', 'https://netbox.example.com', 500, 'Internal server error'
    )
    
    assert '500' in error_msg
    assert 'Server error' in error_msg or 'server' in error_msg.lower()
    assert 'Try again' in error_msg or 'later' in error_msg


@pytest.mark.unit
def test_api_connection_error_no_status_code():
    """
    Test für API-Verbindungsfehler ohne Status Code
    
    Requirements: 12.3
    """
    error_msg = ErrorHandler.api_connection_error(
        'netbox', 'https://netbox.example.com', None, 'Connection timeout'
    )
    
    assert 'Failed to connect' in error_msg
    assert 'netbox' in error_msg
    assert 'Connection timeout' in error_msg
    assert 'Troubleshooting' in error_msg


@pytest.mark.unit
def test_placeholder_error_field_not_found():
    """
    Test für Platzhalter-Fehler: Feld nicht gefunden
    
    Requirements: 12.4
    """
    context = ErrorContext(
        file_path=Path('templates/de/backup/0100_intro.md'),
        line_number=42,
        placeholder='{{ netbox.device_name }}',
        additional_info='Data source: netbox, Field: device_name'
    )
    
    error_msg = ErrorHandler.placeholder_error(
        context, 'field_not_found'
    )
    
    # Verify error message contains context
    assert 'Placeholder error' in error_msg
    assert 'field_not_found' in error_msg
    assert str(context.file_path) in error_msg
    assert '42' in error_msg
    assert context.placeholder in error_msg
    
    # Verify suggestion is provided
    assert 'Suggestion' in error_msg
    assert 'field name' in error_msg.lower()


@pytest.mark.unit
def test_placeholder_error_invalid_format():
    """
    Test für Platzhalter-Fehler: Ungültiges Format
    
    Requirements: 12.4
    """
    context = ErrorContext(
        file_path=Path('templates/de/backup/0100_intro.md'),
        line_number=15,
        placeholder='{ netbox.device_name }',
    )
    
    error_msg = ErrorHandler.placeholder_error(
        context, 'invalid_format'
    )
    
    # Verify error message contains context
    assert 'invalid_format' in error_msg
    assert '15' in error_msg
    
    # Verify suggestion shows correct format
    assert 'Suggestion' in error_msg
    assert '{{ source.field }}' in error_msg


@pytest.mark.unit
def test_placeholder_error_not_alone_in_line():
    """
    Test für Platzhalter-Fehler: Nicht allein in Zeile
    
    Requirements: 12.4
    """
    context = ErrorContext(
        line_number=20,
        placeholder='{{ netbox.device_name }}'
    )
    
    error_msg = ErrorHandler.placeholder_error(
        context, 'not_alone_in_line'
    )
    
    # Verify suggestion about line placement
    assert 'Suggestion' in error_msg
    assert 'own line' in error_msg.lower()


@pytest.mark.unit
def test_placeholder_error_with_custom_suggestion():
    """
    Test für Platzhalter-Fehler mit benutzerdefiniertem Vorschlag
    
    Requirements: 12.4
    """
    context = ErrorContext(
        line_number=10,
        placeholder='{{ unknown.field }}'
    )
    
    custom_suggestion = 'Check the data source name in your configuration'
    error_msg = ErrorHandler.placeholder_error(
        context, 'unknown_source', custom_suggestion
    )
    
    # Verify custom suggestion is used
    assert custom_suggestion in error_msg


@pytest.mark.unit
def test_configuration_error():
    """
    Test für Konfigurationsfehler
    
    Requirements: 12.1, 12.2
    """
    config_path = Path('config.yaml')
    missing_fields = ['netbox_url', 'netbox_api_token']
    invalid_fields = {'output_format': 'Must be one of: markdown, pdf, both'}
    
    error_msg = ErrorHandler.configuration_error(
        config_path, missing_fields, invalid_fields
    )
    
    # Verify error message contains key information
    assert 'Configuration error' in error_msg
    assert str(config_path) in error_msg
    
    # Verify missing fields are listed
    assert 'Missing required fields' in error_msg
    assert 'netbox_url' in error_msg
    assert 'netbox_api_token' in error_msg
    
    # Verify invalid fields are listed
    assert 'Invalid fields' in error_msg
    assert 'output_format' in error_msg
    
    # Verify suggestion is provided
    assert 'Suggestion' in error_msg
    assert 'Update your configuration' in error_msg


@pytest.mark.unit
def test_configuration_error_only_missing():
    """
    Test für Konfigurationsfehler nur mit fehlenden Feldern
    
    Requirements: 12.1
    """
    config_path = Path('config.yaml')
    missing_fields = ['api_token']
    invalid_fields = {}
    
    error_msg = ErrorHandler.configuration_error(
        config_path, missing_fields, invalid_fields
    )
    
    assert 'Missing required fields' in error_msg
    assert 'api_token' in error_msg
    assert 'Invalid fields' not in error_msg


@pytest.mark.unit
def test_configuration_error_only_invalid():
    """
    Test für Konfigurationsfehler nur mit ungültigen Feldern
    
    Requirements: 12.1
    """
    config_path = Path('config.yaml')
    missing_fields = []
    invalid_fields = {'url': 'Must start with http:// or https://'}
    
    error_msg = ErrorHandler.configuration_error(
        config_path, missing_fields, invalid_fields
    )
    
    assert 'Invalid fields' in error_msg
    assert 'url' in error_msg
    assert 'Missing required fields' not in error_msg


@pytest.mark.unit
def test_empty_template_directory_error():
    """
    Test für leeres Template-Verzeichnis
    
    Requirements: 12.2
    """
    template_path = Path('templates/de/backup')
    
    error_msg = ErrorHandler.empty_template_directory_error(template_path)
    
    # Verify error message contains key information
    assert 'Template directory is empty' in error_msg
    assert str(template_path) in error_msg
    
    # Verify suggestion is provided
    assert 'Suggestion' in error_msg
    assert 'Add template files' in error_msg
    
    # Verify example structure is shown
    assert 'Example structure' in error_msg
    assert '0000_metadata' in error_msg
    assert '0100_' in error_msg


@pytest.mark.unit
def test_invalid_filename_warning():
    """
    Test für ungültigen Dateinamen
    
    Requirements: 12.2
    """
    file_path = Path('templates/de/backup/invalid_name.md')
    reason = 'Missing 4-digit prefix'
    
    warning_msg = ErrorHandler.invalid_filename_warning(file_path, reason)
    
    # Verify warning message contains key information
    assert 'Invalid template filename' in warning_msg
    assert file_path.name in warning_msg
    assert reason in warning_msg
    
    # Verify suggestion is provided
    assert 'Suggestion' in warning_msg
    assert 'Rename' in warning_msg
    
    # Verify naming conventions are shown
    assert 'NNNN_name.md' in warning_msg
    assert '0000_metadata' in warning_msg
