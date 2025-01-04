"""
.DESCRIPTION
	This test file will test the docstring parser library. It will test the following fields:

    - Description
    - Dependencies
    - Notes
    - Build Notes
    - Examples

    Each test is parameterized to test all python files in the project directory.

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
	o os # This library provides a way to work with the operating system
    o subprocess # This library will provide a way to run shell commands
    o sys # This library provides access to some variables used or maintained by the interpreter
    o pathlib # This library will provide a way to work with file paths
    o pytest # This library will provide a way to run tests
    o yaml # This library will provide a way to work with yaml files

.BUILD NOTES
	o 1.0.0.20250102
		[Michael Arroyo] Initial Post

.EXAMPLES
	Command: pytest test_docstring_parser.py -v
	Description: This will run the test script with verbose output
	Notes:
	Output: test_docstring_parser.py::test_docstring_parser PASSED

    Command: pytest test_docstring_parser.py -m project_only -v
    Description: With pytest run the test and only process tests with the gitpush marker.
    Notes: These tests are mandatory before pushing to the repository
    Output: test_docstring_parser.py::test_docstring_parser PASSED

"""

import os # This library provides a way to work with the operating system
import subprocess # This library will provide a way to run shell commands
import sys # This library provides access to some variables used or maintained by the interpreter

from pathlib import Path # This library will provide a way to work with file paths

import pytest # This library will provide a way to run tests
import yaml # This library will provide a way to work with yaml files

libs_path = Path(__file__).parent.parent / 'libs'
project_path = Path(__file__).parent.parent
parent_path = Path(__file__).parent
docstring_parser_path = Path(__file__).parent.parent / 'libs' / 'dynamic_help.py'
config_file_path = os.path.join(parent_path, 'test_docstring_parser.yaml')

with open(config_file_path, 'r') as stream:
    config = yaml.safe_load(stream)

exclude_list = config['exclude']

def process_parser(cmd):
    """
    This function will run the dynamic_help command and return the output
    """
    results = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=False)
    return results.stdout

def find_py_files(directory):
    """"
    This function will find all python files in the project directory
    """
    py_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                if file not in exclude_list:
                    py_files.append((os.path.join(root, file), True))
    return py_files

python_files = find_py_files(project_path)

@pytest.mark.gitpush
@pytest.mark.parametrize('cur_input, expected', python_files)
def test_docstring_description(cur_input, expected):
    """
    Parse the docstring for the description field
    """
    description_check = process_parser(f'python {docstring_parser_path} --module "{cur_input}" ')

    assert len(description_check) > 10

@pytest.mark.gitpush
@pytest.mark.parametrize('cur_input, expected', python_files)
def test_docstring_dependencies(cur_input, expected):
    """
    Parse the docstring for the dependencies field
    """
    dependencies_check = process_parser(f'python {docstring_parser_path} --module "{cur_input}" --dependencies')

    assert len(dependencies_check) > 10

@pytest.mark.gitpush
@pytest.mark.parametrize('cur_input, expected', python_files)
def test_docstring_notes(cur_input, expected):
    """
    Parse the docstring for the notes field
    """
    notes_check = process_parser(f'python {docstring_parser_path} --module "{cur_input}" --notes')

    assert len(notes_check) > 10

@pytest.mark.gitpush
@pytest.mark.parametrize('cur_input, expected', python_files)
def test_docstring_build_notes(cur_input, expected):
    """
    Parse the docstring for the build notes field
    """
    build_notes_check = process_parser(f'python {docstring_parser_path} --module "{cur_input}" --build_notes')

    assert len(build_notes_check) > 10

@pytest.mark.gitpush
@pytest.mark.parametrize('cur_input, expected', python_files)
def test_docstring_examples(cur_input, expected):
    """
    Parse the docstring for the examples field
    """
    examples_check = process_parser(f'python {docstring_parser_path} --module "{cur_input}" --examples')

    assert len(examples_check) > 10