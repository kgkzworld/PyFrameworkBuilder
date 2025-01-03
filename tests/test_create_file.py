import os
import pytest
import sys

from pathlib import Path

libs_path = Path(__file__).parent.parent / 'libs'
project_path = Path(__file__).parent.parent
parent_path = Path(__file__).parent
sys.path.insert(0, str(libs_path))

if os.name == 'nt':
    temp_path = os.environ['TEMP']
else:
    temp_path = os.environ['HOME']

import create_file

@pytest.fixture
def setup():
    if os.path.exists(os.path.join(temp_path, 'test_file.txt')):
        os.remove(os.path.join(temp_path, 'test_file.txt'))

@pytest.mark.project_only
def test_create_file():
    create_file.create_file(temp_path, ['test_file.txt'])
    result = os.path.exists(os.path.join(temp_path, 'test_file.txt'))
    if os.path.exists(os.path.join(temp_path, 'test_file.txt')):
        os.remove(os.path.join(temp_path, 'test_file.txt'))
    assert result is True