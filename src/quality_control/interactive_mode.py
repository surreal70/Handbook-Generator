"""
Interactive mode for handling failed tests.

This module provides interactive functionality for presenting failed test details
to users and allowing them to make decisions about how to handle each failure.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

import logging
from typing import List, Dict, Optional
from enum import Enum

from .data_structures import FailedTest, Task


class UserDecision(Enum):
    """Enum representing user decisions for failed tests."""
    FIX_NOW = "fix_now"
    CREATE_TASK = "create_task"
    SKIP = "skip"
    VIEW_FULL_ERROR = "view_full_error"
    QUIT = "quit"


class InteractiveMode:
    """
    Interactive mode handler for failed tests.
    
    Presents failed test details to users and offers options for handling
    each failure. Tracks user decisions and creates tasks as needed.
    """
    
    def __init__(self):
        """Initialize the interactive mode handler."""
        self.logger = logging.getLogger(__name__)
        self.decisions: Dict[str, UserDecision] = {}
        self.created_tasks: List[Task] = []
    
    def present_failed_test(self, test: FailedTest, test_number: int, total_tests: int) -> None:
        """
        Present details of a failed test to the user.
        
        Args:
            test: FailedTest object with test details
            test_number: Current test number (1-indexed)
            total_tests: Total number of failed tests
        """
        print("\n" + "=" * 80)
        print(f"FAILED TEST {test_number}/{total_tests}")
        print("=" * 80)
        print(f"\nTest Name: {test.name}")
        print(f"File: {test.file_path}")
        print(f"Line: {test.line_number}")
        print(f"\nFailure Reason:")
        print("-" * 80)
        # Show first 500 characters of failure reason
        reason = test.failure_reason[:500]
        if len(test.failure_reason) > 500:
            reason += "\n... (truncated, use 'View full error' to see complete output)"
        print(reason)
        print("-" * 80)
    
    def get_user_choice(self) -> UserDecision:
        """
        Prompt user for their decision on how to handle the failed test.
        
        Returns:
            UserDecision enum value representing the user's choice
        """
        print("\nWhat would you like to do?")
        print("  1. Fix now - Get guidance on fixing this issue")
        print("  2. Create task - Save this as a task for later")
        print("  3. Skip - Continue to next failed test")
        print("  4. View full error - See complete error traceback")
        print("  5. Quit - Exit interactive mode")
        
        while True:
            try:
                choice = input("\nEnter your choice (1-5): ").strip()
                
                if choice == '1':
                    return UserDecision.FIX_NOW
                elif choice == '2':
                    return UserDecision.CREATE_TASK
                elif choice == '3':
                    return UserDecision.SKIP
                elif choice == '4':
                    return UserDecision.VIEW_FULL_ERROR
                elif choice == '5':
                    return UserDecision.QUIT
                else:
                    print("Invalid choice. Please enter a number between 1 and 5.")
            except (EOFError, KeyboardInterrupt):
                print("\n\nInteractive mode interrupted by user.")
                return UserDecision.QUIT
    
    def show_full_error(self, test: FailedTest) -> None:
        """
        Display the complete error traceback for a failed test.
        
        Args:
            test: FailedTest object with error details
        """
        print("\n" + "=" * 80)
        print("COMPLETE ERROR TRACEBACK")
        print("=" * 80)
        print(test.error_traceback)
        print("=" * 80)
    
    def provide_fix_guidance(self, test: FailedTest) -> None:
        """
        Provide guidance on fixing the failed test.
        
        Args:
            test: FailedTest object with test details
        """
        print("\n" + "=" * 80)
        print("FIX GUIDANCE")
        print("=" * 80)
        print(f"\nTest: {test.name}")
        print(f"Location: {test.file_path}:{test.line_number}")
        print("\nSuggested steps:")
        print("1. Open the test file in your editor")
        print("2. Navigate to the failing test")
        print("3. Review the failure reason and error traceback")
        print("4. Identify the root cause:")
        print("   - Is the test incorrect?")
        print("   - Is the implementation incorrect?")
        print("   - Is there a missing dependency or setup?")
        print("5. Make the necessary changes")
        print("6. Run the test again to verify the fix")
        print("\nCommand to run this specific test:")
        print(f"  python -m pytest {test.file_path}::{test.name} -v")
        print("=" * 80)
    
    def create_task_for_test(self, test: FailedTest) -> Task:
        """
        Create a task entry for a failed test.
        
        Args:
            test: FailedTest object to create task for
            
        Returns:
            Task object with test details
        """
        # Determine priority based on failure type
        priority = 'high'
        if 'skip' in test.failure_reason.lower() or 'xfail' in test.failure_reason.lower():
            priority = 'low'
        elif 'assert' in test.failure_reason.lower():
            priority = 'medium'
        
        # Create suggested fix based on failure reason
        suggested_fix = None
        if 'FileNotFoundError' in test.failure_reason:
            suggested_fix = "Create the missing file or check the file path"
        elif 'AssertionError' in test.failure_reason:
            suggested_fix = "Review the assertion and verify expected vs actual values"
        elif 'ImportError' in test.failure_reason or 'ModuleNotFoundError' in test.failure_reason:
            suggested_fix = "Install missing dependencies or check import paths"
        elif 'AttributeError' in test.failure_reason:
            suggested_fix = "Verify the object has the expected attribute or method"
        
        task = Task(
            test_name=test.name,
            description=f"Fix failing test: {test.name}",
            error_details=test.failure_reason,
            priority=priority,
            suggested_fix=suggested_fix
        )
        
        self.created_tasks.append(task)
        self.logger.info(f"Created task for test: {test.name}")
        
        print(f"\n✓ Task created for: {test.name}")
        print(f"  Priority: {priority}")
        if suggested_fix:
            print(f"  Suggested fix: {suggested_fix}")
        
        return task
    
    def handle_failed_test(self, test: FailedTest, test_number: int, total_tests: int) -> bool:
        """
        Handle a single failed test interactively.
        
        Presents the test details and processes user decisions until the user
        chooses to move on (skip, create task, or quit).
        
        Args:
            test: FailedTest object to handle
            test_number: Current test number (1-indexed)
            total_tests: Total number of failed tests
            
        Returns:
            True if should continue to next test, False if user wants to quit
        """
        self.present_failed_test(test, test_number, total_tests)
        
        while True:
            decision = self.get_user_choice()
            
            if decision == UserDecision.FIX_NOW:
                self.provide_fix_guidance(test)
                # After showing guidance, ask again what to do
                continue
            
            elif decision == UserDecision.CREATE_TASK:
                self.create_task_for_test(test)
                self.decisions[test.name] = decision
                return True  # Continue to next test
            
            elif decision == UserDecision.SKIP:
                self.decisions[test.name] = decision
                self.logger.info(f"Skipped test: {test.name}")
                return True  # Continue to next test
            
            elif decision == UserDecision.VIEW_FULL_ERROR:
                self.show_full_error(test)
                # After showing error, ask again what to do
                continue
            
            elif decision == UserDecision.QUIT:
                self.decisions[test.name] = decision
                self.logger.info("User quit interactive mode")
                return False  # Stop processing
    
    def process_failed_tests(self, failed_tests: List[FailedTest]) -> Dict[str, any]:
        """
        Process all failed tests interactively.
        
        Iterates through all failed tests, presenting each one to the user
        and collecting their decisions.
        
        Args:
            failed_tests: List of FailedTest objects to process
            
        Returns:
            Dictionary with summary of decisions and created tasks:
            {
                'decisions': Dict[str, UserDecision],
                'created_tasks': List[Task],
                'completed': bool  # True if all tests were processed
            }
        """
        if not failed_tests:
            print("\n✓ No failed tests to process.")
            return {
                'decisions': {},
                'created_tasks': [],
                'completed': True
            }
        
        print(f"\n{'=' * 80}")
        print(f"INTERACTIVE MODE: {len(failed_tests)} FAILED TEST(S)")
        print(f"{'=' * 80}")
        print("\nYou will be presented with each failed test and can decide how to handle it.")
        
        for i, test in enumerate(failed_tests, 1):
            should_continue = self.handle_failed_test(test, i, len(failed_tests))
            if not should_continue:
                print(f"\nInteractive mode ended. Processed {i} of {len(failed_tests)} tests.")
                return {
                    'decisions': self.decisions,
                    'created_tasks': self.created_tasks,
                    'completed': False
                }
        
        # All tests processed
        print(f"\n{'=' * 80}")
        print("INTERACTIVE MODE SUMMARY")
        print(f"{'=' * 80}")
        print(f"Total failed tests: {len(failed_tests)}")
        print(f"Tasks created: {len(self.created_tasks)}")
        print(f"Tests skipped: {sum(1 for d in self.decisions.values() if d == UserDecision.SKIP)}")
        print(f"{'=' * 80}\n")
        
        return {
            'decisions': self.decisions,
            'created_tasks': self.created_tasks,
            'completed': True
        }
    
    def save_tasks_to_file(self, output_path: str) -> None:
        """
        Save created tasks to a file.
        
        Args:
            output_path: Path where to save the tasks file
        """
        if not self.created_tasks:
            self.logger.info("No tasks to save")
            return
        
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write("# Failed Test Tasks\n\n")
                f.write(f"Generated: {self.created_tasks[0] if self.created_tasks else 'N/A'}\n\n")
                
                for i, task in enumerate(self.created_tasks, 1):
                    f.write(f"## Task {i}: {task.test_name}\n\n")
                    f.write(f"**Priority:** {task.priority}\n\n")
                    f.write(f"**Description:** {task.description}\n\n")
                    
                    if task.suggested_fix:
                        f.write(f"**Suggested Fix:** {task.suggested_fix}\n\n")
                    
                    f.write(f"**Error Details:**\n```\n{task.error_details}\n```\n\n")
                    f.write("---\n\n")
            
            self.logger.info(f"Tasks saved to: {output_path}")
            print(f"\n✓ Tasks saved to: {output_path}")
        
        except Exception as e:
            self.logger.error(f"Failed to save tasks: {e}")
            print(f"\n✗ Failed to save tasks: {e}")
