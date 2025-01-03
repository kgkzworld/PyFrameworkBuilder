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

import create_folder

@pytest.fixture
def setup():
    if os.path.exists(os.path.join(temp_path, 'pytest_folder')):
        os.rmdir(os.path.join(temp_path, 'pytest_folder'))

@pytest.mark.project_only
def test_create_folder():
    create_folder.create_folder(temp_path, ['pytest_folder'])
    result = os.path.exists(os.path.join(temp_path, 'pytest_folder'))
    if os.path.exists(os.path.join(temp_path, 'pytest_folder')):
        os.rmdir(os.path.join(temp_path, 'pytest_folder'))
    assert result is True