"""
Property-based tests for unified metadata field access.

Feature: config-separation-and-metadata-unification
Property 7: Unified Placeholder Replacement

Validates: Requirements 3.3, 4.3, 5.3, 6.4, 7.2
"""

import pytest
from hypothesis import given, strategies as st
from src.unified_metadata import (
    GlobalMetadata,
    OrganisationMetadata,
    RolesMetadata,
    HandbookMetadata,
    UnifiedMetadata
)


# Strategy for generating valid field values
field_value_strategy = st.one_of(
    st.text(min_size=1, max_size=50),
    st.integers(min_value=0, max_value=1000).map(str)
)

# Strategy for generating GlobalMetadata
global_metadata_strategy = st.builds(
    GlobalMetadata,
    source=st.text(min_size=1, max_size=50),
    version=st.text(min_size=1, max_size=20)
)

# Strategy for generating OrganisationMetadata
organisation_metadata_strategy = st.builds(
    OrganisationMetadata,
    name=field_value_strategy,
    address=field_value_strategy,
    web=field_value_strategy,
    phone=field_value_strategy,
    revision=st.integers(min_value=0, max_value=100)
)

# Strategy for generating RolesMetadata
roles_metadata_strategy = st.builds(
    RolesMetadata,
    role_CEO=field_value_strategy,
    role_CFO=field_value_strategy,
    role_CTO=field_value_strategy,
    role_CIO=field_value_strategy,
    role_CISO=field_value_strategy,
    role_HR_Manager=field_value_strategy,
    role_Risk_Manager=field_value_strategy,
    role_GDPR_Manager=field_value_strategy,
    role_IT_Manager=field_value_strategy,
    role_Compliance_Manager=field_value_strategy,
    role_Internal_Auditor=field_value_strategy,
    group_IT_Services=field_value_strategy,
    group_DEVOPS=field_value_strategy,
    group_Helpdesk=field_value_strategy
)

# Strategy for generating HandbookMetadata
handbook_metadata_strategy = st.builds(
    HandbookMetadata,
    author=field_value_strategy,
    classification=field_value_strategy,
    status=field_value_strategy,
    type=field_value_strategy,
    templateset_version=field_value_strategy,
    revision=st.integers(min_value=0, max_value=100),
    shortname=field_value_strategy,
    longname=field_value_strategy,
    maintainer=st.one_of(st.none(), field_value_strategy),
    owner=field_value_strategy,
    approver=field_value_strategy,
    creationdate=field_value_strategy,
    modifydate=field_value_strategy,
    valid_from=field_value_strategy,
    next_review=field_value_strategy,
    scope=field_value_strategy
)


