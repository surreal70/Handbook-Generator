"""
Base validator interface for quality control components.

This module defines the abstract base class that all validators must implement,
ensuring consistent interface across all quality control components.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

from abc import ABC, abstractmethod
from typing import Any
import logging


class BaseValidator(ABC):
    """
    Abstract base class for all quality control validators.
    
    All validators must implement the validate() and generate_report() methods
    to ensure consistent interface across the quality control system.
    """
    
    def __init__(self):
        """Initialize the validator with a logger."""
        self.logger = logging.getLogger(self.__class__.__name__)
    
    @abstractmethod
    def validate(self) -> Any:
        """
        Execute the validation logic.
        
        Returns:
            Validation result object specific to the validator type.
        """
        pass
    
    @abstractmethod
    def generate_report(self, result: Any) -> str:
        """
        Generate a human-readable report from validation results.
        
        Args:
            result: The validation result object.
            
        Returns:
            Formatted report as a string.
        """
        pass
