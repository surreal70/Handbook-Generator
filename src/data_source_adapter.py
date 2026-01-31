"""
Data Source Adapter Interface for Handbook Generator

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

from abc import ABC, abstractmethod
from typing import Optional


class DataSourceAdapter(ABC):
    """
    Abstract base class for data source adapters.
    
    Data source adapters provide a unified interface for retrieving data
    from external systems (e.g., NetBox, databases, APIs).
    
    Implementations must handle:
    - Connection establishment and teardown
    - Field retrieval with proper error handling
    - Graceful handling of missing or invalid data
    """
    
    @abstractmethod
    def connect(self) -> bool:
        """
        Establish connection to the data source.
        
        Returns:
            True if connection successful, False otherwise
            
        Raises:
            ConnectionError: If connection cannot be established
            AuthenticationError: If authentication fails
        """
        pass
    
    @abstractmethod
    def get_field(self, field_path: str) -> Optional[str]:
        """
        Retrieve field value from data source.
        
        Args:
            field_path: Dot-separated path to the field (e.g., "device.name", "site_name")
            
        Returns:
            Field value as string, or None if field not found
            
        Raises:
            ConnectionError: If not connected to data source
            ValueError: If field_path is invalid
        """
        pass
    
    @abstractmethod
    def disconnect(self) -> None:
        """
        Close connection to data source and clean up resources.
        
        This method should be idempotent - calling it multiple times
        should not cause errors.
        """
        pass
    
    def __enter__(self):
        """Context manager entry - establish connection."""
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - close connection."""
        self.disconnect()
        return False