@given(
    global_meta=global_metadata_strategy,
    org_meta=organisation_metadata_strategy,
    roles_meta=roles_metadata_strategy,
    handbook_meta=st.one_of(st.none(), handbook_metadata_strategy)
)
def test_property_unified_placeholder_replacement(
    global_meta, org_meta, roles_meta, handbook_meta
):
    """
    Property 7: Unified Placeholder Replacement
    
    For any template containing placeholders in the format {{ meta-source.field }},
    all placeholders should be replaced with corresponding values from the unified
    metadata context (meta-global, meta-organisation, meta-organisation-roles, meta-handbook).
    
    Validates: Requirements 3.3, 4.3, 5.3, 6.4, 7.2
    """
    # Create unified metadata
    unified = UnifiedMetadata(
        global_info=global_meta,
        organisation=org_meta,
        roles=roles_meta,
        handbook=handbook_meta
    )
    
    # Test meta-global field access
    assert unified.get_field('meta-global.source') == global_meta.source
    assert unified.get_field('meta-global.version') == global_meta.version
    
    # Test meta-organisation field access
    assert unified.get_field('meta-organisation.name') == org_meta.name
    assert unified.get_field('meta-organisation.address') == org_meta.address
    assert unified.get_field('meta-organisation.web') == org_meta.web
    assert unified.get_field('meta-organisation.phone') == org_meta.phone
    assert unified.get_field('meta-organisation.revision') == org_meta.revision
    
    # Test meta-organisation-roles field access
    assert unified.get_field('meta-organisation-roles.role_CEO') == roles_meta.role_CEO
    assert unified.get_field('meta-organisation-roles.role_CFO') == roles_meta.role_CFO
    assert unified.get_field('meta-organisation-roles.role_CIO') == roles_meta.role_CIO
    assert unified.get_field('meta-organisation-roles.role_CISO') == roles_meta.role_CISO
    assert unified.get_field('meta-organisation-roles.group_IT_Services') == roles_meta.group_IT_Services
    
    # Test meta-handbook field access (if handbook metadata exists)
    if handbook_meta is not None:
        assert unified.get_field('meta-handbook.author') == handbook_meta.author
        assert unified.get_field('meta-handbook.classification') == handbook_meta.classification
        assert unified.get_field('meta-handbook.status') == handbook_meta.status
        assert unified.get_field('meta-handbook.owner') == handbook_meta.owner
        assert unified.get_field('meta-handbook.revision') == handbook_meta.revision
        # Verify maintainer defaults to author if not specified
        assert unified.get_field('meta-handbook.maintainer') == handbook_meta.maintainer
    else:
        # When handbook metadata is None, meta-handbook fields should return None
        assert unified.get_field('meta-handbook.author') is None
        assert unified.get_field('meta-handbook.status') is None


@given(
    global_meta=global_metadata_strategy,
    org_meta=organisation_metadata_strategy,
    roles_meta=roles_metadata_strategy
)
def test_property_invalid_field_paths_return_none(
    global_meta, org_meta, roles_meta
):
    """
    Property: Invalid field paths should return None.
    
    For any invalid field path (unknown source, unknown field, malformed path),
    the get_field method should return None rather than raising an exception.
    """
    unified = UnifiedMetadata(
        global_info=global_meta,
        organisation=org_meta,
        roles=roles_meta
    )
    
    # Test unknown source
    assert unified.get_field('meta-unknown.field') is None
    
    # Test unknown field in valid source
    assert unified.get_field('meta-global.nonexistent') is None
    assert unified.get_field('meta-organisation.nonexistent') is None
    assert unified.get_field('meta-organisation-roles.nonexistent') is None
    
    # Test malformed paths
    assert unified.get_field('invalid') is None
    assert unified.get_field('') is None
    assert unified.get_field('meta-global') is None


@given(author=field_value_strategy)
def test_property_maintainer_defaults_to_author(author):
    """
    Property: Maintainer defaults to author when not specified.
    
    For any HandbookMetadata where maintainer is not specified,
    the maintainer field should default to the author field value.
    
    Validates: Requirement 6.2
    """
    # Create handbook metadata without maintainer
    handbook = HandbookMetadata(author=author)
    
    # Verify maintainer defaults to author
    assert handbook.maintainer == author
    
    # Create unified metadata and verify field access
    unified = UnifiedMetadata(handbook=handbook)
    assert unified.get_field('meta-handbook.maintainer') == author


@given(
    author=field_value_strategy,
    maintainer=field_value_strategy
)
def test_property_explicit_maintainer_preserved(author, maintainer):
    """
    Property: Explicit maintainer value is preserved.
    
    For any HandbookMetadata where maintainer is explicitly specified,
    the maintainer field should retain that value (not default to author).
    """
    # Create handbook metadata with explicit maintainer
    handbook = HandbookMetadata(author=author, maintainer=maintainer)
    
    # Verify maintainer is preserved
    assert handbook.maintainer == maintainer
    
    # Create unified metadata and verify field access
    unified = UnifiedMetadata(handbook=handbook)
    assert unified.get_field('meta-handbook.maintainer') == maintainer


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--hypothesis-show-statistics"])
