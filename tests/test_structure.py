import os
import pytest
import sys
import yaml

from pathlib import Path

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
    return os.path.exists(os.path.join(project_path, path))

@pytest.mark.gitpush
@pytest.mark.parametrize('cur_input, expected', config_folders)
def test_folders(cur_input, expected):
    assert exists(cur_input) == expected

@pytest.mark.gitpush
@pytest.mark.parametrize('cur_input, expected', config_files)
def test_files(cur_input, expected):
    assert exists(cur_input) == expected