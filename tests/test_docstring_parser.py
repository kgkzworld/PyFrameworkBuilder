import os
import pytest
import subprocess
import sys
import yaml

from pathlib import Path

libs_path = Path(__file__).parent.parent / 'libs'
project_path = Path(__file__).parent.parent
parent_path = Path(__file__).parent
docstring_parser_path = Path(__file__).parent.parent / 'libs' / 'dynamic_help.py'
config_file_path = os.path.join(parent_path, 'test_function_docstring.yaml')

with open(config_file_path, 'r') as stream:
    config = yaml.safe_load(stream)

exclude_list = config['exclude']

def process_parser(cmd):
    """
    Run the dynamic_help command and return the output
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