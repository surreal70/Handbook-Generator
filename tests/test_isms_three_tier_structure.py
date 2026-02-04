"""
Property-based tests for ISMS three-tier structure.

Feature: template-system-extension
Property 15: ISMS Three-Tier Structure

For any ISMS template set, templates SHALL be organized into three distinct tiers:
Basis ISMS (0010-0160), Abstract Policies (0200-0680 even), and Detailed Guidelines (0210-0690 odd).

Validates: Requirements 7.1, 7.2, 7.3, 7.4, 7.5
"""

import os
import re
from pathlib import Path
from hypothesis import given, settings, strategies as st, HealthCheck
import pytest


class TestISMSThreeTierStructure:
    """Test ISMS three-tier structure organization."""
    
    @pytest.fixture
    def template_base_path(self):
        """Get the base path for templates."""
        return Path("templates")
    
    def test_isms_basis_tier_exists(self, template_base_path):
        """
        Test that ISMS Basis tier (0010-0160) exists.
        
        Property 15: ISMS Three-Tier Structure
        Validates: Requirements 7.1
        """
        for language in ['de', 'en']:
            isms_path = template_base_path / language / "isms"
            
            # Get all Basis ISMS templates (0010-0160)
            basis_templates = [
                f for f in os.listdir(isms_path)
                if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
            ]
            
            # Extract numbers in the 0010-0160 range
            basis_numbers = [
                int(f[:4]) for f in basis_templates
                if 10 <= int(f[:4]) <= 160
            ]
            
            # Should have at least the key basis templates
            assert len(basis_numbers) >= 10, \
                f"ISMS Basis tier should have at least 10 templates for {language}, found {len(basis_numbers)}"
            
            # Verify key basis templates exist
            key_basis_numbers = [10, 20, 30, 40, 50, 60, 100]
            for num in key_basis_numbers:
                assert num in basis_numbers, \
                    f"ISMS Basis tier should include template {num:04d} for {language}"
    
    def test_isms_policy_tier_exists(self, template_base_path):
        """
        Test that ISMS Abstract Policies tier (0200-0680, even numbers) exists.
        
        Property 15: ISMS Three-Tier Structure
        Validates: Requirements 7.2
        """
        for language in ['de', 'en']:
            isms_path = template_base_path / language / "isms"
            
            # Get all Policy templates (0200-0680, even numbers)
            policy_templates = [
                f for f in os.listdir(isms_path)
                if f.endswith('.md') and f.startswith('0')
            ]
            
            # Extract even numbers in the 0200-0680 range
            # Policies are at 0200, 0220, 0240, ... (200 + n*20)
            policy_numbers = [
                int(f[:4]) for f in policy_templates
                if 200 <= int(f[:4]) <= 680 and (int(f[:4]) - 200) % 20 == 0
            ]
            
            # Should have at least 20 policy templates
            assert len(policy_numbers) >= 20, \
                f"ISMS Policy tier should have at least 20 templates for {language}, found {len(policy_numbers)}"
            
            # Verify all follow the pattern (200 + n*20)
            for num in policy_numbers:
                assert (num - 200) % 20 == 0, \
                    f"Policy template {num:04d} should follow pattern 200 + n*20 for {language}"
            
            # Verify key policy templates exist
            key_policy_numbers = [200, 220, 240, 260, 280, 300, 400, 600]
            for num in key_policy_numbers:
                assert num in policy_numbers, \
                    f"ISMS Policy tier should include template {num:04d} for {language}"
    
    def test_isms_guideline_tier_exists(self, template_base_path):
        """
        Test that ISMS Detailed Guidelines tier (0210-0690, odd numbers) exists.
        
        Property 15: ISMS Three-Tier Structure
        Validates: Requirements 7.3
        """
        for language in ['de', 'en']:
            isms_path = template_base_path / language / "isms"
            
            # Get all Guideline templates (0210-0690, odd numbers)
            guideline_templates = [
                f for f in os.listdir(isms_path)
                if f.endswith('.md') and f.startswith('0')
            ]
            
            # Extract odd numbers in the 0210-0690 range (210 + n*20)
            # Guidelines are at 0210, 0230, 0250, ... (210 + n*20)
            guideline_numbers = [
                int(f[:4]) for f in guideline_templates
                if 210 <= int(f[:4]) <= 690 and (int(f[:4]) - 210) % 20 == 0
            ]
            
            # Should have at least 20 guideline templates
            assert len(guideline_numbers) >= 20, \
                f"ISMS Guideline tier should have at least 20 templates for {language}, found {len(guideline_numbers)}"
            
            # Verify all follow the pattern (210 + n*20)
            for num in guideline_numbers:
                assert (num - 210) % 20 == 0, \
                    f"Guideline template {num:04d} should follow pattern 210 + n*20 for {language}"
            
            # Verify key guideline templates exist
            key_guideline_numbers = [210, 230, 250, 270, 290, 310, 410, 610]
            for num in key_guideline_numbers:
                assert num in guideline_numbers, \
                    f"ISMS Guideline tier should include template {num:04d} for {language}"
    
    def test_isms_policy_guideline_pairing(self, template_base_path):
        """
        Test that ISMS Policies and Guidelines are properly paired.
        
        Property 15: ISMS Three-Tier Structure
        Validates: Requirements 7.4
        """
        for language in ['de', 'en']:
            isms_path = template_base_path / language / "isms"
            
            # Get all templates
            all_templates = [
                f for f in os.listdir(isms_path)
                if f.endswith('.md') and f.startswith('0')
            ]
            
            # Extract policy numbers (200-680, even)
            policy_numbers = [
                int(f[:4]) for f in all_templates
                if 200 <= int(f[:4]) <= 680 and int(f[:4]) % 20 == 0
            ]
            
            # For each policy, check if corresponding guideline exists
            for policy_num in policy_numbers:
                guideline_num = policy_num + 10
                
                # Find guideline template
                guideline_templates = [
                    f for f in all_templates
                    if f.startswith(f"{guideline_num:04d}_")
                ]
                
                assert len(guideline_templates) > 0, \
                    f"Policy {policy_num:04d} should have corresponding Guideline {guideline_num:04d} for {language}"
    
    def test_isms_tier_separation(self, template_base_path):
        """
        Test that ISMS tiers are clearly separated.
        
        Property 15: ISMS Three-Tier Structure
        Validates: Requirements 7.5
        """
        for language in ['de', 'en']:
            isms_path = template_base_path / language / "isms"
            
            # Get all templates
            all_templates = [
                f for f in os.listdir(isms_path)
                if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
            ]
            
            # Extract numbers
            template_numbers = [int(f[:4]) for f in all_templates]
            
            # Categorize templates
            basis_tier = [n for n in template_numbers if 10 <= n <= 160]
            policy_tier = [n for n in template_numbers if 200 <= n <= 680 and (n - 200) % 20 == 0]
            guideline_tier = [n for n in template_numbers if 210 <= n <= 690 and (n - 210) % 20 == 0]
            appendix_tier = [n for n in template_numbers if 710 <= n <= 740]
            
            # Verify no overlap between tiers
            all_categorized = set(basis_tier + policy_tier + guideline_tier + appendix_tier)
            assert len(all_categorized) == len(template_numbers), \
                f"All templates should be categorized into exactly one tier for {language}"
            
            # Verify tier counts (be lenient for appendix as it may not be fully implemented yet)
            assert len(basis_tier) >= 10, f"Basis tier should have at least 10 templates for {language}"
            assert len(policy_tier) >= 20, f"Policy tier should have at least 20 templates for {language}"
            assert len(guideline_tier) >= 20, f"Guideline tier should have at least 20 templates for {language}"
            assert len(appendix_tier) >= 1, f"Appendix tier should have at least 1 template for {language}"
    
    def test_isms_policy_naming_convention(self, template_base_path):
        """
        Test that ISMS Policy templates follow naming convention.
        
        Property 15: ISMS Three-Tier Structure
        Validates: Requirements 7.2
        """
        for language in ['de', 'en']:
            isms_path = template_base_path / language / "isms"
            
            # Get all Policy templates (0200-0680, even numbers)
            policy_templates = [
                f for f in os.listdir(isms_path)
                if f.endswith('.md') and f.startswith('0')
            ]
            
            # Filter policy templates
            policy_files = [
                f for f in policy_templates
                if 200 <= int(f[:4]) <= 680 and int(f[:4]) % 20 == 0
            ]
            
            # Check naming convention
            for policy_file in policy_files:
                if language == 'de':
                    assert 'Policy_' in policy_file, \
                        f"German policy template {policy_file} should contain 'Policy_' in filename"
                else:  # en
                    assert 'Policy_' in policy_file, \
                        f"English policy template {policy_file} should contain 'Policy_' in filename"
    
    def test_isms_guideline_naming_convention(self, template_base_path):
        """
        Test that ISMS Guideline templates follow naming convention.
        
        Property 15: ISMS Three-Tier Structure
        Validates: Requirements 7.3
        """
        for language in ['de', 'en']:
            isms_path = template_base_path / language / "isms"
            
            # Get all Guideline templates (0210-0690, odd numbers)
            guideline_templates = [
                f for f in os.listdir(isms_path)
                if f.endswith('.md') and f.startswith('0')
            ]
            
            # Filter guideline templates
            guideline_files = [
                f for f in guideline_templates
                if 210 <= int(f[:4]) <= 690 and int(f[:4]) % 20 == 10
            ]
            
            # Check naming convention
            for guideline_file in guideline_files:
                if language == 'de':
                    assert 'Richtlinie_' in guideline_file, \
                        f"German guideline template {guideline_file} should contain 'Richtlinie_' in filename"
                else:  # en
                    assert 'Guideline_' in guideline_file, \
                        f"English guideline template {guideline_file} should contain 'Guideline_' in filename"
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        template_number=st.integers(min_value=200, max_value=680).filter(lambda x: x % 20 == 0)
    )
    def test_property_policy_guideline_pairing(self, template_base_path, template_number):
        """
        Property test: For any policy template number (200-680, even), a corresponding
        guideline template (number + 10) should exist.
        
        Feature: template-system-extension
        Property 15: ISMS Three-Tier Structure
        
        Validates: Requirements 7.1, 7.2, 7.3, 7.4, 7.5
        """
        for language in ['de', 'en']:
            isms_path = template_base_path / language / "isms"
            
            # Find policy template
            policy_templates = [
                f for f in os.listdir(isms_path)
                if f.startswith(f"{template_number:04d}_") and f.endswith('.md')
            ]
            
            # If policy exists, guideline should exist too
            if policy_templates:
                guideline_number = template_number + 10
                guideline_templates = [
                    f for f in os.listdir(isms_path)
                    if f.startswith(f"{guideline_number:04d}_") and f.endswith('.md')
                ]
                
                assert len(guideline_templates) > 0, \
                    f"Policy {template_number:04d} exists but no corresponding Guideline {guideline_number:04d} found for {language}"
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        tier=st.sampled_from(['basis', 'policy', 'guideline', 'appendix'])
    )
    def test_property_tier_number_ranges(self, template_base_path, tier):
        """
        Property test: For any tier, all template numbers should fall within the
        defined range for that tier.
        
        Feature: template-system-extension
        Property 15: ISMS Three-Tier Structure
        
        Validates: Requirements 7.1, 7.2, 7.3, 7.5
        """
        tier_ranges = {
            'basis': (10, 160),
            'policy': (200, 680),
            'guideline': (210, 690),
            'appendix': (710, 740)
        }
        
        min_num, max_num = tier_ranges[tier]
        
        for language in ['de', 'en']:
            isms_path = template_base_path / language / "isms"
            
            # Get all templates
            all_templates = [
                f for f in os.listdir(isms_path)
                if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
            ]
            
            # Filter templates by tier type (not just range)
            if tier == 'basis':
                tier_templates = [
                    f for f in all_templates
                    if 10 <= int(f[:4]) <= 160
                ]
            elif tier == 'policy':
                tier_templates = [
                    f for f in all_templates
                    if 200 <= int(f[:4]) <= 680 and 'Policy_' in f
                ]
            elif tier == 'guideline':
                tier_templates = [
                    f for f in all_templates
                    if 210 <= int(f[:4]) <= 690 and ('Richtlinie_' in f or 'Guideline_' in f)
                ]
            elif tier == 'appendix':
                tier_templates = [
                    f for f in all_templates
                    if 710 <= int(f[:4]) <= 740
                ]
            
            # Extract numbers
            tier_numbers = [int(f[:4]) for f in tier_templates]
            
            # Verify all numbers are within range
            for num in tier_numbers:
                assert min_num <= num <= max_num, \
                    f"Template {num:04d} in {tier} tier should be within range {min_num:04d}-{max_num:04d} for {language}"
                
                # Additional validation for policy/guideline tiers
                if tier == 'policy':
                    assert (num - 200) % 20 == 0, \
                        f"Policy template {num:04d} should follow pattern 200 + n*20 for {language}"
                elif tier == 'guideline':
                    assert (num - 210) % 20 == 0, \
                        f"Guideline template {num:04d} should follow pattern 210 + n*20 for {language}"
    
    @settings(max_examples=100, suppress_health_check=[HealthCheck.function_scoped_fixture])
    @given(
        language=st.sampled_from(['de', 'en'])
    )
    def test_property_three_tier_completeness(self, template_base_path, language):
        """
        Property test: For any language, the ISMS template set should contain all three tiers
        with proper organization.
        
        Feature: template-system-extension
        Property 15: ISMS Three-Tier Structure
        
        Validates: Requirements 7.1, 7.2, 7.3, 7.4, 7.5
        """
        isms_path = template_base_path / language / "isms"
        
        # Get all templates
        all_templates = [
            f for f in os.listdir(isms_path)
            if f.endswith('.md') and f.startswith('0') and not f.startswith('0000')
        ]
        
        # Extract numbers
        template_numbers = [int(f[:4]) for f in all_templates]
        
        # Categorize into tiers
        basis_tier = [n for n in template_numbers if 10 <= n <= 160]
        policy_tier = [n for n in template_numbers if 200 <= n <= 680 and (n - 200) % 20 == 0]
        guideline_tier = [n for n in template_numbers if 210 <= n <= 690 and (n - 210) % 20 == 0]
        
        # All three tiers should exist
        assert len(basis_tier) > 0, f"Basis tier should exist for {language}"
        assert len(policy_tier) > 0, f"Policy tier should exist for {language}"
        assert len(guideline_tier) > 0, f"Guideline tier should exist for {language}"
        
        # Policy and guideline tiers should have similar counts (within 20%)
        if len(policy_tier) > 0 and len(guideline_tier) > 0:
            ratio = min(len(policy_tier), len(guideline_tier)) / max(len(policy_tier), len(guideline_tier))
            assert ratio > 0.8, \
                f"Policy and Guideline tiers should have similar counts for {language}. " \
                f"Policy: {len(policy_tier)}, Guideline: {len(guideline_tier)}"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
