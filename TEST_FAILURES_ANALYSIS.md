# Test Failures Analysis - Full Test Suite Run

**Date:** 2026-02-13  
**Total Tests:** 1768  
**Passed:** 1573  
**Failed:** 166  
**Skipped:** 29  
**Duration:** 15:28 minutes

## Summary

This document catalogs all test failures from the full test suite run, excluding PDF generation related failures. Tests are grouped by category for easier review and fixing.

---

## Category 1: Template Numbering & Range Issues (35 failures)

### Issue: Templates don't meet minimum range requirements

**Affected Frameworks:**
- COSO: Expected ≥500, found 290 (DE & EN)
- DORA: Expected ≥400, found 280 (DE & EN)
- ISO 31000: Expected ≥400, found 290 (DE & EN)
- ISO 38500: Expected ≥400, found 250 (DE & EN)
- SOC1: Expected ≥450, found 160 (DE & EN)
- TISAX: Expected ≥550, found 380 (DE & EN)

**Failed Tests:**
- `test_coso_properties.py::TestCOSOTemplateNumberingRangeCoverage::test_coso_minimum_template_range_*`
- `test_dora_properties.py::TestDORATemplateNumberingRangeCoverage::test_dora_minimum_template_range_*`
- `test_iso31000_properties.py::TestISO31000TemplateNumberingRangeCoverage::test_iso31000_minimum_template_range_*`
- `test_iso38500_properties.py::TestISO38500TemplateNumberingRangeCoverage::test_iso38500_minimum_template_range_*`
- `test_soc1_properties.py::TestSOC1TemplateNumberingRangeCoverage::test_soc1_minimum_template_range_*`
- `test_tisax_properties.py::TestTISAXTemplateNumberingRangeCoverage::test_tisax_minimum_template_range_*`

**Action Required:** Add more templates to reach minimum coverage thresholds

---

## Category 2: Template Numbering Increment Issues (21 failures)

### Issue: Template numbers don't increment by 10

**Affected Frameworks:**
- ISO 38500: 190→250 (diff: 60)
- ISO 31000: 90→170 (diff: 80)
- CSA CCM: 140→200 (diff: 60), max 940 > 800
- TISAX: 90→170 (diff: 80)
- SOC1: 90→130 (diff: 40)
- COSO: 90→150 (diff: 60)
- DORA: 90→150 (diff: 60)
- IDW PS 951: 550→9999 (diff: 9449)
- NIST CSF: 640→9999 (diff: 9359)
- TOGAF: 700→9999 (diff: 9299)

**Failed Tests:**
- `test_framework_properties_phase2.py::TestProperty2TemplateNumberingIncrements::test_property_2_template_numbering_increments_*`
- `test_framework_specific_properties.py::TestTemplateNumberingIncrements::test_*_numbering_increments`

**Action Required:** Renumber templates to follow 10-increment pattern, handle 9999 mapping file specially

---

## Category 3: Framework Mapping Completeness (16 failures)

### Issue: Missing framework requirements in 9999_Framework_Mapping.md

**Affected Frameworks:**
- ISO 38500: No requirements listed (DE), missing template 0320_decision_making.md (EN)
- ISO 31000: No requirements listed (DE), missing template 0300_risk_treatment_overview.md (EN)
- CSA CCM: Missing template 0300_identity_access_management_overview.md (DE & EN)
- TISAX: Missing template 0300_operations_security_overview.md (DE & EN)
- SOC1: No requirements listed (DE), missing template 0200_risk_assessment.md (EN)
- COSO: No requirements listed (DE), missing template 0430_deficiency_evaluation.md (EN)
- DORA: No requirements listed (DE & EN)

**Failed Tests:**
- `test_framework_properties_phase2.py::TestProperty16FrameworkRequirementMappingCompleteness::test_property_16_framework_mapping_completeness_*`

**Action Required:** 
1. Add framework requirements to mapping files
2. Create missing referenced templates

---

## Category 4: Placeholder Processing Issues (15 failures)

### Issue: Placeholders with '{{' not properly handled

