"""
.DESCRIPTION
	This is a test script for the create_file library

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
		o This is a project_only test
	[Python Compatibility / Tested On]
		o Python 3.13.1
	[Forked Project]
		o

.DEPENDENCIES
	o os # This library provides a way to work with the operating system
    o pytest # This library will provide a way to run tests
    o sys # This library provides access to some variables used or maintained by the interpreter
    o pathlib # This library will provide a way to work with file paths
    o create_file # This library will create the files specified

.BUILD NOTES
	o 1.0.0.20250102
		[Michael Arroyo] Initial Post

.EXAMPLES
	Command: pytest test_create_file.py -v
	Description: This will run the test script with verbose output
	Notes:
	Output: test_create_file.py::test_create_file PASSED

    Command: pytest test_create_file.py -m project_only -v
    Description: With pytest run the test and only process tests with the project_only marker.
    Notes: These tests are developer defined tests.  Not mandatory before pushing to the repository
    Output: test_create_file.py::test_create_file PASSED
"""

import os # This library provides a way to work with the operating system
from pathlib import Path # This library will provide a way to work with file paths
import sys # This library provides access to some variables used or maintained by the interpreter

import pytest # This library will provide a way to run tests


libs_path = Path(__file__).parent.parent / 'libs'
project_path = Path(__file__).parent.parent
parent_path = Path(__file__).parent
sys.path.insert(0, str(libs_path))

if os.name == 'nt':
    temp_path = os.environ['TEMP']
else:
    temp_path = os.environ['HOME']

import create_file # This library will create the files specified

@pytest.fixture
def setup():
    """
    This function will setup the test path
    """
    if os.path.exists(os.path.join(temp_path, 'test_file.txt')):
        os.remove(os.path.join(temp_path, 'test_file.txt'))

@pytest.mark.project_only
def test_create_file():
    """
    This function will test the create_file function
    """
    create_file.create_file(temp_path, ['test_file.txt'])
    result = os.path.exists(os.path.join(temp_path, 'test_file.txt'))
    if os.path.exists(os.path.join(temp_path, 'test_file.txt')):
        os.remove(os.path.join(temp_path, 'test_file.txt'))
    assert result is True