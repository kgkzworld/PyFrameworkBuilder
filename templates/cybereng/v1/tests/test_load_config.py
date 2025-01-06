"""
.DESCRIPTION
	This test will check if the config file exists and if it can be loaded

.NOTES
	[Original Author]
		o Michael Arroyo
	[Original Build Version]
		o 1.0.0.20250102 (Major.Minor.Patch.Date<YYYYMMDD>)
	[Latest Author]
		o Michael Arroyo
	[Latest Build Version]
		o 1.0.1.20250105 (Major.Minor.Patch.Date<YYYYMMDD>)
	[Comments]
		o
	[Python Compatibility / Tested On]
		o Python 3.13.1
	[Forked Project]
		o

.DEPENDENCIES
	o os # This library provides a way to work with the operating system
    o pytest # This library will provide a way to run tests
    o sys # This library provides access to some variables used or maintained by the interpreter
    o pathlib # This library will provide a way to work with file paths
    o load_config # This library will load the config.yaml file

.BUILD NOTES
	o 1.0.0.20250102
		[Michael Arroyo] Initial Post
	o 1.0.1.20250105
		[Michael Arroyo] Update the config file to use the default.yaml file
		[Michael Arroyo] Add loading of the config_file_path variable instead of the Project Path

.EXAMPLES
	Command: pytest test_load_config.py -v
	Description: This will run the test script with verbose output
	Notes:
	Output: test_load_config.py::test_load_config PASSED

    Command: pytest test_load_config.py -m project_only -v
    Description: With pytest run the test and only process tests with the project_only marker.
    Notes: These tests are developer defined tests.  Not mandatory before pushing to the repository
    Output: test_load_config.py::test_load_config PASSED

"""

import os # This library provides a way to work with the operating system
import sys # This library provides access to some variables used or maintained by the interpreter

from pathlib import Path # This library will provide a way to work with file paths

import pytest # This library will provide a way to run tests

libs_path = Path(__file__).parent.parent / 'libs'
project_path = Path(__file__).parent.parent
parent_path = Path(__file__).parent
sys.path.insert(0, str(libs_path))
config_file_path = Path(__file__).parent.parent / 'configs' / 'default.yaml'

import load_config # This library will load the config.yaml file

@pytest.mark.project_only
def test_config_exists():
    """
    This function will check if the config file exists
    """
    file_info = os.stat(config_file_path)
    assert file_info.st_size > 0

@pytest.mark.project_only
def test_load_config():
    """
    This function will check if the config file can be loaded
    """
    assert load_config.load_config(config_file_path) is not None