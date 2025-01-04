"""
.DESCRIPTION
	This test will check if the folders and files specified in the config.yaml file exist.

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
    o sys # This library provides access to some variables used or maintained by the interpreter
    o pathlib # This library will provide a way to work with file paths
    o pytest # This library will provide a way to run tests
    o yaml # This library will provide a way to work with yaml files

.BUILD NOTES
	o 1.0.0.20250102
		[Michael Arroyo] Initial Post

.EXAMPLES
	Command: pytest test_structure.py -v
	Description: This will run the test script with verbose output
	Notes:
	Output: test_structure.py::test_structure PASSED

    Command: pytest test_structure.py -m project_only -v
    Description: With pytest run the test and only process tests with the gitpush marker.
    Notes: These tests are mandatory before pushing to the repository
    Output: test_structure.py::test_structure PASSED
"""

import os # This library provides a way to work with the operating system
import sys # This library provides access to some variables used or maintained by the interpreter

from pathlib import Path # This library will provide a way to work with file paths

import pytest # This library will provide a way to run tests
import yaml # This library will provide a way to work with yaml files

project_path = Path(__file__).parent.parent
parent_path = Path(__file__).parent

config_file_path = parent_path / 'test_structure.yaml'
with open(config_file_path, 'r') as file:
    config = yaml.safe_load(file)

config_folders = []
for folder in config['content']['folders']:
    config_folders.append((folder, True))

config_files = []
for file in config['content']['files']:
    config_files.append((file, True))

def exists(path):
    """
    .DESCRIPTION
        This function will check if the specified path exists.

    .PARAMETERS
        path (str): The path to check.
    """
    return os.path.exists(os.path.join(project_path, path))

@pytest.mark.gitpush
@pytest.mark.parametrize('cur_input, expected', config_folders)
def test_folders(cur_input, expected):
    """
    .DESCRIPTION
        This test will check if the folders specified in the config.yaml file exist.

    .PARAMETERS
        cur_input (str): The folder to check.
        expected (bool): The expected result.
    """
    assert exists(cur_input) == expected

@pytest.mark.gitpush
@pytest.mark.parametrize('cur_input, expected', config_files)
def test_files(cur_input, expected):
    """
    .DESCRIPTION
        This test will check if the files specified in the config.yaml file exist.

    .PARAMETERS
        cur_input (str): The file to check.
        expected (bool): The expected result.
    """
    assert exists(cur_input) == expected