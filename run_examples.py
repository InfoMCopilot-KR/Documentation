#!/usr/bin/env python3
"""Demo runner for all examples."""

import sys


def run_all_demos():
    # Basic demo runner
    print("Running all demos...")

    # Import and run each module
    modules = [
        "financial_calculations",
        "data_processing_utils",
        "algorithms",
        "task_management",
        "validation_and_errors",
    ]

    for module_name in modules:
        try:
            print(f"\n--- {module_name} ---")
            module = __import__(module_name)
        except ImportError as e:
            print(f"Could not import {module_name}: {e}")


if __name__ == "__main__":
    run_all_demos()
