"""Grades task 1."""
import pathlib
import subprocess

import pytest

from .common import lint, verbose


@verbose
def grade_lint():
    """
    Runs 'flake8' on the directory 'ceres_workshop/task_1'.
    """

    import ceres_workshop.task_1 as task_1

    task_1_path = pathlib.Path(task_1.__file__).parent
    errors = lint(task_1_path)
    assert not errors, f"Flake8 found {len(errors)} errors!"


@verbose
def grade_import_main():
    """
    Attempts to import ceres_workshop.task_1.main
    """
    import ceres_workshop.task_1.main


@verbose
def grade_clean_import():
    """
    Checks for a clean import of ceres_workshop.task_1.main

    In practice we just check that nothing is passed to stdout.
    """
    result = subprocess.run(
        ["python", "-c", "import ceres_workshop.task_1.main"],
        capture_output=True,
    )
    assert not result.stdout
