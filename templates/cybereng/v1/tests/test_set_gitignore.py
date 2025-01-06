"""
.DESCRIPTION
	This test will check if the .gitignore file exists and is not empty.

.NOTES
	[Original Author]
		o Michael Arroyo
	[Original Build Version]
		o 1.0.0.20250102 (Major.Minor.Patch.Date<YYYYMMDD>)
	[Latest Author]
		o Michael Arroyo
	[Latest Build Version]
		o 1.0.0.20250102 (Major.Minor.Patch.Date<YYYYMMDD>)
	[Comments]
		o
	[Python Compatibility / Tested On]
		o Python 3.13.1
	[Forked Project]
		o

.DEPENDENCIES
	o import os # This library provides a way to work with the operating system
    o pathlib # This library will provide a way to work with file paths
    o pytest # This library will provide a way to run tests

.BUILD NOTES
	o 1.0.0.20250102
		[Michael Arroyo] Initial Post

.EXAMPLES
	Command: pytest test_set_gitignore.py -v
	Description: This will run the test script with verbose output
	Notes:
	Output: test_set_gitignore.py::test_set_gitignore PASSED

    Command: pytest test_set_gitignore.py -m project_only -v
    Description: With pytest run the test and only process tests with the gitpush marker.
    Notes: These tests are mandatory before pushing to the repository
    Output: test_set_gitignore.py::test_set_gitignore PASSED
"""

import os # This library provides a way to work with the operating system
from pathlib import Path # This library will provide a way to work with file paths

import pytest # This library will provide a way to run tests

@pytest.mark.gitpush
def test_gitignore():
    """
    This test will check if the .gitignore file exists and is not empty.
    """
    file_path = Path(__file__).parent.parent / '.gitignore'
    file_info = os.stat(file_path)
    assert file_info.st_size > 0