**Symptoms:**
- Placeholders containing only '{{' are not replaced
- Invalid placeholders remain in content
- Placeholder validation fails for edge cases

**Failed Tests:**
- `test_placeholder_processor.py::TestPlaceholderReplacement::test_property_8_placeholder_replacement`
- `test_placeholder_processor.py::TestMissingFieldHandling::test_property_7_missing_field_handling`
- `test_placeholder_processor.py::TestAdapterRouting::test_property_21_data_source_adapter_routing`
- `test_placeholder_processor.py::TestMetadataPlaceholders::test_property_14_version_number_fallback`
- `test_placeholder_processor.py::TestDualSourceProcessingProperty::test_property_4_dual_source_placeholder_processing`
- `test_placeholder_properties_new_frameworks.py::TestProperty11PlaceholderRecognitionAndProcessing::test_property_11_*`
- `test_placeholder_properties_new_frameworks.py::TestProperty12PlaceholderSubstitutionLogging::test_property_12_logging_with_failures`

**Action Required:** Fix placeholder processor to handle edge cases with '{{' and incomplete placeholders

---

## Category 5: CIS Controls Integration Issues (10 failures)

### Issue: CIS Controls templates have inconsistent placeholders and output structure

**Problems:**
- DE template 9999 has placeholders, EN template has none
- Output path doesn't contain 'markdown' directory
- BCM template count changed from 31 to 32

**Failed Tests:**
- `test_cis_controls_integration.py::TestPlaceholderPreservation::test_*`
- `test_cis_controls_integration.py::TestMultiFormatOutputGeneration::test_cis_controls_markdown_generation`
- `test_cis_controls_integration.py::TestPlaceholderReplacementCorrectness::test_property_placeholder_replacement_correctness`
- `test_cis_controls_integration.py::TestPlaceholderErrorHandling::test_property_placeholder_error_handling`
- `test_cis_controls_integration.py::TestPlaceholderProcessingInMetadata::test_property_mixed_metadata_and_data_source_placeholders`
- `test_cis_controls_integration.py::TestBackwardCompatibilityPreservation::test_existing_handbook_types_count_unchanged`
- `test_cis_controls_integration.py::TestLanguageSelectionFunctionality::test_property_language_flag_controls_output_language`
- `test_cis_controls_integration.py::TestOutputStructureConsistency::test_*`

**Action Required:**
1. Sync placeholders between DE/EN CIS Controls templates
2. Fix output path structure
3. Investigate BCM template count change

---

## Category 6: Metadata Standardization Issues (10 failures)

### Issue: Missing or inconsistent metadata fields

**Problems:**
- ISO 31000 (EN) missing 'date' field
- COSO (DE) missing 'template_version' and 'revision' fields
- IDW PS 951 has different missing fields between DE/EN
- TOGAF (DE) has invalid placeholder syntax: `{{ meta.document.last_updated }}`
- 40 templates missing document history (README.md and 9999_Framework_Mapping.md files)
- 210 templates missing initial version 0.1
- German templates have English "Document History:" header instead of German

**Failed Tests:**
- `test_metadata_standardization_properties.py::TestMetadataCompletenessProperty::test_all_metadata_files_have_required_fields`
- `test_metadata_standardization_properties.py::TestTemplateVersionFormatProperty::test_template_version_follows_semantic_versioning`
- `test_metadata_standardization_properties.py::TestRevisionNumberValidityProperty::test_revision_is_non_negative_integer`
- `test_metadata_standardization_properties.py::TestBilingualConsistencyProperty::test_de_en_metadata_have_same_structure`
- `test_metadata_standardization_properties.py::TestPlaceholderSyntaxProperty::test_all_placeholders_follow_valid_syntax`
- `test_metadata_standardization_properties.py::TestDocumentHistoryPresenceProperty::test_*`

**Action Required:**
1. Add missing metadata fields
2. Fix placeholder syntax (remove extra spaces)
3. Add document history to README and mapping files
4. Set initial version to 0.1 for all templates
5. Translate document history headers to German

---

