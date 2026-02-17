"""
Smoke tests to verify project setup

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

import pytest
from hypothesis import given, strategies as st


@pytest.mark.unit
def test_imports():
    """Verify all required dependencies can be imported."""
    import jinja2
    import pynetbox
    import yaml
    import markdown
    
    assert jinja2.__version__
    assert pynetbox.__version__


@pytest.mark.unit
def test_weasyprint_import():
    """Verify weasyprint can be imported (requires system libraries)."""
    try:
        import weasyprint
        assert weasyprint.__version__
    except OSError as e:
        pytest.skip(f"WeasyPrint system libraries not installed: {e}")


@pytest.mark.unit
def test_src_package():
    """Verify src package is importable."""
    import src
    
    assert src.__version__ == "0.0.12"
    assert src.__author__ == "Andreas Huemmer"


@pytest.mark.property
@given(st.text())
def test_hypothesis_setup(text):
    """
    Feature: handbook-generator, Property: Hypothesis Configuration Test
    
    Verify that Hypothesis is properly configured and working.
    """
    # Simple property: text length is non-negative
    assert len(text) >= 0
