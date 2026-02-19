#!/bin/bash
# migrate_executive_placeholders.sh - Migrate old executive role placeholders to new format
# Based on meta-organisation-roles.yaml structure

set -euo pipefail

echo "=== Executive Role Placeholder Migration ==="
echo ""
echo "This script migrates old-style placeholders to the new format:"
echo "  {{ meta.ceo.name }}   → {{ meta-organisation-roles.role_CEO }}"
echo "  {{ meta.ceo.email }}  → {{ meta-organisation-roles.role_CEO_email }}"
echo "  {{ meta.cio.name }}   → {{ meta-organisation-roles.role_CIO }}"
echo "  {{ meta.cio.email }}  → {{ meta-organisation-roles.role_CIO_email }}"
echo "  {{ meta.ciso.name }}  → {{ meta-organisation-roles.role_CISO }}"
echo "  {{ meta.ciso.email }} → {{ meta-organisation-roles.role_CISO_email }}"
echo ""

# Count occurrences before migration
echo "Counting current occurrences..."
CEO_NAME_COUNT=$(grep -r "{{ meta\.ceo\.name }}" templates/ --include="*.md" 2>/dev/null | wc -l || echo 0)
CEO_EMAIL_COUNT=$(grep -r "{{ meta\.ceo\.email }}" templates/ --include="*.md" 2>/dev/null | wc -l || echo 0)
CIO_NAME_COUNT=$(grep -r "{{ meta\.cio\.name }}" templates/ --include="*.md" 2>/dev/null | wc -l || echo 0)
CIO_EMAIL_COUNT=$(grep -r "{{ meta\.cio\.email }}" templates/ --include="*.md" 2>/dev/null | wc -l || echo 0)
CISO_NAME_COUNT=$(grep -r "{{ meta\.ciso\.name }}" templates/ --include="*.md" 2>/dev/null | wc -l || echo 0)
CISO_EMAIL_COUNT=$(grep -r "{{ meta\.ciso\.email }}" templates/ --include="*.md" 2>/dev/null | wc -l || echo 0)

echo "Found:"
echo "  {{ meta.ceo.name }}:   $CEO_NAME_COUNT occurrences"
echo "  {{ meta.ceo.email }}:  $CEO_EMAIL_COUNT occurrences"
echo "  {{ meta.cio.name }}:   $CIO_NAME_COUNT occurrences"
echo "  {{ meta.cio.email }}:  $CIO_EMAIL_COUNT occurrences"
echo "  {{ meta.ciso.name }}:  $CISO_NAME_COUNT occurrences"
echo "  {{ meta.ciso.email }}: $CISO_EMAIL_COUNT occurrences"
echo ""

TOTAL=$((CEO_NAME_COUNT + CEO_EMAIL_COUNT + CIO_NAME_COUNT + CIO_EMAIL_COUNT + CISO_NAME_COUNT + CISO_EMAIL_COUNT))
echo "Total: $TOTAL occurrences to migrate"
echo ""

read -p "Proceed with migration? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Migration cancelled."
    exit 0
fi

echo ""
echo "Starting migration..."
echo ""

# Phase 1: Email replacements (must be done first to avoid conflicts)
echo "Phase 1: Migrating email placeholders..."

find templates/ -name "*.md" -type f -exec sed -i \
    's/{{ meta\.ceo\.email }}/{{ meta-organisation-roles.role_CEO_email }}/g' {} +
echo "  ✓ CEO email placeholders migrated"

find templates/ -name "*.md" -type f -exec sed -i \
    's/{{ meta\.cio\.email }}/{{ meta-organisation-roles.role_CIO_email }}/g' {} +
echo "  ✓ CIO email placeholders migrated"

find templates/ -name "*.md" -type f -exec sed -i \
    's/{{ meta\.ciso\.email }}/{{ meta-organisation-roles.role_CISO_email }}/g' {} +
echo "  ✓ CISO email placeholders migrated"

echo ""
echo "Phase 2: Migrating name placeholders..."

find templates/ -name "*.md" -type f -exec sed -i \
    's/{{ meta\.ceo\.name }}/{{ meta-organisation-roles.role_CEO }}/g' {} +
echo "  ✓ CEO name placeholders migrated"

find templates/ -name "*.md" -type f -exec sed -i \
    's/{{ meta\.cio\.name }}/{{ meta-organisation-roles.role_CIO }}/g' {} +
echo "  ✓ CIO name placeholders migrated"

find templates/ -name "*.md" -type f -exec sed -i \
    's/{{ meta\.ciso\.name }}/{{ meta-organisation-roles.role_CISO }}/g' {} +
echo "  ✓ CISO name placeholders migrated"

echo ""
echo "=== Migration Complete ==="
echo ""

# Verify migration
echo "Verifying migration..."
REMAINING_CEO=$(grep -r "{{ meta\.ceo\." templates/ --include="*.md" 2>/dev/null | wc -l || echo 0)
REMAINING_CIO=$(grep -r "{{ meta\.cio\." templates/ --include="*.md" 2>/dev/null | wc -l || echo 0)
REMAINING_CISO=$(grep -r "{{ meta\.ciso\." templates/ --include="*.md" 2>/dev/null | wc -l || echo 0)

if [ "$REMAINING_CEO" -eq 0 ] && [ "$REMAINING_CIO" -eq 0 ] && [ "$REMAINING_CISO" -eq 0 ]; then
    echo "✓ All old-style placeholders successfully migrated!"
else
    echo "⚠ Warning: Some old-style placeholders remain:"
    [ "$REMAINING_CEO" -gt 0 ] && echo "  - {{ meta.ceo.* }}: $REMAINING_CEO occurrences"
    [ "$REMAINING_CIO" -gt 0 ] && echo "  - {{ meta.cio.* }}: $REMAINING_CIO occurrences"
    [ "$REMAINING_CISO" -gt 0 ] && echo "  - {{ meta.ciso.* }}: $REMAINING_CISO occurrences"
    echo ""
    echo "Run this to see remaining occurrences:"
    echo "  grep -rn '{{ meta\.c[ei][os][oi]\\.' templates/ --include='*.md'"
fi

echo ""
echo "New placeholder counts:"
NEW_CEO=$(grep -r "{{ meta-organisation-roles\.role_CEO }}" templates/ --include="*.md" 2>/dev/null | wc -l || echo 0)
NEW_CIO=$(grep -r "{{ meta-organisation-roles\.role_CIO }}" templates/ --include="*.md" 2>/dev/null | wc -l || echo 0)
NEW_CISO=$(grep -r "{{ meta-organisation-roles\.role_CISO }}" templates/ --include="*.md" 2>/dev/null | wc -l || echo 0)
echo "  {{ meta-organisation-roles.role_CEO }}:  $NEW_CEO"
echo "  {{ meta-organisation-roles.role_CIO }}:  $NEW_CIO"
echo "  {{ meta-organisation-roles.role_CISO }}: $NEW_CISO"

echo ""
echo "Next steps:"
echo "1. Review changes: git diff templates/"
echo "2. Test generation: ./handbook-generator --handbook isms --language en"
echo "3. Commit changes: git add templates/ && git commit -m 'Migrate executive role placeholders to new format'"