## Category 7: HTML Comment Processing Issues (2 failures)

### Issue: Comment markers not properly removed

**Symptoms:**
- Closing comment marker '-->' remains after processing
- Multiline comments with edge cases fail

**Failed Tests:**
- `test_comprehensive_properties.py::TestHTMLCommentMultilineHandling::test_property_comment_content_removal`
- `test_html_comment_processor.py::TestHTMLCommentRemovalProperty::test_property_1_multiline_comment_removal`

**Action Required:** Fix HTML comment processor to handle edge cases like content that is just '-->'

---

## Category 8: Output Generator Issues (4 failures)

### Issue: Output format detection incorrect

**Symptoms:**
- Expected 'markdown' but got 'backup', 'cis-controls', or 'test-output'
- Output path structure doesn't match expectations

**Failed Tests:**
- `test_output_generator.py::test_generate_markdown_basic`
- `test_output_generator.py::test_test_mode_enabled_allows_markdown_generation`
- `test_output_generator.py::test_cis_controls_combined_markdown_generation`
- `test_output_generator.py::test_cis_controls_english_markdown_generation`

**Action Required:** Fix output format detection logic in output generator

---

## Category 9: Quality Control Integration Issues (7 failures)

### Issue: Version history validation disabled, affecting quality metrics

**Problems:**
- Version history compliance shows 0.0% (validation disabled)
- Quality control reports show FAILED status due to version history
- Sequential execution order incorrect
- Metrics tracking not working

**Failed Tests:**
- `test_quality_control_integration.py::TestQualityControlFullWorkflow::test_complete_quality_control_run_success`
- `test_quality_control_integration.py::TestQualityControlFullWorkflow::test_complete_quality_control_run_with_issues`
- `test_quality_control_integration.py::TestQualityControlFullWorkflow::test_error_handling_and_recovery`
- `test_quality_control_integration.py::TestQualityControlReportGeneration::test_report_with_all_checks_passing`
- `test_quality_control_orchestrator.py::TestSequentialExecution::test_property_sequential_execution`
- `test_quality_control_orchestrator.py::TestSequentialExecution::test_sequential_execution_with_exceptions`
- `test_quality_control_orchestrator.py::TestIntegration::test_*`

**Action Required:**
1. Re-enable version history validation or update tests to handle disabled state
2. Fix sequential execution order
3. Fix metrics tracking

---

## Category 10: Framework Mapping Validator Issues (2 failures)

### Issue: Validation logic errors

**Problems:**
- Framework with incorrect mapping file not detected
- Error reporting incomplete

**Failed Tests:**
- `test_framework_mapping_validator.py::TestFrameworkMappingValidatorProperties::test_property_3_complete_error_reporting`
- `test_framework_mapping_validator.py::TestFrameworkMappingValidatorUnit::test_framework_with_incorrect_mapping_file`

**Action Required:** Fix framework mapping validator logic

---

## Category 11: Coverage Documentation Generator Issues (1 failure)

### Issue: Framework metadata extraction fails with minimal input

**Failed Tests:**
- `test_coverage_documentation_generator.py::TestCoverageDocumentationGeneratorProperties::test_property_framework_metadata_extraction`

**Action Required:** Handle edge cases in metadata extraction

---

## Category 12: Logger Issues (1 failure)

### Issue: Verbose logging format validation

**Failed Tests:**
- `test_logger.py::TestVerboseLogging::test_verbose_details_in_errors_property`

**Action Required:** Fix verbose error message format

---

## Category 13: Metadata Config Manager Issues (2 failures)

### Issue: Role validation allows whitespace-only titles

**Failed Tests:**
- `test_metadata_config_manager.py::TestMetadataConfigManagerProperties::test_property_organization_role_validation`
- `test_metadata_config_manager.py::TestMetadataConfigManagerProperties::test_property_metadata_configuration_validation`

**Action Required:** Add validation to reject whitespace-only role titles

---

## Category 14: Template Structure Issues (12 failures)

### Issue: Various template structure problems

