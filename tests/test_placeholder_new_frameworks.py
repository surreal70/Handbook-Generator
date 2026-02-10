"""
Tests for Placeholder System with New Compliance Frameworks

Tests placeholder recognition and processing for IDW PS 951, NIST CSF 2.0, and TOGAF templates.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2026
"""

import pytest
from pathlib import Path
from src.placeholder_processor import PlaceholderProcessor


class MockDataSourceAdapter:
    """Mock adapter for testing placeholder replacement."""
    
    def __init__(self, data: dict):
        """Initialize with mock data."""
        self.data = data
    
    def get_field(self, field_path: str):
        """Get field value from mock data."""
        return self.data.get(field_path)


class TestPlaceholderRecognitionNewFrameworks:
    """Test placeholder recognition for new framework templates."""
    
    def test_recognize_meta_placeholders_idw_ps_951(self):
        """Test recognition of meta placeholders in IDW PS 951 templates."""
        processor = PlaceholderProcessor()
        
        # Sample content from IDW PS 951 template
        content = """---
Document-ID: idw-ps-951-0420
Owner: {{ meta.audit_lead }}
Version: {{ meta.version }}
Status: {{ meta.status }}
Classification: {{ meta.classification }}
Last Update: {{ meta.date }}
---

# Network Infrastructure Audit

## Audit Scope
{{ source.audit_area }}
{{ source.responsible }}
"""
        
        placeholders = processor.find_placeholders(content)
        
        # Verify all placeholders are found
        assert len(placeholders) == 7
        
        # Verify meta placeholders
        meta_placeholders = [p for p in placeholders if p.source == 'meta']
        assert len(meta_placeholders) == 5
        
        meta_fields = [p.field for p in meta_placeholders]
        assert 'audit_lead' in meta_fields
        assert 'version' in meta_fields
        assert 'status' in meta_fields
        assert 'classification' in meta_fields
        assert 'date' in meta_fields
        
        # Verify source placeholders
        source_placeholders = [p for p in placeholders if p.source == 'source']
        assert len(source_placeholders) == 2
        
        source_fields = [p.field for p in source_placeholders]
        assert 'audit_area' in source_fields
        assert 'responsible' in source_fields
    
    def test_recognize_meta_placeholders_nist_csf(self):
        """Test recognition of meta placeholders in NIST CSF 2.0 templates."""
        processor = PlaceholderProcessor()
        
        # Sample content from NIST CSF template
        content = """---
Document-ID: nist-csf-0020
Owner: {{ meta.ciso }}
Version: {{ meta.version }}
Status: {{ meta.status }}
Classification: {{ meta.classification }}
Last Update: {{ meta.date }}
---

# Organizational Context

## Organization Information
- **Name:** {{ source.organization_name }}
- **Industry:** {{ source.industry_sector }}
- **Size:** {{ source.organization_size }}
"""
        
        placeholders = processor.find_placeholders(content)
        
        # Verify all placeholders are found
        assert len(placeholders) == 8
        
        # Verify meta placeholders
        meta_placeholders = [p for p in placeholders if p.source == 'meta']
        assert len(meta_placeholders) == 5
        
        meta_fields = [p.field for p in meta_placeholders]
        assert 'ciso' in meta_fields
        assert 'version' in meta_fields
        assert 'status' in meta_fields
        assert 'classification' in meta_fields
        assert 'date' in meta_fields
        
        # Verify source placeholders
        source_placeholders = [p for p in placeholders if p.source == 'source']
        assert len(source_placeholders) == 3
        
        source_fields = [p.field for p in source_placeholders]
        assert 'organization_name' in source_fields
        assert 'industry_sector' in source_fields
        assert 'organization_size' in source_fields
    
    def test_recognize_meta_placeholders_togaf(self):
        """Test recognition of meta placeholders in TOGAF templates."""
        processor = PlaceholderProcessor()
        
        # Sample content from TOGAF template
        content = """---
Document-ID: togaf-0020
Owner: {{ meta.enterprise_architect }}
Version: {{ meta.version }}
Status: {{ meta.status }}
Classification: {{ meta.classification }}
Last Update: {{ meta.date }}
---

# Architecture Principles

## Principle Definition
- **Name:** {{ source.principle_name }}
- **Statement:** {{ source.principle_statement }}
- **Rationale:** {{ source.principle_rationale }}
"""
        
        placeholders = processor.find_placeholders(content)
        
        # Verify all placeholders are found
        assert len(placeholders) == 8
        
        # Verify meta placeholders
        meta_placeholders = [p for p in placeholders if p.source == 'meta']
        assert len(meta_placeholders) == 5
        
        meta_fields = [p.field for p in meta_placeholders]
        assert 'enterprise_architect' in meta_fields
        assert 'version' in meta_fields
        assert 'status' in meta_fields
        assert 'classification' in meta_fields
        assert 'date' in meta_fields
        
        # Verify source placeholders
        source_placeholders = [p for p in placeholders if p.source == 'source']
        assert len(source_placeholders) == 3
        
        source_fields = [p.field for p in source_placeholders]
        assert 'principle_name' in source_fields
        assert 'principle_statement' in source_fields
        assert 'principle_rationale' in source_fields
    
    def test_recognize_nested_field_paths(self):
        """Test recognition of nested field paths in placeholders."""
        processor = PlaceholderProcessor()
        
        content = """
{{ meta.organization.name }}
{{ source.audit.scope.systems }}
{{ meta.contact.ciso.email }}
"""
        
        placeholders = processor.find_placeholders(content)
        
        assert len(placeholders) == 3
        
        # Verify nested paths are correctly parsed
        assert placeholders[0].source == 'meta'
        assert placeholders[0].field == 'organization.name'
        
        assert placeholders[1].source == 'source'
        assert placeholders[1].field == 'audit.scope.systems'
        
        assert placeholders[2].source == 'meta'
        assert placeholders[2].field == 'contact.ciso.email'
    
    def test_recognize_placeholders_with_whitespace(self):
        """Test recognition of placeholders with various whitespace."""
        processor = PlaceholderProcessor()
        
        content = """
{{meta.version}}
{{ meta.version }}
{{  meta.version  }}
{{   meta.version   }}
"""
        
        placeholders = processor.find_placeholders(content)
        
        # All variations should be recognized
        assert len(placeholders) == 4
        
        # All should have same source and field
        for p in placeholders:
            assert p.source == 'meta'
            assert p.field == 'version'
    
    def test_recognize_source_field_syntax(self):
        """Test that {{ source.field }} syntax is recognized."""
        processor = PlaceholderProcessor()
        
        content = """
{{ source.organization_name }}
{{ source.audit_period }}
{{ source.systems_in_scope }}
"""
        
        placeholders = processor.find_placeholders(content)
        
        assert len(placeholders) == 3
        
        # Verify all use 'source' as the source
        for p in placeholders:
            assert p.source == 'source'
        
        # Verify fields
        fields = [p.field for p in placeholders]
        assert 'organization_name' in fields
        assert 'audit_period' in fields
        assert 'systems_in_scope' in fields


