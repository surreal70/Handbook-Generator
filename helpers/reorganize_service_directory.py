#!/usr/bin/env python3
"""
Service Directory Reorganization Script

This script reorganizes service-related templates into a dedicated service-directory
structure for better organization and maintainability.

Reorganization:
- templates/de/email-service/ → templates/de/service-directory/email-service/
- templates/de/service-templates/ → templates/de/service-directory/service-templates/
- templates/en/service-templates/ → templates/en/service-directory/service-templates/
"""

import os
import shutil
import sys
from pathlib import Path
from typing import List, Tuple, Dict
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ServiceDirectoryReorganizer:
    """Handles reorganization of service templates into service-directory structure."""
    
    def __init__(self, templates_dir: str = "templates"):
        """
        Initialize the reorganizer.
        
        Args:
            templates_dir: Root templates directory path
        """
        self.templates_dir = Path(templates_dir)
        self.backup_dir = None
        self.moves_performed: List[Tuple[Path, Path]] = []
        
    def validate_environment(self) -> bool:
        """
        Validate that the environment is ready for reorganization.
        
        Returns:
            True if environment is valid, False otherwise
        """
        if not self.templates_dir.exists():
            logger.error(f"Templates directory not found: {self.templates_dir}")
            return False
            
        # Check if source directories exist
        de_email_service = self.templates_dir / "de" / "email-service"
        de_service_templates = self.templates_dir / "de" / "service-templates"
        en_service_templates = self.templates_dir / "en" / "service-templates"
        
        missing_dirs = []
        if not de_email_service.exists():
            missing_dirs.append(str(de_email_service))
        if not de_service_templates.exists():
            missing_dirs.append(str(de_service_templates))
        if not en_service_templates.exists():
            missing_dirs.append(str(en_service_templates))
            
        if missing_dirs:
            logger.warning(f"Some source directories not found: {missing_dirs}")
            logger.warning("Reorganization may be partially complete or not needed")
            
        return True
        
    def create_backup(self) -> bool:
        """
        Create a backup of the templates directory before reorganization.
        
        Returns:
            True if backup successful, False otherwise
        """
        try:
            backup_name = f"{self.templates_dir.name}.backup"
            self.backup_dir = self.templates_dir.parent / backup_name
            
            if self.backup_dir.exists():
                logger.info(f"Removing existing backup: {self.backup_dir}")
                shutil.rmtree(self.backup_dir)
                
            logger.info(f"Creating backup: {self.backup_dir}")
            shutil.copytree(self.templates_dir, self.backup_dir)
            logger.info("Backup created successfully")
            return True
            
        except Exception as e:
            logger.error(f"Failed to create backup: {e}")
            return False
            
    def create_service_directories(self) -> bool:
        """
        Create the new service-directory structure.
        
        Returns:
            True if directories created successfully, False otherwise
        """
        try:
            de_service_dir = self.templates_dir / "de" / "service-directory"
            en_service_dir = self.templates_dir / "en" / "service-directory"
            
            logger.info(f"Creating directory: {de_service_dir}")
            de_service_dir.mkdir(parents=True, exist_ok=True)
            
            logger.info(f"Creating directory: {en_service_dir}")
            en_service_dir.mkdir(parents=True, exist_ok=True)
            
            logger.info("Service directories created successfully")
            return True
            
        except Exception as e:
            logger.error(f"Failed to create service directories: {e}")
            return False
            
    def move_directory(self, source: Path, destination: Path) -> bool:
        """
        Safely move a directory from source to destination.
        
        Args:
            source: Source directory path
            destination: Destination directory path
            
        Returns:
            True if move successful, False otherwise
        """
        try:
            if not source.exists():
                logger.warning(f"Source directory does not exist: {source}")
                return True  # Not an error if already moved
                
            if destination.exists():
                logger.warning(f"Destination already exists: {destination}")
                logger.info(f"Removing existing destination: {destination}")
                shutil.rmtree(destination)
                
            logger.info(f"Moving: {source} → {destination}")
            shutil.move(str(source), str(destination))
            
            # Verify the move
            if not destination.exists():
                logger.error(f"Move verification failed: {destination} does not exist")
                return False
                
            # Count files to verify
            source_would_have = len(list(source.rglob("*"))) if source.exists() else 0
            dest_files = len(list(destination.rglob("*")))
            
            logger.info(f"Move successful: {dest_files} items in {destination}")
            self.moves_performed.append((source, destination))
            return True
            
        except Exception as e:
            logger.error(f"Failed to move {source} to {destination}: {e}")
            return False
            
    def perform_reorganization(self) -> bool:
        """
        Perform the actual reorganization of service directories.
        
        Returns:
            True if reorganization successful, False otherwise
        """
        moves = [
            # German directories
            (
                self.templates_dir / "de" / "email-service",
                self.templates_dir / "de" / "service-directory" / "email-service"
            ),
            (
                self.templates_dir / "de" / "service-templates",
                self.templates_dir / "de" / "service-directory" / "service-templates"
            ),
            # English directories
            (
                self.templates_dir / "en" / "service-templates",
                self.templates_dir / "en" / "service-directory" / "service-templates"
            ),
        ]
        
        for source, destination in moves:
            if not self.move_directory(source, destination):
                logger.error(f"Failed to move {source}")
                return False
                
        logger.info("All directories moved successfully")
        return True
        
    def verify_reorganization(self) -> bool:
        """
        Verify that the reorganization was successful.
        
        Returns:
            True if verification successful, False otherwise
        """
        try:
            # Check that new directories exist
            required_dirs = [
                self.templates_dir / "de" / "service-directory" / "email-service",
                self.templates_dir / "de" / "service-directory" / "service-templates",
                self.templates_dir / "en" / "service-directory" / "service-templates",
            ]
            
            for directory in required_dirs:
                if not directory.exists():
                    logger.error(f"Required directory missing: {directory}")
                    return False
                    
                # Check that directory has content
                files = list(directory.rglob("*"))
                if not files:
                    logger.warning(f"Directory is empty: {directory}")
                else:
                    logger.info(f"Verified: {directory} ({len(files)} items)")
                    
            # Check that old directories are gone
            old_dirs = [
                self.templates_dir / "de" / "email-service",
                self.templates_dir / "de" / "service-templates",
                self.templates_dir / "en" / "service-templates",
            ]
            
            for directory in old_dirs:
                if directory.exists():
                    logger.error(f"Old directory still exists: {directory}")
                    return False
                    
            logger.info("Verification successful: All directories in correct locations")
            return True
            
        except Exception as e:
            logger.error(f"Verification failed: {e}")
            return False
            
    def rollback(self) -> bool:
        """
        Rollback changes by restoring from backup.
        
        Returns:
            True if rollback successful, False otherwise
        """
        if not self.backup_dir or not self.backup_dir.exists():
            logger.error("No backup available for rollback")
            return False
            
        try:
            logger.info("Rolling back changes...")
            
            # Remove current templates directory
            if self.templates_dir.exists():
                shutil.rmtree(self.templates_dir)
                
            # Restore from backup
            shutil.copytree(self.backup_dir, self.templates_dir)
            
            logger.info("Rollback successful")
            return True
            
        except Exception as e:
            logger.error(f"Rollback failed: {e}")
            return False
            
    def cleanup_backup(self) -> None:
        """Remove the backup directory after successful reorganization."""
        if self.backup_dir and self.backup_dir.exists():
            try:
                logger.info(f"Removing backup: {self.backup_dir}")
                shutil.rmtree(self.backup_dir)
                logger.info("Backup removed")
            except Exception as e:
                logger.warning(f"Failed to remove backup: {e}")
                
    def generate_report(self) -> Dict:
        """
        Generate a report of the reorganization.
        
        Returns:
            Dictionary containing reorganization statistics
        """
        report = {
            "directories_moved": len(self.moves_performed),
            "moves": [
                {
                    "source": str(source),
                    "destination": str(dest)
                }
                for source, dest in self.moves_performed
            ]
        }
        return report
        
    def run(self, create_backup: bool = True, keep_backup: bool = False) -> bool:
        """
        Run the complete reorganization process.
        
        Args:
            create_backup: Whether to create a backup before reorganization
            keep_backup: Whether to keep the backup after successful reorganization
            
        Returns:
            True if reorganization successful, False otherwise
        """
        logger.info("Starting service directory reorganization...")
        
        # Step 1: Validate environment
        if not self.validate_environment():
            logger.error("Environment validation failed")
            return False
            
        # Step 2: Create backup
        if create_backup:
            if not self.create_backup():
                logger.error("Backup creation failed")
                return False
                
        # Step 3: Create service directories
        if not self.create_service_directories():
            logger.error("Failed to create service directories")
            if create_backup:
                self.rollback()
            return False
            
        # Step 4: Perform reorganization
        if not self.perform_reorganization():
            logger.error("Reorganization failed")
            if create_backup:
                self.rollback()
            return False
            
        # Step 5: Verify reorganization
        if not self.verify_reorganization():
            logger.error("Verification failed")
            if create_backup:
                self.rollback()
            return False
            
        # Step 6: Generate report
        report = self.generate_report()
        logger.info(f"Reorganization complete: {report['directories_moved']} directories moved")
        
        # Step 7: Cleanup backup if requested
        if create_backup and not keep_backup:
            self.cleanup_backup()
            
        logger.info("Service directory reorganization completed successfully!")
        return True


def main():
    """Main entry point for the script."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Reorganize service templates into service-directory structure"
    )
    parser.add_argument(
        "--templates-dir",
        default="templates",
        help="Root templates directory (default: templates)"
    )
    parser.add_argument(
        "--no-backup",
        action="store_true",
        help="Skip backup creation (not recommended)"
    )
    parser.add_argument(
        "--keep-backup",
        action="store_true",
        help="Keep backup after successful reorganization"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes"
    )
    
    args = parser.parse_args()
    
    if args.dry_run:
        logger.info("DRY RUN MODE - No changes will be made")
        logger.info(f"Would reorganize templates in: {args.templates_dir}")
        logger.info("Moves that would be performed:")
        logger.info("  templates/de/email-service/ → templates/de/service-directory/email-service/")
        logger.info("  templates/de/service-templates/ → templates/de/service-directory/service-templates/")
        logger.info("  templates/en/service-templates/ → templates/en/service-directory/service-templates/")
        return 0
        
    reorganizer = ServiceDirectoryReorganizer(args.templates_dir)
    success = reorganizer.run(
        create_backup=not args.no_backup,
        keep_backup=args.keep_backup
    )
    
    return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
