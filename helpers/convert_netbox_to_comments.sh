#!/bin/bash
# convert_netbox_to_comments.sh - Convert NetBox placeholders to comment format
# Converts {{ netbox.* }} to [[ netbox.* ]] to preserve as reminders for future NetBox integration

set -euo pipefail

echo "=== NetBox Placeholder Conversion ==="
echo ""
echo "This script converts NetBox placeholders from active to comment format:"
echo "  {{ netbox.* }} → [[ netbox.* ]]"
echo ""
echo "This preserves them as reminders for future NetBox integration."
echo ""

# Count occurrences before conversion
echo "Counting current NetBox placeholders..."
NETBOX_COUNT=$(grep -r "{{ netbox\." templates/ --include="*.md" 2>/dev/null | wc -l || echo 0)

echo "Found: $NETBOX_COUNT NetBox placeholder occurrences"
echo ""

if [ "$NETBOX_COUNT" -eq 0 ]; then
    echo "No NetBox placeholders found. Nothing to convert."
    exit 0
fi

read -p "Proceed with conversion? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "Conversion cancelled."
    exit 0
fi

echo ""
echo "Converting NetBox placeholders..."

# Convert {{ netbox.* }} to [[ netbox.* ]]
# This preserves the placeholder structure but makes it inactive
find templates/ -name "*.md" -type f -exec sed -i \
    's/{{ netbox\./[[ netbox./g; s/{{ netbox\./[[ netbox./g' {} +

# Also need to replace the closing braces
find templates/ -name "*.md" -type f -exec sed -i \
    's/\(netbox\.[^}]*\) }}/\1 ]]/g' {} +

echo "  ✓ NetBox placeholders converted to comment format"

echo ""
echo "=== Conversion Complete ==="
echo ""

# Verify conversion
echo "Verifying conversion..."
REMAINING=$(grep -r "{{ netbox\." templates/ --include="*.md" 2>/dev/null | wc -l || echo 0)
CONVERTED=$(grep -r "\[\[ netbox\." templates/ --include="*.md" 2>/dev/null | wc -l || echo 0)

echo "Results:"
echo "  Active NetBox placeholders remaining: $REMAINING"
echo "  Converted to comment format: $CONVERTED"
echo ""

if [ "$REMAINING" -eq 0 ]; then
    echo "✓ All NetBox placeholders successfully converted!"
else
    echo "⚠ Warning: Some active NetBox placeholders remain"
    echo ""
    echo "Run this to see remaining occurrences:"
    echo "  grep -rn '{{ netbox\\.' templates/ --include='*.md'"
fi

echo ""
echo "Next steps:"
echo "1. Review changes: git diff templates/"
echo "2. When NetBox is available, convert back: sed -i 's/\\[\\[ netbox\\./{{ netbox./g; s/\\(netbox\\.[^]]*\\) \\]\\]/\\1 }}/g'"
echo "3. Commit changes: git add templates/ && git commit -m 'Convert NetBox placeholders to comment format for future reference'"