class TestPlaceholderSubstitutionNewFrameworks:
    """Test placeholder substitution for new framework templates."""
    
    def test_substitute_meta_placeholders(self):
        """Test substitution of meta placeholders with data."""
        mock_meta = MockDataSourceAdapter({
            'audit_lead': 'Dr. Schmidt',
            'version': '1.0',
            'status': 'Draft',
            'classification': 'Internal',
            'date': '2026-02-10'
        })
        
        processor = PlaceholderProcessor(data_sources={'meta': mock_meta})
        
        content = """Owner: {{ meta.audit_lead }}
Version: {{ meta.version }}
Status: {{ meta.status }}
"""
        
        result = processor.process_template(content)
        
        # Verify substitutions
        assert 'Dr. Schmidt' in result.content
        assert '1.0' in result.content
        assert 'Draft' in result.content
        
        # Verify placeholders are removed
        assert '{{ meta.audit_lead }}' not in result.content
        assert '{{ meta.version }}' not in result.content
        assert '{{ meta.status }}' not in result.content
        
        # Verify replacement count
        assert len(result.replacements) == 3
    
    def test_substitute_source_placeholders(self):
        """Test substitution of source placeholders with data."""
        mock_source = MockDataSourceAdapter({
            'organization_name': 'AdminSend GmbH',
            'audit_period': '2026-Q1',
            'systems_in_scope': 'ERP, CRM, Email'
        })
        
        processor = PlaceholderProcessor(data_sources={'source': mock_source})
        
        content = """Organization: {{ source.organization_name }}
Period: {{ source.audit_period }}
Systems: {{ source.systems_in_scope }}
"""
        
        result = processor.process_template(content)
        
        # Verify substitutions
        assert 'AdminSend GmbH' in result.content
        assert '2026-Q1' in result.content
        assert 'ERP, CRM, Email' in result.content
        
        # Verify placeholders are removed
        assert '{{ source.organization_name }}' not in result.content
        assert '{{ source.audit_period }}' not in result.content
        assert '{{ source.systems_in_scope }}' not in result.content
        
        # Verify replacement count
        assert len(result.replacements) == 3
    
    def test_preserve_placeholder_when_data_unavailable(self):
        """Test that placeholders are preserved when data is unavailable."""
        mock_meta = MockDataSourceAdapter({
            'version': '1.0'
            # audit_lead is missing
        })
        
        processor = PlaceholderProcessor(data_sources={'meta': mock_meta})
        
        content = """Owner: {{ meta.audit_lead }}
Version: {{ meta.version }}
"""
        
        result = processor.process_template(content)
        
        # Verify available data is substituted
        assert '1.0' in result.content
        assert '{{ meta.version }}' not in result.content
        
        # Verify unavailable placeholder is preserved
        assert '{{ meta.audit_lead }}' in result.content
        
        # Verify warning is generated
        assert len(result.warnings) >= 1
        assert any('audit_lead' in w for w in result.warnings)
        
        # Verify replacement count
        assert len(result.replacements) == 1
    
    def test_mixed_meta_and_source_substitution(self):
        """Test substitution with both meta and source placeholders."""
        mock_meta = MockDataSourceAdapter({
            'audit_lead': 'Dr. Schmidt',
            'version': '1.0'
        })
        mock_source = MockDataSourceAdapter({
            'organization_name': 'AdminSend GmbH',
            'audit_area': 'Network Infrastructure'
        })
        
        processor = PlaceholderProcessor(data_sources={
            'meta': mock_meta,
            'source': mock_source
        })
        
        content = """# Audit Report
Owner: {{ meta.audit_lead }}
Version: {{ meta.version }}
Organization: {{ source.organization_name }}
Area: {{ source.audit_area }}
"""
        
        result = processor.process_template(content)
        
        # Verify all substitutions
        assert 'Dr. Schmidt' in result.content
        assert '1.0' in result.content
        assert 'AdminSend GmbH' in result.content
        assert 'Network Infrastructure' in result.content
        
        # Verify no placeholders remain
        assert '{{' not in result.content
        
        # Verify replacement count
        assert len(result.replacements) == 4
        
        # Verify replacements by source
        meta_replacements = [r for r in result.replacements if r.source == 'meta']
        source_replacements = [r for r in result.replacements if r.source == 'source']
        
        assert len(meta_replacements) == 2
        assert len(source_replacements) == 2


