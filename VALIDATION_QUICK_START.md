# Validation Quick Start Guide

This guide provides quick commands for running quality validation and fixes.

## Quick Validation

```bash
# Run comprehensive validation (recommended)
python validate_quality.py

# Run quality control system
python quality_control.py

# View detailed validation report
cat validation_report.json
```

## Understanding Results

### validate_quality.py Output

The validation script checks:
- ✅ **Document-IDs** - Match between filename and metadata
- ✅ **Metadata Sections** - Presence of required fields
- ✅ **Version History** - Presence of version tracking
- ✅ **Bilingual Consistency** - DE/EN template alignment
- ✅ **Framework Mappings** - Valid template references

**Exit Codes:**
- `0` = No errors (warnings/info may exist)
- `1` = Errors found

### quality_control.py Output

Shows quality metrics:
- Framework Mapping Compliance: Should be 100%
- Bilingual Consistency Rate: Should be 100%
- Test Pass Rate: Current status
- Version History Compliance: Currently disabled

## Fixing Issues

### Add Missing Document-IDs

```bash
# Preview changes (recommended first step)
python fix_document_ids.py --dry-run

# Apply to all frameworks
python fix_document_ids.py

# Apply to specific framework only
python fix_document_ids.py --framework bsi-grundschutz
```

### Add Missing Version History

```bash
# Preview changes (recommended first step)
python fix_version_history.py --dry-run

# Apply to all frameworks
python fix_version_history.py

# Apply to specific framework only
python fix_version_history.py --framework bsi-grundschutz
```

## Validation Workflow

### Initial Check

```bash
# 1. Run validation
python validate_quality.py

# 2. Review summary
# Look at "Issues found" section

# 3. Check detailed report
cat validation_report.json | jq '.error_count, .warning_count'
```

### Fix Critical Issues

```bash
# 1. Preview Document-ID fixes
python fix_document_ids.py --dry-run | head -50

# 2. Apply Document-ID fixes
python fix_document_ids.py

# 3. Preview version history fixes
python fix_version_history.py --dry-run | head -50

# 4. Apply version history fixes
python fix_version_history.py

# 5. Re-run validation
python validate_quality.py
```

### Verify Quality Metrics

```bash
# Run quality control system
python quality_control.py

# Check metrics history
cat .quality/metrics_history.json | jq '.runs[-1]'
```

## Common Issues and Solutions

### Issue: Document-ID Missing

**Symptom:** Error: "Missing Document-ID in metadata"

**Solution:**
```bash
python fix_document_ids.py --framework <framework-name>
```

### Issue: Version History Missing

**Symptom:** Error: "Missing version history section"

**Solution:**
```bash
python fix_version_history.py --framework <framework-name>
```

### Issue: Framework Mapping Reference Error

**Symptom:** Error: "References non-existent template"

**Solution:** Manually edit the 9999_Framework_Mapping.md file to:
- Remove references to non-existent templates, OR
- Create the missing templates

### Issue: Bilingual Inconsistency

**Symptom:** Warning: "Template exists in DE but missing in EN"

**Solution:** Create the missing translation or verify if it's intentional

## Framework-Specific Validation

```bash
# Validate specific framework only
python validate_quality.py 2>&1 | grep "framework-name"

# Fix specific framework
python fix_document_ids.py --framework framework-name
python fix_version_history.py --framework framework-name
```

## Interpreting Severity Levels

- **ERROR** (Red) - Must be fixed for validation to pass
- **WARNING** (Yellow) - Should be fixed for quality
- **INFO** (Blue) - Informational, may be intentional

## Best Practices

1. **Always run dry-run first** before applying fixes
2. **Validate after fixes** to confirm improvements
3. **Review changes** before committing to version control
4. **Run quality control** to track metrics over time
5. **Check specific frameworks** if working on targeted improvements

## Quick Reference

| Command | Purpose | Time |
|---------|---------|------|
| `python validate_quality.py` | Full validation | ~30s |
| `python quality_control.py` | Quality metrics + tests | ~30s |
| `python fix_document_ids.py --dry-run` | Preview ID fixes | ~5s |
| `python fix_document_ids.py` | Apply ID fixes | ~10s |
| `python fix_version_history.py --dry-run` | Preview history fixes | ~5s |
| `python fix_version_history.py` | Apply history fixes | ~10s |

## Getting Help

View detailed documentation:
```bash
# Validation script help
python validate_quality.py --help

# Document-ID fix help
python fix_document_ids.py --help

# Version history fix help
python fix_version_history.py --help

# Quality review
cat FRAMEWORK_QUALITY_REVIEW.md

# Task completion summary
cat TASK_10.5.1.8_COMPLETION_SUMMARY.md
```

## Continuous Quality

Add to your workflow:

```bash
# Before committing changes
python validate_quality.py && echo "✅ Validation passed"

# Weekly quality check
python quality_control.py

# After adding new templates
python validate_quality.py --framework new-framework
```

---

**Need more details?** See:
- `FRAMEWORK_QUALITY_REVIEW.md` - Comprehensive quality analysis
- `TASK_10.5.1.8_COMPLETION_SUMMARY.md` - Task completion details
- `validation_report.json` - Machine-readable validation results
