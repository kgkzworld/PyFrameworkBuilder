"""
.DESCRIPTION
	This is a test script for the create_folder library

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
    o create_folder # This library will create the folders specified

.BUILD NOTES
	o 1.0.0.20250102
		[Michael Arroyo] Initial Post

.EXAMPLES
	Command: pytest test_create_folder.py
	Description: This will run the test script with verbose output
	Notes:
	Output: test_create_folder.py::test_create_folder PASSED

    Command: pytest test_create_folder.py -m project_only -v
    Description: With pytest run the test and only process tests with the project_only marker.
    Notes: These tests are developer defined tests.  Not mandatory before pushing to the repository
    Output: test_create_folder.py::test_create_folder PASSED
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

import create_folder # This library will create the folders specified

@pytest.fixture
def setup():
    """
    This function will setup the test directory
    """
    if os.path.exists(os.path.join(temp_path, 'pytest_folder')):
        os.rmdir(os.path.join(temp_path, 'pytest_folder'))

@pytest.mark.project_only
def test_create_folder():
    """
    This function will test the create_folder function
    """
    create_folder.create_folder(temp_path, ['pytest_folder'])
    result = os.path.exists(os.path.join(temp_path, 'pytest_folder'))
    if os.path.exists(os.path.join(temp_path, 'pytest_folder')):
        os.rmdir(os.path.join(temp_path, 'pytest_folder'))
    assert result is True