class TestPlaceholderSubstitutionLogging:
    """Test logging of placeholder substitution operations."""
    
    def test_log_successful_substitutions(self):
        """Test that successful substitutions are logged in replacements."""
        mock_meta = MockDataSourceAdapter({
            'audit_lead': 'Dr. Schmidt',
            'version': '1.0'
        })
        
        processor = PlaceholderProcessor(data_sources={'meta': mock_meta})
        
        content = """Owner: {{ meta.audit_lead }}
Version: {{ meta.version }}
"""
        
        result = processor.process_template(content)
        
        # Verify replacements are logged
        assert len(result.replacements) == 2
        
        # Verify replacement details
        for replacement in result.replacements:
            assert replacement.placeholder  # Original placeholder text
            assert replacement.value  # Substituted value
            assert replacement.source == 'meta'  # Source name
            assert replacement.line_number > 0  # Line number
        
        # Verify specific replacements
        audit_lead_replacement = next(
            r for r in result.replacements 
            if 'audit_lead' in r.placeholder
        )
        assert audit_lead_replacement.value == 'Dr. Schmidt'
        assert audit_lead_replacement.source == 'meta'
        
        version_replacement = next(
            r for r in result.replacements 
            if 'version' in r.placeholder
        )
        assert version_replacement.value == '1.0'
        assert version_replacement.source == 'meta'
    
    def test_log_failed_substitutions_as_warnings(self):
        """Test that failed substitutions are logged as warnings."""
        mock_meta = MockDataSourceAdapter({
            'version': '1.0'
            # audit_lead is missing
        })
        
        processor = PlaceholderProcessor(data_sources={'meta': mock_meta})
        
        content = """Owner: {{ meta.audit_lead }}
Version: {{ meta.version }}
"""
        
        result = processor.process_template(content)
        
        # Verify warning is generated for missing field
        assert len(result.warnings) >= 1
        
        # Verify warning contains relevant information
        warning = result.warnings[0]
        assert 'audit_lead' in warning
        assert 'meta' in warning or 'Meta' in warning
        
        # Verify successful replacement is still logged
        assert len(result.replacements) == 1
        assert result.replacements[0].value == '1.0'
    
    def test_log_unknown_source_warnings(self):
        """Test that unknown sources are logged as warnings."""
        processor = PlaceholderProcessor(data_sources={})
        
        content = """{{ meta.audit_lead }}
"""
        
        result = processor.process_template(content)
        
        # Verify warning is generated
        assert len(result.warnings) >= 1
        
        # Verify warning mentions unknown source (check for various error messages)
        warning_text = ' '.join(result.warnings).lower()
        assert 'unknown' in warning_text or 'not found' in warning_text or 'unknown_data_source' in warning_text
        assert 'meta' in warning_text
        
        # Verify no replacements were made
        assert len(result.replacements) == 0
    
    def test_log_includes_line_numbers(self):
        """Test that logged replacements include line numbers."""
        mock_meta = MockDataSourceAdapter({
            'audit_lead': 'Dr. Schmidt',
            'version': '1.0',
            'status': 'Draft'
        })
        
        processor = PlaceholderProcessor(data_sources={'meta': mock_meta})
        
        content = """Line 1: {{ meta.audit_lead }}
Line 2: Some text
Line 3: {{ meta.version }}
Line 4: More text
Line 5: {{ meta.status }}
"""
        
        result = processor.process_template(content)
        
        # Verify all replacements have line numbers
        assert len(result.replacements) == 3
        
        for replacement in result.replacements:
            assert replacement.line_number > 0
        
        # Verify correct line numbers
        audit_lead_replacement = next(
            r for r in result.replacements 
            if 'audit_lead' in r.placeholder
        )
        assert audit_lead_replacement.line_number == 1
        
        version_replacement = next(
            r for r in result.replacements 
            if 'version' in r.placeholder
        )
        assert version_replacement.line_number == 3
        
        status_replacement = next(
            r for r in result.replacements 
            if 'status' in r.placeholder
        )
        assert status_replacement.line_number == 5
    
    def test_statistics_summary_includes_all_sources(self):
        """Test that statistics summary includes all data sources used."""
        mock_meta = MockDataSourceAdapter({
            'audit_lead': 'Dr. Schmidt',
            'version': '1.0'
        })
        mock_source = MockDataSourceAdapter({
            'organization_name': 'AdminSend GmbH',
            'audit_area': 'Network'
        })
        
        processor = PlaceholderProcessor(data_sources={
            'meta': mock_meta,
            'source': mock_source
        })
        
        content = """Owner: {{ meta.audit_lead }}
Version: {{ meta.version }}
Organization: {{ source.organization_name }}
Area: {{ source.audit_area }}
"""
        
        result = processor.process_template(content)
        
        # Verify statistics summary
        stats = result.get_statistics_summary()
        
        assert 'meta' in stats
        assert 'source' in stats
        assert stats['meta'] == 2
        assert stats['source'] == 2
        
        # Verify sources used
        sources = result.get_sources_used()
        assert 'meta' in sources
        assert 'source' in sources