**Problems:**
- Template 9999 not a multiple of 10
- Bilingual template line count mismatch (DE: 754, EN: 407)
- Placeholder sources don't match between languages
- Framework mapping documentation missing
- IT-operation templates: expected 30, found 31
- Service-templates directory missing

**Failed Tests:**
- `test_template_structure.py::TestTemplateNumberingSequence::test_property_11_template_numbering_sequence`
- `test_template_structure.py::TestBilingualTemplateConsistency::test_property_10_bilingual_template_consistency`
- `test_template_structure.py::TestMultiLanguagePlaceholderConsistency::test_property_17_multi_language_placeholder_consistency`
- `test_template_structure.py::TestTemplateDocumentation::test_*`
- `test_template_structure.py::TestCompleteTemplateStructure::test_*`

**Action Required:**
1. Exclude 9999 from numbering validation
2. Sync template content between languages
3. Create framework mapping documentation
4. Verify template count expectations
5. Create service-templates directory structure

---

## Category 15: Template Manager Issues (3 failures)

### Issue: Metadata template validation and filename conventions

**Problems:**
- Invalid metadata template names accepted (e.g., 0000_metadata_aa_0.md)
- README.md not recognized as valid content template
- Unicode encoding errors with surrogate characters

**Failed Tests:**
- `test_template_manager.py::TestMetadataTemplates::test_property_13_metadata_template_format_validation`
- `test_template_manager_cis_integration.py::TestFilenameConventionValidation::test_content_template_numbering_validation`
- `test_template_manager_new_frameworks.py::TestProperty10MetadataExtraction::test_property_10_metadata_extraction`

**Action Required:**
1. Fix metadata template name validation
2. Handle special files like README.md
3. Add unicode validation/sanitization

---

## Category 16: Test Suite Runner Issues (2 failures)

### Issue: Command execution and error handling

**Problems:**
- Pytest command includes unexpected markers and maxfail
- Error exit codes not captured properly

**Failed Tests:**
- `test_test_suite_runner.py::TestPytestCommandExecution::test_output_capture_works`
- `test_test_suite_runner.py::TestPytestCommandExecution::test_pytest_error_exit_code`

**Action Required:** Fix test suite runner command construction and error handling

---

## Category 17: Integration Test Issues (1 failure)

### Issue: Phase 2 frameworks don't meet minimum template requirements

**Failed Tests:**
- `test_integration_phase2.py::TestPhase2TemplateValidation::test_phase2_frameworks_have_minimum_templates`

**Action Required:** Add more templates to ISO 38500 (has 20, needs 25)

---

## Category 18: Placeholder Validation Issues (2 failures)

### Issue: Placeholder line validation and template pass-through

**Failed Tests:**
- `test_placeholder_processor.py::TestPlaceholderValidation::test_property_4_placeholder_line_validation`
- `test_placeholder_processor.py::TestTemplatePassThrough::test_property_5_template_pass_through`

**Action Required:** Fix placeholder validation for edge cases with extra content

---

## Priority Recommendations

### High Priority (Blocking Multiple Features)
1. **Fix placeholder processor** - Affects 15+ tests across multiple modules
2. **Add missing templates** - Affects framework coverage and compliance
3. **Fix metadata standardization** - Affects 10 tests and documentation quality
4. **Fix CIS Controls integration** - Affects 10 tests and new feature

### Medium Priority (Quality & Consistency)
5. **Fix template numbering** - Affects 21 tests but mostly validation
6. **Fix framework mapping** - Affects 16 tests and documentation
7. **Fix template structure** - Affects 12 tests and organization
8. **Fix quality control** - Affects 7 tests but feature is new

### Low Priority (Edge Cases & Polish)
9. **Fix HTML comment processing** - Affects 2 tests, edge cases
10. **Fix output generator** - Affects 4 tests, format detection
11. **Fix remaining issues** - Various small fixes

---

## Next Steps

1. Review this analysis with the team
2. Prioritize fixes based on impact and dependencies
3. Create fix branches for each category
4. Implement fixes with corresponding test updates
5. Re-run full test suite to verify fixes
6. Update documentation as needed

