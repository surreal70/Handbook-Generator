"""
Pytest configuration and fixtures for Handbuch-Generator tests

This module provides shared fixtures and Hypothesis configuration for all tests.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

import pytest
from hypothesis import settings, Verbosity

# Configure Hypothesis profiles
settings.register_profile("default", max_examples=100, deadline=None)
settings.register_profile("ci", max_examples=1000, deadline=None)
settings.register_profile("dev", max_examples=10, verbosity=Verbosity.verbose)

# Load the default profile
settings.load_profile("default")


@pytest.fixture
def sample_template_content():
    """Provide sample template content for testing."""
    return """# Test Template

This is a test template with placeholders.

Device Name: {{ netbox.device_name }}
Site: {{ netbox.site_name }}
"""


@pytest.fixture
def sample_config():
    """Provide sample configuration for testing."""
    return {
        "data_sources": {
            "netbox": {
                "url": "https://netbox.example.com",
                "api_token": "test_token_12345"
            }
        },
        "defaults": {
            "language": "de",
            "output_format": "both"
        },
        "metadata": {
            "author": "Andreas Huemmer [andreas.huemmer@adminsend.de]",
            "version": "1.0.0"
        }
    }
