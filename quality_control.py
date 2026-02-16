#!/usr/bin/env python3
"""
Quality Control System Entry Point

This script provides a convenient entry point for running the quality control system.
It can be executed directly from the project root.

Usage:
    python quality_control.py [options]
    
For help:
    python quality_control.py --help

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

from src.quality_control.cli import main

if __name__ == '__main__':
    main()
